# NI DOCUMENT BUNDLE: rfmx-wlan-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-wlan-prop start=1 end=116 -->
<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00002.html language=enus -->
## TOPIC 00001: Reference Level Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00002.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the reference level which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. On a MIMO session, use port::<deviceName>/<channelNumber> as a selector string to configure or read this property per port. If you do not specify port string, this property is configured for all ports. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0000f.html language=enus -->
## TOPIC 00002: OFDM:Number of Frequency Segments Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0000f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0000f.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Number of Frequency Segments Property

**Short Name:**Num Freq Segments

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the number of frequency segments for 802.11ac and 802.11ax signals.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

Valid values are 1 and 2.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00010.html language=enus -->
## TOPIC 00003: OFDM:Number of Receive Chains Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00010.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Number of Receive Chains Property

**Short Name:**Num Rx Chains

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the number of receive chains for OFDM standards.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

The valid values are as follows.

| Standard | Number of Receive Chains |
| --- | --- |
| 802.11a/g, 802.11j, 802.11p | 1 |
| 802.11n | 1–4 |
| 802.11ac, 802.11ax, 802.11be | 1–8 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00017.html language=enus -->
## TOPIC 00004: OFDM:Advanced:PPDU Type Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00017.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:PPDU Type Property

**Short Name:**OFDM PPDU Type

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the PPDU type when you set the [OFDM Auto PPDU Type Detection Enabled](attra00027.html)
 property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Non-HT**.

| Non-HT (0) | Specifies an 802.11a, 802.11j, or 802.11p PPDU type, or 802.11n, 802.11ac, or 802.11ax PPDU type when operating in the Non-HT mode. |
| --- | --- |
| Mixed (1) | Specifies the HT-Mixed PPDU (802.11n) type. |
| Greenfield (2) | Specifies the HT-Greenfield PPDU (802.11n) type. |
| SU (3) | Specifies the VHT SU PPDU type if you set the Standard property to 802.11ac or the HE SU PPDU type if you set the Standard property to 802.11ax. |
| MU (4) | Specifies the VHT MU PPDU type if you set the Standard property to 802.11ac, the HE MU PPDU type if you set the Standard property to 802.11ax, or the EHT MU PPDU type if you set the Standard property to 802.11be. |
| Extended Range SU (5) | Specifies the HE Extended Range SU PPDU (802.11ax) type. |
| Trigger-based (6) | Specifies the HE TB PPDU if you set the Standard property to 802.11ax or the EHT TB PPDU if you set the Standard property to 802.11be. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0001b.html language=enus -->
## TOPIC 00005: OFDM:Advanced:RU Offset/MRU Index Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0001b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0001b.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:RU Offset/MRU Index Property

**Short Name:**OFDM RU Offset/MRU Index

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the location of RU or MRU for a user. If an RU is configured, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is configured, the MRU Index is as defined in the Table 36-8 to Table 36-15 of
 *IEEE P802.11be/D5.0.1*.

This property is applicable for 802.11ax MU and TB PPDU, and 802.11be MU and TB PPDU signals. For 802.11ax TB PPDU and 802.11be TB PPDU, you must always configure this property. For 802.11ax MU PPDU and 802.11be MU PPDU, you must configure this property if [OFDM Header Decoding Enabled](attra00028.html) is set to **False**.

Use "user<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property for 802.11ax MU PPDU, 802.11ax TB PPDU, 802.11be MU PPDU, and 802.11be TB PPDU.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00024.html language=enus -->
## TOPIC 00006: Advanced:Auto Level Initial Reference Level (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00024.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Auto Level Initial Reference Level (dBm) Property

