# NI DOCUMENT BUNDLE: rfmx-wcdma-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-wcdma-prop start=1 end=119 -->
<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500001.html language=enus -->
## TOPIC 00001: rfmxwcdmaprop/attr500001.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500001.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

For a single-carrier measurement, this property specifies the center frequency of the acquired RF signal.

For multi-carrier measurements, this property specifies the reference frequency for the values in the [Carrier Freq](../rfmxwcdmaprop/attr50000f.html) property.

This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Frequency, RFmxWCDMA Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500005.html language=enus -->
## TOPIC 00002: rfmxwcdmaprop/attr500005.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500005.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the source terminal for the digital edge trigger.

This property is used only when you set the [Trigger Type](attr500004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

| PFI0 (PFI0) | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 (PFI1) | The trigger is received on PFI 1. |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50000c.html language=enus -->
## TOPIC 00003: rfmxwcdmaprop/attr50000c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50000c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Duration (s) Property

Trigger:Minimum Quiet Time:Duration (s) Property

**Short Name:**Trigger Min Quiet Time (s)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger.

This value is expressed in seconds.

If you set the [IQ Power Edge Slope](attr500009.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50000e.html language=enus -->
## TOPIC 00004: rfmxwcdmaprop/attr50000e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50000e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Number of Carriers Property

Carrier:Number of Carriers Property

**Short Name:**Num Carriers

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the number of carriers.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Number of Carriers |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500010.html language=enus -->
## TOPIC 00005: rfmxwcdmaprop/attr500010.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500010.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:Configuration Mode Property

Carrier:Channel:Configuration Mode Property

**Short Name:**Channel Configuration Mode

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the channel configuration mode.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

| Auto Detect (0) | The measurement detects the channels. |
| --- | --- |
| User Defined (1) | Configure the channels using the Num Channels property and the RFmxWCDMA Configure User Defined Channel (Array) VI. |
| Test Model (2) | Choose from the standard-defined channel configurations using the UL Test Model property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Channel Configuration Mode |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500015.html language=enus -->
## TOPIC 00006: rfmxwcdmaprop/attr500015.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500015.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Spreading Factor Property

Carrier:Channel:User Defined:Spreading Factor Property

**Short Name:**Spreading Factor

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the spreading factor of the channel.

Use "carrier<*n*>/channel<*k*>" as the selector string to configure or read this property.

The default value is 256. Valid values are 2, 4, 8,16, 32, 64, 128, and 256.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500017.html language=enus -->
## TOPIC 00007: rfmxwcdmaprop/attr500017.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500017.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Modulation Type Property

Carrier:Channel:User Defined:Modulation Type Property

**Short Name:**Mod Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the modulation type for the channel.

Use "carrier<*n*>/channel<*k*>" as the selector string to configure or read this property.

The default value is **BPSK/QPSK**.

| BPSK/QPSK (0) | The modulation type is BPSK. |
| --- | --- |
| 4PAM/16QAM (1) | The modulation type is 4-PAM. |
| 64QAM (2) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500018.html language=enus -->
## TOPIC 00008: rfmxwcdmaprop/attr500018.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500018.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Branch Property

Carrier:Channel:User Defined:Branch Property

**Short Name:**Branch

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the branch on which the data is modulated in the channel.

Use "carrier<*n*>/channel<*k*>" as the selector string to configure or read this property.

The default value is **I**.

| I (0) | The signal is modulated in the in-phase branch. |
| --- | --- |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
| I and Q (2) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr500019.html language=enus -->
## TOPIC 00009: rfmxwcdmaprop/attr500019.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr500019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr500019.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:Uplink Test Model Property

Carrier:Channel:Uplink Test Model Property

**Short Name:**UL Test Model

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the uplink test model when the user sets the [Channel Configuration Mode](attr500010.html) property to **Test Model**.

Each test model is a set of channel configurations defined by the standard.

Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the *3GPP TS 34.121-1* specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<*n*>, where *n* is the oldest release number with a given set of channel configurations.

Use "carrier<*n*>" as the selector string to configure or read this property.

The default value is **R6 C.2.1**.

| R6 C.2.1 (0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| --- | --- |
| R6 C.2.2 (1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.3 (2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.4 (3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.5 (4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.10.1.4 Subtest1 (5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest2 (6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest3 (7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest4 (8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest5 (9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest6 (10) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7 C.10.1.4 Subtest1 (11) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest2 (12) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest3 (13) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest4 (14) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest1 (15) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest2 (16) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest3 (17) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest4 (18) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest5 (19) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8 C.11.1.3 Subtest1 (20) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest2 (21) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest3 (22) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest4 (23) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest5 (24) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.4 Subtest1 (25) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Uplink Test Model |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50001b.html language=enus -->
## TOPIC 00010: rfmxwcdmaprop/attr50001b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50001b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50001b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Scrambling:Uplink:Type Property

Carrier:Scrambling:Uplink:Type Property

**Short Name:**UL Scrambling Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the type of scrambling to use for the measurement.

Use "carrier<*n*>" as the selector string to configure or read this property.

The default value is **Long**.

| Long (0) | A long scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |
| --- | --- |
| Short (1) | A short scrambling code as defined in section 4.3.2 of the 3GPP TS 25.213 specification, version 11.4.0, release 11, is used. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Uplink Scrambling |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50100e.html language=enus -->
## TOPIC 00011: rfmxwcdmaprop/attr50100e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50100e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Integration Bandwidth (Hz) Property

ACP:Offset:Integration Bandwidth (Hz) Property

**Short Name:**ACP Offset IBW (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr501014.html language=enus -->
## TOPIC 00012: rfmxwcdmaprop/attr501014.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr501014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr501014.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Number of Analysis Threads Property

ACP:Number of Analysis Threads Property

**Short Name:**ACP Num Analysis Threads

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the maximum number of threads used for parallelism for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50101c.html language=enus -->
## TOPIC 00013: rfmxwcdmaprop/attr50101c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50101c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:RBW Filter:Bandwidth (Hz) Property

ACP:RBW Filter:Bandwidth (Hz) Property

**Short Name:**ACP RBW (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [ACP RBW Auto](attr50101b.html) property to **False**.

This property is valid only if you set the [ACP RBW Filter Type](attr50101d.html) property to **Gaussian** or **Flat**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 38.4 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50101d.html language=enus -->
## TOPIC 00014: rfmxwcdmaprop/attr50101d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50101d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50101d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:RBW Filter:Type Property

ACP:RBW Filter:Type Property

**Short Name:**ACP RBW Filter Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **FFT Based**.

| FFT Based (0) | No RBW filtering is used. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50101e.html language=enus -->
## TOPIC 00015: rfmxwcdmaprop/attr50101e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50101e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Sweep Time:Auto Property

ACP:Sweep Time:Auto Property

**Short Name:**ACP Sweep Time Auto

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time that you specify in the ACP Sweep Time property |
| --- | --- |
| True (1) | The measurement uses a sweep time value of one slot duration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50101f.html language=enus -->
## TOPIC 00016: rfmxwcdmaprop/attr50101f.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50101f.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Sweep Time:Interval (s) Property

ACP:Sweep Time:Interval (s) Property

**Short Name:**ACP Sweep Time (s)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the sweep time when you set the [ACP Sweep Time Auto](attr50101e.html) property to **False**.

This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr501020.html language=enus -->
## TOPIC 00017: rfmxwcdmaprop/attr501020.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr501020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr501020.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Noise Compensation Enabled Property

ACP:Noise Compensation Enabled Property

**Short Name:**ACP Noise Comp Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| --- | --- |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure Noise Compensation Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr501022.html language=enus -->
## TOPIC 00018: rfmxwcdmaprop/attr501022.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr501022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr501022.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Total Carrier Power (dBm) Property

ACP:Results:Total Carrier Power (dBm) Property

**Short Name:**ACP Results Total Carrier Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the [ACP Results Carrier Abs Pwr](attr501026.html) property. For a single-carrier measurement, total carrier power is the same as carrier absolute power.

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr501027.html language=enus -->
## TOPIC 00019: rfmxwcdmaprop/attr501027.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr501027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr501027.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Carrier:Relative Power (dB) Property

ACP:Results:Carrier:Relative Power (dB) Property

**Short Name:**ACP Results Carrier Rel Pwr (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the carrier power relative to the [ACP Results Total Carrier Pwr](attr501022.html).

This value is expressed in dB.

Use "carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50102d.html language=enus -->
## TOPIC 00020: rfmxwcdmaprop/attr50102d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50102d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Relative Power (dB) Property

ACP:Results:Lower Offset:Relative Power (dB) Property

**Short Name:**ACP Results Lower Offset Rel Pwr (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the lower offset channel power relative to the power of the carrier(s) that you specify in the [ACP Offset Pwr Ref Carrier](attr50100c.html) property.

This value is expressed in dB.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr501032.html language=enus -->
## TOPIC 00021: rfmxwcdmaprop/attr501032.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr501032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr501032.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Absolute Power (dBm) Property

ACP:Results:Upper Offset:Absolute Power (dBm) Property

**Short Name:**ACP Results Upper Offset Abs Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the upper offset channel power.

This value is expressed in dBm.

The upper offset channel power is the integrated power of the RRC-filtered signal at the value of the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr501035.html language=enus -->
## TOPIC 00022: rfmxwcdmaprop/attr501035.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr501035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr501035.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Near IF Output Power Offset (dB) Property

ACP:Advanced:Near IF Output Power Offset (dB) Property

**Short Name:**ACP Near IF Output Power Offset (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the power offset to use to adjust the IF output power level for offset channels near the carrier channel. Adjusting the IF output power level improves the dynamic range.

This value is expressed in dB.

This property is used only if you set the [ACP Meas Method](attr501012.html) property to **Dynamic Range** and set the [ACP IF Output Power Offset Auto](attr501034.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr503002.html language=enus -->
## TOPIC 00023: rfmxwcdmaprop/attr503002.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr503002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr503002.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Carrier:Integration Bandwidth (Hz) Property

CHP:Carrier:Integration Bandwidth (Hz) Property

**Short Name:**CHP Carrier IBW (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the frequency range, over which the measurement integrates the power. This value is expressed in Hz.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr503006.html language=enus -->
## TOPIC 00024: rfmxwcdmaprop/attr503006.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr503006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr503006.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Count Property

CHP:Averaging:Count Property

**Short Name:**CHP Averaging Count

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](attr503007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CHP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr503014.html language=enus -->
## TOPIC 00025: rfmxwcdmaprop/attr503014.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr503014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr503014.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:All Traces Enabled Property

CHP:All Traces Enabled Property

**Short Name:**CHP All Traces Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr503018.html language=enus -->
## TOPIC 00026: rfmxwcdmaprop/attr503018.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr503018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr503018.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Results:Total Carrier Power (dBm) Property

CHP:Results:Total Carrier Power (dBm) Property

**Short Name:**CHP Results Total Carrier Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the [CHP Results Carrier Abs Pwr](attr503015.html) property. For a single-carrier measurement, total carrier power is the same as carrier absolute power.

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CHP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50301b.html language=enus -->
## TOPIC 00027: rfmxwcdmaprop/attr50301b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50301b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50301b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Amplitude Correction Type Property

CHP:Amplitude Correction Type Property

**Short Name:**CHP Amplitude Correction Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

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

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506000.html language=enus -->
## TOPIC 00028: rfmxwcdmaprop/attr506000.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506000.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Measurement Enabled Property

OBW:Measurement Enabled Property

**Short Name:**OBW Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506004.html language=enus -->
## TOPIC 00029: rfmxwcdmaprop/attr506004.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506004.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Span (Hz) Property

OBW:Span (Hz) Property

**Short Name:**OBW Span (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506007.html language=enus -->
## TOPIC 00030: rfmxwcdmaprop/attr506007.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506007.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Enabled Property

OBW:Averaging:Enabled Property

**Short Name:**OBW Averaging Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable averaging for the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506009.html language=enus -->
## TOPIC 00031: rfmxwcdmaprop/attr506009.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506009.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Type Property

OBW:Averaging:Type Property

**Short Name:**OBW Averaging Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

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
| High-level VIs | RFmxWCDMA OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50600c.html language=enus -->
## TOPIC 00032: rfmxwcdmaprop/attr50600c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50600c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50600c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Auto Bandwidth Property

OBW:RBW Filter:Auto Bandwidth Property

**Short Name:**OBW RBW Auto

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement computes the RBW.

This property is valid only if you set the [OBW RBW Filter Type](attr50600e.html) property to **Gaussian** or **Flat**.

If you set the OBW RBW Filter Type property to **FFT Based**, the measurement calculates the RBW regardless of the setting of this property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the RBW that you specify in the OBW RBW property. |
| --- | --- |
| True (1) | The measurement uses an RBW value of 30 kHz. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50600d.html language=enus -->
## TOPIC 00033: rfmxwcdmaprop/attr50600d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50600d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50600d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Bandwidth (Hz) Property

OBW:RBW Filter:Bandwidth (Hz) Property

**Short Name:**OBW RBW (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [OBW RBW Auto](attr50600c.html) property to **False**.

This property is valid only if you set the [OBW RBW Filter Type](attr50600e.html) property to **Gaussian** or **Flat**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 30 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50600e.html language=enus -->
## TOPIC 00034: rfmxwcdmaprop/attr50600e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50600e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Type Property

OBW:RBW Filter:Type Property

**Short Name:**OBW RBW Filter Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | No RBW filtering is applied. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50600f.html language=enus -->
## TOPIC 00035: rfmxwcdmaprop/attr50600f.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50600f.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Sweep Time:Auto Property

OBW:Sweep Time:Auto Property

**Short Name:**OBW Sweep Time Auto

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- |
| True (1) | The measurement uses a sweep time value of one slot duration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506010.html language=enus -->
## TOPIC 00036: rfmxwcdmaprop/attr506010.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506010.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Sweep Time:Interval (s) Property

OBW:Sweep Time:Interval (s) Property

**Short Name:**OBW Sweep Time (s)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the sweep time when you set the [OBW Sweep Time Auto](attr50600f.html) property to **False**.

This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506012.html language=enus -->
## TOPIC 00037: rfmxwcdmaprop/attr506012.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506012.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:All Traces Enabled Property

OBW:All Traces Enabled Property

**Short Name:**OBW All Traces Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506013.html language=enus -->
## TOPIC 00038: rfmxwcdmaprop/attr506013.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506013.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Occupied Bandwidth (Hz) Property

OBW:Results:Occupied Bandwidth (Hz) Property

**Short Name:**OBW Results Occupied BW (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers.

This value is expressed in Hz.

*OBW Results Occupied BW* = *OBW Results Stop Frequency* - *OBW Results Start Frequency*.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506014.html language=enus -->
## TOPIC 00039: rfmxwcdmaprop/attr506014.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506014.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Absolute Power (dBm) Property

OBW:Results:Absolute Power (dBm) Property

**Short Name:**OBW Results Abs Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the total integrated power of the acquired signal.

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506015.html language=enus -->
## TOPIC 00040: rfmxwcdmaprop/attr506015.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506015.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Start Frequency (Hz) Property

OBW:Results:Start Frequency (Hz) Property

**Short Name:**OBW Results Start Freq (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the start frequency of the [occupied bandwidth](attr506013.html).

This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr506016.html language=enus -->
## TOPIC 00041: rfmxwcdmaprop/attr506016.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr506016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr506016.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Stop Frequency (Hz) Property

OBW:Results:Stop Frequency (Hz) Property

**Short Name:**OBW Results Stop Freq (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the stop frequency of the [occupied bandwidth](attr506013.html).

This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50601a.html language=enus -->
## TOPIC 00042: rfmxwcdmaprop/attr50601a.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50601a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50601a.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Amplitude Correction Type Property

OBW:Amplitude Correction Type Property

**Short Name:**OBW Amplitude Correction Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

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

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr508000.html language=enus -->
## TOPIC 00043: rfmxwcdmaprop/attr508000.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr508000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr508000.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Measurement Enabled Property

SEM:Measurement Enabled Property

**Short Name:**SEM Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50800b.html language=enus -->
## TOPIC 00044: rfmxwcdmaprop/attr50800b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50800b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50800b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Number of Offsets Property

SEM:Offset:Number of Offsets Property

**Short Name:**SEM Num Offsets

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the number of offset segments.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr508015.html language=enus -->
## TOPIC 00045: rfmxwcdmaprop/attr508015.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr508015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr508015.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Stop Frequency (Hz) Property

SEM:Offset:Stop Frequency (Hz) Property

**Short Name:**SEM Offset Stop Freq (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50801e.html language=enus -->
## TOPIC 00046: rfmxwcdmaprop/attr50801e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50801e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50801e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Count Property

SEM:Averaging:Count Property

**Short Name:**SEM Averaging Count

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the number of acquisitions used for averaging when you set the [SEM Averaging Enabled](attr50801f.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50801f.html language=enus -->
## TOPIC 00047: rfmxwcdmaprop/attr50801f.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50801f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50801f.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Enabled Property

SEM:Averaging:Enabled Property

**Short Name:**SEM Averaging Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable averaging for the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr508025.html language=enus -->
## TOPIC 00048: rfmxwcdmaprop/attr508025.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr508025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr508025.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Sweep Time:Auto Property

SEM:Sweep Time:Auto Property

**Short Name:**SEM Sweep Time Auto

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time that you specify in the SEM Sweep Time property. |
| --- | --- |
| True (1) | The measurement uses a sweep time value of one slot duration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SEM Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50802d.html language=enus -->
## TOPIC 00049: rfmxwcdmaprop/attr50802d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50802d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50802d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Absolute Integrated Power (dBm) Property

SEM:Results:Carrier:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Carrier Abs Integrated Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the carrier power.

This value is expressed in dBm.

The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the value of the [Center Frequency](attr500001.html) and the [Carrier Freq](attr50000f.html) properties.

Use "carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50802e.html language=enus -->
## TOPIC 00050: rfmxwcdmaprop/attr50802e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50802e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50802e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Relative Integrated Power (dB) Property

SEM:Results:Carrier:Relative Integrated Power (dB) Property

**Short Name:**SEM Results Carrier Rel Integrated Pwr (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the carrier power relative to the [SEM Results Total Carrier Pwr](attr508028.html).

This value is expressed in dB.

Use "carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr508044.html language=enus -->
## TOPIC 00051: rfmxwcdmaprop/attr508044.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr508044.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr508044.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Relative Peak Power (dB) Property

SEM:Results:Upper Offset:Relative Peak Power (dB) Property

**Short Name:**SEM Results Upper Offset Rel Peak Pwr (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the peak power measured in the upper, or positive, offset segment relative to the value of the [SEM Results Total Carrier Pwr](attr508028.html) property.

This value is expressed in dB.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr508045.html language=enus -->
## TOPIC 00052: rfmxwcdmaprop/attr508045.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr508045.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr508045.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Peak Frequency (Hz) Property

SEM:Results:Upper Offset:Peak Frequency (Hz) Property

**Short Name:**SEM Results Upper Offset Pk Freq (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the frequency at which the peak power is observed in the upper offset segment.

This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr508047.html language=enus -->
## TOPIC 00053: rfmxwcdmaprop/attr508047.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr508047.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr508047.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Absolute Power (dBm) Property

SEM:Results:Upper Offset:Margin Absolute Power (dBm) Property

**Short Name:**SEM Results Upper Offset Margin Abs Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the power at the frequency corresponding to the [SEM Results Upper Offset Margin](attr508046.html) property.

This value is expressed in dBm.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50804a.html language=enus -->
## TOPIC 00054: rfmxwcdmaprop/attr50804a.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50804a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50804a.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Measurement Status Property

SEM:Results:Upper Offset:Measurement Status Property

**Short Name:**SEM Results Upper Offset Meas Status

Property of [RFmxWCDMA](crfmxwcdma.html)

Indicates the measurement status based on the [SEM Results Upper Offset Margin](attr508046.html) property.

Use "offset<*n*>" as the selector string to read this result.

| Fail (0) | The value of the SEM Results Upper Offset Margin property is positive. |
| --- | --- |
| Pass (1) | The value of the SEM Results Upper Offset Margin property is zero or negative. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50d001.html language=enus -->
## TOPIC 00055: rfmxwcdmaprop/attr50d001.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50d001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50d001.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Transmitter Architecture Property

Advanced:Transmitter Architecture Property

**Short Name:**Transmitter Architecture

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the RF architecture at the transmitter for a multicarrier signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **LO per Carrier**. The I/Q origin offset is always calculated irrespective of the value of the Transmitter Architecture property.

| LO per Carrier (0) | Specifies that the transmitter has one LO at the center of each carrier. The IQ Origin Offset result is an estimate of the I/Q origin offset of each carrier. |
| --- | --- |
| LO per Band (1) | Specifies that the transmitter has one LO at the center of all the carriers in the band. The Multicarrier IQ Origin Offset result is an estimate of the I/Q origin offset for the LO per Band architecture. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr50d003.html language=enus -->
## TOPIC 00056: rfmxwcdmaprop/attr50d003.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr50d003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr50d003.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Limited Configuration Change Property

Advanced:Limited Configuration Change Property

**Short Name:**Limited Configuration Change

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this property to help achieve faster measurements. When you set this property to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](limitations.html) topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| --- | --- |
| No Change (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Reference Level (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the Reference Level property value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Freq and Ref Level (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only the Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level (5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511000.html language=enus -->
## TOPIC 00057: rfmxwcdmaprop/attr511000.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511000.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Enabled Property

ModAcc:Measurement Enabled Property

**Short Name:**ModAcc Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511002.html language=enus -->
## TOPIC 00058: rfmxwcdmaprop/attr511002.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511002.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Synchronization Mode Property

ModAcc:Synchronization Mode Property

**Short Name:**ModAcc Sync Mode

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement offset slots from the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement Offset slots from the symbol boundary. |
| Marker (3) | The measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement Offset slots from the trigger. This is the fastest way to do a ModAcc measurement. This mode requires the Trigger Type property to be set to Digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511004.html language=enus -->
## TOPIC 00059: rfmxwcdmaprop/attr511004.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511004.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Length (slots) Property

ModAcc:Measurement Length (slots) Property

**Short Name:**ModAcc Meas Length (slots)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the duration of the ModAcc measurement.

This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1. Valid values are [1, (15 - [ModAcc Measurement Offset](attr511003.html))]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511005.html language=enus -->
## TOPIC 00060: rfmxwcdmaprop/attr511005.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511005.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Spectrum Inverted Property

ModAcc:Spectrum Inverted Property

**Short Name:**ModAcc Spectrum Inverted

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The spectrum is not inverted. |
| --- | --- |
| True (1) | The spectrum is inverted. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511007.html language=enus -->
## TOPIC 00061: rfmxwcdmaprop/attr511007.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511007.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Transient Removal Enabled Property

ModAcc:Transient Removal Enabled Property

**Short Name:**ModAcc Transient Removal Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results.

Transients are expected to be present at the slot boundaries, where the mean power of the received signal can change.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The entire measurement interval is used to compute the RMS EVM, peak EVM, RMS magnitude error, and RMS phase error results. |
| --- | --- |
| True (1) | The measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error, and RMS phase error results. The ModAcc Sync Mode property must be set to Frame, Slot, or Marker. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511008.html language=enus -->
## TOPIC 00062: rfmxwcdmaprop/attr511008.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511008.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:All Traces Enabled Property

ModAcc:All Traces Enabled Property

**Short Name:**ModAcc All Traces Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the traces after performing the modulation accuracy (ModAcc) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511009.html language=enus -->
## TOPIC 00063: rfmxwcdmaprop/attr511009.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511009.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Downlink Timing Channel:Spreading Factor Property

ModAcc:Downlink Timing Channel:Spreading Factor Property

**Short Name:**ModAcc Downlink Timing Channel Spreading Factor

Property of [RFmxWCDMA](crfmxwcdma.html)

The spreading factor.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51100a.html language=enus -->
## TOPIC 00064: rfmxwcdmaprop/attr51100a.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51100a.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Downlink Timing Channel:Code Property

ModAcc:Downlink Timing Channel:Code Property

**Short Name:**ModAcc Downlink Timing Channel Code

Property of [RFmxWCDMA](crfmxwcdma.html)

The channel code.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511017.html language=enus -->
## TOPIC 00065: rfmxwcdmaprop/attr511017.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511017.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error (Hz) Property

ModAcc:Results:Frequency Error (Hz) Property

**Short Name:**ModAcc Results Freq Error (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the frequency offset of the composite signal.

This value is expressed in Hz.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511019.html language=enus -->
## TOPIC 00066: rfmxwcdmaprop/attr511019.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511019.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak CDE (dB) Property

ModAcc:Results:Peak CDE (dB) Property

**Short Name:**ModAcc Results Pk CDE (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum code domain error value (CDE).

This value is expressed in dB.

The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used.

The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51101c.html language=enus -->
## TOPIC 00067: rfmxwcdmaprop/attr51101c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51101c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak Active CDE (dB) Property

ModAcc:Results:Peak Active CDE (dB) Property

**Short Name:**ModAcc Results Pk Active CDE (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB.

The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51101f.html language=enus -->
## TOPIC 00068: rfmxwcdmaprop/attr51101f.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51101f.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:P-SCH Power (dBm) Property

ModAcc:Results:P-SCH Power (dBm) Property

**Short Name:**ModAcc Results P-SCH Power (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

The primary SCH power for a BS UUT.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511020.html language=enus -->
## TOPIC 00069: rfmxwcdmaprop/attr511020.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511020.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:S-SCH Power (dBm) Property

ModAcc:Results:S-SCH Power (dBm) Property

**Short Name:**ModAcc Results S-SCH Power (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

The secondary SCH power for a BS UUT.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511021.html language=enus -->
## TOPIC 00070: rfmxwcdmaprop/attr511021.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511021.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DPCH Timing Offset (chips) Property

ModAcc:Results:DPCH Timing Offset (chips) Property

**Short Name:**ModAcc Results DPCH Timing Offset (chips)

Property of [RFmxWCDMA](crfmxwcdma.html)

The timing offset of the selected channel.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511023.html language=enus -->
## TOPIC 00071: rfmxwcdmaprop/attr511023.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511023.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak RCDE Spreading Factor Property

ModAcc:Results:Peak RCDE Spreading Factor Property

**Short Name:**ModAcc Results Pk RCDE Spreading Factor

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the spreading factor of the channel corresponding to the value of the [ModAcc Results Pk RCDE](attr511022.html) property for a carrier.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511024.html language=enus -->
## TOPIC 00072: rfmxwcdmaprop/attr511024.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511024.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak RCDE Code Property

ModAcc:Results:Peak RCDE Code Property

**Short Name:**ModAcc Results Pk RCDE Code

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the spreading code of the channel corresponding to the value of the [ModAcc Results Pk RCDE](attr511022.html) property for a carrier.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511025.html language=enus -->
## TOPIC 00073: rfmxwcdmaprop/attr511025.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511025.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Number of Detected Channels Property

ModAcc:Results:Detected Channel:Number of Detected Channels Property

**Short Name:**ModAcc Results Num Detected Channels

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the number of detected channels when you set the [Channel Configuration Mode](attr500010.html) property to **Auto Detect**. If you set the Channel Configuration Mode property to **User Defined** or **Test Model**, this property returns the number of configured channels.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511026.html language=enus -->
## TOPIC 00074: rfmxwcdmaprop/attr511026.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511026.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Spreading Factor Property

ModAcc:Results:Detected Channel:Spreading Factor Property

**Short Name:**ModAcc Results Detected Spreading Factor

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the spreading factor of the detected channel.

If the [Channel configuration Mode](attr500010.html) property is set to **User Defined** or **Test Model**, the ModAcc Results Detected Spreading Factor property returns the spreading factor of the configured channel of a carrier.

Use "carrier<*n*>/channel<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511027.html language=enus -->
## TOPIC 00075: rfmxwcdmaprop/attr511027.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511027.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Spreading Code Property

ModAcc:Results:Detected Channel:Spreading Code Property

**Short Name:**ModAcc Results Detected Spreading Code

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the spreading code of the detected channel.

If you set the [Channel Configuration Mode](attr500010.html) property to **User Defined** or **Test Model**, the ModAcc Results Detected Spreading Code property returns the spreading code of the configured channel of a carrier.

Use "carrier<*n*>/channel<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr511028.html language=enus -->
## TOPIC 00076: rfmxwcdmaprop/attr511028.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr511028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr511028.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Modulation Type Property

ModAcc:Results:Detected Channel:Modulation Type Property

**Short Name:**ModAcc Results Detected Mod Type

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the modulation type of the detected channel.

If the [Channel Configuration Mode](attr500010.html) property is set to **User Defined** or **Test Model**, the ModAcc Results Detected Mod Type property returns the modulation type of the configured channel of a carrier.

Use "carrier<*n*>/channel<*k*>" as the selector string to read this result.

| BPSK/QPSK (0) | The modulation type is BPSK. |
| --- | --- |
| 4PAM/16QAM (1) | The modulation type is 4-PAM. |
| 64QAM (2) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51102a.html language=enus -->
## TOPIC 00077: rfmxwcdmaprop/attr51102a.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51102a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51102a.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak CDE Branch Property

ModAcc:Results:Peak CDE Branch Property

**Short Name:**ModAcc Results Pk CDE Branch

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the branch corresponding to the value of the [ModAcc Results Pk CDE](attr511019.html) property.

Use "carrier<*n*>" as the selector string to read this property.

| I (0) | The signal is modulated on the in-phase branch. |
| --- | --- |
| Q (1) | The signal is modulated on the quadrature-phase branch. |
| I and Q (2) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51102c.html language=enus -->
## TOPIC 00078: rfmxwcdmaprop/attr51102c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51102c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51102c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak RCDE Branch Property

ModAcc:Results:Peak RCDE Branch Property

**Short Name:**ModAcc Results Pk RCDE Branch

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the branch of the channel corresponding to the value of the [ModAcc Results Pk RCDE](attr511022.html) property for a carrier.

Use "carrier<*n*>" as the selector string to read this property.

| I (0) | The signal is modulated on the in-phase branch. |
| --- | --- |
| Q (1) | The signal is modulated on the quadrature-phase branch. |
| I and Q (2) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51102d.html language=enus -->
## TOPIC 00079: rfmxwcdmaprop/attr51102d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51102d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:I/Q Gain Imbalance (dB) Property

ModAcc:Results:I/Q Gain Imbalance (dB) Property

**Short Name:**ModAcc Results I/Q Gain Imbalance (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the I/Q gain imbalance of the composite signal of a carrier.

 This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51102e.html language=enus -->
## TOPIC 00080: rfmxwcdmaprop/attr51102e.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51102e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51102e.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:I/Q Quadrature Error (deg) Property

ModAcc:Results:I/Q Quadrature Error (deg) Property

**Short Name:**ModAcc Results I/Q Quadrature Error (deg)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the I/Q quadrature error of the composite signal of a carrier.

 This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51102f.html language=enus -->
## TOPIC 00081: rfmxwcdmaprop/attr51102f.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51102f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51102f.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Multicarrier IQ Origin Offset (dB) Property

ModAcc:Results:Multicarrier IQ Origin Offset (dB) Property

**Short Name:**ModAcc Results Multicarrier IQ Origin Offset (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the estimated I/Q origin offset of the multicarrier signal when the [Transmitter Architecture](attr50d001.html) property is set to **LO per Band**. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

This result is useful when the LO is at the center of the multicarrier signal.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51103b.html language=enus -->
## TOPIC 00082: rfmxwcdmaprop/attr51103b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51103b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51103b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:RRC Filter Enabled Property

ModAcc:RRC Filter Enabled Property

**Short Name:**ModAcc RRC Filter Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the RRC filter. Use this property to disable the filter if the received signal is already RRC-filtered.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables the RRC filter in the measurement. |
| --- | --- |
| True (1) | Enables the RRC filter in the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51103c.html language=enus -->
## TOPIC 00083: rfmxwcdmaprop/attr51103c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51103c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51103c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Gain Imbalance Removal Enabled Property

ModAcc:IQ Gain Imbalance Removal Enabled Property

**Short Name:**ModAcc IQ Gain Imbalance Removal Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to remove I/Q gain imbalance before the ModAcc Measurement. In case of multi-carrier measurements, this property is valid only when you set the [Transmitter Architecture](attr50d001.html) property is set to **LO per Carrier**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](attr50d001.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q gain imbalance is not removed before the ModAcc measurement. |
| --- | --- |
| True (1) | The I/Q gain imbalance is removed before the ModAcc measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51103d.html language=enus -->
## TOPIC 00084: rfmxwcdmaprop/attr51103d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51103d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51103d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Quadrature Error Removal Enabled Property

ModAcc:IQ Quadrature Error Removal Enabled Property

**Short Name:**ModAcc IQ Quadrature Error Removal Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. In case of multi-carrier measurements, this property is valid only when you set the [Transmitter Architecture](attr50d001.html) property is set to **LO per Carrier**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q quadrature error is not removed before the ModAcc measurement. |
| --- | --- |
| True (1) | The I/Q quadrature error is removed before the ModAcc measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512003.html language=enus -->
## TOPIC 00085: rfmxwcdmaprop/attr512003.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512003.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Measurement Length (chips) Property

QEVM:Measurement Length (chips) Property

**Short Name:**QEVM Meas Length (chips)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the duration of the QEVM measurement. This value is expressed in chips.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 2560. NI recommends that you set this property to *n* * 512, where the value of *n* can range from 1 to 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA QEVM Configure Measurement Length |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512006.html language=enus -->
## TOPIC 00086: rfmxwcdmaprop/attr512006.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512006.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Averaging:Count Property

QEVM:Averaging:Count Property

**Short Name:**QEVM Averaging Count

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the number of acquisitions used for averaging when you set the [QEVM Averaging Enabled](attr512005.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA QEVM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51200b.html language=enus -->
## TOPIC 00087: rfmxwcdmaprop/attr51200b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51200b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:RRC Filter Enabled Property

QEVM:RRC Filter Enabled Property

**Short Name:**QEVM RRC Filter Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the RRC filter. Use this property to disable the filter if the received signal is already RRC-filtered.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables the RRC filter in the measurement. |
| --- | --- |
| True (1) | Enables the RRC filter in the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51200d.html language=enus -->
## TOPIC 00088: rfmxwcdmaprop/attr51200d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51200d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51200d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Number of Analysis Threads Property

QEVM:Number of Analysis Threads Property

**Short Name:**QEVM Num Analysis Threads

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the maximum number of threads used for parallelism for the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512011.html language=enus -->
## TOPIC 00089: rfmxwcdmaprop/attr512011.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512011.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum Peak EVM (%) Property

QEVM:Results:Maximum Peak EVM (%) Property

**Short Name:**QEVM Results Max Pk EVM (%)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations.

 The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512012.html language=enus -->
## TOPIC 00090: rfmxwcdmaprop/attr512012.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512012.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean Magnitude Error (%) Property

QEVM:Results:Mean Magnitude Error (%) Property

**Short Name:**QEVM Results Mean Magnitude Error (%)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.

This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512013.html language=enus -->
## TOPIC 00091: rfmxwcdmaprop/attr512013.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512013.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum Magnitude Error (%) Property

QEVM:Results:Maximum Magnitude Error (%) Property

**Short Name:**QEVM Results Max Magnitude Error (%)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512014.html language=enus -->
## TOPIC 00092: rfmxwcdmaprop/attr512014.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512014.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean Phase Error (deg) Property

QEVM:Results:Mean Phase Error (deg) Property

**Short Name:**QEVM Results Mean Phase Error (deg)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage.

This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512015.html language=enus -->
## TOPIC 00093: rfmxwcdmaprop/attr512015.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512015.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum Phase Error (deg) Property

QEVM:Results:Maximum Phase Error (deg) Property

**Short Name:**QEVM Results Max Phase Error (deg)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512016.html language=enus -->
## TOPIC 00094: rfmxwcdmaprop/attr512016.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512016.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean Frequency Error (Hz) Property

QEVM:Results:Mean Frequency Error (Hz) Property

**Short Name:**QEVM Results Mean Freq Error (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.

This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512017.html language=enus -->
## TOPIC 00095: rfmxwcdmaprop/attr512017.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512017.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum Frequency Error (Hz) Property

QEVM:Results:Maximum Frequency Error (Hz) Property

**Short Name:**QEVM Results Max Freq Error (Hz)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum value of the frequency errors for a QPSK signal. This value is expressed in Hz.

This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512018.html language=enus -->
## TOPIC 00096: rfmxwcdmaprop/attr512018.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512018.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean I/Q Origin Offset (dB) Property

QEVM:Results:Mean I/Q Origin Offset (dB) Property

**Short Name:**QEVM Results Mean I/Q Origin Offset (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB.

This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr512019.html language=enus -->
## TOPIC 00097: rfmxwcdmaprop/attr512019.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr512019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr512019.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum I/Q Origin Offset (dB) Property

QEVM:Results:Maximum I/Q Origin Offset (dB) Property

**Short Name:**QEVM Results Max I/Q Origin Offset (dB)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum value of the I/Q origin offsets for a QPSK signal. This value is expressed in dB.



This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.



The I/Q Origin Offset is the amount of DC component present in the I/Q signal being measured.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51201a.html language=enus -->
## TOPIC 00098: rfmxwcdmaprop/attr51201a.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51201a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51201a.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean Chip Rate Error (ppm) Property

QEVM:Results:Mean Chip Rate Error (ppm) Property

**Short Name:**QEVM Results Mean Chip Rate Error (ppm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51201b.html language=enus -->
## TOPIC 00099: rfmxwcdmaprop/attr51201b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51201b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51201b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum Chip Rate Error (ppm) Property

QEVM:Results:Maximum Chip Rate Error (ppm) Property

**Short Name:**QEVM Results Max Chip Rate Error (ppm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the maximum chip rate error value for a QPSK signal. This value is expressed in ppm. This value is obtained over all averaging iterations.

 The number of acquisitions is specified by the [QEVM Averaging Count](../rfmxwcdmaprop/attr512006.html) property.

The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr514002.html language=enus -->
## TOPIC 00100: rfmxwcdmaprop/attr514002.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr514002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr514002.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Synchronization Mode Property

SlotPhase:Synchronization Mode Property

**Short Name:**SlotPhase Sync Mode

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement is performed from the frame or the slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the slot boundary. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr514003.html language=enus -->
## TOPIC 00101: rfmxwcdmaprop/attr514003.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr514003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr514003.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Measurement Offset (slots) Property

SlotPhase:Measurement Offset (slots) Property

**Short Name:**SlotPhase Meas Offset (slots)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPhase Sync Mode](attr514002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0. The valid values are any value greater than or equal to 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr514007.html language=enus -->
## TOPIC 00102: rfmxwcdmaprop/attr514007.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr514007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr514007.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Spectrum Inverted Property

SlotPhase:Spectrum Inverted Property

**Short Name:**SlotPhase Spectrum Inverted

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the signal spectrum is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The spectrum is not inverted. |
| --- | --- |
| True (1) | The spectrum is inverted. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr514009.html language=enus -->
## TOPIC 00103: rfmxwcdmaprop/attr514009.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr514009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr514009.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:RRC Filter Enabled Property

SlotPhase:RRC Filter Enabled Property

**Short Name:**SlotPhase RRC Filter Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the RRC filter. Use this property to disable the filter if the received signal is already RRC-filtered.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables the RRC filter in the measurement. |
| --- | --- |
| True (1) | Enables the RRC filter in the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51400c.html language=enus -->
## TOPIC 00104: rfmxwcdmaprop/attr51400c.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51400c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51400c.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:All Traces Enabled Property

SlotPhase:All Traces Enabled Property

**Short Name:**SlotPhase All Traces Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515002.html language=enus -->
## TOPIC 00105: rfmxwcdmaprop/attr515002.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515002.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Synchronization Mode Property

CDA:Synchronization Mode Property

**Short Name:**CDA Sync Mode

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected and the measurement is performed over the number of slots expressed by the CDA Meas Length property, starting at CDA Meas Offset slots from the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by CDA Meas Length property, starting at CDA Meas Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515003.html language=enus -->
## TOPIC 00106: rfmxwcdmaprop/attr515003.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515003.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Offset (slots) Property

CDA:Measurement Offset (slots) Property

**Short Name:**CDA Meas Offset (slots)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [CDA Sync Mode](attr515002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, (15 - [CDA Measurement Length](attr515004.html))]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515004.html language=enus -->
## TOPIC 00107: rfmxwcdmaprop/attr515004.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515004.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Length (slots) Property

CDA:Measurement Length (slots) Property

**Short Name:**CDA Meas Length (slots)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the duration of the code domain measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1. Valid values are [1, (15 - [CDA Measurement Offset](attr515003.html))]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515005.html language=enus -->
## TOPIC 00108: rfmxwcdmaprop/attr515005.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515005.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Spectrum Inverted Property

CDA:Spectrum Inverted Property

**Short Name:**CDA Spectrum Inverted

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The spectrum is not inverted. |
| --- | --- |
| True (1) | The spectrum is inverted. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515006.html language=enus -->
## TOPIC 00109: rfmxwcdmaprop/attr515006.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515006.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:IQ Offset Removal Enabled Property

CDA:IQ Offset Removal Enabled Property

**Short Name:**CDA IQ Offset Removal Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to remove the I/Q offset before the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q offset is not removed before the CDA measurement. |
| --- | --- |
| True (1) | the I/Q offset is removed before the CDA measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515007.html language=enus -->
## TOPIC 00110: rfmxwcdmaprop/attr515007.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515007.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:RRC Filter Enabled Property

CDA:RRC Filter Enabled Property

**Short Name:**CDA RRC Filter Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the RRC filter. Use this property to disable the filter if the received signal is already RRC-filtered.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables the RRC filter in the measurement. |
| --- | --- |
| True (1) | Enables the RRC filter in the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51500d.html language=enus -->
## TOPIC 00111: rfmxwcdmaprop/attr51500d.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51500d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51500d.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Power Unit Property

CDA:Power Unit Property

**Short Name:**CDA Pwr Unit

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the measurement unit of all power results, except [CDA Results Total Pwr](attr51501b.html).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **dB**.

| dB (0) | Specifies the power relative to the total power. |
| --- | --- |
| dBm (1) | Specifies the absolute power measured. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CDA Configure Power Unit |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515017.html language=enus -->
## TOPIC 00112: rfmxwcdmaprop/attr515017.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515017.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:RMS Symbol EVM (%) Property

CDA:Results:RMS Symbol EVM (%) Property

**Short Name:**CDA Results RMS Symbol EVM (%)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the RMS EVM for the measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr515019.html language=enus -->
## TOPIC 00113: rfmxwcdmaprop/attr515019.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr515019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr515019.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:RMS Symbol Magnitude Error (%) Property

CDA:Results:RMS Symbol Magnitude Error (%) Property

**Short Name:**CDA Results RMS Symbol Magnitude Error (%)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr51501b.html language=enus -->
## TOPIC 00114: rfmxwcdmaprop/attr51501b.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr51501b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr51501b.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Total Power (dBm) Property

CDA:Results:Total Power (dBm) Property

**Short Name:**CDA Results Total Pwr (dBm)

Property of [RFmxWCDMA](crfmxwcdma.html)

Returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr516000.html language=enus -->
## TOPIC 00115: rfmxwcdmaprop/attr516000.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr516000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr516000.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Enabled Property

SlotPower:Measurement Enabled Property

**Short Name:**SlotPower Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the SlotPower measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr516002.html language=enus -->
## TOPIC 00116: rfmxwcdmaprop/attr516002.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr516002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr516002.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Offset (slots) Property

SlotPower:Measurement Offset (slots) Property

**Short Name:**SlotPower Meas Offset (slots)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPower Sync Mode](attr516007.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0. The valid values are any value greater than or equal to 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr516003.html language=enus -->
## TOPIC 00117: rfmxwcdmaprop/attr516003.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr516003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr516003.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Length (slots) Property

SlotPower:Measurement Length (slots) Property

**Short Name:**SlotPower Meas Length (slots)

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies the duration of the SlotPower measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 15. The valid values are any value greater than or equal to 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr516005.html language=enus -->
## TOPIC 00118: rfmxwcdmaprop/attr516005.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr516005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr516005.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:RRC Filter Enabled Property

SlotPower:RRC Filter Enabled Property

**Short Name:**SlotPower RRC Filter Enabled

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether to enable the RRC filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables the RRC filter in the measurement. |
| --- | --- |
| True (1) | Enables the RRC filter in the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-wcdma-prop path=rfmxwcdmaprop/attr516007.html language=enus -->
## TOPIC 00119: rfmxwcdmaprop/attr516007.html

- bundle_id: `rfmx-wcdma-prop`
- source_path: `rfmxwcdmaprop/attr516007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-wcdma-prop/raw/resource/enus/rfmxwcdmaprop/attr516007.html
- document_id: `rfmx-wcdma-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Synchronization Mode Property

SlotPower:Synchronization Mode Property

**Short Name:**SlotPower Sync Mode

Property of [RFmxWCDMA](crfmxwcdma.html)

Specifies whether the measurement is performed from the frame or slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length property starting at SlotPower Meas offset slots from the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPower Measurement Length property starting at SlotPower Measurement Offset slots from the slot boundary. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |
