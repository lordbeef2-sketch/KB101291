# NI DOCUMENT BUNDLE: rfmxcdma2k-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxcdma2k-c-api-ref start=251 end=392 -->
<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1ga58f484be8a91ecf6283e54ba6c8cf7d7.html language=enus -->
## TOPIC 00251: RFmxCDMA2k_CHPCfgAveraging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1ga58f484be8a91ecf6283e54ba6c8cf7d7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1ga58f484be8a91ecf6283e54ba6c8cf7d7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CHP measurement. Syntaxint32 __stdcall RFmxCDMA2k_CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxCDMA2k_CHPCfgAveraging

Configures averaging for the CHP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The CHP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the CHP measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The CHP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the CHP measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1gace3c968f84ce179dfd75e64e7035cd07.html language=enus -->
## TOPIC 00252: RFmxCDMA2k_CHPCfgRBWFilter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1gace3c968f84ce179dfd75e64e7035cd07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__chp_1gace3c968f84ce179dfd75e64e7035cd07.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxCDMA2k_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxCDMA2k_CHPCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxCDMA2k_CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW.The default value is True.Refer to the RBW and Sweep Time section in the CHP topic for more information about RBW and sweep time.Name (value)DescriptionFalse (0)The measurement uses the RBW that you specify in the RBW parameter.True (1)The measurement computes the RBW. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |  |
| True (1) | The measurement computes the RBW. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the RBW Auto parameter to False. This value is expressed in Hz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.Name (value)DescriptionFFT Based (0)No RBW filtering is performed.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | No RBW filtering is performed. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency.html language=enus -->
## TOPIC 00253: Frequency

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CfgFrequencyConfigures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. RFmxCDMA2k_CfgFrequencyChannelNumberConfigures the expected carrier frequency of the RF signal to acquire according to the

### Frequency

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CfgFrequency | Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. |
| RFmxCDMA2k_CfgFrequencyChannelNumber | Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency_1ga45acf6472394eae0b0510f2f0dcc0805.html language=enus -->
## TOPIC 00254: RFmxCDMA2k_CfgFrequencyChannelNumber

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency_1ga45acf6472394eae0b0510f2f0dcc0805.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency_1ga45acf6472394eae0b0510f2f0dcc0805.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxCDMA2k_CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 b

### RFmxCDMA2k_CfgFrequencyChannelNumber

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| linkDirection | [in] | int32 | This parameter specifies the direction for which the frequency is calculated. Currently only Uplink is supported.Name (value)DescriptionUplink (1)The frequency is calculated in the reverse link direction, also known as the uplink direction. |
| Name (value) | Description |  |  |
| Uplink (1) | The frequency is calculated in the reverse link direction, also known as the uplink direction. |  |  |
| bandClass | [in] | int32 | This parameter specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. The default value is 0.Name (value)Description0 (0)Specifies the 800 MHz cellular band.1 (1)Specifies the 1.8 GHz to 2.0 GHz PCS band.2 (2)Specifies the 872 MHz to 960 MHz TACS band.3 (3)Specifies the 832 MHz to 925 MHZ JTACS band.4 (4)Specifies the 1.75 GHz to 1.87 GHz Korean PCS band.5 (5)Specifies the 450 MHz NMT band.6 (6)Specifies the 2 GHz IMT-2000 band.7 (7)Specifies the upper 700 MHz PARMR band.8 (8)Specifies the 1,800 MHz to 2 GHz band.9 (9)Specifies the 900 MHz band.10 (10)Specifies the secondary 1,800 MHz band.11 (11)Specifies the 400 MHz European PAMR band.12 (12)Specifies the 800 MHz PAMR band.14 (14)Specifies the US PCS 1.9 GHz band.15 (15)Specifies the AWS band. |
| Name (value) | Description |  |  |
| 0 (0) | Specifies the 800 MHz cellular band. |  |  |
| 1 (1) | Specifies the 1.8 GHz to 2.0 GHz PCS band. |  |  |
| 2 (2) | Specifies the 872 MHz to 960 MHz TACS band. |  |  |
| 3 (3) | Specifies the 832 MHz to 925 MHZ JTACS band. |  |  |
| 4 (4) | Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. |  |  |
| 5 (5) | Specifies the 450 MHz NMT band. |  |  |
| 6 (6) | Specifies the 2 GHz IMT-2000 band. |  |  |
| 7 (7) | Specifies the upper 700 MHz PARMR band. |  |  |
| 8 (8) | Specifies the 1,800 MHz to 2 GHz band. |  |  |
| 9 (9) | Specifies the 900 MHz band. |  |  |
| 10 (10) | Specifies the secondary 1,800 MHz band. |  |  |
| 11 (11) | Specifies the 400 MHz European PAMR band. |  |  |
| 12 (12) | Specifies the 800 MHz PAMR band. |  |  |
| 14 (14) | Specifies the US PCS 1.9 GHz band. |  |  |
| 15 (15) | Specifies the AWS band. |  |  |
| channelNumber | [in] | int32 | This parameter specifies the channel number used to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency_1ga752d0c764c6c5f09daace4054f99cc8f.html language=enus -->
## TOPIC 00255: RFmxCDMA2k_CfgFrequency

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency_1ga752d0c764c6c5f09daace4054f99cc8f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__frequency_1ga752d0c764c6c5f09daace4054f99cc8f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. Syntaxint32 __stdcall RFmxCDMA2k_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)ParametersNameDirectionTypeDescriptioninstrumentHandle[

### RFmxCDMA2k_CfgFrequency

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| centerFrequency | [in] | float64 | This parameter specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. The default value of this parameter is hardware dependent. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Frequency

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__modacc.html language=enus -->
## TOPIC 00256: ModAcc

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__modacc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_ModAccCfgSynchronizationModeAndIntervalConfigures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis. AttachmentsNone

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval | Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__modacc_1ga4a4c6577bb5e32c094eb1e3230c36f88.html language=enus -->
## TOPIC 00257: RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__modacc_1ga4a4c6577bb5e32c094eb1e3230c36f88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__modacc_1ga4a4c6577bb5e32c094eb1e3230c36f88.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis. Syntaxint32 __stdcall RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurement

### RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval

Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame, slot, or symbol boundary.The default value is Slot.Name (value)DescriptionFrame (0)The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary.Slot (1)The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the slot boundary.Arbitrary (2)The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. |
| Name (value) | Description |  |  |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. |  |  |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |  |  |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. |  |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the modulation accuracy measurement. This value is expressed in slots. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw.html language=enus -->
## TOPIC 00258: OBW

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_OBWCfgAveragingConfigures averaging for the OBW measurement. RFmxCDMA2k_OBWCfgRBWFilterConfigures the RBW filter. RFmxCDMA2k_OBWCfgSweepTimeConfigures the sweep time. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_OBWCfgAveraging | Configures averaging for the OBW measurement. |
| RFmxCDMA2k_OBWCfgRBWFilter | Configures the RBW filter. |
| RFmxCDMA2k_OBWCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1ga0af60268916e334f1525a02404bf6404.html language=enus -->
## TOPIC 00259: RFmxCDMA2k_OBWCfgAveraging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1ga0af60268916e334f1525a02404bf6404.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1ga0af60268916e334f1525a02404bf6404.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the OBW measurement. Syntaxint32 __stdcall RFmxCDMA2k_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxCDMA2k_OBWCfgAveraging

Configures averaging for the OBW measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The OBW measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the OBW measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The OBW measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the OBW measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1ga6847926b9860091648b160fa4533e891.html language=enus -->
## TOPIC 00260: RFmxCDMA2k_OBWCfgRBWFilter

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1ga6847926b9860091648b160fa4533e891.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1ga6847926b9860091648b160fa4533e891.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. Syntaxint32 __stdcall RFmxCDMA2k_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session

### RFmxCDMA2k_OBWCfgRBWFilter

Configures the RBW filter.

#### Syntax

int32 __stdcall RFmxCDMA2k_OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| rbwAuto | [in] | int32 | This parameter specifies whether the measurement computes the RBW.The default value is True.Name (value)DescriptionFalse (0)The measurement uses the RBW that you specify in the RBW parameter.True (1)The measurement computes the RBW. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |  |  |
| True (1) | The measurement computes the RBW. |  |  |
| rbw | [in] | float64 | This parameter specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 30 kHz. |
| rbwFilterType | [in] | int32 | This parameter specifies the shape of the digital RBW filter. The default value is Gaussian.Name (value)DescriptionFFT Based (0)No RBW filtering is performed.Gaussian (1)An RBW filter with a Gaussian response is applied.Flat (2)An RBW filter with a flat response is applied. |
| Name (value) | Description |  |  |
| FFT Based (0) | No RBW filtering is performed. |  |  |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |  |  |
| Flat (2) | An RBW filter with a flat response is applied. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1gafb40c6f2ff177520f0e37a4c5986f931.html language=enus -->
## TOPIC 00261: RFmxCDMA2k_OBWCfgSweepTime

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1gafb40c6f2ff177520f0e37a4c5986f931.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__obw_1gafb40c6f2ff177520f0e37a4c5986f931.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxCDMA2k_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxCDMA2k_OBWCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxCDMA2k_OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 0.001667 seconds. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm.html language=enus -->
## TOPIC 00262: QEVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_QEVMCfgAveragingConfigures averaging for QEVM measurement. RFmxCDMA2k_QEVMCfgMeasurementLengthConfigures the number of chips used for a single QEVM measurement iteration. AttachmentsNone

### QEVM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_QEVMCfgAveraging | Configures averaging for QEVM measurement. |
| RFmxCDMA2k_QEVMCfgMeasurementLength | Configures the number of chips used for a single QEVM measurement iteration. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm_1ga1b884976c9f23f5733674380dcec70bd.html language=enus -->
## TOPIC 00263: RFmxCDMA2k_QEVMCfgAveraging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm_1ga1b884976c9f23f5733674380dcec70bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm_1ga1b884976c9f23f5733674380dcec70bd.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for QEVM measurement. Syntaxint32 __stdcall RFmxCDMA2k_QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxCDMA2k_QEVMCfgAveraging

Configures averaging for QEVM measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The QEVM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the QEVM measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The QEVM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the QEVM measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm_1ga302d3e60dbc90eda074b10e2f5d64d9b.html language=enus -->
## TOPIC 00264: RFmxCDMA2k_QEVMCfgMeasurementLength

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm_1ga302d3e60dbc90eda074b10e2f5d64d9b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__qevm_1ga302d3e60dbc90eda074b10e2f5d64d9b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of chips used for a single QEVM measurement iteration. Syntaxint32 __stdcall RFmxCDMA2k_QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis pa

### RFmxCDMA2k_QEVMCfgMeasurementLength

Configures the number of chips used for a single QEVM measurement iteration.

#### Syntax

int32 __stdcall RFmxCDMA2k_QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| measurementLength | [in] | int32 | This parameter specifies the number of chips used for a single measurement. The default value is 1536. The valid values range from 700 to 2500, inclusive. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem.html language=enus -->
## TOPIC 00265: SEM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SEMCfgAveragingConfigures averaging for the SEM measurement. RFmxCDMA2k_SEMCfgSweepTimeConfigures the sweep time. AttachmentsNone

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SEMCfgAveraging | Configures averaging for the SEM measurement. |
| RFmxCDMA2k_SEMCfgSweepTime | Configures the sweep time. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem_1ga0df5447dc18fd9281ff8c3a6579e7da2.html language=enus -->
## TOPIC 00266: RFmxCDMA2k_SEMCfgSweepTime

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem_1ga0df5447dc18fd9281ff8c3a6579e7da2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem_1ga0df5447dc18fd9281ff8c3a6579e7da2.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. Syntaxint32 __stdcall RFmxCDMA2k_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session r

### RFmxCDMA2k_SEMCfgSweepTime

Configures the sweep time.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| sweepTimeAuto | [in] | int32 | This parameter specifies whether the measurement computes the sweep time. The default value is True.Name (value)DescriptionFalse (0)The measurement uses the sweep time that you specify using the Sweep Time Interval parameter.True (1)The measurement uses the default sweep time of 0.001667 seconds. |
| Name (value) | Description |  |  |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |  |  |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |  |  |
| sweepTimeInterval | [in] | float64 | This parameter specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem_1ga630e12c9e16f182bd9cf21bc330a9540.html language=enus -->
## TOPIC 00267: RFmxCDMA2k_SEMCfgAveraging

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem_1ga630e12c9e16f182bd9cf21bc330a9540.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__sem_1ga630e12c9e16f182bd9cf21bc330a9540.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. Syntaxint32 __stdcall RFmxCDMA2k_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis

### RFmxCDMA2k_SEMCfgAveraging

Configures averaging for the SEM measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| averagingEnabled | [in] | int32 | This parameter specifies whether to enable averaging for the measurement. The default value is False.Name (value)DescriptionFalse (0)The measurement is performed on a single acquisition.True (1)The SEM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the SEM measurement is averaged. |
| Name (value) | Description |  |  |
| False (0) | The measurement is performed on a single acquisition. |  |  |
| True (1) | The SEM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the SEM measurement is averaged. |  |  |
| averagingCount | [in] | int32 | This parameter specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. |
| averagingType | [in] | int32 | This parameter specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement.The default value is RMS.Name (value)DescriptionRMS (0)The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor.Log (1)The power spectrum is averaged in a logarithmic scale.Scalar (2)The square root of the power spectrum is averaged.Max (3)The peak power in the spectrum at each frequency bin is retained from one acquisition to the next.Min (4)The least power in the spectrum at each frequency bin is retained from one acquisition to the next.Refer to the Averaging section of the Spectrum topic for more information about averaging types. |
| Name (value) | Description |  |  |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |  |  |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |  |  |
| Scalar (2) | The square root of the power spectrum is averaged. |  |  |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotphase.html language=enus -->
## TOPIC 00268: SlotPhase

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotphase.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndIntervalConfigures the Synchronization Mode, Measurement Offset, and Measurement Length parameters of the SlotPhase measurement. AttachmentsNone

### SlotPhase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval | Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters of the SlotPhase measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotphase_1ga17c0a24f4e951ed9f97fa720c35067fc.html language=enus -->
## TOPIC 00269: RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotphase_1ga17c0a24f4e951ed9f97fa720c35067fc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotphase_1ga17c0a24f4e951ed9f97fa720c35067fc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters of the SlotPhase measurement. Syntaxint32 __stdcall RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurement

### RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval

Configures the **Synchronization Mode**, **Measurement Offset**, and **Measurement Length** parameters of the SlotPhase measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame or slot boundary.The default value is Slot.Name (value)DescriptionFrame (0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary.Slot (1)The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |
| Name (value) | Description |  |  |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. |  |  |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |  |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of the SlotPhase measurement. This value is expressed in slots. The default value is 16. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotpower.html language=enus -->
## TOPIC 00270: SlotPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotpower.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SlotPowerCfgSynchronizationModeAndIntervalConfigures the Synchronization Mode, Measurement Offset, and Measurement Length parameters for the SlotPower measurement. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval | Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters for the SlotPower measurement. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotpower_1gabfd8e28c63b4b9e0db7998736995c1da.html language=enus -->
## TOPIC 00271: RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotpower_1gabfd8e28c63b4b9e0db7998736995c1da.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__slotpower_1gabfd8e28c63b4b9e0db7998736995c1da.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters for the SlotPower measurement. Syntaxint32 __stdcall RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measuremen

### RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval

Configures the **Synchronization Mode**, **Measurement Offset**, and **Measurement Length** parameters for the SlotPower measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| synchronizationMode | [in] | int32 | This parameter specifies whether the measurement is performed from the frame or slot boundary.The default value is Slot.Name (value)DescriptionFrame (0)The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary.Slot (1)The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |
| Name (value) | Description |  |  |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. |  |  |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |  |  |
| measurementOffset | [in] | int32 | This parameter specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the Synchronization Mode parameter. This value is expressed in slots. The default value is 0. |
| measurementLength | [in] | int32 | This parameter specifies the duration of SlotPower measurement. This value is expressed in slots. The default value is 16. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger.html language=enus -->
## TOPIC 00272: Trigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CfgDigitalEdgeTriggerConfigures the device to wait for a digital edge trigger and then marks a reference point within the record. RFmxCDMA2k_CfgIQPowerEdgeTriggerConfigures the device to wait for the complex power of the I/Q data to cross the specifie

### Trigger

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CfgDigitalEdgeTrigger | Configures the device to wait for a digital edge trigger and then marks a reference point within the record. |
| RFmxCDMA2k_CfgIQPowerEdgeTrigger | Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. |
| RFmxCDMA2k_CfgSoftwareEdgeTrigger | Configures the device to wait for a software trigger and then marks a reference point within the record. |
| RFmxCDMA2k_DisableTrigger | Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. |

#### Attachments

None

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga0afb6aa23618f10480337f9938da4b92.html language=enus -->
## TOPIC 00273: RFmxCDMA2k_CfgDigitalEdgeTrigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga0afb6aa23618f10480337f9938da4b92.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga0afb6aa23618f10480337f9938da4b92.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxCDMA2k_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enab

### RFmxCDMA2k_CfgDigitalEdgeTrigger

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| digitalEdgeSource | [in] | char[] | This parameter specifies the source terminal for the digital edge trigger. The default value of this parameter is hardware dependent.Name (value)DescriptionPFI0 (PFI0)The trigger is received on PFI 0.PFI1 (PFI1)The trigger is received on PFI 1.PXI_Trig0 (PXI_Trig0)The trigger is received on PXI trigger line 0.PXI_Trig1 (PXI_Trig1)The trigger is received on PXI trigger line 1.PXI_Trig2 (PXI_Trig2)The trigger is received on PXI trigger line 2.PXI_Trig3 (PXI_Trig3)The trigger is received on PXI trigger line 3.PXI_Trig4 (PXI_Trig4)The trigger is received on PXI trigger line 4.PXI_Trig5 (PXI_Trig5)The trigger is received on PXI trigger line 5.PXI_Trig6 (PXI_Trig6)The trigger is received on PXI trigger line 6.PXI_Trig7 (PXI_Trig7)The trigger is received on PXI trigger line 7.PXI_STAR (PXI_STAR)The trigger is received on the PXI star trigger line. |
| Name (value) | Description |  |  |
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
| digitalEdge | [in] | int32 | This parameter specifies the trigger edge to detect. The default value is Rising Edge.Name (value)DescriptionRising Edge (0)The trigger asserts on the rising edge of the signal.Falling Edge (1)The trigger asserts on the falling edge of the signal. |
| Name (value) | Description |  |  |
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |  |  |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |  |  |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga10c0ffdf99b633811149d41829f3e4cb.html language=enus -->
## TOPIC 00274: RFmxCDMA2k_DisableTrigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga10c0ffdf99b633811149d41829f3e4cb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga10c0ffdf99b633811149d41829f3e4cb.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate. Syntaxint32 __stdcall RFmxCDMA2k_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrum

### RFmxCDMA2k_DisableTrigger

Configures the device to not wait for a trigger to mark a reference point within a record. This function defines the signal triggering as immediate.

#### Syntax

int32 __stdcall RFmxCDMA2k_DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga41a22bf9a37faceed4dd3d1e7f339589.html language=enus -->
## TOPIC 00275: RFmxCDMA2k_CfgIQPowerEdgeTrigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga41a22bf9a37faceed4dd3d1e7f339589.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga41a22bf9a37faceed4dd3d1e7f339589.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. Syntaxint32 __stdcall RFmxCDMA2k_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerE

### RFmxCDMA2k_CfgIQPowerEdgeTrigger

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)

#### Remarks

To trigger on burst signals, specify a minimum quiet time. The minimum quiet time ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| iqPowerEdgeSource | [in] | char[] | This parameter specifies the channel from which the device monitors the trigger. The default value of this parameter is hardware dependent. |
| iqPowerEdgeSlope | [in] | int32 | This parameter specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope.Name (value)DescriptionRising Slope (0)The trigger asserts when the signal power is rising.Falling Slope (1)The trigger asserts when the signal power is falling. |
| Name (value) | Description |  |  |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |  |  |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |  |  |
| iqPowerEdgeLevel | [in] | float64 | This parameter specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this attribute is hardware dependent. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| minimumQuietTimeMode | [in] | int32 | This parameter specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto.Name (value)DescriptionManual (0)The minimum quiet time for triggering is the value you specify using the Minimum Quiet Time input.Auto (1)The measurement computes the minimum quiet time used for triggering. |
| Name (value) | Description |  |  |
| Manual (0) | The minimum quiet time for triggering is the value you specify using the Minimum Quiet Time input. |  |  |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |  |  |
| minimumQuietTime | [in] | float64 | This parameter specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet while it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default value of this parameter is hardware dependent. |
| iqPowerEdgeLevelType | [in] | int32 | This parameter specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type attribute to IQ Power Edge.Name (value)DescriptionRelative (0)The IQ Power Edge Level attribute is relative to the value of the reference level attribute.Absolute (1)The IQ Power Edge Level attribute specifies the absolute power. |
| Name (value) | Description |  |  |
| Relative (0) | The IQ Power Edge Level attribute is relative to the value of the reference level attribute. |  |  |
| Absolute (1) | The IQ Power Edge Level attribute specifies the absolute power. |  |  |
| enableTrigger | [in] | int32 | This parameter specifies whether the trigger is used. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga7460caeb88c2e4f2507a2d4b19bfbcc3.html language=enus -->
## TOPIC 00276: RFmxCDMA2k_CfgSoftwareEdgeTrigger

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga7460caeb88c2e4f2507a2d4b19bfbcc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__configuration__trigger_1ga7460caeb88c2e4f2507a2d4b19bfbcc3.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. Syntaxint32 __stdcall RFmxCDMA2k_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)ParametersNameDirectionTypeDescription

### RFmxCDMA2k_CfgSoftwareEdgeTrigger

Configures the device to wait for a software trigger and then marks a reference point within the record.

#### Syntax

int32 __stdcall RFmxCDMA2k_CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| triggerDelay | [in] | float64 | This parameter specifies the trigger delay time. This value is expressed in seconds. The default value is 0. |
| enableTrigger | [in] | int32 | This parameter specifies whether to enable the trigger. The default value is TRUE. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Trigger

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch.html language=enus -->
## TOPIC 00277: Fetch

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch.html
- document_id: `rfmxcdma2k-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp.html language=enus -->
## TOPIC 00278: ACP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_ACPFetchAbsolutePowersTraceFetches the absolute powers trace for the ACP measurement. RFmxCDMA2k_ACPFetchCarrierAbsolutePowerReturns the absolute carrier power. RFmxCDMA2k_ACPFetchOffsetMeasurementReturns the absolute and relative powers measured in t

### ACP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_ACPFetchAbsolutePowersTrace | Fetches the absolute powers trace for the ACP measurement. |
| RFmxCDMA2k_ACPFetchCarrierAbsolutePower | Returns the absolute carrier power. |
| RFmxCDMA2k_ACPFetchOffsetMeasurement | Returns the absolute and relative powers measured in the specified offset channel. The relative powers are measured relative to the carrier absolute power. |
| RFmxCDMA2k_ACPFetchOffsetMeasurementArray | Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power. |
| RFmxCDMA2k_ACPFetchRelativePowersTrace | Fetches the relative powers trace for the ACP measurement. |
| RFmxCDMA2k_ACPFetchSpectrum | Fetches the spectrum used for the ACP measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga0161c224304b04f2ea9c6ffb74ce2df5.html language=enus -->
## TOPIC 00279: RFmxCDMA2k_ACPFetchCarrierAbsolutePower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga0161c224304b04f2ea9c6ffb74ce2df5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga0161c224304b04f2ea9c6ffb74ce2df5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power. Syntaxint32 __stdcall RFmxCDMA2k_ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specif

### RFmxCDMA2k_ACPFetchCarrierAbsolutePower

Returns the absolute carrier power.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsolutePower | [out] | float64 * | This parameter returns the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga7499e3dde717941aef64deae55c5904a.html language=enus -->
## TOPIC 00280: RFmxCDMA2k_ACPFetchSpectrum

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga7499e3dde717941aef64deae55c5904a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga7499e3dde717941aef64deae55c5904a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the ACP measurement. Syntaxint32 __stdcall RFmxCDMA2k_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptio

### RFmxCDMA2k_ACPFetchSpectrum

Fetches the spectrum used for the ACP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga78a7e082a75753c3052090eb827373e1.html language=enus -->
## TOPIC 00281: RFmxCDMA2k_ACPFetchOffsetMeasurement

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga78a7e082a75753c3052090eb827373e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga78a7e082a75753c3052090eb827373e1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the specified offset channel. The relative powers are measured relative to the carrier absolute power. Syntaxint32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *

### RFmxCDMA2k_ACPFetchOffsetMeasurement

Returns the absolute and relative powers measured in the specified offset channel. The relative powers are measured relative to the carrier absolute power.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *lowerRelativePower, float64 *upperRelativePower, float64 *lowerAbsolutePower, float64 *upperAbsolutePower)

#### Remarks

Use "offset<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxCDMA2k_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64 * | This parameter returns the lower offset channel power measured relative to the carrier absolute power. This value is expressed in dB. |
| upperRelativePower | [out] | float64 * | This parameter returns the upper offset channel power measured relative to the carrier absolute power. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64 * | This parameter returns the lower offset channel absolute power. |
| upperAbsolutePower | [out] | float64 * | This parameter returns the upper offset channel absolute power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga7a94769980a8183dfdff35c1594219b4.html language=enus -->
## TOPIC 00282: RFmxCDMA2k_ACPFetchAbsolutePowersTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga7a94769980a8183dfdff35c1594219b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga7a94769980a8183dfdff35c1594219b4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the ACP measurement. Syntaxint32 __stdcall RFmxCDMA2k_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actua

### RFmxCDMA2k_ACPFetchAbsolutePowersTrace

Fetches the absolute powers trace for the ACP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 absolutePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| absolutePowersTrace | [out] | float32[] | This parameter returns the averaged absolute power at each frequency bin. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga8301edf1bee10515e3651f9c4c283808.html language=enus -->
## TOPIC 00283: RFmxCDMA2k_ACPFetchRelativePowersTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga8301edf1bee10515e3651f9c4c283808.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga8301edf1bee10515e3651f9c4c283808.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for the ACP measurement. Syntaxint32 __stdcall RFmxCDMA2k_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actua

### RFmxCDMA2k_ACPFetchRelativePowersTrace

Fetches the relative powers trace for the ACP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64 *x0, float64 *dx, float32 relativePowersTrace[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| traceIndex | [in] | int32 | Specifies the index of the trace to fetch. The traceIndex can range from 0 to (Number of carriers + 2*Number of offsets). |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| relativePowersTrace | [out] | float32[] | This parameter returns the averaged relative power at each frequency bin relative to absolute carrier power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga8dc5c11a60398e23f504236c65ac7f31.html language=enus -->
## TOPIC 00284: RFmxCDMA2k_ACPFetchOffsetMeasurementArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga8dc5c11a60398e23f504236c65ac7f31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__acp_1ga8dc5c11a60398e23f504236c65ac7f31.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power. Syntaxint32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerR

### RFmxCDMA2k_ACPFetchOffsetMeasurementArray

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power.

#### Syntax

int32 __stdcall RFmxCDMA2k_ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| lowerRelativePower | [out] | float64[] | This parameter returns the array of lower offset channel powers measured relative to the carrier absolute power. This value is expressed in dB. |
| upperRelativePower | [out] | float64[] | This parameter returns the array of upper offset channel powers measured relative to the carrier absolute power. This value is expressed in dB. |
| lowerAbsolutePower | [out] | float64[] | This parameter returns the array of lower offset channel absolute powers. |
| upperAbsolutePower | [out] | float64[] | This parameter returns the array of upper offset channel absolute powers. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda.html language=enus -->
## TOPIC 00285: CDA

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CDAFetchCodeDomainIAndQPowerReturns the I and Q mean active powers, and I and Q peak inactive powers. RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTraceReturns the I and Q code power trace measured in the code domain of the base spreading factor. RFmxCDMA2k

### CDA

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CDAFetchCodeDomainIAndQPower | Returns the I and Q mean active powers, and I and Q peak inactive powers. |
| RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace | Returns the I and Q code power trace measured in the code domain of the base spreading factor. |
| RFmxCDMA2k_CDAFetchCodeDomainPower | Returns the scalar code domain power results. |
| RFmxCDMA2k_CDAFetchIQImpairments | Returns the measured I/Q impairments. |
| RFmxCDMA2k_CDAFetchSymbolConstellationTrace | Returns the symbol constellation trace of the configured measurement channel. |
| RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit | Returns the symbol constellation trace of the configured measurement channel. |
| RFmxCDMA2k_CDAFetchSymbolEVM | Returns the modulation accuracy related measures for the configured measurement channel. |
| RFmxCDMA2k_CDAFetchSymbolEVMTrace | Returns the symbol EVM trace of the configured measurement channel. |
| RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace | Returns the symbol magnitude error trace of the configured measurement channel. |
| RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace | Returns the symbol phase error trace of the configured measurement channel. |
| RFmxCDMA2k_CDAFetchSymbolPowerTrace | Returns the symbol power trace of the configured measurement channel. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga083f8242ed91d10d2ec9ed05c0449f9c.html language=enus -->
## TOPIC 00286: RFmxCDMA2k_CDAFetchSymbolEVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga083f8242ed91d10d2ec9ed05c0449f9c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga083f8242ed91d10d2ec9ed05c0449f9c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation accuracy related measures for the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsSymbolEVM, float64 *peakSymbolEVM, float64 *rmsSymbolMagnitudeError, flo

### RFmxCDMA2k_CDAFetchSymbolEVM

Returns the modulation accuracy related measures for the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsSymbolEVM, float64 *peakSymbolEVM, float64 *rmsSymbolMagnitudeError, float64 *rmsSymbolPhaseError, float64 *meanSymbolPower, float64 *frequencyError, float64 *chipRateError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsSymbolEVM | [out] | float64 * | This parameter returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| peakSymbolEVM | [out] | float64 * | This parameter returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. |
| rmsSymbolMagnitudeError | [out] | float64 * | This parameter returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. |
| rmsSymbolPhaseError | [out] | float64 * | This parameter returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. |
| meanSymbolPower | [out] | float64 * | This parameter returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dB, and in dBm, when you set the CDA Pwr Unit attribute to dBm. |
| frequencyError | [out] | float64 * | This parameter returns the frequency error. This value is expressed in Hz. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error. This value is expressed in parts per million (ppm). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga2ec8ba48d402ba735cece8d6220fe096.html language=enus -->
## TOPIC 00287: RFmxCDMA2k_CDAFetchSymbolPowerTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga2ec8ba48d402ba735cece8d6220fe096.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga2ec8ba48d402ba735cece8d6220fe096.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol power trace of the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescr

### RFmxCDMA2k_CDAFetchSymbolPowerTrace

Returns the symbol power trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolPowers | [out] | float32[] | This parameter returns the array of symbol power of the configured measurement channel. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga318d157a18ceeb7da2ae7117617c0316.html language=enus -->
## TOPIC 00288: RFmxCDMA2k_CDAFetchSymbolConstellationTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga318d157a18ceeb7da2ae7117617c0316.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga318d157a18ceeb7da2ae7117617c0316.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol constellation trace of the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32 *actualArraySize)P

### RFmxCDMA2k_CDAFetchSymbolConstellationTrace

Returns the symbol constellation trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolConstellation | [out] | NIComplexSingle[] | This parameter returns the array of symbol constellation points of the configured measurement channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga3374fdca70b50bb020900d4501f867d0.html language=enus -->
## TOPIC 00289: RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga3374fdca70b50bb020900d4501f867d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga3374fdca70b50bb020900d4501f867d0.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol phase error trace of the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameDir

### RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace

Returns the symbol phase error trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolPhaseError | [out] | float32[] | This parameter returns the array of symbol phase error values of the configured measurement channel. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga5bcf706575eff8171c4f592e1d2eba37.html language=enus -->
## TOPIC 00290: RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga5bcf706575eff8171c4f592e1d2eba37.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga5bcf706575eff8171c4f592e1d2eba37.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol constellation trace of the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 array

### RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit

Returns the symbol constellation trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolConstellationI | [out] | float32[] | This parameter Returns the real part of array of symbol constellation points of the configured measurement channel. |
| symbolConstellationQ | [out] | float32[] | This parameter Returns the imaginary part of array of symbol constellation points of the configured measurement channel. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga60781416c2f7d94a621928609aba22d3.html language=enus -->
## TOPIC 00291: RFmxCDMA2k_CDAFetchIQImpairments

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga60781416c2f7d94a621928609aba22d3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga60781416c2f7d94a621928609aba22d3.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured I/Q impairments. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)ParametersNameDirectionTypeDescriptioninstrumentHandl

### RFmxCDMA2k_CDAFetchIQImpairments

Returns the measured I/Q impairments.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset of the composite signal. This value is expressed in dB. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance of the composite signal. This value is expressed in dB. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error of the composite signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga878360133299a93ec28825ac9ec5a838.html language=enus -->
## TOPIC 00292: RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga878360133299a93ec28825ac9ec5a838.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga878360133299a93ec28825ac9ec5a838.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol magnitude error trace of the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)Param

### RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace

Returns the symbol magnitude error trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolMagnitudeError | [out] | float32[] | This parameter returns the trace of the symbol magnitude errors of the corrected composite signal. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga8bbbb68f27f15c6e2840c679f7a835ed.html language=enus -->
## TOPIC 00293: RFmxCDMA2k_CDAFetchSymbolEVMTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga8bbbb68f27f15c6e2840c679f7a835ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1ga8bbbb68f27f15c6e2840c679f7a835ed.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol EVM trace of the configured measurement channel. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptioni

### RFmxCDMA2k_CDAFetchSymbolEVMTrace

Returns the symbol EVM trace of the configured measurement channel.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| symbolEVM | [out] | float32[] | This parameter returns the array of symbol EVM values of the configured measurement channel. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gaa550551838acaa015af374e915bbb5f3.html language=enus -->
## TOPIC 00294: RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gaa550551838acaa015af374e915bbb5f3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gaa550551838acaa015af374e915bbb5f3.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I and Q code power trace measured in the code domain of the base spreading factor. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int3

### RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace

Returns the I and Q code power trace measured in the code domain of the base spreading factor.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iCodeDomainPowers | [out] | float32[] | This parameter returns the array of I code power measured in the code domain of the base spreading factor. This value is expressed in dB or dBm. |
| qCodeDomainPowers | [out] | float32[] | This parameter returns the array of Q code power measured in the code domain of the base spreading factor. This value is expressed in dB or dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gad6be6fa55f0b25a6eaaef91ba6a1b3b7.html language=enus -->
## TOPIC 00295: RFmxCDMA2k_CDAFetchCodeDomainIAndQPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gad6be6fa55f0b25a6eaaef91ba6a1b3b7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gad6be6fa55f0b25a6eaaef91ba6a1b3b7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I and Q mean active powers, and I and Q peak inactive powers. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *imEanActivePower, float64 *qMeanActivePower, float64 *iPeakInactivePower, float

### RFmxCDMA2k_CDAFetchCodeDomainIAndQPower

Returns the I and Q mean active powers, and I and Q peak inactive powers.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *imEanActivePower, float64 *qMeanActivePower, float64 *iPeakInactivePower, float64 *qPeakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| imEanActivePower | [out] | float64 * | This parameter returns the average power of all active code channels measured on the I-branch. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| qMeanActivePower | [out] | float64 * | This parameter returns the average power of all active code channels measured on the Q-branch. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |
| iPeakInactivePower | [out] | float64 * | This parameter returns the maximum measured code power among the set of inactive channels on the I-Branch. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |
| qPeakInactivePower | [out] | float64 * | This parameter returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gafa619f4bb1f9e441f802a14b8264994b.html language=enus -->
## TOPIC 00296: RFmxCDMA2k_CDAFetchCodeDomainPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gafa619f4bb1f9e441f802a14b8264994b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__cda_1gafa619f4bb1f9e441f802a14b8264994b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the scalar code domain power results. Syntaxint32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalPower, float64 *totalActivePower, float64 *meanActivePower, float64 *peakActivePower, float64 *meanInactive

### RFmxCDMA2k_CDAFetchCodeDomainPower

Returns the scalar code domain power results.

#### Syntax

int32 __stdcall RFmxCDMA2k_CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *totalPower, float64 *totalActivePower, float64 *meanActivePower, float64 *peakActivePower, float64 *meanInactivePower, float64 *peakInactivePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| totalPower | [out] | float64 * | This parameter returns the mean power of the received signal. This value is expressed in dBm. |
| totalActivePower | [out] | float64 * | This parameter returns the sum of the powers of all active code channels. If you set the RFMXCDMA2K_ATTR_CDA_POWER_UNIT attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the RFMXCDMA2K_ATTR_CDA_RESULTS_TOTAL_POWER attribute. |
| meanActivePower | [out] | float64 * | This parameter returns the average power of all active code channels. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |
| peakActivePower | [out] | float64 * | This parameter returns the maximum power among all active code channels. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |
| meanInactivePower | [out] | float64 * | This parameter returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |
| peakInactivePower | [out] | float64 * | This parameter returns the maximum measured code power among the set of inactive channels in the code domain of the base spreading factor. If you set the CDA Pwr Unit attribute to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp.html language=enus -->
## TOPIC 00297: CHP

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CHPFetchCarrierAbsolutePowerReturns the absolute carrier power of the CHP measurement. RFmxCDMA2k_CHPFetchSpectrumFetches the spectrum used for the CHP measurement. AttachmentsNone

### CHP

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CHPFetchCarrierAbsolutePower | Returns the absolute carrier power of the CHP measurement. |
| RFmxCDMA2k_CHPFetchSpectrum | Fetches the spectrum used for the CHP measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp_1ga03e4e4caba32a14d27d43a5bba1c5b1b.html language=enus -->
## TOPIC 00298: RFmxCDMA2k_CHPFetchSpectrum

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp_1ga03e4e4caba32a14d27d43a5bba1c5b1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp_1ga03e4e4caba32a14d27d43a5bba1c5b1b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement. Syntaxint32 __stdcall RFmxCDMA2k_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptio

### RFmxCDMA2k_CHPFetchSpectrum

Fetches the spectrum used for the CHP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp_1ga0bdecd0a766a6d766d3a1668b7c6c4cf.html language=enus -->
## TOPIC 00299: RFmxCDMA2k_CHPFetchCarrierAbsolutePower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp_1ga0bdecd0a766a6d766d3a1668b7c6c4cf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__chp_1ga0bdecd0a766a6d766d3a1668b7c6c4cf.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power of the CHP measurement. Syntaxint32 __stdcall RFmxCDMA2k_CHPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHand

### RFmxCDMA2k_CHPFetchCarrierAbsolutePower

Returns the absolute carrier power of the CHP measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_CHPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsolutePower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsolutePower | [out] | float64 * | This parameter returns the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc.html language=enus -->
## TOPIC 00300: ModAcc

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_ModAccFetchConstellationTraceReturns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement. RFmxCDMA2k_ModAccFetchConstellationTraceSplitReturns the complex chips of the corrected composite signal for the

### ModAcc

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_ModAccFetchConstellationTrace | Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement. |
| RFmxCDMA2k_ModAccFetchConstellationTraceSplit | Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement. |
| RFmxCDMA2k_ModAccFetchDetectedChannel | Returns a detected channel by its channel name. |
| RFmxCDMA2k_ModAccFetchDetectedChannelArray | Returns the detected channels. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the measurement returns the configured channels. |
| RFmxCDMA2k_ModAccFetchEVM | Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal. |
| RFmxCDMA2k_ModAccFetchEVMTrace | Returns the EVM trace of the ModAcc measurement. |
| RFmxCDMA2k_ModAccFetchIQImpairments | Returns the origin offset, gain imbalance, and quadrature error. |
| RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace | Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement. |
| RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels | Returns the total number of detected channels. If the you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the measurement returns the number of configured channels. |
| RFmxCDMA2k_ModAccFetchPeakActiveCDE | Returns the peak value among the code domain errors of the active channels, along with the code number and the code length. |
| RFmxCDMA2k_ModAccFetchPeakCDE | Returns the maximum value among the code domain errors (CDEs), in dB. |
| RFmxCDMA2k_ModAccFetchPhaseErrorTrace | Returns the phase error trace of the ModAcc measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga299d436754eba2743d4085ded8680af9.html language=enus -->
## TOPIC 00301: RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga299d436754eba2743d4085ded8680af9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga299d436754eba2743d4085ded8680af9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total number of detected channels. If the you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the measurement returns the number of configured channels. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle,

### RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels

Returns the total number of detected channels. If the you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**, the measurement returns the number of configured channels.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *numberOfDetectedChannels)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| numberOfDetectedChannels | [out] | int32 * | This parameter returns the total number of detected channels. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga331bc82f742f7f302aa54002313cb602.html language=enus -->
## TOPIC 00302: RFmxCDMA2k_ModAccFetchDetectedChannel

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga331bc82f742f7f302aa54002313cb602.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga331bc82f742f7f302aa54002313cb602.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a detected channel by its channel name. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedWalshCodeLength, int32 *detectedWalshCodeNumber, int32 *detectedBranch)RemarksUse "channel<n>" as the

### RFmxCDMA2k_ModAccFetchDetectedChannel

Returns a detected channel by its channel name.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *detectedWalshCodeLength, int32 *detectedWalshCodeNumber, int32 *detectedBranch)

#### Remarks

Use "channel<n>" as the selector string to read results from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"channel0""signal::sig1/channel0""result::r1/channel0""signal::sig1/result::r1/channel0"You can use the RFmxCDMA2k_BuildChannelString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedWalshCodeLength | [out] | int32 * | This parameter returns the detected Walsh code length. |
| detectedWalshCodeNumber | [out] | int32 * | This parameter returns the detected Walsh code number. |
| detectedBranch | [out] | int32 * | This parameter returns the detected branch.Name (value)DescriptionI (0)The signal modulated on the in-phase branch.Q (1)The signal modulated on the quadrature branch.I and Q (2)The signal modulated on the in-phase branch and quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | The signal modulated on the in-phase branch. |  |  |
| Q (1) | The signal modulated on the quadrature branch. |  |  |
| I and Q (2) | The signal modulated on the in-phase branch and quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga429e74062aab360ec86d6355a0e28e01.html language=enus -->
## TOPIC 00303: RFmxCDMA2k_ModAccFetchPeakCDE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga429e74062aab360ec86d6355a0e28e01.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga429e74062aab360ec86d6355a0e28e01.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the code domain errors (CDEs), in dB. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakCDE, int32 *peakCDEWalshCodeNumber, int32 *peakCDEBranch)RemarksThis function calculates

### RFmxCDMA2k_ModAccFetchPeakCDE

Returns the maximum value among the code domain errors (CDEs), in dB.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakCDE, int32 *peakCDEWalshCodeNumber, int32 *peakCDEBranch)

#### Remarks

This function calculates the CDEs by projecting the descrambled error vector onto the code domain at a specific spreading factor.

The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 32 is used.

This function computes the CDEs separately for I and Q branches.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakCDE | [out] | float64 * | This parameter returns the maximum value among the code domain errors. This value is expressed in dB. |
| peakCDEWalshCodeNumber | [out] | int32 * | This parameter returns the code number of the channel corresponding to the Peak CDE value. |
| peakCDEBranch | [out] | int32 * | This parameter returns the branch of the channel corresponding to the Peak CDE value.Name (value)DescriptionI (0)The signal is modulated on the in-phase branch.Q (1)The signal is modulated on the quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | The signal is modulated on the in-phase branch. |  |  |
| Q (1) | The signal is modulated on the quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga42b346a45357b6273afe136e430bc892.html language=enus -->
## TOPIC 00304: RFmxCDMA2k_ModAccFetchIQImpairments

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga42b346a45357b6273afe136e430bc892.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga42b346a45357b6273afe136e430bc892.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the origin offset, gain imbalance, and quadrature error. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)ParametersNameDirection

### RFmxCDMA2k_ModAccFetchIQImpairments

Returns the origin offset, gain imbalance, and quadrature error.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *iqOriginOffset, float64 *iqGainImbalance, float64 *iqQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| iqOriginOffset | [out] | float64 * | This parameter returns the I/Q origin offset of the composite signal. This value is expressed in dB. |
| iqGainImbalance | [out] | float64 * | This parameter returns the I/Q gain imbalance of the composite signal. This value is expressed in dB. |
| iqQuadratureError | [out] | float64 * | This parameter returns the I/Q quadrature error of the composite signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga5ccd33a73dd6f2b4bb5f5f78950c674b.html language=enus -->
## TOPIC 00305: RFmxCDMA2k_ModAccFetchConstellationTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga5ccd33a73dd6f2b4bb5f5f78950c674b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga5ccd33a73dd6f2b4bb5f5f78950c674b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, i

### RFmxCDMA2k_ModAccFetchConstellationTrace

Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellation | [out] | NIComplexSingle[] | This parameter returns the array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga622dc2dd33dea7105287bfcb144a7146.html language=enus -->
## TOPIC 00306: RFmxCDMA2k_ModAccFetchPeakActiveCDE

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga622dc2dd33dea7105287bfcb144a7146.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga622dc2dd33dea7105287bfcb144a7146.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value among the code domain errors of the active channels, along with the code number and the code length. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakActiveCDE, int32 *peakActiveC

### RFmxCDMA2k_ModAccFetchPeakActiveCDE

Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *peakActiveCDE, int32 *peakActiveCDEWalshCodeLength, int32 *peakActiveCDEWalshCodeNumber, int32 *peakActiveCDEBranch)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| peakActiveCDE | [out] | float64 * | This parameter returns the peak value of all CDEs of the active channels. This value is expressed in dB. |
| peakActiveCDEWalshCodeLength | [out] | int32 * | This parameter returns the Walsh code length of the channel corresponding to the Peak Active CDE value. |
| peakActiveCDEWalshCodeNumber | [out] | int32 * | This parameter returns the Walsh code number of the channel corresponding to the Peak Active CDE value. |
| peakActiveCDEBranch | [out] | int32 * | This parameter returns the branch of the channel corresponding to the Peak Active CDE value.Name (value)DescriptionI (0)The signal is modulated on the in-phase branch.Q (1)The signal is modulated on the quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | The signal is modulated on the in-phase branch. |  |  |
| Q (1) | The signal is modulated on the quadrature branch. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga7dfd18eebe3fc01a42a6335902390b5d.html language=enus -->
## TOPIC 00307: RFmxCDMA2k_ModAccFetchEVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga7dfd18eebe3fc01a42a6335902390b5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga7dfd18eebe3fc01a42a6335902390b5d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsEVM, float64 *peakEVM, float64 *rho, float64 *frequen

### RFmxCDMA2k_ModAccFetchEVM

Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *rmsEVM, float64 *peakEVM, float64 *rho, float64 *frequencyError, float64 *chipRateError, float64 *rmsMagnitudeError, float64 *rmsPhaseError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| rmsEVM | [out] | float64 * | This parameter returns the RMS EVM of the composite signal. This value is expressed as a percentage. |
| peakEVM | [out] | float64 * | This parameter returns the peak value of the uplink EVM. This value is expressed as a percentage. |
| rho | [out] | float64 * | This parameter returns the correlation of the received signal with the reference signal normalized by the signal power. |
| frequencyError | [out] | float64 * | This parameter returns the frequency error. This value is expressed in Hz. |
| chipRateError | [out] | float64 * | This parameter returns the chip rate error. This value is expressed in parts per million (ppm). |
| rmsMagnitudeError | [out] | float64 * | This parameter returns the RMS magnitude error of the composite signal. This value is expressed as a percentage. |
| rmsPhaseError | [out] | float64 * | This parameter returns the RMS phase error of the composite signal. This value is expressed in degrees (deg). |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga88311c0bc6397b8730cd8d3c8fba7ffe.html language=enus -->
## TOPIC 00308: RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga88311c0bc6397b8730cd8d3c8fba7ffe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga88311c0bc6397b8730cd8d3c8fba7ffe.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *

### RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace

Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| magnitudeError | [out] | float32[] | This parameter returns the array of the magnitude error values. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga9662eacb3fe5bc3780ac9555bb05f9d1.html language=enus -->
## TOPIC 00309: RFmxCDMA2k_ModAccFetchEVMTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga9662eacb3fe5bc3780ac9555bb05f9d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1ga9662eacb3fe5bc3780ac9555bb05f9d1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the EVM trace of the ModAcc measurement. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDescriptionins

### RFmxCDMA2k_ModAccFetchEVMTrace

Returns the EVM trace of the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 evm[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the delta parameter. |
| evm | [out] | float32[] | This parameter returns the real signal values stored in an array. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gac995ab90047893bd91ef17172a6395b4.html language=enus -->
## TOPIC 00310: RFmxCDMA2k_ModAccFetchPhaseErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gac995ab90047893bd91ef17172a6395b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gac995ab90047893bd91ef17172a6395b4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase error trace of the ModAcc measurement. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameDirec

### RFmxCDMA2k_ModAccFetchPhaseErrorTrace

Returns the phase error trace of the ModAcc measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| phaseError | [out] | float32[] | This parameter returns the array of phase error values. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gacedb8c4b6e587abbd5988b1b12bd60b8.html language=enus -->
## TOPIC 00311: RFmxCDMA2k_ModAccFetchConstellationTraceSplit

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gacedb8c4b6e587abbd5988b1b12bd60b8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gacedb8c4b6e587abbd5988b1b12bd60b8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellatio

### RFmxCDMA2k_ModAccFetchConstellationTraceSplit

Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationI | [out] | float32[] | This parameter Returns the real part of array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| constellationQ | [out] | float32[] | This parameter Returns the imaginary part of array of complex chips of the corrected signal on which the ModAcc measurements are performed. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gacf7d87c98e55164880986582ac8f3cb6.html language=enus -->
## TOPIC 00312: RFmxCDMA2k_ModAccFetchDetectedChannelArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gacf7d87c98e55164880986582ac8f3cb6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__modacc_1gacf7d87c98e55164880986582ac8f3cb6.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected channels. If you set the RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE attribute to User Defined, the measurement returns the configured channels. Syntaxint32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 tim

### RFmxCDMA2k_ModAccFetchDetectedChannelArray

Returns the detected channels. If you set the [RFMXCDMA2K_ATTR_CHANNEL_CONFIGURATION_MODE](group____root__ni_r_fmx_c_d_m_a2k__attributes__channel_1ga3c88eb1dedd8333791a4fdde39fcdb76.html) attribute to **User Defined**, the measurement returns the configured channels.

#### Syntax

int32 __stdcall RFmxCDMA2k_ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedWalshCodeLength[], int32 detectedWalshCodeNumber[], int32 detectedBranch[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| detectedWalshCodeLength | [out] | int32[] | This parameter returns the array of the detected Walsh code length. |
| detectedWalshCodeNumber | [out] | int32[] | This parameter returns the array of the detected Walsh code number. |
| detectedBranch | [out] | int32[] | This parameter returns the array of the detected branch.Name (value)DescriptionI (0)The signal modulated on the in-phase branch.Q (1)The signal modulated on the quadrature branch.I and Q (2)The signal modulated on the in-phase branch and quadrature branch. |
| Name (value) | Description |  |  |
| I (0) | The signal modulated on the in-phase branch. |  |  |
| Q (1) | The signal modulated on the quadrature branch. |  |  |
| I and Q (2) | The signal modulated on the in-phase branch and quadrature branch. |  |  |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw.html language=enus -->
## TOPIC 00313: OBW

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_OBWFetchMeasurementReturns the OBW measurement. RFmxCDMA2k_OBWFetchSpectrumFetches the spectrum trace used for the OBW measurement. AttachmentsNone

### OBW

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_OBWFetchMeasurement | Returns the OBW measurement. |
| RFmxCDMA2k_OBWFetchSpectrum | Fetches the spectrum trace used for the OBW measurement. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw_1ga5a5548c35e19abb4f9d77f82f6b0a56c.html language=enus -->
## TOPIC 00314: RFmxCDMA2k_OBWFetchSpectrum

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw_1ga5a5548c35e19abb4f9d77f82f6b0a56c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw_1ga5a5548c35e19abb4f9d77f82f6b0a56c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum trace used for the OBW measurement. Syntaxint32 __stdcall RFmxCDMA2k_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)ParametersNameDirectionTypeDesc

### RFmxCDMA2k_OBWFetchSpectrum

Fetches the spectrum trace used for the OBW measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw_1gaf85a3ba5b403a5edf5c89de8717841ed.html language=enus -->
## TOPIC 00315: RFmxCDMA2k_OBWFetchMeasurement

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw_1gaf85a3ba5b403a5edf5c89de8717841ed.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__obw_1gaf85a3ba5b403a5edf5c89de8717841ed.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the OBW measurement. Syntaxint32 __stdcall RFmxCDMA2k_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)ParametersNameDirectionTypeDescriptioninst

### RFmxCDMA2k_OBWFetchMeasurement

Returns the OBW measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *occupiedBandwidth, float64 *absolutePower, float64 *startFrequency, float64 *stopFrequency)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| occupiedBandwidth | [out] | float64 * | This parameter returns the occupied bandwidth. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency |
| absolutePower | [out] | float64 * | This parameter returns the total integrated power of the spectrum acquired by the OBW measurement. This value is expressed in dBm. |
| startFrequency | [out] | float64 * | This parameter returns the start frequency of the OBW. This value is expressed in Hz. |
| stopFrequency | [out] | float64 * | This parameter returns the stop frequency of the OBW. This value is expressed in Hz. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm.html language=enus -->
## TOPIC 00316: QEVM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_QEVMFetchConstellationTraceReturns the complex chips of the corrected received signal for the QEVM measurement. RFmxCDMA2k_QEVMFetchConstellationTraceSplitReturns the complex chips of the corrected received signal for the QEVM measurement. RFmxCDMA2k_

### QEVM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_QEVMFetchConstellationTrace | Returns the complex chips of the corrected received signal for the QEVM measurement. |
| RFmxCDMA2k_QEVMFetchConstellationTraceSplit | Returns the complex chips of the corrected received signal for the QEVM measurement. |
| RFmxCDMA2k_QEVMFetchEVM | Returns the EVM value and related measurement values of the QEVM measurement. |
| RFmxCDMA2k_QEVMFetchEVMTrace | Returns the EVM trace of the last averaging iteration. |
| RFmxCDMA2k_QEVMFetchIQImpairments | Returns the measured I/Q impairments. |
| RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace | Returns the magnitude error trace of the last averaging iteration. |
| RFmxCDMA2k_QEVMFetchPhaseErrorTrace | Returns the phase error trace of the last averaging iteration. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1ga362d7e34df712ff3d1b5151a3eb69daa.html language=enus -->
## TOPIC 00317: RFmxCDMA2k_QEVMFetchIQImpairments

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1ga362d7e34df712ff3d1b5151a3eb69daa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1ga362d7e34df712ff3d1b5151a3eb69daa.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured I/Q impairments. Syntaxint32 __stdcall RFmxCDMA2k_QEVMFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanIQOriginOffset, float64 *meanIQGainImbalance, float64 *meanIQQuadratureError, float64 *maximumIQOriginOffset, float64

### RFmxCDMA2k_QEVMFetchIQImpairments

Returns the measured I/Q impairments.

#### Syntax

int32 __stdcall RFmxCDMA2k_QEVMFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *meanIQOriginOffset, float64 *meanIQGainImbalance, float64 *meanIQQuadratureError, float64 *maximumIQOriginOffset, float64 *maximumIQGainImbalance, float64 *maximumIQQuadratureError)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| meanIQOriginOffset | [out] | float64 * | This parameter returns the mean averaged origin offset of the received signal. This value is expressed in dB. |
| meanIQGainImbalance | [out] | float64 * | This parameter returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. |
| meanIQQuadratureError | [out] | float64 * | This parameter returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| maximumIQOriginOffset | [out] | float64 * | This parameter returns the maximum origin offset of the received signal. This value is expressed in dB. |
| maximumIQGainImbalance | [out] | float64 * | This parameter returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. |
| maximumIQQuadratureError | [out] | float64 * | This parameter returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1ga8ab329cc6b5616ef8ceed9e1e2fe8bcb.html language=enus -->
## TOPIC 00318: RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1ga8ab329cc6b5616ef8ceed9e1e2fe8bcb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1ga8ab329cc6b5616ef8ceed9e1e2fe8bcb.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the magnitude error trace of the last averaging iteration. Syntaxint32 __stdcall RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)Par

### RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace

Returns the magnitude error trace of the last averaging iteration.

#### Syntax

int32 __stdcall RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 magnitudeError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| magnitudeError | [out] | float32[] | This parameter returns the array of the magnitude error values. This value is expressed as a percentage. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1gaaf52b37ff774c8219043f782140ecd8f.html language=enus -->
## TOPIC 00319: RFmxCDMA2k_QEVMFetchConstellationTraceSplit

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1gaaf52b37ff774c8219043f782140ecd8f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1gaaf52b37ff774c8219043f782140ecd8f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the complex chips of the corrected received signal for the QEVM measurement. Syntaxint32 __stdcall RFmxCDMA2k_QEVMFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int3

### RFmxCDMA2k_QEVMFetchConstellationTraceSplit

Returns the complex chips of the corrected received signal for the QEVM measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_QEVMFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| constellationI | [out] | float32[] | This parameter Returns the real part of array of complex chips of the corrected signal on which the QEVM measurements are performed. You can use these chips to obtain the constellation diagram. |
| constellationQ | [out] | float32[] | This parameter Returns the imaginary part of array of complex chips of the corrected signal on which the QEVM measurements are performed. You can use these chips to obtain the constellation diagram. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1gae5963e624180bcaface4cda4e389bcf8.html language=enus -->
## TOPIC 00320: RFmxCDMA2k_QEVMFetchPhaseErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1gae5963e624180bcaface4cda4e389bcf8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__qevm_1gae5963e624180bcaface4cda4e389bcf8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the phase error trace of the last averaging iteration. Syntaxint32 __stdcall RFmxCDMA2k_QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)ParametersNameD

### RFmxCDMA2k_QEVMFetchPhaseErrorTrace

Returns the phase error trace of the last averaging iteration.

#### Syntax

int32 __stdcall RFmxCDMA2k_QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 phaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the chip duration. This value is expressed in seconds. |
| phaseError | [out] | float32[] | This parameter returns the array of phase error values. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem.html language=enus -->
## TOPIC 00321: SEM

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPowerReturns the absolute carrier integrated power of the SEM measurement. RFmxCDMA2k_SEMFetchLowerOffsetMarginReturns the measurement status and margin from the limit line measured in the lower offset segment. RFmxCDM

### SEM

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower | Returns the absolute carrier integrated power of the SEM measurement. |
| RFmxCDMA2k_SEMFetchLowerOffsetMargin | Returns the measurement status and margin from the limit line measured in the lower offset segment. |
| RFmxCDMA2k_SEMFetchLowerOffsetMarginArray | Returns the array of measurement status and margins from the limit line measured in the lower offset segments. |
| RFmxCDMA2k_SEMFetchLowerOffsetPower | Returns the lower offset segment power measurements. |
| RFmxCDMA2k_SEMFetchLowerOffsetPowerArray | Returns the arrays of lower offset segment power measurements. |
| RFmxCDMA2k_SEMFetchMeasurementStatus | Returns the SEM measurement status. |
| RFmxCDMA2k_SEMFetchSpectrum | Returns the spectrum used for the SEM measurement. |
| RFmxCDMA2k_SEMFetchUpperOffsetMargin | Returns the measurement status and margin from the limit line measured in the upper offset segment. |
| RFmxCDMA2k_SEMFetchUpperOffsetMarginArray | Returns the measurement status and margin from the limit line measured in the upper offset segments. |
| RFmxCDMA2k_SEMFetchUpperOffsetPower | Returns the upper offset segment power measurements. |
| RFmxCDMA2k_SEMFetchUpperOffsetPowerArray | Returns the arrays of upper offset segment power measurements. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga00e222e51353ae8b0ee130bc5b2938b0.html language=enus -->
## TOPIC 00322: RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga00e222e51353ae8b0ee130bc5b2938b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga00e222e51353ae8b0ee130bc5b2938b0.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier integrated power of the SEM measurement. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsoluteIntegratedPower)ParametersNameDirectionTypeDescriptioninst

### RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower

Returns the absolute carrier integrated power of the SEM measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *carrierAbsoluteIntegratedPower)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| carrierAbsoluteIntegratedPower | [out] | float64 * | This parameter returns the averaged integrated channel power measured in the specified integration bandwidth. This value is expressed in dBm. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga2faf84ea3e16748be549d2b41d18a80f.html language=enus -->
## TOPIC 00323: RFmxCDMA2k_SEMFetchLowerOffsetPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga2faf84ea3e16748be549d2b41d18a80f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga2faf84ea3e16748be549d2b41d18a80f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment power measurements. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFreq

### RFmxCDMA2k_SEMFetchLowerOffsetPower

Returns the lower offset segment power measurements.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Remarks

Use "offset<n>" as the selector string to read parameters from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxCDMA2k_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the lower (negative) offset segment power measured. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power in the lower (negative) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | [out] | float64 * | This parameter returns the peak power measured in the lower (negative) offset segment. The power is measured in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power in the lower (negative) offset segment relative to the carrier absolute integrated power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga39d0581c4d87056d1db3a241398f72a7.html language=enus -->
## TOPIC 00324: RFmxCDMA2k_SEMFetchLowerOffsetMarginArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga39d0581c4d87056d1db3a241398f72a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga39d0581c4d87056d1db3a241398f72a7.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement status and margins from the limit line measured in the lower offset segments. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], floa

### RFmxCDMA2k_SEMFetchLowerOffsetMarginArray

Returns the array of measurement status and margins from the limit line measured in the lower offset segments.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of lower offset measurement status based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The measurement fails according to the measurement limits specified by this standard.Pass (1)The measurement passes according to the measurement limits specified by this standard. |
| Name (value) | Description |  |  |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |  |  |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |  |  |
| margin | [out] | float64[] | This parameter returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the margin occurred in each lower (negative) offset segment. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurred in each lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga5a36d9452d67ccba97a246cad31aa75f.html language=enus -->
## TOPIC 00325: RFmxCDMA2k_SEMFetchUpperOffsetMarginArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga5a36d9452d67ccba97a246cad31aa75f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga5a36d9452d67ccba97a246cad31aa75f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 margin

### RFmxCDMA2k_SEMFetchUpperOffsetMarginArray

Returns the measurement status and margin from the limit line measured in the upper offset segments.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32[] | This parameter returns the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The measurement fails according to the measurement limits specified by this standard.Pass (1)The measurement passes according to the measurement limits specified by this standard. |
| Name (value) | Description |  |  |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |  |  |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |  |  |
| margin | [out] | float64[] | This parameter returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). |
| marginFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64[] | This parameter returns the array of powers at which the margin occurred in each upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga9874fb9ad8b2f06b019cfa377252e622.html language=enus -->
## TOPIC 00326: RFmxCDMA2k_SEMFetchUpperOffsetMargin

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga9874fb9ad8b2f06b019cfa377252e622.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1ga9874fb9ad8b2f06b019cfa377252e622.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequen

### RFmxCDMA2k_SEMFetchUpperOffsetMargin

Returns the measurement status and margin from the limit line measured in the upper offset segment.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read parameters from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxCDMA2k_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The measurement fails according to the measurement limits specified by this standard.Pass (1)The measurement passes according to the measurement limits specified by this standard. |
| Name (value) | Description |  |  |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |  |  |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |  |  |
| margin | [out] | float64 * | This parameter returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaa1a04c4cc7db4fc2048d79088450a407.html language=enus -->
## TOPIC 00327: RFmxCDMA2k_SEMFetchMeasurementStatus

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaa1a04c4cc7db4fc2048d79088450a407.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaa1a04c4cc7db4fc2048d79088450a407.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM measurement status. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the

### RFmxCDMA2k_SEMFetchMeasurementStatus

Returns the SEM measurement status.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the overall measurement status based on the measurement limits which are specified by the standard for each offset segment.Name (value)DescriptionFail (0)The measurement fails according to the measurement limits specified by this standard.Pass (1)The measurement passes according to the measurement limits specified by this standard. |
| Name (value) | Description |  |  |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |  |  |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |  |  |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gab985dc8f68d3e9ece43d9103a29d56c5.html language=enus -->
## TOPIC 00328: RFmxCDMA2k_SEMFetchUpperOffsetPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gab985dc8f68d3e9ece43d9103a29d56c5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gab985dc8f68d3e9ece43d9103a29d56c5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFreq

### RFmxCDMA2k_SEMFetchUpperOffsetPower

Returns the upper offset segment power measurements.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *absoluteIntegratedPower, float64 *relativeIntegratedPower, float64 *absolutePeakPower, float64 *peakFrequency, float64 *relativePeakPower)

#### Remarks

Use "offset<n>" as the selector string to read parameters from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxCDMA2k_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64 * | This parameter returns the upper (positive) offset segment power measured. |
| relativeIntegratedPower | [out] | float64 * | This parameter returns the power in the upper (positive) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | [out] | float64 * | This parameter returns the peak power measured in the upper (positive) offset segment. The power is measured in dBm. |
| peakFrequency | [out] | float64 * | This parameter returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64 * | This parameter returns the peak power in the upper (positive) offset segment relative to the carrier absolute integrated power. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gab9a74d457fd39cf5148762a636d9459f.html language=enus -->
## TOPIC 00329: RFmxCDMA2k_SEMFetchLowerOffsetPowerArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gab9a74d457fd39cf5148762a636d9459f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gab9a74d457fd39cf5148762a636d9459f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[],

### RFmxCDMA2k_SEMFetchLowerOffsetPowerArray

Returns the arrays of lower offset segment power measurements.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| absoluteIntegratedPower | [out] | float64[] | This parameter returns the array of lower (negative) offset segment powers measured. |
| relativeIntegratedPower | [out] | float64[] | This parameter returns the array of powers in each lower (negative) offset segment relative to the carrier absolute integrated power. |
| absolutePeakPower | [out] | float64[] | This parameter returns the array of peak powers measured in each lower (negative) offset segment. The power is measured in dBm. |
| peakFrequency | [out] | float64[] | This parameter returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. |
| relativePeakPower | [out] | float64[] | This parameter returns the array of peak powers in the lower (negative) offset segment relative to the carrier absolute integrated power. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaef93c87c4613d7fd58f1726a598b5bc0.html language=enus -->
## TOPIC 00330: RFmxCDMA2k_SEMFetchLowerOffsetMargin

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaef93c87c4613d7fd58f1726a598b5bc0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaef93c87c4613d7fd58f1726a598b5bc0.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequen

### RFmxCDMA2k_SEMFetchLowerOffsetMargin

Returns the measurement status and margin from the limit line measured in the lower offset segment.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 *measurementStatus, float64 *margin, float64 *marginFrequency, float64 *marginAbsolutePower, float64 *marginRelativePower)

#### Remarks

Use "offset<n>" as the selector string to read parameters from this function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used.Examples:"offset0""signal::sig1/offset0""result::r1/offset0""signal::sig1/result::r1/offset0"You can use the RFmxCDMA2k_BuildOffsetString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| measurementStatus | [out] | int32 * | This parameter returns the lower offset measurement status based on measurement limits and the failure criteria specified by the standard.Name (value)DescriptionFail (0)The measurement fails according to the measurement limits specified by this standard.Pass (1)The measurement passes according to the measurement limits specified by this standard. |
| Name (value) | Description |  |  |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |  |  |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |  |  |
| margin | [out] | float64 * | This parameter returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). |
| marginFrequency | [out] | float64 * | This parameter returns the frequency at which the margin occurred in the lower (negative) offset. This value is expressed in Hz. |
| marginAbsolutePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. |
| marginRelativePower | [out] | float64 * | This parameter returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaf216099fac0e33de4890b5f249e96667.html language=enus -->
## TOPIC 00331: RFmxCDMA2k_SEMFetchSpectrum

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaf216099fac0e33de4890b5f249e96667.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__sem_1gaf216099fac0e33de4890b5f249e96667.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectrum used for the SEM measurement. Syntaxint32 __stdcall RFmxCDMA2k_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32 *actua

### RFmxCDMA2k_SEMFetchSpectrum

Returns the spectrum used for the SEM measurement.

#### Syntax

int32 __stdcall RFmxCDMA2k_SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start frequency. This value is expressed in Hz. |
| dx | [out] | float64 * | This parameter returns the frequency bin spacing. This value is expressed in Hz. |
| spectrum | [out] | float32[] | This parameter returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| relativeMask | [out] | float32[] | This parameter returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| absoluteMask | [out] | float32[] | This parameter returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase.html language=enus -->
## TOPIC 00332: SlotPhase

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTraceFetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured,

### SlotPhase

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace | Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the slot boundary and extrapolates the phase error to the slot boundaries. |
| RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace | Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform. |
| RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity | Fetches the maximum phase discontinuity value observed in the measurement interval. |
| RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities | Fetches the phase discontinuity values for the slot boundaries in the measurement interval. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1ga9b5b67c1ffcc6740e608988c04dcf32c.html language=enus -->
## TOPIC 00333: RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1ga9b5b67c1ffcc6740e608988c04dcf32c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1ga9b5b67c1ffcc6740e608988c04dcf32c.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity value observed in the measurement interval. Syntaxint32 __stdcall RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumPhaseDiscontinuity)ParametersNameDirectionTypeDescr

### RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity

Fetches the maximum phase discontinuity value observed in the measurement interval.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *maximumPhaseDiscontinuity)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| maximumPhaseDiscontinuity | [out] | float64 * | This parameter returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gab01dbaf973b7113e7cf210ed28602476.html language=enus -->
## TOPIC 00334: RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gab01dbaf973b7113e7cf210ed28602476.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gab01dbaf973b7113e7cf210ed28602476.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform. Syntaxint32 __stdcall RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 ti

### RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace

Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chipPhaseError[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the delta parameter. |
| chipPhaseError | [out] | float32[] | This parameter returns the array of chip phase error for the SlotPhase measurement. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gade607bc1552f8e2ca2546f761e677ed9.html language=enus -->
## TOPIC 00335: RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gade607bc1552f8e2ca2546f761e677ed9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gade607bc1552f8e2ca2546f761e677ed9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of th

### RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace

Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the slot boundary and extrapolates the phase error to the slot boundaries.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 *x0, float64 *dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| x0 | [out] | float64 * | This parameter returns the start time. This value is expressed in seconds. |
| dx | [out] | float64 * | This parameter returns the delta parameter. |
| chipPhaseErrorLinearFit | [out] | float32[] | This parameter returns the array of chip phase error for the SlotPhase measurement. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gae5f13c0ecc9a8b1e48aedf3a5e01f807.html language=enus -->
## TOPIC 00336: RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gae5f13c0ecc9a8b1e48aedf3a5e01f807.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotphase_1gae5f13c0ecc9a8b1e48aedf3a5e01f807.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity values for the slot boundaries in the measurement interval. Syntaxint32 __stdcall RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32 *actual

### RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities

Fetches the phase discontinuity values for the slot boundaries in the measurement interval.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotPhaseDiscontinuity | [out] | float64[] | This parameter returns the array of phase discontinuity values for the slot boundaries in the measurement interval. This value is expressed in degrees. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotpower.html language=enus -->
## TOPIC 00337: SlotPower

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotpower.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotpower.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SlotPowerFetchPowersFetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots. AttachmentsNone

### SlotPower

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SlotPowerFetchPowers | Fetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots. |

#### Attachments

None

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotpower_1ga0b644206a99128fd6fdbd08e41b51102.html language=enus -->
## TOPIC 00338: RFmxCDMA2k_SlotPowerFetchPowers

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotpower_1ga0b644206a99128fd6fdbd08e41b51102.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__fetch__slotpower_1ga0b644206a99128fd6fdbd08e41b51102.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots. Syntaxint32 __stdcall RFmxCDMA2k_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 time

### RFmxCDMA2k_SlotPowerFetchPowers

Fetches the SlotPower and SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots.

#### Syntax

int32 __stdcall RFmxCDMA2k_SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32 *actualArraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |
| slotPower | [out] | float64[] | This parameter returns the array of SlotPower for all slots in the configured measurement interval. This value is expressed in dBm. |
| slotPowerDelta | [out] | float64[] | This parameter returns the array of SlotPower delta values for all slots in the configured measurement interval. The slot power delta is the difference in power between adjacent slots. This value is expressed in dB. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__select__measurement.html language=enus -->
## TOPIC 00339: Select Measurement

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__select__measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__select__measurement.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SelectMeasurementsEnables all the measurements that you specify in the Measurements parameter and disables all other measurements. AttachmentsNone

### Select Measurement

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SelectMeasurements | Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__select__measurement_1ga13787c8b307eea24221d511ff0965b41.html language=enus -->
## TOPIC 00340: RFmxCDMA2k_SelectMeasurements

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__select__measurement_1ga13787c8b307eea24221d511ff0965b41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__select__measurement_1ga13787c8b307eea24221d511ff0965b41.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. Syntaxint32 __stdcall RFmxCDMA2k_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)ParametersNameDirectionTypeDescri

### RFmxCDMA2k_SelectMeasurements

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

#### Syntax

int32 __stdcall RFmxCDMA2k_SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| measurements | [in] | uInt32 | This parameter specifies the measurements to perform.The default is an empty array.Name (value)DescriptionModAcc (0)Enables the ModAcc measurement.ACP (1)Enables the ACP measurement.CHP (2)Enables the CHP measurement.OBW (3)Enables the OBW measurement.SEM (4)Enables the SEM measurement.QEVM (5)Enables the QEVM measurement.CDA (6)Enables the CDA measurement.SlotPhase (7)Enables the SlotPhase measurement.SlotPower (8)Enables the SlotPower measurement. |
| Name (value) | Description |  |  |
| ModAcc (0) | Enables the ModAcc measurement. |  |  |
| ACP (1) | Enables the ACP measurement. |  |  |
| CHP (2) | Enables the CHP measurement. |  |  |
| OBW (3) | Enables the OBW measurement. |  |  |
| SEM (4) | Enables the SEM measurement. |  |  |
| QEVM (5) | Enables the QEVM measurement. |  |  |
| CDA (6) | Enables the CDA measurement. |  |  |
| SlotPhase (7) | Enables the SlotPhase measurement. |  |  |
| SlotPower (8) | Enables the SlotPower measurement. |  |  |
| enableAllTraces | [in] | int32 | This parameter specifies whether to enable all traces for the selected measurements. The default value is False. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Select Measurement

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes.html language=enus -->
## TOPIC 00341: Set and Get Attributes

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes.html
- document_id: `rfmxcdma2k-c-api-ref`
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

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes.html language=enus -->
## TOPIC 00342: Get Attributes

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_GetAttributeF32Queries the value of an RFmx 32-bit floating point number (float32) attribute. RFmxCDMA2k_GetAttributeF32ArrayQueries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buf

### Get Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_GetAttributeF32 | Queries the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxCDMA2k_GetAttributeF32Array | Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeF64 | Queries the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxCDMA2k_GetAttributeF64Array | Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeI16 | Queries the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxCDMA2k_GetAttributeI32 | Queries the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxCDMA2k_GetAttributeI32Array | Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeI64 | Queries the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxCDMA2k_GetAttributeI64Array | Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeI8 | Queries the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxCDMA2k_GetAttributeI8Array | Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeNIComplexDoubleArray | Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeNIComplexSingleArray | Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeString | Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeU16 | Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxCDMA2k_GetAttributeU32 | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxCDMA2k_GetAttributeU32Array | Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeU64Array | Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |
| RFmxCDMA2k_GetAttributeU8 | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxCDMA2k_GetAttributeU8Array | Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the attrVal buffer. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga1b648a4a1f99cb86bb55010e0696e900.html language=enus -->
## TOPIC 00343: RFmxCDMA2k_GetAttributeI16

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga1b648a4a1f99cb86bb55010e0696e900.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga1b648a4a1f99cb86bb55010e0696e900.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxCDMA2k_GetAttributeI16

Queries the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga252433d4ede9812cbc200b67249f5093.html language=enus -->
## TOPIC 00344: RFmxCDMA2k_GetAttributeI32Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga252433d4ede9812cbc200b67249f5093.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga252433d4ede9812cbc200b67249f5093.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxCDMA2k_GetAttributeI32Array

Queries the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga2dadf55a08e9e53e58c03d7d2653ce4b.html language=enus -->
## TOPIC 00345: RFmxCDMA2k_GetAttributeF32

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga2dadf55a08e9e53e58c03d7d2653ce4b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga2dadf55a08e9e53e58c03d7d2653ce4b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleId

### RFmxCDMA2k_GetAttributeF32

Queries the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga3dd2ad2200b4d6f2bee1f7c04c0a78fa.html language=enus -->
## TOPIC 00346: RFmxCDMA2k_GetAttributeU64Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga3dd2ad2200b4d6f2bee1f7c04c0a78fa.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga3dd2ad2200b4d6f2bee1f7c04c0a78fa.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxCDMA2k_GetAttributeU64Array

Queries the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga546a9b3e9c855be8d19bcade7caed175.html language=enus -->
## TOPIC 00347: RFmxCDMA2k_GetAttributeI8Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga546a9b3e9c855be8d19bcade7caed175.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga546a9b3e9c855be8d19bcade7caed175.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and

### RFmxCDMA2k_GetAttributeI8Array

Queries the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga546f03bb3b4527b10ca26e99b3176896.html language=enus -->
## TOPIC 00348: RFmxCDMA2k_GetAttributeU16

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga546f03bb3b4527b10ca26e99b3176896.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga546f03bb3b4527b10ca26e99b3176896.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifie

### RFmxCDMA2k_GetAttributeU16

Queries the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt16 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga5fce57b81c775c9106896ecfa9a71a09.html language=enus -->
## TOPIC 00349: RFmxCDMA2k_GetAttributeNIComplexSingleArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga5fce57b81c775c9106896ecfa9a71a09.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga5fce57b81c775c9106896ecfa9a71a09.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxCDMA2k_GetAttributeNIComplexSingleArray

Queries the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexSingle[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga602fcd610ff9894ca76a583eeab6d556.html language=enus -->
## TOPIC 00350: RFmxCDMA2k_GetAttributeF64

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga602fcd610ff9894ca76a583eeab6d556.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga602fcd610ff9894ca76a583eeab6d556.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleId

### RFmxCDMA2k_GetAttributeF64

Queries the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga6743a9a3b7ad1561bf23d0baee38dabc.html language=enus -->
## TOPIC 00351: RFmxCDMA2k_GetAttributeI64Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga6743a9a3b7ad1561bf23d0baee38dabc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga6743a9a3b7ad1561bf23d0baee38dabc.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize an

### RFmxCDMA2k_GetAttributeI64Array

Queries the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga6c4f8efd290f967623915fbf8048e9c1.html language=enus -->
## TOPIC 00352: RFmxCDMA2k_GetAttributeF32Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga6c4f8efd290f967623915fbf8048e9c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga6c4f8efd290f967623915fbf8048e9c1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxCDMA2k_GetAttributeF32Array

Queries the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga77e2044d63b80de4c5ab520c50d40e23.html language=enus -->
## TOPIC 00353: RFmxCDMA2k_GetAttributeI8

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga77e2044d63b80de4c5ab520c50d40e23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga77e2044d63b80de4c5ab520c50d40e23.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxCDMA2k_GetAttributeI8

Queries the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga8aa403149011186af53d4ad6713b24ad.html language=enus -->
## TOPIC 00354: RFmxCDMA2k_GetAttributeF64Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga8aa403149011186af53d4ad6713b24ad.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga8aa403149011186af53d4ad6713b24ad.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0

### RFmxCDMA2k_GetAttributeF64Array

Queries the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | float64[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga9faa7ef96b452e84d8701b3249b3d875.html language=enus -->
## TOPIC 00355: RFmxCDMA2k_GetAttributeU32Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga9faa7ef96b452e84d8701b3249b3d875.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1ga9faa7ef96b452e84d8701b3249b3d875.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for ar

### RFmxCDMA2k_GetAttributeU32Array

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaae056f46ede549b2c4468d8f772a6146.html language=enus -->
## TOPIC 00356: RFmxCDMA2k_GetAttributeString

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaae056f46ede549b2c4468d8f772a6146.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaae056f46ede549b2c4468d8f772a6146.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL for the a

### RFmxCDMA2k_GetAttributeString

Queries the value of an RFmx string attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 arraySize, char attrVal[])

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being read. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Pass the number of bytes in the char buffer you specify for the attrVal parameter. If you pass 0, you can pass NULL for the attrVal parameter. |
| attrVal | [out] | char[] | Returns the current value of the attribute. This parameter must have at least as many bytes as indicated in the arraySize parameter. If you specify 0 for the arraySize parameter, you can pass NULL for this parameter. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

When the **statusOrRequiredSize** return value returns the buffer size, the status code is not returned.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gab8dbbef571a40aa20e21ca1088a08985.html language=enus -->
## TOPIC 00357: RFmxCDMA2k_GetAttributeI32

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gab8dbbef571a40aa20e21ca1088a08985.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gab8dbbef571a40aa20e21ca1088a08985.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxCDMA2k_GetAttributeI32

Queries the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gac42631c30f364fb850b279e9260a4aca.html language=enus -->
## TOPIC 00358: RFmxCDMA2k_GetAttributeNIComplexDoubleArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gac42631c30f364fb850b279e9260a4aca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gac42631c30f364fb850b279e9260a4aca.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arraySize and NULL

### RFmxCDMA2k_GetAttributeNIComplexDoubleArray

Queries the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | NIComplexDouble[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gac60eb0bd9e4b8ae4a26a60c378782546.html language=enus -->
## TOPIC 00359: RFmxCDMA2k_GetAttributeU8

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gac60eb0bd9e4b8ae4a26a60c378782546.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gac60eb0bd9e4b8ae4a26a60c378782546.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies th

### RFmxCDMA2k_GetAttributeU8

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gad5eec7739c2d48c109d7665233a80b14.html language=enus -->
## TOPIC 00360: RFmxCDMA2k_GetAttributeU8Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gad5eec7739c2d48c109d7665233a80b14.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gad5eec7739c2d48c109d7665233a80b14.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for arra

### RFmxCDMA2k_GetAttributeU8Array

Queries the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. If you want to call this function just to get the required buffer size, you must pass 0 for **arraySize** and NULL for the **attrVal** buffer.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize, int32 *actualArraySize)

#### Remarks

If the current value of the attribute, including the terminating NULL byte, is larger than the size you indicate in the **arraySize** parameter, the function copies buffer size - 1 bytes into the buffer, places an ASCII NULL byte at the end of the buffer, and returns the buffer size you must pass to get the entire value. For example, if the value is "123456" and the buffer size is 4, the function places "123" into the buffer and returns 7.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt8[] | Returns the current value of the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. Set the arraySize parameter to 0 to get the size of all the arrays in the actualArraySize parameter. |
| actualArraySize | [out] | int32 * | Returns the actual size of the array, if you pass NULL to all output array parameters, and set the arraySize parameter to 0. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaefacaf8e3c7e15cd5fea6f4c830b0ac8.html language=enus -->
## TOPIC 00361: RFmxCDMA2k_GetAttributeI64

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaefacaf8e3c7e15cd5fea6f4c830b0ac8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaefacaf8e3c7e15cd5fea6f4c830b0ac8.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx

### RFmxCDMA2k_GetAttributeI64

Queries the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | int64 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaf1f32978834274df85918caa78143c1e.html language=enus -->
## TOPIC 00362: RFmxCDMA2k_GetAttributeU32

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaf1f32978834274df85918caa78143c1e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__get__attributes_1gaf1f32978834274df85918caa78143c1e.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxCDMA2k_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifie

### RFmxCDMA2k_GetAttributeU32

Queries the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 *attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | uInt32 * | Returns the current value of the attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes.html language=enus -->
## TOPIC 00363: Set Attributes

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_SetAttributeF32Sets the value of an RFmx 32-bit floating point number (float32) attribute. RFmxCDMA2k_SetAttributeF32ArraySets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer fo

### Set Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_SetAttributeF32 | Sets the value of an RFmx 32-bit floating point number (float32) attribute. |
| RFmxCDMA2k_SetAttributeF32Array | Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeF64 | Sets the value of an RFmx 64-bit floating point number (float64) attribute. |
| RFmxCDMA2k_SetAttributeF64Array | Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeI16 | Sets the value of an RFmx 16-bit integer (int16) attribute. |
| RFmxCDMA2k_SetAttributeI32 | Sets the value of an RFmx 32-bit integer (int32) attribute. |
| RFmxCDMA2k_SetAttributeI32Array | Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeI64 | Sets the value of an RFmx 64-bit integer (int64) attribute. |
| RFmxCDMA2k_SetAttributeI64Array | Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeI8 | Sets the value of an RFmx 8-bit integer (int8) attribute. |
| RFmxCDMA2k_SetAttributeI8Array | Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeNIComplexDoubleArray | Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeNIComplexSingleArray | Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeString | Sets the value of an RFmx string attribute. |
| RFmxCDMA2k_SetAttributeU16 | Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. |
| RFmxCDMA2k_SetAttributeU32 | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. |
| RFmxCDMA2k_SetAttributeU32Array | Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeU64Array | Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |
| RFmxCDMA2k_SetAttributeU8 | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. |
| RFmxCDMA2k_SetAttributeU8Array | Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. |

#### Attachments

None

Parent topic:

Set and Get Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga1c19142c0a0b15623fbc4a397cce9fbf.html language=enus -->
## TOPIC 00364: RFmxCDMA2k_SetAttributeF64

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga1c19142c0a0b15623fbc4a397cce9fbf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga1c19142c0a0b15623fbc4a397cce9fbf.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdenti

### RFmxCDMA2k_SetAttributeF64

Sets the value of an RFmx 64-bit floating point number (float64) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga222f44b5d547dadfa3064384a5c55762.html language=enus -->
## TOPIC 00365: RFmxCDMA2k_SetAttributeU16

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga222f44b5d547dadfa3064384a5c55762.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga222f44b5d547dadfa3064384a5c55762.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies th

### RFmxCDMA2k_SetAttributeU16

Sets the value of an RFmx 16-bit unsigned integer (uInt16) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga26cc9c6beea257b76e2eddf27efb7d17.html language=enus -->
## TOPIC 00366: RFmxCDMA2k_SetAttributeU64Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga26cc9c6beea257b76e2eddf27efb7d17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga26cc9c6beea257b76e2eddf27efb7d17.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char se

### RFmxCDMA2k_SetAttributeU64Array

Sets the value of an RFmx 64-bit unsigned integer (uInt64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga2fecd1d4c8369f728d281a1545e5ee29.html language=enus -->
## TOPIC 00367: RFmxCDMA2k_SetAttributeI16

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga2fecd1d4c8369f728d281a1545e5ee29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga2fecd1d4c8369f728d281a1545e5ee29.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 16-bit integer (int16) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxCDMA2k_SetAttributeI16

Sets the value of an RFmx 16-bit integer (int16) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int16 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int16 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga33a2219d77e29c5ec151018a9883167b.html language=enus -->
## TOPIC 00368: RFmxCDMA2k_SetAttributeI8Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga33a2219d77e29c5ec151018a9883167b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga33a2219d77e29c5ec151018a9883167b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[

### RFmxCDMA2k_SetAttributeI8Array

Sets the value of an RFmx 8-bit integer (int8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga3935668f0c7b4b0f231991be0645739d.html language=enus -->
## TOPIC 00369: RFmxCDMA2k_SetAttributeU8Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga3935668f0c7b4b0f231991be0645739d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga3935668f0c7b4b0f231991be0645739d.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selec

### RFmxCDMA2k_SetAttributeU8Array

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga51000404d8aebeadb655e42ee732dddb.html language=enus -->
## TOPIC 00370: RFmxCDMA2k_SetAttributeString

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga51000404d8aebeadb655e42ee732dddb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga51000404d8aebeadb655e42ee732dddb.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx string attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session. You can

### RFmxCDMA2k_SetAttributeString

Sets the value of an RFmx string attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, char attrVal[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being set. Refer to the Selector String (C/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [out] | char[] | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga5209f5925ea34224ea99b09dfc58f26f.html language=enus -->
## TOPIC 00371: RFmxCDMA2k_SetAttributeU32

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga5209f5925ea34224ea99b09dfc58f26f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga5209f5925ea34224ea99b09dfc58f26f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies th

### RFmxCDMA2k_SetAttributeU32

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6b60c376a9a790591250e502097a43a9.html language=enus -->
## TOPIC 00372: RFmxCDMA2k_SetAttributeI32Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6b60c376a9a790591250e502097a43a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6b60c376a9a790591250e502097a43a9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorStri

### RFmxCDMA2k_SetAttributeI32Array

Sets the value of an RFmx 32-bit integer (int32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6c09174c9f3c94c0bab29c11c89299be.html language=enus -->
## TOPIC 00373: RFmxCDMA2k_SetAttributeF64Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6c09174c9f3c94c0bab29c11c89299be.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6c09174c9f3c94c0bab29c11c89299be.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, c

### RFmxCDMA2k_SetAttributeF64Array

Sets the value of an RFmx 64-bit floating point number (float64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6e34663aaf04ef1c7e13bc559fc4d556.html language=enus -->
## TOPIC 00374: RFmxCDMA2k_SetAttributeF32

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6e34663aaf04ef1c7e13bc559fc4d556.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga6e34663aaf04ef1c7e13bc559fc4d556.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdenti

### RFmxCDMA2k_SetAttributeF32

Sets the value of an RFmx 32-bit floating point number (float32) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga73ad38dc5be1024bba3714ede88e056f.html language=enus -->
## TOPIC 00375: RFmxCDMA2k_SetAttributeI64Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga73ad38dc5be1024bba3714ede88e056f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga73ad38dc5be1024bba3714ede88e056f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorStri

### RFmxCDMA2k_SetAttributeI64Array

Sets the value of an RFmx 64-bit integer (int64) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga8489ff01f09628463e8ae42037b8b5e1.html language=enus -->
## TOPIC 00376: RFmxCDMA2k_SetAttributeI64

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga8489ff01f09628463e8ae42037b8b5e1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1ga8489ff01f09628463e8ae42037b8b5e1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 64-bit integer (int64) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxCDMA2k_SetAttributeI64

Sets the value of an RFmx 64-bit integer (int64) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int64 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int64 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gaba01c176aec6e10180f8a6be454a4673.html language=enus -->
## TOPIC 00377: RFmxCDMA2k_SetAttributeNIComplexDoubleArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gaba01c176aec6e10180f8a6be454a4673.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gaba01c176aec6e10180f8a6be454a4673.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selecto

### RFmxCDMA2k_SetAttributeNIComplexDoubleArray

Sets the value of an RFmx NIComplexDouble attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexDouble attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexDouble[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gac61817153c1dd630eb7a6bf6c5b8761f.html language=enus -->
## TOPIC 00378: RFmxCDMA2k_SetAttributeF32Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gac61817153c1dd630eb7a6bf6c5b8761f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gac61817153c1dd630eb7a6bf6c5b8761f.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, c

### RFmxCDMA2k_SetAttributeF32Array

Sets the value of an RFmx 32-bit floating point number (float32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, float32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | float32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gad74a5c01cfdb06034716ba6f68575ae1.html language=enus -->
## TOPIC 00379: RFmxCDMA2k_SetAttributeU32Array

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gad74a5c01cfdb06034716ba6f68575ae1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gad74a5c01cfdb06034716ba6f68575ae1.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char se

### RFmxCDMA2k_SetAttributeU32Array

Sets the value of an RFmx 32-bit unsigned integer (uInt32) attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt32 attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt32[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gae32fd876043c1369937fefe466500926.html language=enus -->
## TOPIC 00380: RFmxCDMA2k_SetAttributeNIComplexSingleArray

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gae32fd876043c1369937fefe466500926.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gae32fd876043c1369937fefe466500926.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the arraySize parameter. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selecto

### RFmxCDMA2k_SetAttributeNIComplexSingleArray

Sets the value of an RFmx NIComplexSingle attribute. You must provide a char array to serve as a buffer for the value. Pass the number of bytes in the buffer as the **arraySize** parameter.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, NIComplexSingle attrVal[], int32 arraySize)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | NIComplexSingle[] | Pass the value to which you want to set the attribute. |
| arraySize | [in] | int32 | Specifies the size of the array. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gae9723c5cbfd4f4941eb311d68fc2e1f9.html language=enus -->
## TOPIC 00381: RFmxCDMA2k_SetAttributeI32

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gae9723c5cbfd4f4941eb311d68fc2e1f9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gae9723c5cbfd4f4941eb311d68fc2e1f9.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 32-bit integer (int32) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx sess

### RFmxCDMA2k_SetAttributeI32

Sets the value of an RFmx 32-bit integer (int32) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int32 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int32 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gaf4e46ab3d65112586542f573979c3188.html language=enus -->
## TOPIC 00382: RFmxCDMA2k_SetAttributeU8

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gaf4e46ab3d65112586542f573979c3188.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gaf4e46ab3d65112586542f573979c3188.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RF

### RFmxCDMA2k_SetAttributeU8

Sets the value of an RFmx 8-bit unsigned integer (uInt8) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, uInt8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | uInt8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gafde85f8c7524f6cb61b9f7c54e383283.html language=enus -->
## TOPIC 00383: RFmxCDMA2k_SetAttributeI8

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gafde85f8c7524f6cb61b9f7c54e383283.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__set__and__get__attributes__set__attributes_1gafde85f8c7524f6cb61b9f7c54e383283.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the value of an RFmx 8-bit integer (int8) attribute. Syntaxint32 __stdcall RFmxCDMA2k_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the RFmx session.

### RFmxCDMA2k_SetAttributeI8

Sets the value of an RFmx 8-bit integer (int8) attribute.

#### Syntax

int32 __stdcall RFmxCDMA2k_SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId, int8 attrVal)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Comprises the signal name. If you do not specify the signal name, the default signal instance is used.Example:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |
| attrVal | [in] | int8 | Pass the value to which you want to set the attribute |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Set Attributes

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility.html language=enus -->
## TOPIC 00384: Utility

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFmxCDMA2k_CheckMeasurementStatusChecks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. RFmxCDMA2k_CommitCommits settings to the

### Utility

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFmxCDMA2k_CheckMeasurementStatus | Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |
| RFmxCDMA2k_Commit | Commits settings to the hardware. Calling this function is optional. RFmxCDMA2k commits settings to the hardware when you call the RFmxCDMA2k_Initiate function. |
| RFmxCDMA2k_InitializeFromNIRFSASession | Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions. |
| RFmxCDMA2k_ResetAttribute | Resets an attribute that you specify in the attributeID parameter to default values. |
| RFmxCDMA2k_ResetToDefault | Resets a signal configuration to the default values. |
| RFmxCDMA2k_WaitForAcquisitionComplete | Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. |
| RFmxCDMA2k_WaitForMeasurementComplete | Waits for the specified number of seconds for all the measurements to complete. |

#### Attachments

None

Parent topic:

Functions

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga699206881009d1b60f6bcca67094847b.html language=enus -->
## TOPIC 00385: RFmxCDMA2k_ResetToDefault

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga699206881009d1b60f6bcca67094847b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga699206881009d1b60f6bcca67094847b.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal configuration to the default values. Syntaxint32 __stdcall RFmxCDMA2k_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis parameter specifies the RFmx session refnum. This parameter i

### RFmxCDMA2k_ResetToDefault

Resets a signal configuration to the default values.

#### Syntax

int32 __stdcall RFmxCDMA2k_ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga804e3506b0afde0c8c3cafbfeedb65f4.html language=enus -->
## TOPIC 00386: RFmxCDMA2k_WaitForAcquisitionComplete

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga804e3506b0afde0c8c3cafbfeedb65f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga804e3506b0afde0c8c3cafbfeedb65f4.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function. Syntaxint32 __stdcall RFmxCDMA2k_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)RemarksThis function is a wrapper over the RFmx Instru

### RFmxCDMA2k_WaitForAcquisitionComplete

Waits and blocks the data flow until the acquisition is done. This function is typically called after the specific Initiate function.

#### Syntax

int32 __stdcall RFmxCDMA2k_WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_WaitForAcquisitionComplete](/csh?context=rfmxinstr_rfmxinstrcref_function_wait_for_acquisition_complete) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| timeout | [in] | float64 | Specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga858864d703e6b57dded901c225b1fca5.html language=enus -->
## TOPIC 00387: RFmxCDMA2k_ResetAttribute

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga858864d703e6b57dded901c225b1fca5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1ga858864d703e6b57dded901c225b1fca5.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets an attribute that you specify in the attributeID parameter to default values. Syntaxint32 __stdcall RFmxCDMA2k_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleIdentifies the

### RFmxCDMA2k_ResetAttribute

Resets an attribute that you specify in the **attributeID** parameter to default values.

#### Syntax

int32 __stdcall RFmxCDMA2k_ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeId)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | Identifies the RFmx session. You can obtain this parameter from the RFmxCDMA2k_Initialize function. |
| selectorString | [in] | char[] | Specifies the selector string for the attribute being reset. Refer to the Selector String (C or LabWindows/CVI) topic for more information about configuring the selector string. |
| attributeId | [in] | int32 | Pass the ID of an attribute. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf7c9fdf6aef0565293dd90ab944fd89.html language=enus -->
## TOPIC 00388: RFmxCDMA2k_WaitForMeasurementComplete

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf7c9fdf6aef0565293dd90ab944fd89.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf7c9fdf6aef0565293dd90ab944fd89.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number of seconds for all the measurements to complete. Syntaxint32 __stdcall RFmxCDMA2k_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)ParametersNameDirectionTypeDescriptioninstrumentHandle[in]niRFmxInstrHandleThis param

### RFmxCDMA2k_WaitForMeasurementComplete

Waits for the specified number of seconds for all the measurements to complete.

#### Syntax

int32 __stdcall RFmxCDMA2k_WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| timeout | [in] | float64 | This parameter specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the function waits until the measurement is complete. The default value is 10. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf8366c2d65f4c5aa63a7f2a8a99e84a.html language=enus -->
## TOPIC 00389: RFmxCDMA2k_InitializeFromNIRFSASession

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf8366c2d65f4c5aa63a7f2a8a99e84a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gacf8366c2d65f4c5aa63a7f2a8a99e84a.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device

### RFmxCDMA2k_InitializeFromNIRFSASession

Creates an RFmx session from an existing NI-RFSA session. This function resets all the NI-RFSA attributes to their default values and stops export of all external signals and events. This function takes in an active NI-RFSA instrument handle and returns an RFmx Handle Out that identifies the device in all the subsequent RFmx functions.

#### Syntax

int32 __stdcall RFmxCDMA2k_InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle *handleOut)

#### Remarks

This function is a wrapper over the RFmx Instruments API, and calls the [RFmxInstr_InitializeFromNIRFSASession](/csh?context=rfmxinstr_rfmxinstrcref_function_initialize_from_nirfsa_session) function.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| nirfsaSession | [in] | uInt32 | Specifies the NIRFSA session handle of the device to initialize. |
| handleOut | [out] | niRFmxInstrHandle * | Returns an RFmx instrument session. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadb7605431716089d5430cd2bad652414.html language=enus -->
## TOPIC 00390: RFmxCDMA2k_CheckMeasurementStatus

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadb7605431716089d5430cd2bad652414.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadb7605431716089d5430cd2bad652414.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. Syntaxint32 __stdcall RFmxCDMA2k_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString

### RFmxCDMA2k_CheckMeasurementStatus

Checks the status of the measurement. Use this function to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

#### Syntax

int32 __stdcall RFmxCDMA2k_CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 *done)

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string).Examples:"""signal::sig1""result::r1""signal::sig1/result::r1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |
| done | [out] | int32 * | This parameter indicates whether the measurement is complete. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadc861bbb47d7f5e708244d9a66cded29.html language=enus -->
## TOPIC 00391: RFmxCDMA2k_Commit

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadc861bbb47d7f5e708244d9a66cded29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_c_d_m_a2k__functions__utility_1gadc861bbb47d7f5e708244d9a66cded29.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this function is optional. RFmxCDMA2k commits settings to the hardware when you call the RFmxCDMA2k_Initiate function. Syntaxint32 __stdcall RFmxCDMA2k_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])ParametersNameDirectionTypeDescriptionins

### RFmxCDMA2k_Commit

Commits settings to the hardware. Calling this function is optional. RFmxCDMA2k commits settings to the hardware when you call the [RFmxCDMA2k_Initiate](group____root__ni_r_fmx_c_d_m_a2k__functions_1gafb56460158bf0121f9bf319265307435.html) function.

#### Syntax

int32 __stdcall RFmxCDMA2k_Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| instrumentHandle | [in] | niRFmxInstrHandle | This parameter specifies the RFmx session refnum. This parameter is obtained from the RFmxInstr_Initialize function. |
| selectorString | [in] | char[] | This parameter specifies a Selector String comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).Examples:"""signal::sig1"You can use the RFmxCDMA2k_BuildSignalString function to build the selector string. |

#### Returns

Returns the status code of this operation. The status code either indicates success or describes an error or warning condition. Examine the status code from each call to an RFmx function to determine if an error has occurred.

To obtain a text description of the status code and additional information about the error condition, call the [RFmxCDMA2k_GetError](group____root__ni_r_fmx_c_d_m_a2k__functions_1gad9f4fb2c8324f0aadf0d2fc039c25aff.html) function.

The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive Values | Warnings |
| Negative Values | Errors |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-c-api-ref path=group__root__ni_r_fmx_c_d_m_a2k.html language=enus -->
## TOPIC 00392: niRFmxCDMA2k.h

- bundle_id: `rfmxcdma2k-c-api-ref`
- source_path: `group__root__ni_r_fmx_c_d_m_a2k.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-c-api-ref/raw/resource/enus/group__root__ni_r_fmx_c_d_m_a2k.html
- document_id: `rfmxcdma2k-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAttributesFunctionsGroup membersNoneAttachmentsNone

### niRFmxCDMA2k.h

#### Groups

- Attributes
- Functions

#### Group members

None

#### Attachments

None