**Short Name:**Auto Level Initial Ref Level (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the initial reference level which the [RFmxWLAN Auto Level](/csh?topicname=rfmxwlanvi/rfmxwlan_auto_level.html) VI uses to estimate the peak power of the input signal. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 30.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00029.html language=enus -->
## TOPIC 00007: OFDM:Advanced:MU-MIMO LTF Mode Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00029.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:MU-MIMO LTF Mode Enabled Property

**Short Name:**OFDM MU-MIMO LTF Mode Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the LTF sequence corresponding to each space-time stream is masked by a distinct orthogonal code.

This property is valid for 802.11ax TB PPDU only.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Specifies that the LTF sequence uses single stream pilots. |
| --- | --- |
| True (1) | Specifies that the LTF sequence is HE masked. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00031.html language=enus -->
## TOPIC 00008: OFDM:Advanced:PE Disambiguity Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00031.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:PE Disambiguity Property

**Short Name:**OFDM PE Disambiguity

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the packet extension disambiguity information.

This property is applicable only for 802.11ax TB PPDU and 802.11be TB PPDU.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00033.html language=enus -->
## TOPIC 00009: OFDM:Advanced:Pre-FEC Padding Factor Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00033.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:Pre-FEC Padding Factor Property

**Short Name:**OFDM Pre-FEC Padding Factor

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the pre-FEC padding factor used in 802.11ax TB PPDU and 802.11be TB PPDU for decoding PLCP service data unit (PSDU) bits.

The valid values are 1 to 4, inclusive.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00034.html language=enus -->
## TOPIC 00010: OFDM:Advanced:LDPC Extra Symbol Segment Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00034.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:LDPC Extra Symbol Segment Property

**Short Name:**OFDM LDPC Extra Symbol Segment

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the presence of an extra OFDM symbol segment for LDPC in the 802.11ax TB PPDU and 802.11be TB PPDU.

This value is used for decoding PLCP service data unit (PSDU) bits. The valid values are 0 and 1.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00035.html language=enus -->
## TOPIC 00011: OFDM:Advanced:STBC Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00035.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDM:Advanced:STBC Enabled Property

**Short Name:**OFDM STBC Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether space-time block coding is enabled. This property is applicable only for 802.11ax TB PPDU.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Specifies that space-time block coding is disabled. |
| --- | --- |
| True (1) | Specifies that space-time block coding is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00036.html language=enus -->
## TOPIC 00012: Advanced: Sample Clock Rate Factor Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00036.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

Advanced: Sample Clock Rate Factor Property

**Short Name:**Sample Clock Rate Factor

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the factor by which the sample clock rate is multiplied at the transmitter to generate a signal compressed in the frequency domain and expanded in the time domain.

For example, a 40 MHz signal can be compressed to 20 MHz in the frequency domain if the sample clock rate is reduced to half at the transmitter. In this case, you must set this property to 0.5 to demodulate the signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

The valid values are 0.001 to 1, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra00fff.html language=enus -->
## TOPIC 00013: Trigger:IQ Power Edge:Level Type Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra00fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra00fff.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level Type Property

**Short Name:**IQ Power Edge Level Type

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the reference for the [IQ Power Edge Level](attra00008.html) property. The IQ Power Edge Level Type property is used only when you set the [Trigger Type](attra00004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Relative (0) | The IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0200c.html language=enus -->
## TOPIC 00014: PowerRamp:Acquisition Length (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0200c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0200c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Acquisition Length (s) Property

**Short Name:**PowerRamp Acquisition Length (s)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the duration of the signal to be acquired for the PowerRamp measurement. This value is expressed in seconds.

You must set this to a value that is greater than or equal to the duration of the PPDU under analysis, so that the acquired signal contains both rising and falling power ramp transitions.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1 millisecond.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra02017.html language=enus -->
## TOPIC 00015: PowerRamp:Number of Analysis Threads Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra02017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra02017.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Number of Analysis Threads Property

**Short Name:**PowerRamp Num Analysis Threads

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the maximum number of threads used for parallelism for PowerRamp measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra02019.html language=enus -->
## TOPIC 00016: PowerRamp:Results:Fall Time Mean (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra02019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra02019.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Results:Fall Time Mean (s) Property

**Short Name:**PowerRamp Results Fall Time Mean (s)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the power-ramp fall time of the burst. This value is expressed in seconds.

This measurement is performed in accordance with section 16.3.7.7 of *IEEE Standard 802.11-2016*.

When you set the [PowerRamp Averaging Enabled](attra02014.html) property to **True**, this property returns the mean of the fall time results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03013.html language=enus -->
## TOPIC 00017: DSSSModAcc:Power:Measurement Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03013.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Power:Measurement Enabled Property

**Short Name:**DSSSModAcc Pwr Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether power measurement is performed. This measurement computes power of various fields in the PPDU.

Additionally, this measurement computes power over the custom gates that you can configure using the [DSSSModAcc Pwr Num Custom Gates](attra03014.html), the [DSSSModAcc Pwr Custom Gate Start Time](attra03015.html) and the [DSSSModAcc Pwr Custom Gate Stop Time](attra03016.html) properties.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables power measurement. |
| --- | --- |
| True (1) | Enables power measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03015.html language=enus -->
## TOPIC 00018: DSSSModAcc:Power:Custom Gate Start Time (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03015.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Power:Custom Gate Start Time (s) Property

**Short Name:**DSSSModAcc Pwr Custom Gate Start Time (s)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the start time of the custom power gate. This value is expressed in seconds.

Use "gate<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

A value of 0 indicates that the start time is the start of the PPDU. The default value is 0 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03016.html language=enus -->
## TOPIC 00019: DSSSModAcc:Power:Custom Gate Stop Time (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03016.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Power:Custom Gate Stop Time (s) Property

**Short Name:**DSSSModAcc Pwr Custom Gate Stop Time (s)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the stop time for the custom power gate. This value is expressed in seconds.

Use "gate<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 10 microseconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0302c.html language=enus -->
## TOPIC 00020: DSSSModAcc:Frequency Error Correction Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0302c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0302c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Frequency Error Correction Enabled Property

**Short Name:**DSSSModAcc Freq Error Correction Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable frequency error correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables frequency error correction. |
| --- | --- |
| True (1) | Enables frequency error correction. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0302d.html language=enus -->
## TOPIC 00021: DSSSModAcc:Chip Clock Error Correction Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0302d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0302d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Chip Clock Error Correction Enabled Property

**Short Name:**DSSSModAcc Chip Clock Error Correction Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable chip clock error correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables the chip clock error correction. |
| --- | --- |
| True (1) | Enables the chip clock error correction. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0302e.html language=enus -->
## TOPIC 00022: DSSSModAcc:I/Q Origin Offset Correction Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0302e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0302e.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:I/Q Origin Offset Correction Enabled Property

**Short Name:**DSSSModAcc I/Q Origin Offset Correction Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable I/Q origin offset correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables the I/Q origin offset correction. |
| --- | --- |
| True (1) | Enables the I/Q origin offset correction. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0302f.html language=enus -->
## TOPIC 00023: DSSSModAcc:Averaging:Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0302f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0302f.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Averaging:Enabled Property

**Short Name:**DSSSModAcc Averaging Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable averaging for DSSSModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Performs measurement on a single acquisition. |
| --- | --- |
| True (1) | Measurement uses the DSSSModAcc Averaging Count property for the number of acquisitions using which the results are averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03031.html language=enus -->
## TOPIC 00024: DSSSModAcc:All Traces Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03031.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:All Traces Enabled Property

**Short Name:**DSSSModAcc All Traces Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable all the traces computed by DSSSModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03036.html language=enus -->
## TOPIC 00025: DSSSModAcc:Results:Peak EVM (802.11-2007):Maximum (% or dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03036.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:Peak EVM (802.11-2007):Maximum (% or dB) Property

**Short Name:**DSSSModAcc Results Peak EVM (802.11-2007) Max

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.

This measurement is performed in accordance with section 18.4.7.8 of *IEEE Standard 802.11-2007*.
 When you set the [DSSSModAcc Averaging Enabled](attra0302f.html) property to **True**, this result returns the maximum value of the peak EVM computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0303c.html language=enus -->
## TOPIC 00026: DSSSModAcc:Results:Peak EVM (802.11-2016):Mean (% or dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0303c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0303c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:Peak EVM (802.11-2016):Mean (% or dB) Property

**Short Name:**DSSSModAcc Results Peak EVM (802.11-2016) Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak EVM of the burst. This value is expressed as a percentage or in dB.

This measurement is performed in accordance with section 16.3.7.9 of *IEEE Standard 802.11-2016*.
 When you set the [DSSSModAcc Averaging Enabled](attra0302f.html) property to **True**, this result returns the mean of the peak EVM computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03052.html language=enus -->
## TOPIC 00027: DSSSModAcc:Results:Chip Clock Error Mean (ppm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03052.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03052.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:Chip Clock Error Mean (ppm) Property

**Short Name:**DSSSModAcc Results Chip Clock Error Mean (ppm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the chip clock error of the transmitter. This value is expressed in parts per million (ppm).

When you set the [DSSSModAcc Averaging Enabled](attra0302f.html) property to **True**, this result returns the mean of the chip clock error computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03069.html language=enus -->
## TOPIC 00028: DSSSModAcc:Results:PPDU Info:Payload Length (bytes) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03069.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03069.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:PPDU Info:Payload Length (bytes) Property

**Short Name:**DSSSModAcc Results Payload Length (bytes)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the payload length of the acquired burst. This value is expressed in bytes.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0306a.html language=enus -->
## TOPIC 00029: DSSSModAcc:Results:PPDU Info:Preamble Type Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0306a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0306a.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:PPDU Info:Preamble Type Property

**Short Name:**DSSSModAcc Results Preamble Type

Property of [RFmxWLAN](crfmxwlan.html)

Returns the detected preamble type of the acquired burst.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| Long (0) | Indicates that the PPDU has a long PHY preamble and header. |
| --- | --- |
| Short (1) | Indicates that the PPDU has a short PHY preamble and header. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03071.html language=enus -->
## TOPIC 00030: DSSSModAcc:Number of Analysis Threads Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03071.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03071.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Number of Analysis Threads Property

**Short Name:**DSSSModAcc Num Analysis Threads

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the maximum number of threads used for parallelism for DSSSModAcc measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03072.html language=enus -->
## TOPIC 00031: DSSSModAcc:Results:Power:Preamble Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03072.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03072.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:Power:Preamble Average Power Mean (dBm) Property

**Short Name:**DSSSModAcc Results Pwr Preamble Avg Pwr Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the preamble field of the PPDU. This value is expressed in dBm.

When you set the [DSSSModAcc Averaging Enabled](attra0302f.html) property to **True**, this result returns the mean of the average preamble field power computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra03077.html language=enus -->
## TOPIC 00032: DSSSModAcc:Results:Power:Data Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra03077.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra03077.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Results:Power:Data Peak Power Maximum (dBm) Property

**Short Name:**DSSSModAcc Results Pwr Data Pk Pwr Max

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the data field of the PPDU. This value is expressed in dBm.

When you set the [DSSSModAcc Averaging Enabled](attra0302f.html) property to **True**, this result returns the maximum value of the peak data field power computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0307a.html language=enus -->
## TOPIC 00033: DSSSModAcc:Burst Start Detection Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0307a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0307a.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Burst Start Detection Enabled Property

**Short Name:**DSSSModAcc Burst Start Detection Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the measurement detects the rising edge of a burst in the acquired waveform.

The detected rising edge of the burst is used for the measurement. If you are using an I/Q power edge trigger or a digital edge trigger to trigger approximately and consistently at the start of a burst, set this property to **False**. If you are unable to reliably trigger at the start of a burst, set this property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables detection of a rising edge of the burst in the acquired waveform for measurement. |
| --- | --- |
| True (1) | Enables detection of a rising edge of the burst in the acquired waveform for measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0307c.html language=enus -->
## TOPIC 00034: DSSSModAcc:Data Decoding Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0307c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0307c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

DSSSModAcc:Data Decoding Enabled Property

**Short Name:**DSSSModAcc Data Decoding Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

|  | Note Set the Maximum Measurement Length (chips) property to -1 to decode all chips. Data decoding is not supported if the data rate is 33 Mbps. |
| --- | --- |

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables data decoding. |
| --- | --- |
| True (1) | Enables data decoding. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04000.html language=enus -->
## TOPIC 00035: OFDMModAcc:Measurement Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04000.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Measurement Enabled Property

**Short Name:**OFDMModAcc Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable OFDMModAcc measurement for OFDM based standards.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04002.html language=enus -->
## TOPIC 00036: OFDMModAcc:Averaging:Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04002.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Averaging:Enabled Property

**Short Name:**OFDMModAcc Averaging Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable averaging for OFDMModAcc measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the value of the OFDMModAcc Averaging Count property as the number of acquisitions over which the results are computed according to the OFDMModAcc Averaging Type property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04004.html language=enus -->
## TOPIC 00037: OFDMModAcc:Number of Analysis Threads Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04004.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Number of Analysis Threads Property

**Short Name:**OFDMModAcc Num Analysis Threads

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the maximum number of threads used for parallelism for the OFDMModAcc measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04008.html language=enus -->
## TOPIC 00038: OFDMModAcc:EVM Unit Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04008.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:EVM Unit Property

**Short Name:**OFDMModAcc EVM Unit

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the unit for EVM results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **dB**.

| Percentage (0) | The EVM results are returned as a percentage. |
| --- | --- |
| dB (1) | The EVM results are returned in dB. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0400b.html language=enus -->
## TOPIC 00039: OFDMModAcc:Measurement Offset (symbols) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0400b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0400b.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Measurement Offset (symbols) Property

**Short Name:**OFDMModAcc Meas Offset (symbols)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the number of data symbols to be ignored from the start of the data field for EVM computation. This value is expressed in symbols.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0400d.html language=enus -->
## TOPIC 00040: OFDMModAcc:Common Clock Source Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0400d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0400d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Common Clock Source Enabled Property

**Short Name:**OFDMModAcc Common Clock Source Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the transmitter uses the same reference clock signal for generating the RF carrier and the symbol clock.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Specifies that the transmitter does not use a common reference clock. The OFDMModAcc measurement computes the symbol clock error and carrier frequency error independently. |
| --- | --- |
| True (1) | Specifies that the transmitter uses a common reference clock. The OFDMModAcc measurement derives the symbol clock error from the configured center frequency and carrier frequency error. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0400f.html language=enus -->
## TOPIC 00041: OFDMModAcc:Phase Tracking Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0400f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0400f.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Phase Tracking Enabled Property

**Short Name:**OFDMModAcc Phase Tracking Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable pilot-based common phase error correction per OFDM data symbol.

Phase tracking is useful for tracking the phase variation over the modulation symbol caused by the residual frequency offset and phase noise.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Phase tracking is disabled. |
| --- | --- |
| True (1) | Phase tracking is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04010.html language=enus -->
## TOPIC 00042: OFDMModAcc:Symbol Clock Error Correction Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04010.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Symbol Clock Error Correction Enabled Property

**Short Name:**OFDMModAcc Symbol Clock Error Correction Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to enable symbol clock error correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Symbol clock error correction is disabled. |
| --- | --- |
| True (1) | Symbol clock error correction is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04011.html language=enus -->
## TOPIC 00043: OFDMModAcc:Channel Estimation:Type Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04011.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Channel Estimation:Type Property

**Short Name:**OFDMModAcc Ch Estimation Type

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the fields in the PPDU used to estimate the channel frequency response.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Reference**.

| Reference (0) | The channel is estimated using long training fields (LTFs) in the preamble and the most recently received midamble, if present. |
| --- | --- |
| Reference and Data (1) | The channel is estimated using long training fields (LTFs) in the preamble, the midamble (if present), and the data field. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04016.html language=enus -->
## TOPIC 00044: OFDMModAcc:Results:Number of Symbols Used Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04016.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Number of Symbols Used Property

**Short Name:**OFDMModAcc Results Num Symbols Used

Property of [RFmxWLAN](crfmxwlan.html)

Returns the number of OFDM symbols used by the measurement.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04019.html language=enus -->
## TOPIC 00045: OFDMModAcc:Power:Custom Gate Start Time (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04019.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Power:Custom Gate Start Time (s) Property

**Short Name:**OFDMModAcc Pwr Custom Gate Start Time (s)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the start time of the custom power gate. This value is expressed in seconds.

A value of 0 indicates that the start time is the start of the PPDU.

Use "gate<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04023.html language=enus -->
## TOPIC 00046: OFDMModAcc:Results:Spectral Flatness Margin (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04023.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Spectral Flatness Margin (dB) Property

**Short Name:**OFDMModAcc Results Spectral Flatness Margin (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the spectral flatness margin, which is the minimum of the upper and lower spectral flatness margins. This value is expressed in dB.

The upper spectral flatness margin is the minimum difference between the upper mask and the spectral flatness across subcarriers. The lower spectral flatness margin is the minimum difference between the spectral flatness and the lower mask across subcarriers. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, the spectral flatness is computed using the mean of the channel frequency response magnitude computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04024.html language=enus -->
## TOPIC 00047: OFDMModAcc:Results:Spectral Flatness Margin Subcarrier Index Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04024.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Spectral Flatness Margin Subcarrier Index Property

**Short Name:**OFDMModAcc Results Spectral Flatness Margin Subcarrier Index

Property of [RFmxWLAN](crfmxwlan.html)

Returns the subcarrier index corresponding to the [OFDMModAcc Results Spectral Flatness Margin](attra04023.html) result.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04025.html language=enus -->
## TOPIC 00048: OFDMModAcc:Results:Unused Tone Error:Margin (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04025.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Unused Tone Error:Margin (dB) Property

**Short Name:**OFDMModAcc Results Unused Tone Error Margin (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the unused tone error margin, which is the minimum difference between the unused tone error mask and the unused tone error across 26-tone RUs. This value is expressed in dB.

This result is applicable only to 802.11ax and 802.11be TB PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, the measurement computes the mean of the unused tone error over each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04026.html language=enus -->
## TOPIC 00049: OFDMModAcc:Results:Unused Tone Error:Margin RU Index Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04026.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Unused Tone Error:Margin RU Index Property

**Short Name:**OFDMModAcc Results Unused Tone Error Margin RU Index

Property of [RFmxWLAN](crfmxwlan.html)

Returns the 26-tone RU index corresponding to the [OFDMModAcc Results Unused Tone Error Margin](attra04025.html) result.

This result is applicable for 802.11ax and 802.11be TB PPDU signals.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04028.html language=enus -->
## TOPIC 00050: OFDMModAcc:Results:Frequency Error Mean (Hz) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04028.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Frequency Error Mean (Hz) Property

**Short Name:**OFDMModAcc Results Freq Error Mean (Hz)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the carrier frequency error of the transmitter. This value is expressed in Hz.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the carrier frequency error results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04029.html language=enus -->
## TOPIC 00051: OFDMModAcc:Results:Frequency Error CCDF 10% (Hz) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04029.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Frequency Error CCDF 10% (Hz) Property

**Short Name:**OFDMModAcc Results Freq Error CCDF 10% (Hz)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the 10% point of Complementary Cumulative Distribution Function (CCDF) of the absolute frequency error. This value is expressed in Hz.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, the CCDF is computed over each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0402a.html language=enus -->
## TOPIC 00052: OFDMModAcc:Results:Symbol Clock Error Mean (ppm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0402a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0402a.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Symbol Clock Error Mean (ppm) Property

**Short Name:**OFDMModAcc Results Symbol Clock Error Mean (ppm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the symbol clock error of the transmitter.

Symbol clock error is the difference between the symbol clocks at the digital-to-analog converter (DAC) of the transmitting device under test (DUT) and the digitizer of the instrument. This value is expressed in parts per million (ppm).

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the symbol clock error results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0402b.html language=enus -->
## TOPIC 00053: OFDMModAcc:Results:Relative I/Q Origin Offset Mean (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0402b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0402b.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Relative I/Q Origin Offset Mean (dB) Property

**Short Name:**OFDMModAcc Results Rel I/Q Origin Offset Mean (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the relative I/Q origin offset, which is the ratio of the power of the DC subcarrier to the total power of all the subcarriers. This value is expressed in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the relative I/Q origin offset computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0402d.html language=enus -->
## TOPIC 00054: OFDMModAcc:Results:I/Q Gain Imbalance Mean (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0402d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0402d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:I/Q Gain Imbalance Mean (dB) Property

**Short Name:**OFDMModAcc Results I/Q Gain Imbalance Mean (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the I/Q gain imbalance, which is the ratio of the RMS amplitude of the in-phase (I) component of the signal to the RMS amplitude of the quadrature-phase (Q) component of the signal. This value is expressed in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the I/Q gain imbalance results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0402e.html language=enus -->
## TOPIC 00055: OFDMModAcc:Results:I/Q Quadrature Error Mean (deg) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0402e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0402e.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:I/Q Quadrature Error Mean (deg) Property

**Short Name:**OFDMModAcc Results I/Q Quadrature Error Mean (deg)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the I/Q quadrature error, which is a measure of deviation of the phase difference between the quadrature-phase (Q) and the in-phase (I) component of the signal from 90 degrees. This value is expressed in degrees.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the I/Q quadrature error results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0402f.html language=enus -->
## TOPIC 00056: OFDMModAcc:Results:I/Q Timing Skew Mean (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0402f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0402f.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:I/Q Timing Skew Mean (s) Property

**Short Name:**OFDMModAcc Results I/Q Timing Skew Mean (s)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the I/Q timing skew, which is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the I/Q timing skew computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04030.html language=enus -->
## TOPIC 00057: OFDMModAcc:Results:RMS Common Phase Error Mean (deg) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04030.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:RMS Common Phase Error Mean (deg) Property

**Short Name:**OFDMModAcc Results RMS Common Phase Error Mean (deg)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RMS common phase error.

Common phase error for an OFDM symbol is the average phase deviation of the pilot-subcarriers from their ideal phase. RMS Common Phase Error is the RMS of common phase error of all OFDM symbols. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the RMS common phase error computed for each averaging count.

Refer to [Common Pilot Error in OFDM Standards](/csh?topicname=rfmxwlan/common_pilot_error.html) for more information.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04031.html language=enus -->
## TOPIC 00058: OFDMModAcc:Results:PPDU Info:PPDU Type Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04031.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:PPDU Type Property

**Short Name:**OFDMModAcc Results PPDU Type

Property of [RFmxWLAN](crfmxwlan.html)

Returns the PPDU type of the measured signal.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| Non-HT (0) | Indicates an 802.11a, 802.11j, or 802.11p PPDU, or 802.11n, 802.11ac, or 802.11ax PPDU operating in the Non-HT mode. |
| --- | --- |
| Mixed (1) | Indicates the HT-mixed PPDU (802.11n). |
| Greenfield (2) | Applicable HT-Greenfield PPDU (802.11n). |
| SU (3) | Indicates the VHT SU PPDU if you set the Standard property to 802.11ac or the HE SU PPDU if you set the Standard property to 802.11ax. |
| MU (4) | Indicates the VHT MU PPDU if you set the Standard property to 802.11ac, the HE MU PPDU if you set the Standard property to 802.11ax, or the EHT MU PPDU if you set the Standard property to 802.11be. |
| Extended Range SU (5) | Indicates the HE Extended Range SU PPDU (802.11ax). |
| Trigger-based (6) | Indicates the HE TB PPDU if you set the Standard property to 802.11ax or the EHT TB PPDU if you set the Standard property to 802.11be. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04032.html language=enus -->
## TOPIC 00059: OFDMModAcc:Results:PPDU Info:MCS Index Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04032.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:MCS Index Property

**Short Name:**OFDMModAcc Results MCS Index

Property of [RFmxWLAN](crfmxwlan.html)

Returns the MCS index or the data rate of the measured signal.

The MCS index or data rate for various standard signals are decoded as follows:

| Standard | Field |
| --- | --- |
| 802.11a, 802.11j, 802.11p | The data rate is decoded from the SIGNAL field. |
| 802.11n | The MCS index is decoded from the HT-SIG field. |
| 802.11ac SU | The MCS index is decoded from the VHT-SIG-A field. |
| 802.11ac MU | The MCS index is decoded from the VHT-SIG-B field. |
| 802.11ax SU and Extended Range SU PPDU | The MCS index is decoded from the HE-SIG-A field. |
| 802.11ax MU PPDU | The MCS index is decoded from the HE-SIG-B field. |
| 802.11be MU PPDU | The MCS index is decoded from the EHT-SIG field. |

For 802.11a, 802.11j, and 802.11p signals, the following MCS indices corresponds to their data rates:

| MCS | Data Rate |
| --- | --- |
| 0 | 1.5 Mbps, 3 Mbps, and 6 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 1 | 2.25 Mbps, 4.5 Mbps, and 9 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 2 | 3 Mbps, 6 Mbps, and 12 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 3 | 4.5 Mbps, 9 Mbps, and 18 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 4 | 6 Mbps, 12 Mbps, and 24 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 5 | 9 Mbps, 18 Mbps, and 36 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 6 | 12 Mbps, 24 Mbps, and 48 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |
| 7 | 13.5 Mbps, 27 Mbps, and 54 Mbps for channel bandwidths of 5 MHz, 10 MHz, and 20 MHz, respectively. |

For 802.11ax or 802.11be TB PPDU signals, this property returns the same value as the [OFDM MCS Index](attra00019.html) property.

Use "user<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result for MU PPDU signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04033.html language=enus -->
## TOPIC 00060: OFDMModAcc:Results:PPDU Info:RU Size Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04033.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:RU Size Property

**Short Name:**OFDMModAcc Results RU Size

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RU or the MRU size.

This result is applicable for 802.11ax MU, extended range SU, and TB PPDU signals, and 802.11be MU and TB PPDU signals. For 802.11ax MU PPDU signals, this value is decoded from the HE-SIG-B field. For 802.11ax extended range SU PPDU signals, this value is decoded from the HE-SIG-A field. For 802.11be MU PPDU signals, this value is decoded from the EHT-SIG field. For 802.11ax or 802.11be TB PPDU signals, this property returns the same value as the [OFDM RU Size](attra0001a.html) property.

Use "user<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

| 26 (26) | The RU size is 26. |
| --- | --- |
| 52 (52) | The RU size is 52. |
| 106 (106) | The RU size is 106. |
| 242 (242) | The RU size is 242. |
| 484 (484) | The RU size is 484. |
| 996 (996) | The RU size is 996. |
| 2x996 (1992) | The RU size is 2 x 996. |
| 4x996 (3984) | The RU size is 4 x 996. |
| 52+26 (78) | The RU size is 52 + 26. |
| 106+26 (132) | The RU size is 106 + 26. |
| 484+242 (726) | The RU size is 484 + 242. |
| 996+484 (1480) | The RU size is 996 + 484. |
| 996+484+242 (1722) | The RU size is 996 + 484 + 242. |
| 2x996+484 (2476) | The RU size is 2 x 996 + 484. |
| 3x996 (2988) | The RU size is 3 x 996. |
| 3x996+484 (3472) | The RU size is 3 x 996 + 484 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04034.html language=enus -->
## TOPIC 00061: OFDMModAcc:Results:PPDU Info:RU Offset/MRU Index Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04034.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:RU Offset/MRU Index Property

**Short Name:**OFDMModAcc Results RU Offset/MRU Index

Property of [RFmxWLAN](crfmxwlan.html)

Returns the location of RU or MRU for a user. If an RU is detected, the RU Offset is in terms of the index of a 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs. If an MRU is detected, the MRU Index is as defined in the Table 36-8 to Table 36-15 of *IEEE P802.11be/D5.0.1*.

This result is applicable for 802.11ax MU and TB PPDU signals, and 802.11be MU and TB PPDU signals. For 802.11ax MU PPDU signals, this value is decoded from the HE-SIG-B field. For 802.11be MU PPDU signals, this value is decoded from the EHT-SIG field. For 802.11ax or 802.11be TB PPDU signals, this property returns the same value as the [OFDM RU Offset/MRU Index](attra0001b.html) property.

Use "user<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04035.html language=enus -->
## TOPIC 00062: OFDMModAcc:Results:PPDU Info:Number of Users Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04035.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:Number of Users Property

**Short Name:**OFDMModAcc Results Num Users

Property of [RFmxWLAN](crfmxwlan.html)

Returns the number of users.

For 802.11ac MU PPDU signals, this value is decoded from the VHT-SIG-A field. For 802.11ax MU PPDU signals, this value is derived from the HE-SIG-B field. For 802.11be MU PPDU signals, this value is decoded from the EHT-SIG field.

For all other PPDUs, this property returns 1.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04037.html language=enus -->
## TOPIC 00063: OFDMModAcc:Results:PPDU Info:Guard Interval Type Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04037.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:Guard Interval Type Property

**Short Name:**OFDMModAcc Results Guard Interval Type

Property of [RFmxWLAN](crfmxwlan.html)

Returns the size of the guard interval of OFDM symbols.

This result is always **1/4** for 802.11a, 802.11j, and 802.11p signals. The value is decoded for various standards as follows:

| Standards | Fields |
| --- | --- |
| 802.11n | The guard interval type is decoded from HT-SIG field. |
| 802.11ac | The guard interval type is decoded from VHT-SIG-A field. |
| 802.11ax | The guard interval type is decoded from HE-SIG-A field. |
| 802.11be | The guard interval type is decoded from EHT-SIG field. |

For 802.11ax or 802.11be TB PPDU signals, the property returns the same value as the [OFDM Guard Interval Type](attra0001c.html) property.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| 1/4 (0) | The Guard interval is 1/4th of the IFFT duration. |
| --- | --- |
| 1/8 (1) | The Guard interval is 1/8th of the IFFT duration. |
| 1/16 (2) | The Guard interval is 1/16th of the IFFT duration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04038.html language=enus -->
## TOPIC 00064: OFDMModAcc:Results:PPDU Info:LTF Size Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04038.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:LTF Size Property

**Short Name:**OFDMModAcc Results LTF Size

Property of [RFmxWLAN](crfmxwlan.html)

Returns the HE-LTF size or EHT-LTF size when you set the [Standard](attra0000d.html) property to **802.11ax** or **802.11be**, respectively.

This result is applicable only to 802.11ax and 802.11be signals. This value is decoded from the HE-SIG-A field when you set the Standard property to **802.11ax** and from the EHT-SIG field when you set the Standard property to **802.11be**.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| Not Applicable (-1) | Indicates that the LTF Size is invalid for the current waveform. |
| --- | --- |
| 4x (0) | Indicates that the LTF Size is 4x. |
| 2x (1) | Indicates that the LTF Size is 2x. |
| 1x (2) | Indicates that the LTF Size is 1x. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0403a.html language=enus -->
## TOPIC 00065: OFDMModAcc:Results:Power:L-STF Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0403a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0403a.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:L-STF Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr L-STF Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the L-STF or STF field. This value is expressed in dBm.

This result is not applicable for 802.11n greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the L-STF or STF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0403c.html language=enus -->
## TOPIC 00066: OFDMModAcc:Results:Power:L-LTF Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0403c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0403c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:L-LTF Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr L-LTF Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the L-LTF or LTF field. This value is expressed in dBm.

This result is not applicable for 802.11n Greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the L-LTF or LTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0403d.html language=enus -->
## TOPIC 00067: OFDMModAcc:Results:Power:L-LTF Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0403d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0403d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:L-LTF Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr L-LTF Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the L-LTF or LTF field. This value is expressed in dBm.

This result is not applicable for 802.11n Greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the L-LTF or LTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0403e.html language=enus -->
## TOPIC 00068: OFDMModAcc:Results:Power:L-SIG Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0403e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0403e.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:L-SIG Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr L-SIG Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the L-SIG or SIGNAL field. This value is expressed in dBm.

This result is not applicable for 802.11n Greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the L-SIG or SIGNAL field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0403f.html language=enus -->
## TOPIC 00069: OFDMModAcc:Results:Power:L-SIG Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0403f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0403f.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:L-SIG Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr L-SIG Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the L-SIG or SIGNAL field. This value is expressed in dBm.

This result is not applicable for 802.11n Greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the L-SIG or SIGNAL field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04040.html language=enus -->
## TOPIC 00070: OFDMModAcc:Results:Power:RL-SIG Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04040.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04040.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:RL-SIG Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr RL-SIG Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the RL-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11ax and 802.11be signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the RL-SIG field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04041.html language=enus -->
## TOPIC 00071: OFDMModAcc:Results:Power:RL-SIG Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04041.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04041.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:RL-SIG Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr RL-SIG Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the RL-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11ax and 802.11be signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the RL-SIG field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04042.html language=enus -->
## TOPIC 00072: OFDMModAcc:Results:Power:HT-SIG Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04042.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04042.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HT-SIG Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HT-SIG Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the HT-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-SIG field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04043.html language=enus -->
## TOPIC 00073: OFDMModAcc:Results:Power:HT-SIG Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04043.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04043.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HT-SIG Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HT-SIG Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the HT-SIG field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HT-SIG field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04045.html language=enus -->
## TOPIC 00074: OFDMModAcc:Results:Power:VHT-SIG-A Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04045.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04045.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:VHT-SIG-A Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr VHT-SIG-A Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the VHT-SIG-A field. This value is expressed in dBm.

This result is applicable only to 802.11ac signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the VHT-SIG-A field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0404b.html language=enus -->
## TOPIC 00075: OFDMModAcc:Results:Power:HE-SIG-B Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0404b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0404b.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HE-SIG-B Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HE-SIG-B Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the HE-SIG-B field. This value is expressed in dBm.

This result is applicable only to 802.11ax signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HE-SIG-B field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0404d.html language=enus -->
## TOPIC 00076: OFDMModAcc:Results:Power:HT-STF Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0404d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0404d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HT-STF Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HT-STF Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the HT-STF field. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HT-STF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0404e.html language=enus -->
## TOPIC 00077: OFDMModAcc:Results:Power:HT-GF-STF Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0404e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0404e.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HT-GF-STF Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HT-GF-STF Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the HT-GF-STF. This value is expressed in dBm.

This result is applicable only to 802.11n greenfield PPDU signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-GF-STF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04054.html language=enus -->
## TOPIC 00078: OFDMModAcc:Results:Power:HT-DLTF Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04054.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04054.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HT-DLTF Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HT-DLTF Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the HT-DLTF. This value is expressed in dBm.

This result is applicable only to 802.11n signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HT-DLTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04058.html language=enus -->
## TOPIC 00079: OFDMModAcc:Results:Power:VHT-LTF Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04058.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04058.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:VHT-LTF Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr VHT-LTF Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the VHT-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11ac signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the VHT-LTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04059.html language=enus -->
## TOPIC 00080: OFDMModAcc:Results:Power:VHT-LTF Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04059.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04059.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:VHT-LTF Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr VHT-LTF Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the VHT-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11ac signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the VHT-LTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0405a.html language=enus -->
## TOPIC 00081: OFDMModAcc:Results:Power:HE-LTF Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0405a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0405a.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HE-LTF Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HE-LTF Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the HE-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11ax signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the HE-LTF average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0405b.html language=enus -->
## TOPIC 00082: OFDMModAcc:Results:Power:HE-LTF Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0405b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0405b.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:HE-LTF Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr HE-LTF Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the HE-LTF field. This value is expressed in dBm.

This result is applicable only to 802.11ax signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the HE-LTF peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0405c.html language=enus -->
## TOPIC 00083: OFDMModAcc:Results:Power:Data Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0405c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0405c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:Data Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr Data Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the data field. This value is expressed in dBm.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the data field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0405d.html language=enus -->
## TOPIC 00084: OFDMModAcc:Results:Power:Data Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0405d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0405d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:Data Peak Power Maximum (dBm) Property

**Short Name:**OFDMModAcc Results Pwr Data Pk Pwr Max (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the data field. This value is expressed in dBm.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the maximum of the data field peak power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0405e.html language=enus -->
## TOPIC 00085: OFDMModAcc:Results:Power:PE Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0405e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0405e.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:PE Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr PE Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the packet extension field. This value is expressed in dBm.

This result is applicable for 802.11ax and 802.11be signals. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the packet extension field average power results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04062.html language=enus -->
## TOPIC 00086: OFDMModAcc:Results:Power:Custom Gate Average Power Mean (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04062.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04062.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Power:Custom Gate Average Power Mean (dBm) Property

**Short Name:**OFDMModAcc Results Pwr Custom Gate Avg Pwr Mean (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the custom gate. This value is expressed in dBm.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the custom gate average power results computed for each averaging count.

Use "gate<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04066.html language=enus -->
## TOPIC 00087: OFDMModAcc:Measurement Mode Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04066.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04066.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Measurement Mode Property

**Short Name:**OFDMModAcc Meas Mode

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the measurement calibrates the noise floor of analyzer or performs the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Measure (0) | The OFDMModAcc measurement is performed on the acquired signal. |
| --- | --- |
| Calibrate Noise Floor (1) | The OFDMModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04067.html language=enus -->
## TOPIC 00088: OFDMModAcc:Noise Compensation:Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04067.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04067.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Noise Compensation:Enabled Property

**Short Name:**OFDMModAcc Noise Comp Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the contribution of the instrument noise is compensated for EVM computation.

You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the OFDMModAcc measurement and cached for future use.

**Supported devices:**PXIe-5830/5831/5832/5646/5840/5841/5842.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables instrument noise compensation for EVM results. |
| --- | --- |
| True (1) | Enables instrument noise compensation for EVM results. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0406e.html language=enus -->
## TOPIC 00089: OFDMModAcc:Results:Composite RMS EVM Mean (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0406e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0406e.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Composite RMS EVM Mean (dB or %) Property

**Short Name:**OFDMModAcc Results Composite RMS EVM Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RMS EVM of all subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04076.html language=enus -->
## TOPIC 00090: OFDMModAcc:Results:Stream Pilot RMS EVM Mean (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04076.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04076.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Stream Pilot RMS EVM Mean (dB or %) Property

**Short Name:**OFDMModAcc Results Stream Pilot RMS EVM Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the stream RMS EVM of pilot subcarriers in all OFDM symbols. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of pilot stream RMS EVM results computed for each averaging count.

Use "segment<*n*>/stream<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04077.html language=enus -->
## TOPIC 00091: OFDMModAcc:Results:User Stream RMS EVM Mean (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04077.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04077.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:User Stream RMS EVM Mean (dB or %) Property

**Short Name:**OFDMModAcc Results User Stream RMS EVM Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RMS EVM of all subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.

This result is applicable for MU PPDU. When you set [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of RMS EVM results for the specified user that is computed for each averaging count.

Use "user<*n*>/stream<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04078.html language=enus -->
## TOPIC 00092: OFDMModAcc:Results:User Stream Data RMS EVM Mean (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04078.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04078.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:User Stream Data RMS EVM Mean (dB or %) Property

**Short Name:**OFDMModAcc Results User Stream Data RMS EVM Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RMS EVM of data-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.

This result is applicable for MU PPDU. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of data RMS EVM results for the specified user that is computed for each averaging count.

Use "user<*n*>/stream<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04079.html language=enus -->
## TOPIC 00093: OFDMModAcc:Results:User Stream Pilot RMS EVM Mean (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04079.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04079.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:User Stream Pilot RMS EVM Mean (dB or %) Property

**Short Name:**OFDMModAcc Results User Stream Pilot RMS EVM Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RMS EVM of pilot-subcarriers in all OFDM symbols for the specified user. This value is expressed as a percentage or in dB.

This result is applicable for MU PPDU. When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of pilot RMS EVM results for the specified user that is computed for each averaging count.

Use "user<*n*>/stream<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0407d.html language=enus -->
## TOPIC 00094: OFDMModAcc:Optimize Dynamic Range for EVM:Margin (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0407d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0407d.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Optimize Dynamic Range for EVM:Margin (dB) Property

**Short Name:**OFDMModAcc Optimize Dynamic Range for EVM Margin (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the margin above the reference level you specify when you set the [OFDMModAcc Optimize Dynamic Range for EVM Enabled](../rfmxwlanprop/attra0407c.html) property to **True**. This value is expressed in dB.

When the property's value 0, the dynamic range is optimized. When you set a positive value to the property, the dynamic range reduces from the optimized dynamic range. You can use this property to avoid ADC and onboard signal processing (OSP) overflows.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04085.html language=enus -->
## TOPIC 00095: OFDMModAcc:Burst Start Detection Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04085.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04085.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Burst Start Detection Enabled Property

**Short Name:**OFDMModAcc Burst Start Detection Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the measurement detects a rising edge of a burst in the acquired waveform.

If you are using an I/Q power edge trigger or digital edge trigger to trigger approximately and consistently at the start of a burst, set this property to **False**. If you are unable to reliably trigger at the start of a burst, set this property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables detecting a rising edge of a burst in the acquired waveform. |
| --- | --- |
| True (1) | Enables detecting a rising edge of a burst in the acquired waveform. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0408b.html language=enus -->
## TOPIC 00096: OFDMModAcc:Data Decoding Enabled Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0408b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0408b.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Data Decoding Enabled Property

**Short Name:**OFDMModAcc Data Decoding Enabled

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether to decode data bits and check for the validity of the cyclic redundancy check (CRC).

This further enables the check for the validity of SIG-B cyclic redundancy check (CRC) of the 802.11ac PPDU.

|  | Note Set the Maximum Measurement Length (symbols) property to -1 to decode all symbols. |
| --- | --- |

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables data decoding. |
| --- | --- |
| True (1) | Enables data decoding. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04090.html language=enus -->
## TOPIC 00097: OFDMModAcc:Results:PPDU Info:Space Time Stream Offset Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04090.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04090.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:Space Time Stream Offset Property

**Short Name:**OFDMModAcc Results Space Time Stream Offset

Property of [RFmxWLAN](crfmxwlan.html)

Returns the space time stream offset. This property is applicable only to 802.11ac, 802.11ax and 802.11be signals.

Use "user<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04091.html language=enus -->
## TOPIC 00098: OFDMModAcc:Results:PPDU Info:U-SIG CRC Status Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04091.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04091.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:U-SIG CRC Status Property

**Short Name:**OFDMModAcc Results U-SIG CRC Status

Property of [RFmxWLAN](crfmxwlan.html)

Returns whether the cyclic redundancy check (CRC) has passed for the U-SIG field of the 802.11be waveform.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| Not Applicable (-1) | Returns that the U-SIG CRC is invalid for the current waveform. |
| --- | --- |
| Fail (0) | Returns that the U-SIG CRC failed. |
| Pass (1) | Returns that the U-SIG CRC passed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04092.html language=enus -->
## TOPIC 00099: OFDMModAcc:Results:PPDU Info:EHT-SIG CRC Status Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04092.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04092.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:PPDU Info:EHT-SIG CRC Status Property

**Short Name:**OFDMModAcc Results EHT-SIG CRC Status

Property of [RFmxWLAN](crfmxwlan.html)

Returns whether the cyclic redundancy check (CRC) has passed for the EHT-SIG field of the 802.11be waveform.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| Not Applicable (-1) | Returns that the EHT-SIG CRC is invalid for the current waveform. |
| --- | --- |
| Fail (0) | Returns that the EHT-SIG CRC failed. |
| Pass (1) | Returns that the EHT-SIG CRC passed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra04096.html language=enus -->
## TOPIC 00100: OFDMModAcc:Results:Stream RMS EVM Maximum (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra04096.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra04096.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Stream RMS EVM Maximum (dB or %) Property

**Short Name:**OFDMModAcc Results Stream RMS EVM Max

Property of [RFmxWLAN](crfmxwlan.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040a3.html language=enus -->
## TOPIC 00101: OFDMModAcc:Results:Symbol Clock Error Minimum (ppm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040a3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040a3.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Symbol Clock Error Minimum (ppm) Property

**Short Name:**OFDMModAcc Results Symbol Clock Error Min (ppm)

Property of [RFmxWLAN](crfmxwlan.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040a4.html language=enus -->
## TOPIC 00102: OFDMModAcc:Results:Relative I/Q Origin Offset Maximum (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040a4.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040a4.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Relative I/Q Origin Offset Maximum (dB) Property

**Short Name:**OFDMModAcc Results Rel I/Q Origin Offset Max (dB)

Property of [RFmxWLAN](crfmxwlan.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040a5.html language=enus -->
## TOPIC 00103: OFDMModAcc:Results:Relative I/Q Origin Offset Minimum (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040a5.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Relative I/Q Origin Offset Minimum (dB) Property

**Short Name:**OFDMModAcc Results Rel I/Q Origin Offset Min (dB)

Property of [RFmxWLAN](crfmxwlan.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040a9.html language=enus -->
## TOPIC 00104: OFDMModAcc:Results:I/Q Quadrature Error Minimum (deg) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040a9.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040a9.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:I/Q Quadrature Error Minimum (deg) Property

**Short Name:**OFDMModAcc Results I/Q Quadrature Error Min (deg)

Property of [RFmxWLAN](crfmxwlan.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040b0.html language=enus -->
## TOPIC 00105: OFDMModAcc:Results:Burst Start Time Mean (s) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040b0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040b0.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:Burst Start Time Mean (s) Property

**Short Name:**OFDMModAcc Results Burst Start Time Mean (s)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the absolute time corresponding to the detected start of the analyzed burst. The start time is computed with respect to the initial time value of the acquired waveform. This value is expressed in seconds.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of the burst start time computed for each averaging count.

Use "segment<*n*>/chain<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040bc.html language=enus -->
## TOPIC 00106: OFDMModAcc:Results:SIG RMS EVM Mean (dB or %) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040bc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040bc.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Results:SIG RMS EVM Mean (dB or %) Property

**Short Name:**OFDMModAcc Results SIG RMS EVM Mean

Property of [RFmxWLAN](crfmxwlan.html)

Returns the RMS EVM of subcarriers in the SIG symbol. This value is expressed as a percentage or in dB.

When you set the [OFDMModAcc Averaging Enabled](attra04002.html) property to **True**, this property returns the mean of RMS EVM results computed for each averaging count.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra040d1.html language=enus -->
## TOPIC 00107: OFDMModAcc:Common Pilot Error Scaling Reference Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra040d1.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra040d1.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

OFDMModAcc:Common Pilot Error Scaling Reference Property

**Short Name:**OFDMModAcc Common Pilot Error Scaling Reference

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether common pilot error is computed relative to only LTF or scaling by average CPE.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Average CPE**.

| None (0) | Specifies that Common Pilot Error is computed relative to only LTF and no scaling is performed. |
| --- | --- |
| Average CPE (1) | Specifies that Common Pilot Error is computed relative to LTF and scaling by average CPE is performed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05008.html language=enus -->
## TOPIC 00108: SEM:Offset:Stop Frequency (Hz) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05008.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Stop Frequency (Hz) Property

**Short Name:**SEM Offset Stop Freq (Hz)

Property of [RFmxWLAN](crfmxwlan.html)

Specifies the stop frequency of the offset segment relative to carrier frequency. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure this property.

The default value is 11 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra0500c.html language=enus -->
## TOPIC 00109: SEM:Span:Auto Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra0500c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra0500c.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Span:Auto Property

**Short Name:**SEM Span Auto

Property of [RFmxWLAN](crfmxwlan.html)

Specifies whether the frequency range of the spectrum used for SEM measurement is computed automatically by the measurement or is configured by you.

This property is applicable when you set the [SEM Mask Type](attra05002.html)
 property to **Standard**.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The span you configure is used as the frequency range for the SEM measurement. |
| --- | --- |
| True (1) | The span is automatically computed based on the configured standard and channel bandwidth. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05022.html language=enus -->
## TOPIC 00110: SEM:Results:Lower Offset:Absolute Integrated Power (dBm) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05022.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Lower Offset Abs Integrated Pwr (dBm)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the lower (negative) offset channel over the bandwidth obtained by the start and stop frequencies of the offset channel. This value is expressed in dBm.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05023.html language=enus -->
## TOPIC 00111: SEM:Results:Lower Offset:Relative Integrated Power (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05023.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Relative Integrated Power (dB) Property

**Short Name:**SEM Results Lower Offset Rel Integrated Pwr (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the average power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05025.html language=enus -->
## TOPIC 00112: SEM:Results:Lower Offset:Relative Peak Power (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05025.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Relative Peak Power (dB) Property

**Short Name:**SEM Results Lower Offset Rel Pk Pwr (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the peak power of the lower (negative) offset segment relative to the peak power of the carrier channel. This value is expressed in dB.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05030.html language=enus -->
## TOPIC 00113: SEM:Results:Upper Offset:Peak Frequency (Hz) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05030.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Peak Frequency (Hz) Property

**Short Name:**SEM Results Upper Offset Pk Freq (Hz)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the frequency at which the peak power occurs in the offset (positive) channel. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05031.html language=enus -->
## TOPIC 00114: SEM:Results:Upper Offset:Margin (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05031.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin (dB) Property

**Short Name:**SEM Results Upper Offset Margin (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the margin from the SEM measurement mask for the offset (positive). This value is expressed in dB.

Margin is computed as

Margin(dB) = Max(Spectrum[] - Mask[])

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05033.html language=enus -->
## TOPIC 00115: SEM:Results:Upper Offset:Margin Relative Power (dB) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05033.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Relative Power (dB) Property

**Short Name:**SEM Results Upper Offset Margin Rel Pwr (dB)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the power level of the spectrum corresponding to the result of the [SEM Results Upper Offset Margin](attra05031.html) property. This value is expressed in dB.

The power level is returned relative to the peak power of the carrier channel.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wlan-prop path=rfmxwlanprop/attra05034.html language=enus -->
## TOPIC 00116: SEM:Results:Upper Offset:Margin Frequency (Hz) Property

- bundle_id: `rfmx-wlan-prop`
- source_path: `rfmxwlanprop/attra05034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wlan-prop/raw/resource/enus/rfmxwlanprop/attra05034.html
- document_id: `rfmx-wlan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Frequency (Hz) Property

**Short Name:**SEM Results Upper Offset Margin Freq (Hz)

Property of [RFmxWLAN](crfmxwlan.html)

Returns the frequency of the spectrum corresponding to the result of the [SEM Results Upper Offset Margin](attra05031.html) property. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |
