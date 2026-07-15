# NI DOCUMENT BUNDLE: rfmxspecan-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxspecan-c-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes.html language=enus -->
## TOPIC 00001: Attributes

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsACPAdvancedAMPMCCDFCHPDPDFCntHarmIDPDIMIQListNFOBWPAVTPhaseNoisePowerListSEMSpectrumSpurTriggerTXPGroup membersNameDescriptionRFMXSPECAN_ATTR_CENTER_FREQUENCYSpecifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer

### Attributes

#### Groups

- ACP
- Advanced
- AMPM
- CCDF
- CHP
- DPD
- FCnt
- Harm
- IDPD
- IM
- IQ
- List
- NF
- OBW
- PAVT
- PhaseNoise
- PowerList
- SEM
- Spectrum
- Spur
- Trigger
- TXP

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_CENTER_FREQUENCY | Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. |
| RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. |
| RFMXSPECAN_ATTR_REFERENCE_LEVEL | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. |
| RFMXSPECAN_ATTR_REFERENCE_LEVEL_HEADROOM | Specifies the margin RFmx adds to the RFMXSPECAN_ATTR_REFERENCE_LEVEL attribute. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. |
| RFMXSPECAN_ATTR_RESULT_FETCH_TIMEOUT | Specifies the time, in seconds, to wait before results are available in the RFmxSpecAn Attribute. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxSpecAn Attribute waits until the measurement is complete. |
| RFMXSPECAN_ATTR_SELECTED_PORTS | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. |

#### Attachments

None

Parent topic:

niRFmxSpecAn.h

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes_1ga36dd9f79b0dc54e7f5df3a96bbd75b3d.html language=enus -->
## TOPIC 00002: RFMXSPECAN_ATTR_SELECTED_PORTS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes_1ga36dd9f79b0dc54e7f5df3a96bbd75b3d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes_1ga36dd9f79b0dc54e7f5df3a96bbd75b3d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr_GetAvailablePorts function to get the valid port names. SyntaxRFMXSPECAN_ATTR_SELECTED_PORTSNumeric ValueData TypeAccessApplies To1052669char[]Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXSPECAN_ATTR_SELECTED_PORTS

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr_GetAvailablePorts](/csh?context=rfmxinstr_rfmxinstrcref_function_get_available_ports) function to get the valid port names.

#### Syntax

RFMXSPECAN_ATTR_SELECTED_PORTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052669 | char[] | Read/Write | N/A |

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

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes_1ga4cb262c24fad615157cf8eaf5bbb51df.html language=enus -->
## TOPIC 00003: RFMXSPECAN_ATTR_CENTER_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes_1ga4cb262c24fad615157cf8eaf5bbb51df.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes_1ga4cb262c24fad615157cf8eaf5bbb51df.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency. SyntaxRFMXSPECAN_ATTR_CENTER_FREQUENCYNumeric ValueData TypeAccessApplies To1048577float64Read/WriteN/ARemarks You do not need to use a sel

### RFMXSPECAN_ATTR_CENTER_FREQUENCY

Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

#### Syntax

RFMXSPECAN_ATTR_CENTER_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1048577 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default of this attribute is hardware dependent.

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp.html language=enus -->
## TOPIC 00004: ACP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedAveragingCarrierDetectorFFTNoise CalibrationNoise CompensationOffsetRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. RFMXSPECAN_ATTR_ACP_A

### ACP

#### Groups

- Advanced
- Averaging
- Carrier
- Detector
- FFT
- Noise Calibration
- Noise Compensation
- Offset
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. |
| RFMXSPECAN_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. |
| RFMXSPECAN_ATTR_ACP_MEASUREMENT_ENABLED | Specifies whether to enable the ACP measurement. |
| RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD | Specifies the method for performing the ACP measurement. |
| RFMXSPECAN_ATTR_ACP_MEASUREMENT_MODE | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. |
| RFMXSPECAN_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. |
| RFMXSPECAN_ATTR_ACP_POWER_UNITS | Specifies the units for the absolute power. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp_1ga60852779e54b8c98fd9b81ec32727edd.html language=enus -->
## TOPIC 00005: RFMXSPECAN_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp_1ga60852779e54b8c98fd9b81ec32727edd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp_1ga60852779e54b8c98fd9b81ec32727edd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRF

### RFMXSPECAN_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXSPECAN_ATTR_ACP_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052729 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_ACP_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp_1gacee8ed74bd254285ccc279245739affe.html language=enus -->
## TOPIC 00006: RFMXSPECAN_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp_1gacee8ed74bd254285ccc279245739affe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp_1gacee8ed74bd254285ccc279245739affe.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. SyntaxRFMXSPECAN_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1052692int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores

### RFMXSPECAN_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement.

#### Syntax

RFMXSPECAN_ATTR_ACP_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052692 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp_1gae1caacb1e0a2d8cb40bc401d1207efe8.html language=enus -->
## TOPIC 00007: RFMXSPECAN_ATTR_ACP_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp_1gae1caacb1e0a2d8cb40bc401d1207efe8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp_1gae1caacb1e0a2d8cb40bc401d1207efe8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ACP measurement. SyntaxRFMXSPECAN_ATTR_ACP_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1052672int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Str

### RFMXSPECAN_ATTR_ACP_MEASUREMENT_ENABLED

Specifies whether to enable the ACP measurement.

#### Syntax

RFMXSPECAN_ATTR_ACP_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052672 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__advanced.html language=enus -->
## TOPIC 00008: Advanced

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__advanced.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSETSpecifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_FAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set the RFMXSPECAN_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False. |
| RFMXSPECAN_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO | Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This attribute is used only if you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range. |
| RFMXSPECAN_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET | Specifies the offset by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set the RFMXSPECAN_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO attribute to False. |
| RFMXSPECAN_ATTR_ACP_SEQUENTIAL_FFT_SIZE | Specifies the FFT size when you set the. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__advanced_1gad22a7c573dee84345152b93ad914446b.html language=enus -->
## TOPIC 00009: RFMXSPECAN_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__advanced_1gad22a7c573dee84345152b93ad914446b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__advanced_1gad22a7c573dee84345152b93ad914446b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Dynamic Range and set

### RFMXSPECAN_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

Specifies the offset by which to adjust the IF output power level for offset channels that are near to the carrier channel to improve the dynamic range. This value is expressed in dB. This attribute is used only if you set the [RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__acp_1gaa55689a2b3f2cbad7e5e18c041cffb57.html) attribute to **Dynamic Range** and set the [RFMXSPECAN_ATTR_ACP_IF_OUTPUT_POWER_OFFSET_AUTO](group____root__ni_r_fmx_spec_an__attributes__acp__advanced_1ga85c70debc1d2e7c468cfaf8cf1c011d5.html) attribute to **False**.

#### Syntax

RFMXSPECAN_ATTR_ACP_NEAR_IF_OUTPUT_POWER_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052725 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 dB.

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__averaging_1ga12c8937dc9188684ec647f34e29a3f1f.html language=enus -->
## TOPIC 00010: RFMXSPECAN_ATTR_ACP_AVERAGING_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__averaging_1ga12c8937dc9188684ec647f34e29a3f1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__averaging_1ga12c8937dc9188684ec647f34e29a3f1f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. SyntaxRFMXSPECAN_ATTR_ACP_AVERAGING_TYPENumeric ValueData TypeAccessApplies To1052696int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read t

### RFMXSPECAN_ATTR_ACP_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

#### Syntax

RFMXSPECAN_ATTR_ACP_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052696 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_ACP_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_ACP_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_ACP_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXSPECAN_VAL_ACP_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_ACP_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1gabb8d8059e3f1c2b2808a0f1d4b1424bd.html language=enus -->
## TOPIC 00011: RFMXSPECAN_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1gabb8d8059e3f1c2b2808a0f1d4b1424bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1gabb8d8059e3f1c2b2808a0f1d4b1424bd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To1052677float64Read/WriteCarrierRemarks Use "carrier<n>" as the Selector String to configu

### RFMXSPECAN_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

Specifies the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_ACP_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052677 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1 MHz.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1gae61dc7c9d59faf3c498719bd92860669.html language=enus -->
## TOPIC 00012: RFMXSPECAN_ATTR_ACP_NUMBER_OF_CARRIERS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1gae61dc7c9d59faf3c498719bd92860669.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__carrier_1gae61dc7c9d59faf3c498719bd92860669.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of carriers. SyntaxRFMXSPECAN_ATTR_ACP_NUMBER_OF_CARRIERSNumeric ValueData TypeAccessApplies To1052674int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for in

### RFMXSPECAN_ATTR_ACP_NUMBER_OF_CARRIERS

Specifies the number of carriers.

#### Syntax

RFMXSPECAN_ATTR_ACP_NUMBER_OF_CARRIERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052674 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__carrier__rrc__filter_1ga2db87c7646758d4f27a95e916ab63fe4.html language=enus -->
## TOPIC 00013: RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__carrier__rrc__filter_1ga2db87c7646758d4f27a95e916ab63fe4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__carrier__rrc__filter_1ga2db87c7646758d4f27a95e916ab63fe4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power. SyntaxRFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ENABLEDNumeric ValueData TypeAccessApplies To1052678int32Read/WriteCarrierRemarks Use "carrier<n>" as the Selector S

### RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ENABLED

Specifies whether to apply the root-raised-cosine (RRC) filter on the acquired carrier channel before measuring the carrier channel power.

#### Syntax

RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052678 | int32 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_FALSE | 0 (0x0) | The channel power of the acquired carrier channel is measured directly. |
| RFMXSPECAN_VAL_ACP_CARRIER_RRC_FILTER_ENABLED_TRUE | 1 (0x1) | The measurement applies the RRC filter on the acquired carrier channel before measuring the carrier channel power. |

Parent topic:

RRC Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__carrier__rrc__filter_1gab1c9b7477343e36e02a7fbda0aed753f.html language=enus -->
## TOPIC 00014: RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ALPHA

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__carrier__rrc__filter_1gab1c9b7477343e36e02a7fbda0aed753f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__carrier__rrc__filter_1gab1c9b7477343e36e02a7fbda0aed753f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxRFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ALPHANumeric ValueData TypeAccessApplies To1052679float64Read/WriteCarrierRemarks Use "carrier<n>" as the Selector String to configure or read this attribute.The default value is 0.1.

### RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ALPHA

Specifies the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

RFMXSPECAN_ATTR_ACP_CARRIER_RRC_FILTER_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052679 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.1.

Parent topic:

RRC Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__detector.html language=enus -->
## TOPIC 00015: Detector

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__detector.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__detector.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_DETECTOR_POINTSSpecifies the number of trace points after the detector is applied. RFMXSPECAN_ATTR_ACP_DETECTOR_TYPESpecifies the type of detector to be used. AttachmentsNone

### Detector

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_DETECTOR_POINTS | Specifies the number of trace points after the detector is applied. |
| RFMXSPECAN_ATTR_ACP_DETECTOR_TYPE | Specifies the type of detector to be used. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__detector_1ga1984943928205843e483fb64fae090f1.html language=enus -->
## TOPIC 00016: RFMXSPECAN_ATTR_ACP_DETECTOR_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__detector_1ga1984943928205843e483fb64fae090f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__detector_1ga1984943928205843e483fb64fae090f1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of detector to be used. SyntaxRFMXSPECAN_ATTR_ACP_DETECTOR_TYPENumeric ValueData TypeAccessApplies To1052738int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic fo

### RFMXSPECAN_ATTR_ACP_DETECTOR_TYPE

Specifies the type of detector to be used.

#### Syntax

RFMXSPECAN_ATTR_ACP_DETECTOR_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052738 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **None**.

Refer to [Spectral Measurements Concepts](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/spectral-measurements-concepts.html) topic for more information on detector types.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_NONE | 0 (0x0) | The detector is disabled. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_SAMPLE | 1 (0x1) | The middle sample in the bucket is detected. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_NORMAL | 2 (0x2) | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_PEAK | 3 (0x3) | The maximum value of the samples in the bucket is detected. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_NEGATIVE_PEAK | 4 (0x4) | The minimum value of the samples in the bucket is detected. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_AVERAGE_RMS | 5 (0x5) | The average RMS of all the samples in the bucket is detected. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_AVERAGE_VOLTAGE | 6 (0x6) | The average voltage of all the samples in the bucket is detected. |
| RFMXSPECAN_VAL_ACP_DETECTOR_TYPE_AVERAGE_LOG | 7 (0x7) | The average log of all the samples in the bucket is detected. |

Parent topic:

Detector

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__detector_1ga71a4244e23a484397c081b2f2564dcf6.html language=enus -->
## TOPIC 00017: RFMXSPECAN_ATTR_ACP_DETECTOR_POINTS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__detector_1ga71a4244e23a484397c081b2f2564dcf6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__detector_1ga71a4244e23a484397c081b2f2564dcf6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of trace points after the detector is applied. SyntaxRFMXSPECAN_ATTR_ACP_DETECTOR_POINTSNumeric ValueData TypeAccessApplies To1052739int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to t

### RFMXSPECAN_ATTR_ACP_DETECTOR_POINTS

Specifies the number of trace points after the detector is applied.

#### Syntax

RFMXSPECAN_ATTR_ACP_DETECTOR_POINTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052739 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1001.

Parent topic:

Detector

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__fft.html language=enus -->
## TOPIC 00018: FFT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__fft.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_FFT_OVERLAPSpecifies the samples to overlap between the consecutive chunks as a percentage of the RFMXSPECAN_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute when you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT and the RF

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_FFT_OVERLAP | Specifies the samples to overlap between the consecutive chunks as a percentage of the RFMXSPECAN_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute when you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT and the RFMXSPECAN_ATTR_ACP_FFT_OVERLAP_MODE attribute to User Defined. This value is expressed as a percentage. |
| RFMXSPECAN_ATTR_ACP_FFT_OVERLAP_MODE | Specifies the overlap mode when you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT. |
| RFMXSPECAN_ATTR_ACP_FFT_PADDING | Specifies the factor by which the time-domain waveform is zero-padded before fast Fourier transform (FFT). The FFT size is given by the following formula: |
| RFMXSPECAN_ATTR_ACP_FFT_WINDOW | Specifies the FFT window type to use to reduce spectral leakage. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__fft_1ga143fb0426a57a20c5feaab047b71db6e.html language=enus -->
## TOPIC 00019: RFMXSPECAN_ATTR_ACP_FFT_WINDOW

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__fft_1ga143fb0426a57a20c5feaab047b71db6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__fft_1ga143fb0426a57a20c5feaab047b71db6e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type to use to reduce spectral leakage. SyntaxRFMXSPECAN_ATTR_ACP_FFT_WINDOWNumeric ValueData TypeAccessApplies To1052697int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selec

### RFMXSPECAN_ATTR_ACP_FFT_WINDOW

Specifies the FFT window type to use to reduce spectral leakage.

#### Syntax

RFMXSPECAN_ATTR_ACP_FFT_WINDOW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052697 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Flat Top**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_NONE | 0 (0x0) | Analyzes transients for which duration is shorter than the window length. You can also use this window type to separate two tones with frequencies close to each other but with almost equal amplitudes. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_FLAT_TOP | 1 (0x1) | Measures single-tone amplitudes accurately. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_HANNING | 2 (0x2) | Analyzes transients for which duration is longer than the window length. You can also use this window type to provide better frequency resolution for noise measurements. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_HAMMING | 3 (0x3) | Analyzes closely-spaced sine waves. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_GAUSSIAN | 4 (0x4) | Provides a good balance of spectral leakage, frequency resolution, and amplitude attenuation. Hence, this windowing is useful for time-frequency analysis. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_BLACKMAN | 5 (0x5) | Analyzes single tone because it has a low maximum side lobe level and a high side lobe roll-off rate. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_BLACKMAN_HARRIS | 6 (0x6) | Useful as a good general purpose window, having side lobe rejection greater than 90 dB and having a moderately wide main lobe. |
| RFMXSPECAN_VAL_ACP_FFT_WINDOW_KAISER_BESSEL | 7 (0x7) | Separates two tones with frequencies close to each other but with widely-differing amplitudes. |

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__fft_1gae58b63ed631bd1d064272ff6678724bf.html language=enus -->
## TOPIC 00020: RFMXSPECAN_ATTR_ACP_FFT_PADDING

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__fft_1gae58b63ed631bd1d064272ff6678724bf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__fft_1gae58b63ed631bd1d064272ff6678724bf.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the time-domain waveform is zero-padded before fast Fourier transform (FFT). The FFT size is given by the following formula: SyntaxRFMXSPECAN_ATTR_ACP_FFT_PADDINGNumeric ValueData TypeAccessApplies To1052698float64Read/WriteN/ARemarks waveform size * paddingThis attribu

### RFMXSPECAN_ATTR_ACP_FFT_PADDING

Specifies the factor by which the time-domain waveform is zero-padded before fast Fourier transform (FFT). The FFT size is given by the following formula:

#### Syntax

RFMXSPECAN_ATTR_ACP_FFT_PADDING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052698 | float64 | Read/Write | N/A |

#### Remarks

waveform size * padding

This attribute is used only when the acquisition span is less than the device instantaneous bandwidth of the device.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -1.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__fft_1gafab9f64d9097cb06bf6eae1339468211.html language=enus -->
## TOPIC 00021: RFMXSPECAN_ATTR_ACP_FFT_OVERLAP

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__fft_1gafab9f64d9097cb06bf6eae1339468211.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__fft_1gafab9f64d9097cb06bf6eae1339468211.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the samples to overlap between the consecutive chunks as a percentage of the RFMXSPECAN_ATTR_ACP_SEQUENTIAL_FFT_SIZE attribute when you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Sequential FFT and the RFMXSPECAN_ATTR_ACP_FFT_OVERLAP_MODE attribute to User Defined. This va

### RFMXSPECAN_ATTR_ACP_FFT_OVERLAP

Specifies the samples to overlap between the consecutive chunks as a percentage of the [RFMXSPECAN_ATTR_ACP_SEQUENTIAL_FFT_SIZE](group____root__ni_r_fmx_spec_an__attributes__acp__advanced_1ga4c42fbb825fcd6f59ad64e8c8f5325bb.html) attribute when you set the [RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__acp_1gaa55689a2b3f2cbad7e5e18c041cffb57.html) attribute to **Sequential FFT** and the [RFMXSPECAN_ATTR_ACP_FFT_OVERLAP_MODE](group____root__ni_r_fmx_spec_an__attributes__acp__fft_1ga3847d28714b5d8a74f805c72be19a5f2.html) attribute to **User Defined**. This value is expressed as a percentage.

#### Syntax

RFMXSPECAN_ATTR_ACP_FFT_OVERLAP

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052732 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__noise__calibration__averaging.html language=enus -->
## TOPIC 00022: Averaging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__noise__calibration__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__noise__calibration__averaging.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTOSpecifies whether RFmx automatically computes the averaging count used for instrument noise calibration. RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNTSpecifies the averaging count used for noise calibra

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. |
| RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT | Specifies the averaging count used for noise calibration when you set the RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO attribute to False. |

#### Attachments

None

Parent topic:

Noise Calibration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__noise__calibration__averaging_1gaeccaaafe2f408b3c886edce354b6fe38.html language=enus -->
## TOPIC 00023: RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__noise__calibration__averaging_1gaeccaaafe2f408b3c886edce354b6fe38.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__noise__calibration__averaging_1gaeccaaafe2f408b3c886edce354b6fe38.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. SyntaxRFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTONumeric ValueData TypeAccessApplies To1052736int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

#### Syntax

RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052736 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_FALSE | 0 (0x0) | RFmx uses the averages that you set for the RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_AVERAGING_COUNT attribute. |
| RFMXSPECAN_VAL_ACP_NOISE_CALIBRATION_AVERAGING_AUTO_TRUE | 1 (0x1) | When you set the RFMXSPECAN_ATTR_ACP_MEASUREMENT_METHOD attribute to Normal or Sequential FFT, RFmx uses a noise calibration averaging count of 32. When you set the ACP Meas Method attribute to Dynamic Range and the sweep time is less than 5 ms, RFmx uses a noise calibration averaging count of 15. When you set the ACP Meas Method attribute to Dynamic Range and the sweep time is greater than or equal to 5 ms, RFmx uses a noise calibration averaging count of 5. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__noise__compensation.html language=enus -->
## TOPIC 00024: Noise Compensation

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__noise__compensation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__noise__compensation.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_NOISE_COMPENSATION_ENABLEDSpecifies whether RFmx compensates for the instrument noise while performing the measurement when you set the RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_MODE attribute to Auto, or when you set the ACP Noise Cal Mode attri

### Noise Compensation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_NOISE_COMPENSATION_ENABLED | Specifies whether RFmx compensates for the instrument noise while performing the measurement when you set the RFMXSPECAN_ATTR_ACP_NOISE_CALIBRATION_MODE attribute to Auto, or when you set the ACP Noise Cal Mode attribute to Manual and RFMXSPECAN_ATTR_ACP_MEASUREMENT_MODE to Measure. Refer to the Noise Compensation Algorithm topic for more information. |
| RFMXSPECAN_ATTR_ACP_NOISE_COMPENSATION_TYPE | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__offset.html language=enus -->
## TOPIC 00025: Offset

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__offset.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__offset.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsPower ReferenceRRC FilterGroup membersNameDescriptionRFMXSPECAN_ATTR_ACP_NUMBER_OF_OFFSETSSpecifies the number of offset channels. RFMXSPECAN_ATTR_ACP_OFFSET_ENABLEDSpecifies whether to enable the offset channel for ACP measurement. RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCYSpecifies the center or e

### Offset

#### Groups

- Power Reference
- RRC Filter

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_ACP_NUMBER_OF_OFFSETS | Specifies the number of offset channels. |
| RFMXSPECAN_ATTR_ACP_OFFSET_ENABLED | Specifies whether to enable the offset channel for ACP measurement. |
| RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY | Specifies the center or edge frequency of the offset channel, relative to the center frequency of the closest carrier as determined by the RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY_DEFINITION attribute. This value is expressed in Hz. The sign of offset frequency is ignored and the RFMXSPECAN_ATTR_ACP_OFFSET_SIDEBAND attribute determines whether the upper, lower, or both offsets are measured. |
| RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY_DEFINITION | Specifies the offset frequency definition used to specify the RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY attribute. |
| RFMXSPECAN_ATTR_ACP_OFFSET_INTEGRATION_BANDWIDTH | Specifies the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_ACP_OFFSET_RELATIVE_ATTENUATION | Specifies the attenuation relative to the external attenuation specified by the RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION attribute. This value is expressed in dB. Use the ACP Offset Rel Attn attribute to compensate for variations in external attenuation when the offset channels are spread wide in frequency. |
| RFMXSPECAN_ATTR_ACP_OFFSET_SIDEBAND | Specifies whether the offset channel is present on one side, or on both sides of the carrier. |

#### Attachments

None

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__offset_1ga216d508bc572e4218fe28d1e90cbe82c.html language=enus -->
## TOPIC 00026: RFMXSPECAN_ATTR_ACP_OFFSET_RELATIVE_ATTENUATION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__offset_1ga216d508bc572e4218fe28d1e90cbe82c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__offset_1ga216d508bc572e4218fe28d1e90cbe82c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation relative to the external attenuation specified by the RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION attribute. This value is expressed in dB. Use the ACP Offset Rel Attn attribute to compensate for variations in external attenuation when the offset channels are spread wide in freque

### RFMXSPECAN_ATTR_ACP_OFFSET_RELATIVE_ATTENUATION

Specifies the attenuation relative to the external attenuation specified by the [RFMXSPECAN_ATTR_EXTERNAL_ATTENUATION](group____root__ni_r_fmx_spec_an__attributes_1gac9b3a86f36d174f69641a611fdf4a53b.html) attribute. This value is expressed in dB. Use the ACP Offset Rel Attn attribute to compensate for variations in external attenuation when the offset channels are spread wide in frequency.

#### Syntax

RFMXSPECAN_ATTR_ACP_OFFSET_RELATIVE_ATTENUATION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052687 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__acp__offset_1ga552a9a895e146b724843b36cf2a155b0.html language=enus -->
## TOPIC 00027: RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__acp__offset_1ga552a9a895e146b724843b36cf2a155b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__acp__offset_1ga552a9a895e146b724843b36cf2a155b0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the center or edge frequency of the offset channel, relative to the center frequency of the closest carrier as determined by the RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY_DEFINITION attribute. This value is expressed in Hz. The sign of offset frequency is ignored and the RFMXSPECAN_ATTR_ACP_OFF

### RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY

Specifies the center or edge frequency of the offset channel, relative to the center frequency of the closest carrier as determined by the [RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__acp__offset_1gad26a6e361128166feaaf27985e89c43d.html) attribute. This value is expressed in Hz. The sign of offset frequency is ignored and the [RFMXSPECAN_ATTR_ACP_OFFSET_SIDEBAND](group____root__ni_r_fmx_spec_an__attributes__acp__offset_1gaac04cda611acd756e611e56862f419fd.html) attribute determines whether the upper, lower, or both offsets are measured.

#### Syntax

RFMXSPECAN_ATTR_ACP_OFFSET_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052682 | float64 | Read/Write | Offset |

#### Remarks

Use "offset<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1 MHz.

Parent topic:

Offset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm_1gacc070646259769f942ccdc5b8e536952.html language=enus -->
## TOPIC 00028: RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm_1gacc070646259769f942ccdc5b8e536952.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm_1gacc070646259769f942ccdc5b8e536952.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference power used for AM to AM and AM to PM traces. SyntaxRFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPENumeric ValueData TypeAccessApplies To1105955int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Ref

### RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE

Specifies the reference power used for AM to AM and AM to PM traces.

#### Syntax

RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105955 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Input**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_REFERENCE_POWER_TYPE_INPUT | 0 (0x0) | The instantaneous powers at the input port of device under test (DUT) forms the x-axis of AM to AM and AM to PM traces. |
| RFMXSPECAN_VAL_AMPM_REFERENCE_POWER_TYPE_OUTPUT | 1 (0x1) | The instantaneous powers at the output port of DUT forms the x-axis of AM to AM and AM to PM traces. |

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__am__to__am__curve__fit_1ga79bf88e6fa212457d130929b6b1a076c.html language=enus -->
## TOPIC 00029: RFMXSPECAN_ATTR_AMPM_AM_TO_AM_CURVE_FIT_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__am__to__am__curve__fit_1ga79bf88e6fa212457d130929b6b1a076c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__am__to__am__curve__fit_1ga79bf88e6fa212457d130929b6b1a076c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic. SyntaxRFMXSPECAN_ATTR_AMPM_AM_TO_AM_CURVE_FIT_TYPENumeric ValueData TypeAccessApplies To1105923int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute

### RFMXSPECAN_ATTR_AMPM_AM_TO_AM_CURVE_FIT_TYPE

Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic.

#### Syntax

RFMXSPECAN_ATTR_AMPM_AM_TO_AM_CURVE_FIT_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105923 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Least Absolute Residual**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_AM_TO_AM_CURVE_FIT_TYPE_LEAST_SQUARE | 0 (0x0) | The measurement minimizes the energy of the polynomial approximation error. |
| RFMXSPECAN_VAL_AMPM_AM_TO_AM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL | 1 (0x1) | The measurement minimizes the magnitude of the polynomial approximation error. |
| RFMXSPECAN_VAL_AMPM_AM_TO_AM_CURVE_FIT_TYPE_BISQUARE | 2 (0x2) | The measurement excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

