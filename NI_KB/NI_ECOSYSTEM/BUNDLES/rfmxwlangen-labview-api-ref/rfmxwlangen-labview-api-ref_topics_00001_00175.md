# NI DOCUMENT BUNDLE: rfmxwlangen-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwlangen-labview-api-ref start=1 end=175 -->
<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1.html language=enus -->
## TOPIC 00001: Obsolete:Power Level (dBm)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the average power level of the active portion of the burst for signal generation. The active portion of the burst is the WLAN packet excluding the interframe spacing. This value is expressed in dBm. This property is available only if you set the toolkit compatibility version parameter of t

### Obsolete:Power Level (dBm)

Specifies the average power level of the active portion of the burst for signal generation. The active portion of the burst is the WLAN packet excluding the interframe spacing. This value is expressed in dBm.

Note

toolkit compatibility version

niWLANG Open Session

1.0.0

2.0.0

If you set the [Standard](attr1f.html) property to **80211N MIMOOFDM**, use an [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string to configure this property.

The default value is -10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Level (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr15.html language=enus -->
## TOPIC 00002: Impairments:IQ Impairments:IQ Gain Imbalance (dB)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr15.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr15.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. This value is expressed in dB. If you set this property to a large value, you may experience dynamic range loss at the digital-to-analog converter (DAC). I/Q gain imbalance

### Impairments:IQ Impairments:IQ Gain Imbalance (dB)

Specifies the ratio of the mean amplitude of the in-phase (I) signal to the mean amplitude of the quadrature-phase (Q) signal. This value is expressed in dB.

Note

I/Q gain imbalance follows the definition shown in the following equation:

*I'* = *I* - *γ* * sin(φ) * *Q* + *I*
 0

*Q'* = *γ* * cos(φ) * *Q* + *Q*
 0

| where | γ = 10(I/Q gain imbalance/20) |
| --- | --- |
|  | φ is the quadrature skew |
|  | I is the in-phase component of the waveform before applying impairments |
|  | Q is the quadrature component of the waveform before applying impairments |
|  | I' is the in-phase component of the waveform after applying impairments |
|  | Q' is the quadrature component of the waveform after applying impairments |
|  | I 0 = (I RMS * I DC Offset)/100 |
|  | Q 0 = (Q RMS * Q DC Offset)/100 |

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx" |
| 80211AC MIMOOFDM , 80211AF MIMOOFDM | "segmentx/channely" |
| 80211AX MIMOOFDM | "segmentx/channely", if you set the PPDU Type property to SU PPDU, Extended Range SU PPDU or MU PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty/channelz", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "channelx", if you set the PPDU Type property to MU PPDU |
| 80211BE MIMOOFDM | "[userx]/channely", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "channelx", if you set the PPDU Type property to MU PPDU or ELR PPDU |
| 80211BN MIMOOFDM | "[userx]/channely", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |

The default value is 0. Valid values are -6 to +6, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr19.html language=enus -->
## TOPIC 00003: Impairments:Sample Clock Offset (ppm)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr19.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr19.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset in the Sample Clock frequency from the sampling frequency defined by the following equation: Sampling Frequency = max (maximum hardware I/Q Rate, Oversampling Ratio * Nyquist Sampling Rate) where Maximum Hardware I/Q is the value of the Maximum Hardware IQ Rate property Oversamp

### Impairments:Sample Clock Offset (ppm)

Specifies the offset in the Sample Clock frequency from the sampling frequency defined by the following equation:

*Sampling Frequency* = max (maximum hardware I/Q Rate, *Oversampling Ratio* * *Nyquist Sampling Rate*)

where

*Maximum Hardware I/Q* is the value of the [Maximum Hardware IQ Rate](attr66.html) property

*Oversampling Ratio* is the value of the [Oversampling Ratio](attrd3.html) property

This value is expressed in parts per million (ppm).

For large offset values, with large waveform sizes, clock cycle slips may occur. Clock cycle slips can cause the final waveform size to be different from the expected size, given the ideal burst length and the interframe spacing.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM | "segmentx" |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS , 80211G DSSSOFDM, 80211N MIMOOFDM, 80211AH MIMOOFDM | "" (empty string) |
| 80211AX MIMOOFDM | "segmentx", if you set the PPDU Type property to SU PPDU, Extended Range SU PPDU or MU PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "" (empty string), if you set the PPDU Type property to MU PPDU |
| 80211BE MIMOOFDM | "[userx]", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to MU PPDU |
| 80211BN MIMOOFDM | "[userx]", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |

The default value is 0. Valid values are -1000 to 1000, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sample Clock Offset (ppm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1a.html language=enus -->
## TOPIC 00004: Spectrum Control:Pulse Shaping Filter Type

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1a.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the pulse-shaping filter type to use to ensure that the signal spectrum meets the spectral mask criteria as defined in section 17.3.9.2 of IEEE Standard 802.11a-1999, section 18.4.7.3 of IEEE Standard 802.11b-1999, and section 20.3.21.1 of IEEE Standard 802.11n-2009. The default value is R

### Spectrum Control:Pulse Shaping Filter Type

Specifies the pulse-shaping filter type to use to ensure that the signal spectrum meets the spectral mask criteria as defined in section 17.3.9.2 of *IEEE Standard 802.11a-1999*, section 18.4.7.3 of *IEEE Standard 802.11b-1999*, and section 20.3.21.1 of *IEEE Standard 802.11n-2009*.

The default value is **Rectangular** if you set the [Standard](attr1f.html) property to **80211A/G OFDM**, **80211J OFDM**, **80211G DSSSOFDM**, **80211N MIMOOFDM**, **80211AC MIMOOFDM**, **80211AH MIMOOFDM**, **80211AF MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, or **80211BN MIMOOFDM**.

The default value is **Root Raised Cosine** if you set the Standard property to **80211B/G DSSS**.

The default value is **Raised Cosine** if you set the Standard property to **80211P DSSS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Shaping Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Rectangular | 0 | Generates a rectangular filter that is always one symbol long. |
| --- | --- | --- |
| Raised Cosine | 1 | Generates a filter with a frequency-domain response in the transition band that has the shape of a raised cosine. The filter is defined by a roll-off factor configured using the Pulse Shaping Filter Parameter property. |
| Root Raised Cosine | 2 | Generates a filter with a frequency-domain response in transition band that has the shape of a square root of a raised cosine. The filter is defined by a roll-off factor configured using the Pulse Shaping Filter Parameter property. |
| Gaussian | 3 | Generates a filter with a frequency-domain response and time-domain response that are Gaussian. The filter is defined by the product of 3 dB bandwidth and symbol time, configured using the Pulse Shaping Filter Parameter property. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1b.html language=enus -->
## TOPIC 00005: Spectrum Control:Pulse Shaping Filter Parameter

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1b.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the rolloff factor (alpha) if you set the Pulse Shaping Filter Type property to Raised Cosine or Root Raised Cosine. If you set the Pulse Shaping Filter Type property to Gaussian, you can calculate the Pulse Shaping Filter Parameter property by multiplying B and T, where B is

### Spectrum Control:Pulse Shaping Filter Parameter

Specifies the value of the rolloff factor (alpha) if you set the [Pulse Shaping Filter Type](/csh?topicname=attr1a.html) property to **Raised Cosine** or **Root Raised Cosine**. If you set the Pulse Shaping Filter Type property to **Gaussian**, you can calculate the Pulse Shaping Filter Parameter property by multiplying *B* and *T*, where *B* is the 3 dB bandwidth and *T* is the symbol period for a Gaussian filter.

If you set the Pulse Shaping Filter Type property to **Rectangular**, the WLAN Generation ignores the Pulse Shaping Filter Parameter property.

If you set the Standard property to **80211P OFDM**, the default value is 0.1. In all other instances, the default value is 0.5. Valid values are 0.1 to 0.95, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Shaping Filter Parameter |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1d.html language=enus -->
## TOPIC 00006: Spectrum Control:DSSS Window Length (s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1d.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window length for direct spread spectrum signals If you do not want windowing, set this property to 0. This value is expressed in seconds. This property provides power ramp-up and ramp-down for the entire burst. Refer to the Windowing help topic for more information about windowing for

### Spectrum Control:DSSS Window Length (s)

Specifies the window length for direct spread spectrum signals If you do not want windowing, set this property to 0. This value is expressed in seconds.

This property provides power ramp-up and ramp-down for the entire burst.

Refer to the [Windowing](/csh?context=rfmxwlangen_wlangen_windowing) help topic for more information about windowing for DSSS signals.

The default value is 2 microseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSSS Window Length (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1f.html language=enus -->
## TOPIC 00007: Standard

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr1f.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IEEE 802.11 standard, which indicates the type of physical layer, for signal generation. If you do not select a standard, the WLAN Generation returns an error. Remarks The following table lists the characteristics of this property. Short Name Standard Data type ci32.png Permissions Rea

### Standard

Specifies the IEEE 802.11 standard, which indicates the type of physical layer, for signal generation.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Standard |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Standard |
| Resettable | No |

| 80211A/G OFDM | 0 | Corresponds to the OFDM mode defined in IEEE Standard 802.11a-1999, and the extended rate physical layer-OFDM (ERP-OFDM) mode defined in IEEE Standard 802.11g-2003. |
| --- | --- | --- |
| 80211J OFDM | 7 | Corresponds to the OFDM mode defined in IEEE Standard 802.11j 2004. |
| 80211P OFDM | 8 | Corresponds to the OFDM mode defined in IEEE Standard 802.11p 2010. |
| 80211B/G DSSS | 1 | Corresponds to all the compulsory and optional modes defined in IEEE Standard 802.11b-1999 and the ERP-packet binary convolutional coding (ERP-PBCC) mode defined in IEEE Standard 802.11g-2003. |
| 80211G DSSSOFDM | 2 | Corresponds to the optional direct sequence spread spectrum-OFDM (DSSS-OFDM) mode defined in IEEE Standard 802.11g-2003. |
| 80211N MIMOOFDM | 3 | Corresponds to IEEE Standard 802.11n-2009. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 2.0.0, 3.0.0, 4.0.0, 5.0.0, or 6.0.0. |
| 80211AC MIMOOFDM | 4 | Corresponds to IEEE Standard 802.11ac-2013. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 3.0.0, 4.0.0, 5.0.0, or 6.0.0. |
| 80211AH MIMOOFDM | 5 | Corresponds to IEEE P802.11ah/D1.3. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 3.0.0, 4.0.0, 5.0.0, or 6.0.0. |
| 80211AF MIMOOFDM | 6 | Corresponds to IEEE Standard 802.11af-2013. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 3.0.0, 4.0.0, 5.0.0, or 6.0.0. |
| 80211AX MIMOOFDM | 9 | Corresponds to IEEE P802.11ax/D8.0. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 3.0.0, 4.0.0 , 5.0.0, or 6.0.0. |
| 80211BE MIMOOFDM | 10 | Corresponds to IEEE P802.11be/D7.0. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 3.0.0, 4.0.0 , 5.0.0, or 6.0.0. |
| 80211BN MIMOOFDM | 11 | Corresponds to IEEE P802.11bn/D1.3. To use this option, you must set the toolkit compatibility version parameter on the niWLANG Open Session VI to 3.0.0, 4.0.0 , 5.0.0, or 6.0.0. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr20.html language=enus -->
## TOPIC 00008: Data Rate and Frame Format:OFDM Data Rate (Mbps)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr20.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr20.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data rate for the OFDM payload, as defined in section 17.3.2.2 of IEEE Standard 802.11-2007. This value is expressed in Mbps. Configure this property only when you set the Standard property to 80211A/G OFDM, 80211J OFDM, 80211P OFDM or 80211G DSSSOFDM, or if you set the Non-HT Modulati

### Data Rate and Frame Format:OFDM Data Rate (Mbps)

Specifies the data rate for the OFDM payload, as defined in section 17.3.2.2 of *IEEE Standard 802.11-2007*. This value is expressed in Mbps.

Note

Standard

80211A/G OFDM

80211J OFDM

80211P OFDM

80211G DSSSOFDM

Non-HT Modulation Mode

On

The default value is **6**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM Data Rate (Mbps) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set OFDM Data Rate |
| Resettable | No |

| 6 | 0 | Specifies a data rate of 1.5 Mbps, 3 Mbps, and 6 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| --- | --- | --- |
| 9 | 1 | Specifies a data rate of 2.25 Mbps, 4.5 Mbps, and 9 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| 12 | 2 | Specifies a data rate of 3 Mbps, 6 Mbps, and 12 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| 18 | 3 | Specifies a data rate of 4.5 Mbps, 9 Mbps, and 18 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| 24 | 4 | Specifies a data rate of 6 Mbps, 12 Mbps, and 24 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| 36 | 5 | Specifies a data rate of 9 Mbps, 18 Mbps, and 36 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| 48 | 6 | Specifies a data rate of 12 Mbps, 24 Mbps, and 48 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |
| 54 | 7 | Specifies a data rate of 13.5 Mbps, 27 Mbps, and 54 Mbps for respective channel bandwidths of 5 MHz, 10 MHz, and 20 MHz. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr21.html language=enus -->
## TOPIC 00009: Data Rate and Frame Format:DSSS Data Rate (Mbps)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr21.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr21.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the data rate for the direct sequence spread spectrum (DSSS) payload, as defined in IEEE Standard 802.11b-1999 and the extended rate physical layer-packet binary convolutional coding (ERP-PBCC) mode in IEEE Standard 802.11g-2003. This value is expressed in Mbps. Configure this property onl

### Data Rate and Frame Format:DSSS Data Rate (Mbps)

Specifies the data rate for the direct sequence spread spectrum (DSSS) payload, as defined in *IEEE Standard 802.11b-1999* and the extended rate physical layer-packet binary convolutional coding (ERP-PBCC) mode in *IEEE Standard 802.11g-2003*. This value is expressed in Mbps.

Note

Standard

80211B/G DSSS

The default value is **1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSSS Data Rate (Mbps) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set DSSS Data Rate |
| Resettable | No |

| 1 | 0 | Specifies a data rate of 1 Mbps, as defined in sections 18.4.6.3 and 18.4.6.4 of IEEE Standard 802.11b-1999. |
| --- | --- | --- |
| 2 | 1 | Specifies a data rate of 2 Mbps, as defined in sections 18.4.6.3 and 18.4.6.4 of IEEE Standard 802.11b-1999. |
| 5.5 CCK | 2 | Specifies a data rate of 5.5 Mbps complementary code keying (CCK), as defined in section 18.4.6.5 of IEEE Standard 802.11b-1999. |
| 5.5 PBCC | 3 | Specifies a data rate of 5.5 Mbps PBCC, as defined in section 18.4.6.6 of IEEE Standard 802.11b-1999. |
| 11 CCK | 4 | Specifies a data rate of 11 Mbps CCK, as defined in section 18.4.6.5 of IEEE Standard 802.11b-1999. |
| 11 PBCC | 5 | Specifies a data rate of 11 Mbps PBCC, as defined in section 18.4.6.6 of IEEE Standard 802.11b-1999. |
| 22 | 6 | Specifies a data rate of 22 Mbps, as defined in section 19.3.3.2 of IEEE Standard 802.11g-2003. |
| 33 | 7 | Specifies a data rate of 33 Mbps, as defined in section 19.3.3.2 of IEEE Standard 802.11g-2003. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr23.html language=enus -->
## TOPIC 00010: Hardware Settings:Recommended Settings:IQ Rate (S/s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr23.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended sample rate for the current signal configuration. The dt parameter of the created waveform is the inverse of the recommended sample rate. If you set the use waveform dt for IQ rate? parameter of the niRFSG Write Arb Waveform VI to False, wire the IQ Rate property to the niRFS

### Hardware Settings:Recommended Settings:IQ Rate (S/s)

Returns the recommended sample rate for the current signal configuration. The **dt** parameter of the created waveform is the inverse of the recommended sample rate. If you set the **use waveform dt for IQ rate?** parameter of the niRFSG Write Arb Waveform VI to **False**, wire the IQ Rate property to the niRFSG IQ Rate property. This value is expressed in samples per second.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Rate (S/s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niWLANG Get IQ Rate |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr24.html language=enus -->
## TOPIC 00011: Obsolete:Waveform Scaling Factor

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr24.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr24.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the scaling factor for the waveform, as a percentage of the maximum sample magnitude, to reduce the overshoot associated with the digital-to-analog converter (DAC) interpolation filter and other finite impulse response (FIR) filters in the NI RF vector signal generators. This property is a

### Obsolete:Waveform Scaling Factor

Specifies the scaling factor for the waveform, as a percentage of the maximum sample magnitude, to reduce the overshoot associated with the digital-to-analog converter (DAC) interpolation filter and other finite impulse response (FIR) filters in the NI RF vector signal generators.

Note

toolkit compatibility version

niWLANG Open Session

1.0.0

The default value is 99. Valid values are 1 to 100, inclusive. You can reduce the value to avoid clipping, but you may lose dynamic range.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waveform Scaling Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr25.html language=enus -->
## TOPIC 00012: Advanced:IQ Waveform Size

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr25.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr25.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the size of the generated I/Q waveform. This value is expressed in samples. Remarks The following table lists the characteristics of this property. Short Name IQ Waveform Size Data type ci32.png Permissions Read Only High-level VIs niWLANG Get IQ Waveform Size Resettable No

### Advanced:IQ Waveform Size

Returns the size of the generated I/Q waveform. This value is expressed in samples.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Waveform Size |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niWLANG Get IQ Waveform Size |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr28.html language=enus -->
## TOPIC 00013: Hardware Settings:Headroom (dB)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr28.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr28.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the headroom per transmit channel. This value represents the maximum peak-to-average power ratio (PAPR) allowed in the generated signal. This value is expressed in dB. the WLAN Generation clips any portion of the signal that exceeds the peak power corresponding to this value. the WLAN Gene

### Hardware Settings:Headroom (dB)

Specifies the headroom per transmit channel. This value represents the maximum peak-to-average power ratio (PAPR) allowed in the generated signal. This value is expressed in dB.

the WLAN Generation clips any portion of the signal that exceeds the peak power corresponding to this value. the WLAN Generation ignores this property if you set the [Auto Headroom Enabled](attr57.html) property to **True**. If you set the Auto Headroom Enabled property to **False** and you do not specify the headroom property the WLAN Generation uses default values based on the [Standard](attr1f.html) property.

If you set the Standard property to **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM**, the headroom applied on the signal with respect to the average power computed is based on the [Average Power Reference](attraa.html) property.

Note

Note

False

3.0.0

4.0.0

5.0.0

6.0.0

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "channelx" |
| 80211AF MIMOOFDM, 80211AX MIMOOFDM | "[segmenty/]channelx" ("segment0/" is optional if the Number of Segments property is set to 1) |
| 80211AC MIMOOFDM | "[segmenty/]channelx" ("[segment0/]" is optional if the Number of Segments property is set to 1) |
| "channelx" when the Multi-segment Generation Mode property is set to Single Generator |  |

If you set the Standard property to **80211B/G DSSS**, the default value is 5. Otherwise, the default value is 12.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Headroom (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Headroom |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr29.html language=enus -->
## TOPIC 00014: Data Rate and Frame Format:MCS Index

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr29.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr29.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the modulation and coding scheme (MCS) index. The MCS index is a compact representation that determines the modulation scheme, coding rate, and number of spatial streams, as specified in section 20.3.5 of IEEE Standard 802.11n-2009, section 22.5 of IEEE Standard 802.11ac-2013,

### Data Rate and Frame Format:MCS Index

Specifies the value of the modulation and coding scheme (MCS) index. The MCS index is a compact representation that determines the modulation scheme, coding rate, and number of spatial streams, as specified in section 20.3.5 of *IEEE Standard 802.11n-2009*, section 22.5 of *IEEE Standard 802.11ac-2013*, section 24.5 of *IEEE P802.11ah/D1.3*, section 23.5 of *IEEE Standard 802.11af-2013*, section 27.5 of *IEEE P802.11ax/D8.0*, and section 36.5 of *IEEE P802.11be/D7.0*.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM | "" (empty string) |
| 80211AC MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU |
| 80211AC MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU |
| 80211AX MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BE MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |

The default value is 0. For **80211AC MIMOOFDM**, valid values are 0 to 11, inclusive. For **80211BE MIMOOFDM**, valid values are 0 to 15, inclusive. For **80211AX MIMOOFDM**, valid values are 0 to 13, inclusive. For **80211N MIMOOFDM**, valid values are 0 to 32, inclusive. For **80211AH MIMOOFDM**, valid values are 0 to 10, inclusive. For **80211AF MIMOOFDM**, valid values are 0 to 9, inclusive. For **80211BN MIMOOFDM**, valid values are 0 to 15, inclusive and 17, 19, 20 and 23.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MCS Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set MCS Index |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2a.html language=enus -->
## TOPIC 00015: Channel Bandwidth (Hz)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2a.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel width used for transmitting the signal. This value is expressed in Hz. The valid values are shown in the following table. Standard Property Value Channel Bandwidth (MHz) 80211A/G OFDM 20 80211J OFDM 10 or 20 80211P OFDM 5, 10 or 20 80211N MIMOOFDM 20 or 40 80211AC MIMOOFDM 20,

### Channel Bandwidth (Hz)

Specifies the channel width used for transmitting the signal. This value is expressed in Hz.

The valid values are shown in the following table.

| Standard Property Value | Channel Bandwidth (MHz) |
| --- | --- |
| 80211A/G OFDM | 20 |
| 80211J OFDM | 10 or 20 |
| 80211P OFDM | 5, 10 or 20 |
| 80211N MIMOOFDM | 20 or 40 |
| 80211AC MIMOOFDM | 20, 40, 80, or 160 |
| 80211AX MIMOOFDM | 20, 40, 80, or 160 |
| 80211BE MIMOOFDM | 20, 40, 80, 160, or 320 |
| 80211BN MIMOOFDM | 20, 40, 80, 160, or 320 |
| 80211AH MIMOOFDM | 1, 2, 4, 8, or 16 |
| 80211AF MIMOOFDM | 6, 7, or 8 |

For OFDM signals, channel bandwidth determines the number of pilot and data subcarriers used. the WLAN Generation ignores the Channel Bandwidth property for other values of the [Standard](attr1f.html) property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Bandwidth (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Channel Bandwidth |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2b.html language=enus -->
## TOPIC 00016: Data Rate and Frame Format:80211n PLCP Frame Format

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2b.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the format of the physical layer convergence protocol (PLCP) frame structure. The frame structure determines the arrangement of preambles, header (SIGNAL field), and payload in a frame, as defined in section 20.3.2 of IEEE Standard 802.11n-2009. The default value is Mixed Format. Remarks T

### Data Rate and Frame Format:80211n PLCP Frame Format

Specifies the format of the physical layer convergence protocol (PLCP) frame structure. The frame structure determines the arrangement of preambles, header (SIGNAL field), and payload in a frame, as defined in section 20.3.2 of *IEEE Standard 802.11n-2009*.

The default value is **Mixed Format**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 80211n PLCP Frame Format |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set PLCP Frame Format (802 11N) |
| Resettable | No |

| Mixed Format | 0 | Specifies that the PLCP frame structure consists of non-high throughput (HT) preamble and header (SIGNAL field) followed by HT header, preambles, and payload as specified in IEEE Standard 802.11n-2009. |
| --- | --- | --- |
| Greenfield Format | 1 | Specifies that the PLCP frame structure does not support non-HT and that it starts with HT preamble, followed by HT SIGNAL field and payload. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2e.html language=enus -->
## TOPIC 00017: MIMO:Number of Extension Spatial Streams

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2e.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of extension spatial streams (NESS ) as defined in section 20.3.9.4.6 of IEEE Standard 802.11n-2009. The value of NESS follows the definition shown in the following equation: NSTS + NESS ≤ NTx where NSTS is the number of space-time streams and is determined by the MCS index and

### MIMO:Number of Extension Spatial Streams

Specifies the number of extension spatial streams (*NESS*) as defined in section 20.3.9.4.6 of *IEEE Standard 802.11n-2009*.

The value of *NESS* follows the definition shown in the following equation: *NSTS* + *NESS* ≤ *NTx*

| where | NSTS is the number of space-time streams and is determined by the MCS index and STBC index |
| --- | --- |
|  | NTx is the number of transmit channels specified by the Number of Transmit Channels property |

The default value is 0. Valid values are 0 to 3, inclusive.

Note

NTx

NSTS

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Extension Spatial Streams |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2f.html language=enus -->
## TOPIC 00018: MIMO:Number of Transmit Channels

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr2f.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of IEEE Standard 802.11n-2009. If you set the Mapping Matrix Type property to Direct, the number of transmit channels must be equal to the number of space-time streams. If you se

### MIMO:Number of Transmit Channels

Specifies the number of transmit channels for multiple input multiple output (MIMO) signals, as defined in section 20.3.3 of *IEEE Standard 802.11n-2009*.

If you set the [Mapping Matrix Type](attr37.html) property to **Direct**, the number of transmit channels must be equal to the number of space-time streams. If you set the Mapping Matrix Type property to values other than **Direct**, the number of transmit channels must be greater than or equal to the sum of the number of space-time streams and the [Number of Extension Spatial Streams](attr2e.html) property. the WLAN Generation defines the number of space-time streams using the [MCS Index](attr29.html) property and the [STBC Index](attr31.html) property, as specified in *IEEE Standard 802.11n-2009*.

If you set the [Standard](attr1f.html) property to **80211A/G OFDM**, **80211J OFDM**, **80211P OFDM**, **80211B/G DSSS**, or **80211G DSSSOFDM** and the Number of Transmit Channels property to greater than one, the same waveform is generated on multiple RFSG devices inside the [niWLANG RFSG Create and Download Waveforms (Multiple Channel)](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_create_and_download_waveform) VI.

The default value is 1. If you set the Standard property to **80211N MIMOOFDM** or **80211AH MIMOOFDM**, the valid values are 1 to 4, inclusive. If you set the Standard property to any other value, the valid values are 1 to 8, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Transmit Channels |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Number of Transmit Channels |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr30.html language=enus -->
## TOPIC 00019: Active Channel

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr30.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr30.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active channel string used to access all subsequent properties in a property node until a new active channel is specified. If the property you want to use is channel-specific, you must first select the Active Channel property and then pass the name of the specific channel. If you speci

### Active Channel

Specifies the [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string used to access all subsequent properties in a property node until a new active channel is specified.

If the property you want to use is channel-specific, you must first select the Active Channel property and then pass the name of the specific channel. If you specify an active channel for a property that is not channel-specific, the WLAN Generation returns an error.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Active Channel |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr31.html language=enus -->
## TOPIC 00020: MIMO:STBC Index

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr31.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the difference between the number of space-time streams and the number of spatial streams, as defined in section 20.3.9.4.3 of IEEE Standard 802.11n-2009. the WLAN Generation derives the number of spatial streams from the specified value of the MCS Index property. Different space-time codi

### MIMO:STBC Index

Specifies the difference between the number of space-time streams and the number of spatial streams, as defined in section 20.3.9.4.3 of *IEEE Standard 802.11n-2009*. the WLAN Generation derives the number of spatial streams from the specified value of the [MCS Index](/csh?topicname=attr29.html) property. Different space-time coding schemes are defined in section 20.3.11.8.1 of *IEEE Standard 802.11n-2009*.

The default value is 0. Valid values are 0 to 2, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | STBC Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set STBC Index |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr35.html language=enus -->
## TOPIC 00021: Payload:MAC Header:QoS Control Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr35.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr35.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the QoS Control field of the medium access control (MAC) header. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOF

### Payload:MAC Header:QoS Control Enabled

Specifies whether to enable the QoS Control field of the medium access control (MAC) header.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

Note

MAC Frame Format

Short

The default value is **False**.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header QoS Control Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the QoS Control field of the MAC header. |
| --- | --- | --- |
| True | 1 | Enables the QoS Control field of the MAC header. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr3b.html language=enus -->
## TOPIC 00022: Payload:MAC Header:Address1 Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr3b.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Address1 field of the medium access control (MAC) header. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM

### Payload:MAC Header:Address1 Enabled

Specifies whether to enable the Address1 field of the medium access control (MAC) header.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Address1 Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the Address1 field of the MAC header. |
| --- | --- | --- |
| True | 1 | Enables the Address1 field of the MAC header. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr3c.html language=enus -->
## TOPIC 00023: Payload:MAC Header:Address1

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr3c.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Address1 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/

### Payload:MAC Header:Address1

Specifies the Address1 field as defined in section 7.1.3 of *IEEE Standard 802.11-2007* and *IEEE Standard 802.11n-2009*, section 8.2.4 of *IEEE Standard 802.11ac-2013* and *IEEE P802.11ah/D1.3*, section 9.2.4 of *IEEE P802.11ax/D8.0*, section 9.2.4 of *IEEE P802.11be/D7.0*, and section 9.2.4 of *IEEE P802.11bn/D1.3*. The length of this field is defined by the [Address1 Length](/csh?context=rfmxwlangen_lvwlangenprop_attr79) property if you set the [MAC Frame Format](/csh?context=rfmxwlangen_lvwlangenprop_attr78) property to **Short**. In all other instances, the length of this field is six bytes. If this field is a MAC address, it is represented with the least significant byte in the leftmost position, and each byte is represented with the least significant bit in the rightmost position.

For example, the medium access control (MAC) address 12-34-56-78-9A-BC is represented by the number 0 x 123456789ABC.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant six bytes.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Address1 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4.html language=enus -->
## TOPIC 00024: Data Rate and Frame Format:DSSS Preamble Type

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use a long or short preamble for direct sequence spread spectrum (DSSS) and DSSS-OFDM packets, as defined in IEEE Standard 802.11b-1999. Configure this property only if you set the Standard property to 80211B/G DSSS or 80211G DSSSOFDM. The default value is Long Preamble. Remarks

### Data Rate and Frame Format:DSSS Preamble Type

Specifies whether to use a long or short preamble for direct sequence spread spectrum (DSSS) and DSSS-OFDM packets, as defined in *IEEE Standard 802.11b-1999*.

Note

Standard

80211B/G DSSS

80211G DSSSOFDM

The default value is **Long Preamble**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DSSS Preamble Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set DSSS Preamble Type |
| Resettable | No |

| Short Preamble | 0 | Uses a short preamble as defined in section 18.2.2.2 of IEEE Standard 802.11b-1999. |
| --- | --- | --- |
| Long Preamble | 1 | Uses a long preamble as defined in section 18.2.2.1 of IEEE Standard 802.11b-1999. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr40.html language=enus -->
## TOPIC 00025: Payload:MAC Header:Address3

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr40.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr40.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the six-byte Address3 field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P

### Payload:MAC Header:Address3

Specifies the six-byte Address3 field as defined in section 7.1.3 of *IEEE Standard 802.11-2007* and *IEEE Standard 802.11n-2009*, section 8.2.4 of *IEEE Standard 802.11ac-2013* and *IEEE P802.11ah/D1.3*, section 9.2.4 of *IEEE P802.11ax/D8.0*, section 9.2.4 of *IEEE P802.11be/D7.0*, and section 9.2.4 of *IEEE P802.11bn/D1.3*. This field is represented with the least significant byte in the leftmost position, and each byte is represented with the least significant bit in the rightmost position.

For example, the medium access control (MAC) address 12-34-56-78-9A-BC is represented by the number 0x123456789ABC.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant six bytes.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Address3 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr41.html language=enus -->
## TOPIC 00026: Payload:MAC Header:Sequence Control Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr41.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr41.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Sequence Control field of the medium access control (MAC) header. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G D

### Payload:MAC Header:Sequence Control Enabled

Specifies whether to enable the Sequence Control field of the medium access control (MAC) header.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

The default value is **True**.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Sequence Control Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the Sequence Control field of the MAC header. |
| --- | --- | --- |
| True | 1 | Enables the Sequence Control of the MAC header. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr43.html language=enus -->
## TOPIC 00027: Payload:MAC Header:Address4 Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr43.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr43.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Address4 field of the medium access control (MAC) header. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM

### Payload:MAC Header:Address4 Enabled

Specifies whether to enable the Address4 field of the medium access control (MAC) header.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

The default value is **True**.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Address4 Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the Address4 field of the MAC header. |
| --- | --- | --- |
| True | 1 | Enables the Address4 field of the MAC header. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr47.html language=enus -->
## TOPIC 00028: Payload:MAC Header:QoS Control

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr47.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr47.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the two-byte QoS Control field as defined in section 7.1.3 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEE

### Payload:MAC Header:QoS Control

Specifies the two-byte QoS Control field as defined in section 7.1.3 of *IEEE Standard 802.11-2007* and *IEEE Standard 802.11n-2009*, section 8.2.4 of *IEEE Standard 802.11ac-2013* and *IEEE P802.11ah/D1.3*, section 9.2.4 of *IEEE P802.11ax/D8.0*, section 9.2.4 of *IEEE P802.11be/D7.0*, and section 9.2.4 of *IEEE P802.11bn/D1.3*. This field is represented with the least significant bit in the rightmost position.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

Note

MAC Frame Format

Short

The default value is 0x0. Valid values are 0x0 to 0xFFFF. For values outside this range, the WLAN Generation uses the least significant two bytes.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header QoS Control |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr48.html language=enus -->
## TOPIC 00029: Payload:MAC Header:HT Control Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr48.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr48.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the HT Control field of the medium access control (MAC) header. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFD

### Payload:MAC Header:HT Control Enabled

Specifies whether to enable the HT Control field of the medium access control (MAC) header.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

Note

MAC Frame Format

Short

MAC Frame Type

Trigger Frame

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header HT Control Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the HT Control field of the MAC header. |
| --- | --- | --- |
| True | 1 | Enables the HT Control field of the MAC header. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr49.html language=enus -->
## TOPIC 00030: Payload:MAC Header:HT Control

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr49.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr49.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the four-byte HT Control field as defined in section 7.1.3 of IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013 and IEEE P802.11ah/D1.3, section 9.2.4 of IEEE P802.11ax/D8.0, section 9.2.4 of IEEE P802.11be/D7.0, and section 9.2.4 of IEEE P802.11bn/D1.3. This field i

### Payload:MAC Header:HT Control

Specifies the four-byte HT Control field as defined in section 7.1.3 of *IEEE Standard 802.11n-2009*, section 8.2.4 of *IEEE Standard 802.11ac-2013* and *IEEE P802.11ah/D1.3*, section 9.2.4 of *IEEE P802.11ax/D8.0*, section 9.2.4 of *IEEE P802.11be/D7.0*, and section 9.2.4 of *IEEE P802.11bn/D1.3*. This field is represented with the least significant bit in the rightmost position.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

Note

MAC Frame Format

Short

The default value is 0x0. Valid values are 0x0 to 0xFFFFFFFF. For values outside this range, the WLAN Generation uses the least significant four bytes.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header HT Control |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4a.html language=enus -->
## TOPIC 00031: Spectrum Control:Windowing Method

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4a.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method of applying window to the baseband signal if the Standard property is set to 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211G DSSSOFDM, 80211N MIMOOFDM, 80211AC MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM, 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM. This property is

### Spectrum Control:Windowing Method

Specifies the method of applying window to the baseband signal if the [Standard](/csh?topicname=attr1f.html) property is set to **80211A/G OFDM**, **80211J OFDM**, **80211P OFDM**, **80211G DSSSOFDM**, **80211N MIMOOFDM**, **80211AC MIMOOFDM**, **80211AH MIMOOFDM**, **80211AF MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, or **80211BN MIMOOFDM**. This property is ignored if the Standard property is set to **80211B/G DSSS**.

Refer to the [Windowing](/csh?context=rfmxwlangen_wlangen_windowing) topic for more information about windowing for OFDM signals.

The default value is **Centered At Symbol Boundary**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Windowing Method |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Centered At Symbol Boundary | 0 | Specifies that the window is applied with its center at the boundary between two OFDM symbols. |
| --- | --- | --- |
| Starting At Symbol Boundary | 1 | Specifies that the window is applied with its starting position at the boundary between two OFDM symbols. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4b.html language=enus -->
## TOPIC 00032: MIMO:Number of Segments

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4b.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of frequency segments for 802.11ac or 802.11ax signals. For 80 MHz + 80 MHz transmission of 802.11ac or 802.11ax signals, set this property to 2 and the Channel Bandwidth property to 80 MHz. The default value is 1. Remarks The following table lists the characteristics of this pr

### MIMO:Number of Segments

Specifies the number of frequency segments for 802.11ac or 802.11ax signals.

For 80 MHz + 80 MHz transmission of 802.11ac or 802.11ax signals, set this property to 2 and the [Channel Bandwidth](attr2a.html) property to 80 MHz.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Segments |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Number of Segments |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4c.html language=enus -->
## TOPIC 00033: MIMO:Number of Space Time Streams

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4c.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of space-time streams into which the data is divided. You must use the following active channel string formats to set this property. Standard Property Value Active Channel String Format 80211AC MIMOOFDM "" (empty string), if you set the PPDU Type property to SU PPDU 80211AC MIMO

### MIMO:Number of Space Time Streams

Specifies the number of space-time streams into which the data is divided.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to set this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211AC MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU |
| 80211AC MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU |
| 80211AX MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM | "" (empty string) |
| 80211BE MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BE MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU |

The default value is 1. The valid values for this property are as follows:

| Standard Property Value | Valid Values(Inclusive) |
| --- | --- |
| 80211N MIMOOFDM | 1 to 4 |
| 80211AC MIMOFDM | 1 to 8, if you set the PPDU Type property to SU PPDU |
| 80211AC MIMOFDM | 1 to 4, if you set the PPDU Type property to MU PPDU |
| 80211AX MIMOFDM | 1 to 8, if you set the PPDU Type property to SU PPDU |
| 80211AX MIMOFDM | 1 to 4, if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211AX MIMOFDM | 1 to 2, if you set the PPDU Type property to Extended Range SU PPDU |
| 80211BE MIMOFDM | 1 to 8, if you set the PPDU Type property to MU PPDU, SIG Compression Enabled property to True, and Number of Users property to 1. |
| 80211BE MIMOFDM | 1 to 4, if you set the PPDU Type property to MU PPDU and Number of Users property greater than 1. |
| 80211BN MIMOFDM | 1 to 8, if you set the PPDU Type property to MU PPDU, SIG Compression Enabled property to True, and Number of Users property to 1. |
| 80211BN MIMOFDM | 1 to 4, if you set the PPDU Type property to MU PPDU and Number of Users property greater than 1. |
| 80211BN MIMOFDM | 1, if you set the PPDU Type property to ELR PPDU. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Space Time Streams |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Number of Space Time Streams |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4d.html language=enus -->
## TOPIC 00034: MIMO:STBC All Streams Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4d.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether space-time block coding (STBC) is performed at the transmitter when the Standard property is set to 80211AC MIMOOFDM or 80211AX MIMOOFDM. Whenever STBC is performed, the number of space-time streams is equal to two times the number of spatial streams. The default value is False. Re

### MIMO:STBC All Streams Enabled

Specifies whether space-time block coding (STBC) is performed at the transmitter when the [Standard](/csh?topicname=attr1f.html) property is set to **80211AC MIMOOFDM** or **80211AX MIMOOFDM**. Whenever STBC is performed, the number of space-time streams is equal to two times the number of spatial streams.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | STBC All Streams Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Specifies that STBC is not performed at the transmitter. |
| --- | --- | --- |
| True | 1 | Specifies that STBC is performed at the transmitter. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4e.html language=enus -->
## TOPIC 00035: Advanced:Swap I and Q Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4e.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to swap the data in the I and Q streams. The default value is False. Remarks The following table lists the characteristics of this property. Short Name Swap I and Q Enabled Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No False 0 Specifies that the WLAN Ge

### Advanced:Swap I and Q Enabled

Specifies whether to swap the data in the I and Q streams.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Swap I and Q Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Specifies that the WLAN Generation does not swap the data in the I and Q streams. |
| --- | --- | --- |
| True | 1 | Specifies that the WLAN Generation swaps the data in the I and Q streams. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4f.html language=enus -->
## TOPIC 00036: Impairments:IQ Impairments:Timing Skew (s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr4f.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the difference between the sampling instants of I and Q streams. This value is expressed in seconds. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B DSSS, 80211G DSSSOFDM "" (empty string) 80211N MIMOOFDM, 80211AH MIMOOFDM "channelx" 802

### Impairments:IQ Impairments:Timing Skew (s)

Specifies the difference between the sampling instants of I and Q streams. This value is expressed in seconds.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx" |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM | "segmentx/channely" |
| 80211AX MIMOOFDM | "segmentx/channely", if you set the PPDU Type property to SU PPDU, Extended Range SU PPDU or MU PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty/channelz", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "channelx", if you set the PPDU Type property to MU PPDU |
| 80211BE MIMOOFDM | "[userx]/channely", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "channelx", if you set the PPDU Type property to MU PPDU or ELR PPDU |
| 80211BN MIMOOFDM | "[userx]/channely", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |

The default value is 0. Valid values are -1 microsecond to 1 microsecond, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Timing Skew (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5.html language=enus -->
## TOPIC 00037: Payload:Data Length (bytes)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the payload, excluding the lengths of the medium access control (MAC) header and frame check sequence (FCS). The payload length encoded into the physical layer (PHY) header is the sum of the payload data length and the lengths of the MAC header and FCS. This value is expresse

### Payload:Data Length (bytes)

Specifies the length of the payload, excluding the lengths of the medium access control (MAC) header and frame check sequence (FCS). The payload length encoded into the physical layer (PHY) header is the sum of the payload data length and the lengths of the MAC header and FCS. This value is expressed in bytes.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "" (empty string), if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "userx", if you set the A-MPDU Enabled property to False and use the niWLANG Create Trigger Frame MSDU VI to generate the trigger frame |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BE MIMOOFDM | "userx", if you set the A-MPDU Enabled property to False and use the niWLANG Create Trigger Frame MSDU VI to generate the trigger frame |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "userx", if you set the A-MPDU Enabled property to False and use the niWLANG Create Trigger Frame MSDU VI to generate the trigger frame |

The default values are as follows:

- If you set the Standard property to 80211N MIMOOFDM and the A-MPDU Enabled property to True , the default value is 1,024, the limits on MPDU length are 0 to 4,095 (inclusive), and the limits on PSDU length are 0 to 65,535 (inclusive).
- If you set the Standard property to 80211N MIMOOFDM and the A-MPDU Enabled property to False , the default value is 4,096 and the limits on PSDU length are 0 to 65,535 (inclusive).
- If you set the Standard property to 80211AC MIMOOFDM and the A-MPDU Enabled property to True , the default value is 4,096, the limits on MPDU length are 0 to 16,383 (inclusive), and the limits on PSDU length are 0 to 46,92,480 (inclusive).
- If you set the Standard property to 80211AC MIMOOFDM and the A-MPDU Enabled property to False , the default value is 4,096, and the limits on PSDU length are 0 to 4692480 (inclusive).
- If you set the Standard property to 80211AH MIMOOFDM and the A-MPDU Enabled property to True , the default value is 256, the limits on MPDU length are 0 to 16,383 (inclusive), and the limits on PSDU length are 0 to 7,97,159 (inclusive).
- If you set the Standard property to 80211AH MIMOOFDM and the A-MPDU Enabled property to False , the default value is 256, and the limits on PSDU length are 0 to 511 (inclusive).
- If you set the Standard property to 80211AF MIMOOFDM and the A-MPDU Enabled property to True , the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive), and the limits on PSDU length are 0 to 1,065,600 (inclusive).
- If you set the Standard property to 80211AF MIMOOFDM and the A-MPDU Enabled property to False , the default value is 4096, and the limits on PSDU length are 0 to 1,065,600 (inclusive).
- If you set the Standard property to 80211AX MIMOOFDM and the A-MPDU Enabled property to True , the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive), and the limits on PSDU length are 0 to 65,00,631 (inclusive).
- If you set the Standard property to 80211AX MIMOOFDM and the A-MPDU Enabled property to False , the default value is 4096, and the limits on PSDU length are 0 to 65,00,631 (inclusive).
- If you set the Standard property to 80211BE MIMOOFDM and the A-MPDU Enabled property to True , the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive), and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).
- If you set the Standard property to 80211BE MIMOOFDM and the A-MPDU Enabled property to False , the default value is 4096, and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).
- If you set the Standard property to 80211BN MIMOOFDM and the A-MPDU Enabled property to True , the default value is 4096, the limits on MPDU length are 0 to 16,383 (inclusive), and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).
- If you set the Standard property to 80211BN MIMOOFDM and the A-MPDU Enabled property to False , the default value is 4096, and the limits on PSDU length are 0 to 1,55,23,198 (inclusive).

If you set the Standard property to any other value, the default value is 1,024, and valid values are 0 to 4,095 (inclusive).

the WLAN Generation ignores this property, if you set the [Auto Data Length](attrb3.html) property to **L-SIG Length or Frame Duration**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Payload Data Length (bytes) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr50.html language=enus -->
## TOPIC 00038: Payload:MAC Header:Sequence Control:Sequence Number Increment Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr50.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr50.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to increment the sequence number in a sequence of frames. The default value is False. the WLAN Generation ignores this property if you set the MAC Frame Type property to Trigger Frame. Remarks The following table lists the characteristics of this property. Short Name MAC Header Seq

### Payload:MAC Header:Sequence Control:Sequence Number Increment Enabled

Specifies whether to increment the sequence number in a sequence of frames.

The default value is **False**.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Seq Num Increment Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Does not increment the sequence number. |
| --- | --- | --- |
| True | 1 | Increments the sequence number. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr51.html language=enus -->
## TOPIC 00039: Payload:MAC Header:Sequence Control:Sequence Number Increment Interval (frames)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr51.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr51.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of frames after which the sequence number is incremented by 1. The starting number is the value represented by the sequence number sub-field of the Sequence Control field. The sequence number is wrapped to 0 after reaching the value 4,095 or (2^12 -1). The default value is 1. Va

### Payload:MAC Header:Sequence Control:Sequence Number Increment Interval (frames)

Specifies the number of frames after which the sequence number is incremented by 1. The starting number is the value represented by the sequence number sub-field of the Sequence Control field. The sequence number is wrapped to 0 after reaching the value 4,095 or (2<sup>12</sup> -1).

The default value is 1. Valid values are 0 to 4,095 (inclusive).

the WLAN Generation ignores this property if you set the [MAC Header Seq Num Increment Enabled](attr50.html) property to **False** and the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Seq Num Increment Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr52.html language=enus -->
## TOPIC 00040: Payload:MAC Header:Sequence Control:Fragment Number Increment Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr52.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr52.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to increment the fragment number in a sequence of frames. The starting number is the value represented by the fragment number sub-field of the MAC Header Sequence Control property. If you set the MAC Header Frag Num Increment Enabled property to True, the WLAN Generation increments

### Payload:MAC Header:Sequence Control:Fragment Number Increment Enabled

Specifies whether to increment the fragment number in a sequence of frames. The starting number is the value represented by the fragment number sub-field of the [MAC Header Sequence Control](/csh?topicname=attr42.html) property. If you set the MAC Header Frag Num Increment Enabled property to **True**, the WLAN Generation increments the fragment number by 1 for every successive frame having the same sequence number. The fragment number wraps to the starting number when the sequence number increments. The fragment number wraps to 0 after reaching the value 15.

The default value is **False**.

the WLAN Generation ignores this property if you set the [MAC Frame Type](attrbc.html) property to **Trigger Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Header Frag Num Increment Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Does not increment the fragment number. |
| --- | --- | --- |
| True | 1 | Increments the fragment number. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr53.html language=enus -->
## TOPIC 00041: Payload:MPDU Length (bytes)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr53.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr53.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the length of the medium access control (MAC) protocol data unit (MPDU). An MPDU comprises of a MAC header, a frame body, and a frame check sequence (FCS). The MPDU Length property is the sum of the length of MAC header, the value of the Payload Data Length property, and the length of FCS, w

### Payload:MPDU Length (bytes)

Returns the length of the medium access control (MAC) protocol data unit (MPDU). An MPDU comprises of a MAC header, a frame body, and a frame check sequence (FCS). The MPDU Length property is the sum of the length of MAC header, the value of the [Payload Data Length](/csh?topicname=attr5.html) property, and the length of FCS, which is equal to four bytes. If you disable the [MAC Header Enabled](/csh?topicname=attrb.html) and [MAC FCS Enabled](/csh?topicname=attr64.html) properties, the lengths of MAC header and FCS are zero. This value is expressed in bytes.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to query this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MPDU Length (bytes) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr56.html language=enus -->
## TOPIC 00042: Data Rate and Frame Format:Not Sounding Bit

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr56.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr56.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the Not Sounding field of the HT-SIG field when you set the Standard property to 80211N MIMOOFDM. For more information about Not Sounding Bit, refer to section 20.3.9.4.3 of IEEE Standard 802.11n-2009. The default value is 1. Valid values are 0 or 1. Remarks The following tabl

### Data Rate and Frame Format:Not Sounding Bit

Specifies the value of the Not Sounding field of the HT-SIG field when you set the [Standard](/csh?topicname=attr1f.html) property to **80211N MIMOOFDM**. For more information about Not Sounding Bit, refer to section 20.3.9.4.3 of *IEEE Standard 802.11n-2009*.

The default value is 1. Valid values are 0 or 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Not Sounding Bit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr57.html language=enus -->
## TOPIC 00043: Hardware Settings:Auto Headroom Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr57.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr57.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the WLAN Generation calculates the headroom or uses the value that you specify. For multiframe generation, the WLAN Generation uses the headroom calculated on the first frame to scale the waveform for every frame. NI recommends that you do not set this property to True for multifra

### Hardware Settings:Auto Headroom Enabled

Specifies whether the WLAN Generation calculates the headroom or uses the value that you specify. For multiframe generation, the WLAN Generation uses the headroom calculated on the first frame to scale the waveform for every frame. NI recommends that you do not set this property to **True** for multiframe generation because variation of the peak-to-average power ratio (PAPR) across frames may lead to excessive clipping. To avoid excessive clipping, set this property to **False** and use the default values for the [Headroom](/csh?topicname=attr28.html) property.

Note

toolkit compatibility version

niWLANG Open Session

3.0.0

4.0.0

5.0.0

6.0.0

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Headroom Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Auto Headroom Enabled |
| Resettable | No |

| False | 0 | Specifies that the WLAN Generation uses the headroom that you specify in the Headroom property. |
| --- | --- | --- |
| True | 1 | Specifies that the WLAN Generation calculates the headroom automatically. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr58.html language=enus -->
## TOPIC 00044: Hardware Settings:Recommended Settings:Actual Headroom (dB)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr58.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr58.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the actual headroom that the WLAN Generation applies to the waveform. Use an active channel string to query this property for a transmit channel. This value is expressed in dB. You must use the following active channel string formats to query this property. Standard Property Value Active Cha

### Hardware Settings:Recommended Settings:Actual Headroom (dB)

Returns the actual headroom that the WLAN Generation applies to the waveform. Use an [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string to query this property for a transmit channel. This value is expressed in dB.

You must use the following active channel string formats to query this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "channelx" |
| 80211AF MIMOOFDM, 80211AX MIMOOFDM | "[segmenty/]channelx" ("segment0/" is optional if the Number of Segments property is set to 1) |
| 80211AC MIMOOFDM | "[segmenty/]channelx" ("[segment0/]" is optional if the Number of Segments property is set to 1) |
| "channelx" when the Multi-segment Generation Mode property is set to Single Generator |  |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Actual Headroom (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | niWLANG Get Actual Headroom |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr59.html language=enus -->
## TOPIC 00045: Data Rate and Frame Format:Actual OFDM Data Rate (Mbps)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr59.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr59.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the OFDM data rate depending upon the values of the Channel Bandwidth and OFDM Data Rate properties. This query is only successful if you set the Standard property to 80211A/G OFDM, 80211J OFDM, 80211P OFDM or 80211G DSSSOFDM, or if you set the Non-HT Modulation Mode property to On. For more

### Data Rate and Frame Format:Actual OFDM Data Rate (Mbps)

Returns the OFDM data rate depending upon the values of the [Channel Bandwidth](/csh?topicname=attr2a.html) and [OFDM Data Rate](/csh?topicname=attr20.html) properties. This query is only successful if you set the [Standard](/csh?topicname=attr1f.html) property to **80211A/G OFDM**, **80211J OFDM**, **80211P OFDM** or **80211G DSSSOFDM**, or if you set the [Non-HT Modulation Mode](/csh?topicname=attr7f.html) property to **On**. For more information about the OFDM data rate, refer to section 17.2.3.3 of *IEEE Standard 802.11-2007*. This value is expressed in Mbps.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Actual OFDM Data Rate (Mbps) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5a.html language=enus -->
## TOPIC 00046: Hardware Settings:RF Blanking Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5a.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable RF blanking. If you want to attenuate the RF OUT signal during the idle interval, set this property to True. This behavior prevents any DC leakage from the local oscillator of the signal generator from appearing at the RF OUT signal. RF blanking attenuates the RF OUT sign

### Hardware Settings:RF Blanking Enabled

Specifies whether to enable RF blanking.

If you want to attenuate the RF OUT signal during the idle interval, set this property to **True**. This behavior prevents any DC leakage from the local oscillator of the signal generator from appearing at the RF OUT signal. RF blanking attenuates the RF OUT signal of signal generators quickly.

For more information about RF blanking, refer to the [Burst Start Locations](attrae.html) property, the [Burst Stop Locations](attrae.html) property, the [niWLANG RFSG Create and Download Waveform](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_create_and_download_waveform) VI, and the [niWLANG RFSG Configure Script](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_configure_script) VI.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Blanking Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Specifies that the WLAN Generation does not enable RF blanking. |
| --- | --- | --- |
| True | 1 | Specifies that the WLAN Generation enables RF blanking. If you select this option, the WLAN Generation completes the following actions: the WLAN Generation returns the value of the RF Blanking Marker Positions property. the WLAN Generation queries the burst start locations and the burst stop locations to get marker positions that can be used to toggle the state of RF blanking. These marker positions are generated such that RF blanking is ON during the idle interval. The niWLANG RFSG Create and Download Waveform VI sets the niRFSG RF Blanking Source property to "marker0", if it is not set already. The niWLANG RFSG Configure Script VI modifies the input from the script parameter to specify marker events. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5b.html language=enus -->
## TOPIC 00047: Hardware Settings:Recommended Settings:RF Blanking Marker Positions []

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5b.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of sample positions of marker events, which are used to toggle the state of RF blanking, within the waveform. The marker positions are such that RF blanking is enabled during the idle interval. This property is applicable only if you set the RF Blanking Enabled property to True. Th

### Hardware Settings:Recommended Settings:RF Blanking Marker Positions []

Returns the array of sample positions of marker events, which are used to toggle the state of RF blanking, within the waveform.

The marker positions are such that RF blanking is enabled during the idle interval. This property is applicable only if you set the [RF Blanking Enabled](attr5a.html) property to **True**. The RF Blanking Marker Positions property is queried by the [niWLANG RFSG Create and Download Waveform](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_create_and_download_waveform) VI to store RF blanking marker positions in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Blanking Marker Positions [] |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5e.html language=enus -->
## TOPIC 00048: Payload:Number of Data Symbols

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5e.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of symbols in the data portion of the WLAN frame. The symbol refers to the chip if the Standard property is set to 80211B/G DSSS, and the symbol refers to the OFDM symbol for other values of the Standard property. Remarks The following table lists the characteristics of this prope

### Payload:Number of Data Symbols

Returns the number of symbols in the data portion of the WLAN frame. The symbol refers to the chip if the [Standard](/csh?topicname=attr1f.html) property is set to **80211B/G DSSS**, and the symbol refers to the OFDM symbol for other values of the Standard property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Data Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5f.html language=enus -->
## TOPIC 00049: Data Rate and Frame Format:PPDU Type

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr5f.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of physical layer convergence procedure (PLCP) protocol data unit (PPDU), if the Standard property is set to 80211AC MIMOOFDM, 80211AX MIMOOFDM, 80211BE MIMOOFDM or 80211BN MIMOOFDM. The default value is SU PPDU. Remarks The following table lists the characteristics of this proper

### Data Rate and Frame Format:PPDU Type

Specifies the type of physical layer convergence procedure (PLCP) protocol data unit (PPDU), if the [Standard](/csh?topicname=attr1f.html) property is set to **80211AC MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM**.

The default value is **SU PPDU**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PPDU Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set PPDU Type |
| Resettable | No |

| SU PPDU | 0 | Specifies that the WLAN Generation generates a single user (SU) PPDU. |
| --- | --- | --- |
| MU PPDU | 1 | Specifies that the WLAN Generation generates a multi-user (MU) PPDU. |
| Extended Range SU PPDU | 2 | Specifies that the WLAN Generation generates an extended range single user (ER SU) PPDU. |
| Trigger-Based PPDU | 3 | Specifies that the WLAN Generation generates a trigger-based (TB) PPDU. |
| ELR PPDU | 4 | Specifies that the WLAN Generation generates an enhanced long range (ELR) PPDU. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr6.html language=enus -->
## TOPIC 00050: Number of Frames

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr6.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of frames to generate. Each iteration of the niWLANG Create Waveform VI generates only one frame along with the idle interval that you specify using the Idle Interval property. If you set the Number of Frames property to a value greater than 1, create a loop around the niWLANG C

### Number of Frames

Specifies the number of frames to generate. Each iteration of the [niWLANG Create Waveform](/csh?context=rfmxwlangen_lvwlangenref_niwlang_create_waveform) VI generates only one frame along with the idle interval that you specify using the [Idle Interval](/csh?topicname=attr3.html) property.

If you set the Number of Frames property to a value greater than 1, create a loop around the niWLANG Create Waveform VI and concatenate the output values from different iterations. If you encounter memory usage issues, download a single frame to the NI RF vector signal generator memory on each iteration.

To generate the required number of frames, wire the Number of Frames property to the loop iteration count. You also can use the **generation done?** parameter on the niWLANG Create Waveform VI as a termination signal.

You can use the niRFSG Allocate Arb Waveform VI to preallocate arb memory and then download the waveform frame-by-frame.

The default value is 1. Valid values are 1 to 1,000 (inclusive).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Frames |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Number of Frames |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr61.html language=enus -->
## TOPIC 00051: Impairments:AWGN:Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr61.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr61.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to introduce additive white Gaussian noise (AWGN) to the baseband waveform. the WLAN Generation uses the value specified in the Carrier to Noise Ratio property to add the AWGN. The default value is False. Remarks The following table lists the characteristics of this property. Short

### Impairments:AWGN:Enabled

Specifies whether to introduce additive white Gaussian noise (AWGN) to the baseband waveform. the WLAN Generation uses the value specified in the [Carrier to Noise Ratio](/csh?topicname=attr62.html) property to add the AWGN.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AWGN Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables AWGN addition. |
| --- | --- | --- |
| True | 1 | Enables AWGN addition. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr62.html language=enus -->
## TOPIC 00052: Impairments:AWGN:Carrier to Noise Ratio (dB)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr62.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr62.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the carrier-to-noise ratio (CNR) of the waveform generated. Noise bandwidth is equal to the value of the IQ Rate property. the WLAN Generation ignores the Carrier to Noise Ratio property if you set the AWGN Enabled property to False. This value is expressed in dB. Standard Property Value A

### Impairments:AWGN:Carrier to Noise Ratio (dB)

Specifies the carrier-to-noise ratio (CNR) of the waveform generated. Noise bandwidth is equal to the value of the [IQ Rate](/csh?topicname=attr23.html) property. the WLAN Generation ignores the Carrier to Noise Ratio property if you set the [AWGN Enabled](/csh?topicname=attr61.html) property to **False**. This value is expressed in dB.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "channelx" |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM | "segmentx/channely" |
| 80211AX MIMOOFDM | "segmentx/channely", if you set the PPDU Type property to SU PPDU, Extended Range SU PPDU or MU PPDU |
| 80211AX MIMOOFDM | "[userx]/segmenty/channelz", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BE MIMOOFDM | "channelx", if you set the PPDU Type property to MU PPDU |
| 80211BE MIMOOFDM | "[userx]/channely", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |
| 80211BN MIMOOFDM | "channelx", if you set the PPDU Type property to MU PPDU or ELR PPDU |
| 80211BN MIMOOFDM | "[userx]/channely", if you set the PPDU Type property to Trigger-Based PPDU (userx is optional if you want to apply to all users) |

The default value is 50. Valid values are -100 to 100, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Carrier to Noise Ratio (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr64.html language=enus -->
## TOPIC 00053: Payload:MAC FCS Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr64.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr64.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the medium access control (MAC) frame check sequence (FCS), as defined in section 7.1.2 of IEEE Standard 802.11-2007 and IEEE Standard 802.11n-2009, section 8.2.4 of IEEE Standard 802.11ac-2013, IEEE P802.11ah/D1.3 and IEEE Standard P802.11af-2013, section 9.2.4 of IEEE P

### Payload:MAC FCS Enabled

Specifies whether to enable the medium access control (MAC) frame check sequence (FCS), as defined in section 7.1.2 of *IEEE Standard 802.11-2007* and *IEEE Standard 802.11n-2009*, section 8.2.4 of *IEEE Standard 802.11ac-2013*, *IEEE P802.11ah/D1.3* and *IEEE Standard P802.11af-2013*, section 9.2.4 of *IEEE P802.11ax/D8.0*, section 9.2.4 of *IEEE P802.11be/D7.0*, and section 9.2.4 of *IEEE P802.11bn/D1.3*.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", If you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True |

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC FCS Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the MAC FCS field. |
| --- | --- | --- |
| True | 1 | Enables the MAC FCS field. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr65.html language=enus -->
## TOPIC 00054: Obsolete:Legacy Scaling Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr65.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable standard-defined transmit chain scaling of the legacy part of the high throughput (HT) and very high throughput (VHT) frames. Configure this property only when you set the Standard property to 80211N MIMOOFDM or 80211AC MIMOOFDM. the WLAN Generation ignores the Legacy Sca

### Obsolete:Legacy Scaling Enabled

Specifies whether to enable standard-defined transmit chain scaling of the legacy part of the high throughput (HT) and very high throughput (VHT) frames.

Note

Standard

80211N MIMOOFDM

80211AC MIMOOFDM

Note

toolkit compatibility version

niWLANG Open Session

2.0.0

3.0.0.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Legacy Scaling Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables the legacy part of the HT and VHT frame. |
| --- | --- | --- |
| True | 1 | Enables the legacy part of the HT and VHT frame. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr66.html language=enus -->
## TOPIC 00055: Hardware Settings:Maximum Hardware IQ Rate (S/s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr66.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum I/Q rate that the NI vector signal generator supports. This property will be set according to the device model in the niWLANG RFSG Create and Download Waveform VI. Device Valid Values (MS/s) PXIe-5842 2500 PXIe-5840/PXIe-5841/PXIe-5841 with PXIe-5655/PXIe-5820/PXIe-5830/PXIe-58

### Hardware Settings:Maximum Hardware IQ Rate (S/s)

Specifies the maximum I/Q rate that the NI vector signal generator supports.

This property will be set according to the device model in the [niWLANG RFSG Create and Download Waveform](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_create_and_download_waveform) VI.

| Device | Valid Values (MS/s) |
| --- | --- |
| PXIe-5842 | 2500 |
| PXIe-5840/PXIe-5841/PXIe-5841 with PXIe-5655/PXIe-5820/PXIe-5830/PXIe-5831/PXIe-5860 | 1250 |
| PXIe-5646 | 250 |
| PXIe-5644/PXIe-5645 | 120 |
| PXIe-5673/5673E | 200 |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Maximum Hardware IQ Rate (S/s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr67.html language=enus -->
## TOPIC 00056: Payload:A-MPDU Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr67.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr67.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether all medium access control (MAC) protocol data units (MPDUs) are transmitted as aggregate-MPDU (A-MPDU). This property is applicable only if you set the Standard property to 80211N MIMOOFDM, 80211AC MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM, 80211AX MIMOOFDM, 80211BE MIMOOFDM, or

### Payload:A-MPDU Enabled

Specifies whether all medium access control (MAC) protocol data units (MPDUs) are transmitted as aggregate-MPDU (A-MPDU).

Note

Standard

80211N MIMOOFDM

80211AC MIMOOFDM

80211AH MIMOOFDM

80211AF MIMOOFDM

80211AX MIMOOFDM

80211BE MIMOOFDM

80211BN MIMOOFDM

Non-HT Modulation Mode

Off

The default value is **False**, if you set the Standard property to **80211N MIMOOFDM** or **80211AH MIMOOFDM**. The default value is **True**, if you set the Standard property to **80211AC MIMOOFDM**, **80211AF MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | A-MPDU Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Payload AMPDU Enabled |
| Resettable | No |

| False | 0 | the WLAN Generation does not transmit an A-MPDU. |
| --- | --- | --- |
| True | 1 | the WLAN Generation transmits an A-MPDU. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr68.html language=enus -->
## TOPIC 00057: Payload:Number of MPDUs

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr68.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of medium access control (MAC) protocol data units (MPDUs) to combine into one aggregate-MPDU (A-MPDU). You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211N MIMOOFDM, 80211AH MIMOOFDM, 80

### Payload:Number of MPDUs

Specifies the number of medium access control (MAC) protocol data units (MPDUs) to combine into one aggregate-MPDU (A-MPDU).

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211AF MIMOOFDM | "" (empty string) |
| 80211AC MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU |
| 80211AC MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU |
| 80211AX MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BE MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU |

Note

A-MPDU Enabled

False

Standard

80211N MIMOOFDM

80211AC MIMOOFDM

80211AH MIMOOFDM

80211AF MIMOOFDM

80211AX MIMOOFDM

80211BE MIMOOFDM

80211BN MIMOOFDM

Non-HT Modulation Mode

On

Auto Number of MPDUs

True

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Payload Number of MPDUs |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Payload Number of MPDUs |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr7.html language=enus -->
## TOPIC 00058: Payload:Data Type

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr7.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of payload for waveform generation. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM "" (empty string) 80211N MIMOOFDM,

### Payload:Data Type

Specifies the type of payload for waveform generation.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", If you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True |

The default value is **PN Sequence**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Payload Data Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| User Defined Pattern | 0 | Specifies that the WLAN Generation uses the sequence that you specify using the Payload User Defined Bits property. |
| --- | --- | --- |
| PN Sequence | 1 | Specifies that the WLAN Generation generates the bits using a pseudonoise (PN) sequence with the PN seed and order you specify using the Payload PN Seed and Payload PN Order properties, respectively. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr70.html language=enus -->
## TOPIC 00059: Spectrum Control:Pulse Shaping Filter Length

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr70.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr70.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the length of the pulse-shaping filter. This value is expressed in symbols. The length affects the frequency response of the filter. the WLAN Generation ignores this property when the Pulse Shaping Filter Enabled property is set to False. If you set the Standard property to 80211P OFDM, th

### Spectrum Control:Pulse Shaping Filter Length

Specifies the length of the pulse-shaping filter. This value is expressed in symbols.

The length affects the frequency response of the filter. the WLAN Generation ignores this property when the [Pulse Shaping Filter Enabled](attr36.html) property is set to **False**.

If you set the Standard property to **80211P OFDM**, the default value is 100. In all other instances, the default value is 8.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Shaping Filter Length |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr73.html language=enus -->
## TOPIC 00060: MIMO:Number of Users

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr73.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of users in a multi-user (MU) physical layer convergence procedure (PLCP) protocol data unit (PPDU). The default value is 1. You can set this property only when you set the Standard property to 80211AC MIMOOFDM and the PPDU Type property to MU PPDU, or when you set the Standard

### MIMO:Number of Users

Specifies the number of users in a multi-user (MU) physical layer convergence procedure (PLCP) protocol data unit (PPDU).

The default value is 1. You can set this property only when you set the [Standard](attr1f.html) property to **80211AC MIMOOFDM** and the [PPDU Type](attr5f.html) property to **MU PPDU**, or when you set the Standard property to **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM** and the PPDU Type property to **MU PPDU** or **Trigger-Based PPDU**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Users |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | niWLANG Set Number of Users |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr76.html language=enus -->
## TOPIC 00061: Hardware Settings:LO Sharing Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr76.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable configuration for sharing of local oscillator (LO) signal for multiple NI RF vector signal analyzers or vector signal transceivers. This property is read when you call the niWLANG RFSG Configure Multiple Device Synchronization VI. The default value is False. Remarks The f

### Hardware Settings:LO Sharing Enabled

Specifies whether to enable configuration for sharing of local oscillator (LO) signal for multiple NI RF vector signal analyzers or vector signal transceivers.

This property is read when you call the [niWLANG RFSG Configure Multiple Device Synchronization](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_configure_multiple_device_synchronization) VI.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Sharing Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables LO sharing. |
| --- | --- | --- |
| True | 1 | Enables LO sharing. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr7d.html language=enus -->
## TOPIC 00062: Spectrum Control:OFDM Window Length (samples)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr7d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr7d.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the window length, for OFDM signals at the sampling rate equal to the channel bandwidth. For example, if the window length is 2, the channel bandwidth is 20 MHz and the oversampling ratio is 4, the samples over which windowing is applied is 8. This value is expressed in samples. This prope

### Spectrum Control:OFDM Window Length (samples)

Specifies the window length, for OFDM signals at the sampling rate equal to the channel bandwidth. For example, if the window length is 2, the channel bandwidth is 20 MHz and the oversampling ratio is 4, the samples over which windowing is applied is 8. This value is expressed in samples.

This property provides a smooth, spurious-free transition from the end of one OFDM symbol to the cyclic prefix of the next symbol. If you do not want windowing, set this property to 0.

Refer to the [Windowing](/csh?context=rfmxwlangen_wlangen_windowing) help topic for more information about windowing for OFDM signals.

The default value is 2.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OFDM Window Length (samples) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr85.html language=enus -->
## TOPIC 00063: Data Rate and Frame Format:RU Allocation Settings:RU Offset/MRU Index

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr85.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr85.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the location of the resource unit (RU) or multiple resource unit (MRU). If an RU is configured, the RU Offset is in terms of the index of 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs in 802.11ax, 802.11be and 802.11bn signal. For example, in the following figure, to

### Data Rate and Frame Format:RU Allocation Settings:RU Offset/MRU Index

Specifies the location of the resource unit (RU) or multiple resource unit (MRU).

If an RU is configured, the RU Offset is in terms of the index of 26-tone RU, assuming the entire bandwidth is composed of 26-tone RUs in 802.11ax, 802.11be and 802.11bn signal. For example, in the following figure, to specify the 106-tone RU second from left, you must configure this property to 5.

[IMAGE alt='image' src='242_tone_ru.PNG']

In the preceding image,

- The shaded area indicates null subcarriers
- The square bracket value indicates the RU Offset/MRU Index

If an MRU is configured, the MRU Index is as defined in tables 36-8 to 36-15 of *IEEE P802.11be/D7.0* standard.

If a dRU is configured, the RU Offset represents dRU index as defined in tables 38-4 to 38-6 and equation 38-1 of *IEEE P802.11bn/D1.3* standard.

This property is valid only if you set the [PPDU Type](attr5f.html) property to **MU PPDU** or **Trigger-Based PPDU**.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU. |

The valid values, when the Standard property is set to 80211AX MIMOOFDM, are as follows:

| Channel Bandwidth (MHz) | Number of Segments | Valid Values (all inclusive) |
| --- | --- | --- |
| 20 | 1 | 0 to 8 |
| 40 | 1 | 0 to 17 |
| 80 | 1 | 0 to 36 |
| 160 | 1 | 0 to 73 |
| 80 | 2 | 0 to 73 |

The valid RU offset values, when the Standard property is set to 80211BE MIMOOFDM or 80211BN MIMOOFDM, are as follows:

| Channel Bandwidth (MHz) | Valid Values (all inclusive) |
| --- | --- |
| 20 | 0 to 8 |
| 40 | 0 to 17 |
| 80 | 0 to 36 except 18 |
| 160 | 0 to 73 except 18 and 55 |
| 320 | 0 to 147 except 18, 55, 92, and 129 |

The valid MRU Index values, when the Standard property is set to **80211BE MIMOOFDM** or **80211BN MIMOOFDM**, are as defined in tables 36-8 to 36-15 of *IEEE P802.11be/D7.0* standard.

The valid RU Offset values if dRUs are configured, when the Standard property is set to **80211BN MIMOOFDM**, are as defined in tables 38-4 to 38-6 and equation 38-1 of *IEEE P802.11bn/D1.3* standard.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RU Offset/MRU Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr86.html language=enus -->
## TOPIC 00064: MIMO:Multi-segment Generation Mode

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr86.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr86.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use a single generator or two generators for each channel of a multi-segment (80+80) MHz 802.11ac signal. This property is applicable when the Number of Segments property is 2 and the channel bandwidth is 80 MHz. When you set this property to Single Generator, you have to specif

### MIMO:Multi-segment Generation Mode

Specifies whether to use a single generator or two generators for each channel of a multi-segment (80+80) MHz 802.11ac signal. This property is applicable when the [Number of Segments](/csh?topicname=attr4b.html) property is 2 and the channel bandwidth is 80 MHz. When you set this property to **Single Generator**, you have to specify the value of the [Carrier Frequency](/csh?topicname=attr0.html) property for both the segments.

The default value is **Multiple Generators**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Multi-segment Generation Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Single Generator | 0 | Specifies that one vector signal generator is used to generate the (80+80) MHz 802.11ac signal. |
| --- | --- | --- |
| Multiple Generators | 1 | Specifies that two vector signal generators are used to generate the (80+80) MHz 802.11ac signal. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr87.html language=enus -->
## TOPIC 00065: Impairments:Time Delay (s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr87.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr87.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time delay for each user within an 802.11ax, 802.11be and 802.11bn Trigger-Based signal. This value is expressed in seconds. You must set the Standard property to 80211AX MIMOOFDM, 80211BE MIMOOFDM or 80211BN MIMOOFDM and the PPDU Type property to Trigger-Based PPDU. Use this property

### Impairments:Time Delay (s)

Specifies the time delay for each user within an 802.11ax, 802.11be and 802.11bn Trigger-Based signal. This value is expressed in seconds. You must set the [Standard](/csh?topicname=attr1f.html) property to **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM** and the [PPDU Type](/csh?topicname=attr5f.html) property to **Trigger-Based PPDU**. Use this property to introduce relative time delays between multiple users within an 802.11ax Trigger-Based signal.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to set this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to Trigger-Based PPDU. |

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Time Delay (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attr9f.html language=enus -->
## TOPIC 00066: Data Rate and Frame Format:Packet Extension Duration (s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attr9f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attr9f.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the duration of packet extension in the waveform when you set the Standard property to 80211AX MIMOOFDM, 80211BE MIMOOFDM or 80211BN MIMOOFDM. This value is expressed in seconds. Remarks The following table lists the characteristics of this property. Short Name Packet Extension Duration (s)

### Data Rate and Frame Format:Packet Extension Duration (s)

Returns the duration of packet extension in the waveform when you set the [Standard](/csh?topicname=attr1f.html) property to **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM**. This value is expressed in seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Packet Extension Duration (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb0.html language=enus -->
## TOPIC 00067: Hardware Settings:LO Frequency Offset Mode

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb0.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the LO frequency offset is derived to configure frequency on the NI RF vector signal generators and the NI synthesizers in the niWLANG RFSG Configure Frequency VI. the WLAN Generation ignores this property if you do not use PXIe-5840, PXIe-5841, PXIe-5841 with PXIe-5655, PXIe-5646, PXI

### Hardware Settings:LO Frequency Offset Mode

Specifies how the LO frequency offset is derived to configure frequency on the NI RF vector signal generators and the NI synthesizers in the [niWLANG RFSG Configure Frequency](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_configure_frequency) VI. the WLAN Generation ignores this property if you do not use PXIe-5840, PXIe-5841, PXIe-5841 with PXIe-5655, PXIe-5646, PXIe-5830, PXIe-5831, or PXIe-5842 devices.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Frequency Offset Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Auto | 0 | Specifies that the LO frequency offset value is computed for optimal EVM performance. |
| --- | --- | --- |
| User defined | 1 | Sets the LO frequency offset value to the value you specified in the LO Frequency Offset property. |
| Disabled | 2 | Specifies that the LO frequency offset is not set by the WLAN Generation. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb7.html language=enus -->
## TOPIC 00068: Data Rate and Frame Format:LDPC Extra Symbol Segment

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb7.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the LDPC extra symbol segment field in the trigger frame which is used for 802.11ax Trigger-Based PPDU, 802.11be Trigger-Based PPDU and 802.11bn Trigger-Based PPDU generation. The default value is -1, which indicates that the value of the LDPC extra symbol segment field is der

### Data Rate and Frame Format:LDPC Extra Symbol Segment

Specifies the value of the LDPC extra symbol segment field in the trigger frame which is used for 802.11ax Trigger-Based PPDU, 802.11be Trigger-Based PPDU and 802.11bn Trigger-Based PPDU generation.

The default value is -1, which indicates that the value of the LDPC extra symbol segment field is derived from the payload settings.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LDPC Extra Symbol Segment |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb8.html language=enus -->
## TOPIC 00069: Data Rate and Frame Format:BSS Color

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb8.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the identifier of the BSS (Basic Service Set) from which the 802.11ax PPDU, 802.11be PPDU and 802.11bn PPDU are transmitted. The default value is 63. The valid values are 0 to 63, inclusive. Remarks The following table lists the characteristics of this property. Short Name BSS Color Data t

### Data Rate and Frame Format:BSS Color

Specifies the identifier of the BSS (Basic Service Set) from which the 802.11ax PPDU, 802.11be PPDU and 802.11bn PPDU are transmitted.

The default value is 63. The valid values are 0 to 63, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | BSS Color |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb9.html language=enus -->
## TOPIC 00070: MIMO:Spatial Mapping Mode

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrb9.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spatial mapping is created from a single global matrix or per user. This property is valid, when you set the PPDU Type property to Trigger-Based PPDU. The default value is Common. Remarks The following table lists the characteristics of this property. Short Name Spatial Mapping

### MIMO:Spatial Mapping Mode

Specifies whether the spatial mapping is created from a single global matrix or per user. This property is valid, when you set the [PPDU Type](/csh?topicname=attr5f.html) property to **Trigger-Based PPDU**.

The default value is **Common**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Spatial Mapping Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Common | 0 | Specifies that a single global matrix is used for spatial mapping of all users. |
| --- | --- | --- |
| User Specific | 1 | Specifies that per user spatial mapping is done. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrba.html language=enus -->
## TOPIC 00071: MIMO:MU-MIMO LTF Mode Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrba.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrba.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the HE-LTF sequence corresponding to each space time stream is masked by a distinct orthogonal code if you set the Standard property to 80211AX MIMOOFDM and PPDU Type property to Trigger-Based PPDU. The default value is False. Remarks The following table lists the characteristics o

### MIMO:MU-MIMO LTF Mode Enabled

Specifies whether the HE-LTF sequence corresponding to each space time stream is masked by a distinct orthogonal code if you set the [Standard](/csh?topicname=attr1f.html) property to **80211AX MIMOOFDM** and [PPDU Type](/csh?topicname=attr5f.html) property to **Trigger-Based PPDU**.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MU-MIMO LTF Mode Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Specifies that single stream pilots are used in LTF sequence. |
| --- | --- | --- |
| True | 1 | Specifies that the LTF sequence is HE masked. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbb.html language=enus -->
## TOPIC 00072: MIMO:Space Time Stream Offset

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbb.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbb.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the space time stream offset which is used for 802.11ax, 802.11be and 802.11bn Trigger-Based PPDU generation. You must use the following active channel string formats to set this property. Standard Property Value Active Channel String Format 80211AX MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMO

### MIMO:Space Time Stream Offset

Specifies the space time stream offset which is used for 802.11ax, 802.11be and 802.11bn Trigger-Based PPDU generation.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to set this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to Trigger-Based PPDU |

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Space Time Stream Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbc.html language=enus -->
## TOPIC 00073: Payload:MAC Frame Type

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbc.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of frame for the MPDU. This property can be set to Trigger Frame only if you set the Standard property to 80211A/G OFDM, 80211N MIMOOFDM, 80211AC MIMOOFDM, 80211AX MIMOOFDM, 80211BE MIMOOFDM, or 80211BN MIMOOFDM. You must use the following active channel string formats to configur

### Payload:MAC Frame Type

Specifies the type of frame for the MPDU. This property can be set to Trigger Frame only if you set the [Standard](/csh?topicname=attr1f.html) property to **80211A/G OFDM**, **80211N MIMOOFDM**, **80211AC MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, or **80211BN MIMOOFDM**.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, 80211G DSSSOFDM | "" (empty string) |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM, 80211AH MIMOOFDM | "mpdux", if you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AC MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AC MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU and the A-MPDU Enabled property to True. |
| 80211AF MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False. |
| 80211AF MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "" (empty string), if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to False. |
| 80211AX MIMOOFDM | "mpdux", if you set the PPDU Type property to SU PPDU or Extended Range SU PPDU and the A-MPDU Enabled property to True. |
| 80211AX MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BE MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "userx/mpduy", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU and the A-MPDU Enabled property to True. |
| 80211BN MIMOOFDM | "" (empty string), if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to False. |
| 80211BN MIMOOFDM | "mpdux", if you set the PPDU Type property to ELR PPDU and the A-MPDU Enabled property to True. |

The default value is **General Frame**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Frame Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| General Frame | 0 | Specifies that the MAC frame type is General. |
| --- | --- | --- |
| Data Frame | 1 | Specifies that the MAC frame type is Data. |
| Trigger Frame | 2 | Specifies that the MAC frame type is Trigger Frame. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbd.html language=enus -->
## TOPIC 00074: Payload:Trigger Frame:MAC Padding Duration (s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbd.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the padding duration when the MAC Frame Type property is set to Trigger Frame. This property is valid if you set the Standard property to 80211A/G OFDM, 80211N MIMOOFDM, 80211AC MIMOOFDM, 80211AX MIMOOFDM, 80211BE MIMOOFDM, and 80211BN MIMOOFDM. You must use the following active channel st

### Payload:Trigger Frame:MAC Padding Duration (s)

Specifies the padding duration when the [MAC Frame Type](/csh?topicname=attrbc.html) property is set to **Trigger Frame**. This property is valid if you set the [Standard](/csh?topicname=attr1f.html) property to **80211A/G OFDM**, **80211N MIMOOFDM**, **80211AC MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, and **80211BN MIMOOFDM**.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211A/G OFDM | "" (empty string) |
| 80211N MIMOOFDM | "", if you set the A-MPDU Enabled property to False |
| 80211N MIMOOFDM | "mpdux", If you set the A-MPDU Enabled property to True |
| 80211AC MIMOOFDM, 80211AX MIMOOFDM | "", if you set the PPDU Type property to SU PPDU and the A-MPDU Enabled property to False |
| 80211AC MIMOOFDM, 80211AX MIMOOFDM | "mpdux", If you set the A-MPDU Enabled property to True |
| 80211BE MIMOOFDM, 80211BN MIMOOFDM | "mpdux", If you set the A-MPDU Enabled property to True |

The default value is **0us**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | MAC Padding Duration (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| 0us | 0 | Specifies that there is no padding. |
| --- | --- | --- |
| 8us | 1 | Specifies that the padding duration is 8us. |
| 16us | 2 | Specifies that the padding duration is 16us. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbe.html language=enus -->
## TOPIC 00075: Payload:Trigger Frame:CS Required

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbe.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbe.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the CS required sub-field in the 802.11ax, 802.11be and 802.11bn Trigger Frame. The default value is 0. The valid values are 0 and 1. Remarks The following table lists the characteristics of this property. Short Name CS Required Data type ci32.png Permissions Read/Write High-level VIs N/A

### Payload:Trigger Frame:CS Required

Specifies the CS required sub-field in the 802.11ax, 802.11be and 802.11bn Trigger Frame.

The default value is 0. The valid values are 0 and 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CS Required |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbf.html language=enus -->
## TOPIC 00076: Data Rate and Frame Format:Preamble Puncturing:Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrbf.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable preamble puncturing (channel puncturing) on 802.11ax MU PPDU, 802.11be MU PPDU and 802.11bn MU PPDU signals. Preamble puncturing is valid only when you set the Channel Bandwidth property to 80 MHz, 160 MHz, or 320 MHz. The default value is False. Remarks The following tab

### Data Rate and Frame Format:Preamble Puncturing:Enabled

Specifies whether to enable preamble puncturing (channel puncturing) on 802.11ax MU PPDU, 802.11be MU PPDU and 802.11bn MU PPDU signals. Preamble puncturing is valid only when you set the [Channel Bandwidth](/csh?topicname=attr2a.html) property to 80 MHz, 160 MHz, or 320 MHz.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Preamble Puncturing Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Specifies that preamble puncturing is disabled. |
| --- | --- | --- |
| True | 1 | Specifies that preamble puncturing is enabled. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc.html language=enus -->
## TOPIC 00077: Coding:Subcarrier Mask

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sequence of attenuation values on each subcarrier in the signal and payload symbols if you set the Standard property to 80211A/G OFDM, 80211J OFDM, 80211P OFDM or 80211G DSSSOFDM. You must specify a 64-element array. The first element of the array corresponds to subcarrier index-32, an

### Coding:Subcarrier Mask

Specifies the sequence of attenuation values on each subcarrier in the signal and payload symbols if you set the [Standard](/csh?topicname=attr1f.html) property to **80211A/G OFDM**, **80211J OFDM**, **80211P OFDM** or **80211G DSSSOFDM**. You must specify a 64-element array. The first element of the array corresponds to subcarrier index-32, and the 64th element corresponds to subcarrier index 31, as defined in section 17.3.2.5 of *IEEE Standard 802.11a-1999*.

If an element has a value of 0, this indicates that the corresponding subcarrier is absent in the generated signal. If an element has a value of 1, this indicates that the corresponding subcarrier is present in the generated signal.

The default value is a 64-element array of all ones. Valid values are 64-element arrays of zeros and ones.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Subcarrier Mask |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc2.html language=enus -->
## TOPIC 00078: Hardware Settings:Recommended Settings:Signal Bandwidth (Hz)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc2.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Signal Bandwidth value that needs to be configured on the NI RFSG session for the PXIe-5820, PXIe-5830, PXIe-5831, PXIe-5841, PXIe-5841 with PXIe-5655, PXIe-5842, or PXIe-5860 devices. the WLAN Generation computes this value using the following equation. Signal Bandwidth (Hz) = 2 * {(Cha

### Hardware Settings:Recommended Settings:Signal Bandwidth (Hz)

Returns the Signal Bandwidth value that needs to be configured on the NI RFSG session for the PXIe-5820, PXIe-5830, PXIe-5831, PXIe-5841, PXIe-5841 with PXIe-5655, PXIe-5842, or PXIe-5860 devices.

the WLAN Generation computes this value using the following equation.

Signal Bandwidth (Hz) = 2 * {(Channel Bandwidth/2) + |Maximum Carrier Frequency Offset|}

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Signal Bandwidth (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc3.html language=enus -->
## TOPIC 00079: Data Rate and Frame Format:Nominal Packet Padding

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc3.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the nominal packet padding value used for determining the packet extension duration when you set the Standard property to 80211AX MIMOOFDM, 80211BE MIMOOFDM or 80211BN MIMOOFDM. When you set the PPDU Type property to MU PPDU or Trigger-Based PPDU , this property value corresponds to the ma

### Data Rate and Frame Format:Nominal Packet Padding

Specifies the nominal packet padding value used for determining the packet extension duration when you set the [Standard](/csh?topicname=attr1f.html) property to **80211AX MIMOOFDM**, **80211BE MIMOOFDM** or **80211BN MIMOOFDM**.

When you set the [PPDU Type](attr5f.html) property to **MU PPDU** or **Trigger-Based PPDU** , this property value corresponds to the maximum nominal packet padding across all users. When you set the PPDU Type property to **Trigger-Based PPDU**; and none of the [L-SIG Length](attrb4.html) property, [Pre-FEC Padding Factor](attrb5.html) property, [PE Disambiguity](attrb6.html) property, and [LDPC Extra Symbol Segment](attrb6.html) property are set to -1, the WLAN Generation ignores this property. When you set the PPDU Type property to **ELR PPDU**, only nominal packet padding value of **8us** is supported.

Nominal packet padding value of **20us** is supported only if you set the Standard property to **80211BE MIMOOFDM**.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Nominal Packet Padding |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Auto | -1 | Specifies that the nominal packet padding is any of the following: 0us, if all the resource units are of size less than 242 and DCM is disabled. 0us, if all the resource units are of size less than 106 and DCM is enabled. 20us, if MCS Index is 12 or 13 or resource unit size is greater than 996*2 or number of spatial streams is greater than 8 for 80211BE MIMOOFDM and 80211BN MIMOOFDM. 16us, otherwise. |
| --- | --- | --- |
| 0us | 0 | Specifies that the nominal packet padding is 0us. |
| 8us | 1 | Specifies that the nominal packet padding is 8us. |
| 16us | 2 | Specifies that the nominal packet padding is 16us. |
| 20us | 3 | Specifies that the nominal packet padding is 20us if MCS Index is 12 or 13 or resource unit size is greater than 996*2 or number of spatial streams is greater than 8, and is 16us, otherwise. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc4.html language=enus -->
## TOPIC 00080: Payload:Trigger Frame:AID12

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc4.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the AID12 field in the trigger frame. The valid values are 1 to 2007, which are used for indication of RUs used by Trigger-based PPDU. The values 0 and 2045 are used for Random Access RU information specification, the value 2046 is used for unassigned RU location indication, a

### Payload:Trigger Frame:AID12

Specifies the value of the AID12 field in the trigger frame.

The valid values are 1 to 2007, which are used for indication of RUs used by Trigger-based PPDU.

The values 0 and 2045 are used for Random Access RU information specification, the value 2046 is used for unassigned RU location indication, and the value 4095 is reserved for trigger frame padding indication.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string format to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211AX MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to Trigger-Based PPDU. |

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | AID12 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc7.html language=enus -->
## TOPIC 00081: Idle Interval Mode

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc7.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies how the idle interval is placed in the generated waveform. You cannot set this property to Split if you set the RF Blanking Enabled property to True. The default value is Split. Remarks The following table lists the characteristics of this property. Short Name Idle Interval Mode Data type

### Idle Interval Mode

Specifies how the idle interval is placed in the generated waveform. You cannot set this property to **Split** if you set the [RF Blanking Enabled](/csh?topicname=attr5a.html) property to **True**.

The default value is **Split**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Idle Interval Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Split | 0 | Half the idle interval is placed on either side of the burst in the generated waveform. |
| --- | --- | --- |
| Post Burst | 1 | Entire idle interval is placed at the end of the burst in the generated waveform. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc9.html language=enus -->
## TOPIC 00082: Hardware Settings:Run Time Scaling (dB)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrc9.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Runtime Scaling value in dB to store in the file along with the waveform. The default value is -1.5 dB Remarks The following table lists the characteristics of this property. Short Name Run Time Scaling (dB) Data type cdbl.png Permissions Read/Write High-level VIs N/A Resettable No

### Hardware Settings:Run Time Scaling (dB)

Specifies the Runtime Scaling value in dB to store in the file along with the waveform.

The default value is -1.5 dB

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Run Time Scaling (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrca.html language=enus -->
## TOPIC 00083: Waveform File Version

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrca.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrca.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the waveform file version to be saved. The default value is 1.0. Remarks The following table lists the characteristics of this property. Short Name Waveform File Version Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No 1.0 0 Indicates that the waveform file versio

### Waveform File Version

Specifies the waveform file version to be saved.

The default value is 1.0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waveform File Version |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| 1.0 | 0 | Indicates that the waveform file version is set to 1.0. |
| --- | --- | --- |
| 2.0 | 1 | Indicates that the waveform file version is set to 2.0. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd1.html language=enus -->
## TOPIC 00084: Frame Duration (s)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd1.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of a generated frame excluding idle interval. This property is applicable only if you set Auto Data Length Mode property to Frame Duration. When the value of Frame Duration results in fractional Number of Data Symbols, and if it results in generated frame duration less than 5.

### Frame Duration (s)

Specifies the duration of a generated frame excluding idle interval. This property is applicable only if you set [Auto Data Length Mode](/csh?topicname=attrb3.html) property to **Frame Duration**.

When the value of **Frame Duration** results in fractional **Number of Data Symbols**, and if it results in generated frame duration less than 5.484 milliseconds, the number of data symbols is rounded to the next highest integer, otherwise, the number of symbols is rounded to the next lowest integer.

The default value is 1 millisecond. Valid values are 100 microseconds to 5.484 milliseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Frame Duration (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd4.html language=enus -->
## TOPIC 00085: Data Rate and Frame Format:SIG MCS Index

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd4.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of the modulation and coding scheme (MCS) index of the SIG field of 802.11be and 802.11bn signal when you set the PPDU Type property to MU PPDU. The default value is 0. The valid values are 0 to 3, inclusive. Remarks The following table lists the characteristics of this property.

### Data Rate and Frame Format:SIG MCS Index

Specifies the value of the modulation and coding scheme (MCS) index of the SIG field of 802.11be and 802.11bn signal when you set the PPDU Type property to **MU PPDU**.

The default value is 0. The valid values are 0 to 3, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SIG MCS Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd5.html language=enus -->
## TOPIC 00086: Data Rate and Frame Format:SIG Compression Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd5.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the generated 802.11be and 802.11bn signal is a non-OFDMA signal or not. The default value is True. Remarks The following table lists the characteristics of this property. Short Name SIG Compression Enabled Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable No

### Data Rate and Frame Format:SIG Compression Enabled

Specifies whether the generated 802.11be and 802.11bn signal is a non-OFDMA signal or not.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SIG Compression Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Disables SIG compression. |
| --- | --- | --- |
| True | 1 | Enables SIG compression |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd6.html language=enus -->
## TOPIC 00087: Data Rate and Frame Format:Phase Rotation:Coefficient 1

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd6.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase rotation coefficient 1 as defined in IEEE Standard P802.11be/D7.0. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This property is valid only for 802.11be or 802.11bn and 320 MHz

### Data Rate and Frame Format:Phase Rotation:Coefficient 1

Specifies the phase rotation coefficient 1 as defined in *IEEE Standard P802.11be/D7.0*. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This property is valid only for 802.11be or 802.11bn and 320 MHz bandwidth.

The default value is **+1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Phase Rotation Coefficient 1 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| +1 | 0 | Specifies that phase rotation coefficient 1 is +1. |
| --- | --- | --- |
| -1 | 1 | Specifies that phase rotation coefficient 1 is –1. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd7.html language=enus -->
## TOPIC 00088: Data Rate and Frame Format:Phase Rotation:Coefficient 2

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrd7.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase rotation coefficient 2 as defined in IEEE Standard P802.11be/D7.0. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This property is valid only for 802.11be or 802.11bn and 320 MHz

### Data Rate and Frame Format:Phase Rotation:Coefficient 2

Specifies the phase rotation coefficient 2 as defined in *IEEE Standard P802.11be/D7.0*. To reduce PAPR, EHT-PPDUs and UHR-PPDUs apply phase rotation on pre-EHT and pre-UHR modulated fields (L-STF, L-LTF, L-SIG, RL-SIG, U-SIG, EHT-SIG). This property is valid only for 802.11be or 802.11bn and 320 MHz bandwidth.

The default value is **-1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Phase Rotation Coefficient 2 |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| +1 | 0 | Specifies that phase rotation coefficient 2 is +1. |
| --- | --- | --- |
| -1 | 1 | Specifies that phase rotation coefficient 2 is –1. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrde.html language=enus -->
## TOPIC 00089: Data Rate and Frame Format:RU Allocation Settings:RU Type

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrde.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrde.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU). This property is applicable only for 802.11bn TB PPDU. You must use the following active channel string formats to configure this property. Standard Property Value Active

### Data Rate and Frame Format:RU Allocation Settings:RU Type

Specifies whether contiguous subcarriers form the resource unit (rRU) or non-contiguous subcarriers form the resource unit (dRU).

This property is applicable only for 802.11bn TB PPDU.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to Trigger-Based PPDU. |

The default value is **rRU**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RU Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| rRU | 0 | RU Type configured is rRU. |
| --- | --- | --- |
| dRU | 1 | RU Type configured is dRU. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attrdf.html language=enus -->
## TOPIC 00090: Hardware Settings:Hybrid LO Sharing Mode

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attrdf.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attrdf.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable sharing of local oscillator (LO) in star plus daisy-chained way for multiple PXIe-5842. This property is read when you call the niWLANG RFSG Configure Frequency VI. The default value is Disabled. Remarks The following table lists the characteristics of this property. Shor

### Hardware Settings:Hybrid LO Sharing Mode

Specifies whether to enable sharing of local oscillator (LO) in star plus daisy-chained way for multiple PXIe-5842.

This property is read when you call the [niWLANG RFSG Configure Frequency](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_configure_frequency) VI.

The default value is **Disabled**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Hybrid LO Sharing Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Disabled | 0 | Hybrid LO Sharing is disabled. |
| --- | --- | --- |
| Mode 0 | 1 | Hybrid LO Sharing Mode 0 is enabled. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre0.html language=enus -->
## TOPIC 00091: Hardware Settings:Multi-Chassis TClk Synchronization Mode

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre0.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether Multi-Chassis TClk Synchronization is performed using Timing Module or automatically for multiple PXIe-5842, or PXIe-5860 devices. This property is read when you call the niWLANG RFSG Configure Multiple Device Synchronization VI. The default value is Auto. Remarks The following tab

### Hardware Settings:Multi-Chassis TClk Synchronization Mode

Specifies whether Multi-Chassis TClk Synchronization is performed using Timing Module or automatically for multiple PXIe-5842, or PXIe-5860 devices.

This property is read when you call the [niWLANG RFSG Configure Multiple Device Synchronization](/csh?context=rfmxwlangen_lvwlangenref_niwlang_rfsg_configure_multiple_device_synchronization) VI.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Multi-Chassis TClk Synchronization Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| Auto | 0 | Specifies that the Multi-Chassis TClk synchronization is done automatically. |
| --- | --- | --- |
| Timing Module | 1 | Specifies that the Multi-Chassis TClk synchronization is done using Timing Module. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre1.html language=enus -->
## TOPIC 00092: Hardware Settings:LO Splitter:LO Splitter Loss (dB)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre1.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre1.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of splitter loss values in dB, for corresponding array of splitter loss frequencies in Hz, if Hybrid LO Sharing Mode is set to Mode0. The default value is an empty array. Remarks The following table lists the characteristics of this property. Short Name LO Splitter Loss (dB) Data

### Hardware Settings:LO Splitter:LO Splitter Loss (dB)

Specifies the array of splitter loss values in dB, for corresponding array of splitter loss frequencies in Hz, if Hybrid LO Sharing Mode is set to Mode0.

The default value is an empty array.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Splitter Loss (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre2.html language=enus -->
## TOPIC 00093: Hardware Settings:LO Splitter:LO Splitter Loss Frequency (Hz)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre2.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the array of splitter loss frequencies in Hz, for corresponding array of splitter loss values in dB, if Hybrid LO Sharing Mode is set to Mode0. The default value is an empty array. Remarks The following table lists the characteristics of this property. Short Name LO Splitter Loss Frequency

### Hardware Settings:LO Splitter:LO Splitter Loss Frequency (Hz)

Specifies the array of splitter loss frequencies in Hz, for corresponding array of splitter loss values in dB, if Hybrid LO Sharing Mode is set to Mode0.

The default value is an empty array.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Splitter Loss Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre3.html language=enus -->
## TOPIC 00094: Data Rate and Frame Format:RU Allocation Settings:Distribution Bandwidth (Hz)

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre3.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth across which RU subcarriers are spread, when you set RU Type property to dRU. This property is applicable only for 802.11bn TB PPDU. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211

### Data Rate and Frame Format:RU Allocation Settings:Distribution Bandwidth (Hz)

Specifies the bandwidth across which RU subcarriers are spread, when you set RU Type property to **dRU**.

This property is applicable only for 802.11bn TB PPDU.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to Trigger-Based PPDU. |

The default value is **20M**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre4.html language=enus -->
## TOPIC 00095: Data Rate and Frame Format:2xLDPC Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre4.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals. You must use the following active channel string formats to configure this property. Standard Property Value Active Channel String Format 80211BN MIMOOFDM "userx", if you set the PPDU Type property to MU PPDU or Tr

### Data Rate and Frame Format:2xLDPC Enabled

Specifies whether to enable 2xLDPC for 802.11bn MU PPDU and 802.11bn TB PPDU signals.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU or Trigger-Based PPDU |

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | 2xLDPC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | 2xLDPC is disabled. |
| --- | --- | --- |
| True | 1 | 2xLDPC is enabled. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre5.html language=enus -->
## TOPIC 00096: Data Rate and Frame Format:Unequal Modulation:Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre5.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable unequal modulation (UEQM) for 802.11bn MU PPDU signals with 2 to 4 spatial streams. UEQM is only supported in non-MU-MIMO beamformed transmission. Modulation order of different spatial streams is determined by value of Pattern Index property. This property is applicable o

### Data Rate and Frame Format:Unequal Modulation:Enabled

Specifies whether to enable unequal modulation (UEQM) for 802.11bn MU PPDU signals with 2 to 4 spatial streams. UEQM is only supported in non-MU-MIMO beamformed transmission. Modulation order of different spatial streams is determined by value of Pattern Index property. This property is applicable only when Standard property is set to **80211BN MIMOOFDM**.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU |

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | UEQM Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Equal modulation order is used on all the spatial streams. |
| --- | --- | --- |
| True | 1 | Unequal modulation orders are used on different spatial streams. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre6.html language=enus -->
## TOPIC 00097: Data Rate and Frame Format:Unequal Modulation:Pattern Index

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre6.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unequal modulation pattern index when Unequal Modulation Enabled property is set to True. This property is applicable only when Standard property is set to 80211BN MIMOFDM. The allowed modulation orders for unequal modulation are QPSK, 16-QAM, 64-QAM, 256-QAM, 1024-QAM and 4096-QAM. Mo

### Data Rate and Frame Format:Unequal Modulation:Pattern Index

Specifies the unequal modulation pattern index when Unequal Modulation Enabled property is set to **True**. This property is applicable only when Standard property is set to **80211BN MIMOFDM**. The allowed modulation orders for unequal modulation are QPSK, 16-QAM, 64-QAM, 256-QAM, 1024-QAM and 4096-QAM. Modulation order of the first spatial stream is determined by the MCS Index property value. Pattern Index value determines the modulation order of remaining spatial streams with respect to the first spatial stream, as defined in the Table 38-29 of *IEEE P802.11bn/D1.3*.

You must use the following [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) string formats to configure this property.

| Standard Property Value | Active Channel String Format |
| --- | --- |
| 80211BN MIMOOFDM | "userx", if you set the PPDU Type property to MU PPDU |

The default value is 0. The valid values are 0 to 3, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | UEQM Pattern Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre7.html language=enus -->
## TOPIC 00098: Channelization

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre7.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the 320 MHz channelization value if you set the Standard property to 80211BE MIMOOFDM or 80211BN MIMOOFDM,. As defined in section 36.3.24.2 of IEEE P802.11be/D7.0 for 320 MHz channel. 320 MHz-1 consists of 320 MHz channels with channel center frequency numbers 31, 95 and 159. 320 MHz-2 con

### Channelization

Specifies the 320 MHz channelization value if you set the [Standard](/csh?topicname=attr1f.html) property to **80211BE MIMOOFDM** or **80211BN MIMOOFDM**,. As defined in section 36.3.24.2 of *IEEE P802.11be/D7.0* for 320 MHz channel. 320 MHz-1 consists of 320 MHz channels with channel center frequency numbers 31, 95 and 159. 320 MHz-2 consists of 320 MHz channels with channel center frequency numbers 63, 127 and 191.

The default value is **320 MHz-1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channelization |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| 320 MHz-1 | 0 |  |
| --- | --- | --- |
| 320 MHz-2 | 1 |  |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=resource/objmgr/niwlangeneration-rc/niwlangeneration/attre9.html language=enus -->
## TOPIC 00099: Data Rate and Frame Format:Interference Mitigation Pilots Enabled

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `resource/objmgr/niwlangeneration-rc/niwlangeneration/attre9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/resource/objmgr/niwlangeneration-rc/niwlangeneration/attre9.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether Interference Mitigation (IM) Pilots are added in the data field of the PPDU for the generated 802.11bn signal or not. The default value is False. Remarks The following table lists the characteristics of this property. Short Name Interference Mitigation Pilots Enabled Data type ci32

### Data Rate and Frame Format:Interference Mitigation Pilots Enabled

Specifies whether Interference Mitigation (IM) Pilots are added in the data field of the PPDU for the generated 802.11bn signal or not.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Interference Mitigation Pilots Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | No |

| False | 0 | Specifies that the Interference Mitigation (IM) Pilots are not added in the data field of the PPDU for the generated 802.11bn signal. |
| --- | --- | --- |
| True | 1 | Specifies that the Interference Mitigation (IM) Pilots are added in the data field of the PPDU for the generated 802.11bn signal. |

Parent topic:

niWLANGeneration Properties

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/getvis/niwlang-get-iq-rate-vi.html language=enus -->
## TOPIC 00100: niWLANG Get IQ Rate VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/getvis/niwlang-get-iq-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/getvis/niwlang-get-iq-rate-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the IQ Rate property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan

### niWLANG Get IQ Rate VI

Returns the value of the [IQ Rate](/csh?context=rfmxwlangen_lvwlangenprop_attr23) property.

[IMAGE alt='icon' src='niwlang-get-iq-rate-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. IQ rate (S/s) — error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Generation Information

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-channel-number-to-carrier-frequency-802-11ax-vi.html language=enus -->
## TOPIC 00101: niWLANG Channel Number to Carrier Frequency (802.11ax) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-channel-number-to-carrier-frequency-802-11ax-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-channel-number-to-carrier-frequency-802-11ax-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Calculates the carrier frequency of the 802.11ax channels. icon Inputs/Outputs cdbl.png channel starting frequency (Hz) channel starting frequency specifies the start frequency of the frequency band. This value is expressed in Hz. ci32.png channel number channel number specifies the offset of the ce

### niWLANG Channel Number to Carrier Frequency (802.11ax) VI

Calculates the carrier frequency of the 802.11ax channels.

[IMAGE alt='icon' src='niwlang-channel-number-to-carrier-frequency-802-11ax-vi.png']

#### Inputs/Outputs

| channel starting frequency (Hz) — channel starting frequency specifies the start frequency of the frequency band. This value is expressed in Hz. channel number — channel number specifies the offset of the center frequency, in increments of 5 MHz, above the start frequency of the channel. The default value is 1. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. carrier frequency (Hz) — carrier frequency returns the carrier frequency. This value is expressed in Hz. The VI calculates the carrier frequency using the following equation: Carrier Frequency (Hz) = Channel Starting Frequency (Hz) + (Channel Number * 5 MHz). error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

niWLANG Channel Number to Carrier Frequency VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-iq-complex-cluster-vi.html language=enus -->
## TOPIC 00102: niWLANG Create Multiple Channel Waveform (IQ Complex Cluster) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-iq-complex-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-iq-complex-cluster-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q data for multiple channels and returns the data as an array of complex clusters. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the gen

### niWLANG Create Multiple Channel Waveform (IQ Complex Cluster) VI

Creates WLAN I/Q data for multiple channels and returns the data as an array of complex clusters. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the **reset?** parameter to FALSE and run the VI in a loop for a specified number of times or until the **generation done?** parameter is TRUE.

Note

Standard

80211N MIMOOFDM

80211AC MIMOOFDM

80211AH MIMOOFDM

80211AF MIMOOFDM

80211AX MIMOOFDM

80211BE MIMOOFDM

80211BN MIMOOFDM

[IMAGE alt='icon' src='niwlang-create-multiple-channel-waveform-iq-complex-cluster-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset? — reset? specifies whether to reset data. The default value is FALSE. TRUE Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. FALSE Does not reset the data. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. output waveform — output waveform returns an array of WLAN I/Q data. t0 — t0 returns the start time, in seconds. dt — dt returns the time interval, in seconds, between baseband I/Q samples. Y — Y returns the waveform data. generation done? — generation done? indicates whether the VI has generated all the data. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. |
| FALSE | Does not reset the data. |
| t0 — t0 returns the start time, in seconds. dt — dt returns the time interval, in seconds, between baseband I/Q samples. Y — Y returns the waveform data. |  |

Parent topic:

niWLANG Create Waveform VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-vi.html language=enus -->
## TOPIC 00103: niWLANG Create Multiple Channel Waveform VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q data for multiple channels and returns the data as an array of complex waveforms. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the ge

### niWLANG Create Multiple Channel Waveform VI

Creates WLAN I/Q data for multiple channels and returns the data as an array of complex waveforms. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the **reset?** parameter to FALSE and run the VI in a loop for a specified number of times or until the **generation done?** parameter is TRUE.

Note

Standard

80211N MIMOOFDM

80211AC MIMOOFDM

80211AH MIMOOFDM

80211AF MIMOOFDM

80211AX MIMOOFDM

80211BE MIMOOFDM

80211BN MIMOOFDM

[IMAGE alt='icon' src='niwlang-create-multiple-channel-waveform-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset? — reset? specifies whether to reset data. The default value is FALSE. TRUE Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. FALSE Does not reset the data. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. output waveform — output waveform returns an array of WLAN I/Q data. generation done? — generation done? indicates whether the VI has generated all the data. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. |
| FALSE | Does not reset the data. |

Parent topic:

niWLANG Create Waveform VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-iq-complex-cluster-vi.html language=enus -->
## TOPIC 00104: niWLANG Create Single Channel Waveform (IQ Complex Cluster) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-iq-complex-cluster-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-iq-complex-cluster-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q data and returns the data as a complex cluster. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the generation done? parameter is TRUE.

### niWLANG Create Single Channel Waveform (IQ Complex Cluster) VI

Creates WLAN I/Q data and returns the data as a complex cluster. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the **reset?** parameter to FALSE and run the VI in a loop for a specified number of times or until the **generation done?** parameter is TRUE.

Note

Standard

80211A/G OFDM

80211J OFDM

80211P OFDM

80211B/G DSSS

80211G DSSSOFDM

[IMAGE alt='icon' src='niwlang-create-single-channel-waveform-iq-complex-cluster-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset? — reset? specifies whether to reset data. The default value is FALSE. TRUE Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. FALSE Does not reset the data. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. output waveform — output waveform returns the WLAN I/Q data. t0 — t0 returns the start time, in seconds. dt — dt returns the time interval, in seconds, between baseband I/Q samples. Y — Y returns the waveform data. generation done? — generation done? indicates whether the VI has generated all the data. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. |
| FALSE | Does not reset the data. |
| t0 — t0 returns the start time, in seconds. dt — dt returns the time interval, in seconds, between baseband I/Q samples. Y — Y returns the waveform data. |  |

Parent topic:

niWLANG Create Waveform VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-vi.html language=enus -->
## TOPIC 00105: niWLANG Create Single Channel Waveform VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q data and returns the data as a complex waveform. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set reset? to FALSE and run the VI in a loop for a specified number of times or until the generation done? output is TRUE. Use this instanc

### niWLANG Create Single Channel Waveform VI

Creates WLAN I/Q data and returns the data as a complex waveform. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set **reset?** to FALSE and run the VI in a loop for a specified number of times or until the **generation done?** output is TRUE.

Note

Standard

80211A/G OFDM

80211J OFDM

80211P OFDM

80211B/G DSSS

80211G DSSSOFDM

[IMAGE alt='icon' src='niwlang-create-single-channel-waveform-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. reset? — reset? specifies whether to reset data. The default value is FALSE. TRUE Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. FALSE Does not reset the data. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. output waveform — output waveform returns the WLAN I/Q data. generation done? — generation done? indicates whether the VI has generated all the data. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TRUE | Resets the data. Set this parameter to TRUE after you have generated the required number of frames or if you want to reset the pseudonoise (PN) seed. |
| FALSE | Does not reset the data. |

Parent topic:

niWLANG Create Waveform VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-create-waveform-vi.html language=enus -->
## TOPIC 00106: niWLANG Create Waveform VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-create-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-create-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates WLAN I/Q waveform data according to the properties that you specify. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the generation done? paramet

### niWLANG Create Waveform VI

Creates WLAN I/Q waveform data according to the properties that you specify. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the **reset?** parameter to FALSE and run the VI in a loop for a specified number of times or until the **generation done?** parameter is TRUE.

[IMAGE alt='icon' src='niwlang-create-waveform-vi.png']

- [niWLANG Create Single Channel Waveform VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-vi.html) Creates WLAN I/Q data and returns the data as a complex waveform. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set reset? to FALSE and run the VI in a loop for a specified number of times or until the generation done? output is TRUE.
- [niWLANG Create Single Channel Waveform (IQ Complex Cluster) VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-create-single-channel-waveform-iq-complex-cluster-vi.html) Creates WLAN I/Q data and returns the data as a complex cluster. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the generation done? parameter is TRUE.
- [niWLANG Create Multiple Channel Waveform VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-vi.html) Creates WLAN I/Q data for multiple channels and returns the data as an array of complex waveforms. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the generation done? parameter is TRUE.
- [niWLANG Create Multiple Channel Waveform (IQ Complex Cluster) VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-create-multiple-channel-waveform-iq-complex-cluster-vi.html) Creates WLAN I/Q data for multiple channels and returns the data as an array of complex clusters. This VI returns one frame, including the idle interval, at a time. For multi-frame generation, set the reset? parameter to FALSE and run the VI in a loop for a specified number of times or until the generation done? parameter is TRUE.

Parent topic:

Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-get-number-of-users-from-ru-allocation-vi.html language=enus -->
## TOPIC 00107: niWLANG Get Number of Users from RU Allocation VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-get-number-of-users-from-ru-allocation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-get-number-of-users-from-ru-allocation-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of users derived from the configured RU allocation in a 802.11ax MU PPDU or 802.11be MU PPDU signal. To use this VI, you must set the RU Allocation Mode property to Group and configure the RU Allocation property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan

### niWLANG Get Number of Users from RU Allocation VI

Returns the number of users derived from the configured RU allocation in a 802.11ax MU PPDU or 802.11be MU PPDU signal. To use this VI, you must set the [RU Allocation Mode](/csh?context=rfmxwlangen_lvwlangenprop_attrcd) property to **Group** and configure the [RU Allocation](/csh?context=rfmxwlangen_lvwlangenprop_attrce) property.

[IMAGE alt='icon' src='niwlang-get-number-of-users-from-ru-allocation-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. number of users — number of users returns the number of users in 802.11ax MU PPDU signal. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Generation Information

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-get-ofdm-allocation-map-trace-vi.html language=enus -->
## TOPIC 00108: niWLANG Get OFDM Allocation Map Trace VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-get-ofdm-allocation-map-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-get-ofdm-allocation-map-trace-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a map of allocation of users in space frequency grid, for the 802.11ax MU PPDU and Trigger-Based PPDU signals, 802.11be MU PPDU and Trigger-Based PPDU signals and 802.11bn MU PPDU and Trigger-Based PPDU signals. icon Inputs/Outputs cigrn.png intensity graph refnum intensity graph refnum spec

### niWLANG Get OFDM Allocation Map Trace VI

Returns a map of allocation of users in space frequency grid, for the 802.11ax MU PPDU and Trigger-Based PPDU signals, 802.11be MU PPDU and Trigger-Based PPDU signals and 802.11bn MU PPDU and Trigger-Based PPDU signals.

[IMAGE alt='icon' src='niwlang-get-ofdm-allocation-map-trace-vi.png']

#### Inputs/Outputs

| intensity graph refnum — intensity graph refnum specifies the reference to the intensity graph on which space frequency map will be displayed. niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. space frequency map — space frequency map returns an array of the space frequency maps of the set configuration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Generation Information

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-load-configuration-from-file-vi.html language=enus -->
## TOPIC 00109: niWLANG Load Configuration from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-load-configuration-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-load-configuration-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the properties of a session saved in a file. icon Inputs/Outputs cbool.png reset session? reset session? specifies whether to reset all the properties of the session before loading the settings from a file. The default value is TRUE. cgenclassrn.png niwlan generation session niwlan generation

### niWLANG Load Configuration from File VI

Loads the properties of a session saved in a file.

[IMAGE alt='icon' src='niwlang-load-configuration-from-file-vi.png']

#### Inputs/Outputs

| reset session? — reset session? specifies whether to reset all the properties of the session before loading the settings from a file. The default value is TRUE. niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. file path — file path specifies the complete path to the file from which the WLAN Generation loads the configuration. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-open-session-vi.html language=enus -->
## TOPIC 00110: niWLANG Open Session VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-open-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-open-session-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Looks up an existing WLAN generation session using the session name parameter and returns the refnum that you can pass to subsequent niWLAN Generation VIs and the niWLANG Property Node. If the look up fails, the niWLANG Open Session VI creates a new niWLAN generation session and returns a new refnum

### niWLANG Open Session VI

Looks up an existing WLAN generation session using the **session name** parameter and returns the refnum that you can pass to subsequent niWLAN Generation VIs and the [niWLANG Property Node](/csh?context=rfmxwlangen_lvwlangenref_niwlang_property_node). If the look up fails, the niWLANG Open Session VI creates a new niWLAN generation session and returns a new refnum.

[IMAGE alt='icon' src='niwlang-open-session-vi.png']

#### Inputs/Outputs

| session name — session name specifies the name of the session that you are looking up or creating. If a session with the same name already exists, this VI returns a reference to that session. To get the reference to an already-opened session x, specify x as the session name. You can obtain the reference to an existing session multiple times if you have not called the niWLANG Close Session VI in that session. You do not need to close the session multiple times. To create an unnamed session, pass an empty string to the session name parameter or leave this parameter unwired. Tip NI recommends that you call the niWLANG Close Session VI for each unique named instance of the niWLANG Open Session VI or each instance of the niWLANG Open Session VI with an unnamed session. toolkit compatibility version — toolkit compatibility version specifies the version of the WLAN Generation to which the current version of the WLAN Generation is compatible. If the behavior of the WLAN Generation changes in a new version, use this parameter to specify that you want to continue using the behavior of the previous release. The default value is 6.0.0. 1.0.0 (10000) Specifies that the WLAN Generation exhibits version 1.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 1.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 1.0.0 and later versions. 2.0.0 (20000) Specifies that the WLAN Generation exhibits version 2.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 2.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 2.0.0 and 3.0.0. 3.0.0 (30000) Specifies that the WLAN Generation exhibits version 3.0.0 behavior. Select this option if you want 3.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 2.0.0 and 3.0.0. 4.0.0 (40000) Specifies that the WLAN Generation exhibits version 4.0.0 behavior. Select this option if you want 4.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 3.0.0 and 4.0.0. 5.0.0 (50000) Specifies that the WLAN Generation exhibits version 5.0.0 behavior. Select this option if you want 5.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 4.0.0 and 5.0.0. 6.0.0 (60000) Specifies that the WLAN Generation exhibits version 6.0.0 behavior. Select this option if you want 6.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 5.0.0 and 6.0.0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session — niwlan generation session returns the niWLAN generation session refnum. Use this parameter to configure the behavior and operation of the appropriate RFmx WLAN Generation VIs that accept the niwlan generation session refnum as an input. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. new session? — new session? indicates whether the VI creates a new session. TRUE Indicates that the VI creates a new session. FALSE Indicates that the VI returns a reference to an existing session. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 1.0.0 (10000) | Specifies that the WLAN Generation exhibits version 1.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 1.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 1.0.0 and later versions. |
| 2.0.0 (20000) | Specifies that the WLAN Generation exhibits version 2.0.0 behavior, and all new features in later releases are unavailable. Select this option if you purchased version 2.0.0 and want to maintain functional behavior. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 2.0.0 and 3.0.0. |
| 3.0.0 (30000) | Specifies that the WLAN Generation exhibits version 3.0.0 behavior. Select this option if you want 3.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 2.0.0 and 3.0.0. |
| 4.0.0 (40000) | Specifies that the WLAN Generation exhibits version 4.0.0 behavior. Select this option if you want 4.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 3.0.0 and 4.0.0. |
| 5.0.0 (50000) | Specifies that the WLAN Generation exhibits version 5.0.0 behavior. Select this option if you want 5.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 4.0.0 and 5.0.0. |
| 6.0.0 (60000) | Specifies that the WLAN Generation exhibits version 6.0.0 behavior. Select this option if you want 6.0.0 behavior and access to new features and bug fixes. Refer to the RFmx WLAN Generation Readme for a list of changes between versions 5.0.0 and 6.0.0. |
| TRUE | Indicates that the VI creates a new session. |
| FALSE | Indicates that the VI returns a reference to an existing session. |

Parent topic:

Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-property-node-vi.html language=enus -->
## TOPIC 00111: niWLANG Property Node VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-property-node-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets (writes) or gets (reads) niWLAN Generation properties. Some niWLAN Generation properties are channel based. When a property is channel based, you must specify an active channel before setting or getting properties. icon Inputs/Outputs cgenclassrn.png niWLANGeneration session niwlan generation s

### niWLANG Property Node VI

Sets (writes) or gets (reads) [niWLAN Generation properties](/csh?context=rfmxwlangen_lvwlangenprop_cniwlangeneration).

Some niWLAN Generation properties are channel based. When a property is channel based, you must specify an [active channel](/csh?context=rfmxwlangen_wlangen_config_gen_active_channel_lv) before setting or getting properties.

[IMAGE alt='icon' src='niwlang-property-node-vi.png']

#### Inputs/Outputs

| niWLANGeneration session — niwlan generation session specifies the niWLAN generation session refnum. error in (no error) — error in(no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — Property is used to get (read), set (write), or reset (set to default value) RFmx WLAN Gen properties. niWLANGeneration session — niwlan generation session passes reference of the WLAN generation session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-read-burst-start-locations-from-file-vi.html language=enus -->
## TOPIC 00112: niWLANG Read Burst Start Locations from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-read-burst-start-locations-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-read-burst-start-locations-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the burst start locations from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the niWLANG Create and Write Waveforms to File VI in a programming environment. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from w

### niWLANG Read Burst Start Locations from File VI

Reads the burst start locations from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the [niWLANG Create and Write Waveforms to File](/csh?topicname=niwlang-create-and-write-waveforms-to-file-vi.html) VI in a programming environment.

[IMAGE alt='icon' src='niwlang-read-burst-start-locations-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the WLAN Generation reads the waveform. waveform name — waveform name specifies the name of the waveform to read from the file. For example, use the channel0 string as a waveform name to read the waveform for channel 0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. burst start locations — burst start locations returns the burst start locations saved in the TDMS file. It is an array of sample positions of the start of the burst, within the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-read-burst-stop-locations-from-file-vi.html language=enus -->
## TOPIC 00113: niWLANG Read Burst Stop Locations from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-read-burst-stop-locations-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-read-burst-stop-locations-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the burst stop locations from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the niWLANG Create and Write Waveforms to File VI in a programming environment. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file from wh

### niWLANG Read Burst Stop Locations from File VI

Reads the burst stop locations from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the [niWLANG Create and Write Waveforms to File](/csh?topicname=niwlang-create-and-write-waveforms-to-file-vi.html) VI in a programming environment.

[IMAGE alt='icon' src='niwlang-read-burst-stop-locations-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the WLAN Generation reads the waveform. waveform name — waveform name specifies the name of the waveform to read from the file. For example, use the channel0 string as a waveform name to read the waveform for channel 0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. burst stop locations — burst stop locations returns the burst stop locations saved in the TDMS file. It is an array of sample positions of the end of the burst, within the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-read-rf-blanking-marker-positions-from-file-vi.html language=enus -->
## TOPIC 00114: niWLANG Read RF Blanking Marker Positions from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-read-rf-blanking-marker-positions-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-read-rf-blanking-marker-positions-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads RF blanking marker positions from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the niWLANG Create and Write Waveforms to File VI in a programming environment. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file fro

### niWLANG Read RF Blanking Marker Positions from File VI

Reads RF blanking marker positions from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the [niWLANG Create and Write Waveforms to File](/csh?context=rfmxwlangen_lvwlangenref_niwlang_create_and_write_waveforms_to_file) VI in a programming environment.

[IMAGE alt='icon' src='niwlang-read-rf-blanking-marker-positions-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the WLAN Generation reads the waveform. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RF blanking marker positions — RF blanking marker positions returns the RF blanking marker positions saved in the TDMS file. It is an array of sample positions, within waveform, of marker events that can be used to toggle the state of RF blanking. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-read-waveform-from-file-vi.html language=enus -->
## TOPIC 00115: niWLANG Read Waveform from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-read-waveform-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-read-waveform-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads a waveform from a TDMS file. You can save this file using the WLAN Generation Soft Front Panel. This VI returns headroom and I/Q rate waveform data that you can subsequently download to an NI RF vector signal generator. icon Inputs/Outputs ci64.png count count specifies the maximum number of s

### niWLANG Read Waveform from File VI

Reads a waveform from a TDMS file. You can save this file using the *WLAN Generation Soft Front Panel*. This VI returns headroom and I/Q rate waveform data that you can subsequently download to an NI RF vector signal generator.

[IMAGE alt='icon' src='niwlang-read-waveform-from-file-vi.png']

#### Inputs/Outputs

| count — count specifies the maximum number of samples of the I/Q complex waveform to read from the file. The default value is -1, which returns all samples. If you set count to 1,000 and offset to 2, the VI returns 1,000 samples, starting from index 2 and ending at index 1,002. offset — offset specifies the number of waveform samples at which the VI begins reading the I/Q data. The default value is 0. If you set count to 1,000 and offset to 2, the VI returns 1,000 samples, starting from index 2 and ending at index 1,002. file path — file path specifies the absolute path to the TDMS file from which the WLAN Generation reads the waveform. waveform name — waveform name specifies the name of the waveform to read from the file. For example, use the channel0 string as a waveform name to read the waveform for channel 0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveform — waveform returns the waveform saved in a TDMS file. t0 — t0 returns the start time, in seconds, of the Y array. dt — dt returns the time interval, in seconds, between the samples in the Y array. The reciprocal of dt indicates the I/Q rate of the signal. Y — Y returns an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. IQ rate (S/s) — IQ rate returns the I/Q rate, in samples per second (S/s), of the waveform. headroom (dB) — headroom returns the headroom, in dB, of the waveform. error out — error out contains error information. This output provides standard error out functionality. eof — eof indicates whether the end of file has been reached with this read. |
| --- |
| t0 — t0 returns the start time, in seconds, of the Y array. dt — dt returns the time interval, in seconds, between the samples in the Y array. The reciprocal of dt indicates the I/Q rate of the signal. Y — Y returns an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

#### Details

| Standard Property Value | Active Channel String Syntax | Comments |
| --- | --- | --- |
| 80211A/G OFDM, 80211J OFDM, 80211P OFDM, 80211B/G DSSS, or 80211G DSSSOFDM | "" | "" for all waveforms |
| 80211N MIMOOFDM, 80211AH MIMOOFDM, 80211BE MIMOOFDM, 80211BN MIMOOFDM | "channelx" | "channel1" for a waveform of channel with index 1 |
| 80211AC MIMOOFDM, 80211AF MIMOOFDM, 80211AX MIMOOFDM | "[segmentz/]channelx" | "segment1/channel0" for a waveform of channel with index 0 of segment with index 1. "segment0/" is optional if the segment index is 0. |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-read-waveform-names-from-file-vi.html language=enus -->
## TOPIC 00116: niWLANG Read Waveform Names from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-read-waveform-names-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-read-waveform-names-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads names of all waveforms present in a TDMS file. You can save this file using the WLAN Generation Soft Front Panel or the niWLANG Create and Write Waveforms to File VI in a programming environment. icon Inputs/Outputs cpath.png file path file path specifies the absolute path to the TDMS file fro

### niWLANG Read Waveform Names from File VI

Reads names of all waveforms present in a TDMS file. You can save this file using the *WLAN Generation Soft Front Panel* or the [niWLANG Create and Write Waveforms to File](/csh?context=rfmxwlangen_lvwlangenref_niwlang_create_and_write_waveforms_to_file) VI in a programming environment.

[IMAGE alt='icon' src='niwlang-read-waveform-names-from-file-vi.png']

#### Inputs/Outputs

| file path — file path specifies the absolute path to the TDMS file from which the WLAN Generation reads the waveform. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. waveform names — waveform names returns an array of names of all the waveforms present in the TDMS file. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-reset-session-vi.html language=enus -->
## TOPIC 00117: niWLANG Reset Session VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-reset-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-reset-session-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets all the properties of the session to their default values. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan generation session specifies the niWLAN generation session refnum. cerrcodeclst.png error in error in describes error conditions that occur before this node runs. Th

### niWLANG Reset Session VI

Resets all the properties of the session to their default values.

[IMAGE alt='icon' src='niwlang-reset-session-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-multiple-lo-vi.html language=enus -->
## TOPIC 00118: niWLANG RFSG Configure Frequency (Multiple LO) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-multiple-lo-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-multiple-lo-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external LO devices. This VI also configures LO frequency offset based on the LO Frequency Offset Mode and LO Frequency Offset properties. This VI equally divides the NI RF vector signal

### niWLANG RFSG Configure Frequency (Multiple LO) VI

Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external LO devices. This VI also configures LO frequency offset based on the LO Frequency Offset Mode and LO Frequency Offset properties. This VI equally divides the NI RF vector signal generators and NI RF synthesizers into sets such that each set corresponds to one carrier frequency. The number of sets is equal to the size of the carrier frequencies array. In each set, the first NI RF vector signal generator is used as the master device for LO daisy chaining. It also configures the Signal Bandwidth and IQ Rate properties on NI RF vector signal generators and the Carrier Frequency property.

[IMAGE alt='icon' src='niwlang-rfsg-configure-frequency-multiple-lo-vi.png']

#### Inputs/Outputs

| external LO handles — external LO handles identifies the instrument sessions of external LO devices. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. RFSG handles — RFSG handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. carrier frequencies (Hz) — carrier frequencies specifies an array of the carrier frequencies used to generate signals. This value is expressed in Hz. LO source — LO source specifies whether to use the internal or the external LO source. This value is applicable only for the first RFSG device within a set if the RFSG LO daisy-chain enabled parameter is set to True. The default value is Onboard. Onboard (0) Uses an internal LO as the LO source. External (1) Uses an external LO as the LO source. SG SA Shared (2) Shares the internal RFSG LO between RFSG and RFSA. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RFSG LO daisy-chain enabled — RFSG LO daisy-chain enabled specifies whether to export the LO signal from one RFSG device to the next. The default value is FALSE. LO export to external devices enabled — LO export to external devices enabled specifies whether to export the LO signal from each RFSG device on its LO OUT terminal, which you can use to share the LO signal with an external device. An example of an external device would be an RFSA device. The default value is FALSE. external LO handles out — external LO handles out passes an array of references from the external LO sessions to the next VI. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. RFSG handles out — RFSG handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Onboard (0) | Uses an internal LO as the LO source. |
| External (1) | Uses an external LO as the LO source. |
| SG SA Shared (2) | Shares the internal RFSG LO between RFSG and RFSA. |

Parent topic:

niWLANG RFSG Configure Frequency VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-single-lo-vi.html language=enus -->
## TOPIC 00119: niWLANG RFSG Configure Frequency (Single LO) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-single-lo-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-single-lo-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external local oscillator (LO) devices. This VI also configures LO frequency offset based on the LO Frequency Offset Mode and LO Frequency Offset properties. It also configures the Signa

### niWLANG RFSG Configure Frequency (Single LO) VI

Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external local oscillator (LO) devices. This VI also configures LO frequency offset based on the [LO Frequency Offset Mode](/csh?context=rfmxwlangen_lvwlangenprop_attrb0) and [LO Frequency Offset](/csh?context=rfmxwlangen_lvwlangenprop_attrb1) properties. It also configures the Signal Bandwidth and IQ Rate properties on NI RF vector signal generators and the Carrier Frequency property.

[IMAGE alt='icon' src='niwlang-rfsg-configure-frequency-single-lo-vi.png']

#### Inputs/Outputs

| external LO handle — external LO handle identifies the instrument session of the external LO device. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. RFSG handles — RFSG handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. carrier frequency (Hz) — carrier frequency specifies the carrier frequency used to generate signals. This value is expressed in Hz. LO source — LO source specifies whether to use the internal or the external LO source. This value is applicable only for the first RFSG device within a set if the RFSG LO daisy-chain enabled parameter is set to True. The default value is Onboard. Onboard (0) Uses an internal LO as the LO source. External (1) Uses an external LO as the LO source. SG SA Shared (2) Shares the internal RFSG LO between RFSG and RFSA. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RFSG LO daisy-chain enabled — RFSG LO daisy-chain enabled specifies whether to export the LO signal from one RFSG device to the next. The default value is FALSE. LO export to external devices enabled — LO export to external devices enabled specifies whether to export the LO signal from each RFSG device on its LO OUT terminal, which you can use to share the LO signal with an external device. An example of an external device would be an RFSA device. The default value is FALSE. external LO handle out — external LO handle out passes a reference from the external LO session to the next VI. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. RFSG handles out — RFSG handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Onboard (0) | Uses an internal LO as the LO source. |
| External (1) | Uses an external LO as the LO source. |
| SG SA Shared (2) | Shares the internal RFSG LO between RFSG and RFSA. |

Parent topic:

niWLANG RFSG Configure Frequency VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-vi.html language=enus -->
## TOPIC 00120: niWLANG RFSG Configure Frequency VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the frequency on NI RF vector signal generators, and NI RF synthesizers used as external LO devices. It also configures the Carrier Frequency property. You must ensure that after a frequency configuration change, the output of the external LO device settles before generating the WLAN sign

### niWLANG RFSG Configure Frequency VI

Configures the frequency on NI RF vector signal generators, and NI RF synthesizers used as external LO devices. It also configures the [Carrier Frequency](/csh?context=rfmxwlangen_lvwlangenprop_attr0) property.

You must ensure that after a frequency configuration change, the output of the external LO device settles before generating the WLAN signal. You must use one of the following programming flows:

- Before calling the niWLANG RFSG Configure Frequency VI, if the external LO device is in generation state, ensure that it is brought in configuration state, by stopping signal generation. Initiate signal generation on the external LO device after calling the niWLANG RFSG Configure Frequency VI.
- You may choose to do on-the-fly frequency change on the external LO device while the device is in generation state. You must allow its output to settle by calling the niRFSG Wait Until Settled VI after the niWLANG RFSG Configure Frequency VI.

[IMAGE alt='icon' src='niwlang-rfsg-configure-frequency-vi.png']

- [niWLANG RFSG Configure Frequency (Single LO) VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-single-lo-vi.html) Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external local oscillator (LO) devices. This VI also configures LO frequency offset based on the LO Frequency Offset Mode and LO Frequency Offset properties. It also configures the Signal Bandwidth and IQ Rate properties on NI RF vector signal generators and the Carrier Frequency property.
- [niWLANG RFSG Configure Frequency (Multiple LO) VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-frequency-multiple-lo-vi.html) Configures the frequency on NI RF vector signal generators and NI RF synthesizers. NI RF synthesizers are used as external LO devices. This VI also configures LO frequency offset based on the LO Frequency Offset Mode and LO Frequency Offset properties. This VI equally divides the NI RF vector signal generators and NI RF synthesizers into sets such that each set corresponds to one carrier frequency. The number of sets is equal to the size of the carrier frequencies array. In each set, the first NI RF vector signal generator is used as the master device for LO daisy chaining. It also configures the Signal Bandwidth and IQ Rate properties on NI RF vector signal generators and the Carrier Frequency property.

Parent topic:

Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-multiple-device-synchronization-vi.html language=enus -->
## TOPIC 00121: niWLANG RFSG Configure Multiple Device Synchronization VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-multiple-device-synchronization-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-configure-multiple-device-synchronization-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures multiple NI RF vector signal generators for sharing the local oscillator (LO), configures the Reference Clock settings, and synchronizes multiple devices. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan generation session specifies the niWLAN generation session refnum

### niWLANG RFSG Configure Multiple Device Synchronization VI

Configures multiple NI RF vector signal generators for sharing the local oscillator (LO), configures the Reference Clock settings, and synchronizes multiple devices.

[IMAGE alt='icon' src='niwlang-rfsg-configure-multiple-device-synchronization-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. instrument handles — instrument handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. master reference clock source — master reference clock source specifies the device Reference Clock to configure on the master NI RF vector signal generator. The default value is PXI_CLK. OnboardClock (OnboardClock) Uses the onboard Reference Clock as the clock source. RefIn (RefIn) Uses the clock signal present at the front panel REF IN connector as the clock source. PXI_CLK (PXI_CLK) Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source. ClkIn (ClkIn) Uses the clock signal present at the front panel CLK IN connector as the clock source. PXI trigger lines — PXI trigger lines specifies the array of trigger lines used for distribution of synchronized trigger signals. The default value is "" (empty string). The valid values are PXI_Trig0, PXI_Trig1, PXI_Trig2, PXI_Trig3, PXI_Trig4, PXI_Trig5, PXI_Trig6, PXI_Trig7, and PFI0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. instrument handles out — instrument handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| OnboardClock (OnboardClock) | Uses the onboard Reference Clock as the clock source. |
| RefIn (RefIn) | Uses the clock signal present at the front panel REF IN connector as the clock source. |
| PXI_CLK (PXI_CLK) | Uses the PXI_CLK signal, which is present on the PXI backplane, as the clock source. |
| ClkIn (ClkIn) | Uses the clock signal present at the front panel CLK IN connector as the clock source. |

#### Details

For PXIe-5673/5673E/5840/5841/5830/5831 RF vector signal generators, this VI configures LO sharing and clock settings in daisy-chained manner.

For PXIe-5644, PXIe-5645, and PXIe-5646 RF vector signal transceiver (VST) devices, this VI configures daisy-chained LO sharing and low-level properties for multidevice synchronization. These VSTs do not support daisy-chained Reference Clocks for synchronization. You must set the master Reference Clock source to PXI_CLK for these devices.

For PXIe-5840/5841/5830/5831 RF VST devices, this VI configures daisy-chained LO sharing and Reference Clocks for synchronization, and for PXIe-5820 baseband I/Q VST devices, this VI configures daisy-chained Reference Clocks for synchronization. For additional information, refer to the *Synchronization Using NI-RFSA and NI-RFSG* topic in the *NI RF Signal Generators Help*.

For PXIe-5842/5860 RF VST devices, this VI configures Reference Clock settings for synchronization and applies NI-TClk trigger configuration for multi-chassis setups. PXIe-5860 does not support LO sharing, and synchronization is achieved through a common reference clock and NI-TClk.

This VI assumes that the devices are interconnected in the same order as the elements in the instrument handles array. In time synchronization, assume the first device is the master device, and the remaining devices the slave devices. The VI divides the devices into two sets when the number of segments is two. In LO sharing, the first device in
 each set is assumed to be the master device, and the remaining devices in the set are assumed to be slave devices. To interconnect multiple devices, refer to the following topics in the *NI RF Signal Generators Help*:

- Interconnecting Multiple PXIe-5673E Modules
- Interconnecting Multiple PXIe-5673 Modules
- Interconnecting Multiple PXIe-5644 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5645 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5646 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5840 RF Channels (Homogeneous Channel Types)
- Interconnecting Multiple PXIe-5841 RF Channels (Homogeneous Channel Types)

If you use PXIe-5644, PXIe-5645, or PXIe-5646 RF VSTs, the VI completes the following actions:

- The VI sets the niRFSG Reference Clock Source to the value you specify in the master reference clock source parameter.
- If you set the LO Sharing Enabled property to True , the VI completes the following actions.
  - For the master device, the VI exports the LO by setting the niRFSG LO Out Enabled property to True . The VI also reads the niRFSG Upconverter Center Frequency property so that the value can be set on the slave devices.
  - For the slave devices, the VI sets the niRFSG LO Source property to LO IN and the niRFSG Upconverter Center Frequency property to the value read from the master device. With the exception of the last slave device, the VI also exports the LO to the next device in the daisy chain by setting the niRFSG LO Out Enabled property to True .
- The VI configures the trigger synchronization for the master and slave devices.
  - For the master device, the VI completes the following actions:
    - Sets the niRFSG Sync Start Trigger Master property to True . For PXIe-5646R, the VI sets the niRFSG Sync Sample Clock Master property to True .
    - Sets the niRFSG Sync Start Dist Line property to the first element of the PXI trigger lines . For PXIe-5646, the VI sets the niRFSG Sync Sample Clock Dist Line property to the second element of the PXI trigger lines array.
    - Calls the niRFSG Commit VI to commit the synchronization settings to the device.
  - For the slave devices, the VI completes the following actions:
    - Sets the niRFSG Sync Start Trigger Master property to False . For PXIe-5646, the VI sets the niRFSG Sync Sample Clock Master Property to False .
    - Sets the niRFSG Sync Start Dist Line property to the first element of the PXI trigger lines. For PXIe-5646, the VI sets the niRFSG Sync Sample Clock Dist Line property to the second element of the PXI trigger lines array.
    - Sets the niRFSG Start Trigger Type property to Digital Edge and the niRFSG Start Trigger Digital Edge Source property to sync_start .

If you use PXIe-5673/5673E RF vector signal generator, the VI completes the following actions:

- The VI configures the devices for daisy-chained Reference Clock synchronization.
  - For the master device, the VI sets the niRFSG Reference Clock Source property to the value you specify in master reference clock source and sets the niRFSG Reference Clock Export Output Terminal property to ClkOut .
  - For the slave devices, the VI sets the niRFSG Reference Clock Source property to ClkIn and sets the niRFSG Reference Clock Export Output Terminal property to ClkOut .
  - If you set the LO Sharing Enabled Property to True , the VI does the following actions:
    - For the master device, the VI exports the LO by setting the niRFSG LO Export Enabled property to True. The VI also reads the niRFSG LO Out Power(dBm) property so that it can be set on the next device in the daisy chain.
    - For the slave devices, the VI sets the niRFSG LO In Power (dBm) property to the value read from the master and reads the niRFSG LO Out Power (dBm) property. The VI also exports the LO to the next device in the daisy chain by setting the niRFSG LO Out Enabled property to True .

If you use PXIe-5840, PXIe-5841, PXIe-5830, or PXIe-5831 RF vector signal generators, the VI completes the following actions:

- For reference clock synchronization:
  - The VI configures all the devices to use PXI_CLK as reference clock if you set the master reference clock source parameter to PXI_CLK .
  - The VI configures the devices for daisy-chained reference clock synchronization, if you set the master reference clock source parameter to a value other than PXI_CLK .
    - For the master device, the VI sets the niRFSG Reference Clock Source property to the value you specify in the master reference clock source parameter and sets the niRFSG Reference Clock Exported Terminal property to RefOut .
    - For the slave devices, the VI sets the niRFSG Reference Clock Source property to RefIn . Except for the last slave device, this VI also sets the niRFSG Reference Clock Exported Terminal property to RefOut .

- If you set the LO Sharing Enabled property to True , the VI completes the following actions:
  - For the master device, the VI exports the LO by setting the niRFSG LO Out property to True . The VI also reads the niRFSG Upconverter Center Frequency property so that the value can be set on slave devices.
  - For the slave devices, the VI sets the niRFSG LO Source property to LO_In and the niRFSG Upconverter Center Frequency property to the value read from the master device. Except for the last slave device, this VI also exports the LO to the next device in the daisy chain by setting the niRFSG LO Out property to True .

If you use PXIe-5820 baseband I/Q vector signal generators, the VI completes the following actions:

- For reference clock synchronization:
  - The VI configures all the devices to use PXI_CLK as reference clock if you set the master reference clock source parameter to PXI_CLK .
  - The VI configures the devices for daisy-chained reference clock synchronization, if you set the master reference clock source parameter to a value other than PXI_CLK .
    - For the master device, the VI sets the niRFSG Reference Clock Source property to the value you specify in the master reference clock source parameter and sets the niRFSG Reference Clock Exported Terminal property to RefOut .
    - For the slave devices, the VI sets the niRFSG Reference Clock Source property to RefIn . Except for the last slave device, this VI also sets the niRFSG Reference Clock Exported Terminal property to RefOut .

If you use PXIe-5830 or PXIe-5831 RF vector signal generators, the VI completes the following actions:

- For reference clock synchronization:
  - The VI configures all the devices to use PXI_CLK as reference clock if you set the master reference clock source parameter to PXI_CLK .
  - The VI configures the devices for daisy-chained reference clock synchronization, if you set the master reference clock source parameter to a value other than PXI_CLK .
    - For the master device, the VI sets the niRFSG Reference Clock Source property to the value you specify in the master reference clock source parameter and sets the niRFSG Reference Clock Exported Terminal property to RefOut .
    - For the slave devices, the VI sets the niRFSG Reference Clock Source property to RefIn . Except for the last slave device, this VI also sets the niRFSG Reference Clock Exported Terminal property to RefOut .

- If you set the LO Sharing Enabled property to True , the VI completes the following actions:
  - For the master device, the VI exports the LO by setting the niRFSG LO Out property to True . The VI also reads the niRFSG Upconverter Center Frequency property so that the value can be set on slave devices.
  - For the slave devices, the VI sets the niRFSG LO Source property to LO_In and the niRFSG Upconverter Center Frequency property to the value read from the master device. Except for the last slave device, this VI also exports the LO to the next device in the daisy chain by setting the niRFSG LO Out property to True .

If you use PXIe-5842, or PXIe-5860 RF vector signal generators, the VI completes the following actions:

- For reference clock synchronization:
  - The VI configures all the devices to use PXI_CLK as reference clock if you set the master reference clock source parameter to PXI_CLK .
  - The VI configures the devices for daisy-chained reference clock synchronization, if you set the master reference clock source parameter to a value other than PXI_CLK .
    - For the master device, the VI sets the niRFSG Reference Clock Source property to the value you specify in the master reference clock source parameter and sets the niRFSG Reference Clock Exported Terminal property to RefOut .
    - For the slave devices, the VI sets the niRFSG Reference Clock Source property to RefIn . Except for the last slave device, this VI also sets the niRFSG Reference Clock Exported Terminal property to RefOut .

- If you set the Multi-Chassis TClk Synchronization Mode property to Timing Module , the VI performs Multi-Chassis TClk Synchronization using Timing Module.

- If you set the Multi-Chassis TClk Synchronization Mode property to Auto , the VI performs Multi-Chassis TClk Synchronization automatically.

Parent topic:

Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-single-channel-vi.html language=enus -->
## TOPIC 00122: niWLANG RFSG Create and Download Waveform (Single Channel) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-single-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-single-channel-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a single channel waveform, writes it into the RFSG memory, and stores the I/Q rate, burst start locations, burst stop locations, waveform size, and the actual headroom of the waveform in the RFSG database. Use this instance if the Standard property is set to 80211A/G OFDM, 80211J OFDM, 80211

### niWLANG RFSG Create and Download Waveform (Single Channel) VI

Creates a single channel waveform, writes it into the RFSG memory, and stores the I/Q rate, burst start locations, burst stop locations, waveform size, and the actual headroom of the waveform in the RFSG database.

Note

Standard

80211A/G OFDM

80211J OFDM

80211P OFDM

80211B/G DSSS

80211G DSSSOFDM

[IMAGE alt='icon' src='niwlang-rfsg-create-and-download-waveform-single-channel-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name used to write the waveform to NI-RFSG device memory and store its properties to RFSG database. This string is case-insensitive, alphanumeric, and does not use reserved words. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Inside the niWLANG Create and Download Waveform (Single Channel) VI, all the following operations that involve NI-RFSG are performed on the device. The niWLANG RFSG Create and Download Waveforms (Single Channel) VI completes the following operations:

1. Sets the Maximum Hardware IQ Rate property according to the device model. You must set the value of the Maximum Hardware IQ Rate property to 2500 MS/s if you are using the PXIe-5842, 1250 MS/s if you are using the PXIe-5840/5841/5841 with 5655/5820/5830/5831/5860, 250 MS/s if you are using the PXIe-5646R, 120 Ms/s if you are using the PXIe-5644R/5645R, and 200MS/s if you are using the PXIe-5673/5673E.
2. Reads the IQ Rate property and sets the niRFSG IQ Rate property to the value specified in the IQ Rate property. The value is stored in the RFSG database for the waveform and device.
3. If the RF Blanking Enabled property is set to True and the device model PXIe-5644R, PXIe-5645R, PXIe-5646R, PXIe-5840, PXIe-5841, PXIe-5841 with PXIe-5655, PXIe-5842, or PXIe-5860 is used, sets the niRFSG RF Blanking Source property to "marker0", if it is not set already.
4. Reads and stores the Signal Bandwidth property in the RFSG database for PXIe-5820/5830/5831/5841/5841 with 5655/5842/5860.
5. Reads and stores the Burst Start Locations property, the Burst Stop Locations property, and the waveform size in the RFSG database.
6. Creates the WLAN waveform and downloads it to device.
7. Stores the Actual Headroom property to the RFSG database.

Parent topic:

niWLANG RFSG Create and Download Waveform VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-vi.html language=enus -->
## TOPIC 00123: niWLANG RFSG Create and Download Waveform VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the waveform according to the parameters that you specify, writes it into the NI RF vector signal generator memory, and stores the I/Q rate and actual headroom of the waveform in the RFSG database. icon

### niWLANG RFSG Create and Download Waveform VI

Creates the waveform according to the parameters that you specify, writes it into the NI RF vector signal generator memory, and stores the I/Q rate and actual headroom of the waveform in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-create-and-download-waveform-vi.png']

- [niWLANG RFSG Create and Download Waveform (Single Channel) VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveform-single-channel-vi.html) Creates a single channel waveform, writes it into the RFSG memory, and stores the I/Q rate, burst start locations, burst stop locations, waveform size, and the actual headroom of the waveform in the RFSG database.
- [niWLANG RFSG Create and Download Waveforms (Multiple Channel) VI](../../../../vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveforms-multiple-channel-vi.html) The VI creates multiple channel waveforms, writes each waveform into the respective RFSG memory, and stores the I/Q rate, burst start locations, burst stop locations, waveform size, and the actual headroom for each channel of the waveform in the respective RFSG database , if you set the Standard property to 80211N MIMOOFDM , 80211AC MIMOOFDM , 80211AH MIMOOFDM , 80211AF MIMOOFDM , 80211AX MIMOOFDM , 80211BE MIMOOFDM , or 80211BN MIMOOFDM .

Parent topic:

RFSG Database

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveforms-multiple-channel-vi.html language=enus -->
## TOPIC 00124: niWLANG RFSG Create and Download Waveforms (Multiple Channel) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveforms-multiple-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-create-and-download-waveforms-multiple-channel-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The VI creates multiple channel waveforms, writes each waveform into the respective RFSG memory, and stores the I/Q rate, burst start locations, burst stop locations, waveform size, and the actual headroom for each channel of the waveform in the respective RFSG database, if you set the Standard prop

### niWLANG RFSG Create and Download Waveforms (Multiple Channel) VI

The VI creates multiple channel waveforms, writes each waveform into the respective RFSG memory, and stores the I/Q rate, burst start locations, burst stop locations, waveform size, and the actual headroom for each channel of the waveform in the respective [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database), if you set the [Standard](/csh?context=rfmxwlangen_lvwlangenprop_attr1f) property to **80211N MIMOOFDM**, **80211AC MIMOOFDM**, **80211AH MIMOOFDM**, **80211AF MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, or **80211BN MIMOOFDM**.

The VI creates a single channel waveform and writes the same waveform to RFSG memory of all devices, and stores the I/Q rate, burst start locations, burst stop locations, waveform size and actual headroom of the waveform in all RFSG databases, if you set the Standard property to **80211A/G OFDM**, **80211J OFDM**, **80211P OFDM**, **80211B/G DSSS**, or **80211G DSSSOFDM**.

[IMAGE alt='icon' src='niwlang-rfsg-create-and-download-waveforms-multiple-channel-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. instrument handles — instrument handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name used to write the waveform to NI-RFSG device memory and store its properties to RFSG database. This string is case-insensitive, alphanumeric, and does not use reserved words. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. instrument handles out — instrument handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Inside the niWLANG Create and Download Waveform (Multiple Channel) VI, all the operations listed below involving NI-RFSG are performed on the device corresponding to each channel. The niWLANG RFSG Create and Download Waveforms (Multiple Channel) VI completes the following operations.

1. Sets the Maximum Hardware IQ Rate property according to the device model. You must set the value of the Maximum Hardware IQ Rate property to 2500 MS/s if you are using the PXIe-5842, 1250 MS/s if you are using the PXIe-5840/5841/5820/5830/5831/5860, 250 MS/s if you are using the PXIe-5646, 120 Ms/s if you are using the PXIe-5644/5645, and 200MS/s if you are using the PXIe-5673/5673E.
2. Reads the IQ Rate property and sets the niRFSG IQ Rate property to the value specified in the IQ Rate property. The value is stored in the RFSG database for the waveform and device.
3. Sets the niRFSG RF Blanking Source property to "marker0" (if it is not set already), if the RF Blanking Enabled property is set to True and the device model PXIe-5644, PXIe-5645, PXIe-5646, PXIe-5840, PXIe-5841, PXIe-5842, or PXIe-5860 is used.
4. Reads and stores the Signal Bandwidth property in the RFSG database for PXIe-5820/5830/5831/5841/5842/5860.
5. Reads and stores the Burst Start Locations property, the Burst Stop Locations property, and the waveform size in the RFSG database.
6. Creates the WLAN waveform and downloads it to device.
7. Stores the Actual Headroom property to the RFSG database.

Parent topic:

niWLANG RFSG Create and Download Waveform VI

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-force-tclk-synchronization-vi.html language=enus -->
## TOPIC 00125: niWLANG RFSG Force TClk Synchronization VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-force-tclk-synchronization-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-force-tclk-synchronization-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies that the TClk synchronization has to be performed as the previous TClk synchronization is invalid due to niRFSG Reset VI. This setting will be used by niWLANG RFSG Synchronize TClk VI for TClk synchronization. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan generation

### niWLANG RFSG Force TClk Synchronization VI

Specifies that the TClk synchronization has to be performed as the previous TClk synchronization is invalid due to niRFSG Reset VI. This setting will be used by niWLANG RFSG Synchronize TClk VI for TClk synchronization.

[IMAGE alt='icon' src='niwlang-rfsg-force-tclk-synchronization-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. instrument handles — instrument handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. force sync? — force sync? specifies that a fresh TClk synchronization has to be performed for TClk synchronized generation. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. instrument handles out — instrument handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-multiple-device-initiate-vi.html language=enus -->
## TOPIC 00126: niWLANG RFSG Multiple Device Initiate VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-multiple-device-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-multiple-device-initiate-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to hardware, waits for hardware settling, and starts multi-device synchronized generation. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan generation session specifies the niWLAN generation session refnum. c1divrn.png instrument handles instrument handles identi

### niWLANG RFSG Multiple Device Initiate VI

Commits settings to hardware, waits for hardware settling, and starts multi-device synchronized generation.

[IMAGE alt='icon' src='niwlang-rfsg-multiple-device-initiate-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. instrument handles — instrument handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. instrument handles out — instrument handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

If you use PXIe-5644, PXIe-5645, or PXIe-5646, this VI performs the following steps:

- Commits the device settings to the master device by calling the niRFSG Commit VI.
- Initializes generation first for slave devices and then for the master device by calling the niRFSG Initiate VI in a loop.

If you use PXIe-5673/5673E, PXIe-5840, PXIe-5841, PXIe-5820, PXIe-5830, PXIe-5831, PXIe-5842, or PXIe-5860, this VI performs the following steps:

- If the number of devices required is more than 1, this VI uses the niWLANG RFSG Configure TClk For Homogeneous Triggers VI, niWLANG RFSG Synchronize TClk VI, and the niTClk Initiate VI for synchronized generation. 
 Refer to the NI-TClk Synchronization section of NI RF Vector Signal Generators help for more information about the niTClk VIs.
- Otherwise, this VI calls the niRFSG Initiate VI for the first device.

Parent topic:

Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-read-and-download-waveforms-from-file-vi.html language=enus -->
## TOPIC 00127: niWLANG RFSG Read and Download Waveforms from File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-read-and-download-waveforms-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-rfsg-read-and-download-waveforms-from-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads the waveforms stored in a TDMS file, writes them to the memory of the respective RF vector signal generato, and stores the I/Q rate, actual headroom, burst start locations, burst stop locations, waveform size, and RF blanking marker positions of the waveforms in the RFSG Database. icon Inputs/

### niWLANG RFSG Read and Download Waveforms from File VI

Reads the waveforms stored in a TDMS file, writes them to the memory of the respective RF vector signal generato, and stores the I/Q rate, actual headroom, burst start locations, burst stop locations, waveform size, and RF blanking marker positions of the waveforms in the [RFSG Database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-read-and-download-waveforms-from-file-vi.png']

#### Inputs/Outputs

| instrument handles — instrument handles identifies instruments for multiple NI-RFSG sessions. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. file path — file path specifies the absolute path to the TDMS file from which the WLAN Generation reads the waveforms. waveform name — waveform name specifies the names of the waveforms to clear. If you set this parameter as empty, the VI clears all the waveforms and their properties. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handles out — instrument handles out passes an array of RFSG instrument sessions to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

This VI completes the following tasks:

- Calls the niWLANG Read Waveform Names from File VI to read the names of all waveforms present in the TDMS file.
- Calls the niWLANG Read RF Blanking Marker Positions from File VI to read RF blanking marker positions.
- Completes the following tasks for each waveform in the file and corresponding NI-RFSG device (instrument handle).
  - Calls the niWLANG Read Waveform from File VI to read the waveform, along with its I/Q rate and headroom. The niRFSG I/Q Rate (S/s) property is set to the value of I/Q rate read from the file. The I/Q rate and headroom are stored in the RFSG database for the waveform specified in the waveform name parameter and NI-RFSG device.
  - For PXIe-5820/5830/5831/5841/5841 with 5655/5842/5860 devices, reads the signal bandwidth from the file and stores in the RFSG database for the waveform specified in the waveform name parameter and NI-RFSG device. If the value is not found in the file, then stores the value equal to 0.8*I/Q rate.
  - If the RF blanking marker positions, or burst start locations and burst stop locations read from the file are not empty arrays and are any of PXIe-5644, PXIe-5645, PXIe-5646, PXIe-5840, PXIe-5841, PXIe-5841 with PXIe-5655, PXIe-5842, or PXIe-5860 devices, the niRFSG RF Blanking Source property is set to "marker0", if it is not set. The RF blanking marker positions, burst start locations, burst stop locations, and the waveform size are stored in the RFSG database for the waveform specified in the waveform name parameter and the NI-RFSG device.
  - The VI downloads the waveform read from the file to the NI-RFSG device.

Note

Parent topic:

RFSG Database

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-save-configuration-to-file-vi.html language=enus -->
## TOPIC 00128: niWLANG Save Configuration to File VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-save-configuration-to-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-save-configuration-to-file-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Saves all properties of the session to a file located at a specified path. Use this file to save the current state of the WLAN Generation. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan generation session specifies the niWLAN generation session refnum. cpath.png file path file

### niWLANG Save Configuration to File VI

Saves all properties of the session to a file located at a specified path. Use this file to save the current state of the WLAN Generation.

[IMAGE alt='icon' src='niwlang-save-configuration-to-file-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. file path — file path specifies the complete path to the TDMS file to which the WLAN Generation saves the configuration. operation — operation specifies the operation to perform on the file. The default value is create or replace. open (0) Opens an existing file to write the niWLANG settings. open or create (1) Opens an existing file or creates a new file if the file does not exist. create or replace (2) Creates a new file or replaces an existing file. create (3) Creates a new file. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| open (0) | Opens an existing file to write the niWLANG settings. |
| open or create (1) | Opens an existing file or creates a new file if the file does not exist. |
| create or replace (2) | Creates a new file or replaces an existing file. |
| create (3) | Creates a new file. |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/niwlang-set-ofdm-packet-extension-thresholds-vi.html language=enus -->
## TOPIC 00129: niWLANG Set OFDM Packet Extension Thresholds VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/niwlang-set-ofdm-packet-extension-thresholds-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/niwlang-set-ofdm-packet-extension-thresholds-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the packet extension (PE) thresholds that determine the nominal packet padding of the 802.11ax, 802.11be or 802.11bn signal. This VI configures the thresholds for each resource unit (RU) size and each space-time stream of the 802.11ax, 802.11be or 802.11bn DUT. You must configure this tab

### niWLANG Set OFDM Packet Extension Thresholds VI

Configures the packet extension (PE) thresholds that determine the nominal packet padding of the 802.11ax, 802.11be or 802.11bn signal. This VI configures the thresholds for each resource unit (RU) size and each space-time stream of the 802.11ax, 802.11be or 802.11bn DUT. You must configure this table based on the nominal packet padding requirements of the DUT.

[IMAGE alt='icon' src='niwlang-set-ofdm-packet-extension-thresholds-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. RU size — RU size specifies the size of the RU in terms of the number of subcarriers. The default value is "" (empty array). number of space time streams — number of space time streams specifies the number of space-time streams for the corresponding RU size. The default value is "" (empty array). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. PPET8 — PPET8 specifies the 8 microsecond mode PE threshold values. The default value is "" (empty array). PPET16 — PPET16 specifies the 16 microsecond mode PE threshold values. The default value is "" (empty array). niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

The PE field of 802.11ax or 802.11be signal provides additional processing time to the receiver to decode the last symbol. The possible durations of the PE field are 0 microseconds, 4 microseconds, 8 microseconds, 12 microseconds, 16 microseconds, or 20 microseconds. The PE duration is determined by both the pre-FEC padding factor of the data field and the nominal packet padding requested by the recipient; and the modulation scheme of the current PPDU. The nominal packet padding as defined by the HE/EHT/UHR Capabilities element are 0 microseconds, 8 microseconds, 16 microseconds, and 20 microseconds, which can be specified using this VI.

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

The PE can be defined in two modes.

1. Nominal PE mode, 8 microseconds: PE duration is 0, 0, 4 and 8 microseconds for pre-FEC padding factor of 1, 2, 3, and 4 respectively
2. Nominal PE mode, 16 microseconds: PE duration is 4, 8, 12 and 16 microseconds for pre-FEC padding factor of 1, 2, 3, and 4 respectively
3. Nominal PE mode, 20 microseconds: PE duration is 8, 12, 16, and 20 microseconds for pre-FEC padding factor of 1, 2, 3, and 4 respectively

The nominal packet padding is calculated from the threshold values and the constellation index for the specified MCS index as follows.

- If the constellation is greater than or equal to PPET16, you must apply the value of the maximum PPET16 parameter, or if the constellation is greater than or equal to PPET8, you must apply the value of the maximum PPET8 parameter; otherwise, there is no packet extension.
- If no PE is required for all constellations, set PPET8 and PPET16 to "" (empty array).
- If only the nominal PE 8 microseconds mode is required, set PPET16 to be "" (empty array), and PPET8 to be the constellation at which max PE 8 microseconds mode starts.
- If only the nominal PE 16 microseconds mode is required, set PPET16 to be the constellation at which max PE 16 microseconds mode starts, and PPET8 to be "" (empty array).

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-clear-database-vi.html language=enus -->
## TOPIC 00130: niWLANG RFSG Clear Database VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-clear-database-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-clear-database-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the properties stored in the RFSG database and clears the waveforms from the RF vector signal generator memory. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the

### niWLANG RFSG Clear Database VI

Clears the properties stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database) and clears the waveforms from the RF vector signal generator memory.

[IMAGE alt='icon' src='niwlang-rfsg-clear-database-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the names of the waveforms to clear. If you set this parameter as empty, the VI clears all the waveforms and their properties. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

This VI clears the waveforms and the properties of the waveforms you specified in the **waveform name** parameter. If you do not set the **waveform name** parameter or set it to "" (empty string), this VI clears all the waveforms and their properties.

Parent topic:

RFSG Database

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-configure-power-level-vi.html language=enus -->
## TOPIC 00131: niWLANG RFSG Configure Power Level VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-configure-power-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-configure-power-level-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Looks up the waveforms in the script, retrieves the minimum actual headrooms of the waveforms in the script, adds this value to the power level parameter, and sets the result to the niRFSG Power Level property. Set the niRFSG Power Level Type property to Peak Power before calling this VI. icon Input

### niWLANG RFSG Configure Power Level VI

Looks up the waveforms in the script, retrieves the minimum actual headrooms of the waveforms in the script, adds this value to the **power level** parameter, and sets the result to the niRFSG Power Level property. Set the niRFSG Power Level Type property to **Peak Power** before calling this VI.

[IMAGE alt='icon' src='niwlang-rfsg-configure-power-level-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. script — script specifies the script that controls waveform generation. NI-RFSG supports multiple scripts that may be selected by name using the NI-RFSG Selected Script property. power level (dBm) — power level specifies the average power level, in dBm. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFSG Database

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-configure-script-vi.html language=enus -->
## TOPIC 00132: niWLANG RFSG Configure Script VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-configure-script-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-configure-script-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the I/Q rate and power level of the waveforms that you specify in the script parameter. If the I/Q rates are the same for all the waveforms, this VI sets the niRFSG IQ Rate property to the I/Q rate in the RFSG database. The VI sets the niRFSG Power Level property to the sum of the power l

### niWLANG RFSG Configure Script VI

Configures the I/Q rate and power level of the waveforms that you specify in the **script** parameter. If the I/Q rates are the same for all the waveforms, this VI sets the niRFSG IQ Rate property to the I/Q rate in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database). The VI sets the niRFSG Power Level property to the sum of the power level that you specify in the **power level** parameter and the minimum headroom value of all the waveforms.

[IMAGE alt='icon' src='niwlang-rfsg-configure-script-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. — script specifies the script that controls waveform generation. NI-RFSG supports multiple scripts that may be selected by name using the NI-RFSG Selected Script property. power level (dBm) — power level specifies the average power level, in dBm. The default value is -10 dBm. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

Note

niWLANG RFSG Create and Download Waveform

This VI completes the following tasks:

1. For devices other than PXIe 5820, calls the niWLANG RFSG Retrieve Minimum PAPR (Script) VI to retrieve the minimum peak-to-average power ratio (PAPR) across all waveforms present in the script parameter. The niRFSG Power Level property is set to the sum of the power level parameter and the minimum PAPR.
2. For PXIe 5820/5830/5831/5841/5841 with 5655/5842, calls niWLANG RFSG Retrieve Signal Bandwidth (Script) VI to retrieve the Signal Bandwidth and set niRFSG Signal Bandwidth to that value.
3. Calls the niWLANG RFSG Retrieve IQ Rate (Script) VI to retrieve the I/Q rate and sets niRFSG IQ Rate to the value.
4. Sets the niRFSG Power Level Type property to Peak Power .
5. Calls the niWLANG RFSG Insert RF Blanking Marker Positions VI to configure the script with RF blanking marker events.
6. Writes the resultant script to the NI-RFSG device using the niRFSG Write Script VI.
7. Parses the script name from the script parameter and sets the niRFSG Selected Script property to the value.

Parent topic:

RFSG Database

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-insert-rf-blanking-marker-positions-vi.html language=enus -->
## TOPIC 00133: niWLANG RFSG Insert RF Blanking Marker Positions VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-insert-rf-blanking-marker-positions-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-insert-rf-blanking-marker-positions-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the script you specify in the script parameter for RF blanking marker events. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options

### niWLANG RFSG Insert RF Blanking Marker Positions VI

Configures the script you specify in the **script** parameter for RF blanking marker events.

[IMAGE alt='icon' src='niwlang-rfsg-insert-rf-blanking-marker-positions-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. — script specifies the script that controls waveform generation. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. script out — script out returns the modified script that has RF blanking marker events configured. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

#### Details

The following example will illustrate how the VI configures the script you specify:

Assume that the niRFSG RF Blanking Source property is set to “marker0”, the value of the [RF Blanking Marker Positions](/csh?context=rfmxwlangen_lvwlangenprop_attr5b) property is {10000, 12000}, and you configure the **script** parameter as shown in the following example.

| script scriptName |
| --- |
| generate waveformName |
| end script |

The **script out** parameter value is as shown in the following example.

| script scriptName |
| --- |
| generate waveformName marker0 (10000, 12000) |
| end script |

Parent topic:

RFSG Database

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-burst-start-locations-vi.html language=enus -->
## TOPIC 00134: niWLANG RFSG Retrieve Burst Start Locations VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-burst-start-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-burst-start-locations-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst start locations stored in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. cstr.png waveform nam

### niWLANG RFSG Retrieve Burst Start Locations VI

Returns the burst start locations stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-burst-start-locations-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the burst start locations. the WLAN Generation uses this parameter as the key to retrieve the waveform properties in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. burst start locations — burst start locations returns the burst start locations stored, for the waveform you specified in the waveform name parameter. It is an array of sample positions of the start of the burst, within the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-burst-stop-locations-vi.html language=enus -->
## TOPIC 00135: niWLANG RFSG Retrieve Burst Stop Locations VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-burst-stop-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-burst-stop-locations-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the burst stop locations stored in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. cstr.png waveform name

### niWLANG RFSG Retrieve Burst Stop Locations VI

Returns the burst stop locations stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-burst-stop-locations-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the burst stop locations. the WLAN Generation uses this parameter as the key to retrieve the waveform properties in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. burst stop locations — burst stop locations returns the burst stop locations stored, for the waveform you specified in the waveform name parameter. It is an array of sample positions of the end of the burst, within the waveform. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-iq-rate-script-vi.html language=enus -->
## TOPIC 00136: niWLANG RFSG Retrieve IQ Rate (Script) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-iq-rate-script-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-iq-rate-script-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the I/Q rate of all the waveforms in the script that you specify in the script parameter. This VI returns the I/Q rate if the I/Q rates are the same for all the waveforms. If the I/Q rates are different, the VI returns an error. icon Inputs/Outputs civrn.png instrument handle instrument handl

### niWLANG RFSG Retrieve IQ Rate (Script) VI

Checks the I/Q rate of all the waveforms in the script that you specify in the **script** parameter. This VI returns the I/Q rate if the I/Q rates are the same for all the waveforms. If the I/Q rates are different, the VI returns an error.

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-iq-rate-script-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. script — script specifies the script that controls waveform generation. NI-RFSG supports multiple scripts that may be selected by name using the NI-RFSG Selected Script property. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. IQ rate (S/s) — IQ rate returns the I/Q rate, in samples per second (S/s), if the I/Q rates are the same for all the waveforms that you specify in the script parameter. If the I/Q rates are different, the VI returns an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-iq-rate-waveform-vi.html language=enus -->
## TOPIC 00137: niWLANG RFSG Retrieve IQ Rate (Waveform) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-iq-rate-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-iq-rate-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q rate stored in the RFSG database. The VI uses the waveform name as the key to retrieve the waveform properties. Use the niWLANG RFSG Store IQ Rate VI to store the I/Q rate in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrumen

### niWLANG RFSG Retrieve IQ Rate (Waveform) VI

Returns the I/Q rate stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database). The VI uses the waveform name as the key to retrieve the waveform properties.

Note

niWLANG RFSG Store IQ Rate

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-iq-rate-waveform-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the I/Q rate. the WLAN Generation uses the waveform name parameter as the key to retrieve the waveform properties in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. IQ rate (S/s) — IQ rate returns the I/Q rate, in samples per second (S/s), stored in the RFSG database for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-minimum-papr-script-vi.html language=enus -->
## TOPIC 00138: niWLANG RFSG Retrieve Minimum PAPR (Script) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-minimum-papr-script-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-minimum-papr-script-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum value of the headroom, or PAPR, of all the waveforms in the script that you specify in the script parameter. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize

### niWLANG RFSG Retrieve Minimum PAPR (Script) VI

Returns the minimum value of the headroom, or PAPR, of all the waveforms in the script that you specify in the **script** parameter.

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-minimum-papr-script-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. — script specifies the script that controls waveform generation. NI-RFSG supports multiple scripts that may be selected by name using the NI-RFSG Selected Script property. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. PAPR (dB) — PAPR returns the minimum of all the maximum expected peak-to-average power ratio (PAPR) values, in dB, stored in the RFSG database. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-papr-waveform-vi.html language=enus -->
## TOPIC 00139: niWLANG RFSG Retrieve PAPR (Waveform) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-papr-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-papr-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the headroom, or PAPR, stored in the RFSG database. The VI uses the waveform name as the key to retrieve the waveform PAPR. Use the niWLANG RFSG Store PAPR VI to store the PAPR in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument s

### niWLANG RFSG Retrieve PAPR (Waveform) VI

Returns the headroom, or PAPR, stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database). The VI uses the waveform name as the key to retrieve the waveform PAPR.

Note

niWLANG RFSG Store PAPR

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-papr-waveform-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the PAPR. the WLAN Generation uses the waveform name parameter as the key to retrieve the waveform properties in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. PAPR (dB) — PAPR returns the peak-to-average power ratio (PAPR), in dB, stored in the RFSG database, for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-rf-blanking-marker-positions-waveform-vi.html language=enus -->
## TOPIC 00140: niWLANG RFSG Retrieve RF Blanking Marker Positions (Waveform) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-rf-blanking-marker-positions-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-rf-blanking-marker-positions-waveform-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RF blanking marker positions stored in the RFSG database. The VI uses the waveform name as the key to retrieve the waveform properties. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the

### niWLANG RFSG Retrieve RF Blanking Marker Positions (Waveform) VI

Returns the RF blanking marker positions stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database). The VI uses the waveform name as the key to retrieve the waveform properties.

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-rf-blanking-marker-positions-waveform-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the names of the waveforms to clear. If you set this parameter as empty, the VI clears all the waveforms and their properties. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. RF blanking marker positions — RF blanking marker positions returns the RF blanking marker positions saved in the TDMS file. It is an array of sample positions, within waveform, of marker events that can be used to toggle the state of RF blanking. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-waveform-size-vi.html language=enus -->
## TOPIC 00141: niWLANG RFSG Retrieve Waveform Size VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-waveform-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-retrieve-waveform-size-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the waveform size stored in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. cstr.png waveform name wavefo

### niWLANG RFSG Retrieve Waveform Size VI

Returns the waveform size stored in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-retrieve-waveform-size-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to retrieve the waveform size. the WLAN Generation uses this parameter as the key to retrieve the waveform properties in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. waveform size — waveform size returns the waveform size stored, for the waveform you specified in the waveform name parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Retrieve

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-burst-start-locations-vi.html language=enus -->
## TOPIC 00142: niWLANG RFSG Store Burst Start Locations VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-burst-start-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-burst-start-locations-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the burst start locations that you specify in the burst start locations parameter in the RFSG Database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG I

### niWLANG RFSG Store Burst Start Locations VI

Stores the burst start locations that you specify in the **burst start locations** parameter in the [RFSG Database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-store-burst-start-locations-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the burst start locations. burst start locations — burst start locations specifies the burst start locations to store. It is an array of sample positions of the start of the burst, within the waveform. The default value is "" (empty array). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Store

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-burst-stop-locations-vi.html language=enus -->
## TOPIC 00143: niWLANG RFSG Store Burst Stop Locations VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-burst-stop-locations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-burst-stop-locations-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the burst stop locations that you specify in the burst stop locations parameter in the RFSG Database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Ini

### niWLANG RFSG Store Burst Stop Locations VI

Stores the burst stop locations that you specify in the **burst stop locations** parameter in the [RFSG Database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-store-burst-stop-locations-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the burst stop locations. burst stop locations — burst stop locations specifies the burst stop locations to store. It is an array of sample positions of the end of the burst, within the waveform. The default value is "" (empty array). error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Store

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-iq-rate-vi.html language=enus -->
## TOPIC 00144: niWLANG RFSG Store IQ Rate VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-iq-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-iq-rate-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the I/Q rate that you specify in the IQ rate parameter, in the RFSG Database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI.

### niWLANG RFSG Store IQ Rate VI

Stores the I/Q rate that you specify in the **IQ rate** parameter, in the [RFSG Database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-store-iq-rate-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the I/Q rate. IQ rate (S/s) — IQ rate specifies the I/Q rate, in samples per second (S/s), to store in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Store

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-papr-vi.html language=enus -->
## TOPIC 00145: niWLANG RFSG Store PAPR VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-papr-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-papr-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the headroom, or peak-to-average power ratio (PAPR), which you specify in the PAPR parameter, in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or

### niWLANG RFSG Store PAPR VI

Stores the headroom, or peak-to-average power ratio (PAPR), which you specify in the **PAPR** parameter, in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-store-papr-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the maximum expected peak-to-average power ratio (PAPR). PAPR (dB) — PAPR specifies the headroom (or PAPR), in dB, to store in the RFSG database. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Store

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-rf-blanking-marker-positions-vi.html language=enus -->
## TOPIC 00146: niWLANG RFSG Store RF Blanking Marker Positions VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-rf-blanking-marker-positions-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-rf-blanking-marker-positions-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the RF blanking marker positions that you specify in the RF Blanking Marker Positions parameter in the RFSG database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI o

### niWLANG RFSG Store RF Blanking Marker Positions VI

Stores the RF blanking marker positions that you specify in the **RF Blanking Marker Positions** parameter in the [RFSG database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-store-rf-blanking-marker-positions-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the waveform for which you want to store the RF blanking marker positions. RF Blanking Marker Positions — RF Blanking Marker Positions specifies the RF blanking marker positions to store. It is an array of sample positions, within the waveform, of marker events that can be used to toggle the state of RF blanking. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Store

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-waveform-size-vi.html language=enus -->
## TOPIC 00147: niWLANG RFSG Store Waveform Size VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-waveform-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/rfsg-database/niwlang-rfsg-store-waveform-size-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the waveform size that you specify in the waveform size parameter in the RFSG Database. icon Inputs/Outputs civrn.png instrument handle instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With O

### niWLANG RFSG Store Waveform Size VI

Stores the waveform size that you specify in the **waveform size** parameter in the [RFSG Database](/csh?context=rfmxwlangen_wlangen_rfsg_database).

[IMAGE alt='icon' src='niwlang-rfsg-store-waveform-size-vi.png']

#### Inputs/Outputs

| instrument handle — instrument handle identifies the instrument session. the WLAN Generation obtains this parameter from the niRFSG Initialize VI or the niRFSG Initialize With Options VI. waveform name — waveform name specifies the name of the waveform for which you want to store the waveform size. waveform size — waveform size specifies the waveform size to store. This value is expressed in samples. The default value is 1. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. instrument handle out — instrument handle out passes a reference from the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Store

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-auto-headroom-enabled-vi.html language=enus -->
## TOPIC 00148: niWLANG Set Auto Headroom Enabled VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-auto-headroom-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-auto-headroom-enabled-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Auto Headroom Enabled property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan an

### niWLANG Set Auto Headroom Enabled VI

Sets the [Auto Headroom Enabled](/csh?context=rfmxwlangen_lvwlangenprop_attr57) property.

[IMAGE alt='icon' src='niwlang-set-auto-headroom-enabled-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. auto headroom enabled — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-channel-bandwidth-vi.html language=enus -->
## TOPIC 00149: niWLANG Set Channel Bandwidth VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-channel-bandwidth-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-channel-bandwidth-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Channel Bandwidth property. icon Inputs/Outputs cgenclassrn.png niwlan generation session cdbl.png channel bandwidth (Hz) cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed

### niWLANG Set Channel Bandwidth VI

Sets the [Channel Bandwidth](/csh?context=rfmxwlangen_lvwlangenprop_attr2a) property.

[IMAGE alt='icon' src='niwlang-set-channel-bandwidth-vi.png']

#### Inputs/Outputs

| niwlan generation session — channel bandwidth (Hz) — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-dsss-data-rate-vi.html language=enus -->
## TOPIC 00150: niWLANG Set DSSS Data Rate VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-dsss-data-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-dsss-data-rate-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the DSSS Data Rate property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png DSSS data rate cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the even

### niWLANG Set DSSS Data Rate VI

Sets the [DSSS Data Rate](/csh?context=rfmxwlangen_lvwlangenprop_attr21) property.

[IMAGE alt='icon' src='niwlang-set-dsss-data-rate-vi.png']

#### Inputs/Outputs

| niwlan generation session — DSSS data rate — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-dsss-preamble-type-vi.html language=enus -->
## TOPIC 00151: niWLANG Set DSSS Preamble Type VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-dsss-preamble-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-dsss-preamble-type-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the DSSS Preamble Type property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png DSSS preamble type cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in

### niWLANG Set DSSS Preamble Type VI

Sets the [DSSS Preamble Type](/csh?context=rfmxwlangen_lvwlangenprop_attr4) property.

[IMAGE alt='icon' src='niwlang-set-dsss-preamble-type-vi.png']

#### Inputs/Outputs

| niwlan generation session — DSSS preamble type — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-guard-interval-type-vi.html language=enus -->
## TOPIC 00152: niWLANG Set Guard Interval Type VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-guard-interval-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-guard-interval-type-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Guard Interval Type property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png guard interval type cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed i

### niWLANG Set Guard Interval Type VI

Sets the [Guard Interval Type](/csh?context=rfmxwlangen_lvwlangenprop_attr7b) property.

[IMAGE alt='icon' src='niwlang-set-guard-interval-type-vi.png']

#### Inputs/Outputs

| niwlan generation session — guard interval type — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-headroom-vi.html language=enus -->
## TOPIC 00153: niWLANG Set Headroom VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-headroom-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-headroom-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Headroom property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis sessio

### niWLANG Set Headroom VI

Sets the [Headroom](/csh?context=rfmxwlangen_lvwlangenprop_attr28) property.

[IMAGE alt='icon' src='niwlang-set-headroom-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. active channel — headroom (dB) — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-idle-interval-vi.html language=enus -->
## TOPIC 00154: niWLANG Set Idle Interval VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-idle-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-idle-interval-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Idle Interval property. icon Inputs/Outputs cgenclassrn.png niwlan generation session cdbl.png idle interval cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event

### niWLANG Set Idle Interval VI

Sets the [Idle Interval](/csh?context=rfmxwlangen_lvwlangenprop_attr3) property.

[IMAGE alt='icon' src='niwlang-set-idle-interval-vi.png']

#### Inputs/Outputs

| niwlan generation session — idle interval — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mapping-matrix-type-vi.html language=enus -->
## TOPIC 00155: niWLANG Set Mapping Matrix Type VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mapping-matrix-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mapping-matrix-type-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Mapping Matrix Type property. icon Inputs/Outputs cgenclassrn.png niwlan generation session cstr.png active channel ci32.png mapping matrix type cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functional

### niWLANG Set Mapping Matrix Type VI

Sets the [Mapping Matrix Type](/csh?context=rfmxwlangen_lvwlangenprop_attr37) property.

[IMAGE alt='icon' src='niwlang-set-mapping-matrix-type-vi.png']

#### Inputs/Outputs

| niwlan generation session — active channel — mapping matrix type — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mapping-matrix-vi.html language=enus -->
## TOPIC 00156: niWLANG Set Mapping Matrix VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mapping-matrix-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mapping-matrix-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the matrix for mapping space-time streams to the transmit channels as defined in section 20.3.11.10.1 of IEEE Standard 802.11n-2009. the WLAN Generation ignores this VI, if the Mapping Matrix Type property is not set to User Defined. icon Inputs/Outputs cgenclassrn.png niwlan generation se

### niWLANG Set Mapping Matrix VI

Specifies the matrix for mapping space-time streams to the transmit channels as defined in section 20.3.11.10.1 of *IEEE Standard 802.11n-2009*. the WLAN Generation ignores this VI, if the [Mapping Matrix Type](/csh?context=rfmxwlangen_lvwlangenprop_attr37) property is not set to **User Defined**.

[IMAGE alt='icon' src='niwlang-set-mapping-matrix-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan generation session specifies the niWLAN generation session refnum. active channel — active channel specifies the active channel string. You must use the following active channel string formats when you set the PPDU Type property to Trigger-Based PPDU. Spatial Mapping Mode property value Active channel string format Common "" (empty string) User Specific "userx" mapping matrix — mapping matrix specifies the matrix for mapping spatial streams to the transmit channels. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan generation session out passes a reference of the WLAN generation session to the next VI. Note Close the niWLAN generation session reference using the niWLANG Close Session VI before the completion of execution to avoid possible memory leak issues. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Spatial Mapping Mode property value | Active channel string format |
| Common | "" (empty string) |
| User Specific | "userx" |

#### Details

The dimensions of the matrix must be *N_Tx* * (*N_STS* + *N_ESS*) if you set the Standard property to **80211N MIMOOFDM**, and *N_Tx* * *N_STS* if you set the Standard property to **80211AC MIMOOFDM**, **80211AH MIMOOFDM**, **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, or **80211BN MIMOOFDM**.

| where, | N_Tx is the number of transmit channels |
| --- | --- |
|  | N_STS is the number of space-time streams. If you set the Standard property to 80211N MIMOOFDM, N_STS is determined by the MCS index and the STBC index |
|  | N_ESS is the number of extension spatial streams |

For one-to-one mapping (direct mapping), *N_Tx* = *N_SS* and *N_ESS* = *0*. For one-to-many mapping (spatial expansion), *N_Tx* >= (*N_SS* + *N_ESS*).

If you set the Standard property to **80211AX MIMOOFDM**, **80211BE MIMOOFDM**, or **80211BN MIMOOFDM** and the PPDU Type property to **Trigger-Based PPDU**, the *N STS* value is dependent on the [Spatial Mapping Mode](/csh?context=rfmxwlangen_lvwlangenprop_attrb9) property.

| Spatial Mapping Mode property value | N_STS value |
| --- | --- |
| Common | Maximum number of space time streams across Resource Units (RUs) |
| User Specific | Number of space time streams for the specified user |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mcs-index-vi.html language=enus -->
## TOPIC 00157: niWLANG Set MCS Index VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mcs-index-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-mcs-index-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the MCS Index property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png modulation and coding scheme index cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypas

### niWLANG Set MCS Index VI

Sets the [MCS Index](/csh?context=rfmxwlangen_lvwlangenprop_attr29) property.

[IMAGE alt='icon' src='niwlang-set-mcs-index-vi.png']

#### Inputs/Outputs

| niwlan generation session — modulation and coding scheme index — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-frames-vi.html language=enus -->
## TOPIC 00158: niWLANG Set Number of Frames VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-frames-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-frames-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Number of Frames property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png number of frames cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the

### niWLANG Set Number of Frames VI

Sets the [Number of Frames](/csh?context=rfmxwlangen_lvwlangenprop_attr6) property.

[IMAGE alt='icon' src='niwlang-set-number-of-frames-vi.png']

#### Inputs/Outputs

| niwlan generation session — number of frames — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-segments-vi.html language=enus -->
## TOPIC 00159: niWLANG Set Number of Segments VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-segments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-segments-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Number of Segments property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analy

### niWLANG Set Number of Segments VI

Sets the [Number of Segments](/csh?context=rfmxwlangen_lvwlangenprop_attr4b) property.

[IMAGE alt='icon' src='niwlang-set-number-of-segments-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. number of segments — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-space-time-streams-vi.html language=enus -->
## TOPIC 00160: niWLANG Set Number of Space Time Streams VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-space-time-streams-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-space-time-streams-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Number of Space Time Streams property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the ni

### niWLANG Set Number of Space Time Streams VI

Sets the [Number of Space Time Streams](/csh?context=rfmxwlangen_lvwlangenprop_attr4c) property.

[IMAGE alt='icon' src='niwlang-set-number-of-space-time-streams-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. number of space time streams — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-transmit-channels-vi.html language=enus -->
## TOPIC 00161: niWLANG Set Number of Transmit Channels VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-transmit-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-transmit-channels-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Number of Transmit Channels property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png number of transmit channels cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality shou

### niWLANG Set Number of Transmit Channels VI

Sets the [Number of Transmit Channels](/csh?context=rfmxwlangen_lvwlangenprop_attr2f) property.

[IMAGE alt='icon' src='niwlang-set-number-of-transmit-channels-vi.png']

#### Inputs/Outputs

| niwlan generation session — number of transmit channels — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-users-vi.html language=enus -->
## TOPIC 00162: niWLANG Set Number of Users VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-users-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-number-of-users-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Number of Users property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png number of users cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the ev

### niWLANG Set Number of Users VI

Sets the [Number of Users](/csh?context=rfmxwlangen_lvwlangenprop_attr73) property.

[IMAGE alt='icon' src='niwlang-set-number-of-users-vi.png']

#### Inputs/Outputs

| niwlan generation session — number of users — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ofdm-data-rate-vi.html language=enus -->
## TOPIC 00163: niWLANG Set OFDM Data Rate VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ofdm-data-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ofdm-data-rate-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the OFDM Data Rate property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png OFDM data rate cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the even

### niWLANG Set OFDM Data Rate VI

Sets the [OFDM Data Rate](/csh?context=rfmxwlangen_lvwlangenprop_attr20) property.

[IMAGE alt='icon' src='niwlang-set-ofdm-data-rate-vi.png']

#### Inputs/Outputs

| niwlan generation session — OFDM data rate — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-oversampling-ratio-vi.html language=enus -->
## TOPIC 00164: niWLANG Set Oversampling Ratio VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-oversampling-ratio-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-oversampling-ratio-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Oversampling Ratio property that defines the ratio by which the Nyquist rate is multiplied to get the final sampling rate. If you set the Standard property to 80211B/G DSSS or 80211G DSSSOFDM, the default value is 4 and the minimum value is 2. If you set the Standard property to other Stand

### niWLANG Set Oversampling Ratio VI

Sets the [Oversampling Ratio](/csh?context=rfmxwlangen_lvwlangenprop_attrd3) property that defines the ratio by which the Nyquist rate is multiplied to get the final sampling rate.

If you set the Standard property to **80211B/G DSSS** or **80211G DSSSOFDM**, the default value is 4 and the minimum value is 2. If you set the Standard property to other Standards, the default and minimum value are both 1.25.

[IMAGE alt='icon' src='niwlang-set-oversampling-ratio-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. oversampling ratio — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-payload-ampdu-enabled-vi.html language=enus -->
## TOPIC 00165: niWLANG Set Payload AMPDU Enabled VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-payload-ampdu-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-payload-ampdu-enabled-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the A-MPDU Enabled property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis

### niWLANG Set Payload AMPDU Enabled VI

Sets the [A-MPDU Enabled](/csh?context=rfmxwlangen_lvwlangenprop_attr67) property.

[IMAGE alt='icon' src='niwlang-set-payload-ampdu-enabled-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. payload A-MPDU enabled — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-payload-number-of-mpdus-vi.html language=enus -->
## TOPIC 00166: niWLANG Set Payload Number of MPDUs VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-payload-number-of-mpdus-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-payload-number-of-mpdus-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Payload Number of MPDUs property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan

### niWLANG Set Payload Number of MPDUs VI

Sets the [Payload Number of MPDUs](/csh?context=rfmxwlangen_lvwlangenprop_attr68) property.

[IMAGE alt='icon' src='niwlang-set-payload-number-of-mpdus-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. payload number of MPDUs — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-plcp-frame-format-802-11n-vi.html language=enus -->
## TOPIC 00167: niWLANG Set PLCP Frame Format (802_11N) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-plcp-frame-format-802-11n-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-plcp-frame-format-802-11n-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the 80211n PLCP Frame Format property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png 80211N PLCP frame format cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be

### niWLANG Set PLCP Frame Format (802_11N) VI

Sets the [80211n PLCP Frame Format](/csh?context=rfmxwlangen_lvwlangenprop_attr2b) property.

[IMAGE alt='icon' src='niwlang-set-plcp-frame-format-802-11n-vi.png']

#### Inputs/Outputs

| niwlan generation session — 80211N PLCP frame format — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ppdu-type-vi.html language=enus -->
## TOPIC 00168: niWLANG Set PPDU Type VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ppdu-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ppdu-type-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the PPDU Type property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png PPDU type cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of error

### niWLANG Set PPDU Type VI

Sets the [PPDU Type](/csh?context=rfmxwlangen_lvwlangenprop_attr5f) property.

[IMAGE alt='icon' src='niwlang-set-ppdu-type-vi.png']

#### Inputs/Outputs

| niwlan generation session — PPDU type — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-preamble-type-802-11ah-vi.html language=enus -->
## TOPIC 00169: niWLANG Set Preamble Type (802_11AH) VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-preamble-type-802-11ah-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-preamble-type-802-11ah-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the 80211ah Preamble Type property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan an

### niWLANG Set Preamble Type (802_11AH) VI

Sets the [80211ah Preamble Type](/csh?context=rfmxwlangen_lvwlangenprop_attr77) property.

[IMAGE alt='icon' src='niwlang-set-preamble-type-802-11ah-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. 80211ah Preamble Type — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ru-offset-vi.html language=enus -->
## TOPIC 00170: niWLANG Set RU Offset VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ru-offset-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ru-offset-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RU Offset property. icon Inputs/Outputs cgenclassrn.png niwlan generation session cstr.png Active Channel ci32.png RU Offset cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypass

### niWLANG Set RU Offset VI

Sets the [RU Offset](/csh?context=rfmxwlangen_lvwlangenprop_attr85) property.

[IMAGE alt='icon' src='niwlang-set-ru-offset-vi.png']

#### Inputs/Outputs

| niwlan generation session — Active Channel — RU Offset — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ru-size-vi.html language=enus -->
## TOPIC 00171: niWLANG Set RU Size VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ru-size-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-ru-size-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the RU Size property. icon Inputs/Outputs cgenclassrn.png niwlan generation session cstr.png Active Channel ci32.png RU Size cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed i

### niWLANG Set RU Size VI

Sets the [RU Size](/csh?context=rfmxwlangen_lvwlangenprop_attr84) property.

[IMAGE alt='icon' src='niwlang-set-ru-size-vi.png']

#### Inputs/Outputs

| niwlan generation session — Active Channel — RU Size — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-standard-vi.html language=enus -->
## TOPIC 00172: niWLANG Set Standard VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-standard-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-standard-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Standard property. icon Inputs/Outputs cgenclassrn.png niwlan generation session ci32.png standard cerrcodeclst.png error in error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors

### niWLANG Set Standard VI

Sets the [Standard](/csh?context=rfmxwlangen_lvwlangenprop_attr1f) property.

[IMAGE alt='icon' src='niwlang-set-standard-vi.png']

#### Inputs/Outputs

| niwlan generation session — standard — error in — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. niwlan generation session out — error out — error in can accept error information wired from VIs previously called. Use this information to decide if any functionality should be bypassed in the event of errors from other VIs. Right-click the error in control on the front panel and select Explain Error or Explain Warning from the shortcut menu for more information about the error. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-stbc-index-vi.html language=enus -->
## TOPIC 00173: niWLANG Set STBC Index VI

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-stbc-index-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/setvis/niwlang-set-stbc-index-vi.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the STBC Index property. icon Inputs/Outputs cgenclassrn.png niwlan generation session niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis sess

### niWLANG Set STBC Index VI

Sets the [STBC Index](/csh?context=rfmxwlangen_lvwlangenprop_attr31) property.

[IMAGE alt='icon' src='niwlang-set-stbc-index-vi.png']

#### Inputs/Outputs

| niwlan generation session — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. STBC index — error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. niwlan generation session out — niwlan analysis session returns the niWLAN analysis session refnum. Use this parameter to configure the behavior and operation of the appropriate WLAN Analysis Toolkit VIs that accept the niwlan analysis session refnum as an input. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configure Generation

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00174: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |

<!--NI_TOPIC bundle=rfmxwlangen-labview-api-ref path=vi-lib/rf-toolkits/wlan/generation/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00175: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxwlangen-labview-api-ref`
- source_path: `vi-lib/rf-toolkits/wlan/generation/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwlangen-labview-api-ref/raw/resource/enus/vi-lib/rf-toolkits/wlan/generation/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxwlangen-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
