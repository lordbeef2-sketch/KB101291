# NI DOCUMENT BUNDLE: rfmx-nr-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-nr-prop start=1 end=70 -->
<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900014.html language=enus -->
## TOPIC 00001: Component Carrier at Center Frequency Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900014.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier at Center Frequency Property

**Short Name:**CC at Center Freq

Property of [RFmxNR](crfmxnr.html)

Specifies the index of the component carrier having its center at the user-configured center frequency. The measurement uses this property along with [CC Spacing Type](attr900013.html) property to calculate the value of the [CC Freq](attr900017.html). This property is ignored if you set the CC Spacing Type property to **User**.

Use "subblock<*n*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

Valid values are -1, 0, 1 ... *n* - 1, inclusive, where *n* is the number of component carriers in the subblock.

The default value is -1. If the value is -1, the component carrier frequency values are calculated such that the center of the subcarrier(with maximum subcarrier spacing for a frequency range), which is closest to the center of the aggregated channel bandwidth, lies at the center frequency.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900017.html language=enus -->
## TOPIC 00002: Component Carrier:Frequency (Hz) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900017.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Frequency (Hz) Property

**Short Name:**CC Freq (Hz)

Property of [RFmxNR](crfmxnr.html)

Specifies the offset of the component carrier from the subblock center frequency that you configure in the [Center Frequency](attr900001.html) property. This value is expressed in Hz.

This property is applicable only if you set the [CC Spacing Type](attr900013.html) property to **User**.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90001a.html language=enus -->
## TOPIC 00003: Component Carrier:Bandwidth Part:Cyclic Prefix Mode Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90001a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90001a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:Cyclic Prefix Mode Property

**Short Name:**BWP Cyclic Prefix Mode

Property of [RFmxNR](crfmxnr.html)

Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Normal**.

| Normal (0) | The number of symbols in the slot is 14. |
| --- | --- |
| Extended (1) | The number of symbols in the slot is 12. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900022.html language=enus -->
## TOPIC 00004: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:Sequence Hopping Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900022.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:Sequence Hopping Enabled Property

**Short Name:**PUSCH DMRS Sequence Hopping Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether the sequence hopping is enabled. This property is valid only when you set the [PUSCH Transform Precoding Enabled](attr90001e.html) property to **True**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **False**.

| False (0) | The measurement uses zero as the base sequence number for all the slots. |
| --- | --- |
| True (1) | The measurement calculates the base sequence number for each slot according to 3GPP specification. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900026.html language=enus -->
## TOPIC 00005: Component Carrier:Bandwidth Part:User:PUSCH:Modulation Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900026.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:Modulation Type Property

**Short Name:**PUSCH Mod Type

Property of [RFmxNR](crfmxnr.html)

Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured.

The **PI/2 BPSK** modulation type is supported only when you set the [PUSCH Transform Precoding Enabled](attr90001e.html) property to **True**. This property is ignored if you set the [Auto RB Detection Enabled](attr90001f.html) property to **True**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **QPSK**.

| PI/2 BPSK (0) | Specifies a PI/2 BPSK modulation scheme. |
| --- | --- |
| QPSK (1) | Specifies a QPSK modulation scheme. |
| 16 QAM (2) | Specifies a 16 QAM modulation scheme. |
| 64 QAM (3) | Specifies a 64 QAM modulation scheme. |
| 256 QAM (4) | Specifies a 256 QAM modulation scheme. |
| 1024 QAM (5) | Specifies a 1024 QAM modulation scheme. |
| 8 PSK (100) | Specifies a 8 PSK modulation scheme. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90002f.html language=enus -->
## TOPIC 00006: ModAcc:DC Subcarrier Removal Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90002f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90002f.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:DC Subcarrier Removal Enabled Property

**Short Name:**ModAcc DC Subcarrier Removal Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether the DC subcarrier is removed from the EVM results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The DC subcarrier is present in the EVM results. |
| --- | --- |
| True (1) | The DC subcarrier is removed from the EVM results. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900030.html language=enus -->
## TOPIC 00007: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:DMRS Power (dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900030.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:DMRS Power (dB) Property

**Short Name:**PUSCH DMRS Pwr (dB)

Property of [RFmxNR](crfmxnr.html)

Specifies the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This property is ignored if you set the [PUSCH DMRS Pwr Mode](attr900051.html) property to **CDM Groups**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900031.html language=enus -->
## TOPIC 00008: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Configuration Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900031.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Configuration Type Property

**Short Name:**PUSCH DMRS Configuration Type

Property of [RFmxNR](crfmxnr.html)

Specifies the configuration type of DMRS.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Type 1**.

| Type 1 (0) | One DMRS subcarrier alternates with one data subcarrier. |
| --- | --- |
| Type 2 (1) | Two consecutive DMRS subcarriers alternate with four consecutive data subcarriers. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900032.html language=enus -->
## TOPIC 00009: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Additional Positions Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900032.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Additional Positions Property

**Short Name:**PUSCH DMRS Additional Positions

Property of [RFmxNR](crfmxnr.html)

Specifies the number of additional sets of consecutive DMRS symbols in a slot.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **0**.

| 0 (0) | No additional DMRS symbol set is present in the slot. |
| --- | --- |
| 1 (1) | One additional DMRS symbol set is present in the slot. |
| 2 (2) | Two additional DMRS symbol sets are present in the slot. |
| 3 (3) | Three additional DMRS symbol sets are present in the slot. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900033.html language=enus -->
## TOPIC 00010: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Duration Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900033.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Duration Property

**Short Name:**PUSCH DMRS Duration

Property of [RFmxNR](crfmxnr.html)

Specifies whether the DMRS is single-symbol or double-symbol.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Single-Symbol**.

| Single-Symbol (1) | There are one or more non-consecutive DMRS symbols in a slot.. |
| --- | --- |
| Double-Symbol (2) | There are one or more sets of two consecutive DMRS symbols in the slot. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900034.html language=enus -->
## TOPIC 00011: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:PUSCH Mapping Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900034.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:PUSCH Mapping Type Property

**Short Name:**PUSCH Mapping Type

Property of [RFmxNR](crfmxnr.html)

Specifies the mapping type of DMRS.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Type A**.

| Type A (0) | The first DMRS symbol index in a slot is either 2 or 3 based on PUSCH DMRS Type A Position property. |
| --- | --- |
| Type B (1) | The first DMRS symbol index in a slot is the first active PUSCH symbol. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900035.html language=enus -->
## TOPIC 00012: Frequency Range Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900035.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Frequency Range Property

**Short Name:**Frequency Range

Property of [RFmxNR](crfmxnr.html)

Specifies whether to use channel bandwidth and subcarrier spacing configuration supported in Frequency Range 1 (sub 6GHz), Frequency Range 2-1 (between 24.25GHz and 52.6GHz) or Frequency Range 2-2 (between 52.6GHz and 71GHz).

Use "subblock<*n*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Range 1**.

| Range 1 (0) | Measurement uses the channel bandwidth and the subcarrier spacing configuration supported in frequency range 1 (sub 6 GHz). |
| --- | --- |
| Range 2-1 (1) | Measurement uses the channel bandwidth and the subcarrier spacing configuration supported in frequency range 2-1 (between 24.25 GHz and 52.6 GHz). |
| Range 2-2 (2) | Measurement uses the channel bandwidth and the subcarrier spacing configuration supported in frequency range 2-2 (between 52.6 GHz and 71 GHz). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900037.html language=enus -->
## TOPIC 00013: Advanced:Reference Grid Alignment Mode Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900037.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Reference Grid Alignment Mode Property

**Short Name:**Ref Grid Alignment Mode

Property of [RFmxNR](crfmxnr.html)

Specifies whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for the named signals.

The default value is **Auto**.

| Manual (0) | The subcarrier spacing of the reference resource grid and the grid start of each bandwidthpart is user specified. Center of subcarrier 0 in common resource block 0 of the reference resource grid is considered as Reference Point A. |
| --- | --- |
| Auto (1) | The subcarrier spacing of the reference resource grid is determined by the largest subcarrier spacing among the configured bandwidthparts and the SSB. The grid start of each bandwidthpart and the SSB is computed by minimizing k0 to {0, +6} subcarriers. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90003f.html language=enus -->
## TOPIC 00014: Component Carrier:Bandwidth Part:Number of Resource Blocks Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90003f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90003f.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:Number of Resource Blocks Property

**Short Name:**BWP Num RBs

Property of [RFmxNR](crfmxnr.html)

Sets the number of consecutive resource blocks in a bandwidth part.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is -1. If you set this property to -1, all available resource blocks for the specified bandwidth that do not violate the minimum guard band are configured.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900048.html language=enus -->
## TOPIC 00015: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:PUSCH ID Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900048.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900048.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:PUSCH ID Property

**Short Name:**PUSCH DMRS PUSCH ID

Property of [RFmxNR](crfmxnr.html)

Specifies the value of PUSCH DMRS PUSCH ID used for reference signal generation. This property is valid only when you set the [PUSCH Transform Precoding Enabled](attr90001e.html) property to **True** and [PUSCH DMRS PUSCH ID Mode](attr900047.html) property to **User Defined**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0. Valid values are from 0 to 1007, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90005d.html language=enus -->
## TOPIC 00016: Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS Frequency Density Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90005d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90005d.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS Frequency Density Property

**Short Name:**PUSCH PTRS Freq Density

Property of [RFmxNR](crfmxnr.html)

Specifies the density of PTRS in frequency domain. This property is valid only if you set the [PUSCH PTRS Enabled](attr900055.html) property to **True** and [PUSCH Transform Precoding Enabled](attr90001e.html) property to **False**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **2**.

| 2 (2) | The density of PTRS in frequency domain is 2. |
| --- | --- |
| 4 (4) | The density of PTRS in frequency domain is 4. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90005e.html language=enus -->
## TOPIC 00017: Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS RE Offset Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90005e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90005e.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS RE Offset Property

**Short Name:**PUSCH PTRS RE Offset

Property of [RFmxNR](crfmxnr.html)

Specifies the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of *3GPP 38.211* specification. This property is valid only if you set the [PUSCH PTRS Enabled](attr900055.html) property to **True** and [PUSCH Transform Precoding Enabled](attr90001e.html) property to **False**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **00**.

| 00 (0) | The RE offset used for transmission of PTRS is 00. |
| --- | --- |
| 01 (1) | The RE offset used for transmission of PTRS is 01. |
| 10 (2) | The RE offset used for transmission of PTRS is 10. |
| 11 (3) | The RE offset used for transmission of PTRS is 11. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900064.html language=enus -->
## TOPIC 00018: Component Carrier:Bandwidth Part:User:Number of Users Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900064.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900064.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:Number of Users Property

**Short Name:**Num Users

Property of [RFmxNR](crfmxnr.html)

Specifies the number of users present in the bandwidth part.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900065.html language=enus -->
## TOPIC 00019: Component Carrier:Bandwidth Part:User:RNTI Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900065.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900065.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:RNTI Property

**Short Name:**RNTI

Property of [RFmxNR](crfmxnr.html)

Specifies the RNTI.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900069.html language=enus -->
## TOPIC 00020: Component Carrier:Bandwidth Part:User:PDSCH:Number of Resource Blocks Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900069.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900069.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PDSCH:Number of Resource Blocks Property

**Short Name:**PDSCH Num RBs

Property of [RFmxNR](crfmxnr.html)

Specifies the number of consecutive resource blocks in a PDSCH cluster.

Use "pdschcluster<*s*>" or "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>/pdschcluster<*s*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is -1. If you set this property to -1, all available resource blocks within the bandwidth part are configured.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90006a.html language=enus -->
## TOPIC 00021: Component Carrier:Bandwidth Part:User:PDSCH:Modulation Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90006a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90006a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PDSCH:Modulation Type Property

**Short Name:**PDSCH Mod Type

Property of [RFmxNR](crfmxnr.html)

Specifies the modulation scheme used in PDSCH channel of the signal being measured.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **QPSK**.

| QPSK (1) | Specifies a QPSK modulation scheme. |
| --- | --- |
| 16 QAM (2) | Specifies a 16 QAM modulation scheme. |
| 64 QAM (3) | Specifies a 64 QAM modulation scheme. |
| 256 QAM (4) | Specifies a 256 QAM modulation scheme. |
| 1024 QAM (5) | Specifies a 1024 QAM modulation scheme. |
| 8 PSK (100) | Specifies an 8 PSK modulation scheme. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90006b.html language=enus -->
## TOPIC 00022: Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Antenna Ports Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90006b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90006b.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Antenna Ports Property

**Short Name:**PDSCH DMRS Antenna Ports

Property of [RFmxNR](crfmxnr.html)

Specifies the antenna ports used for DMRS transmission.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90009f.html language=enus -->
## TOPIC 00023: Auto Increment Cell ID Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90009f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90009f.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Auto Increment Cell ID Enabled Property

**Short Name:**Auto Increment Cell ID Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement uses the user-configured cell IDs. |
| --- | --- |
| True (1) | The Cell ID of each CC is auto calculated as specified in section 4.9.2.3 of 3GPP 38.141 specification. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr9000a0.html language=enus -->
## TOPIC 00024: gNodeB Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr9000a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr9000a0.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

gNodeB Type Property

**Short Name:**gNodeB Type

Property of [RFmxNR](crfmxnr.html)

Specifies the downlink gNodeB (Base Station) type. Refer to the *3GPP 38.104* specification for more information about gNodeB Type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Type 1-C**.

| Type 1-C (0) | Type 1-C NR base station operating at FR1 and conducted requirements apply. |
| --- | --- |
| Type 1-H (1) | Type 1-H base station operating at FR1 and conducted and OTA requirements apply. |
| Type 1-O (2) | Type 1-O base station operating at FR1 and OTA requirements apply. |
| Type 2-O (3) | Type 2-O base station operating at FR2 and OTA requirements apply. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr9000a3.html language=enus -->
## TOPIC 00025: Satellite Access Node Class Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr9000a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr9000a3.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Satellite Access Node Class Property

**Short Name:**SAN Class

Property of [RFmxNR](crfmxnr.html)

Specifies the downlink SAN (Satellite Access Node) class representing the satellite constellation as specified in section 6.6.4 of *3GPP 38.108* specification.

This property impacts the spectral emission mask for downlink.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **GEO (0)**.

| GEO (0) | Specifies the downlink SAN (Satellite Access Node) class corresponding to GEO satellite constellation. |
| --- | --- |
| LEO (1) | Specifies the downlink SAN (Satellite Access Node) class corresponding to LEO satellite constellation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900107.html language=enus -->
## TOPIC 00026: Component Carrier:Bandwidth Part:CORESET:Symbol Offset Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900107.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900107.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:CORESET:Symbol Offset Property

**Short Name:**CORESET Symbol Offset

Property of [RFmxNR](crfmxnr.html)

Specifies the starting symbol number of the CORESET within a slot.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90010a.html language=enus -->
## TOPIC 00027: Component Carrier:Bandwidth Part:CORESET:Resource Block Offset Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90010a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90010a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:CORESET:Resource Block Offset Property

**Short Name:**CORESET RB Offset

Property of [RFmxNR](crfmxnr.html)

Specifies the starting resource block of a CORESET cluster.

Use "coresetcluster<*j*>" or "coreset<*k*>" or "bwp<*l*>" or "carrier<*m*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*m*>/bwp<*l*>/coreset<*k*>"/coresetcluster<*j*> as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

Valid values should be a multiple of 6. The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90010e.html language=enus -->
## TOPIC 00028: Component Carrier:Bandwidth Part:CORESET:REG Bundle Size Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90010e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90010e.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:CORESET:REG Bundle Size Property

**Short Name:**CORESET REG Bundle Size

Property of [RFmxNR](crfmxnr.html)

Specifies the RBG bundle size of CORESET for interleaved CCE to REG mapping.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **6**.

For interleaved Mapping Type, the valid values are 2, 3, and 6. For non-interleaved Mapping Type, the valid value is 6.

| 2 (2) | The RBG bundle size of CORESET is 2. |
| --- | --- |
| 3 (3) | The RBG bundle size of CORESET is 3. |
| 6 (6) | The RBG bundle size of CORESET is 6. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90010f.html language=enus -->
## TOPIC 00029: Component Carrier:Bandwidth Part:CORESET:Interleaver Size Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90010f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90010f.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:CORESET:Interleaver Size Property

**Short Name:**CORESET Interleaver Size

Property of [RFmxNR](crfmxnr.html)

Specifies the interleaver size of CORESET for interleaved CCE to REG mapping.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **2**.

| 2 (2) | Interleaver size is 2. |
| --- | --- |
| 3 (3) | Interleaver size is 3. |
| 6 (6) | Interleaver size is 6. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900110.html language=enus -->
## TOPIC 00030: Component Carrier:Bandwidth Part:CORESET:Shift Index Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900110.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900110.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:CORESET:Shift Index Property

**Short Name:**CORESET Shift Index

Property of [RFmxNR](crfmxnr.html)

Specifies the shift index of CORESET for interleaved CCE to REG mapping.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900118.html language=enus -->
## TOPIC 00031: Component Carrier:Allocated Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900118.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900118.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Allocated Property

**Short Name:**CC Allocated

Property of [RFmxNR](crfmxnr.html)

Specifies whether a component carrier has one or more resource elements allocated.

While performing IBE measurement on a subblock, you set this property to **False** for all secondary component carriers as specified in section 6.4A.2.3 of *3GPP 38.521-1* and *3GPP 38.521-2* specifications.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **True**.

| False (0) | No resource elements are allocated for the component carrier. Only subblock IBE is computed. |
| --- | --- |
| True (1) | One or more resource elements are allocated for the component carrier. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90011e.html language=enus -->
## TOPIC 00032: Downlink Test Model Cell ID Mode Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90011e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90011e.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Downlink Test Model Cell ID Mode Property

**Short Name:**DL Test Model Cell ID Mode

Property of [RFmxNR](crfmxnr.html)

Specifies whether the cell ID of downlink test model component carriers is auto calculated and configured by the measurement or configured by the user.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Auto (0) | Cell ID of each CC is auto calculated as specified in section 4.9.2.3 of the 3GPP 38.141 specification. |
| --- | --- |
| Manual (1) | The measurement uses the user-configured cell IDs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr900121.html language=enus -->
## TOPIC 00033: Component Carrier:Bandwidth Part:DC Location Known Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr900121.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr900121.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Bandwidth Part:DC Location Known Property

**Short Name:**BWP DC Location Known

Property of [RFmxNR](crfmxnr.html)

Specifies whether Uplink Tx Direct Current location within the carrier is determined. If set to **False**, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only **General** In-Band Emission limits are applied. If set to **True**, DC location is determined within the carrier.

This property is not supported when [Link Direction](attr90000e.html) property is set to **Downlink**.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **True**.

| False (0) | DC Location is un-known. |
| --- | --- |
| True (1) | DC Location is known. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr901000.html language=enus -->
## TOPIC 00034: ACP:Measurement Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr901000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr901000.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Enabled Property

**Short Name:**ACP Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether to enable the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr901042.html language=enus -->
## TOPIC 00035: ACP:Results:Upper Offset:Relative Power (dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr901042.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr901042.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Relative Power (dB) Property

**Short Name:**ACP Results Upper Offset Rel Pwr (dB)

Property of [RFmxNR](crfmxnr.html)

Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr901043.html language=enus -->
## TOPIC 00036: ACP:Offset:Number of ENDC Offsets Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr901043.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr901043.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Number of ENDC Offsets Property

**Short Name:**ACP Num ENDC Offsets

Property of [RFmxNR](crfmxnr.html)

Specifies the number of ENDC adjacent channel offsets to be configured at offset positions.

Use "subblock<*n*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is dependent on 3GPP specification.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr901046.html language=enus -->
## TOPIC 00037: ACP:FFT:Overlap Mode Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr901046.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr901046.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap Mode Property

**Short Name:**ACP FFT Overlap Mode

Property of [RFmxNR](crfmxnr.html)

Specifies the overlap mode when you set the [ACP Meas Method](attr90101c.html) property to **Sequential FFT**. In the Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. The FFT is then computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | Disables the overlap between the FFT chunks. |
| --- | --- |
| Automatic (1) | Measurement sets the overlap based on the value you have set for the ACP FFT Window property. When you set the ACP FFT Window property to any value other than None, the number of overlapped samples between consecutive chunks is set to 50% of the value of the ACP Sequential FFT Size property. When you set the ACP FFT Window property to None, the chunks are not overlapped and the overlap is set to 0%. |
| User Defined (2) | Measurement uses the overlap that you specify in the ACP FFT Overlap property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr901048.html language=enus -->
## TOPIC 00038: ACP:Measurement Mode Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr901048.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr901048.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Mode Property

**Short Name:**ACP Meas Mode

Property of [RFmxNR](crfmxnr.html)

Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement.

Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?topicname=rfmxspecan/noise_compensation_algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Measure (0) | Performs the ACP measurement on the acquired signal. |
| --- | --- |
| Calibrate Noise Floor (1) | Performs manual noise calibration of the signal analyzer for the ACP measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90300e.html language=enus -->
## TOPIC 00039: CHP:Averaging:Count Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90300e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90300e.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Count Property

**Short Name:**CHP Averaging Count

Property of [RFmxNR](crfmxnr.html)

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](attr90300d.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr903010.html language=enus -->
## TOPIC 00040: CHP:Averaging:Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr903010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr903010.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Type Property

**Short Name:**CHP Averaging Type

Property of [RFmxNR](crfmxnr.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **RMS**.

| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr903012.html language=enus -->
## TOPIC 00041: CHP:Amplitude Correction Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr903012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr903012.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

CHP:Amplitude Correction Type Property

**Short Name:**CHP Amplitude Correction Type

Property of [RFmxNR](crfmxnr.html)

Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the [RFmxInstr Configure External Attenuation Table](/csh?topicname=rfmxinstrvi/rfmxinstr_configure_external_attenuation_table.html) VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| RF Center Frequency (0) | All frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| --- | --- |
| Spectrum Frequency Bin (1) | Individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr903024.html language=enus -->
## TOPIC 00042: CHP:Noise Calibration:Averaging:Count Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr903024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr903024.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

CHP:Noise Calibration:Averaging:Count Property

**Short Name:**CHP Noise Cal Averaging Count

Property of [RFmxNR](crfmxnr.html)

Specifies the averaging count used for noise calibration when you set the [CHP Noise Cal Averaging Auto](attr903025.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 32.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr903025.html language=enus -->
## TOPIC 00043: CHP:Noise Calibration:Averaging:Auto Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr903025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr903025.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

CHP:Noise Calibration:Averaging:Auto Property

**Short Name:**CHP Noise Cal Averaging Auto

Property of [RFmxNR](crfmxnr.html)

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | RFmx uses the averages that you set for CHP Noise Cal Averaging Count property. |
| --- | --- |
| True (1) | RFmx uses a noise calibration averaging count of 32. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr903026.html language=enus -->
## TOPIC 00044: CHP:Noise Calibration:Mode Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr903026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr903026.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

CHP:Noise Calibration:Mode Property

**Short Name:**CHP Noise Cal Mode

Property of [RFmxNR](crfmxnr.html)

Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx.

Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?topicname=rfmxspecan/noise_compensation_algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Manual (0) | When you set CHP Meas Mode property to Calibrate Noise Floor, you can initiate the instrument noise calibration for CHP manually. When you set the CHP Meas Mode property to Measure, you can initiate the CHP measurement manually. |
| --- | --- |
| Auto (1) | When you set the CHP Noise Comp Enabled property to True, RFmx sets the Input Isolation Enabled property to Enabled and calibrates the instrument noise in the current state of the instrument. Next, RFmx resets the Input Isolation Enabled property and performs the CHP measurement including compensation for the noise contribution of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set the CHP Noise Comp Enabled to False, RFmx does not calibrate instrument noise and performs the CHP measurement without compensating for the noise contribution of the instrument. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr904006.html language=enus -->
## TOPIC 00045: ModAcc:Measurement Offset Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr904006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr904006.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Offset Property

**Short Name:**ModAcc Meas Offset

Property of [RFmxNR](crfmxnr.html)

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [ModAcc Sync Mode](attr904004.html) property. The unit for this is specified by [ModAcc Measurement Length Unit](attr904005.html).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr904057.html language=enus -->
## TOPIC 00046: ModAcc:Results:PDSCH:PDSCH 64 QAM RMS EVM Mean (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr904057.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr904057.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH 64 QAM RMS EVM Mean (% or dB) Property

**Short Name:**ModAcc Results PDSCH 64 QAM RMS EVM Mean

Property of [RFmxNR](crfmxnr.html)

Returns the mean value of RMS EVMs calculated over measurement length on all 64 QAM modulated PDSCH data symbols.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr904058.html language=enus -->
## TOPIC 00047: ModAcc:Results:PDSCH:PDSCH 256 QAM RMS EVM Mean (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr904058.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr904058.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH 256 QAM RMS EVM Mean (% or dB) Property

**Short Name:**ModAcc Results PDSCH 256 QAM RMS EVM Mean

Property of [RFmxNR](crfmxnr.html)

Returns the mean value of RMS EVMs calculated over measurement length on all 256 QAM modulated PDSCH data symbols.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr904059.html language=enus -->
## TOPIC 00048: ModAcc:Results:PDSCH:PDSCH Data RMS EVM Mean (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr904059.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr904059.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH Data RMS EVM Mean (% or dB) Property

**Short Name:**ModAcc Results PDSCH Data RMS EVM Mean

Property of [RFmxNR](crfmxnr.html)

Returns the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90405a.html language=enus -->
## TOPIC 00049: ModAcc:Results:PDSCH:PDSCH Data Peak EVM Maximum (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90405a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90405a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH Data Peak EVM Maximum (% or dB) Property

**Short Name:**ModAcc Results PDSCH Data Pk EVM Max

Property of [RFmxNR](crfmxnr.html)

Returns the maximum value of peak EVMs calculated over measurement length on PDSCH data symbols.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90405b.html language=enus -->
## TOPIC 00050: ModAcc:Results:PDSCH:PDSCH DMRS RMS EVM Mean (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90405b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90405b.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH DMRS RMS EVM Mean (% or dB) Property

**Short Name:**ModAcc Results PDSCH DMRS RMS EVM Mean

Property of [RFmxNR](crfmxnr.html)

Returns the mean value of RMS EVMs calculated over measurement length on PDSCH DMRS.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90405c.html language=enus -->
## TOPIC 00051: ModAcc:Results:PDSCH:PDSCH DMRS Peak EVM Maximum (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90405c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90405c.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH DMRS Peak EVM Maximum (% or dB) Property

**Short Name:**ModAcc Results PDSCH DMRS Pk EVM Max

Property of [RFmxNR](crfmxnr.html)

Returns the maximum value of peak EVMs calculated over measurement length on PDSCH DMRS.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90405d.html language=enus -->
## TOPIC 00052: ModAcc:Results:PDSCH:PDSCH PTRS RMS EVM Mean (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90405d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90405d.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH PTRS RMS EVM Mean (% or dB) Property

**Short Name:**ModAcc Results PDSCH PTRS RMS EVM Mean

Property of [RFmxNR](crfmxnr.html)

Returns the mean value of RMS EVMs calculated over measurement length on PDSCH PTRS.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90405e.html language=enus -->
## TOPIC 00053: ModAcc:Results:PDSCH:PDSCH PTRS Peak EVM Maximum (% or dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90405e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90405e.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:PDSCH:PDSCH PTRS Peak EVM Maximum (% or dB) Property

**Short Name:**ModAcc Results PDSCH PTRS Pk EVM Max

Property of [RFmxNR](crfmxnr.html)

Returns the maximum value of peak EVMs calculated over measurement length on PDSCH PTRS.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr904062.html language=enus -->
## TOPIC 00054: ModAcc:Results:Subblock LO Component Carrier Index Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr904062.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr904062.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Subblock LO Component Carrier Index Property

**Short Name:**ModAcc Results Subblock LO CC Index

Property of [RFmxNR](crfmxnr.html)

Returns the index of the component carrier that includes the LO of the transmitter according to the [Subblock Freq (Hz)](attr90011f.html) and [Subblock TX LO Freq](attr900060.html) properties. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the property returns -1. This result is valid only when you set the [Transmitter Architecture](attr90043b.html) property to **LO per Subblock**.

Use "subblock<*n*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90408a.html language=enus -->
## TOPIC 00055: ModAcc:Results:Spectral Flatness:Range1-Min (dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90408a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90408a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Spectral Flatness:Range1-Min (dB) Property

**Short Name:**ModAcc Results Spectral Flatness Range1-Min (dB)

Property of [RFmxNR](crfmxnr.html)

Returns the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr9040a4.html language=enus -->
## TOPIC 00056: ModAcc:Transient:Transient Period Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr9040a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr9040a4.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Transient:Transient Period Property

**Short Name:**ModAcc Transient Period

Property of [RFmxNR](crfmxnr.html)

It configures the transient duration as specified in section 6.4.2.1a of *3GPP 38.101-1* specification.

If [Transient Period EVM Mode](attr9040a3.html) is set to **Include**, configures the transient duration to calculate FFT window positions used to compute the transient EVM as specified in section 6.4.2.1a of *3GPP 38.101-1* specification.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **2us**.

| 2us (2e-06) |  |
| --- | --- |
| 4us (4e-06) |  |
| 7us (7e-06) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr906006.html language=enus -->
## TOPIC 00057: OBW:RBW Filter:Auto Bandwidth Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr906006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr906006.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Auto Bandwidth Property

**Short Name:**OBW RBW Auto

Property of [RFmxNR](crfmxnr.html)

Specifies whether the measurement computes the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the RBW that you specify in the OBW RBW property. |
| --- | --- |
| True (1) | The measurement computes the RBW. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90600b.html language=enus -->
## TOPIC 00058: OBW:Averaging:Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90600b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90600b.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Enabled Property

**Short Name:**OBW Averaging Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether to enable averaging for the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90600c.html language=enus -->
## TOPIC 00059: OBW:Averaging:Count Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90600c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90600c.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Count Property

**Short Name:**OBW Averaging Count

Property of [RFmxNR](crfmxnr.html)

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](attr90600b.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr906011.html language=enus -->
## TOPIC 00060: OBW:Amplitude Correction Type Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr906011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr906011.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

OBW:Amplitude Correction Type Property

**Short Name:**OBW Amplitude Correction Type

Property of [RFmxNR](crfmxnr.html)

Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?topicname=rfmxinstrvi/rfmxinstr_configure_external_attenuation_table.html) VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

| RF Center Frequency (0) | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| --- | --- |
| Spectrum Frequency Bin (1) | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr906012.html language=enus -->
## TOPIC 00061: OBW:All Traces Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr906012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr906012.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

OBW:All Traces Enabled Property

**Short Name:**OBW All Traces Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr906018.html language=enus -->
## TOPIC 00062: OBW:Results:Subblock:Stop Frequency (Hz) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr906018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr906018.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Subblock:Stop Frequency (Hz) Property

**Short Name:**OBW Results Stop Freq (Hz)

Property of [RFmxNR](crfmxnr.html)

Returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:

*Occupied bandwidth* = *Stop frequency* - *Start frequency*

Use "subblock<*n*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90700a.html language=enus -->
## TOPIC 00063: TXP:Results:Average Power Mean (dBm) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90700a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90700a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:Average Power Mean (dBm) Property

**Short Name:**TXP Results Avg Pwr Mean (dBm)

Property of [RFmxNR](crfmxnr.html)

Returns the average power of the acquired signal.

When you set the [Averaging Enabled](attr907004.html) property to **True**, it returns the max of the peak power computed for each averaging count.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **dBm**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr908027.html language=enus -->
## TOPIC 00064: SEM:Results:Lower Offset:Absolute Peak Power (dBm) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr908027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr908027.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Absolute Peak Power (dBm) Property

**Short Name:**SEM Results Lower Offset Abs Pk Pwr (dBm)

Property of [RFmxNR](crfmxnr.html)

Returns the peak power in the lower (negative) offset segment. This value is expressed in dBm.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90802a.html language=enus -->
## TOPIC 00065: SEM:Results:Lower Offset:Margin (dB) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90802a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90802a.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Margin (dB) Property

**Short Name:**SEM Results Lower Offset Margin (dB)

Property of [RFmxNR](crfmxnr.html)

Returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90802b.html language=enus -->
## TOPIC 00066: SEM:Results:Lower Offset:Margin Absolute Power (dBm) Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90802b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90802b.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Margin Absolute Power (dBm) Property

**Short Name:**SEM Results Lower Offset Margin Abs Pwr (dBm)

Property of [RFmxNR](crfmxnr.html)

Returns the power at which the Margin occurs in the lower (negative) offset segment. This value is expressed in dBm.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr908040.html language=enus -->
## TOPIC 00067: SEM:FFT:Window Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr908040.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr908040.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

SEM:FFT:Window Property

**Short Name:**SEM FFT Window

Property of [RFmxNR](crfmxnr.html)

Specifies the FFT window type to be used to reduce spectral leakage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Flat Top**.

| None (0) | No spectral leakage. |
| --- | --- |
| Flat Top (1) | Spectral leakage is reduced using flat top window type. |
| Hanning (2) | Spectral leakage is reduced using Hanning window type. |
| Hamming (3) | Spectral leakage is reduced using Hamming window type. |
| Gaussian (4) | Spectral leakage is reduced using Gaussian window type. |
| Blackman (5) | Spectral leakage is reduced using Blackman window type. |
| Blackman-Harris (6) | Spectral leakage is reduced using Blackman-Harris window type. |
| Kaiser-Bessel (7) | Spectral leakage is reduced using Kaiser-Bessel window type. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr909009.html language=enus -->
## TOPIC 00068: PVT:All Traces Enabled Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr909009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr909009.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

PVT:All Traces Enabled Property

**Short Name:**PVT All Traces Enabled

Property of [RFmxNR](crfmxnr.html)

Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/attr90900c.html language=enus -->
## TOPIC 00069: PVT:Results:Measurement Status Property

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/attr90900c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/attr90900c.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Measurement Status Property

**Short Name:**PVT Results Meas Status

Property of [RFmxNR](crfmxnr.html)

Returns the measurement status indicating whether the off power before and after is within the standard defined limit.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) to read this property.

The default value is 0.

| Fail (0) | Indicates that the measurement has failed. |
| --- | --- |
| Pass (1) | Indicates that the measurement has passed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-nr-prop path=rfmxnrprop/crfmxnr.html language=enus -->
## TOPIC 00070: RFmxNR Properties

- bundle_id: `rfmx-nr-prop`
- source_path: `rfmxnrprop/crfmxnr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-nr-prop/raw/resource/enus/rfmxnrprop/crfmxnr.html
- document_id: `rfmx-nr-prop`
- page_type: `leaf`
- content_type: ``

RFmxNR Properties

Use the RFmxNR properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the active channel string used to access all subsequent channel-based properties in this instance of the property node. Details |
| Selected Ports | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. Details |
| Center Frequency (Hz) | Specifies the center frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. Details |
| Reference Level | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. Details |
| External Attenuation (dB) | Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. Details |
| Reference Level Headroom | Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Details |
| Trigger:Type | Specifies the type of trigger to be used for signal acquisition. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:IQ Power Edge:Source | Specifies the channel from which the device monitors the trigger. Details |
| Trigger:IQ Power Edge:Level (dB or dBm) | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative; and in dBm when you set the IQ Power Edge Level Type property to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level Type | Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Slope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. Details |
| Trigger:Delay (s) | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples. Details |
| Trigger:Minimum Quiet Time:Mode | Specifies whether the measurement computes the minimum quiet time used for triggering. Details |
| Trigger:Minimum Quiet Time:Duration (s) | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope, the signal is quiet above the trigger level. Details |
| Link Direction | Specifies the link direction of the received signal. Details |
| gNodeB Category | Specifies the downlink gNodeB (Base Station) category. Refer to the 3GPP 38.104 specification for more information about gNodeB category. Details |
| gNodeB Type | Specifies the downlink gNodeB (Base Station) type. Refer to the 3GPP 38.104 specification for more information about gNodeB Type. Details |
| Satellite Access Node Class | Specifies the downlink SAN (Satellite Access Node) class representing the satellite constellation as specified in section 6.6.4 of 3GPP 38.108 specification. Details |
| Transmit Antenna to Analyze | Specifies the physical antenna that is currently connected to the analyzer. Details |
| Power Class | Specifies the power class for the UE as specified in section 6.2 of 3GPP 38.101-1/2/3 specification. Details |
| PIby2BPSK Power Boost Enabled | Specifies the power boost for PI/2 BPSK signal when you set the Frequency Range property to Range 1. This property is valid only for uplink direction. Details |
| Signal Detection:Auto Resource Block Detection Enabled | Specifies whether the values of modulation type, number of resource block clusters, resource block offsets, and number of resource blocks are auto-detected by the measurement or configured by you. Details |
| Signal Detection:Auto Cell ID Detection Enabled | Specifies whether to enable the autodetection of the cell ID. Details |
| Downlink Channel Configuration Mode | Specifies the downlink channel configuration mode. Details |
| Auto Increment Cell ID Enabled | Specifies whether the cell ID of component carrier is auto calculated and configured by the measurement or configured by the user. Details |
| Downlink Test Model Cell ID Mode | Specifies whether the cell ID of downlink test model component carriers is auto calculated and configured by the measurement or configured by the user. Details |
| Number of Subblocks | Specifies the number of subblocks configured in intraband non-contiguous carrier aggregation scenarios. Details |
| Subblock Frequency (Hz) | Specifies the offset of the subblock from the Center Freq (Hz). Details |
| Subblock Transmit LO Frequency (Hz) | Specifies the frequency of the transmitters local oscillator. This value is expressed in Hz. The frequency is defined per subblock and relative to the respective subblock center frequency. Details |
| Phase Compensation Frequency (Hz) | Specifies the frequency used for phase compensation of the signal when you set the Ph Compensation property to User Defined. This value is expressed in Hz. Details |
| Frequency Range | Specifies whether to use channel bandwidth and subcarrier spacing configuration supported in Frequency Range 1 (sub 6GHz), Frequency Range 2-1 (between 24.25GHz and 52.6GHz) or Frequency Range 2-2 (between 52.6GHz and 71GHz). Details |
| Band | Specifies the evolved universal terrestrial radio access (E-UTRA) or NR operating frequency band of a subblock as specified in section 5.2 of the 3GPP 38.101-1/2/3 specification. Band determines the spectral flatness mask and spectral emission mask. Details |
| Subblock ENDC Nominal Spacing Adjustment (Hz) | Specifies the adjustment of the center frequency for adjacent E-UTRA and NR Channels in case of nominal spacing. The value is expressed in Hz. Details |
| Channel Raster (Hz) | Specifies the subblock channel raster which is used for computing nominal spacing between aggregated carriers as specified in section 5.4A.1 of 3GPP 38.101-1/2 specification and section 5.4.1.2 of 3GPP TS 38.104 specification. The value is expressed in Hz. Details |
| Component Carrier Spacing Type | Specifies the spacing between adjacent component carriers (CCs) within a subblock. Details |
| Component Carrier at Center Frequency | Specifies the index of the component carrier having its center at the user-configured center frequency. The measurement uses this property along with CC Spacing Type property to calculate the value of the CC Freq. This property is ignored if you set the CC Spacing Type property to User. Details |
| Component Carrier:Number of Component Carriers | Specifies the number of component carriers configured within a subblock. Set this property to 1 for single carrier. Details |
| Component Carrier:Downlink Test Model | Specifies the NR test model type when you set the Channel Configuration Mode property to Test Model. Refer to section 4.9.2 of the 3GPP 38.141 specification for more information regarding test model configurations. Details |
| Component Carrier:Downlink Test Model Modulation Type | Specifies the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. Details |
| Component Carrier:Downlink Test Model Duplex Scheme | Specifies the duplexing technique of the signal being measured. Refer to section 4.9.2 of 3GPP 38.141 specification for more information regarding test model configurations based on duplex scheme. Details |
| Component Carrier:Rated TRP (dBm) | Specifies the rated carrier TRP output power. This value is expressed in dBm. Details |
| Component Carrier:Rated EIRP (dBm) | Specifies the rated carrier EIRP output power. This value is expressed in dBm. Details |
| Component Carrier:Bandwidth (Hz) | Specifies the channel bandwidth of the signal being measured. This value is expressed in Hz. Details |
| Component Carrier:Frequency (Hz) | Specifies the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency property. This value is expressed in Hz. Details |
| Component Carrier:Allocated | Specifies whether a component carrier has one or more resource elements allocated. While performing IBE measurement on a subblock, you set this property to False for all secondary component carriers as specified in section 6.4A.2.3 of 3GPP 38.521-1 and 3GPP 38.521-2 specifications. Details |
| Component Carrier:Radio Access Type | Specifies if a carrier is a NR or an E-UTRA carrier while using dual connectivity (EN-DC) signal. Details |
| Component Carrier:Cell ID | Specifies a physical layer cell identity. Details |
| Component Carrier:Reference Grid Subcarrier Spacing (Hz) | Specifies the subcarrier spacing of the reference resource grid when you set the Reference Grid Alignment Mode property to Manual. This should be the largest subcarrier spacing used in the component carrier. This value is expressed in Hz. Details |
| Component Carrier:Reference Grid Start | Specifies the reference resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode property to Manual. Center of subcarrier 0 in common resource block 0 is considered as Reference Point A. Details |
| Component Carrier:Reference Grid Size | Specifies the reference resource grid size when you set the Grid Size Mode property to Manual. Details |
| Component Carrier:Sub-band Allocation | Details |
| Component Carrier:Bandwidth Part:Number of Bandwidth Parts | Specifies the number of bandwidth parts present in the component carrier. Details |
| Component Carrier:Bandwidth Part:Subcarrier Spacing (Hz) | Specifies the subcarrier spacing of the bandwidth part used in the component carrier. Details |
| Component Carrier:Bandwidth Part:Cyclic Prefix Mode | Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. Details |
| Component Carrier:Bandwidth Part:Grid Start | Specifies the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode property to Manual. Details |
| Component Carrier:Bandwidth Part:Grid Size | Specifies the reference resource grid size when you set the Grid Size Mode property to Manual. Details |
| Component Carrier:Bandwidth Part:Resource Block Offset | Specifies the resource block offset of a bandwidth part relative to the resource Grid Start property. Details |
| Component Carrier:Bandwidth Part:Number of Resource Blocks | Sets the number of consecutive resource blocks in a bandwidth part. Details |
| Component Carrier:Bandwidth Part:DC Location Known | Specifies whether Uplink Tx Direct Current location within the carrier is determined. If set to False, DC location is undetermined within the carrier. In ModAcc measurement, IQ impairments are not estimated and compensated, and only General In-Band Emission limits are applied. If set to True, DC location is determined within the carrier. This property is not supported when Link Direction property is set to Downlink. Details |
| Component Carrier:Bandwidth Part:User:Number of Users | Specifies the number of users present in the bandwidth part. Details |
| Component Carrier:Bandwidth Part:User:RNTI | Specifies the RNTI. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Number of PUSCH Configurations | Specifies the number of PUSCH slot configurations. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Transform Precoding Enabled | Specifies whether transform precoding is enabled. Enable transform precoding when analyzing a DFT-s-OFDM waveform. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Number of Resource Block Clusters | Specifies the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. This property is ignored if you set the Auto RB Detection Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Resource Block Offset | Specifies the starting resource block number of a PUSCH cluster. This property is ignored if you set the Auto RB Detection Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Number of Resource Blocks | Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This property is ignored if you set the Auto RB Detection Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Modulation Type | Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Release Version | Specifies the 3GGP release version for PUSCH DMRS. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Antenna Ports | Specifies the antenna ports used for DMRS transmission. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:DMRS Power Mode | Specifies whether the value of PUSCH DMRS Pwr property is calculated based on the PUSCH DMRS Num CDM Groups property or specified by you. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:DMRS Power (dB) | Specifies the factor which boosts the PUSCH DMRS REs. This value is expressed in dB. This property is ignored if you set the PUSCH DMRS Pwr Mode property to CDM Groups. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Number of CDM Groups | Specifies the number of CDM groups, when you set the PUSCH Transform Precoding Enabled property to False, otherwise it is coerced to 2. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Pseudo Random Sequence:Scrambling ID Mode | Specifies whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Pseudo Random Sequence:Scrambling ID | Specifies the value of scrambling ID. This property is valid only when you set the PUSCH Transform Precoding Enabled property to False. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Pseudo Random Sequence:nSCID | Specifies the value of PUSCH DMRS nSCID used for reference signal generation. This property is valid only when you set the PUSCH Transform Precoding Enabled property to False. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:Group Hopping Enabled | Specifies whether the group hopping is enabled. This property is valid only when you set the PUSCH Transform Precoding Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:Sequence Hopping Enabled | Specifies whether the sequence hopping is enabled. This property is valid only when you set the PUSCH Transform Precoding Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:PUSCH ID Mode | Specifies whether PUSCH DMRS PUSCH ID is based on Cell ID or specified by you. This property is valid only when you set the PUSCH Transform Precoding Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Low PAPR Sequence:PUSCH ID | Specifies the value of PUSCH DMRS PUSCH ID used for reference signal generation. This property is valid only when you set the PUSCH Transform Precoding Enabled property to True and PUSCH DMRS PUSCH ID Mode property to User Defined. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Configuration Type | Specifies the configuration type of DMRS. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:PUSCH Mapping Type | Specifies the mapping type of DMRS. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Type A Position | Specifies the position of first DMRS symbol in a slot when you set the PUSCH Mapping Type property to Type A. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Duration | Specifies whether the DMRS is single-symbol or double-symbol. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Additional Positions | Specifies the number of additional sets of consecutive DMRS symbols in a slot. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Enabled | Specifies whether the PUSCH transmission contains PTRS signals. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Antenna Ports | Specifies the DMRS antenna ports associated with PTRS transmission. This property is valid only if you set the PUSCH PTRS Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:PTRS Power Mode | Specifies whether the PUSCH PTRS power scaling is calculated as defined in 3GPP specification or specified by you. This property is valid only if you set the PUSCH PTRS Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:PTRS Power (dB) | Specifies the factor by which the PUSCH PTRS REs are boosted. This value is expressed in dB. This property is valid only if you set the PUSCH PTRS Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Transform Precoding Sequence:Number of PTRS Groups | Specifies the number of PTRS groups per OFDM symbol. This property is valid only if you set the PUSCH PTRS Enabled property to True and PUSCH Transform Precoding Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Transform Precoding Sequence:Samples per PTRS Group | Specifies the number of samples per each PTRS group. This property is valid only if you set the PUSCH PTRS Enabled property to True and PUSCH Transform Precoding Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS Time Density | Specifies the density of PTRS in time domain. This property is valid only if you set the PUSCH PTRS Enabled property to True. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS Frequency Density | Specifies the density of PTRS in frequency domain. This property is valid only if you set the PUSCH PTRS Enabled property to True and PUSCH Transform Precoding Enabled property to False. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS RE Offset | Specifies the RE offset to be used for transmission of PTRS as defined in the Table 6.4.1.2.2.1-1 of 3GPP 38.211 specification. This property is valid only if you set the PUSCH PTRS Enabled property to True and PUSCH Transform Precoding Enabled property to False. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Slot Allocation | Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots. Details |
| Component Carrier:Bandwidth Part:User:PUSCH:Symbol Allocation | Specifies the symbol allocation of each slot allocation. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Number of PDSCH Configurations | Specifies the number of PDSCH slot configurations. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Number of Resource Block Clusters | Specifies the number of clusters of resource allocations with each cluster including one or more consecutive resource blocks. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Resource Block Offset | Specifies the starting resource block number of a PDSCH cluster. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Number of Resource Blocks | Specifies the number of consecutive resource blocks in a PDSCH cluster. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Modulation Type | Specifies the modulation scheme used in PDSCH channel of the signal being measured. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Release Version | Specifies the 3GGP release version for PDSCH DMRS. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Antenna Ports | Specifies the antenna ports used for DMRS transmission. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:DMRS Power Mode | Specifies whether the configured PDSCH DMRS Pwr is calculated based on the PDSCH DMRS Num CDM Groups or specified by you. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:DMRS Power (dB) | Specifies the factor by which the PDSCH DMRS REs are boosted. This value is expressed in dB. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Number of CDM Groups | Specifies the number of CDM groups. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Pseudo Random Sequence:Scrambling ID Mode | Specifies whether the configured Scrambling ID is based on Cell ID or specified by you. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Pseudo Random Sequence:Scrambling ID | Specifies the value of scrambling ID used for reference signal generation. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Pseudo Random Sequence:nSCID | Specifies the value of PDSCH DMRS nSCID used for reference signal generation. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Configuration Type | Specifies the configuration type of DMRS. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:PDSCH Mapping Type | Specifies the mapping type of DMRS. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Type A Position | Specifies the position of first DMRS symbol in a slot for Type A configurations. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Duration | Specifies whether the DMRS is single-symbol or double-symbol. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Additional Positions | Specifies the number of additional sets of consecutive DMRS symbols in a slot. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Enabled | Specifies whether PT-RS is present in the transmitted signal. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Antenna Ports | Specifies the DMRS Antenna Ports associated with PTRS transmission. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:PTRS Power Mode | Specifies whether the configured PDSCH PTRS Pwr is calculated as defined in 3GPP specification or configured by you. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:EPRE Ratio Port | Specifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode property to Standard. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:PTRS Power (dB) | Specifies the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this property is taken as an input when you set the PDSCH PTRS Pwr Mode property to User Defined. If you set the PDSCH PTRS Pwr Mode property to Standard, the value is computed from other parameters. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Mapping:PDSCH PTRS Time Density | Specifies the density of PTRS in time domain Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Mapping:PDSCH PTRS Frequency Density | Specifies the density of PTRS in frequency domain Details |
| Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Mapping:PDSCH PTRS RE Offset | Specifies the RE Offset to be used for transmission of PTRS as defined in Table 7.4.1.2.2-1 of 3GPP 38.211 specification. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Slot Allocation | Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots. Details |
| Component Carrier:Bandwidth Part:User:PDSCH:Symbol Allocation | Specifies the symbol allocation of each slot allocation. Details |
| Component Carrier:Bandwidth Part:CORESET:Number of CORESETs | Specifies the number of CORSETs present in the bandwidth part. Details |
| Component Carrier:Bandwidth Part:CORESET:Symbol Offset | Specifies the starting symbol number of the CORESET within a slot. Details |
| Component Carrier:Bandwidth Part:CORESET:Number of Symbols | Specifies the number of symbols allotted to CORESET in each slot. Details |
| Component Carrier:Bandwidth Part:CORESET:Number of Resource Block Clusters | Specifies the number of RB clusters present in the CORESET. Details |
| Component Carrier:Bandwidth Part:CORESET:Resource Block Offset | Specifies the starting resource block of a CORESET cluster. Details |
| Component Carrier:Bandwidth Part:CORESET:Number of Resource Blocks | Specifies the number of consecutive resource blocks of CORESET cluster. Details |
| Component Carrier:Bandwidth Part:CORESET:Precoding Granularity | Specifies the precoding granularity of the CORESET. Details |
| Component Carrier:Bandwidth Part:CORESET:CCE to REG Mapping Type | Specifies the CCE-to-REG mapping type of CORESET. Details |
| Component Carrier:Bandwidth Part:CORESET:REG Bundle Size | Specifies the RBG bundle size of CORESET for interleaved CCE to REG mapping. Details |
| Component Carrier:Bandwidth Part:CORESET:Interleaver Size | Specifies the interleaver size of CORESET for interleaved CCE to REG mapping. Details |
| Component Carrier:Bandwidth Part:CORESET:Shift Index | Specifies the shift index of CORESET for interleaved CCE to REG mapping. Details |
| Component Carrier:Bandwidth Part:CORESET:PDCCH:Number of PDCCH Configurations | Specifies the number of PDCCH Configurations for a CORESET. Details |
| Component Carrier:Bandwidth Part:CORESET:PDCCH:CCE Aggregation level | Specifies the CCE aggregation level of PDCCH. Details |
| Component Carrier:Bandwidth Part:CORESET:PDCCH:CCE Offset | Specifies the PDCCH CCE offset. Details |
| Component Carrier:Bandwidth Part:CORESET:PDCCH:Slot Allocation | Specifies the slot allocation in NR frame. This defines the indices of the allocated slots. Details |
| Component Carrier:SSB:SSB Enabled | Specifies whether synchronization signal block (SSB) is present in the transmitted signal. Details |
| Component Carrier:SSB:Grid Start | Specifies the SSB resource grid start relative to Reference Point A in terms of resource block offset. Details |
| Component Carrier:SSB:Grid Size | Specifies the SSB resource grid size when you set the Grid Size Mode property to Manual. Details |
| Component Carrier:SSB:SSB CRB Offset | Specifies the CRB offset for the SS/PBCH block relative to the reference Point A in units of 15 kHz resource blocks for frequency range 1 or 60 kHz resource blocks for frequency range 2-1 and frequency range 2-2. Details |
| Component Carrier:SSB:Subcarrier Spacing Common | Specifies the basic unit of SSB Subcarrier Offset property for frequency range 2-1 and frequency range 2-2. The property refers to the MIB control element subCarrierSpacingCommon in 3GPP TS 38.331. Details |
| Component Carrier:SSB:SSB Subcarrier Offset | Specifies an additional subcarrier offset for the SS/PBCH block in units of resource blocks of 15 kHz subcarrier spacing given by SSB Subcarrier Common property for frequency range 1, and of 60kHz subcarrier spacing given by SSB Subcarrier Common property for frequency range 2-1 and frequency range 2-2. Details |
| Component Carrier:SSB:SSB Periodicity (s) | Specifies the time difference with which the SS/PBCH block transmit pattern repeats. Details |
| Component Carrier:SSB:SSB Pattern | Specifies the candidate SS/PBCH blocks with different subcarrier spacing configurations as defined in the section 4.1 of 3GPP TS 38.213 specification. In order to configure Case C up to 1.88GHz unpaired spectrum, configure this property to Case C up to 3GHz. Similarly, to configure Case C 1.88GHz to 6GHz unpaired spectrum, configure this property to Case C 3GHz to 6GHz. Details |
| Component Carrier:SSB:SSB Active Blocks | Specifies the SSB burst(s) indices for the SSB pattern that needs to be transmitted. Details |
| Component Carrier:SSB:PSS Power (dB) | Specifies the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. Details |
| Component Carrier:SSB:SSS Power (dB) | Specifies the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. Details |
| Component Carrier:SSB:PBCH Power (dB) | Specifies the power scaling value for the PBCH REs in the SS/PBCH block. This value is expressed in dB. Details |
| Component Carrier:SSB:PBCH DMRS Power (dB) | Specifies the power scaling value for the PBCH DMRS symbols in the SS/PBCH block. This value is expressed in dB. Details |
| Component Carrier:SSB:SSB HRF Index | Specifies the half radio frame in which the SS/PBCH block should be allocated. Details |
| List:Number of Steps | Specifies the number of active steps in the list. Details |
| List:Step:Timer Unit | Specifies the units in which List Step Timer Duration and List Step Timer Offset are specified. Details |
| List:Step:Timer Duration | Specifies the duration of a given list step in units specified by List Step Timer Unit. Details |
| List:Step:Timer Offset | Specifies the offset from the start of the step for which the measurements are computed. The unit for this property is specified by List Step Timer Unit. This property is valid only when you set the Digital Edge Source property to TimerEvent. Details |
| ModAcc:Measurement Enabled | Specifies whether to enable the ModAcc measurement. Details |
| ModAcc:Multicarrier Filter Enabled | Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this property, if number of carriers is set to more than 1 or if you set the Acq BW Optimization Enabled property to False, where in the multi carrier filter will always be used. Details |
| ModAcc:Synchronization Mode | Specifies whether the measurement is performed from slot or frame boundary. Details |
| ModAcc:Measurement Length Unit | Specifies the units in which measurement offset and measurement length are specified. Details |
| ModAcc:Measurement Offset | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the ModAcc Sync Mode property. The unit for this is specified by ModAcc Measurement Length Unit. Details |
| ModAcc:Measurement Length | Specifies the measurement length in units specified by Measurement Length Unit property. Details |
| ModAcc:Frequency Error Estimation | Specifies the operation mode of frequency error estimation. If frequency error is absent in the signal to be analyzed, you may disable frequency estimation to reduce measurement time or to avoid measurement inaccuracy due to error in frequency error estimation. Details |
| ModAcc:Symbol Clock Error Estimation Enabled | Specifies whether to estimate symbol clock error. This property is ignored when the Common Clock Source Enabled property is True and the Frequency Error Estimation property is Disabled, in which case, symbol clock error is not estimated. If symbol clock error is absent in the signal to be analyzed, you may disable symbol clock error estimation to reduce measurement time or to avoid measurement inaccuracy due to error in symbol clock error estimation. Details |
| ModAcc:IQ Impairments:Model | Specifies the I/Q impairments model used by the measurement for estimating I/Q impairments. Details |
| ModAcc:IQ Impairments:IQ Origin Offset Estimation Enabled | Specifies whether to estimate the IQ origin offset. If IQ origin offset is absent in the signal to be analyzed, you may disable IQ origin offset estimation to reduce measurement time or to avoid measurement inaccuracy due to error in IQ origin offset estimation. Details |
| ModAcc:IQ Impairments:IQ Mismatch Estimation Enabled | Specifies whether to estimate the IQ impairments such as IQ gain imbalance and quadrature skew. Details |
| ModAcc:IQ Impairments:IQ Gain Imbalance Correction Enabled | Specifies whether to enable IQ gain imbalance correction. Details |
| ModAcc:IQ Impairments:IQ Quadrature Error Correction Enabled | Specifies whether to enable IQ quadrature error correction. Details |
| ModAcc:IQ Impairments:IQ Timing Skew Correction Enabled | Specifies whether to enable IQ timing skew correction. Details |
| ModAcc:IQ Impairments:IQ Impairments Per Subcarrier Enabled | Specifies whether to return I/Q impairments independently for each subcarrier. Details |
| ModAcc:Magnitude and Phase Error Enabled | Specifies whether to measure the magnitude and the phase error. Details |
| ModAcc:EVM Reference Data Symbols Mode | Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. Details |
| ModAcc:Spectrum Inverted | Specifies whether the spectrum of the signal being measured is inverted. This happens when I and Q component of the baseband complex signal is swapped. Details |
| ModAcc:Channel Estimation Type | Specifies the method used for channel estimation. Details |
| ModAcc:Phase Tracking Mode | Specifies the method used for phase tracking. Details |
| ModAcc:Timing Tracking Mode | Specifies the method used for timing tracking. Details |
| ModAcc:Pre-FFT Error Estimation Interval | Specifies the interval used for Pre-FFT error estimation. Details |
| ModAcc:EVM Unit | Specifies the units of the EVM results. Details |
| ModAcc:FFT Window Type | Specifies the FFT window type used for EVM calculation. Details |
| ModAcc:FFT Window Offset (%CP) | Specifies the position of the FFT window used to calculate the EVM when ModAcc FFT Window Type property is set to Custom. The offset is expressed as a percentage of the cyclic prefix length. If you set this property to 0, the EVM window starts at the end of cyclic prefix. If you set this property to 100, the EVM window starts at the beginning of cyclic prefix. Details |
| ModAcc:FFT Window Length (%CP) | Specifies the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This property is used when you set the ModAcc FFT Window Type property to 3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Details |
| ModAcc:DC Subcarrier Removal Enabled | Specifies whether the DC subcarrier is removed from the EVM results. Details |
| ModAcc:Common Clock Source Enabled | Specifies whether same reference clock is used for local oscillator and digital-to-analog converter. When same reference clock is used the Carrier Frequency Offset is proportional to Sample Clock Error. Details |
| ModAcc:Spectral Flatness Condition | Specifies the test condition for Spectral Flatness measurement. Details |
| ModAcc:Noise Compensation:Enabled | Specifies whether the contribution of the instrument noise is compensated for EVM computation. You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use. Details |
| ModAcc:Noise Compensation:Input Power Check Enabled | Specifies whether the measurement checks if any high power signal is present at the RFIn port of the instrument while performing noise floor calibration. Details |
| ModAcc:Noise Compensation:Reference Level Coercion Limit (dB) | Specifies the coercion limit for the reference level for noise compensation. When you set ModAcc Meas Mode property to Measure and ModAcc Noise Comp Enabled property to True, the measurement attempts to read noise floor calibration data corresponding to the configured reference level. Details |
| ModAcc:Measurement Mode | Specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. Details |
| ModAcc:Composite Results:Include DMRS | Specifies whether the DMRS resource elements are included for composite EVM and magnitude and phase error results and traces. Details |
| ModAcc:Composite Results:Include PTRS | Specifies whether the PTRS resource elements are included for composite EVM and magnitude and phase error results and traces. Details |
| ModAcc:Averaging:Enabled | Enables averaging for the measurement. Details |
| ModAcc:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ModAcc Averaging Enabled property to True. Details |
| ModAcc:Auto Level:Allow Overflow | Specifies whether the RFmxNR ModAcc Auto Level VI should search for the optimum reference levels while allowing ADC overflow. Details |
| ModAcc:Short Frame:Enabled | Specifies whether the input signal has a periodicity shorter than the NR frame duration. Details |
| ModAcc:Short Frame:Length | Specifies the short frame periodicity in unit specified by Short Frame Length Unit. Details |
| ModAcc:Short Frame:Length Unit | Specifies the units in which Short Frame Length is specified. Details |
| ModAcc:Transient:Transient Period EVM Mode | Configures the EVM measurement behavior for symbols affected by power transients. Details |
| ModAcc:Transient:Transient Period | It configures the transient duration as specified in section 6.4.2.1a of 3GPP 38.101-1 specification. Details |
| ModAcc:Transient:Power Change Threshold (dB) | Specifies transient period power change threshold level in dB. Details |
| ModAcc:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. Details |
| ModAcc:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. Details |
| ModAcc:Results:Detected Cell ID | Returns the detected Cell ID, if the Auto Cell ID Detection Enabled property is set to True. A value of -1 is returned, if the measurement fails to auto detect the Cell ID. Returns the user configured Cell ID, if the Auto Cell ID Detection Enabled property is set to False. Details |
| ModAcc:Results:Composite RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length. Note If ModAcc Composite Results Include DMRS property and ModAcc Composite Results Include PTRS property are set to False, EVM is computed only for the shared channel. Details |
|  | Note If ModAcc Composite Results Include DMRS property and ModAcc Composite Results Include PTRS property are set to False, EVM is computed only for the shared channel. |
| ModAcc:Results:Composite Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length. Note If ModAcc Composite Results Include DMRS property and ModAcc Composite Results Include PTRS property are set to False, EVM is computed only for the shared channel. Details |
|  | Note If ModAcc Composite Results Include DMRS property and ModAcc Composite Results Include PTRS property are set to False, EVM is computed only for the shared channel. |
| ModAcc:Results:Composite Peak EVM Bandwidth Part Index | Returns the bandwidth part index where ModAcc Results Max Pk Composite EVM occurs. Details |
| ModAcc:Results:Composite Peak EVM Slot Index | Returns the slot index where ModAcc Results Max Pk Composite EVM occurs. Details |
| ModAcc:Results:Composite Peak EVM Symbol Index | Returns the symbol index where ModAcc Results Max Pk Composite EVM occurs. Details |
| ModAcc:Results:Composite Peak EVM Subcarrier Index | Returns the subcarrier index where ModAcc Results Max Pk Composite EVM occurs. Details |
| ModAcc:Results:Composite RMS Magnitude Error Mean (% or dB) | Returns the RMS mean value of magnitude error calculated over measurement length on all configured channels. Details |
| ModAcc:Results:Composite Peak Magnitude Error Maximum (% or dB) | Returns the peak value of magnitude error calculated over measurement length on all configured channels. Details |
| ModAcc:Results:Composite RMS Phase Error Mean (deg) | Returns the RMS mean value of Phase error calculated over measurement length on all configured channels. This value is expressed in degrees. Details |
| ModAcc:Results:Composite Peak Phase Error Maximum (deg) | Returns the peak value of Phase error calculated over measurement length on all configured channels. This value is expressed in degrees. Details |
| ModAcc:Results:SCH Symbol Power Mean (dBm) | Returns the mean value (over ModAcc Meas Length) of power calculated on OFDM symbols allocated only with the shared channel. Details |
| ModAcc:Results:SCH Detected Modulation Type | Returns the modulation of the shared channel user data if you set the Auto RB Detection Enabled property to True; otherwise, returns the configured modulation of the shared user data. In case of downlink test model, the modulation type specified by the 3GPP standard is returned. Details |
| ModAcc:Results:PUSCH:PUSCH Data RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH data symbols. Details |
| ModAcc:Results:PUSCH:PUSCH Data Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH data symbols. Details |
| ModAcc:Results:PUSCH:PUSCH DMRS RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH DMRS. Details |
| ModAcc:Results:PUSCH:PUSCH DMRS Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH DMRS. Details |
| ModAcc:Results:PUSCH:PUSCH PTRS RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on PUSCH PTRS. Details |
| ModAcc:Results:PUSCH:PUSCH PTRS Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PUSCH PTRS. Details |
| ModAcc:Results:PUSCH:PUSCH Data RE Power Mean (dBm) | Returns the mean value (over Meas Length) of power calculated on PUSCH data REs. Details |
| ModAcc:Results:PUSCH:PUSCH DMRS RE Power Mean (dBm) | Returns the mean value (over Meas Length) of power calculated on PUSCH DMRS REs. Details |
| ModAcc:Results:PUSCH:PUSCH PTRS RE Power Mean (dBm) | Returns the mean value (over Meas Length) of power calculated on PUSCH PTRS REs. Details |
| ModAcc:Results:PUSCH:PUSCH Data Transient RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calulated over measurement interval for the PUSCH symbols where the transient occurs. Details |
| ModAcc:Results:PUSCH:Peak Phase Offset Maximum (deg) | Returns the maximum value over Meas Length of peak phase offsets between the reference and measurement slots. Details |
| ModAcc:Results:PUSCH:Peak Phase Offset Slot Index | Returns the slot index where ModAcc Results PUSCH Pk Phase Offset Max occurs. Details |
| ModAcc:Results:PDSCH:PDSCH QPSK RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on all QPSK modulated PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH 16 QAM RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on all 16 QAM modulated PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH 64 QAM RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on all 64 QAM modulated PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH 256 QAM RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on all 256 QAM modulated PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH 1024 QAM RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on all 1024 QAM modulated PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH 8 PSK RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on all 8 PSK modulated PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH Data RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH Data Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PDSCH data symbols. Details |
| ModAcc:Results:PDSCH:PDSCH DMRS RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on PDSCH DMRS. Details |
| ModAcc:Results:PDSCH:PDSCH DMRS Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PDSCH DMRS. Details |
| ModAcc:Results:PDSCH:PDSCH PTRS RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs calculated over measurement length on PDSCH PTRS. Details |
| ModAcc:Results:PDSCH:PDSCH PTRS Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PDSCH PTRS. Details |
| ModAcc:Results:PDSCH:PDSCH Data RE Power Mean (dBm) | Returns the mean value (over Meas Length) of power calculated on PDSCH data REs. Details |
| ModAcc:Results:PDSCH:PDSCH DMRS RE Power Mean (dBm) | Returns the mean value (over Meas Length) of power calculated on PDSCH DMRS REs. Details |
| ModAcc:Results:PDSCH:PDSCH PTRS RE Power Mean (dBm) | Returns the mean value (over Meas Length) of power calculated on PDSCH PTRS REs. Details |
| ModAcc:Results:SSB:PSS RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs computed over measurement length on PSS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:PSS Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on PSS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:SSS RMS EVM Mean (% or dB) | Returns the mean value of RMS EVMs computed over measurement length on SSS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:SSS Peak EVM Maximum (% or dB) | Returns the maximum value of peak EVMs calculated over measurement length on SSS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:PBCH Data RMS EVM Mean (% or dB) | Returns the mean value calculated over measurement length of RMS EVMs calculated on PBCH data symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:PBCH Data Peak EVM Maximum (% or dB) | Returns the maximum value calculated over measurement length of peak EVMs calculated on PBCH data symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:PBCH DMRS RMS EVM Mean (% or dB) | Returns the mean value calculated over measurement length of RMS EVMs calculated on PBCH DMRS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:SSB:PBCH DMRS Peak EVM Maximum (% or dB) | Returns the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this result in dB. Details |
| ModAcc:Results:In-Band Emission Margin (dB) | Returns In-Band Emission Margin of the component carrier. This value is expressed in dB. Details |
| ModAcc:Results:Subblock In-Band Emission Margin (dB) | Returns In-Band Emission Margin of the subblock's aggregated bandwidth. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Margin Slot Index | Returns the slot index with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2. Details |
| ModAcc:Results:Spectral Flatness:Range1-Max to Range1-Min (dB) | Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range1 for the measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range2-Max to Range2-Min (dB) | Returns the peak-to-peak ripple of the magnitude of EVM equalizer coefficients within Range2 for the Measurement unit, that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range1-Max to Range2-Min (dB) | Returns the peak-to-peak ripple of the EVM equalizer coefficients from maximum in Range1 to minimum in Range2 for the Measurement unit that has the worst ripple margin among all four ripple results defined in 3section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range2-Max to Range1-Min (dB) | Returns the peak-to-peak ripple of the EVM equalizer coefficients from maximum in Range2 to minimum in Range1 for the Measurement unit that has the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range1-Max (dB) | Returns the maximum magnitude of the EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range1-Min (dB) | Returns the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range2-Max (dB) | Returns the maximum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range2-Min (dB) | Returns the minimum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range1-Max Subcarrier Index | Returns the maximum subcarrier index magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. Details |
| ModAcc:Results:Spectral Flatness:Range1-Min Subcarrier Index | Returns the minimum subcarrier index magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. Details |
| ModAcc:Results:Spectral Flatness:Range2-Max Subcarrier Index | Returns the maximum subcarrier index magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. Details |
| ModAcc:Results:Spectral Flatness:Range2-Min Subcarrier Index | Returns the minimum subcarrier index magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. Details |
| ModAcc:Results:Component Carrier Time Offset Mean (s) | Returns the time difference between the detected slot or frame boundary depending on the sync mode and reference trigger location. This value is expressed in seconds. Details |
| ModAcc:Results:Component Carrier Frequency Error Mean (Hz) | Returns the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. Details |
| ModAcc:Results:Component Carrier Slot Frequency Error Maximum (Hz) | Returns the estimated maximum per slot carrier frequency offset over the Measurement Length. Details |
| ModAcc:Results:Component Carrier Symbol Clock Error Mean (ppm) | Returns the estimated sample clock error averaged over measurement length. This value is expressed in ppm. Details |
| ModAcc:Results:Component Carrier IQ Origin Offset Mean (dBc) | Returns the estimated IQ origin offset averaged over measurement length. This value is expressed in dBc. Details |
| ModAcc:Results:Component Carrier Slot IQ Origin Offset Maximum (dBc) | Returns the estimated maximum per slot carrier IQ origin offset over the Measurement Length Details |
| ModAcc:Results:Component Carrier IQ Gain Imbalance Mean (dB) | Returns the estimated IQ gain imbalance averaged over measurement length. This value is expressed in dB. IQ gain imbalance is the ratio of the amplitude of the I component to the Q component of the IQ signal being measured. Details |
| ModAcc:Results:Component Carrier Quadrature Error Mean (deg) | Returns the estimated quadrature error averaged over measurement length. This value is expressed in degrees. Quadrature error is the measure of skewness in degree of the I component with respect to the Q component of the IQ signal being measured. Details |
| ModAcc:Results:Component Carrier IQ Timing Skew Mean (s) | Returns the estimated IQ Timing Skew averaged over Meas Length. Details |
| ModAcc:Results:Subblock LO Component Carrier Index | Returns the index of the component carrier that includes the LO of the transmitter according to the Subblock Freq (Hz) and Subblock TX LO Freq properties. If the LO of the transmitter doesn't fall into any component carrier of the subblock, the property returns -1. This result is valid only when you set the Transmitter Architecture property to LO per Subblock. Details |
| ModAcc:Results:Subblock LO Subcarrier Index | Returns the subcarrier index within the respective component carrier where the transmitter LO is located. Due to its dependence on Subblock Freq (Hz) and Subblock TX LO Freq properties, the value can be fractional, and the LO might reside in between subcarriers of a component carrier. This result is valid only when you set the Transmitter Architecture property to LO per Subblock. Details |
| ModAcc:Results:Subblock IQ Origin Offset Mean (dBc) | Returns the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the Transmitter Architecture property to LO per Subblock. Details |
| ModAcc:Results:Noise Compensation Applied | Specifies whether the noise compensation is applied to the EVM measurement. Details |
| ACP:Measurement Enabled | Specifies whether to enable the ACP measurement. Details |
| ACP:Channel Configuration Type | Specifies the method to configure the carrier and the offset channel settings. Details |
| ACP:Subblock Integration Bandwidth (Hz) | Specifies the integration bandwidth of a subblock. This value is expressed in Hz. Details |
| ACP:Subblock Offset (Hz) | Specifies the offset of the subblock measurement relative to the subblock center. This value is expressed in Hz. Details |
| ACP:Component Carrier:Integration Bandwidth (Hz) | Specifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz. Details |
| ACP:Offset:Number of UTRA Offsets | Specifies the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions. For uplink ACP measurement in frequency range 2-1 and frequency range 2-2, and for downlink ACP measurement, the ACP Num UTRA Offsets has to be 0. Details |
| ACP:Offset:Number of EUTRA Offsets | Specifies the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions. For uplink ACP measurement, and for downlink ACP measurement in frequency range 2-1 and frequency range 2-2, this property has to be 0. Details |
| ACP:Offset:Number of NR Offsets | Specifies the number of NR adjacent channel offsets to be configured at offset positions. Details |
| ACP:Offset:Number of ENDC Offsets | Specifies the number of ENDC adjacent channel offsets to be configured at offset positions. Details |
| ACP:Offset:Channel Spacing Adjustment (Hz) | Specifies the additional spacing of ACP offset channels at nominal spacing. Details |
| ACP:Offset:Number of Offsets | Specifies the number of configured offset channels. Details |
| ACP:Offset:Frequency (Hz) | Specifies the offset frequency of an offset channel. This value is expressed in Hz. The offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel. Details |
| ACP:Offset: Sideband | Specifies the sideband measured for the offset channel. Details |
| ACP:Offset:Integration Bandwidth (Hz) | Specifies the integration bandwidth of an offset channel. This value is expressed in Hz. Details |
| ACP:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| ACP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the ACP RBW Auto property to False. This value is expressed in Hz. Details |
| ACP:RBW Filter:Type | Specifies the shape of the RBW filter. Details |
| ACP:Sweep Time:Auto | Specifies whether the measurement sets the sweep time. Details |
| ACP:Sweep Time:Interval (s) | Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| ACP:Power Units | Specifies the unit for absolute power. Details |
| ACP:Measurement Method | Specifies the method for performing the ACP measurement. Details |
| ACP:Noise Calibration:Mode | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:Noise Calibration:Averaging:Auto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. Details |
| ACP:Noise Calibration:Averaging:Count | Specifies the averaging count used for noise calibration when you set the ACP Noise Cal Averaging Auto property to False. Details |
| ACP:Noise Compensation:Enabled | Specifies whether RFmx compensates for the instrument noise when performing the measurement when you set ACP Noise Cal Mode property to Auto, or when you set ACP Noise Cal Mode to Manual and ACP Meas Mode property to Measure Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:Noise Compensation:Type | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:Averaging:Enabled | Specifies whether to enable averaging for the ACP measurement. Details |
| ACP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True. Details |
| ACP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. Details |
| ACP:Measurement Mode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:FFT:Window | Specifies the FFT window type to be used to reduce spectral leakage. Details |
| ACP:FFT:Overlap Mode | Specifies the overlap mode when you set the ACP Meas Method property to Sequential FFT. In the Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. The FFT is then computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. Details |
| ACP:FFT:Overlap (%) | Specifies the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property when you set the ACP Meas Method property to Sequential FFT and the ACP FFT Overlap Mode property to User Defined. This value is expressed as a percentage. Details |
| ACP:Advanced:IF Output Power Offset Auto | Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This property is applicable only when you set the ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Near IF Output Power Offset (dB) | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is applicable only when you set the ACP IF Output Pwr Offset Auto property to False and ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Far IF Output Power Offset (dB) | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is applicable only when you set the ACP IF Output Pwr Offset Auto property to False and ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Sequential FFT Size | Specifies the number of bins to be used for FFT computation, when you set the ACP Meas Method property to Sequential FFT. Details |
| ACP:Amplitude Correction Type | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| ACP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. Details |
| ACP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the ACP measurement. Details |
| ACP:Results:Total Aggregated Power (dBm or dBm/Hz) | Returns the total power of all the subblocks. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. Details |
| ACP:Results:Subblock Power (dBm or dBm/Hz) | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Component Carrier:Absolute Power (dBm or dBm/Hz) | Returns the power measured over the integration bandwidth of the component carrier. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Component Carrier:Relative Power (dB) | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Details |
| ACP:Results:Lower Offset:Absolute Power (dBm or dBm/Hz) | Returns the lower (negative) offset channel power. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Lower Offset:Relative Power (dB) | Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. Details |
| ACP:Results:Upper Offset:Absolute Power (dBm or dBm/Hz) | Returns the upper (positive) offset channel power. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Upper Offset:Relative Power (dB) | Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. Details |
| CHP:Measurement Enabled | Specifies whether to enable the channel power measurement. Details |
| CHP:Sweep Time:Auto | Specifies whether the measurement sets the sweep time. Details |
| CHP:Sweep Time:Interval (s) | Specifies the sweep time when you set the CHP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| CHP:Integration Bandwidth Type | Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. Details |
| CHP:Subblock Integration Bandwidth (Hz) | Specifies the integration bandwidth of the subblock. This value is expressed in Hz. It is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock. Details |
| CHP:Component Carrier:Integration Bandwidth (Hz) | Specifies the integration bandwidth of a component carrier (CC). This value is expressed in Hz. Details |
| CHP:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| CHP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the CHP RBW Auto property to False. This value is expressed in Hz. Details |
| CHP:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| CHP:Noise Calibration:Mode | Specifies whether the noise calibration and measurement is performed manually by the user or automatically by RFmx. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Noise Calibration:Averaging:Auto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. Details |
| CHP:Noise Calibration:Averaging:Count | Specifies the averaging count used for noise calibration when you set the CHP Noise Cal Averaging Auto property to False. Details |
| CHP:Noise Compensation:Enabled | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the CHP Noise Cal Mode property to Auto, or set the CHP Noise Cal Mode property to Manual and the CHP Meas Mode property to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Noise Compensation:Type | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Averaging:Enabled | Specifies whether to enable averaging for the CHP measurement. Details |
| CHP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. Details |
| CHP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. Details |
| CHP:Measurement Mode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:FFT:Window | Specifies the FFT window type to be used to reduce spectral leakage. Details |
| CHP:Amplitude Correction Type | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| CHP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. Details |
| CHP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| CHP:Results:Total Aggregated Power (dBm) | Returns the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. Details |
| CHP:Results:Subblock Power (dBm) | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Details |
| CHP:Results:Component Carrier:Absolute Power (dBm) | Returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Details |
| CHP:Results:Component Carrier:Relative Power (dB) | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Details |
| OBW:Measurement Enabled | Specifies whether to enable the OBW measurement. Details |
| OBW:Span:Auto | Specifies whether the frequency range of the spectrum used for the OBW measurement is auto computed or configured by the user. Details |
| OBW:Span:Span (Hz) | Specifies the frequency range around the subblock center frequency, which is used to find the Subblock Occupied Bandwidth. When OBW Span Auto is set to False, the configured span value is used by the measurement. This value is expressed in Hz. Details |
| OBW:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| OBW:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the OBW RBW Auto property to False. This value is expressed in Hz. Details |
| OBW:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| OBW:Sweep Time:Auto | Specifies whether the measurement sets the sweep time. Details |
| OBW:Sweep Time:Interval (s) | Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. Details |
| OBW:Averaging:Enabled | Specifies whether to enable averaging for the OBW measurement. Details |
| OBW:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. Details |
| OBW:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. Details |
| OBW:FFT:Window | Specifies the FFT window type to be used to reduce spectral leakage. Details |
| OBW:Amplitude Correction Type | Specifies whether the amplitude of frequency bins in the spectrum used by the measurement is corrected for external attenuation at RF center frequency or corrected for external attenuation at individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| OBW:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. Details |
| OBW:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| OBW:Results:Subblock:Occupied Bandwidth (Hz) | Returns the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Details |
| OBW:Results:Subblock:Absolute Power (dBm) | Returns the total power measured in the spectrum acquired by the measurement. This value is expressed in dBm. Details |
| OBW:Results:Subblock:Start Frequency (Hz) | Returns the start frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Details |
| OBW:Results:Subblock:Stop Frequency (Hz) | Returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Details |
| SEM:Measurement Enabled | Specifies whether to enable the SEM measurement. Details |
| SEM:Uplink Mask Type | Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. Details |
| SEM:Downlink Mask Type | Specifies the limits to be used in the measurement for Downlink. Details |
| SEM:Delta F_Maximum (Hz) | Specifies the stop frequency for 3rd offset segment to be used in the measurement. This property is valid only for downlink and when you set the SEM DL Mask Type property to Standard. Details |
| SEM:Subblock Integration Bandwidth (Hz) | Returns the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Details |
| SEM:Subblock Aggregated Channel Bandwidth (Hz) | Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. Details |
| SEM:Component Carrier:Integration Bandwidth (Hz) | Returns the integration bandwidth of a component carrier. This value is expressed in Hz. Details |
| SEM:Component Carrier:Rated Output Power (dBm) | Specifies the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, FR2 Category A and FR2 Category B, and also for NTN supported masks. This value is expressed in dBm. Details |
| SEM:Offset:Number of Offsets | Specifies the number of SEM offset segments. Details |
| SEM:Offset:Start Frequency (Hz) | Details |
| SEM:Offset:Stop Frequency (Hz) | Details |
| SEM:Offset:Sideband | Specifies whether the offset segment is present either on one side or on both sides of a carrier. Details |
| SEM:Offset:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the resolution bandwidth (RBW) filter used to sweep the acquired offset segment, when you set the SEM Offset RBW Auto property to False. This value is expressed in Hz. Details |
| SEM:Offset:RBW Filter:Type | Specifies the shape of a digital RBW filter. Details |
| SEM:Offset:Bandwidth Integral | Specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. Details |
| SEM:Offset:Limit Fail Mask | Specifies the criteria to determine the measurement fail status. Details |
| SEM:Offset:Frequency Definition | Specifies the definition of the the start frequency and stop frequency of the offset segments. Details |
| SEM:Offset:Absolute Limit:Start (dBm) | Specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. Details |
| SEM:Offset:Absolute Limit:Stop (dBm) | Specifies the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. Details |
| SEM:Offset:Relative Limit:Start (dB) | Specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. Details |
| SEM:Offset:Relative Limit:Stop (dB) | Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. Details |
| SEM:Sweep Time:Auto | Specifies whether the measurement sets the sweep time. Details |
| SEM:Sweep Time:Interval (s) | Specifies the sweep time when you set the SEM Sweep Time Auto property to False. This value is expressed in seconds. Details |
| SEM:Averaging:Enabled | Specifies whether to enable averaging for the SEM measurement. Details |
| SEM:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True. Details |
| SEM:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. Details |
| SEM:FFT:Window | Specifies the FFT window type to be used to reduce spectral leakage. Details |
| SEM:Amplitude Correction Type | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| SEM:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. Details |
| SEM:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| SEM:Results:Total Aggregated Power (dBm) | Returns the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. Details |
| SEM:Results:Measurement Status | Returns the overall measurement status based on the standard mask type that you configure in the SEM UL Mask Type property. Details |
| SEM:Results:Subblock Power (dBm) | Returns the power measured over the SEM CC IBW property. This value is expressed in dBm. Details |
| SEM:Results:Component Carrier:Absolute Integrated Power (dBm) | Returns the power measured over the SEM CC IBW property. This value is expressed in dBm. Details |
| SEM:Results:Component Carrier:Relative Integrated Power (dB) | Returns the component carrier power relative to SEM Results Subblock Pwr. This value is expressed in dB. Details |
| SEM:Results:Component Carrier:Absolute Peak Power (dBm) | Returns the peak power in the component carrier. This value is expressed in dBm. Details |
| SEM:Results:Component Carrier:Peak Frequency (Hz) | Returns the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. Details |
| SEM:Results:Lower Offset:Measurement Status | Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM UL Mask Type property. Details |
| SEM:Results:Lower Offset:Absolute Integrated Power (dBm) | Returns the lower (negative) offset segment power. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Relative Integrated Power (dB) | Returns the power in the lower (negative) offset segment relative to SEM Results Total Aggregated Pwr property. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Absolute Peak Power (dBm) | Returns the peak power in the lower (negative) offset segment. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Relative Peak Power (dB) | Returns the peak power in the lower (negative) offset segment relative to SEM Results Total Aggregated Pwr property. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz. Details |
| SEM:Results:Lower Offset:Margin (dB) | Returns the margin from the absolute limit mask for lower (negative) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Margin Absolute Power (dBm) | Returns the power at which the Margin occurs in the lower (negative) offset segment. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Margin Relative Power (dB) | Returns the power at which the Margin occurs in the lower (negative) offset segment relative to SEM Results Total Aggregated Pwr property. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Margin Frequency (Hz) | Returns the frequency at which the Margin occurs in the lower (negative) offset. This value is expressed in Hz. Details |
| SEM:Results:Upper Offset:Measurement Status | Returns the measurement status based on the user-configured standard measurement limits. Spectrum emission limits can be defined by setting SEM UL Mask Type property. Details |
| SEM:Results:Upper Offset:Absolute Integrated Power (dBm) | Returns the upper (positive) offset segment power. This value is expressed in dBm. Details |
| SEM:Results:Upper Offset:Relative Integrated Power (dB) | Returns the power in the upper (positive) offset segment relative to SEM Results Total Aggregated Pwr property. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Absolute Peak Power (dBm) | Returns the peak power in the upper (positive) offset segment. This value is expressed in dBm. Details |
| SEM:Results:Upper Offset:Relative Peak Power (dB) | Returns the peak power in the upper (positive) offset segment relative to SEM Results Total Aggregated Pwr property. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. Details |
| SEM:Results:Upper Offset:Margin (dB) | Returns the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Margin Absolute Power (dBm) | Returns the power at which the Margin occurs in the upper (positive) offset segment. This value is expressed in dBm. Details |
| SEM:Results:Upper Offset:Margin Relative Power (dB) | Returns the power at which the Margin occurs in the upper (positive) offset segment relative to SEM Results Total Aggregated Pwr property. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Margin Frequency (Hz) | Returns the frequency at which the Margin occurs in the upper (positive) offset. This value is expressed in Hz. Details |
| TXP:Enabled | Specifies whether to enable the TXP measurement. Details |
| TXP:Measurement Offset | Specifies the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. Details |
| TXP:Measurement Interval | Specifies the measurement interval. This value is expressed in seconds. Details |
| TXP:Averaging:Enabled | Specifies whether to enable averaging for TXP measurement. Details |
| TXP:Averaging:Count | Specifies the number of acquisitions used for averaging when Averaging Enabled is True. Details |
| TXP:All Traces Enabled | Enables the traces to be stored and retrieved after the TXP measurement is performed. Details |
| TXP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism inside TXP measurement. Details |
| TXP:Results:Average Power Mean (dBm) | Returns the average power of the acquired signal. Details |
| TXP:Results:Peak Power Maximum (dBm) | Returns the peak power of the acquired signal. Details |
| PVT:Measurement Enabled | Specifies whether to enable the PVT measurement. Details |
| PVT:Measurement Interval Auto | Specifies whether the measurement interval is computed by the measurement or configured by the user through Measurement Interval property. Details |
| PVT:Measurement Interval (s) | Specifies the measurement interval when the Measurement Interval Auto property is set to False. This value is expressed in seconds. Details |
| PVT:Measurement Method | Specifies the PVT measurement method. Details |
| PVT:Averaging:Enabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. Details |
| PVT:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the PVT Averaging Enabled property to True. Details |
| PVT:Averaging:Type | Specifies the measurement averaging type. Details |
| PVT:OFF Power Exclusion Before (s) | Specifies the time excluded from the OFF region before the burst and at the beginning for uplink and downlink, respectively. The value is expressed in seconds. Details |
| PVT:OFF Power Exclusion After (s) | Specifies the time excluded from the OFF region after the burst and at the end for uplink and downlink, respectively. The value is expressed in seconds. Details |
| PVT:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. Details |
| PVT:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism inside the PVT measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| PVT:Results:Measurement Status | Returns the measurement status indicating whether the off power before and after is within the standard defined limit. Details |
| PVT:Results:Absolute OFF Power Before (dBm) | Returns the OFF power in the segment before the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. Details |
| PVT:Results:Absolute OFF Power After (dBm) | Returns the OFF power in the segment after the captured burst for the uplink direction, while it returns NaN in the segment after the captured burst for the downlink direction. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. Details |
| PVT:Results:Absolute ON Power (dBm) | Returns the average ON power within the measurement interval. This value is expressed in dBm. Details |
| PVT:Results:Burst Width (s) | Returns the width of the captured burst for the uplink direction, while it returns NaN of the captured burst for the downlink direction. This value is expressed in seconds. Details |
| PVT:Results:Peak Windowed OFF Power (dBm/MHz) | Returns the NaN for the uplink direction, while it returns the peak power value of 70/N us windowed power during all OFF regions in the measurement interval. This value is expressed in dBm/MHz. Details |
| PVT:Results:Peak Windowed OFF Power Margin (dB) | Returns the NaN for the uplink direction, while it returns the PVT Results Pk Windowed OFF Pwr to the 3GPP limit. This value is expressed in dB. Details |
| PVT:Results:Peak Windowed OFF Power Time (s) | Returns the NaN for the uplink direction, while it returns the time offset of the PVT Results Pk Windowed OFF Pwr. This value is expressed in seconds. Details |
| Advanced:Acquisition Bandwidth Optimization Enabled | Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. Details |
| Advanced:Transmitter Architecture | Specifies the RF architecture at the transmitter, whether each component carriers have a separate LO or one common LO for the entire subblock. Details |
| Advanced:Phase Compensation | Specifies whether phase compensation is disabled, auto-set by the measurement or set by the you. Details |
| Advanced:Reference Grid Alignment Mode | Specifies whether to align the bandwidthparts and the SSB in a component carrier to a reference resource grid automatically or manually. Details |
| Advanced:Grid Size Mode | Specifies whether to set the grid size of all BWPs and SSB in a component carrier automatically or manually. Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. Details |
| Result Fetch Timeout (s) | Specifies the time to wait before results are available in the RFmxNR Property Node. This value is expressed in seconds. Details |