Parent topic:

AM to AM Curve Fit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__carrier.html language=enus -->
## TOPIC 00030: Carrier

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__carrier.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__carrier.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLEDSpecifies if auto detection of carrier offset and carrier bandwidth is enabled. RFMXSPECAN_ATTR_AMPM_CARRIER_BANDWIDTHSpecifies the carrier bandwidth when you set the RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_

### Carrier

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED | Specifies if auto detection of carrier offset and carrier bandwidth is enabled. |
| RFMXSPECAN_ATTR_AMPM_CARRIER_BANDWIDTH | Specifies the carrier bandwidth when you set the RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED attribute to False. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_AMPM_CARRIER_OFFSET | Specifies the carrier offset when you set the RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED attribute to False. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_AMPM_NUMBER_OF_CARRIERS | Specifies the number of carriers in the reference waveform when you set the RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED attribute to False. |

#### Attachments

None

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga718b7dec20bc5ee8d84a9d0fa1068783.html language=enus -->
## TOPIC 00031: RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga718b7dec20bc5ee8d84a9d0fa1068783.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga718b7dec20bc5ee8d84a9d0fa1068783.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if auto detection of carrier offset and carrier bandwidth is enabled. SyntaxRFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLEDNumeric ValueData TypeAccessApplies To1105963int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED

Specifies if auto detection of carrier offset and carrier bandwidth is enabled.

#### Syntax

RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105963 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_AUTO_CARRIER_DETECTION_ENABLED_FALSE | 0 (0x0) | Disables auto detection of carrier offset and carrier bandwidth. |
| RFMXSPECAN_VAL_AMPM_AUTO_CARRIER_DETECTION_ENABLED_TRUE | 1 (0x1) | Enables auto detection of carrier offset and carrier bandwidth. |

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga93fe5f9c8b22365d795e85f857fb4cbf.html language=enus -->
## TOPIC 00032: RFMXSPECAN_ATTR_AMPM_NUMBER_OF_CARRIERS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga93fe5f9c8b22365d795e85f857fb4cbf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga93fe5f9c8b22365d795e85f857fb4cbf.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of carriers in the reference waveform when you set the RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED attribute to False. SyntaxRFMXSPECAN_ATTR_AMPM_NUMBER_OF_CARRIERSNumeric ValueData TypeAccessApplies To1105964int32Read/WriteN/ARemarks You do not need to use a selector st

### RFMXSPECAN_ATTR_AMPM_NUMBER_OF_CARRIERS

Specifies the number of carriers in the reference waveform when you set the [RFMXSPECAN_ATTR_AMPM_AUTO_CARRIER_DETECTION_ENABLED](group____root__ni_r_fmx_spec_an__attributes__ampm__carrier_1ga718b7dec20bc5ee8d84a9d0fa1068783.html) attribute to **False**.

#### Syntax

RFMXSPECAN_ATTR_AMPM_NUMBER_OF_CARRIERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105964 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__compression__point__gain_1ga3a59240e8b385b969bf4695ab29a68c7.html language=enus -->
## TOPIC 00033: RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_GAIN_REFERENCE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__compression__point__gain_1ga3a59240e8b385b969bf4695ab29a68c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__compression__point__gain_1ga3a59240e8b385b969bf4695ab29a68c7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference power corresponding to the gain reference to be used for compression point calculation when you set the RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_GAIN_REFERENCE attribute to Reference Power. The reference power can be configured as either input or output power based on the value

### RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_GAIN_REFERENCE_POWER

Specifies the reference power corresponding to the gain reference to be used for compression point calculation when you set the [RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_GAIN_REFERENCE](group____root__ni_r_fmx_spec_an__attributes__ampm__compression__point__gain_1gafd93d4e4c304422cfc7cd3afc4bd14ab.html) attribute to **Reference Power**. The reference power can be configured as either input or output power based on the value of the [RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE](group____root__ni_r_fmx_spec_an__attributes__ampm_1gacc070646259769f942ccdc5b8e536952.html) attribute. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_AMPM_COMPRESSION_POINT_GAIN_REFERENCE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105973 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -20.

Parent topic:

Gain

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__equalizer_1ga10932df011572255398cf1e695f16881.html language=enus -->
## TOPIC 00034: RFMXSPECAN_ATTR_AMPM_EQUALIZER_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__equalizer_1ga10932df011572255398cf1e695f16881.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__equalizer_1ga10932df011572255398cf1e695f16881.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement equalizes the channel. SyntaxRFMXSPECAN_ATTR_AMPM_EQUALIZER_MODENumeric ValueData TypeAccessApplies To1105967int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector

### RFMXSPECAN_ATTR_AMPM_EQUALIZER_MODE

Specifies whether the measurement equalizes the channel.

#### Syntax

RFMXSPECAN_ATTR_AMPM_EQUALIZER_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105967 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Off**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_EQUALIZER_MODE_OFF | 0 (0x0) | Equalization is not performed. |
| RFMXSPECAN_VAL_AMPM_EQUALIZER_MODE_TRAIN | 1 (0x1) | The equalizer is turned on to compensate for the effect of the channel. |

Parent topic:

Equalizer

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__equalizer_1ga8d35d360963ac5dc38e493c4b3a7999e.html language=enus -->
## TOPIC 00035: RFMXSPECAN_ATTR_AMPM_EQUALIZER_FILTER_LENGTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__equalizer_1ga8d35d360963ac5dc38e493c4b3a7999e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__equalizer_1ga8d35d360963ac5dc38e493c4b3a7999e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the equalizer filter. The measurement maintains the filter length as an odd number by incrementing any even numbered value by one. SyntaxRFMXSPECAN_ATTR_AMPM_EQUALIZER_FILTER_LENGTHNumeric ValueData TypeAccessApplies To1105968int32Read/WriteN/ARemarks You do not need to use a

### RFMXSPECAN_ATTR_AMPM_EQUALIZER_FILTER_LENGTH

Specifies the length of the equalizer filter. The measurement maintains the filter length as an odd number by incrementing any even numbered value by one.

#### Syntax

RFMXSPECAN_ATTR_AMPM_EQUALIZER_FILTER_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105968 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 21.

Parent topic:

Equalizer

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__measurement__sample__rate_1gaa8b57e0e82460a7cee8481b13a91fe02.html language=enus -->
## TOPIC 00036: RFMXSPECAN_ATTR_AMPM_MEASUREMENT_SAMPLE_RATE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__measurement__sample__rate_1gaa8b57e0e82460a7cee8481b13a91fe02.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__measurement__sample__rate_1gaa8b57e0e82460a7cee8481b13a91fe02.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition sample rate when you set the RFMXSPECAN_ATTR_AMPM_MEASUREMENT_SAMPLE_RATE_MODE attribute to User. This value is expressed in samples per second (S/s). SyntaxRFMXSPECAN_ATTR_AMPM_MEASUREMENT_SAMPLE_RATENumeric ValueData TypeAccessApplies To1105932float64Read/WriteN/ARemarks

### RFMXSPECAN_ATTR_AMPM_MEASUREMENT_SAMPLE_RATE

Specifies the acquisition sample rate when you set the [RFMXSPECAN_ATTR_AMPM_MEASUREMENT_SAMPLE_RATE_MODE](group____root__ni_r_fmx_spec_an__attributes__ampm__measurement__sample__rate_1ga0918638770a2eb15e73d18f07cd90aa1.html) attribute to **User**. This value is expressed in samples per second (S/s).

#### Syntax

RFMXSPECAN_ATTR_AMPM_MEASUREMENT_SAMPLE_RATE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105932 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 120,000,000.

Parent topic:

Measurement Sample Rate

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__results.html language=enus -->
## TOPIC 00037: Results

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__results.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCompression PointGroup membersNameDescriptionRFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_COEFFICIENTSReturns the coefficients of the polynomial that approximates the measured AM-to-AM characteristic of the device under test. RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUALReturns t

### Results

#### Groups

- Compression Point

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_COEFFICIENTS | Returns the coefficients of the polynomial that approximates the measured AM-to-AM characteristic of the device under test. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUAL | Returns the approximation error of the polynomial approximation of the measured device under test AM-to-AM characteristic. This value is expressed in dB. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_PM_CURVE_FIT_COEFFICIENTS | Returns the coefficients of the polynomial that approximates the measured AM-to-PM characteristic of the device under test. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_PM_CURVE_FIT_RESIDUAL | Returns the approximation error of the polynomial approximation of the measured AM-to-PM characteristic of the device under test. This value is expressed in degrees. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_GAIN_ERROR_RANGE | Returns the peak-to-peak deviation of the device under test gain. This value is expressed in dB. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_LINEAR_GAIN | Returns the average linear gain of the device under test, computed by rejecting signal samples containing gain compression. This value is expressed in dB. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_PHASE_ERROR | Returns the mean phase error of the acquired signal relative to the reference waveform caused by the device under test. This value is expressed in degrees. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_RMS_EVM | Returns the ratio, as a percentage, of l2 norm of difference between the normalized reference and acquired waveforms, to the l2 norm of the normalized reference waveform. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_PEAK_REFERENCE_POWER | Returns the peak reference power. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_PEAK_REFERENCE_POWER_GAIN | Returns the gain at the peak reference power. This value is expressed in dB. |
| RFMXSPECAN_ATTR_AMPM_RESULTS_PHASE_ERROR_RANGE | Returns the peak-to-peak deviation of the phase distortion of the acquired signal relative to the reference waveform caused by the device under test. This value is expressed in degrees. |

#### Attachments

None

Parent topic:

AMPM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga23bc7cbf795baf4ba3870576c919a4fd.html language=enus -->
## TOPIC 00038: RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga23bc7cbf795baf4ba3870576c919a4fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga23bc7cbf795baf4ba3870576c919a4fd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the approximation error of the polynomial approximation of the measured device under test AM-to-AM characteristic. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUALNumeric ValueData TypeAccessApplies To1105945float64Read-OnlyN/ARemarks You do not n

### RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUAL

Returns the approximation error of the polynomial approximation of the measured device under test AM-to-AM characteristic. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_AM_CURVE_FIT_RESIDUAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105945 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga5cfca5f996378553a42ebee9af1602bd.html language=enus -->
## TOPIC 00039: RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_PM_CURVE_FIT_RESIDUAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga5cfca5f996378553a42ebee9af1602bd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga5cfca5f996378553a42ebee9af1602bd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the approximation error of the polynomial approximation of the measured AM-to-PM characteristic of the device under test. This value is expressed in degrees. SyntaxRFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_PM_CURVE_FIT_RESIDUALNumeric ValueData TypeAccessApplies To1105946float64Read-OnlyN/ARemarks

### RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_PM_CURVE_FIT_RESIDUAL

Returns the approximation error of the polynomial approximation of the measured AM-to-PM characteristic of the device under test. This value is expressed in degrees.

#### Syntax

RFMXSPECAN_ATTR_AMPM_RESULTS_AM_TO_PM_CURVE_FIT_RESIDUAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105946 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga5dd1ac490e37c48e608f0a40b94b8a28.html language=enus -->
## TOPIC 00040: RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_RMS_EVM

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga5dd1ac490e37c48e608f0a40b94b8a28.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga5dd1ac490e37c48e608f0a40b94b8a28.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the ratio, as a percentage, of l^2 norm of difference between the normalized reference and acquired waveforms, to the l^2 norm of the normalized reference waveform. SyntaxRFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_RMS_EVMNumeric ValueData TypeAccessApplies To1105944float64Read-OnlyN/ARemarks You do n

### RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_RMS_EVM

Returns the ratio, as a percentage, of l<sup>2</sup> norm of difference between the normalized reference and acquired waveforms, to the l<sup>2</sup> norm of the normalized reference waveform.

#### Syntax

RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_RMS_EVM

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105944 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga788cc5c26de5e82d01966d1bfe125347.html language=enus -->
## TOPIC 00041: RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_PHASE_ERROR

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga788cc5c26de5e82d01966d1bfe125347.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__results_1ga788cc5c26de5e82d01966d1bfe125347.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean phase error of the acquired signal relative to the reference waveform caused by the device under test. This value is expressed in degrees. SyntaxRFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_PHASE_ERRORNumeric ValueData TypeAccessApplies To1105943float64Read-OnlyN/ARemarks You do not need to us

### RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_PHASE_ERROR

Returns the mean phase error of the acquired signal relative to the reference waveform caused by the device under test. This value is expressed in degrees.

#### Syntax

RFMXSPECAN_ATTR_AMPM_RESULTS_MEAN_PHASE_ERROR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105943 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1ga9ffb9a1e42359b14537f9210dabb22b4.html language=enus -->
## TOPIC 00042: RFMXSPECAN_ATTR_AMPM_THRESHOLD_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1ga9ffb9a1e42359b14537f9210dabb22b4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1ga9ffb9a1e42359b14537f9210dabb22b4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the definition to use for thresholding acquired and reference waveform. SyntaxRFMXSPECAN_ATTR_AMPM_THRESHOLD_DEFINITIONNumeric ValueData TypeAccessApplies To1105980int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal

### RFMXSPECAN_ATTR_AMPM_THRESHOLD_DEFINITION

Specifies the definition to use for thresholding acquired and reference waveform.

#### Syntax

RFMXSPECAN_ATTR_AMPM_THRESHOLD_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105980 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Reference Power Type**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_DEFINITION_INPUT_AND_OUTPUT | 0 (0x0) | Corresponding acquired and reference waveform samples are used for AMPM measurement when both samples are greater or equal to the threshold level. |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_DEFINITION_REFERENCE_POWER_TYPE | 1 (0x1) | Corresponding acquired and reference waveform samples are used for AMPM measurement when reference waveform sample is greater than or equal to the threshold level and RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE attribute is set to Input. Corresponding acquired and reference waveform samples are used for AMPM measurement when acquired waveform sample is greater than or equal to the threshold level and RFMXSPECAN_ATTR_AMPM_REFERENCE_POWER_TYPE attribute is set to Output. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1gac81edd7ed2c3b08cb63ac56a06344f19.html language=enus -->
## TOPIC 00043: RFMXSPECAN_ATTR_AMPM_THRESHOLD_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1gac81edd7ed2c3b08cb63ac56a06344f19.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1gac81edd7ed2c3b08cb63ac56a06344f19.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxRFMXSPECAN_ATTR_AMPM_THRESHOLD_TYPENumeric ValueData TypeAccessApplies To1105934int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to th

### RFMXSPECAN_ATTR_AMPM_THRESHOLD_TYPE

Specifies the reference for the power level used for thresholding.

#### Syntax

RFMXSPECAN_ATTR_AMPM_THRESHOLD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105934 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_TYPE_RELATIVE | 0 (0x0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_TYPE_ABSOLUTE | 1 (0x1) | The threshold is the absolute power, in dBm. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1gafb12dab3f7b625984443ca3c40111115.html language=enus -->
## TOPIC 00044: RFMXSPECAN_ATTR_AMPM_THRESHOLD_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1gafb12dab3f7b625984443ca3c40111115.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ampm__threshold_1gafb12dab3f7b625984443ca3c40111115.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable thresholding of the acquired samples used for the AMPM measurement. SyntaxRFMXSPECAN_ATTR_AMPM_THRESHOLD_ENABLEDNumeric ValueData TypeAccessApplies To1105933int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXSPECAN_ATTR_AMPM_THRESHOLD_ENABLED

Specifies whether to enable thresholding of the acquired samples used for the AMPM measurement.

#### Syntax

RFMXSPECAN_ATTR_AMPM_THRESHOLD_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1105933 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_FALSE | 0 (0x0) | All samples are considered for the AMPM measurement. |
| RFMXSPECAN_VAL_AMPM_THRESHOLD_ENABLED_TRUE | 1 (0x1) | Samples above the threshold level specified in the RFMXSPECAN_ATTR_AMPM_THRESHOLD_LEVEL attribute are considered for the AMPM measurement. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf_1ga42c826145eb44ad8d0005ae1139c32fd.html language=enus -->
## TOPIC 00045: RFMXSPECAN_ATTR_CCDF_NUMBER_OF_RECORDS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf_1ga42c826145eb44ad8d0005ae1139c32fd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf_1ga42c826145eb44ad8d0005ae1139c32fd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for the CCDF measurement. SyntaxRFMXSPECAN_ATTR_CCDF_NUMBER_OF_RECORDSNumeric ValueData TypeAccessApplies To1056772int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer t

### RFMXSPECAN_ATTR_CCDF_NUMBER_OF_RECORDS

Specifies the number of acquisitions used for the CCDF measurement.

#### Syntax

RFMXSPECAN_ATTR_CCDF_NUMBER_OF_RECORDS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056772 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

CCDF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf_1gaa1f354a31f9a510a62788e4bfeac03fe.html language=enus -->
## TOPIC 00046: RFMXSPECAN_ATTR_CCDF_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf_1gaa1f354a31f9a510a62788e4bfeac03fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf_1gaa1f354a31f9a510a62788e4bfeac03fe.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the CCDF measurement. SyntaxRFMXSPECAN_ATTR_CCDF_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1056768int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector S

### RFMXSPECAN_ATTR_CCDF_MEASUREMENT_ENABLED

Specifies whether to enable the CCDF measurement.

#### Syntax

RFMXSPECAN_ATTR_CCDF_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056768 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

CCDF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf__rbw__filter_1gaae99795c17bf39269399634ef8137fbb.html language=enus -->
## TOPIC 00047: RFMXSPECAN_ATTR_CCDF_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf__rbw__filter_1gaae99795c17bf39269399634ef8137fbb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf__rbw__filter_1gaae99795c17bf39269399634ef8137fbb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_CCDF_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To1056775float64Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXSPECAN_ATTR_CCDF_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_CCDF_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056775 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 100 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf__results.html language=enus -->
## TOPIC 00048: Results

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf__results.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWERReturns the average power of all the samples. This value is expressed in dBm. If you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to True, samples above the threshold are measured. RFMXSPECAN_ATTR_CCDF_RESULTS_M

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER | Returns the average power of all the samples. This value is expressed in dBm. If you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to True, samples above the threshold are measured. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILE | Returns the percentage of samples that have more power than the mean power. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_MEASURED_SAMPLES_COUNT | Returns the total number of samples measured. The total number of samples includes only the samples above the threshold, when you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_HUNDREDTH_PERCENT_POWER | Returns the power above the mean power, over which 0.01% of the total samples in the signal are present. This value is expressed in dB. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_PERCENT_POWER | Returns the power above the mean power, over which 1% of the total samples in the signal are present. This value is expressed in dB. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_TENTH_PERCENT_POWER | Returns the power above the mean power, over which 0.1% of the total samples in the signal are present. This value is expressed in dB. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_TEN_THOUSANDTH_PERCENT_POWER | Returns the power above the mean power, over which 0.0001% of the total samples in the signal are present. This value is expressed in dB. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_THOUSANDTH_PERCENT_POWER | Returns the power above the mean power, over which 0.001% of the total samples in the signal are present. This value is expressed in dB. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_PEAK_POWER | Returns the peak power of the acquired signal, relative to the mean power. |
| RFMXSPECAN_ATTR_CCDF_RESULTS_TEN_PERCENT_POWER | Returns the power above the mean power, over which 10% of the total samples in the signal are present. This value is expressed in dB. |

#### Attachments

None

Parent topic:

CCDF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1ga47f7b58e0b658aaa57b802dbe7ee0138.html language=enus -->
## TOPIC 00049: RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1ga47f7b58e0b658aaa57b802dbe7ee0138.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1ga47f7b58e0b658aaa57b802dbe7ee0138.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the percentage of samples that have more power than the mean power. SyntaxRFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILENumeric ValueData TypeAccessApplies To1056783float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result insta

### RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILE

Returns the percentage of samples that have more power than the mean power.

#### Syntax

RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER_PERCENTILE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056783 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1ga61293216b3f308eaae4990aa94da5f54.html language=enus -->
## TOPIC 00050: RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1ga61293216b3f308eaae4990aa94da5f54.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1ga61293216b3f308eaae4990aa94da5f54.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of all the samples. This value is expressed in dBm. If you set the RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED attribute to True, samples above the threshold are measured. SyntaxRFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWERNumeric ValueData TypeAccessApplies To1056782float64Read-OnlyN

### RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER

Returns the average power of all the samples. This value is expressed in dBm. If you set the [RFMXSPECAN_ATTR_CCDF_THRESHOLD_ENABLED](group____root__ni_r_fmx_spec_an__attributes__ccdf__threshold_1ga2785c66bc2247109d9af863362cd85e0.html) attribute to **True**, samples above the threshold are measured.

#### Syntax

RFMXSPECAN_ATTR_CCDF_RESULTS_MEAN_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056782 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1gad03e97ebcac435e8796c74839073bdc4.html language=enus -->
## TOPIC 00051: RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_THOUSANDTH_PERCENT_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1gad03e97ebcac435e8796c74839073bdc4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf__results_1gad03e97ebcac435e8796c74839073bdc4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power above the mean power, over which 0.001% of the total samples in the signal are present. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_CCDF_RESULTS_ONE_THOUSANDTH_PERCENT_POWERNumeric ValueData TypeAccessApplies To1056788float64Read-OnlyN/ARemarks You do not need to use a sel

### RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_THOUSANDTH_PERCENT_POWER

Returns the power above the mean power, over which 0.001% of the total samples in the signal are present. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_CCDF_RESULTS_ONE_THOUSANDTH_PERCENT_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056788 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__ccdf__threshold_1ga3f811be32c75cd9214f4560f7d2c6814.html language=enus -->
## TOPIC 00052: RFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__ccdf__threshold_1ga3f811be32c75cd9214f4560f7d2c6814.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__ccdf__threshold_1ga3f811be32c75cd9214f4560f7d2c6814.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxRFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPENumeric ValueData TypeAccessApplies To1056779int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to th

### RFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPE

Specifies the reference for the power level used for thresholding.

#### Syntax

RFMXSPECAN_ATTR_CCDF_THRESHOLD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1056779 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_RELATIVE | 0 (0x0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_CCDF_THRESHOLD_TYPE_ABSOLUTE | 1 (0x1) | The threshold is the absolute power, in dBm. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__carrier_1ga820821b0e57ea6efa364f7f8b96a7e44.html language=enus -->
## TOPIC 00053: RFMXSPECAN_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__carrier_1ga820821b0e57ea6efa364f7f8b96a7e44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__carrier_1ga820821b0e57ea6efa364f7f8b96a7e44.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency range, over which the measurement integrates the power. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To1060866float64Read/WriteCarrierRemarks Use "carrier<n>" as the Selector String to configure or r

### RFMXSPECAN_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

Specifies the frequency range, over which the measurement integrates the power. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_CHP_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060866 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1 MHz.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__carrier_1gaedbb47033fdbad87e617941e4e20543e.html language=enus -->
## TOPIC 00054: RFMXSPECAN_ATTR_CHP_NUMBER_OF_CARRIERS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__carrier_1gaedbb47033fdbad87e617941e4e20543e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__carrier_1gaedbb47033fdbad87e617941e4e20543e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of carriers. SyntaxRFMXSPECAN_ATTR_CHP_NUMBER_OF_CARRIERSNumeric ValueData TypeAccessApplies To1060888int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for in

### RFMXSPECAN_ATTR_CHP_NUMBER_OF_CARRIERS

Specifies the number of carriers.

#### Syntax

RFMXSPECAN_ATTR_CHP_NUMBER_OF_CARRIERS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060888 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__carrier__rrc__filter_1ga844f852bcf9c64928ecdf3663340de48.html language=enus -->
## TOPIC 00055: RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ALPHA

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__carrier__rrc__filter_1ga844f852bcf9c64928ecdf3663340de48.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__carrier__rrc__filter_1ga844f852bcf9c64928ecdf3663340de48.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor of the root-raised-cosine (RRC) filter. SyntaxRFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ALPHANumeric ValueData TypeAccessApplies To1060880float64Read/WriteCarrierRemarks Use "carrier<n>" as the Selector String to configure or read this attribute.The default value is 0.1.

### RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ALPHA

Specifies the roll-off factor of the root-raised-cosine (RRC) filter.

#### Syntax

RFMXSPECAN_ATTR_CHP_CARRIER_RRC_FILTER_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060880 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.1.

Parent topic:

RRC Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__noise__calibration_1ga2c4bf33eb942c4963dfe6a360373c347.html language=enus -->
## TOPIC 00056: RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__noise__calibration_1ga2c4bf33eb942c4963dfe6a360373c347.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__noise__calibration_1ga2c4bf33eb942c4963dfe6a360373c347.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. SyntaxRFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODENumeric ValueData TypeAccess

### RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE

Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/noise-compensation-algorithm.html) topic for more information.

#### Syntax

RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060901 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_MODE_MANUAL | 0 (0x0) | When you set the RFMXSPECAN_ATTR_CHP_MEASUREMENT_MODE attribute to Calibrate Noise Floor, you can initiate instrument noise calibration for the CHP measurement manually. When you set the CHP Meas Mode attribute to Measure, you can initiate the CHP measurement manually. |
| RFMXSPECAN_VAL_CHP_NOISE_CALIBRATION_MODE_AUTO | 1 (0x1) | When you set the RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED attribute to True, RFmx sets RFMXINSTR_ATTR_INPUT_ISOLATION_ENABLED to Enabled and calibrates the intrument noise in the current state of the instrument. RFmx then resets the Input Isolation Enabled attribute and performs the CHP measurement, including compensation for noise of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set the CHP Noise Comp Enabled attribute to False, RFmx does not calibrate instrument noise and performs only the CHP measurement without compensating for the noise contribution of the instrument. |

Parent topic:

Noise Calibration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__noise__compensation.html language=enus -->
## TOPIC 00057: Noise Compensation

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__noise__compensation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__noise__compensation.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLEDSpecifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE at

### Noise Compensation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE attribute to Auto, or set the CHP Noise Cal Mode attribute to Manual and RFMXSPECAN_ATTR_CHP_MEASUREMENT_MODE attribute to Measure. |
| RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_TYPE | Specifies the noise compensation type. Refer to the Noise Compensation Algorithm topic for more information. |

#### Attachments

None

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__noise__compensation_1gaf24cdc491fa21dc826dc6eebdb86fa71.html language=enus -->
## TOPIC 00058: RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__noise__compensation_1gaf24cdc491fa21dc826dc6eebdb86fa71.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__noise__compensation_1gaf24cdc491fa21dc826dc6eebdb86fa71.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE attribute to Auto, or set the CHP Noise Cal Mode attribute to Manual and RFMXSPECAN_AT

### RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED

Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the [RFMXSPECAN_ATTR_CHP_NOISE_CALIBRATION_MODE](group____root__ni_r_fmx_spec_an__attributes__chp__noise__calibration_1ga2c4bf33eb942c4963dfe6a360373c347.html) attribute to **Auto**, or set the CHP Noise Cal Mode attribute to **Manual** and [RFMXSPECAN_ATTR_CHP_MEASUREMENT_MODE](group____root__ni_r_fmx_spec_an__attributes__chp_1gaac411a95778c5a33f2fa5eadfffe3e67.html) attribute to **Measure**.

#### Syntax

RFMXSPECAN_ATTR_CHP_NOISE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060897 | int32 | Read/Write | N/A |

#### Remarks

Refer to the measurement guidelines section in the [Noise Compensation Algorithm](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/noise-compensation-algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables noise compensation. |
| RFMXSPECAN_VAL_CHP_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables noise compensation. |

Parent topic:

Noise Compensation

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga0181596f362dac5e6117faf269ba585f.html language=enus -->
## TOPIC 00059: RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga0181596f362dac5e6117faf269ba585f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga0181596f362dac5e6117faf269ba585f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital resolution bandwidth (RBW) filter. SyntaxRFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To1060878int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to

### RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE

Specifies the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060878 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FFT_BASED | 0 (0x0) | No RBW filtering is performed. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | An RBW filter with a Gaussian response is applied. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_TYPE_FLAT | 2 (0x2) | An RBW filter with a flat response is applied. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2e43a9b6886adbf10b7cf98da540aae7.html language=enus -->
## TOPIC 00060: RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2e43a9b6886adbf10b7cf98da540aae7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2e43a9b6886adbf10b7cf98da540aae7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To10

### RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the [RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1gafccb6e42b6b5052d1761d2811ecf42b5.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060877 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2ed160a0a64706348d32a839e570d261.html language=enus -->
## TOPIC 00061: RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2ed160a0a64706348d32a839e570d261.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2ed160a0a64706348d32a839e570d261.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth definition that you use to specify the value of the RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. SyntaxRFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH_DEFINITIONNumeric ValueData TypeAccessApplies To1060894int32Read/WriteN/ARemarks The default value is 3dB.NameValueDescriptio

### RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH_DEFINITION

Specifies the bandwidth definition that you use to specify the value of the [RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1ga2e43a9b6886adbf10b7cf98da540aae7.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060894 | int32 | Read/Write | N/A |

#### Remarks

The default value is **3dB**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_3DB | 0 (0x0) | Defines the RBW in terms of the 3 dB bandwidth of the RBW filter. When you set the RFMXSPECAN_ATTR_CHP_RBW_FILTER_TYPE attribute to FFT Based, RBW is the 3 dB bandwidth of the window specified by the RFMXSPECAN_ATTR_CHP_FFT_WINDOW attribute. |
| RFMXSPECAN_VAL_CHP_RBW_FILTER_BANDWIDTH_DEFINITION_BIN_WIDTH | 2 (0x2) | Defines the RBW in terms of the spectrum bin width computed using an FFT when you set the CHP RBW Filter Type attribute to FFT Based. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1gafccb6e42b6b5052d1761d2811ecf42b5.html language=enus -->
## TOPIC 00062: RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1gafccb6e42b6b5052d1761d2811ecf42b5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__rbw__filter_1gafccb6e42b6b5052d1761d2811ecf42b5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the resolution bandwidth (RBW). SyntaxRFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To1060876int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the resolution bandwidth (RBW).

#### Syntax

RFMXSPECAN_ATTR_CHP_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060876 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CHP_RBW_AUTO_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_CHP_RBW_AUTO_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__results__carrier_1ga3e9ead9044dba8d30c0bfe45bd549003.html language=enus -->
## TOPIC 00063: RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__results__carrier_1ga3e9ead9044dba8d30c0bfe45bd549003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__results__carrier_1ga3e9ead9044dba8d30c0bfe45bd549003.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power measured relative to the total carrier power of all carriers. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWERNumeric ValueData TypeAccessApplies To1060893float64Read-OnlyCarrierRemarks Use "carrier<n>" as the Selector String to read t

### RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER

Returns the carrier power measured relative to the total carrier power of all carriers. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060893 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__results__carrier_1gaebde5a49473612c05018eb5bb4579998.html language=enus -->
## TOPIC 00064: RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__results__carrier_1gaebde5a49473612c05018eb5bb4579998.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__results__carrier_1gaebde5a49473612c05018eb5bb4579998.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_INTEGRATION_BANDWIDTHNumeric ValueData TypeAccessApplies To1060892float64Read-OnlyCarrierRemarks Use "carrier<n>" as the Selector String to re

### RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_CHP_RESULTS_CARRIER_INTEGRATION_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060892 | float64 | Read-Only | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Carrier

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__chp__sweep__time_1ga0353a2ce0800b0ad6446b4ad65ecbc87.html language=enus -->
## TOPIC 00065: RFMXSPECAN_ATTR_CHP_SWEEP_TIME_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__chp__sweep__time_1ga0353a2ce0800b0ad6446b4ad65ecbc87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__chp__sweep__time_1ga0353a2ce0800b0ad6446b4ad65ecbc87.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXSPECAN_ATTR_CHP_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To1060881int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXSPECAN_ATTR_CHP_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXSPECAN_ATTR_CHP_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1060881 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_CHP_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_CHP_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_CHP_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_CHP_RBW_FILTER_BANDWIDTH attribute. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd_1ga0f9b12dad444d77c68f0a668db2b7772.html language=enus -->
## TOPIC 00066: RFMXSPECAN_ATTR_DPD_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd_1ga0f9b12dad444d77c68f0a668db2b7772.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd_1ga0f9b12dad444d77c68f0a668db2b7772.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism of the DPD measurement. SyntaxRFMXSPECAN_ATTR_DPD_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1110048int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. However, the number

### RFMXSPECAN_ATTR_DPD_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism of the DPD measurement.

#### Syntax

RFMXSPECAN_ATTR_DPD_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110048 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. However, the number of threads you set may not all be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd_1ga397107843e53544fb12fbffedbba4892.html language=enus -->
## TOPIC 00067: RFMXSPECAN_ATTR_DPD_MEASUREMENT_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd_1ga397107843e53544fb12fbffedbba4892.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd_1ga397107843e53544fb12fbffedbba4892.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the training waveform required for the extraction of the DPD model coefficients is acquired from the hardware or is configured by the user. SyntaxRFMXSPECAN_ATTR_DPD_MEASUREMENT_MODENumeric ValueData TypeAccessApplies To1110123int32Read/WriteN/ARemarks You do not need to use a selector

### RFMXSPECAN_ATTR_DPD_MEASUREMENT_MODE

Specifies if the training waveform required for the extraction of the DPD model coefficients is acquired from the hardware or is configured by the user.

#### Syntax

RFMXSPECAN_ATTR_DPD_MEASUREMENT_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110123 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Acquire and Extract**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_MEASUREMENT_MODE_ACQUIRE_AND_EXTRACT | 0 (0x0) | The measurement acquires the training waveform required for the extraction of the DPD model coefficients from the hardware and then computes the model coefficients. In this mode, the supported RFMXSPECAN_ATTR_DPD_MODEL are Lookup Table, Memory Polynomial , and Generalized Memory Polynomial. |
| RFMXSPECAN_VAL_DPD_MEASUREMENT_MODE_EXTRACT_ONLY | 1 (0x1) | The measurement uses the user configured training waveform required for the extraction of the DPD model coefficients. In this mode, the only supported RFMXSPECAN_ATTR_DPD_MODEL is Decomposed Vector Rotation. |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd_1ga3b9abb97c1fba5586569ceb507261686.html language=enus -->
## TOPIC 00068: RFMXSPECAN_ATTR_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd_1ga3b9abb97c1fba5586569ceb507261686.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd_1ga3b9abb97c1fba5586569ceb507261686.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the IQ origin offset correction for the measurement. SyntaxRFMXSPECAN_ATTR_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To1110117int32Read/WriteN/ARemarks When you set this attribute to True, the measurement computes and corrects any origin offset between the re

### RFMXSPECAN_ATTR_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED

Enables the IQ origin offset correction for the measurement.

#### Syntax

RFMXSPECAN_ATTR_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110117 | int32 | Read/Write | N/A |

#### Remarks

When you set this attribute to **True**, the measurement computes and corrects any origin offset between the reference and the acquired waveforms. When you set this attribute to **False**, origin offset correction is not performed.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_FALSE | 0 (0x0) | Disables IQ origin offset correction. |
| RFMXSPECAN_VAL_DPD_IQ_ORIGIN_OFFSET_CORRECTION_ENABLED_TRUE | 1 (0x1) | Enables IQ origin offset correction. |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd_1ga50c1336818cfd6e2d3ec533076b2f539.html language=enus -->
## TOPIC 00069: RFMXSPECAN_ATTR_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd_1ga50c1336818cfd6e2d3ec533076b2f539.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd_1ga50c1336818cfd6e2d3ec533076b2f539.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable frequency offset correction for the DPD measurement. SyntaxRFMXSPECAN_ATTR_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To1110073int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the de

### RFMXSPECAN_ATTR_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED

Specifies whether to enable frequency offset correction for the DPD measurement.

#### Syntax

RFMXSPECAN_ATTR_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110073 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_FALSE | 0 (0x0) | The measurement computes and corrects any frequency offset between the reference and the acquired waveforms. |
| RFMXSPECAN_VAL_DPD_FREQUENCY_OFFSET_CORRECTION_ENABLED_TRUE | 1 (0x1) | The measurement does not perform frequency offset correction. |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd_1ga6776c83367493cab6a8a8420106110b2.html language=enus -->
## TOPIC 00070: RFMXSPECAN_ATTR_DPD_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd_1ga6776c83367493cab6a8a8420106110b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd_1ga6776c83367493cab6a8a8420106110b2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable DPD measurement. SyntaxRFMXSPECAN_ATTR_DPD_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1110016int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String

### RFMXSPECAN_ATTR_DPD_MEASUREMENT_ENABLED

Specifies whether to enable DPD measurement.

#### Syntax

RFMXSPECAN_ATTR_DPD_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110016 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd_1gae3c48c765820d7c94a5ba27b35fe625c.html language=enus -->
## TOPIC 00071: RFMXSPECAN_ATTR_DPD_NMSE_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd_1gae3c48c765820d7c94a5ba27b35fe625c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd_1gae3c48c765820d7c94a5ba27b35fe625c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the normalized mean-squared error (NMSE) computation. SyntaxRFMXSPECAN_ATTR_DPD_NMSE_ENABLEDNumeric ValueData TypeAccessApplies To1110075int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance.

### RFMXSPECAN_ATTR_DPD_NMSE_ENABLED

Specifies whether to enable the normalized mean-squared error (NMSE) computation.

#### Syntax

RFMXSPECAN_ATTR_DPD_NMSE_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110075 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_NMSE_ENABLED_FALSE | 0 (0x0) | Disables NMSE computation. NaN is returned as NMSE. |
| RFMXSPECAN_VAL_DPD_NMSE_ENABLED_TRUE | 1 (0x1) | Enables NMSE computation. |

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1ga2643759289052f1267d9e4935b71f88c.html language=enus -->
## TOPIC 00072: RFMXSPECAN_ATTR_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1ga2643759289052f1267d9e4935b71f88c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1ga2643759289052f1267d9e4935b71f88c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the predistortion type when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPENumeric ValueData TypeAccessApplies To1110050int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE

Specifies the predistortion type when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Lookup Table**.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110050 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Magnitude and Phase**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_AND_PHASE | 0 (0x0) | The measurement predistorts the magnitude and phase of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_MAGNITUDE_ONLY | 1 (0x1) | The measurement predistorts only the magnitude of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_LOOKUP_TABLE_CORRECTION_TYPE_PHASE_ONLY | 2 (0x2) | The measurement predistorts only the phase of the input waveform. |

Parent topic:

Apply DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1gab359e7d82093b22f3a16df272b2e3adc.html language=enus -->
## TOPIC 00073: RFMXSPECAN_ATTR_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1gab359e7d82093b22f3a16df272b2e3adc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1gab359e7d82093b22f3a16df272b2e3adc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the predistortion type when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPENumeric ValueData TypeAccessApplies To1110070int32Read/WriteN/ARemarks You do not need to use a

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE

Specifies the predistortion type when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial**.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110070 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Magnitude and Phase**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE_MAGNITUDE_AND_PHASE | 0 (0x0) | The measurement predistorts the magnitude and phase of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE_MAGNITUDE_ONLY | 1 (0x1) | The measurement predistorts only the magnitude of the input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_MEMORY_MODEL_CORRECTION_TYPE_PHASE_ONLY | 2 (0x2) | The measurement predistorts only the phase of the input waveform. |

Parent topic:

Apply DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga135d69cafde5b1672b95cb1949be73e8.html language=enus -->
## TOPIC 00074: RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga135d69cafde5b1672b95cb1949be73e8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga135d69cafde5b1672b95cb1949be73e8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the target PAPR type when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPENumeric ValueData TypeAccessApplies To1110089int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read th

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPE

Specifies the target PAPR type when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga7b05ee10e8c124560089f6a29093cce8.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110089 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Input PAPR**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPE_INPUT_PAPR | 0 (0x0) | Sets the target PAPR for pre-distorted waveform equal to the PAPR of input waveform. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_TARGET_PAPR_TYPE_CUSTOM | 1 (0x1) | Sets the target PAPR equal to the value that you set for the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_TARGET_PAPR attribute. |

Parent topic:

Crest Factor Reduction

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga33fbdb997239ec40796af10cc862388f.html language=enus -->
## TOPIC 00075: RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_MAXIMUM_ITERATIONS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga33fbdb997239ec40796af10cc862388f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga33fbdb997239ec40796af10cc862388f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of iterations allowed to converge waveform PAPR to target PAPR when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_MAXIMUM_ITERATIONSNumeric ValueData TypeAccessApplies To1110088int32Read/WriteN/ARemarks Y

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_MAXIMUM_ITERATIONS

Specifies the maximum number of iterations allowed to converge waveform PAPR to target PAPR when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga7b05ee10e8c124560089f6a29093cce8.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_MAXIMUM_ITERATIONS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110088 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Crest Factor Reduction

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga736d52ea248aed251ed5e04a2af49938.html language=enus -->
## TOPIC 00076: RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga736d52ea248aed251ed5e04a2af49938.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga736d52ea248aed251ed5e04a2af49938.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to perform the crest factor reduction (CFR) when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHODNumeric ValueData TypeAccessApplies To1110087int32Read/WriteN/ARemarks You do not need to use a selector s

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD

Specifies the method used to perform the crest factor reduction (CFR) when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga7b05ee10e8c124560089f6a29093cce8.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110087 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Clipping**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_METHOD_CLIPPING | 0 (0x0) | Hard clips the signal such that the target PAPR is achieved. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_METHOD_PEAK_WINDOWING | 1 (0x1) | Scales the peaks in the signal using weighted window function to get smooth peaks and achieve the target PAPR. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_CFR_METHOD_SIGMOID | 2 (0x2) | Scales the peaks using modified sigmoid transfer function to get smooth peaks and achieve the target PAPR. This method does not support the filter operation. |

Parent topic:

Crest Factor Reduction

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid.html language=enus -->
## TOPIC 00077: Sigmoid

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_FACTORSpecifies the shaping factor to be used when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD attribute to Sigmoid. Refer to DPD concept topic

### Sigmoid

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_FACTOR | Specifies the shaping factor to be used when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD attribute to Sigmoid. Refer to DPD concept topic for more information about shaping factor. |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_THRESHOLD | Specifies the shaping threshold to be used when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD attribute to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. |

#### Attachments

None

Parent topic:

Crest Factor Reduction

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid_1gab86e2774d0572d2e04d107f037568c08.html language=enus -->
## TOPIC 00078: RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_THRESHOLD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid_1gab86e2774d0572d2e04d107f037568c08.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid_1gab86e2774d0572d2e04d107f037568c08.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shaping threshold to be used when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD attribute to Sigmoid. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold. Synta

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_THRESHOLD

Specifies the shaping threshold to be used when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga7b05ee10e8c124560089f6a29093cce8.html) attribute to **True** and the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga736d52ea248aed251ed5e04a2af49938.html) attribute to **Sigmoid**. This value is expressed in dB. Refer to DPD concept topic for more information about shaping threshold.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_THRESHOLD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110110 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -5.

Parent topic:

Sigmoid

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid_1gadad11849a826ef8d69279b1069c1f391.html language=enus -->
## TOPIC 00079: RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_FACTOR

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid_1gadad11849a826ef8d69279b1069c1f391.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction__sigmoid_1gadad11849a826ef8d69279b1069c1f391.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shaping factor to be used when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD attribute to Sigmoid. Refer to DPD concept topic for more information about shaping factor. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SH

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_FACTOR

Specifies the shaping factor to be used when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga7b05ee10e8c124560089f6a29093cce8.html) attribute to **True** and the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_METHOD](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__crest__factor__reduction_1ga736d52ea248aed251ed5e04a2af49938.html) attribute to **Sigmoid**. Refer to DPD concept topic for more information about shaping factor.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_SHAPING_FACTOR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110109 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 5.

Parent topic:

Sigmoid

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user.html language=enus -->
## TOPIC 00080: User

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsLookup TableMemory PolynomialGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODELSpecifies the DPD model for applying DPD when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DUT_AVERAGE_INPUT_POWERSpecifie

### User

#### Groups

- Lookup Table
- Memory Polynomial

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL | Specifies the DPD model for applying DPD when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DUT_AVERAGE_INPUT_POWER | Specifies the average input power for the device under test that was used to compute the DPD Apply DPD User DPD Polynomial or the DPD Apply DPD User LUT Complex Gain when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEASUREMENT_SAMPLE_RATE | Specifies the acquisition sample rate used to compute the DPD Apply DPD User DPD Polynomial or DPD Apply DPD User LUT Complex Gain when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. This value is expressed in Hz. Actual sample rate may differ from requested sample rate in order to ensure a waveform is phase continuous. |

#### Attachments

None

Parent topic:

Apply DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user_1ga9bdce8c8195909c83e2f6ed8692c6981.html language=enus -->
## TOPIC 00081: RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user_1ga9bdce8c8195909c83e2f6ed8692c6981.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user_1ga9bdce8c8195909c83e2f6ed8692c6981.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DPD model for applying DPD when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. SyntaxRFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODELNumeric ValueData TypeAccessApplies To1110054int32Read/WriteN/ARemarks You do not need to use a selector string to configur

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL

Specifies the DPD model for applying DPD when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1gaab6752310dafc3162bfeb60f05776828.html) attribute to **User**.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110054 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Lookup Table**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_LOOKUP_TABLE | 0 (0x0) | This model computes the complex gain coefficients applied to linearize systems with negligible memory effects. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_MEMORY_POLYNOMIAL | 1 (0x1) | This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. |
| RFMXSPECAN_VAL_DPD_APPLY_DPD_USER_DPD_MODEL_GENERALIZED_MEMORY_POLYNOMIAL | 2 (0x2) | This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. |

Parent topic:

User

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial.html language=enus -->
## TOPIC 00082: Memory Polynomial

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCross TermsGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MEMORY_DEPTHSpecifies the memory depth of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial and set the RFM

### Memory Polynomial

#### Groups

- Cross Terms

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MEMORY_DEPTH | Specifies the memory depth of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial and set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. This value corresponds to Qa in the DPD for generalized memory polynomial. |
| RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_ORDER | Specifies the order of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial and set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. This value corresponds to Ka in the DPD for generalized memory polynomial. |

#### Attachments

None

Parent topic:

User

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial_1ga04642514b3a0905ed8213724f3c0a49f.html language=enus -->
## TOPIC 00083: RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_ORDER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial_1ga04642514b3a0905ed8213724f3c0a49f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial_1ga04642514b3a0905ed8213724f3c0a49f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial and set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. This value corresponds to K[a] in the DPD for gener

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_ORDER

Specifies the order of the DPD polynomial when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user_1ga9bdce8c8195909c83e2f6ed8692c6981.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial** and set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1gaab6752310dafc3162bfeb60f05776828.html) attribute to **User**. This value corresponds to K<sub>a</sub> in the [DPD](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/dpd.html) for generalized memory polynomial.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110058 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 3.

Parent topic:

Memory Polynomial

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial_1ga93a0413e0a437b30a81c3672f9c1eab1.html language=enus -->
## TOPIC 00084: RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MEMORY_DEPTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial_1ga93a0413e0a437b30a81c3672f9c1eab1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user__memory__polynomial_1ga93a0413e0a437b30a81c3672f9c1eab1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the memory depth of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL attribute to Memory Polynomial or Generalized Memory Polynomial and set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT attribute to User. This value corresponds to Q[a] in the DPD fo

### RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MEMORY_DEPTH

Specifies the memory depth of the DPD polynomial when you set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd__user_1ga9bdce8c8195909c83e2f6ed8692c6981.html) attribute to **Memory Polynomial** or **Generalized Memory Polynomial** and set the [RFMXSPECAN_ATTR_DPD_APPLY_DPD_CONFIGURATION_INPUT](group____root__ni_r_fmx_spec_an__attributes__dpd__apply__dpd_1gaab6752310dafc3162bfeb60f05776828.html) attribute to **User**. This value corresponds to Q<sub>a</sub> in the [DPD](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/dpd.html) for generalized memory polynomial.

#### Syntax

RFMXSPECAN_ATTR_DPD_APPLY_DPD_USER_MEMORY_POLYNOMIAL_MEMORY_DEPTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110059 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Memory Polynomial

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__dvr_1ga9de24ece661ad18fa62f2def9965ea14.html language=enus -->
## TOPIC 00085: RFMXSPECAN_ATTR_DPD_DVR_LINEAR_MEMORY_DEPTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__dvr_1ga9de24ece661ad18fa62f2def9965ea14.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__dvr_1ga9de24ece661ad18fa62f2def9965ea14.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the linear memory depth of the Decomposed Vector Rotation model when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Decomposed Vector Rotation. This value corresponds to M[l] in the DPD for the decomposed vector rotation model. SyntaxRFMXSPECAN_ATTR_DPD_DVR_LINEAR_MEMORY_DEPTHNumeric V

### RFMXSPECAN_ATTR_DPD_DVR_LINEAR_MEMORY_DEPTH

Specifies the linear memory depth of the Decomposed Vector Rotation model when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Decomposed Vector Rotation**. This value corresponds to *M<sub>l</sub> in the [DPD](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/dpd.html) for the decomposed vector rotation model.*

#### Syntax

RFMXSPECAN_ATTR_DPD_DVR_LINEAR_MEMORY_DEPTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110120 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 21. This value must be greater than or equal to 0.

Parent topic:

DVR

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__dvr_1gafc3648a930a68f98fed812a66fb5c496.html language=enus -->
## TOPIC 00086: RFMXSPECAN_ATTR_DPD_DVR_DDR_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__dvr_1gafc3648a930a68f98fed812a66fb5c496.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__dvr_1gafc3648a930a68f98fed812a66fb5c496.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Dynamic Deviation Reduction (DDR) terms which are a subset of Decomposed Vector Rotation Model when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Decomposed Vector Rotation. For more details, refer to the DPD for the decomposed vector rotation model. SyntaxRFMXSP

### RFMXSPECAN_ATTR_DPD_DVR_DDR_ENABLED

Specifies whether to enable the Dynamic Deviation Reduction (DDR) terms which are a subset of Decomposed Vector Rotation Model when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Decomposed Vector Rotation**. For more details, refer to the [DPD](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/dpd.html) for the decomposed vector rotation model.

#### Syntax

RFMXSPECAN_ATTR_DPD_DVR_DDR_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110122 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_DVR_DDR_ENABLED_FALSE | 0 (0x0) | The Dynamic Deviation Reduction (DDR) terms which are a subset of Decomposed Vector Rotation model are disabled. |
| RFMXSPECAN_VAL_DPD_DVR_DDR_ENABLED_TRUE | 1 (0x1) | The Dynamic Deviation Reduction (DDR) terms which are a subset of Decomposed Vector Rotation model are enabled. |

Parent topic:

DVR

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit.html language=enus -->
## TOPIC 00087: AM to PM Curve Fit

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDERSpecifies the degree of the polynomial used to approximate the device under test AM-to-PM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. RFMXSPECAN_ATTR_DPD_LOOKUP_TAB

### AM to PM Curve Fit

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDER | Specifies the degree of the polynomial used to approximate the device under test AM-to-PM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. |
| RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE | Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. |

#### Attachments

None

Parent topic:

Lookup Table

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit_1ga9b0b48656711ea01226a66c41f9ec373.html language=enus -->
## TOPIC 00088: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit_1ga9b0b48656711ea01226a66c41f9ec373.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit_1ga9b0b48656711ea01226a66c41f9ec373.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the degree of the polynomial used to approximate the device under test AM-to-PM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. SyntaxRFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDERNumeric ValueData TypeAccessApplies To1110027int32Read/WriteN/

### RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDER

Specifies the degree of the polynomial used to approximate the device under test AM-to-PM characteristic when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Lookup Table**.

#### Syntax

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110027 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 7.

Parent topic:

AM to PM Curve Fit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit_1gaad01ac5d3506eadafef26fe262852175.html language=enus -->
## TOPIC 00089: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit_1gaad01ac5d3506eadafef26fe262852175.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__am__to__pm__curve__fit_1gaad01ac5d3506eadafef26fe262852175.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. SyntaxRFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPENumeric ValueData TypeAccessApplies To1110028int32Read/WriteN/ARem

### RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE

Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Lookup Table**.

#### Syntax

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110028 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Least Absolute Residual**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_SQUARE | 0 (0x0) | Minimizes the energy of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_LEAST_ABSOLUTE_RESIDUAL | 1 (0x1) | Minimizes the magnitude of the polynomial approximation error. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_AM_TO_PM_CURVE_FIT_TYPE_BISQUARE | 2 (0x2) | Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

Parent topic:

AM to PM Curve Fit

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__threshold.html language=enus -->
## TOPIC 00090: Threshold

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__threshold.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__threshold.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_DEFINITIONSpecifies the definition to use for thresholding acquired and reference waveform. RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_ENABLEDSpecifies whether to enable thresholding of the acquired samples to be used f

### Threshold

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_DEFINITION | Specifies the definition to use for thresholding acquired and reference waveform. |
| RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_ENABLED | Specifies whether to enable thresholding of the acquired samples to be used for the DPD measurement when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Lookup Table. |
| RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_LEVEL | Specifies either the relative or absolute threshold power level based on the value of the RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE attribute. This value is expressed in dB or dBm. |
| RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE | Specifies the reference for the power level used for thresholding. |

#### Attachments

None

Parent topic:

Lookup Table

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__threshold_1ga647716530f7bc8a10af007ab4f178713.html language=enus -->
## TOPIC 00091: RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__threshold_1ga647716530f7bc8a10af007ab4f178713.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__lookup__table__threshold_1ga647716530f7bc8a10af007ab4f178713.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxRFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPENumeric ValueData TypeAccessApplies To1110030int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance.

### RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE

Specifies the reference for the power level used for thresholding.

#### Syntax

RFMXSPECAN_ATTR_DPD_LOOKUP_TABLE_THRESHOLD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110030 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_RELATIVE | 0 (0x0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_DPD_LOOKUP_TABLE_THRESHOLD_TYPE_ABSOLUTE | 1 (0x1) | The threshold is the absolute power, in dBm. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1ga64ee4f366c0687d2528f9ef96dac87a4.html language=enus -->
## TOPIC 00092: RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1ga64ee4f366c0687d2528f9ef96dac87a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1ga64ee4f366c0687d2528f9ef96dac87a4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition sample rate when you set the RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE_MODE attribute to User. This value is expressed in Samples per second (S/s). Actual sample rate may differ from requested sample rate in order to ensure a waveform is phase continuous. SyntaxRFMXSPECAN

### RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE

Specifies the acquisition sample rate when you set the [RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE_MODE](group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1gae9fbf9f41afede212c670779e2d111e6.html) attribute to **User**. This value is expressed in Samples per second (S/s). Actual sample rate may differ from requested sample rate in order to ensure a waveform is phase continuous.

#### Syntax

RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110019 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 120 MHz.

Parent topic:

Measurement Sample Rate

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1gae9fbf9f41afede212c670779e2d111e6.html language=enus -->
## TOPIC 00093: RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1gae9fbf9f41afede212c670779e2d111e6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__measurement__sample__rate_1gae9fbf9f41afede212c670779e2d111e6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition sample rate configuration mode. SyntaxRFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE_MODENumeric ValueData TypeAccessApplies To1110018int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer t

### RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE_MODE

Specifies the acquisition sample rate configuration mode.

#### Syntax

RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110018 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Reference Waveform**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_MEASUREMENT_SAMPLE_RATE_MODE_USER | 0 (0x0) | The acquisition sample rate is defined by the value of the RFMXSPECAN_ATTR_DPD_MEASUREMENT_SAMPLE_RATE attribute. |
| RFMXSPECAN_VAL_DPD_MEASUREMENT_SAMPLE_RATE_MODE_REFERENCE_WAVEFORM | 1 (0x1) | The acquisition sample rate is set to match the sample rate of the reference waveform. |

Parent topic:

Measurement Sample Rate

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__cross__terms_1gad4eefd1d60cbec55b4c1266618b26c5d.html language=enus -->
## TOPIC 00094: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__cross__terms_1gad4eefd1d60cbec55b4c1266618b26c5d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__cross__terms_1gad4eefd1d60cbec55b4c1266618b26c5d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lag order cross term of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Generalized Memory Polynomial. This term value corresponds to K[b] in the DPD for the generalized memory polynomial. SyntaxRFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDERNumeric ValueData

### RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER

Specifies the lag order cross term of the DPD polynomial when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Generalized Memory Polynomial**. This term value corresponds to *K<sub>b</sub> in the [DPD](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/dpd.html) for the generalized memory polynomial.*

#### Syntax

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110036 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Cross Terms

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__cross__terms_1gae1c7663501a20a56454276586f49b748.html language=enus -->
## TOPIC 00095: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__cross__terms_1gae1c7663501a20a56454276586f49b748.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__cross__terms_1gae1c7663501a20a56454276586f49b748.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lead order cross term of the DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Generalized Memory Polynomial. This term value corresponds to K[c] in the DPD for the generalized memory polynomial. SyntaxRFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDERNumeric ValueDa

### RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER

Specifies the lead order cross term of the DPD polynomial when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Generalized Memory Polynomial**. This term value corresponds to *K<sub>c</sub> in the [DPD](https://www.ni.com/docs/en-US/bundle/rfmx-specan/page/dpd.html) for the generalized memory polynomial.*

#### Syntax

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110035 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Cross Terms

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__model__subset__cross__terms.html language=enus -->
## TOPIC 00096: Cross Terms

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__model__subset__cross__terms.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__model__subset__cross__terms.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPEConfigures the type of terms of the lag order DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Generalized Memory Polynomial. RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPEConfigure

### Cross Terms

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LAG_ORDER_TYPE | Configures the type of terms of the lag order DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Generalized Memory Polynomial. |
| RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE | Configures the type of terms of the lead order DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Generalized Memory Polynomial. |

#### Attachments

None

Parent topic:

Model Subset

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__model__subset__cross__terms_1ga37deb864e736b52783a302c79903f9a7.html language=enus -->
## TOPIC 00097: RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__model__subset__cross__terms_1ga37deb864e736b52783a302c79903f9a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__memory__polynomial__model__subset__cross__terms_1ga37deb864e736b52783a302c79903f9a7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of terms of the lead order DPD polynomial when you set the RFMXSPECAN_ATTR_DPD_MODEL attribute to Generalized Memory Polynomial. SyntaxRFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPENumeric ValueData TypeAccessApplies To1110096int32Read/WriteN/ARemarks You do not need to us

### RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE

Configures the type of terms of the lead order DPD polynomial when you set the [RFMXSPECAN_ATTR_DPD_MODEL](group____root__ni_r_fmx_spec_an__attributes__dpd_1gacecd93cf0649b5b0bbf50cc396218149.html) attribute to **Generalized Memory Polynomial**.

#### Syntax

RFMXSPECAN_ATTR_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110096 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **All Orders**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE_ALL_ORDERS | 0 (0x0) | The memory polynomial will compute all the terms for the given order. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE_ODD_ORDERS_ONLY | 1 (0x1) | The memory polynomial will compute the non-zero coefficients only for the odd terms. |
| RFMXSPECAN_VAL_DPD_MEMORY_POLYNOMIAL_LEAD_ORDER_TYPE_EVEN_ORDERS_ONLY | 2 (0x2) | The memory polynomial will compute the non-zero coefficents only for the even terms. |

Parent topic:

Cross Terms

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__predpd.html language=enus -->
## TOPIC 00098: Pre-DPD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__predpd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__predpd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsCrest Factor ReductionGroup membersNoneAttachmentsNone

### Pre-DPD

#### Groups

- Crest Factor Reduction

#### Group members

None

#### Attachments

None

Parent topic:

DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction.html language=enus -->
## TOPIC 00099: Crest Factor Reduction

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsFilterPeak WindowingSigmoidGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_BANDWIDTHSpecifies the carrier bandwidth when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED attribute to True. This value is express

### Crest Factor Reduction

#### Groups

- Filter
- Peak Windowing
- Sigmoid

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_BANDWIDTH | Specifies the carrier bandwidth when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED attribute to True. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_OFFSET | Specifies the carrier offset relative to the center of the complex baseband equivalent of the RF signal when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED attribute to True. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED | Specifies whether to enable the crest factor reduction (CFR) when applying pre-DPD signal conditioning. |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_MAXIMUM_ITERATIONS | Specifies the maximum number of iterations allowed to converge waveform PAPR to target PAPR, when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_METHOD | Specifies the method used to perform crest factor reduction (CFR) when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute to True. Refer to DPD concept topic for more information about CFR methods. |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_NUMBER_OF_CARRIERS | Specifies the number of carriers in the input waveform when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_TARGET_PAPR | Specifies the target peak-to-average power ratio when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute to True. This value is expressed in dB. |

#### Attachments

None

Parent topic:

Pre-DPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1ga7dc83d3b63529a4e6a49285f30d45b92.html language=enus -->
## TOPIC 00100: RFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1ga7dc83d3b63529a4e6a49285f30d45b92.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1ga7dc83d3b63529a4e6a49285f30d45b92.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier bandwidth when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED attribute to True. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_BANDWIDTHNumeric ValueData TypeAccessApplies To1110116

### RFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_BANDWIDTH

Specifies the carrier bandwidth when you set the [RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1ga362c9f29ff1f5b3779aaef8951713388.html) attribute and the [RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__filter_1ga53ce98c061bc0e92649baf0c99986df2.html) attribute to **True**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_DPD_PRE_DPD_CARRIER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110116 | float64 | Read/Write | Carrier |

#### Remarks

Use "carrier<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 20 MHz.

Parent topic:

Crest Factor Reduction

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__filter.html language=enus -->
## TOPIC 00101: Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLEDSpecifies whether to enable the filtering operation when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True. Refer to DPD concept topic for more information about filtering. AttachmentsNone

### Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_FILTER_ENABLED | Specifies whether to enable the filtering operation when you set the RFMXSPECAN_ATTR_DPD_APPLY_DPD_CFR_ENABLED attribute to True. Refer to DPD concept topic for more information about filtering. |

#### Attachments

None

Parent topic:

Crest Factor Reduction

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__peak__windowing_1ga059e9fa616af44c899b0e658d104026c.html language=enus -->
## TOPIC 00102: RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__peak__windowing_1ga059e9fa616af44c899b0e658d104026c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__peak__windowing_1ga059e9fa616af44c899b0e658d104026c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window type to be used when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_METHOD attribute to Peak Windowing. SyntaxRFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_TYPENumeric ValueData TypeAccessApplies To1110082int32Read/WriteN/A

### RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_TYPE

Specifies the window type to be used when you set the [RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1ga362c9f29ff1f5b3779aaef8951713388.html) attribute to **True** and the [RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_METHOD](group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1gac5122420c77bbd69dd20006629c9bc8b.html) attribute to **Peak Windowing**.

#### Syntax

RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110082 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Kaiser-Bessel**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_FLAT_TOP | 1 (0x1) | Uses the flat top window function to scale peaks. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_HANNING | 2 (0x2) | Uses the Hanning window function to scale peaks. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_HAMMING | 3 (0x3) | Uses the Hamming window function to scale peaks. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_GAUSSIAN | 4 (0x4) | Uses the Gaussian window function to scale peaks. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_BLACKMAN | 5 (0x5) | Uses the Blackman window function to scale peaks. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_BLACKMAN_HARRIS | 6 (0x6) | Uses the Blackman-Harris window function to scale peaks. |
| RFMXSPECAN_VAL_DPD_PRE_DPD_CFR_WINDOW_TYPE_KAISER_BESSEL | 7 (0x7) | Uses the Kaiser-Bessel window function to scale peaks. |

Parent topic:

Peak Windowing

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__peak__windowing_1ga60042f77e3cb3c7e593bb634dac68159.html language=enus -->
## TOPIC 00103: RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_LENGTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__peak__windowing_1ga60042f77e3cb3c7e593bb634dac68159.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction__peak__windowing_1ga60042f77e3cb3c7e593bb634dac68159.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum window length to be used when you set the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED attribute to True and the RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_METHOD attribute to Peak Windowing. SyntaxRFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_LENGTHNumeric ValueData TypeAccessApplies To1110083int32R

### RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_LENGTH

Specifies the maximum window length to be used when you set the [RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_ENABLED](group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1ga362c9f29ff1f5b3779aaef8951713388.html) attribute to **True** and the [RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_METHOD](group____root__ni_r_fmx_spec_an__attributes__dpd__predpd__crest__factor__reduction_1gac5122420c77bbd69dd20006629c9bc8b.html) attribute to **Peak Windowing**.

#### Syntax

RFMXSPECAN_ATTR_DPD_PRE_DPD_CFR_WINDOW_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110083 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Peak Windowing

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__dpd__results_1ga67765f5b0d699e73091e93d6fd1c733b.html language=enus -->
## TOPIC 00104: RFMXSPECAN_ATTR_DPD_RESULTS_AVERAGE_GAIN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__dpd__results_1ga67765f5b0d699e73091e93d6fd1c733b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__dpd__results_1ga67765f5b0d699e73091e93d6fd1c733b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average gain of the device under test. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_DPD_RESULTS_AVERAGE_GAINNumeric ValueData TypeAccessApplies To1110067float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result for default signal and result instance.

### RFMXSPECAN_ATTR_DPD_RESULTS_AVERAGE_GAIN

Returns the average gain of the device under test. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_DPD_RESULTS_AVERAGE_GAIN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110067 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt_1ga0e69dbb159d299ff0a839b75992dcd13.html language=enus -->
## TOPIC 00105: RFMXSPECAN_ATTR_FCNT_ALL_TRACES_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt_1ga0e69dbb159d299ff0a839b75992dcd13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt_1ga0e69dbb159d299ff0a839b75992dcd13.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the FCnt measurement. SyntaxRFMXSPECAN_ATTR_FCNT_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To1064976int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute fo

### RFMXSPECAN_ATTR_FCNT_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the FCnt measurement.

#### Syntax

RFMXSPECAN_ATTR_FCNT_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064976 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

FCnt

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt_1gac3a2c78ea7520749daa130e9ab528c72.html language=enus -->
## TOPIC 00106: RFMXSPECAN_ATTR_FCNT_MEASUREMENT_INTERVAL

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt_1gac3a2c78ea7520749daa130e9ab528c72.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt_1gac3a2c78ea7520749daa130e9ab528c72.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition time for the FCnt measurement. This value is expressed in seconds. SyntaxRFMXSPECAN_ATTR_FCNT_MEASUREMENT_INTERVALNumeric ValueData TypeAccessApplies To1064962float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the de

### RFMXSPECAN_ATTR_FCNT_MEASUREMENT_INTERVAL

Specifies the acquisition time for the FCnt measurement. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_FCNT_MEASUREMENT_INTERVAL

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064962 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001.

Parent topic:

FCnt

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt_1gaf0840a9c0e9ea6452b3c13a2a28f4bac.html language=enus -->
## TOPIC 00107: RFMXSPECAN_ATTR_FCNT_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt_1gaf0840a9c0e9ea6452b3c13a2a28f4bac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt_1gaf0840a9c0e9ea6452b3c13a2a28f4bac.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for FCnt measurement. SyntaxRFMXSPECAN_ATTR_FCNT_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1064963int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threads

### RFMXSPECAN_ATTR_FCNT_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for FCnt measurement.

#### Syntax

RFMXSPECAN_ATTR_FCNT_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064963 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

FCnt

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1ga16bafe6479a0809bf536aad5c022b3a1.html language=enus -->
## TOPIC 00108: RFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1ga16bafe6479a0809bf536aad5c022b3a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1ga16bafe6479a0809bf536aad5c022b3a1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the FCnt measurement. SyntaxRFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To1064966int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to th

### RFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLED

Specifies whether to enable averaging for the FCnt measurement.

#### Syntax

RFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064966 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_FCNT_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_FCNT_AVERAGING_ENABLED_TRUE | 1 (0x1) | The FCnt measurement uses the RFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLED attribute as the number of acquisitions over which the FCnt measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1gaaee39d7e943f21d0b1a6cdfda935a321.html language=enus -->
## TOPIC 00109: RFMXSPECAN_ATTR_FCNT_AVERAGING_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1gaaee39d7e943f21d0b1a6cdfda935a321.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1gaaee39d7e943f21d0b1a6cdfda935a321.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for the FCnt measurement. The averaged instantaneous signal phase difference is used for the measurement. SyntaxRFMXSPECAN_ATTR_FCNT_AVERAGING_TYPENumeric ValueData TypeAccessApplies To1064968int32Read/WriteN/ARemarks You do not need to use a selector string to configure

### RFMXSPECAN_ATTR_FCNT_AVERAGING_TYPE

Specifies the averaging type for the FCnt measurement. The averaged instantaneous signal phase difference is used for the measurement.

#### Syntax

RFMXSPECAN_ATTR_FCNT_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064968 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Mean**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_FCNT_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The maximum instantaneous signal phase difference over multiple acquisitions is used for the frequency measurement. |
| RFMXSPECAN_VAL_FCNT_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The minimum instantaneous signal phase difference over multiple acquisitions is used for the frequency measurement. |
| RFMXSPECAN_VAL_FCNT_AVERAGING_TYPE_MEAN | 6 (0x6) | The mean of the instantaneous signal phase difference over multiple acquisitions is used for the frequency measurement. |
| RFMXSPECAN_VAL_FCNT_AVERAGING_TYPE_MINMAX | 7 (0x7) | The maximum instantaneous signal phase difference over multiple acquisitions is used for the frequency measurement. The sign of the phase difference is ignored to find the maximum instantaneous value. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1gaedc4db84bc24ed89eb402834a5fd3d78.html language=enus -->
## TOPIC 00110: RFMXSPECAN_ATTR_FCNT_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1gaedc4db84bc24ed89eb402834a5fd3d78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1gaedc4db84bc24ed89eb402834a5fd3d78.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_FCNT_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1064965int32Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXSPECAN_ATTR_FCNT_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXSPECAN_ATTR_FCNT_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__fcnt__averaging_1ga16bafe6479a0809bf536aad5c022b3a1.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_FCNT_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064965 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga0486153c01647ff2751e001657b40c7a.html language=enus -->
## TOPIC 00111: RFMXSPECAN_ATTR_FCNT_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga0486153c01647ff2751e001657b40c7a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga0486153c01647ff2751e001657b40c7a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_FCNT_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To1064970float64Read/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXSPECAN_ATTR_FCNT_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the signal. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_FCNT_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064970 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 100 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga4d27ec95feb61ea33ef43904938d8e87.html language=enus -->
## TOPIC 00112: RFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHA

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga4d27ec95feb61ea33ef43904938d8e87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga4d27ec95feb61ea33ef43904938d8e87.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxRFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHANumeric ValueData TypeAccessApplies To1064969float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance.

### RFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHA

Specifies the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

RFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064969 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.1.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga92fa5c1147f7b083fcc7ade4ba6c7c7b.html language=enus -->
## TOPIC 00113: RFMXSPECAN_ATTR_FCNT_RBW_FILTER_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga92fa5c1147f7b083fcc7ade4ba6c7c7b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__rbw__filter_1ga92fa5c1147f7b083fcc7ade4ba6c7c7b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital resolution bandwidth (RBW) filter. SyntaxRFMXSPECAN_ATTR_FCNT_RBW_FILTER_TYPENumeric ValueData TypeAccessApplies To1064971int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer t

### RFMXSPECAN_ATTR_FCNT_RBW_FILTER_TYPE

Specifies the shape of the digital resolution bandwidth (RBW) filter.

#### Syntax

RFMXSPECAN_ATTR_FCNT_RBW_FILTER_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064971 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **None**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_GAUSSIAN | 1 (0x1) | The RBW filter has a Gaussian response. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_FLAT | 2 (0x2) | The RBW filter has a flat response. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_NONE | 5 (0x5) | The measurement does not use any RBW filtering. |
| RFMXSPECAN_VAL_FCNT_RBW_FILTER_TYPE_RRC | 6 (0x6) | The RRC filter with the roll-off specified by RFMXSPECAN_ATTR_FCNT_RBW_FILTER_RRC_ALPHA attribute is used as the RBW filter. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__results_1ga722a16502fd8d5ea5dd17600baa60254.html language=enus -->
## TOPIC 00114: RFMXSPECAN_ATTR_FCNT_RESULTS_AVERAGE_ABSOLUTE_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__results_1ga722a16502fd8d5ea5dd17600baa60254.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__results_1ga722a16502fd8d5ea5dd17600baa60254.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF signal frequency. Only samples above the threshold are used when you set the RFMXSPECAN_ATTR_FCNT_THRESHOLD_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_FCNT_RESULTS_AVERAGE_ABSOLUTE_FREQUENCYNumeric ValueData TypeAccessApplies To1064979float64Read-OnlyN/ARemarks You do not need t

### RFMXSPECAN_ATTR_FCNT_RESULTS_AVERAGE_ABSOLUTE_FREQUENCY

Returns the RF signal frequency. Only samples above the threshold are used when you set the [RFMXSPECAN_ATTR_FCNT_THRESHOLD_ENABLED](group____root__ni_r_fmx_spec_an__attributes__fcnt__threshold_1ga2ce0f4169a2e4dcc8610afb710031074.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_FCNT_RESULTS_AVERAGE_ABSOLUTE_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064979 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__fcnt__threshold_1ga5d892529eb98f84582674ac929af42a1.html language=enus -->
## TOPIC 00115: RFMXSPECAN_ATTR_FCNT_THRESHOLD_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__fcnt__threshold_1ga5d892529eb98f84582674ac929af42a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__fcnt__threshold_1ga5d892529eb98f84582674ac929af42a1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the power level used for thresholding. SyntaxRFMXSPECAN_ATTR_FCNT_THRESHOLD_TYPENumeric ValueData TypeAccessApplies To1064974int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to th

### RFMXSPECAN_ATTR_FCNT_THRESHOLD_TYPE

Specifies the reference for the power level used for thresholding.

#### Syntax

RFMXSPECAN_ATTR_FCNT_THRESHOLD_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1064974 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_FCNT_THRESHOLD_TYPE_RELATIVE | 0 (0x0) | The threshold is relative to the peak power of the acquired samples. |
| RFMXSPECAN_VAL_FCNT_THRESHOLD_TYPE_ABSOLUTE | 1 (0x1) | The threshold is the absolute power, in dBm. |

Parent topic:

Threshold

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm_1ga841d4b184f06eaf789db3bc95b0830b3.html language=enus -->
## TOPIC 00116: RFMXSPECAN_ATTR_HARM_NOISE_COMPENSATION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm_1ga841d4b184f06eaf789db3bc95b0830b3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm_1ga841d4b184f06eaf789db3bc95b0830b3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer. SyntaxRFMXSPECAN_ATTR_HARM_NOISE_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To1069083int32Read/WriteN/ARemarks You do not need to use a selector string to configure o

### RFMXSPECAN_ATTR_HARM_NOISE_COMPENSATION_ENABLED

Specifies whether to enable compensation of the average harmonic powers for inherent noise floor of the signal analyzer.

#### Syntax

RFMXSPECAN_ATTR_HARM_NOISE_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069083 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Disables compensation of the average harmonic powers for the noise floor of the signal analyzer. |
| RFMXSPECAN_VAL_HARM_NOISE_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Enables compensation of the average harmonic powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the harmonics measurement and cached for future use. If the signal analyzer or measurement parameters change, noise floors are measured again.Supported devices: PXIe-5663/5665/5668 |

Parent topic:

Harm

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm_1gad4a7b61bee906c2e083e84536d9f10d6.html language=enus -->
## TOPIC 00117: RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm_1gad4a7b61bee906c2e083e84536d9f10d6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm_1gad4a7b61bee906c2e083e84536d9f10d6.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable auto configuration of successive harmonics. SyntaxRFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLEDNumeric ValueData TypeAccessApplies To1069064int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Re

### RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED

Specifies whether to enable auto configuration of successive harmonics.

#### Syntax

RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069064 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_FALSE | 0 (0x0) | The measurement uses manual configuration for the harmonic order, harmonic bandwidth, and harmonic measurement interval. |
| RFMXSPECAN_VAL_HARM_AUTO_HARMONICS_SETUP_ENABLED_TRUE | 1 (0x1) | The measurement uses the RFMXSPECAN_ATTR_HARM_NUMBER_OF_HARMONICS attribute and configuration of the fundamental to configure successive harmonics. Bandwidth of Nth order harmonic = N * (Bandwidth of fundamental). Measurement interval of Nth order harmonics = (Measurement interval of fundamental)/N |

Parent topic:

Harm

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__fundamental__rbw__filter.html language=enus -->
## TOPIC 00118: RBW Filter

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__fundamental__rbw__filter.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__fundamental__rbw__filter.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHASpecifies the roll-off factor for the root-raised-cosine (RRC) filter. RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_BANDWIDTHSpecifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the fund

### RBW Filter

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA | Specifies the roll-off factor for the root-raised-cosine (RRC) filter. |
| RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_BANDWIDTH | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to measure the fundamental signal. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_TYPE | Specifies the shape of the digital resolution bandwidth (RBW) filter. |

#### Attachments

None

Parent topic:

Fundamental

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__fundamental__rbw__filter_1gad1436f7c92efab3901aae9434d3a4845.html language=enus -->
## TOPIC 00119: RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__fundamental__rbw__filter_1gad1436f7c92efab3901aae9434d3a4845.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__fundamental__rbw__filter_1gad1436f7c92efab3901aae9434d3a4845.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the roll-off factor for the root-raised-cosine (RRC) filter. SyntaxRFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHANumeric ValueData TypeAccessApplies To1069059float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal i

### RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA

Specifies the roll-off factor for the root-raised-cosine (RRC) filter.

#### Syntax

RFMXSPECAN_ATTR_HARM_FUNDAMENTAL_RBW_FILTER_ALPHA

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069059 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.1.

**Supported devices**: PXIe-5665/5668

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__harmonic_1ga14ebe9e16d9cc7b250bc66e6b83fe7d0.html language=enus -->
## TOPIC 00120: RFMXSPECAN_ATTR_HARM_HARMONIC_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__harmonic_1ga14ebe9e16d9cc7b250bc66e6b83fe7d0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__harmonic_1ga14ebe9e16d9cc7b250bc66e6b83fe7d0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable a particular harmonic for measurement. Only the enabled harmonics are used to measure the total harmonic distortion (THD). This attribute is not used if you set the RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED to True. SyntaxRFMXSPECAN_ATTR_HARM_HARMONIC_ENABLEDNumeric ValueDa

### RFMXSPECAN_ATTR_HARM_HARMONIC_ENABLED

Specifies whether to enable a particular harmonic for measurement. Only the enabled harmonics are used to measure the total harmonic distortion (THD). This attribute is not used if you set the [RFMXSPECAN_ATTR_HARM_AUTO_SETUP_ENABLED](group____root__ni_r_fmx_spec_an__attributes__harm_1gad4a7b61bee906c2e083e84536d9f10d6.html) to **True**.

#### Syntax

RFMXSPECAN_ATTR_HARM_HARMONIC_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069065 | int32 | Read/Write | Harmonic |

#### Remarks

Use "harmonic<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **True**.

**Supported devices**: PXIe-5665/5668

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_FALSE | 0 (0x0) | Disables the harmonic for measurement. |
| RFMXSPECAN_VAL_HARM_HARMONIC_ENABLED_TRUE | 1 (0x1) | Enables the harmonic for measurement. |

Parent topic:

Harmonic

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__results_1ga2fad5a55e7778793962f19920cbe1536.html language=enus -->
## TOPIC 00121: RFMXSPECAN_ATTR_HARM_RESULTS_FUNDAMENTAL_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__results_1ga2fad5a55e7778793962f19920cbe1536.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__results_1ga2fad5a55e7778793962f19920cbe1536.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency used as the fundamental frequency. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_HARM_RESULTS_FUNDAMENTAL_FREQUENCYNumeric ValueData TypeAccessApplies To1069073float64Read-OnlyN/ARemarks You do not need to use a selector string to configure or read this attribute for the

### RFMXSPECAN_ATTR_HARM_RESULTS_FUNDAMENTAL_FREQUENCY

Returns the frequency used as the fundamental frequency. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_HARM_RESULTS_FUNDAMENTAL_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069073 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic.html language=enus -->
## TOPIC 00122: Harmonic

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_ABSOLUTE_POWERReturns the average absolute power measured at the harmonic specified by the selector string. This value is expressed in dBm. RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWERReturns the aver

### Harmonic

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_ABSOLUTE_POWER | Returns the average absolute power measured at the harmonic specified by the selector string. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER | Returns the average power relative to the fundamental power measured at the harmonic specified by the selector string. This value is expressed in dB. |
| RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_FREQUENCY | Returns the RF frequency of the harmonic. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBW | Returns the resolution bandwidth (RBW) which is used by the harmonic measurement, for the harmonic specified by the selector string. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic_1ga036ca442db7cd8d8dfef4e25fc5f7ad5.html language=enus -->
## TOPIC 00123: RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBW

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic_1ga036ca442db7cd8d8dfef4e25fc5f7ad5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic_1ga036ca442db7cd8d8dfef4e25fc5f7ad5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the resolution bandwidth (RBW) which is used by the harmonic measurement, for the harmonic specified by the selector string. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBWNumeric ValueData TypeAccessApplies To1069077float64Read-OnlyHarmonicRemarks Use "harmoni

### RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBW

Returns the resolution bandwidth (RBW) which is used by the harmonic measurement, for the harmonic specified by the selector string. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_RBW

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069077 | float64 | Read-Only | Harmonic |

#### Remarks

Use "harmonic<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Harmonic

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic_1gaf956a479c35663542527553e4b696746.html language=enus -->
## TOPIC 00124: RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic_1gaf956a479c35663542527553e4b696746.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__harm__results__harmonic_1gaf956a479c35663542527553e4b696746.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power relative to the fundamental power measured at the harmonic specified by the selector string. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWERNumeric ValueData TypeAccessApplies To1069079float64Read-OnlyHarmonicRemarks Use "ha

### RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER

Returns the average power relative to the fundamental power measured at the harmonic specified by the selector string. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_HARM_RESULTS_HARMONIC_AVERAGE_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1069079 | float64 | Read-Only | Harmonic |

#### Remarks

Use "harmonic<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Harmonic

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd_1gad37144bdb15a13c2be97c56ba0f18b63.html language=enus -->
## TOPIC 00125: RFMXSPECAN_ATTR_IDPD_SIGNAL_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd_1gad37144bdb15a13c2be97c56ba0f18b63.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd_1gad37144bdb15a13c2be97c56ba0f18b63.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of reference waveform. SyntaxRFMXSPECAN_ATTR_IDPD_SIGNAL_TYPENumeric ValueData TypeAccessApplies To1310726int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for

### RFMXSPECAN_ATTR_IDPD_SIGNAL_TYPE

Specifies the type of reference waveform.

#### Syntax

RFMXSPECAN_ATTR_IDPD_SIGNAL_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1310726 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Modulated.**

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IDPD_SIGNAL_TYPE_MODULATED | 0 (0x0) | Specifies the reference waveform is a banded signal like cellular or connectivity standard signals. |
| RFMXSPECAN_VAL_IDPD_SIGNAL_TYPE_TONES | 1 (0x1) | Specifies the reference waveform is a continuous signal comprising of one or more tones. IDPD measurement chooses alignment algorithms based on the IDPD Signal Type attribute. |

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd_1gaf284cc3ee1181c2b6053b9f3963bfb3e.html language=enus -->
## TOPIC 00126: RFMXSPECAN_ATTR_IDPD_POWER_LINEARITY_TRADEOFF

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd_1gaf284cc3ee1181c2b6053b9f3963bfb3e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd_1gaf284cc3ee1181c2b6053b9f3963bfb3e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain tradeoff factor that sets the gain expected from the DUT after applying IDPD on the input waveform. This value is expressed as a percentage. SyntaxRFMXSPECAN_ATTR_IDPD_POWER_LINEARITY_TRADEOFFNumeric ValueData TypeAccessApplies To1310747float64Read/WriteN/ARemarks The percentages

### RFMXSPECAN_ATTR_IDPD_POWER_LINEARITY_TRADEOFF

Specifies the gain tradeoff factor that sets the gain expected from the DUT after applying IDPD on the input waveform. This value is expressed as a percentage.

#### Syntax

RFMXSPECAN_ATTR_IDPD_POWER_LINEARITY_TRADEOFF

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1310747 | float64 | Read/Write | N/A |

#### Remarks

The percentages zero corresponds to the gain at maximum linearity, hundred corresponds to the gain at maximum power, and fifty corresponds to the gain at average power output from the DUT.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 50.

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd__averaging_1gaebee70060d09e6f2f753460e7471914d.html language=enus -->
## TOPIC 00127: RFMXSPECAN_ATTR_IDPD_AVERAGING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd__averaging_1gaebee70060d09e6f2f753460e7471914d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd__averaging_1gaebee70060d09e6f2f753460e7471914d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the IDPD measurement. SyntaxRFMXSPECAN_ATTR_IDPD_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To1310735int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to th

### RFMXSPECAN_ATTR_IDPD_AVERAGING_ENABLED

Specifies whether to enable averaging for the IDPD measurement.

#### Syntax

RFMXSPECAN_ATTR_IDPD_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1310735 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IDPD_AVERAGING_ENABLED_FALSE | 0 (0x0) | The number of acquisitions is 1. |
| RFMXSPECAN_VAL_IDPD_AVERAGING_ENABLED_TRUE | 1 (0x1) | The measurement uses RFMXSPECAN_ATTR_IDPD_AVERAGING_COUNT for the number of acquisitions over which the measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer.html language=enus -->
## TOPIC 00128: Equalizer

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTHSpecifies the length of the equalizer filter to be trained. RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODESpecifies whether to enable equalization. AttachmentsNone

### Equalizer

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH | Specifies the length of the equalizer filter to be trained. |
| RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE | Specifies whether to enable equalization. |

#### Attachments

None

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1ga6cc9a1f4b30a6ee911eae34be88aa5f1.html language=enus -->
## TOPIC 00129: RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1ga6cc9a1f4b30a6ee911eae34be88aa5f1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1ga6cc9a1f4b30a6ee911eae34be88aa5f1.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the equalizer filter to be trained. SyntaxRFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTHNumeric ValueData TypeAccessApplies To1310723int32Read/WriteN/ARemarks This attribute is applicable when you set RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE to Train.You do not need to use a selecto

### RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH

Specifies the length of the equalizer filter to be trained.

#### Syntax

RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1310723 | int32 | Read/Write | N/A |

#### Remarks

This attribute is applicable when you set [RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE](group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1gaad9bd9da5d277483352c9fc03e2fe163.html) to **Train**.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 101. Valid values are 1 to 4096, inclusive.

Parent topic:

Equalizer

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1gaad9bd9da5d277483352c9fc03e2fe163.html language=enus -->
## TOPIC 00130: RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1gaad9bd9da5d277483352c9fc03e2fe163.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd__equalizer_1gaad9bd9da5d277483352c9fc03e2fe163.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable equalization. SyntaxRFMXSPECAN_ATTR_IDPD_EQUALIZER_MODENumeric ValueData TypeAccessApplies To1310722int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic f

### RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE

Specifies whether to enable equalization.

#### Syntax

RFMXSPECAN_ATTR_IDPD_EQUALIZER_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1310722 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **OFF.**

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_OFF | 0 (0x0) | Equalization filter is not applied. |
| RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_TRAIN | 1 (0x1) | Train Equalization filter. The filter length is obtained from the RFMXSPECAN_ATTR_IDPD_EQUALIZER_FILTER_LENGTH. |
| RFMXSPECAN_VAL_IDPD_EQUALIZER_MODE_HOLD | 2 (0x2) | The RFmxSpecAn_IDPDCfgEqualizerCoefficients function specifies the filter that acts as the equalization filter. This filter is applied prior to calculating the predistorted waveform. |

Parent topic:

Equalizer

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__idpd__measurement__sample__rate.html language=enus -->
## TOPIC 00131: Measurement Sample Rate

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__idpd__measurement__sample__rate.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__idpd__measurement__sample__rate.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATESpecifies the acquisition sample rate, in S/s, when you set the RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE_MODE is User. Users should read back the actual sample rate used by the measurement. Actual sample rate may d

### Measurement Sample Rate

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE | Specifies the acquisition sample rate, in S/s, when you set the RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE_MODE is User. Users should read back the actual sample rate used by the measurement. Actual sample rate may differ from requested sample rate in order to ensure a waveform is phase continuous. |
| RFMXSPECAN_ATTR_IDPD_MEASUREMENT_SAMPLE_RATE_MODE | Specifies acquisition sample rate configuration mode. |

#### Attachments

None

Parent topic:

IDPD

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im.html language=enus -->
## TOPIC 00132: IM

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAdvancedAveragingFFTFundamentalIntermodRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXSPECAN_ATTR_IM_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the IM measurement. RFMXSPECAN_ATTR_IM_AMPLITUDE_CORRECTION_TYPESpecifies whethe

### IM

#### Groups

- Advanced
- Averaging
- FFT
- Fundamental
- Intermod
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IM_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the IM measurement. |
| RFMXSPECAN_ATTR_IM_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. |
| RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED | Specifies whether the measurement computes the intermod frequencies or uses user-specified frequencies. |
| RFMXSPECAN_ATTR_IM_FREQUENCY_DEFINITION | Specifies whether the tones and intermod frequencies are relative to the RF RFMXSPECAN_ATTR_CENTER_FREQUENCY, or are absolute frequencies. |
| RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED | Specifies whether to enable a local peak search around the tone or intermod frequencies to account for small frequency offsets. |
| RFMXSPECAN_ATTR_IM_MAXIMUM_INTERMOD_ORDER | Specifies the order up to which the RFmx driver measures odd order intermodulation products when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. The lower and upper intermodulation products are measured for each order. |
| RFMXSPECAN_ATTR_IM_MEASUREMENT_ENABLED | Specifies whether to enable the IM measurement. |
| RFMXSPECAN_ATTR_IM_MEASUREMENT_METHOD | Specifies the method used to perform the IM measurement. |
| RFMXSPECAN_ATTR_IM_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the IM measurement. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im_1ga15698ce37222ec07a6095a85e223b62b.html language=enus -->
## TOPIC 00133: RFMXSPECAN_ATTR_IM_MEASUREMENT_METHOD

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im_1ga15698ce37222ec07a6095a85e223b62b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im_1ga15698ce37222ec07a6095a85e223b62b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to perform the IM measurement. SyntaxRFMXSPECAN_ATTR_IM_MEASUREMENT_METHODNumeric ValueData TypeAccessApplies To1114125int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXSPECAN_ATTR_IM_MEASUREMENT_METHOD

Specifies the method used to perform the IM measurement.

#### Syntax

RFMXSPECAN_ATTR_IM_MEASUREMENT_METHOD

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114125 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_NORMAL | 0 (0x0) | The IM measurement acquires the spectrum using the same signal analyzer settings across frequency bands. Use this method when the fundamental tone separation is not large. Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668. |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_DYNAMIC_RANGE | 1 (0x1) | The IM measurement acquires a segmented spectrum using the signal analyzer specific optimizations for different frequency bands. The spectrum is acquired in segments, one per tone or intermod frequency to be measured. The span of each acquired spectral segment is equal to the frequency separation between the two input tones, or 1 MHz, whichever is smaller. Use this method to configure the IM measurement and the signal analyzer for maximum dynamic range instead of measurement speed.Supported devices: PXIe-5665/5668. |
| RFMXSPECAN_VAL_IM_MEASUREMENT_METHOD_SEGMENTED | 2 (0x2) | Similar to the Dynamic Range method, this method also acquires a segmented spectrum, except that signal analyzer is not explicitly configured to provide maximum dynamic range. Use this method when the frequency separation of the two input tones is large and the measurement accuracy can be traded off for measurement speed.Supported devices: PXIe-5644/5645/5646/5840/5841/5842/5860/5830/5831/5832, PXIe-5663/5665/5668. |

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__advanced_1gaf8d10effd6ef88fa057a25173dde5929.html language=enus -->
## TOPIC 00134: RFMXSPECAN_ATTR_IM_IF_OUTPUT_POWER_OFFSET_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__advanced_1gaf8d10effd6ef88fa057a25173dde5929.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__advanced_1gaf8d10effd6ef88fa057a25173dde5929.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This attribute is used only if you set the RFMXSPECAN_ATTR_IM_MEASUREMENT_METHOD attribute to Dynamic Range. SyntaxRFMXSPECAN_ATTR_IM_IF_OUTPUT_POWER_OFF

### RFMXSPECAN_ATTR_IM_IF_OUTPUT_POWER_OFFSET_AUTO

Specifies whether the measurement computes an IF output power level offset for the intermods to maximize the dynamic range of the signal analyzer. This attribute is used only if you set the [RFMXSPECAN_ATTR_IM_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__im_1ga15698ce37222ec07a6095a85e223b62b.html) attribute to **Dynamic Range**.

#### Syntax

RFMXSPECAN_ATTR_IM_IF_OUTPUT_POWER_OFFSET_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114137 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IM_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE | 0 (0x0) | The measurement sets the IF output power level offset using the values of the RFMXSPECAN_ATTR_IM_NEAR_IF_OUTPUT_POWER_OFFSET and RFMXSPECAN_ATTR_IM_FAR_IF_OUTPUT_POWER_OFFSET attributes. |
| RFMXSPECAN_VAL_IM_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE | 1 (0x1) | The measurement computes an IF output power level offset for the intermods to improve the dynamic range of the IM measurement. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__averaging_1ga1b88a64e77d7b8d088debcb63cec92c7.html language=enus -->
## TOPIC 00135: RFMXSPECAN_ATTR_IM_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__averaging_1ga1b88a64e77d7b8d088debcb63cec92c7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__averaging_1ga1b88a64e77d7b8d088debcb63cec92c7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_IM_AVERAGING_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_IM_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1114132int32Read/WriteN/ARemarks You do not need to use a selector string to configure or rea

### RFMXSPECAN_ATTR_IM_AVERAGING_COUNT

Specifies the number of acquisitions used for averaging when you set the [RFMXSPECAN_ATTR_IM_AVERAGING_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im__averaging_1gac3a0aa677fe4aa81717be00ff670f225.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_IM_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114132 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__fft.html language=enus -->
## TOPIC 00136: FFT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__fft.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__fft.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_IM_FFT_PADDINGSpecifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: RFMXSPECAN_ATTR_IM_FFT_WINDOWSpecifies the FFT window type to use to reduce spectral leakage. Attac

### FFT

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IM_FFT_PADDING | Specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: |
| RFMXSPECAN_ATTR_IM_FFT_WINDOW | Specifies the FFT window type to use to reduce spectral leakage. |

#### Attachments

None

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__fft_1ga2a5011ded9365556a5ca1bf84c4caab4.html language=enus -->
## TOPIC 00137: RFMXSPECAN_ATTR_IM_FFT_PADDING

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__fft_1ga2a5011ded9365556a5ca1bf84c4caab4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__fft_1ga2a5011ded9365556a5ca1bf84c4caab4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula: SyntaxRFMXSPECAN_ATTR_IM_FFT_PADDINGNumeric ValueData TypeAccessApplies To1114136float64Read/WriteN/ARemarksFFT size = waveform size * paddingThis attribute is used on

### RFMXSPECAN_ATTR_IM_FFT_PADDING

Specifies the factor by which the time-domain waveform is zero-padded before an FFT. The FFT size is given by the following formula:

#### Syntax

RFMXSPECAN_ATTR_IM_FFT_PADDING

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114136 | float64 | Read/Write | N/A |

#### Remarks

*FFT size* = *waveform size* * *padding*

This attribute is used only when the acquisition span is less than the device instantaneous bandwidth.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is -1.

Parent topic:

FFT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__intermod.html language=enus -->
## TOPIC 00138: Intermod

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__intermod.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__intermod.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_IM_INTERMOD_ENABLEDSpecifies whether to enable an intermod for the IM measurement. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. RFMXSPECAN_ATTR_IM_INTERMOD_ORDERSpecifies the order

### Intermod

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IM_INTERMOD_ENABLED | Specifies whether to enable an intermod for the IM measurement. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_IM_INTERMOD_ORDER | Specifies the order of the intermod. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_IM_INTERMOD_SIDE | Specifies whether to measure intermodulation products corresponding to both lower and upper intermod frequencies or either one of them. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY | Specifies the frequency of the lower intermodulation product. This value is expressed in Hz. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_IM_NUMBER_OF_INTERMODS | Specifies the number of intermods to measure when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to False. |
| RFMXSPECAN_ATTR_IM_UPPER_INTERMOD_FREQUENCY | Specifies the frequency of the upper intermodulation product. This value is expressed in Hz. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. |

#### Attachments

None

Parent topic:

IM

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__intermod_1ga251b3f68887778b531fb12460b4d9eb4.html language=enus -->
## TOPIC 00139: RFMXSPECAN_ATTR_IM_INTERMOD_ORDER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__intermod_1ga251b3f68887778b531fb12460b4d9eb4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__intermod_1ga251b3f68887778b531fb12460b4d9eb4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the order of the intermod. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_IM_INTERMOD_ORDERNumeric ValueData TypeAccessApplies To1114121int32Read/WriteIntermodRemarks Use "intermod<n>" as the Selector Str

### RFMXSPECAN_ATTR_IM_INTERMOD_ORDER

Specifies the order of the intermod. This attribute is not used when you set the [RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im_1gae977834382c65591476900915ad7ca4d.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_IM_INTERMOD_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114121 | int32 | Read/Write | Intermod |

#### Remarks

Use "intermod<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 3.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__intermod_1ga7d9eb3467a34778717ef1845c179c523.html language=enus -->
## TOPIC 00140: RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__intermod_1ga7d9eb3467a34778717ef1845c179c523.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__intermod_1ga7d9eb3467a34778717ef1845c179c523.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency of the lower intermodulation product. This value is expressed in Hz. This attribute is not used when you set the RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED attribute to True. SyntaxRFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCYNumeric ValueData TypeAccessApplies To1114123fl

### RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY

Specifies the frequency of the lower intermodulation product. This value is expressed in Hz. This attribute is not used when you set the [RFMXSPECAN_ATTR_IM_AUTO_INTERMODS_SETUP_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im_1gae977834382c65591476900915ad7ca4d.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_IM_LOWER_INTERMOD_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114123 | float64 | Read/Write | Intermod |

#### Remarks

Use "intermod<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is -3 MHz.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__rbw__filter_1gaba1c948c08935750606e954772f54df2.html language=enus -->
## TOPIC 00141: RFMXSPECAN_ATTR_IM_RBW_FILTER_AUTO_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__rbw__filter_1gaba1c948c08935750606e954772f54df2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__rbw__filter_1gaba1c948c08935750606e954772f54df2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. SyntaxRFMXSPECAN_ATTR_IM_RBW_FILTER_AUTO_BANDWIDTHNumeric ValueData TypeAccessApplies To1114126int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Sele

### RFMXSPECAN_ATTR_IM_RBW_FILTER_AUTO_BANDWIDTH

Specifies whether the measurement computes the RBW.

#### Syntax

RFMXSPECAN_ATTR_IM_RBW_FILTER_AUTO_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114126 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IM_RBW_FILTER_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the RBW that you specify in the RFMXSPECAN_ATTR_IM_RBW_FILTER_BANDWIDTH attribute. |
| RFMXSPECAN_VAL_IM_RBW_FILTER_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement computes the RBW. |

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__fundamental_1ga4a0f148a8d95ecf8c6d371b2e0c5a678.html language=enus -->
## TOPIC 00142: RFMXSPECAN_ATTR_IM_RESULTS_UPPER_TONE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__fundamental_1ga4a0f148a8d95ecf8c6d371b2e0c5a678.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__fundamental_1ga4a0f148a8d95ecf8c6d371b2e0c5a678.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured around the upper tone frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to True. This value is expressed in dBm. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the power at the upper tone frequ

### RFMXSPECAN_ATTR_IM_RESULTS_UPPER_TONE_POWER

Returns the peak power measured around the upper tone frequency when you set the [RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im_1ga3c80980f5d785cf802fb14182d87f53a.html) attribute to **True**. This value is expressed in dBm. When you set the IM Local Peak Search Enabled attribute to **False**, the measurement returns the power at the upper tone frequency.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_UPPER_TONE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114145 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Fundamental

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga012d6cd83375a4608f121c95a9a22170.html language=enus -->
## TOPIC 00143: RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga012d6cd83375a4608f121c95a9a22170.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga012d6cd83375a4608f121c95a9a22170.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the worst case intermod power that is equal to the maximum of the values of both the RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_POWER and RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_POWER results. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_ABSOLUTE_POWE

### RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_ABSOLUTE_POWER

Returns the worst case intermod power that is equal to the maximum of the values of both the [RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_POWER](group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga20505738b1c5eac3f27170479cbfc24b.html) and [RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_POWER](group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gabd90d651e9f1d4437b2c61b46cc1ce55.html) results. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114162 | float64 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga4f52114a420ff831217312ee0a6a0745.html language=enus -->
## TOPIC 00144: RFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga4f52114a420ff831217312ee0a6a0745.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga4f52114a420ff831217312ee0a6a0745.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result. SyntaxRFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWERNumeric ValueData TypeAccessApplies To1114151float64Read-OnlyIntermodRemarks Use "intermod<n>" as the s

### RFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER

Returns the lower output intercept power. This value is expressed in dBm. Refer to the IM topic for more information about this result.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114151 | float64 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga8aee88c5e6d45e9f3df4c71bde844ed2.html language=enus -->
## TOPIC 00145: RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_OUTPUT_INTERCEPT_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga8aee88c5e6d45e9f3df4c71bde844ed2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga8aee88c5e6d45e9f3df4c71bde844ed2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the worst case output intercept power which is equal to the minimum of the values of the RFMXSPECAN_ATTR_IM_RESULTS_UPPER_OUTPUT_INTERCEPT_POWER and RFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER results. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_OU

### RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_OUTPUT_INTERCEPT_POWER

Returns the worst case output intercept power which is equal to the minimum of the values of the [RFMXSPECAN_ATTR_IM_RESULTS_UPPER_OUTPUT_INTERCEPT_POWER](group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga05e3ad9ae98f52c1176e9b489446e706.html) and [RFMXSPECAN_ATTR_IM_RESULTS_LOWER_OUTPUT_INTERCEPT_POWER](group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga4f52114a420ff831217312ee0a6a0745.html) results. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_OUTPUT_INTERCEPT_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114153 | float64 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga9c1f557eb832bef2996b1e3cd19dd169.html language=enus -->
## TOPIC 00146: RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga9c1f557eb832bef2996b1e3cd19dd169.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga9c1f557eb832bef2996b1e3cd19dd169.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relative peak power measured around the lower intermod frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to True. This value is expressed in dBc. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the relative power a

### RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_RELATIVE_POWER

Returns the relative peak power measured around the lower intermod frequency when you set the [RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im_1ga3c80980f5d785cf802fb14182d87f53a.html) attribute to **True**. This value is expressed in dBc. When you set the IM Local Peak Search Enabled attribute to **False**, the measurement returns the relative power at the lower intermod frequency.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114160 | float64 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gacc008489e1a3828beee42788add4df2b.html language=enus -->
## TOPIC 00147: RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gacc008489e1a3828beee42788add4df2b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gacc008489e1a3828beee42788add4df2b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the worst case intermod relative power that is equal to the maximum of the values of both the RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_RELATIVE_POWER and RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_RELATIVE_POWER results. This value is expressed in dBc. SyntaxRFMXSPECAN_ATTR_IM_RESULTS_WORST_

### RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_RELATIVE_POWER

Returns the worst case intermod relative power that is equal to the maximum of the values of both the [RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_RELATIVE_POWER](group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gaceda235534080edbefa36b25819e71b3.html) and [RFMXSPECAN_ATTR_IM_RESULTS_LOWER_INTERMOD_RELATIVE_POWER](group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1ga9c1f557eb832bef2996b1e3cd19dd169.html) results. This value is expressed in dBc.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_WORST_CASE_INTERMOD_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114163 | float64 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gaceda235534080edbefa36b25819e71b3.html language=enus -->
## TOPIC 00148: RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_RELATIVE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gaceda235534080edbefa36b25819e71b3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gaceda235534080edbefa36b25819e71b3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the relative peak power measured around the upper intermod frequency when you set the RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED attribute to True. This value is expressed in dBc. When you set the IM Local Peak Search Enabled attribute to False, the measurement returns the relative power a

### RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_RELATIVE_POWER

Returns the relative peak power measured around the upper intermod frequency when you set the [RFMXSPECAN_ATTR_IM_LOCAL_PEAK_SEARCH_ENABLED](group____root__ni_r_fmx_spec_an__attributes__im_1ga3c80980f5d785cf802fb14182d87f53a.html) attribute to **True**. This value is expressed in dBc. When you set the IM Local Peak Search Enabled attribute to **False**, the measurement returns the relative power at the upper intermod frequency.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_UPPER_INTERMOD_RELATIVE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114161 | float64 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gadfb0ff0aed447495378d85d3b67771e0.html language=enus -->
## TOPIC 00149: RFMXSPECAN_ATTR_IM_RESULTS_INTERMOD_ORDER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gadfb0ff0aed447495378d85d3b67771e0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__results__intermod_1gadfb0ff0aed447495378d85d3b67771e0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the order of the intermod. SyntaxRFMXSPECAN_ATTR_IM_RESULTS_INTERMOD_ORDERNumeric ValueData TypeAccessApplies To1114146int32Read-OnlyIntermodRemarks Use "intermod<n>" as the selector string to read this result.

### RFMXSPECAN_ATTR_IM_RESULTS_INTERMOD_ORDER

Returns the order of the intermod.

#### Syntax

RFMXSPECAN_ATTR_IM_RESULTS_INTERMOD_ORDER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114146 | int32 | Read-Only | Intermod |

#### Remarks

Use "intermod<n>" as the selector string to read this result.

Parent topic:

Intermod

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__im__sweep__time_1ga7202d81827df38a9620c49836aae6ac0.html language=enus -->
## TOPIC 00150: RFMXSPECAN_ATTR_IM_SWEEP_TIME_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__im__sweep__time_1ga7202d81827df38a9620c49836aae6ac0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__im__sweep__time_1ga7202d81827df38a9620c49836aae6ac0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXSPECAN_ATTR_IM_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To1114129int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXSPECAN_ATTR_IM_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXSPECAN_ATTR_IM_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1114129 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_IM_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_IM_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement computes the sweep time based on the value of the RFMXSPECAN_ATTR_IM_RBW_FILTER_BANDWIDTH attribute. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__iq.html language=enus -->
## TOPIC 00151: IQ

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__iq.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__iq.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsBandwidthGroup membersNameDescriptionRFMXSPECAN_ATTR_IQ_ACQUISITION_TIMESpecifies the acquisition time for the I/Q measurement. This value is expressed in seconds. RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCHSpecifies whether the measurement deletes the fetched record. RFMXSPECAN_ATTR_IQ_MEASUREM

### IQ

#### Groups

- Bandwidth

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_IQ_ACQUISITION_TIME | Specifies the acquisition time for the I/Q measurement. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCH | Specifies whether the measurement deletes the fetched record. |
| RFMXSPECAN_ATTR_IQ_MEASUREMENT_ENABLED | Specifies whether to enable the I/Q measurement. |
| RFMXSPECAN_ATTR_IQ_MEASUREMENT_MODE | Specifies the mode for performing the IQ measurement. |
| RFMXSPECAN_ATTR_IQ_NUMBER_OF_RECORDS | Specifies the number of records to acquire. |
| RFMXSPECAN_ATTR_IQ_PRETRIGGER_TIME | Specifies the pretrigger time for the I/Q measurement. This value is expressed in seconds. |
| RFMXSPECAN_ATTR_IQ_SAMPLE_RATE | Specifies the acquisition sample rate. This value is expressed in samples per second (S/s). |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__iq_1ga12ff377f86faf2ef50a73aa837245726.html language=enus -->
## TOPIC 00152: RFMXSPECAN_ATTR_IQ_NUMBER_OF_RECORDS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__iq_1ga12ff377f86faf2ef50a73aa837245726.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__iq_1ga12ff377f86faf2ef50a73aa837245726.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of records to acquire. SyntaxRFMXSPECAN_ATTR_IQ_NUMBER_OF_RECORDSNumeric ValueData TypeAccessApplies To1110275int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topi

### RFMXSPECAN_ATTR_IQ_NUMBER_OF_RECORDS

Specifies the number of records to acquire.

#### Syntax

RFMXSPECAN_ATTR_IQ_NUMBER_OF_RECORDS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110275 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__iq_1ga7410377d53138869cde776a626d1d63a.html language=enus -->
## TOPIC 00153: RFMXSPECAN_ATTR_IQ_ACQUISITION_TIME

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__iq_1ga7410377d53138869cde776a626d1d63a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__iq_1ga7410377d53138869cde776a626d1d63a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the acquisition time for the I/Q measurement. This value is expressed in seconds. SyntaxRFMXSPECAN_ATTR_IQ_ACQUISITION_TIMENumeric ValueData TypeAccessApplies To1110276float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default s

### RFMXSPECAN_ATTR_IQ_ACQUISITION_TIME

Specifies the acquisition time for the I/Q measurement. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_IQ_ACQUISITION_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110276 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.001.

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__iq_1ga8c6c04a944542c035e570447d96c27f7.html language=enus -->
## TOPIC 00154: RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__iq_1ga8c6c04a944542c035e570447d96c27f7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__iq_1ga8c6c04a944542c035e570447d96c27f7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement deletes the fetched record. SyntaxRFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCHNumeric ValueData TypeAccessApplies To1110282int32Read/WriteN/ARemarks The default value is True.NameValueDescriptionRFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_FALSE0 (0x0)The measurement does

### RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCH

Specifies whether the measurement deletes the fetched record.

#### Syntax

RFMXSPECAN_ATTR_IQ_DELETE_RECORD_ON_FETCH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110282 | int32 | Read/Write | N/A |

#### Remarks

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_FALSE | 0 (0x0) | The measurement does not delete the fetched record. |
| RFMXSPECAN_VAL_IQ_DELETE_RECORD_ON_FETCH_TRUE | 1 (0x1) | The measurement deletes the fetched record. |

Parent topic:

IQ

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__iq__bandwidth_1ga0f08ac09294f8fbe5284673c9578dc3f.html language=enus -->
## TOPIC 00155: RFMXSPECAN_ATTR_IQ_BANDWIDTH_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__iq__bandwidth_1ga0f08ac09294f8fbe5284673c9578dc3f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__iq__bandwidth_1ga0f08ac09294f8fbe5284673c9578dc3f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum acquisition bandwidth. SyntaxRFMXSPECAN_ATTR_IQ_BANDWIDTH_AUTONumeric ValueData TypeAccessApplies To1110280int32Read/WriteN/ARemarks The default value is True.NameValueDescriptionRFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_FALSE0 (0x0)The measurement uses

### RFMXSPECAN_ATTR_IQ_BANDWIDTH_AUTO

Specifies whether the measurement computes the minimum acquisition bandwidth.

#### Syntax

RFMXSPECAN_ATTR_IQ_BANDWIDTH_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1110280 | int32 | Read/Write | N/A |

#### Remarks

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_FALSE | 0 (0x0) | The measurement uses the value of the RFMXSPECAN_ATTR_IQ_BANDWIDTH attribute as the minimum acquisition bandwidth. |
| RFMXSPECAN_VAL_IQ_AUTO_BANDWIDTH_TRUE | 1 (0x1) | The measurement uses 0.8 * sample rate as the minimum signal bandwidth. |

Parent topic:

Bandwidth

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__list.html language=enus -->
## TOPIC 00156: List

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__list.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__list.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsStepGroup membersNameDescriptionRFMXSPECAN_ATTR_NUMBER_OF_STEPSSpecifies the number of active steps in a list. AttachmentsNone

### List

#### Groups

- Step

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NUMBER_OF_STEPS | Specifies the number of active steps in a list. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__list_1gaf32b8675bd6057b357b5917da2f69727.html language=enus -->
## TOPIC 00157: RFMXSPECAN_ATTR_NUMBER_OF_STEPS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__list_1gaf32b8675bd6057b357b5917da2f69727.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__list_1gaf32b8675bd6057b357b5917da2f69727.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of active steps in a list. SyntaxRFMXSPECAN_ATTR_NUMBER_OF_STEPSNumeric ValueData TypeAccessApplies To1052664int32Read/WriteN/ARemarks You need to use a selector string to configure or read this attribute for the list instance.The default value is 0.

### RFMXSPECAN_ATTR_NUMBER_OF_STEPS

Specifies the number of active steps in a list.

#### Syntax

RFMXSPECAN_ATTR_NUMBER_OF_STEPS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1052664 | int32 | Read/Write | N/A |

#### Remarks

You need to use a selector string to configure or read this attribute for the list instance.

The default value is 0.

Parent topic:

List

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf_1ga6231b655350ce024e4af7e1b70edb97e.html language=enus -->
## TOPIC 00158: RFMXSPECAN_ATTR_NF_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf_1ga6231b655350ce024e4af7e1b70edb97e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf_1ga6231b655350ce024e4af7e1b70edb97e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the noise figure (NF) measurement. SyntaxRFMXSPECAN_ATTR_NF_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1179649int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String top

### RFMXSPECAN_ATTR_NF_MEASUREMENT_ENABLED

Enables the noise figure (NF) measurement.

#### Syntax

RFMXSPECAN_ATTR_NF_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179649 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf_1ga956358da155c892930adcfc412b3c7ae.html language=enus -->
## TOPIC 00159: RFMXSPECAN_ATTR_NF_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf_1ga956358da155c892930adcfc412b3c7ae.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf_1ga956358da155c892930adcfc412b3c7ae.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the noise figure (NF) measurement. SyntaxRFMXSPECAN_ATTR_NF_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1179681int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The nu

### RFMXSPECAN_ATTR_NF_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the noise figure (NF) measurement.

#### Syntax

RFMXSPECAN_ATTR_NF_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179681 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

The default value is 1.

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf_1gaf67ba4f63e9445d75070fd29426d4b69.html language=enus -->
## TOPIC 00160: RFMXSPECAN_ATTR_NF_CALIBRATION_SETUP_ID

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf_1gaf67ba4f63e9445d75070fd29426d4b69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf_1gaf67ba4f63e9445d75070fd29426d4b69.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Associates a unique string identifier with the hardware setup used to perform calibration for the NF measurement. SyntaxRFMXSPECAN_ATTR_NF_CALIBRATION_SETUP_IDNumeric ValueData TypeAccessApplies To1179700char[]Read/WriteN/ARemarks You do not need to use a selector string to configure or read this at

### RFMXSPECAN_ATTR_NF_CALIBRATION_SETUP_ID

Associates a unique string identifier with the hardware setup used to perform calibration for the NF measurement.

#### Syntax

RFMXSPECAN_ATTR_NF_CALIBRATION_SETUP_ID

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179700 | char[] | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty string.

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf_1gafd7c2f04bb6af47f1b859fc7b083abf2.html language=enus -->
## TOPIC 00161: RFMXSPECAN_ATTR_NF_MEASUREMENT_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf_1gafd7c2f04bb6af47f1b859fc7b083abf2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf_1gafd7c2f04bb6af47f1b859fc7b083abf2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_NF_MEASUREMENT_BANDWIDTHNumeric ValueData TypeAccessApplies To1179653float64Read/WriteN/ARemarks The default value is 100 kHz.

### RFMXSPECAN_ATTR_NF_MEASUREMENT_BANDWIDTH

Specifies the effective noise-bandwidth in which power measurements are performed for the noise figure (NF) measurement. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_NF_MEASUREMENT_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179653 | float64 | Read/Write | N/A |

#### Remarks

The default value is 100 kHz.

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__advanced.html language=enus -->
## TOPIC 00162: Advanced

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__advanced.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__advanced.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_DEVICE_TEMPERATURE_TOLERANCESpecifies the tolerance for device temperature beyond which the calibration data is considered invalid. This value is expressed in Celsius. AttachmentsNone

### Advanced

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_DEVICE_TEMPERATURE_TOLERANCE | Specifies the tolerance for device temperature beyond which the calibration data is considered invalid. This value is expressed in Celsius. |

#### Attachments

None

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__averaging_1ga92dca58b5cd53985a4061a5ce451f25e.html language=enus -->
## TOPIC 00163: RFMXSPECAN_ATTR_NF_AVERAGING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__averaging_1ga92dca58b5cd53985a4061a5ce451f25e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__averaging_1ga92dca58b5cd53985a4061a5ce451f25e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the noise figure (NF) measurement. SyntaxRFMXSPECAN_ATTR_NF_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To1179655int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance.

### RFMXSPECAN_ATTR_NF_AVERAGING_ENABLED

Specifies whether to enable averaging for the noise figure (NF) measurement.

#### Syntax

RFMXSPECAN_ATTR_NF_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179655 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_NF_AVERAGING_ENABLED_TRUE | 1 (0x1) | The NF measurement uses the value of the RFMXSPECAN_ATTR_NF_AVERAGING_COUNT attribute as the number of acquisitions for each frequency which you specify in the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, over which the NF measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__dut_1gafb668908fb198873d28a617d70232330.html language=enus -->
## TOPIC 00164: RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S12

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__dut_1gafb668908fb198873d28a617d70232330.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__dut_1gafb668908fb198873d28a617d70232330.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of the input-isolations of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the RFMXSPECAN_ATTR_NF_COLD_SO

### RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S12

Specifies an array of the input-isolations of the DUT as a function of frequency, when the input port of the DUT is terminated with an impedance equal to the characteristic impedance. This value is expressed in dB. The corresponding array of frequencies is specified by the [RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S_PARAMETERS_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__dut_1gaaa63ec12c9b29ef71f486362a4c4a1db.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_NF_COLD_SOURCE_DUT_S12

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179696 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

DUT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__input__termination.html language=enus -->
## TOPIC 00165: Input Termination

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__input__termination.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__input__termination.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURESpecifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin. RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_VS

### Input Termination

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURE | Specifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin. |
| RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_VSWR | Specifies an array of voltage standing wave ratios (VSWR) as a function of frequency of the microwave termination used as the noise source in cold source method. The corresponding array of frequencies is specified by the RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_VSWR_FREQUENCY attribute. |
| RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_VSWR_FREQUENCY | Specifies an array of frequencies corresponding to the voltage standing wave ratios (VSWR) of the microwave termination used in the cold source method as specified by the RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_VSWR attribute. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Cold Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__input__termination_1ga6727ad7189b8ba70dd2b2874bf0b7886.html language=enus -->
## TOPIC 00166: RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__input__termination_1ga6727ad7189b8ba70dd2b2874bf0b7886.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__cold__source__input__termination_1ga6727ad7189b8ba70dd2b2874bf0b7886.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin. SyntaxRFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURENumeric ValueData TypeAccessApplies To1179694float64Read/WriteN/ARemarks You do not

### RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURE

Specifies the physical temperature of the microwave termination used as the noise source in the cold source method. This value is expressed in kelvin.

#### Syntax

RFMXSPECAN_ATTR_NF_COLD_SOURCE_INPUT_TERMINATION_TEMPERATURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179694 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 297.

Parent topic:

Input Termination

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__external__preamp.html language=enus -->
## TOPIC 00167: External Preamp

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__external__preamp.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__external__preamp.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_FREQUENCYSpecifies the array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_GAIN attribute. RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_GAINSpecifies the gain of the external preamp as a function of

### External Preamp

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_FREQUENCY | Specifies the array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_GAIN attribute. |
| RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_GAIN | Specifies the gain of the external preamp as a function of frequency. The value is expressed in dB. |
| RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENT | Specifies if an external preamplifier is present in the signal path. |

#### Attachments

None

Parent topic:

NF

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__external__preamp_1ga4639af48fac1c1a92d1294a40cca5336.html language=enus -->
## TOPIC 00168: RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__external__preamp_1ga4639af48fac1c1a92d1294a40cca5336.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__external__preamp_1ga4639af48fac1c1a92d1294a40cca5336.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if an external preamplifier is present in the signal path. SyntaxRFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENTNumeric ValueData TypeAccessApplies To1179701int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Re

### RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENT

Specifies if an external preamplifier is present in the signal path.

#### Syntax

RFMXSPECAN_ATTR_NF_EXTERNAL_PREAMP_PRESENT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179701 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_FALSE | 0 (0x0) | No external preamplifier present in the signal path. |
| RFMXSPECAN_VAL_NF_EXTERNAL_PREAMP_PRESENT_TRUE | 1 (0x1) | An external preamplifier present in the signal path. |

Parent topic:

External Preamp

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__frequency__converter_1ga1a5537cbbd94d8cde237796bc7559ee2.html language=enus -->
## TOPIC 00169: RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_IMAGE_REJECTION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__frequency__converter_1ga1a5537cbbd94d8cde237796bc7559ee2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__frequency__converter_1ga1a5537cbbd94d8cde237796bc7559ee2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the gain ratio of the DUT at the image frequency to that at the RF frequency. This value is expressed in dB. Refer to NF concept help for more details. SyntaxRFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_IMAGE_REJECTIONNumeric ValueData TypeAccessApplies To1179712float64Read/WriteN/ARemarks You d

### RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_IMAGE_REJECTION

Specifies the gain ratio of the DUT at the image frequency to that at the RF frequency. This value is expressed in dB. Refer to NF concept help for more details.

#### Syntax

RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_IMAGE_REJECTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179712 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 999.99 dB.

Parent topic:

Frequency Converter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__frequency__converter_1ga7a6e9565630cd1dfa64824665e172c07.html language=enus -->
## TOPIC 00170: RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_LO_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__frequency__converter_1ga7a6e9565630cd1dfa64824665e172c07.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__frequency__converter_1ga7a6e9565630cd1dfa64824665e172c07.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the fixed LO frequency of the DUT when you set the RFMXSPECAN_ATTR_NF_DUT_TYPE attribute to either Downconverter or Upconverter. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_LO_FREQUENCYNumeric ValueData TypeAccessApplies To1179708float64Read/WriteN/ARemarks

### RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_LO_FREQUENCY

Specifies the fixed LO frequency of the DUT when you set the [RFMXSPECAN_ATTR_NF_DUT_TYPE](group____root__ni_r_fmx_spec_an__attributes__nf_1ga3d8a2a2c2634cb3558c94c7861768ac9.html) attribute to either **Downconverter** or **Upconverter**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_NF_FREQUENCY_CONVERTER_LO_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179708 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 MHz.

Parent topic:

Frequency Converter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__calibration_1ga3eef749c40c77212fdf5d681227635b2.html language=enus -->
## TOPIC 00171: RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_COMPENSATION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__calibration_1ga3eef749c40c77212fdf5d681227635b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__calibration_1ga3eef749c40c77212fdf5d681227635b2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. SyntaxRFMXSPECAN_ATT

### RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_COMPENSATION_ENABLED

Specifies whether the noise figure (NF) measurement accounts for the ohmic losses between the noise source and input port of the analyzer during the calibration step, excluding any losses which you have specified using the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1gacd20b6149733ab79712501ded248bf50.html) attribute.

#### Syntax

RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179677 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_CALIBRATION_LOSS_COMPENSATION_ENABLED_FALSE | 0 (0x0) | The NF measurement ignores the ohmic losses. |
| RFMXSPECAN_VAL_NF_CALIBRATION_LOSS_COMPENSATION_ENABLED_TRUE | 1 (0x1) | The NF measurement accounts for the ohmic losses. |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__calibration_1gaef03e02c66588872fb9a6d6e39d0d116.html language=enus -->
## TOPIC 00172: RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__calibration_1gaef03e02c66588872fb9a6d6e39d0d116.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__calibration_1gaef03e02c66588872fb9a6d6e39d0d116.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. This value is expressed in Hz. This attribute is applicable only when you set the RFMXSPECAN_ATTR_NF_Y_FACTOR_MODE attribute to Calibrate and set the RFMXSPECAN_ATTR_NF_MEASUREM

### RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_FREQUENCY

Specifies an array of frequencies corresponding to the ohmic losses between the source and the input port of the analyzer. This value is expressed in Hz. This attribute is applicable only when you set the [RFMXSPECAN_ATTR_NF_Y_FACTOR_MODE](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor_1ga13bda64456ae13eeb882c46955c1c891.html) attribute to **Calibrate** and set the [RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__nf_1ga4c9893b81ea5b8a00fa5a3c6f933fa24.html) attribute to **Y-Factor**, or when you set the [RFMXSPECAN_ATTR_NF_COLD_SOURCE_MODE](group____root__ni_r_fmx_spec_an__attributes__nf__cold__source_1ga1fb6b8cd00aa18089c86fddaca58f54c.html) attribute to **Calibrate** and set the NF Meas Method attribute to **Cold Source**.

#### Syntax

RFMXSPECAN_ATTR_NF_CALIBRATION_LOSS_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179679 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__input.html language=enus -->
## TOPIC 00173: DUT Input

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__input.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__input.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_DUT_INPUT_LOSSSpecifies an array of the ohmic losses between the noise source and the input port of the DUT, as a function of the frequency. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the RFMXS

### DUT Input

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS | Specifies an array of the ohmic losses between the noise source and the input port of the DUT, as a function of the frequency. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED attribute to True. You must exclude any loss which is inherent to the noise source and is common between the calibration and measurement steps, and configure the loss using the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. |
| RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_COMPENSATION_ENABLED | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the noise source and the input port of the DUT, excluding the losses that are common to calibration and the measurement steps for the Y-Factor method, which are specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. |
| RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_FREQUENCY | Specifies an array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS attribute. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS_TEMPERATURE | Specifies the physical temperature of the ohmic loss elements considered in the RFMXSPECAN_ATTR_NF_DUT_INPUT_LOSS attribute. This value is expressed in kelvin. |

#### Attachments

None

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output.html language=enus -->
## TOPIC 00174: DUT Output

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSSSpecifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measuremen

### DUT Output

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS | Specifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED | Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. |
| RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY | Specifies the array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS attribute. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_TEMPERATURE | Specifies the physical temperature of the ohmic loss elements specified by the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS attribute. This value is expressed in kelvin. |

#### Attachments

None

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga598d415e913aa659d749ddd6cd394a66.html language=enus -->
## TOPIC 00175: RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga598d415e913aa659d749ddd6cd394a66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga598d415e913aa659d749ddd6cd394a66.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of frequencies corresponding to the value of the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS attribute. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCYNumeric ValueData TypeAccessApplies To1179671AdoubleRead/WriteN/ARemarks You do not need to use a select

### RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY

Specifies the array of frequencies corresponding to the value of the [RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS](group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga7a2443d153ca24c6ee2157a9ebe87220.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179671 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

DUT Output

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga7a2443d153ca24c6ee2157a9ebe87220.html language=enus -->
## TOPIC 00176: RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga7a2443d153ca24c6ee2157a9ebe87220.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga7a2443d153ca24c6ee2157a9ebe87220.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABL

### RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS

Specifies the array of ohmic losses between the output port of the DUT and the input port of the analyzer, as a function of frequency. This value is expressed in dB. This loss is accounted for by the noise figure (NF) measurement when you set the [RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED](group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga847e9a4fc03cca90c88d12d17dd47c76.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179670 | Adouble | Read/Write | N/A |

#### Remarks

Specify the array of frequencies at which the losses were measured using the [RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga598d415e913aa659d749ddd6cd394a66.html) attribute.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

DUT Output

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga847e9a4fc03cca90c88d12d17dd47c76.html language=enus -->
## TOPIC 00177: RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga847e9a4fc03cca90c88d12d17dd47c76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__loss__dut__output_1ga847e9a4fc03cca90c88d12d17dd47c76.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer. SyntaxRFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To1179669int32Read/WriteN/ARemarks You do not need to

### RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED

Specifies whether the noise figure (NF) measurement accounts for ohmic losses between the output port of the DUT and the input port of the analyzer.

#### Syntax

RFMXSPECAN_ATTR_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179669 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_FALSE | 0 (0x0) | The NF measurement ignores ohmic losses. |
| RFMXSPECAN_VAL_NF_DUT_OUTPUT_LOSS_COMPENSATION_ENABLED_TRUE | 1 (0x1) | The NF measurement accounts for the ohmic losses. |

Parent topic:

DUT Output

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__results_1gacf4d1960baa915b71b05861c058f675e.html language=enus -->
## TOPIC 00178: RFMXSPECAN_ATTR_NF_RESULTS_ANALYZER_NOISE_FIGURE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__results_1gacf4d1960baa915b71b05861c058f675e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__results_1gacf4d1960baa915b71b05861c058f675e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the noise figures of the analyzer measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_NF_RESULTS_ANALYZER_NOISE_FIGURENumeric ValueData TypeAccessApplies To1179685AdoubleRead-OnlyN/ARemarks

### RFMXSPECAN_ATTR_NF_RESULTS_ANALYZER_NOISE_FIGURE

Returns an array of the noise figures of the analyzer measured at the frequencies specified by the [RFMXSPECAN_ATTR_NF_FREQUENCY_LIST](group____root__ni_r_fmx_spec_an__attributes__nf_1ga68d994a621e04ddd98faa4bfa1b827d9.html) attribute. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_NF_RESULTS_ANALYZER_NOISE_FIGURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179685 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__results__cold__source.html language=enus -->
## TOPIC 00179: Cold Source

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__results__cold__source.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__results__cold__source.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_RESULTS_COLD_SOURCE_POWERReturns the power measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMEN

### Cold Source

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_RESULTS_COLD_SOURCE_POWER | Returns the power measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Cold-source. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__results__dut_1gafcf666327dcbb319f6d1a50c6405ffdd.html language=enus -->
## TOPIC 00180: RFMXSPECAN_ATTR_NF_RESULTS_DUT_NOISE_FIGURE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__results__dut_1gafcf666327dcbb319f6d1a50c6405ffdd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__results__dut_1gafcf666327dcbb319f6d1a50c6405ffdd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the noise figures of the DUT measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. SyntaxRFMXSPECAN_ATTR_NF_RESULTS_DUT_NOISE_FIGURENumeric ValueData TypeAccessApplies To1179682AdoubleRead-OnlyN/ARemarks You do no

### RFMXSPECAN_ATTR_NF_RESULTS_DUT_NOISE_FIGURE

Returns an array of the noise figures of the DUT measured at the frequencies specified by the [RFMXSPECAN_ATTR_NF_FREQUENCY_LIST](group____root__ni_r_fmx_spec_an__attributes__nf_1ga68d994a621e04ddd98faa4bfa1b827d9.html) attribute. This value is expressed in dB.

#### Syntax

RFMXSPECAN_ATTR_NF_RESULTS_DUT_NOISE_FIGURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179682 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

DUT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__results__yfactor.html language=enus -->
## TOPIC 00181: Y-Factor

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__results__yfactor.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__results__yfactor.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_RESULTS_CALIBRATION_Y_FACTORReturns an array of the calibration Y-Factors measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. A valid result is returned only when you set the

### Y-Factor

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_RESULTS_CALIBRATION_Y_FACTOR | Returns an array of the calibration Y-Factors measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. |
| RFMXSPECAN_ATTR_NF_RESULTS_MEASUREMENT_Y_FACTOR | Returns an array of the measurement Y-Factors measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute. This value is expressed in dB. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. |
| RFMXSPECAN_ATTR_NF_RESULTS_Y_FACTOR_COLD_POWER | Returns the array of powers measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, when the noise source is disabled. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. |
| RFMXSPECAN_ATTR_NF_RESULTS_Y_FACTOR_HOT_POWER | Returns the array of powers measured at the frequencies specified by the RFMXSPECAN_ATTR_NF_FREQUENCY_LIST attribute, when the noise source is enabled. This value is expressed in dBm. A valid result is returned only when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor_1ga13bda64456ae13eeb882c46955c1c891.html language=enus -->
## TOPIC 00182: RFMXSPECAN_ATTR_NF_Y_FACTOR_MODE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor_1ga13bda64456ae13eeb882c46955c1c891.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor_1ga13bda64456ae13eeb882c46955c1c891.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_MODENumeric ValueData TypeAccessApplies To11796

### RFMXSPECAN_ATTR_NF_Y_FACTOR_MODE

Specifies whether the measurement should calibrate the noise characteristics of the analyzer or compute the noise characteristics of the DUT when you set the [RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__nf_1ga4c9893b81ea5b8a00fa5a3c6f933fa24.html) attribute to **Y-Factor**.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_MODE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179658 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_Y_FACTOR_MODE_MEASURE | 0 (0x0) | The noise figure (NF) measurement computes the noise characteristics of the DUT, compensating for the noise figure of the analyzer. |
| RFMXSPECAN_VAL_NF_Y_FACTOR_MODE_CALIBRATE | 1 (0x1) | The NF measurement computes the noise characteristics of the analyzer. |

Parent topic:

Y-Factor

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga07a0ba4b1129ba50ee08f9e621289551.html language=enus -->
## TOPIC 00183: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_OFF_TEMPERATURE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga07a0ba4b1129ba50ee08f9e621289551.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga07a0ba4b1129ba50ee08f9e621289551.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_OFF_TEMPERATURENumeric ValueData TypeAccessApplies To1179663float64Read/WriteN/ARemarks You do not

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_OFF_TEMPERATURE

Specifies the physical temperature of the noise source used in the Y-Factor method when the noise source is turned off. This value is expressed in kelvin.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_OFF_TEMPERATURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179663 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 297.

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga334af9326d5c2d787e0643426b1d9c2e.html language=enus -->
## TOPIC 00184: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga334af9326d5c2d787e0643426b1d9c2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga334af9326d5c2d787e0643426b1d9c2e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the noise source type for performing the noise figure (NF) measurement when you set the RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD attribute to Y-Factor. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPENumeric ValueData TypeAccessApplies To1179713int32Read/WriteN/ARemarks You do not need to

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE

Specifies the noise source type for performing the noise figure (NF) measurement when you set the [RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__nf_1ga4c9893b81ea5b8a00fa5a3c6f933fa24.html) attribute to **Y-Factor**.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179713 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **External Noise Source**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_EXTERNAL_NOISE_SOURCE | 0 (0x0) | The NF measurement generates noise using an external noise source, that is controlled either by an internal noise source power supply or an NI Source Measure Unit (SMU).Supported Devices: PXIe-5665 (3.6 GHz), PXIe-5668, PXIe-5644/5645/5646*, PXIe-5840*/5841*/5842*/5860*, PXIe 5830/5831*/5832* *Use an external NI Source Measure Unit (SMU) as the noise source power supply for the Noise Figure measurement. During initialization, specify the SMU resource name using "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You should allocate a dedicated SMU channel for RFmx. RFmx supports PXIe-4138, PXIe-4139, and PXIe-4139 (40 W) SMUs. |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_TYPE_RF_SIGNAL_GENERATOR | 1 (0x1) | When you measure Y-Factor based NF using a supported NI vector signal transceiver (VST) instrument, RFmx generates noise using the vector signal generator (VSG) integrated into the same VST. RFmx automatically configures the vector signal generator (VSG) to generate noise at the specified bandwidth and ENR levels that you set using the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY and RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR attributes.Supported Devices: PXIe-5842/5860 |

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga3a7a2e98493fa26515cd5d14ea25799b.html language=enus -->
## TOPIC 00185: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga3a7a2e98493fa26515cd5d14ea25799b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga3a7a2e98493fa26515cd5d14ea25799b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of frequencies corresponding to the effective noise ratio (ENR) values specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR attribute. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCYNumeric ValueData TypeAccessApplies To1179661A

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY

Specifies an array of frequencies corresponding to the effective noise ratio (ENR) values specified by the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga524e0413780c6a64fa92382a33949822.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179661 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga524e0413780c6a64fa92382a33949822.html language=enus -->
## TOPIC 00186: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga524e0413780c6a64fa92382a33949822.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga524e0413780c6a64fa92382a33949822.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of effective noise ratio (ENR) values of the noise source as a function of the frequency. This value is expressed in dB. The corresponding frequencies are specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY attribute. This attribute is used only when you set t

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR

Specifies the array of effective noise ratio (ENR) values of the noise source as a function of the frequency. This value is expressed in dB. The corresponding frequencies are specified by the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga3a7a2e98493fa26515cd5d14ea25799b.html) attribute. This attribute is used only when you set the [RFMXSPECAN_ATTR_NF_MEASUREMENT_METHOD](group____root__ni_r_fmx_spec_an__attributes__nf_1ga4c9893b81ea5b8a00fa5a3c6f933fa24.html) attribute to **Y-Factor**.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_ENR

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179660 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga9ca438dfd1593617402a22612808b98b.html language=enus -->
## TOPIC 00187: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_COLD_TEMPERATURE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga9ca438dfd1593617402a22612808b98b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga9ca438dfd1593617402a22612808b98b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the calibrated cold noise temperature of the noise source used in the Y-Factor method. This value is expressed in kelvin. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_COLD_TEMPERATURENumeric ValueData TypeAccessApplies To1179662float64Read/WriteN/ARemarks You do not need to use a selecto

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_COLD_TEMPERATURE

Specifies the calibrated cold noise temperature of the noise source used in the Y-Factor method. This value is expressed in kelvin.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_COLD_TEMPERATURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179662 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 302.8.

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga9e987cce3c0de2ec9af7051a2212b3dd.html language=enus -->
## TOPIC 00188: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_SETTLING_TIME

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga9e987cce3c0de2ec9af7051a2212b3dd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga9e987cce3c0de2ec9af7051a2212b3dd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This attribute is used only when you set the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE attribute to External Noise Source. This value is exp

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_SETTLING_TIME

Specifies the time to wait till the noise source used in the Y-Factor method settles to either hot or cold state when the noise source is turned on or off. This attribute is used only when you set the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_TYPE](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source_1ga334af9326d5c2d787e0643426b1d9c2e.html) attribute to **External Noise Source**. This value is expressed in seconds.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_SETTLING_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179664 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss.html language=enus -->
## TOPIC 00189: Loss

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSSSpecifies an array of the ohmic losses inherent to the noise source used in the Y-Factor method. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the RFMXSPECAN_ATTR_NF_Y_FA

### Loss

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS | Specifies an array of the ohmic losses inherent to the noise source used in the Y-Factor method. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED | Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. |
| RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY | Specifies the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. This value is expressed in Hz. |
| RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_TEMPERATURE | Specifies the physical temperature of the ohmic loss elements specified in the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. This value is expressed in kelvin. |

#### Attachments

None

Parent topic:

Noise Source

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga1a8c3f52b88b64b0530400730d514c69.html language=enus -->
## TOPIC 00190: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_TEMPERATURE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga1a8c3f52b88b64b0530400730d514c69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga1a8c3f52b88b64b0530400730d514c69.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the physical temperature of the ohmic loss elements specified in the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. This value is expressed in kelvin. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_TEMPERATURENumeric ValueData TypeAccessApplies To1179676float64Read/WriteN/AR

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_TEMPERATURE

Specifies the physical temperature of the ohmic loss elements specified in the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1gacd20b6149733ab79712501ded248bf50.html) attribute. This value is expressed in kelvin.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_TEMPERATURE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179676 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 297.

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga217319d11bd8b8c4d05e612d0d8b54a8.html language=enus -->
## TOPIC 00191: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga217319d11bd8b8c4d05e612d0d8b54a8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga217319d11bd8b8c4d05e612d0d8b54a8.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS attribute. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCYNumeric ValueData T

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY

Specifies the frequencies corresponding to the ohmic loss inherent to the noise source used in the Y-Factor method specified by the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1gacd20b6149733ab79712501ded248bf50.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179675 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga38c10ab38f6cdfe324155e120eaa31bb.html language=enus -->
## TOPIC 00192: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga38c10ab38f6cdfe324155e120eaa31bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga38c10ab38f6cdfe324155e120eaa31bb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps. SyntaxRFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLEDNumeric ValueData TypeAccessApplies To

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED

Specifies whether the noise figure (NF) measurement should account for ohmic losses inherent to the noise source used in the Y-Factor method common to the calibration and measurement steps.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179673 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED_FALSE | 0 (0x0) | Ohmic losses are ignored. |
| RFMXSPECAN_VAL_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED_TRUE | 1 (0x1) | Ohmic losses are accounted for in the NF measurement. |

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1gacd20b6149733ab79712501ded248bf50.html language=enus -->
## TOPIC 00193: RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1gacd20b6149733ab79712501ded248bf50.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1gacd20b6149733ab79712501ded248bf50.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of the ohmic losses inherent to the noise source used in the Y-Factor method. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED attribute to True. SyntaxRFMXSPECAN_ATT

### RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS

Specifies an array of the ohmic losses inherent to the noise source used in the Y-Factor method. This value is expressed in dB. This loss is accounted for by the NF measurement when you set the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_COMPENSATION_ENABLED](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga38c10ab38f6cdfe324155e120eaa31bb.html) attribute to **True**.

#### Syntax

RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1179674 | Adouble | Read/Write | N/A |

#### Remarks

You must specify the frequencies at which the losses were measured using the [RFMXSPECAN_ATTR_NF_Y_FACTOR_NOISE_SOURCE_LOSS_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes__nf__yfactor__noise__source__loss_1ga217319d11bd8b8c4d05e612d0d8b54a8.html) attribute.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is an empty array.

Parent topic:

Loss

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw.html language=enus -->
## TOPIC 00194: OBW

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsAveragingFFTRBW FilterResultsSweep TimeGroup membersNameDescriptionRFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLEDSpecifies whether to enable the traces to be stored and retrieved after performing the OBW. RFMXSPECAN_ATTR_OBW_AMPLITUDE_CORRECTION_TYPESpecifies whether the amplitude of the frequency bin

### OBW

#### Groups

- Averaging
- FFT
- RBW Filter
- Results
- Sweep Time

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLED | Specifies whether to enable the traces to be stored and retrieved after performing the OBW. |
| RFMXSPECAN_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE | Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. |
| RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE | Specifies the percentage of the total power that is contained in the OBW. |
| RFMXSPECAN_ATTR_OBW_MEASUREMENT_ENABLED | Specifies whether to enable OBW measurement. |
| RFMXSPECAN_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS | Specifies the maximum number of threads used for parallelism for the OBW measurement. |
| RFMXSPECAN_ATTR_OBW_POWER_UNITS | Specifies the units for the absolute power. |
| RFMXSPECAN_ATTR_OBW_SPAN | Specifies the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1ga04aebea136a6b65e7ae3fc41c2c1923a.html language=enus -->
## TOPIC 00195: RFMXSPECAN_ATTR_OBW_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1ga04aebea136a6b65e7ae3fc41c2c1923a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1ga04aebea136a6b65e7ae3fc41c2c1923a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable OBW measurement. SyntaxRFMXSPECAN_ATTR_OBW_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1073152int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String

### RFMXSPECAN_ATTR_OBW_MEASUREMENT_ENABLED

Specifies whether to enable OBW measurement.

#### Syntax

RFMXSPECAN_ATTR_OBW_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073152 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1ga4ac7eb6002296390dc9f578ed73bed76.html language=enus -->
## TOPIC 00196: RFMXSPECAN_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1ga4ac7eb6002296390dc9f578ed73bed76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1ga4ac7eb6002296390dc9f578ed73bed76.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table function to configure the external attenuation table. SyntaxRF

### RFMXSPECAN_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

Specifies whether the amplitude of the frequency bins, used in the measurement, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrcref_function_cfg_external_attenuation_table) function to configure the external attenuation table.

#### Syntax

RFMXSPECAN_ATTR_OBW_AMPLITUDE_CORRECTION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073178 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_RF_CENTER_FREQUENCY | 0 (0x0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| RFMXSPECAN_VAL_OBW_AMPLITUDE_CORRECTION_TYPE_SPECTRUM_FREQUENCY_BIN | 1 (0x1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1ga56063b738ab7093607e205678cec653a.html language=enus -->
## TOPIC 00197: RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1ga56063b738ab7093607e205678cec653a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1ga56063b738ab7093607e205678cec653a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the percentage of the total power that is contained in the OBW. SyntaxRFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGENumeric ValueData TypeAccessApplies To1073154float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instanc

### RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE

Specifies the percentage of the total power that is contained in the OBW.

#### Syntax

RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073154 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 99%.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1gaa10adf22f549e8b706a7f1b843f995f7.html language=enus -->
## TOPIC 00198: RFMXSPECAN_ATTR_OBW_POWER_UNITS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1gaa10adf22f549e8b706a7f1b843f995f7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1gaa10adf22f549e8b706a7f1b843f995f7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the units for the absolute power. SyntaxRFMXSPECAN_ATTR_OBW_POWER_UNITSNumeric ValueData TypeAccessApplies To1073176int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector String topic for

### RFMXSPECAN_ATTR_OBW_POWER_UNITS

Specifies the units for the absolute power.

#### Syntax

RFMXSPECAN_ATTR_OBW_POWER_UNITS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073176 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM | 0 (0x0) | The absolute powers are reported in dBm. |
| RFMXSPECAN_VAL_OBW_POWER_UNITS_DBM_PER_HZ | 1 (0x1) | The absolute powers are reported in dBm/Hz. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1gaa1be46a0d94a225877c9ef38f33b460a.html language=enus -->
## TOPIC 00199: RFMXSPECAN_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1gaa1be46a0d94a225877c9ef38f33b460a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1gaa1be46a0d94a225877c9ef38f33b460a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the OBW measurement. SyntaxRFMXSPECAN_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADSNumeric ValueData TypeAccessApplies To1073155int32Read/WriteN/ARemarks The number of threads can range from 1 to the number of physical cores. The number of threa

### RFMXSPECAN_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

Specifies the maximum number of threads used for parallelism for the OBW measurement.

#### Syntax

RFMXSPECAN_ATTR_OBW_NUMBER_OF_ANALYSIS_THREADS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073155 | int32 | Read/Write | N/A |

#### Remarks

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1gac36c7032a78e69b28342551de7c89fcc.html language=enus -->
## TOPIC 00200: RFMXSPECAN_ATTR_OBW_SPAN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1gac36c7032a78e69b28342551de7c89fcc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1gac36c7032a78e69b28342551de7c89fcc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_OBW_SPANNumeric ValueData TypeAccessApplies To1073156float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribut

### RFMXSPECAN_ATTR_OBW_SPAN

Specifies the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_OBW_SPAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073156 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 MHz.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw_1gacc5e8459cc72a51cf57990c578d7b2a4.html language=enus -->
## TOPIC 00201: RFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw_1gacc5e8459cc72a51cf57990c578d7b2a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw_1gacc5e8459cc72a51cf57990c578d7b2a4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the OBW. SyntaxRFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To1073170int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default

### RFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the OBW.

#### Syntax

RFMXSPECAN_ATTR_OBW_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073170 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__averaging.html language=enus -->
## TOPIC 00202: Averaging

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__averaging.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__averaging.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_OBW_AVERAGING_COUNTSpecifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED attribute to True. RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLEDSpecifies whether to enable averaging for the OBW measuremen

### Averaging

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT | Specifies the number of acquisitions used for averaging when you set the RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED attribute to True. |
| RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED | Specifies whether to enable averaging for the OBW measurement. |
| RFMXSPECAN_ATTR_OBW_AVERAGING_TYPE | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for OBW measurement. |

#### Attachments

None

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__averaging_1ga8d2b14d6c35fb678de024d1353cd283a.html language=enus -->
## TOPIC 00203: RFMXSPECAN_ATTR_OBW_AVERAGING_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__averaging_1ga8d2b14d6c35fb678de024d1353cd283a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__averaging_1ga8d2b14d6c35fb678de024d1353cd283a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for OBW measurement. SyntaxRFMXSPECAN_ATTR_OBW_AVERAGING_TYPENumeric ValueData TypeAccessApplies To1073161int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read t

### RFMXSPECAN_ATTR_OBW_AVERAGING_TYPE

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for OBW measurement.

#### Syntax

RFMXSPECAN_ATTR_OBW_AVERAGING_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073161 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_RMS | 0 (0x0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_LOG | 1 (0x1) | The power spectrum is averaged in a logarithmic scale. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_SCALAR | 2 (0x2) | The square root of the power spectrum is averaged. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MAXIMUM | 3 (0x3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| RFMXSPECAN_VAL_OBW_AVERAGING_TYPE_MINIMUM | 4 (0x4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__averaging_1ga941fe0ba2f1d089ad00a5cbae689c8a7.html language=enus -->
## TOPIC 00204: RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__averaging_1ga941fe0ba2f1d089ad00a5cbae689c8a7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__averaging_1ga941fe0ba2f1d089ad00a5cbae689c8a7.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the OBW measurement. SyntaxRFMXSPECAN_ATTR_OBW_AVERAGING_ENABLEDNumeric ValueData TypeAccessApplies To1073159int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED

Specifies whether to enable averaging for the OBW measurement.

#### Syntax

RFMXSPECAN_ATTR_OBW_AVERAGING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073159 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_FALSE | 0 (0x0) | The measurement is performed on a single acquisition. |
| RFMXSPECAN_VAL_OBW_AVERAGING_ENABLED_TRUE | 1 (0x1) | The OBW measurement uses the RFMXSPECAN_ATTR_OBW_AVERAGING_COUNT attribute as the number of acquisitions over which the OBW measurement is averaged. |

Parent topic:

Averaging

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__rbw__filter_1ga7fbe9f387ab45780529aea3dd7f5c1bb.html language=enus -->
## TOPIC 00205: RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__rbw__filter_1ga7fbe9f387ab45780529aea3dd7f5c1bb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__rbw__filter_1ga7fbe9f387ab45780529aea3dd7f5c1bb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the RFMXSPECAN_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH attribute to False. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTHNumeric ValueData TypeAccessApplies To10

### RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH

Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired signal, when you set the [RFMXSPECAN_ATTR_OBW_RBW_FILTER_AUTO_BANDWIDTH](group____root__ni_r_fmx_spec_an__attributes__obw__rbw__filter_1gaa3ece292fc57931d3f94b041aa0ce8a8.html) attribute to **False**. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073165 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 kHz.

Parent topic:

RBW Filter

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga0f51ca7539161ef680e57a3e3ef64c88.html language=enus -->
## TOPIC 00206: RFMXSPECAN_ATTR_OBW_RESULTS_FREQUENCY_RESOLUTION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga0f51ca7539161ef680e57a3e3ef64c88.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga0f51ca7539161ef680e57a3e3ef64c88.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency bin spacing of the spectrum acquired by the OBW measurement. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_OBW_RESULTS_FREQUENCY_RESOLUTIONNumeric ValueData TypeAccessApplies To1073175float64Read-OnlyN/ARemarks You do not need to use a selector string to read this result

### RFMXSPECAN_ATTR_OBW_RESULTS_FREQUENCY_RESOLUTION

Returns the frequency bin spacing of the spectrum acquired by the OBW measurement. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_OBW_RESULTS_FREQUENCY_RESOLUTION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073175 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga2cd3a85365f8cb21cf3169e975b19fe5.html language=enus -->
## TOPIC 00207: RFMXSPECAN_ATTR_OBW_RESULTS_AVERAGE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga2cd3a85365f8cb21cf3169e975b19fe5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga2cd3a85365f8cb21cf3169e975b19fe5.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total integrated power, in dBm, of the averaged spectrum acquired by the OBW measurement when you set the RFMXSPECAN_ATTR_OBW_POWER_UNITS attribute to dBm. The OBW Results Avg Pwr attribute returns the power spectral density, in dBm/Hz, when you set the OBW Power Units attribute to dBm/H

### RFMXSPECAN_ATTR_OBW_RESULTS_AVERAGE_POWER

Returns the total integrated power, in dBm, of the averaged spectrum acquired by the OBW measurement when you set the [RFMXSPECAN_ATTR_OBW_POWER_UNITS](group____root__ni_r_fmx_spec_an__attributes__obw_1gaa10adf22f549e8b706a7f1b843f995f7.html) attribute to **dBm**. The OBW Results Avg Pwr attribute returns the power spectral density, in dBm/Hz, when you set the OBW Power Units attribute to **dBm/Hz**.

#### Syntax

RFMXSPECAN_ATTR_OBW_RESULTS_AVERAGE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073172 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga39243d41b7a49d7e1a2ebd3e047337a0.html language=enus -->
## TOPIC 00208: RFMXSPECAN_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga39243d41b7a49d7e1a2ebd3e047337a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga39243d41b7a49d7e1a2ebd3e047337a0.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth that occupies the percentage of the total power of the signal that you specify in the RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE attribute. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTHNumeric ValueData TypeAccessApplies To1073171float64Read-

### RFMXSPECAN_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

Returns the bandwidth that occupies the percentage of the total power of the signal that you specify in the [RFMXSPECAN_ATTR_OBW_BANDWIDTH_PERCENTAGE](group____root__ni_r_fmx_spec_an__attributes__obw_1ga56063b738ab7093607e205678cec653a.html) attribute. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_OBW_RESULTS_OCCUPIED_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073171 | float64 | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga6ee7d20721c79587ab89427536094039.html language=enus -->
## TOPIC 00209: RFMXSPECAN_ATTR_OBW_RESULTS_STOP_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga6ee7d20721c79587ab89427536094039.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__results_1ga6ee7d20721c79587ab89427536094039.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the OBW. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_OBW_RESULTS_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To1073174float64Read-OnlyN/ARemarks The OBW is calculated using the following formula: OBW = stop frequency - start frequencyYou do not need to us

### RFMXSPECAN_ATTR_OBW_RESULTS_STOP_FREQUENCY

Returns the stop frequency of the OBW. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_OBW_RESULTS_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073174 | float64 | Read-Only | N/A |

#### Remarks

The OBW is calculated using the following formula: OBW = stop frequency - start frequency

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__results_1gacdcb836f2cccf0d8b1648f94b28bfbcb.html language=enus -->
## TOPIC 00210: RFMXSPECAN_ATTR_OBW_RESULTS_START_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__results_1gacdcb836f2cccf0d8b1648f94b28bfbcb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__results_1gacdcb836f2cccf0d8b1648f94b28bfbcb.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the OBW. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_OBW_RESULTS_START_FREQUENCYNumeric ValueData TypeAccessApplies To1073173float64Read-OnlyN/ARemarks The OBW is calculated using the following formula: OBW = stop frequency - start frequencyYou do not need to

### RFMXSPECAN_ATTR_OBW_RESULTS_START_FREQUENCY

Returns the start frequency of the OBW. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_OBW_RESULTS_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073173 | float64 | Read-Only | N/A |

#### Remarks

The OBW is calculated using the following formula: OBW = stop frequency - start frequency

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__obw__sweep__time_1ga565b7298235375eafe081f1c2e122bf3.html language=enus -->
## TOPIC 00211: RFMXSPECAN_ATTR_OBW_SWEEP_TIME_AUTO

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__obw__sweep__time_1ga565b7298235375eafe081f1c2e122bf3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__obw__sweep__time_1ga565b7298235375eafe081f1c2e122bf3.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. SyntaxRFMXSPECAN_ATTR_OBW_SWEEP_TIME_AUTONumeric ValueData TypeAccessApplies To1073167int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Select

### RFMXSPECAN_ATTR_OBW_SWEEP_TIME_AUTO

Specifies whether the measurement computes the sweep time.

#### Syntax

RFMXSPECAN_ATTR_OBW_SWEEP_TIME_AUTO

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1073167 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **True**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_FALSE | 0 (0x0) | The measurement uses the sweep time that you specify in the RFMXSPECAN_ATTR_OBW_SWEEP_TIME_INTERVAL attribute. |
| RFMXSPECAN_VAL_OBW_SWEEP_TIME_AUTO_TRUE | 1 (0x1) | The measurement calculates the sweep time based on the value of the RFMXSPECAN_ATTR_OBW_RBW_FILTER_BANDWIDTH attribute. |

Parent topic:

Sweep Time

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga302105fc2d1256451a770cd1b9fc3d12.html language=enus -->
## TOPIC 00212: RFMXSPECAN_ATTR_PAVT_FREQUENCY_TRACKING_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga302105fc2d1256451a770cd1b9fc3d12.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga302105fc2d1256451a770cd1b9fc3d12.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable frequency offset correction per segment for the measurement. While you set this attribute to True, ensure that the RFMXSPECAN_ATTR_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED attribute is set to True and the RFMXSPECAN_ATTR_PAVT_SEGMENT_TYPE attribute is set to Phase and Amp

### RFMXSPECAN_ATTR_PAVT_FREQUENCY_TRACKING_ENABLED

Specifies whether to enable frequency offset correction per segment for the measurement. While you set this attribute to **True**, ensure that the [RFMXSPECAN_ATTR_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED](group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3bc4dc2b749ef011ec46bcf7b2038e78.html) attribute is set to **True** and the [RFMXSPECAN_ATTR_PAVT_SEGMENT_TYPE](group____root__ni_r_fmx_spec_an__attributes__pavt_1gae55d062eef584e1aa0551e5003d2d50f.html) attribute is set to **Phase and Amplitude**.

#### Syntax

RFMXSPECAN_ATTR_PAVT_FREQUENCY_TRACKING_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077270 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_PAVT_FREQUENCY_TRACKING_ENABLED_FALSE | 0 (0x0) | Disables the drift correction for the measurement. |
| RFMXSPECAN_VAL_PAVT_FREQUENCY_TRACKING_ENABLED_TRUE | 1 (0x1) | Enables the drift correction. The measurement corrects and reports the frequency offset per segment. |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3a664232830f9dd65a6072f9cbcda98c.html language=enus -->
## TOPIC 00213: RFMXSPECAN_ATTR_PAVT_NUMBER_OF_SEGMENTS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3a664232830f9dd65a6072f9cbcda98c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3a664232830f9dd65a6072f9cbcda98c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of segments to be measured. SyntaxRFMXSPECAN_ATTR_PAVT_NUMBER_OF_SEGMENTSNumeric ValueData TypeAccessApplies To1077251int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selector Str

### RFMXSPECAN_ATTR_PAVT_NUMBER_OF_SEGMENTS

Specifies the number of segments to be measured.

#### Syntax

RFMXSPECAN_ATTR_PAVT_NUMBER_OF_SEGMENTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077251 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3b8d6d84edc09e2bcd243e131500d210.html language=enus -->
## TOPIC 00214: RFMXSPECAN_ATTR_PAVT_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3b8d6d84edc09e2bcd243e131500d210.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3b8d6d84edc09e2bcd243e131500d210.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Phase Amplitude Versus Time (PAVT) measurement. SyntaxRFMXSPECAN_ATTR_PAVT_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1077248int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal ins

### RFMXSPECAN_ATTR_PAVT_MEASUREMENT_ENABLED

Specifies whether to enable the Phase Amplitude Versus Time (PAVT) measurement.

#### Syntax

RFMXSPECAN_ATTR_PAVT_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077248 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3bc4dc2b749ef011ec46bcf7b2038e78.html language=enus -->
## TOPIC 00215: RFMXSPECAN_ATTR_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3bc4dc2b749ef011ec46bcf7b2038e78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga3bc4dc2b749ef011ec46bcf7b2038e78.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable frequency offset correction for the measurement. SyntaxRFMXSPECAN_ATTR_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLEDNumeric ValueData TypeAccessApplies To1077260int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defau

### RFMXSPECAN_ATTR_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED

Specifies whether to enable frequency offset correction for the measurement.

#### Syntax

RFMXSPECAN_ATTR_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077260 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED_FALSE | 0 (0x0) | Disables the frequency offset correction. |
| RFMXSPECAN_VAL_PAVT_FREQUENCY_OFFSET_CORRECTION_ENABLED_TRUE | 1 (0x1) | Enables the frequency offset correction. The measurement computes and corrects any frequency offset between the reference and the acquired waveforms. |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga561a5d555441a29b254ab1e6e6597c0c.html language=enus -->
## TOPIC 00216: RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LENGTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga561a5d555441a29b254ab1e6e6597c0c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga561a5d555441a29b254ab1e6e6597c0c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration within the segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This attribute is valid only when you set the RFMXSPECAN_ATTR_PAVT_MEASUREMENT_INTERVAL_MODE attribute to Uniform. SyntaxRFMXSPECAN_ATT

### RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LENGTH

Specifies the duration within the segment over which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This attribute is valid only when you set the [RFMXSPECAN_ATTR_PAVT_MEASUREMENT_INTERVAL_MODE](group____root__ni_r_fmx_spec_an__attributes__pavt_1ga04af51889e561acce2a189e374579061.html) attribute to **Uniform**.

#### Syntax

RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LENGTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077254 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga58c24ed9b1005c842217b80234ef9303.html language=enus -->
## TOPIC 00217: RFMXSPECAN_ATTR_PAVT_SEGMENT_MEASUREMENT_OFFSET

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga58c24ed9b1005c842217b80234ef9303.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga58c24ed9b1005c842217b80234ef9303.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This attribute is valid only when you set the RFMXSPECAN_ATTR_PAVT_MEASUREMENT_INTERVAL_MODE attribute to Variable. Syntax

### RFMXSPECAN_ATTR_PAVT_SEGMENT_MEASUREMENT_OFFSET

Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This attribute is valid only when you set the [RFMXSPECAN_ATTR_PAVT_MEASUREMENT_INTERVAL_MODE](group____root__ni_r_fmx_spec_an__attributes__pavt_1ga04af51889e561acce2a189e374579061.html) attribute to **Variable**.

#### Syntax

RFMXSPECAN_ATTR_PAVT_SEGMENT_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077265 | float64 | Read/Write | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6703aaca2e70caac31a70a7c05225fa4.html language=enus -->
## TOPIC 00218: RFMXSPECAN_ATTR_PAVT_MEASUREMENT_OFFSET

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6703aaca2e70caac31a70a7c05225fa4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6703aaca2e70caac31a70a7c05225fa4.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This attribute is valid only when you set the RFMXSPECAN_ATTR_PAVT_MEASUREMENT_INTERVAL_MODE attribute to Uniform. SyntaxR

### RFMXSPECAN_ATTR_PAVT_MEASUREMENT_OFFSET

Specifies the time offset from the start of the segment for which the phase and amplitude, amplitude, or frequency error values are computed. This value is expressed in seconds. This attribute is valid only when you set the [RFMXSPECAN_ATTR_PAVT_MEASUREMENT_INTERVAL_MODE](group____root__ni_r_fmx_spec_an__attributes__pavt_1ga04af51889e561acce2a189e374579061.html) attribute to **Uniform**.

#### Syntax

RFMXSPECAN_ATTR_PAVT_MEASUREMENT_OFFSET

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077253 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 0.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6cf6130e6f6d7c6744f6a36a1f4706cc.html language=enus -->
## TOPIC 00219: RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LOCATION_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6cf6130e6f6d7c6744f6a36a1f4706cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6cf6130e6f6d7c6744f6a36a1f4706cc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the location at which the segment is measured is indicated by time or trigger. SyntaxRFMXSPECAN_ATTR_PAVT_MEASUREMENT_LOCATION_TYPENumeric ValueData TypeAccessApplies To1077250int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for

### RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LOCATION_TYPE

Specifies whether the location at which the segment is measured is indicated by time or trigger.

#### Syntax

RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LOCATION_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077250 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Time**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TIME | 0 (0x0) | The measurement is performed over a single record across multiple segments separated in time. The measurement locations of the segments are specified by the RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME attribute. The number of segments is equal to the number of segment start times. |
| RFMXSPECAN_VAL_PAVT_MEASUREMENT_LOCATION_TYPE_TRIGGER | 1 (0x1) | The measurement is performed across segments obtained in multiple records, where each record is obtained when a trigger is received. The number of segments is equal to the number of triggers (records). |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1ga9c03f6b984bfb6a9d90b7786a1d60a0b.html language=enus -->
## TOPIC 00220: RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1ga9c03f6b984bfb6a9d90b7786a1d60a0b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1ga9c03f6b984bfb6a9d90b7786a1d60a0b.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start time of measurement of the segments. This value is expressed in seconds. You can use this attribute only when you set the RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LOCATION_TYPE attribute to Time. SyntaxRFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIMENumeric ValueData TypeAccessApplies To1077252fl

### RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME

Specifies the start time of measurement of the segments. This value is expressed in seconds. You can use this attribute only when you set the [RFMXSPECAN_ATTR_PAVT_MEASUREMENT_LOCATION_TYPE](group____root__ni_r_fmx_spec_an__attributes__pavt_1ga6cf6130e6f6d7c6744f6a36a1f4706cc.html) attribute to **Time**.

#### Syntax

RFMXSPECAN_ATTR_PAVT_SEGMENT_START_TIME

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077252 | float64 | Read/Write | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 0.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1gacfb02c85fc87685b13a6df98d54d1079.html language=enus -->
## TOPIC 00221: RFMXSPECAN_ATTR_PAVT_MEASUREMENT_BANDWIDTH

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1gacfb02c85fc87685b13a6df98d54d1079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1gacfb02c85fc87685b13a6df98d54d1079.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth over which the signal is measured. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_PAVT_MEASUREMENT_BANDWIDTHNumeric ValueData TypeAccessApplies To1077261float64Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the defa

### RFMXSPECAN_ATTR_PAVT_MEASUREMENT_BANDWIDTH

Specifies the bandwidth over which the signal is measured. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_PAVT_MEASUREMENT_BANDWIDTH

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077261 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10 MHz.

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt_1gae55d062eef584e1aa0551e5003d2d50f.html language=enus -->
## TOPIC 00222: RFMXSPECAN_ATTR_PAVT_SEGMENT_TYPE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt_1gae55d062eef584e1aa0551e5003d2d50f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt_1gae55d062eef584e1aa0551e5003d2d50f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of segment. SyntaxRFMXSPECAN_ATTR_PAVT_SEGMENT_TYPENumeric ValueData TypeAccessApplies To1077264int32Read/WriteSegmentRemarks Use "segment<n>" as the Selector String to configure or read this attribute.The default value is Phase and Amplitude.NameValueDescriptionRFMXSPECAN_VAL_PAV

### RFMXSPECAN_ATTR_PAVT_SEGMENT_TYPE

Specifies the type of segment.

#### Syntax

RFMXSPECAN_ATTR_PAVT_SEGMENT_TYPE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077264 | int32 | Read/Write | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is **Phase and Amplitude**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_PHASE_AND_AMPLITUDE | 0 (0x0) | Phase and amplitude is measured in this segment. |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_AMPLITUDE | 1 (0x1) | Amplitude is measured in this segment. |
| RFMXSPECAN_VAL_PAVT_SEGMENT_TYPE_FREQUENCY_ERROR_MEASUREMENT | 2 (0x2) | Frequency error is measured in this segment. |

Parent topic:

PAVT

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt__results_1ga10c8f1e2fc48b3bcff16bda6411b7bfd.html language=enus -->
## TOPIC 00223: RFMXSPECAN_ATTR_PAVT_RESULTS_FREQUENCY_ERROR_MEAN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt__results_1ga10c8f1e2fc48b3bcff16bda6411b7bfd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt__results_1ga10c8f1e2fc48b3bcff16bda6411b7bfd.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean frequency error of the segment. This value is expressed in Hz. SyntaxRFMXSPECAN_ATTR_PAVT_RESULTS_FREQUENCY_ERROR_MEANNumeric ValueData TypeAccessApplies To1077268float64Read-OnlySegmentRemarks Use "segment<n>" as the Selector String to read this result.

### RFMXSPECAN_ATTR_PAVT_RESULTS_FREQUENCY_ERROR_MEAN

Returns the mean frequency error of the segment. This value is expressed in Hz.

#### Syntax

RFMXSPECAN_ATTR_PAVT_RESULTS_FREQUENCY_ERROR_MEAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077268 | float64 | Read-Only | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__pavt__results_1ga6627655f1e78b32526e200195cc101ec.html language=enus -->
## TOPIC 00224: RFMXSPECAN_ATTR_PAVT_RESULTS_MEAN_ABSOLUTE_AMPLITUDE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__pavt__results_1ga6627655f1e78b32526e200195cc101ec.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__pavt__results_1ga6627655f1e78b32526e200195cc101ec.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean absolute amplitude of the segment. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_PAVT_RESULTS_MEAN_ABSOLUTE_AMPLITUDENumeric ValueData TypeAccessApplies To1077262float64Read-OnlySegmentRemarks Use "segment<n>" as the Selector String to read this result.

### RFMXSPECAN_ATTR_PAVT_RESULTS_MEAN_ABSOLUTE_AMPLITUDE

Returns the mean absolute amplitude of the segment. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_PAVT_RESULTS_MEAN_ABSOLUTE_AMPLITUDE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1077262 | float64 | Read-Only | Segment |

#### Remarks

Use "segment<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to read this result.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga39e1d66b597432c61c5c8cf8c14e547c.html language=enus -->
## TOPIC 00225: RFMXSPECAN_ATTR_PHASENOISE_ALL_TRACES_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga39e1d66b597432c61c5c8cf8c14e547c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga39e1d66b597432c61c5c8cf8c14e547c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the Phase Noise measurement. SyntaxRFMXSPECAN_ATTR_PHASENOISE_ALL_TRACES_ENABLEDNumeric ValueData TypeAccessApplies To1245203int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this

### RFMXSPECAN_ATTR_PHASENOISE_ALL_TRACES_ENABLED

Specifies whether to enable the traces to be stored and retrieved after performing the Phase Noise measurement.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_ALL_TRACES_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245203 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga8b65cbdd46fa7c4b167b597a5b6b552a.html language=enus -->
## TOPIC 00226: RFMXSPECAN_ATTR_PHASENOISE_RBW_PERCENTAGE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga8b65cbdd46fa7c4b167b597a5b6b552a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga8b65cbdd46fa7c4b167b597a5b6b552a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RBW as a percentage of the start frequency of each subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Auto. SyntaxRFMXSPECAN_ATTR_PHASENOISE_RBW_PERCENTAGENumeric ValueData TypeAccessApplies To1245189float64Read/WriteN/ARemarks You do not need to use a s

### RFMXSPECAN_ATTR_PHASENOISE_RBW_PERCENTAGE

Specifies the RBW as a percentage of the start frequency of each subrange when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Auto**.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_RBW_PERCENTAGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245189 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 10.

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga9425202d3296339fbc7c2b344f6c231f.html language=enus -->
## TOPIC 00227: RFMXSPECAN_ATTR_PHASENOISE_AVERAGING_MULTIPLIER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga9425202d3296339fbc7c2b344f6c231f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga9425202d3296339fbc7c2b344f6c231f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which you increase the averaging count for each range. This setting applies to both Auto and Manual range definitions. SyntaxRFMXSPECAN_ATTR_PHASENOISE_AVERAGING_MULTIPLIERNumeric ValueData TypeAccessApplies To1245190int32Read/WriteN/ARemarks You do not need to use a selector

### RFMXSPECAN_ATTR_PHASENOISE_AVERAGING_MULTIPLIER

Specifies the factor by which you increase the averaging count for each range. This setting applies to both **Auto** and **Manual** range definitions.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_AVERAGING_MULTIPLIER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245190 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise_1gad9ada220ae2dfd73b1fa5cbf4752f49d.html language=enus -->
## TOPIC 00228: RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise_1gad9ada220ae2dfd73b1fa5cbf4752f49d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise_1gad9ada220ae2dfd73b1fa5cbf4752f49d.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start frequency of the offset frequency range when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Auto. SyntaxRFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCYNumeric ValueData TypeAccessApplies To1245187float64Read/WriteN/ARemarks You do not need to use a selector strin

### RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY

Specifies the start frequency of the offset frequency range when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Auto**.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_START_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245187 | float64 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1000.

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise_1gada8d1253ba8aa3b4d2ed7c86615d0e04.html language=enus -->
## TOPIC 00229: RFMXSPECAN_ATTR_PHASENOISE_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise_1gada8d1253ba8aa3b4d2ed7c86615d0e04.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise_1gada8d1253ba8aa3b4d2ed7c86615d0e04.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the phase noise measurement. SyntaxRFMXSPECAN_ATTR_PHASENOISE_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1245184int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to t

### RFMXSPECAN_ATTR_PHASENOISE_MEASUREMENT_ENABLED

Specifies whether to enable the phase noise measurement.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245184 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation.html language=enus -->
## TOPIC 00230: Cancellation

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_ENABLEDSpecifies whether to enable or disable the phase noise cancellation. RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCYSpecifies an array of frequencies where the reference phase noise has been measured. RFMXSPECAN_A

### Cancellation

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_ENABLED | Specifies whether to enable or disable the phase noise cancellation. |
| RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY | Specifies an array of frequencies where the reference phase noise has been measured. |
| RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE | Specifies an array of reference phase noise at the frequencies specified by the RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY attribute . |
| RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_THRESHOLD | Specifies the minimum difference between the reference and pre-cancellation traces that must exist before cancellation is performed. |

#### Attachments

None

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation_1ga053e2cbf54f286eeaa174617cacc301a.html language=enus -->
## TOPIC 00231: RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation_1ga053e2cbf54f286eeaa174617cacc301a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation_1ga053e2cbf54f286eeaa174617cacc301a.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of reference phase noise at the frequencies specified by the RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY attribute . SyntaxRFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISENumeric ValueData TypeAccessApplies To1245218AfloatRead/WriteN/ARemarks You do not need to

### RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE

Specifies an array of reference phase noise at the frequencies specified by the [RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes__phasenoise__cancellation_1gab7da7f8149327e96a7a1c90e8997792e.html) attribute .

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_CANCELLATION_REFERENCE_PHASE_NOISE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245218 | Afloat | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Cancellation

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__integrated__noise_1gaa9a121a80553919bb3783e10bd0ab6f2.html language=enus -->
## TOPIC 00232: RFMXSPECAN_ATTR_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__integrated__noise_1gaa9a121a80553919bb3783e10bd0ab6f2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__integrated__noise_1gaa9a121a80553919bb3783e10bd0ab6f2.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency range for integrated noise measurements. SyntaxRFMXSPECAN_ATTR_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITIONNumeric ValueData TypeAccessApplies To1245200int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signa

### RFMXSPECAN_ATTR_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION

Specifies the frequency range for integrated noise measurements.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245200 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **Measurement**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION_NONE | 0 (0x0) | Integrated noise measurement is not computed. |
| RFMXSPECAN_VAL_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION_MEASUREMENT | 1 (0x1) | The complete log plot frequency range, considered as a single range, is used for computing integrated measurements. |
| RFMXSPECAN_VAL_PHASENOISE_INTEGRATED_NOISE_RANGE_DEFINITION_CUSTOM | 2 (0x2) | The measurement range(s) specified by RFMXSPECAN_ATTR_PHASENOISE_INTEGRATED_NOISE_START_FREQUENCY attribute and the RFMXSPECAN_ATTR_PHASENOISE_INTEGRATED_NOISE_STOP_FREQUENCY attribute is used for computing integrated measurements. |

Parent topic:

Integrated Noise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__range.html language=enus -->
## TOPIC 00233: Range

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__range.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__range.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_PHASENOISE_NUMBER_OF_RANGESSpecifies the number of manual ranges. RFMXSPECAN_ATTR_PHASENOISE_RANGE_AVERAGING_COUNTSpecifies the averaging count for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to M

### Range

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_PHASENOISE_NUMBER_OF_RANGES | Specifies the number of manual ranges. |
| RFMXSPECAN_ATTR_PHASENOISE_RANGE_AVERAGING_COUNT | Specifies the averaging count for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. |
| RFMXSPECAN_ATTR_PHASENOISE_RANGE_RBW_PERCENTAGE | Specifies the RBW as a percentage of the RFMXSPECAN_ATTR_PHASENOISE_RANGE_START_FREQUENCY attribute of the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. |
| RFMXSPECAN_ATTR_PHASENOISE_RANGE_START_FREQUENCY | Specifies the start frequency for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. |
| RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY | Specifies the stop frequency for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. |

#### Attachments

None

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga16c688a3f428c6c499eb680d67989601.html language=enus -->
## TOPIC 00234: RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga16c688a3f428c6c499eb680d67989601.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga16c688a3f428c6c499eb680d67989601.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop frequency for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. SyntaxRFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCYNumeric ValueData TypeAccessApplies To1245194float64Read/WriteRangeRemarks Use "range<n>" as the Selector Str

### RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY

Specifies the stop frequency for the specified subrange when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Manual**.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_RANGE_STOP_FREQUENCY

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245194 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 1E+06.

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga457393e79b7dd022622be43431a6047e.html language=enus -->
## TOPIC 00235: RFMXSPECAN_ATTR_PHASENOISE_RANGE_RBW_PERCENTAGE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga457393e79b7dd022622be43431a6047e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga457393e79b7dd022622be43431a6047e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RBW as a percentage of the RFMXSPECAN_ATTR_PHASENOISE_RANGE_START_FREQUENCY attribute of the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. SyntaxRFMXSPECAN_ATTR_PHASENOISE_RANGE_RBW_PERCENTAGENumeric ValueData TypeAccessApplies To1

### RFMXSPECAN_ATTR_PHASENOISE_RANGE_RBW_PERCENTAGE

Specifies the RBW as a percentage of the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_START_FREQUENCY](group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga967947f7da865fe1fe10ababeb897b12.html) attribute of the specified subrange when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Manual**.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_RANGE_RBW_PERCENTAGE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245195 | float64 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 10.

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga6bb49f490bcbec77df191418a8ac58cc.html language=enus -->
## TOPIC 00236: RFMXSPECAN_ATTR_PHASENOISE_RANGE_AVERAGING_COUNT

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga6bb49f490bcbec77df191418a8ac58cc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__range_1ga6bb49f490bcbec77df191418a8ac58cc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging count for the specified subrange when you set the RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION attribute to Manual. SyntaxRFMXSPECAN_ATTR_PHASENOISE_RANGE_AVERAGING_COUNTNumeric ValueData TypeAccessApplies To1245196int32Read/WriteRangeRemarks Use "range<n>" as the Selector Str

### RFMXSPECAN_ATTR_PHASENOISE_RANGE_AVERAGING_COUNT

Specifies the averaging count for the specified subrange when you set the [RFMXSPECAN_ATTR_PHASENOISE_RANGE_DEFINITION](group____root__ni_r_fmx_spec_an__attributes__phasenoise_1ga2760aff00c7960526c3bcfc3a8b607b4.html) attribute to **Manual**.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_RANGE_AVERAGING_COUNT

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245196 | int32 | Read/Write | Range |

#### Remarks

Use "range<n>" as the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) to configure or read this attribute.

The default value is 10.

Parent topic:

Range

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise.html language=enus -->
## TOPIC 00237: Integrated Noise

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_JITTERReturns the jitter in seconds. RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_FMReturns the residual FM in Hz. RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREEReturn

### Integrated Noise

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_JITTER | Returns the jitter in seconds. |
| RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_FM | Returns the residual FM in Hz. |
| RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREE | Returns the residual PM in degrees. |
| RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_RADIAN | Returns the residual PM in radians. |
| RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_PHASE_NOISE | Returns the integrated phase noise. |

#### Attachments

None

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise_1ga1989fca63d5c23e04b2a6db3161dd8bc.html language=enus -->
## TOPIC 00238: RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREE

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise_1ga1989fca63d5c23e04b2a6db3161dd8bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise_1ga1989fca63d5c23e04b2a6db3161dd8bc.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the residual PM in degrees. SyntaxRFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREENumeric ValueData TypeAccessApplies To1245210AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Sel

### RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREE

Returns the residual PM in degrees.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_DEGREE

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245210 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Integrated Noise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise_1gac0f24ea9391ef4246652d1c939c46c3c.html language=enus -->
## TOPIC 00239: RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_RADIAN

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise_1gac0f24ea9391ef4246652d1c939c46c3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__results__integrated__noise_1gac0f24ea9391ef4246652d1c939c46c3c.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the residual PM in radians. SyntaxRFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_RADIANNumeric ValueData TypeAccessApplies To1245209AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read this attribute for the default signal instance. Refer to the Sel

### RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_RADIAN

Returns the residual PM in radians.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_RESULTS_INTEGRATED_NOISE_RESIDUAL_PM_IN_RADIAN

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245209 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Integrated Noise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__spot__noise.html language=enus -->
## TOPIC 00240: Spot Noise

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__spot__noise.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__spot__noise.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_PHASENOISE_SPOT_NOISE_FREQUENCY_LISTSpecifies an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. AttachmentsNone

### Spot Noise

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_PHASENOISE_SPOT_NOISE_FREQUENCY_LIST | Specifies an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. |

#### Attachments

None

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__spot__noise_1gaf83c9ba0ed5abdcdb6e86207edc1edce.html language=enus -->
## TOPIC 00241: RFMXSPECAN_ATTR_PHASENOISE_SPOT_NOISE_FREQUENCY_LIST

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__spot__noise_1gaf83c9ba0ed5abdcdb6e86207edc1edce.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__spot__noise_1gaf83c9ba0ed5abdcdb6e86207edc1edce.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace. SyntaxRFMXSPECAN_ATTR_PHASENOISE_SPOT_NOISE_FREQUENCY_LISTNumeric ValueData TypeAccessApplies To1245199AdoubleRead/WriteN/ARemarks You do not need to use a selector string to configure or

### RFMXSPECAN_ATTR_PHASENOISE_SPOT_NOISE_FREQUENCY_LIST

Specifies an array of offset frequencies at which the phase noise is measured using the smoothed log plot trace.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_SPOT_NOISE_FREQUENCY_LIST

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245199 | Adouble | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

Parent topic:

Spot Noise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__spur__removal.html language=enus -->
## TOPIC 00242: Spur Removal

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__spur__removal.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__spur__removal.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_ENABLEDSpecifies whether to remove spurs from the log plot trace. RFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_PEAK_EXCURSIONSpecifies the peak excursion to be used when spur detection is performed. AttachmentsNone

### Spur Removal

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_ENABLED | Specifies whether to remove spurs from the log plot trace. |
| RFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_PEAK_EXCURSION | Specifies the peak excursion to be used when spur detection is performed. |

#### Attachments

None

Parent topic:

PhaseNoise

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__phasenoise__spur__removal_1ga15fb5c7bee77183fff3fbde5826bc00f.html language=enus -->
## TOPIC 00243: RFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__phasenoise__spur__removal_1ga15fb5c7bee77183fff3fbde5826bc00f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__phasenoise__spur__removal_1ga15fb5c7bee77183fff3fbde5826bc00f.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove spurs from the log plot trace. SyntaxRFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_ENABLEDNumeric ValueData TypeAccessApplies To1245213int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer t

### RFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_ENABLED

Specifies whether to remove spurs from the log plot trace.

#### Syntax

RFMXSPECAN_ATTR_PHASENOISE_SPUR_REMOVAL_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1245213 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is **False**.

| Name | Value | Description |
| --- | --- | --- |
| RFMXSPECAN_VAL_PHASENOISE_SPUR_REMOVAL_ENABLED_FALSE | 0 (0x0) | Disables spur removal on the log plot trace. |
| RFMXSPECAN_VAL_PHASENOISE_SPUR_REMOVAL_ENABLED_TRUE | 1 (0x1) | Enables spur removal on the log plot trace. |

Parent topic:

Spur Removal

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist.html language=enus -->
## TOPIC 00244: PowerList

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsResultsSegmentGroup membersNameDescriptionRFMXSPECAN_ATTR_POWERLIST_MEASUREMENT_ENABLEDSpecifies whether to enable the PowerList measurement. RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTSSpecifies the number of segments to be measured. AttachmentsNone

### PowerList

#### Groups

- Results
- Segment

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_POWERLIST_MEASUREMENT_ENABLED | Specifies whether to enable the PowerList measurement. |
| RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS | Specifies the number of segments to be measured. |

#### Attachments

None

Parent topic:

Attributes

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist_1ga3f7e619877b75d88617f62d7778e4fea.html language=enus -->
## TOPIC 00245: RFMXSPECAN_ATTR_POWERLIST_MEASUREMENT_ENABLED

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist_1ga3f7e619877b75d88617f62d7778e4fea.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist_1ga3f7e619877b75d88617f62d7778e4fea.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the PowerList measurement. SyntaxRFMXSPECAN_ATTR_POWERLIST_MEASUREMENT_ENABLEDNumeric ValueData TypeAccessApplies To1376256int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the

### RFMXSPECAN_ATTR_POWERLIST_MEASUREMENT_ENABLED

Specifies whether to enable the PowerList measurement.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_MEASUREMENT_ENABLED

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376256 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is FALSE.

Parent topic:

PowerList

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html language=enus -->
## TOPIC 00246: RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist_1gaa05ec5a76376c68c36c90273630aa120.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of segments to be measured. SyntaxRFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTSNumeric ValueData TypeAccessApplies To1376258int32Read/WriteN/ARemarks You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the Selecto

### RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS

Specifies the number of segments to be measured.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_NUMBER_OF_SEGMENTS

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376258 | int32 | Read/Write | N/A |

#### Remarks

You do not need to use a selector string to configure or read this attribute for the default signal instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals.

The default value is 1.

Parent topic:

PowerList

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__results.html language=enus -->
## TOPIC 00247: Results

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__results.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__results.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionRFMXSPECAN_ATTR_POWERLIST_RESULTS_MAXIMUM_POWERReturns an array of maximum power of the signal, each corresponding to a segment. This value is expressed in dBm. RFMXSPECAN_ATTR_POWERLIST_RESULTS_MEAN_ABSOLUTE_POWERReturns an array of mean absolute power of the s

### Results

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| RFMXSPECAN_ATTR_POWERLIST_RESULTS_MAXIMUM_POWER | Returns an array of maximum power of the signal, each corresponding to a segment. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_POWERLIST_RESULTS_MEAN_ABSOLUTE_POWER | Returns an array of mean absolute power of the signal, each corresponding to a segment. This value is expressed in dBm. |
| RFMXSPECAN_ATTR_POWERLIST_RESULTS_MINIMUM_POWER | Returns an array of minimum power of the signal, each corresponding to a segment. This value is expressed in dBm. |

#### Attachments

None

Parent topic:

PowerList

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaec50c289376459c417cf0620b6bcafda.html language=enus -->
## TOPIC 00248: RFMXSPECAN_ATTR_POWERLIST_RESULTS_MEAN_ABSOLUTE_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaec50c289376459c417cf0620b6bcafda.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaec50c289376459c417cf0620b6bcafda.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of mean absolute power of the signal, each corresponding to a segment. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_POWERLIST_RESULTS_MEAN_ABSOLUTE_POWERNumeric ValueData TypeAccessApplies To1376268AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read

### RFMXSPECAN_ATTR_POWERLIST_RESULTS_MEAN_ABSOLUTE_POWER

Returns an array of mean absolute power of the signal, each corresponding to a segment. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_RESULTS_MEAN_ABSOLUTE_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376268 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaeda7716de2a94187254b85864403211e.html language=enus -->
## TOPIC 00249: RFMXSPECAN_ATTR_POWERLIST_RESULTS_MINIMUM_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaeda7716de2a94187254b85864403211e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaeda7716de2a94187254b85864403211e.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of minimum power of the signal, each corresponding to a segment. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_POWERLIST_RESULTS_MINIMUM_POWERNumeric ValueData TypeAccessApplies To1376270AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read this result

### RFMXSPECAN_ATTR_POWERLIST_RESULTS_MINIMUM_POWER

Returns an array of minimum power of the signal, each corresponding to a segment. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_RESULTS_MINIMUM_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376270 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results

<!--NI_TOPIC bundle=rfmxspecan-c-api-ref path=group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaee6f84b0f8550fd4cdd3d7c1e502a547.html language=enus -->
## TOPIC 00250: RFMXSPECAN_ATTR_POWERLIST_RESULTS_MAXIMUM_POWER

- bundle_id: `rfmxspecan-c-api-ref`
- source_path: `group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaee6f84b0f8550fd4cdd3d7c1e502a547.html`
- source_url: https://docs-be.ni.com/bundle/rfmxspecan-c-api-ref/raw/resource/enus/group____root__ni_r_fmx_spec_an__attributes__powerlist__results_1gaee6f84b0f8550fd4cdd3d7c1e502a547.html
- document_id: `rfmxspecan-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of maximum power of the signal, each corresponding to a segment. This value is expressed in dBm. SyntaxRFMXSPECAN_ATTR_POWERLIST_RESULTS_MAXIMUM_POWERNumeric ValueData TypeAccessApplies To1376269AdoubleRead-OnlyN/ARemarks You do not need to use a selector string to read this result

### RFMXSPECAN_ATTR_POWERLIST_RESULTS_MAXIMUM_POWER

Returns an array of maximum power of the signal, each corresponding to a segment. This value is expressed in dBm.

#### Syntax

RFMXSPECAN_ATTR_POWERLIST_RESULTS_MAXIMUM_POWER

| Numeric Value | Data Type | Access | Applies To |
| --- | --- | --- | --- |
| 1376269 | Adouble | Read-Only | N/A |

#### Remarks

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector String](https://www.ni.com/docs/en-US/bundle/rfmx/page/selector-string-cvi.html) topic for information about the string syntax for named signals and results.

Parent topic:

Results
