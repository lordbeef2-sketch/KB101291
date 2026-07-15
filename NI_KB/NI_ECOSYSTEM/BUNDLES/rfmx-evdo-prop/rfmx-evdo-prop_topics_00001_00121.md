# NI DOCUMENT BUNDLE: rfmx-evdo-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-evdo-prop start=1 end=121 -->
<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800000.html language=enus -->
## TOPIC 00001: rfmxevdoprop/attr800000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

Selector String Property

**Short Name:**Selector String

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node.

For configuration properties, you can specify the signal name and any required repeated capability instances, such as "offset0", for the property.

For results, you can specify the signal name, result name, and any required repeated capability instances for the result.

Examples:

"carrier0"

"signal::sig1/carrier0"

"result::r1/offset0"

"signal::sig1/result::r1/offset0"

You can use one of the Build String VIs to build the selector string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800001.html language=enus -->
## TOPIC 00002: rfmxevdoprop/attr800001.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800001.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Frequency, RFmxEVDO Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800002.html language=enus -->
## TOPIC 00003: rfmxevdoprop/attr800002.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800002.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Reference Level, RFmxEVDO Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800003.html language=enus -->
## TOPIC 00004: rfmxevdoprop/attr800003.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800003.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure External Attenuation, RFmxEVDO Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800004.html language=enus -->
## TOPIC 00005: rfmxevdoprop/attr800004.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800004.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the trigger type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **None**.

| None (0) | No Reference Trigger is configured. |
| --- | --- |
| Digital Edge (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Slope property. |
| Software (3) | The Reference Trigger is not asserted until a software trigger occurs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800005.html language=enus -->
## TOPIC 00006: rfmxevdoprop/attr800005.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800005.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](attr800004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

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
| High-level VIs | RFmxEVDO Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800006.html language=enus -->
## TOPIC 00007: rfmxevdoprop/attr800006.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800006.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the active edge for the trigger. This property is used only when you set the [Trigger Type](attr800004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| --- | --- |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800007.html language=enus -->
## TOPIC 00008: rfmxevdoprop/attr800007.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800007.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Source Property

Trigger:IQ Power Edge:Source Property

**Short Name:**IQ Power Edge Source

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the channel from which the device monitors the trigger. This property is used only when you set the [Trigger Type](attr800004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800008.html language=enus -->
## TOPIC 00009: rfmxevdoprop/attr800008.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800008.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level (dB or dBm) Property

Trigger:IQ Power Edge:Level (dB or dBm) Property

**Short Name:**IQ Power Edge Level

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the power level at which the device triggers. This value is expressed in dB when the [IQ Power Edge Level Type](attr800fff.html) property is set to **Relative** and in dBm when the IQ Power Edge Level Type property is set to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the [Trigger Type](attr800004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80000a.html language=enus -->
## TOPIC 00010: rfmxevdoprop/attr80000a.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80000a.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80000b.html language=enus -->
## TOPIC 00011: rfmxevdoprop/attr80000b.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80000b.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Mode Property

Trigger:Minimum Quiet Time:Mode Property

**Short Name:**Trigger Min Quiet Time Mode

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measurement computes the minimum quiet time used for triggering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto**.

| Manual (0) | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property |
| --- | --- |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800011.html language=enus -->
## TOPIC 00012: rfmxevdoprop/attr800011.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800011.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Physical Layer Subtype Property

Carrier:Physical Layer Subtype Property

**Short Name:**Physical Layer Subtype

Property of [RFmxEVDO](crfmxevdo.html)

Selects the EV-DO physical layer subtype.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **0,1**.

| 0,1 (0) | Specifies subtype 0, 1. 3GPP2 C.S0024-B v3.0 defines this subtype in 10 DEFAULT (SUBTYPE 0) AND SUBTYPE 1 PHYSICAL LAYER PROTOCOL. |
| --- | --- |
| 2 (1) | Specifies subtype 2. 3GPP2 C.S0024-B v3.0 defines this subtype in 11 SUBTYPE 2 PHYSICAL LAYER. |
| 3 (2) | Specifies subtype 3. 3GPP2 C.S0024-B v3.0 defines this subtype in 12 SUBTYPE 3 PHYSICAL LAYER. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Physical Layer Subtype |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800012.html language=enus -->
## TOPIC 00013: rfmxevdoprop/attr800012.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800012.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:Configuration Mode Property

Carrier:Channel:Configuration Mode Property

**Short Name:**Channel Configuration Mode

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to detect the channels automatically or to use a specified channel configuration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

| Auto Detect (0) | Specifies that the system automatically detects the channels. |
| --- | --- |
| User Defined (1) | Specifies that the system uses a specific channel configuration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Channel Configuration Mode |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800018.html language=enus -->
## TOPIC 00014: rfmxevdoprop/attr800018.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800018.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Uplink:Number of Channels Property

Carrier:Channel:User Defined:Uplink:Number of Channels Property

**Short Name:**UL Num Channels

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the number of user-defined channels. This property is used only when you set the [Channel Configuration Mode](attr800012.html) property to **User Defined**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Uplink Number of Channels |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800019.html language=enus -->
## TOPIC 00015: rfmxevdoprop/attr800019.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800019.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Uplink:Data Modulation Type Property

Carrier:Channel:User Defined:Uplink:Data Modulation Type Property

**Short Name:**UL Data Mod Type

Property of [RFmxEVDO](crfmxevdo.html)

Defines the modulation of the data channel. This property is used only when you set the [Channel Configuration Mode](attr800012.html) property to **User Defined**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto**.

| Auto (0) | Specifies that the measurement automatically detects the modulation type. |
| --- | --- |
| Data Channel Absent (1) | Specifies that the data channel is absent. |
| B4 (2) | Specifies binary phase shift keying (BPSK) with the Walsh function W(4,2). |
| Q4 (3) | Specifies quadrature phase shift keying (QPSK) with the Walsh function W(4,2). |
| Q2 (4) | Specifies QPSK with the Walsh function W(2,1). |
| Q4Q2 (5) | Specifies QPSK with the Walsh functions W(4,2) and W(2,1). |
| E4E2 (6) | Specifies 8-bit phase shift keying (8-PSK) with the Walsh functions W(4,2) and W(2,1). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Uplink Data Modulation Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80001b.html language=enus -->
## TOPIC 00016: rfmxevdoprop/attr80001b.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80001b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80001b.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Uplink:Walsh Code Number Property

Carrier:Channel:User Defined:Uplink:Walsh Code Number Property

**Short Name:**UL Walsh Code Number

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the Walsh Code Number of a specific user-defined channel. This property is used only when you set the [Channel Configuration Mode](attr800012.html) property to **User Defined**.

Use "channel*<n>*" as the Selector Strings to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80001c.html language=enus -->
## TOPIC 00017: rfmxevdoprop/attr80001c.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80001c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80001c.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Channel:User Defined:Uplink:Branch Property

Carrier:Channel:User Defined:Uplink:Branch Property

**Short Name:**UL Branch

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the quadrature branch on which a specific user defined-channel is mapped. This property is used only when you set the [Channel Configuration Mode](attr800012.html) property to **User Defined**.

Use "channel*<n>*" as the Selector Strings to configure or read this property.

The default value is **I**.

| I (0) | Specifies the in-phase component. |
| --- | --- |
| Q (1) | Specifies the quadrature component. |
| I and Q (2) | Specifies both the in-phase component and the quadrature component. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Uplink User Defined Channel, RFmxEVDO Configure Uplink User Defined Channel (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800029.html language=enus -->
## TOPIC 00018: rfmxevdoprop/attr800029.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800029.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Spreading:Uplink:I mask Property

Carrier:Spreading:Uplink:I mask Property

**Short Name:**UL Spreading I mask

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the long code mask of the in-phase (I) channel.

The default value is 0x0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Uplink Spreading |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80002a.html language=enus -->
## TOPIC 00019: rfmxevdoprop/attr80002a.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80002a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80002a.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Carrier:Spreading:Uplink:Q mask Property

Carrier:Spreading:Uplink:Q mask Property

**Short Name:**UL Spreading Q mask

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the long code mask of the quadrature (Q) channel.

The default value is 0x0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO Configure Uplink Spreading |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800ffc.html language=enus -->
## TOPIC 00020: rfmxevdoprop/attr800ffc.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800ffc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800ffc.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Headroom Property

Reference Level Headroom Property

**Short Name:**Reference Level Headroom

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the margin RFmx adds to the [Reference Level](attr800002.html) property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

**Supported devices:**PXIe-5668R, PXIe-5830/5831/5832/5840/5841/5842.

**Default values**

| PXIe-5668 | 6 dB |
| --- | --- |
| PXIe-5830/5831/5832/5841/5842 | 1 dB |
| PXIe-5840 | 0 dB |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr800ffd.html language=enus -->
## TOPIC 00021: rfmxevdoprop/attr800ffd.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr800ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr800ffd.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

**Valid values**

| PXIe-5830 | if0, if1 |
| --- | --- |
| PXIe-5831/5832 | if0, if1, rf<0-1>/port<x>, where 0-1 indicates one (0) or two (1) mmRH-5582 connections and x is the port number on the mmRH-5582 front panel |
| Other devices | "" (empty string) |

**Default values**

| PXIe-5830/5831/5832 | if1 |
| --- | --- |
| Other devices | "" (empty string) |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801000.html language=enus -->
## TOPIC 00022: rfmxevdoprop/attr801000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Enabled Property

ACP:Measurement Enabled Property

**Short Name:**ACP Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801008.html language=enus -->
## TOPIC 00023: rfmxevdoprop/attr801008.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801008.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Number of Offsets Property

ACP:Offset:Number of Offsets Property

**Short Name:**ACP Num Offsets

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the number of offset channels for the adjacent channel power (ACP) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 2.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Number of Offsets |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80100d.html language=enus -->
## TOPIC 00024: rfmxevdoprop/attr80100d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80100d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Power Reference:Specific Property

ACP:Offset:Power Reference:Specific Property

**Short Name:**ACP Offset Pwr Ref Specific

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the [ACP Offset Pwr Ref Carrier](attr80100c.html) property to **Specific**.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Offset Power Reference |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80100e.html language=enus -->
## TOPIC 00025: rfmxevdoprop/attr80100e.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80100e.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Integration Bandwidth (Hz) Property

ACP:Offset:Integration Bandwidth (Hz) Property

**Short Name:**ACP Offset IBW (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801012.html language=enus -->
## TOPIC 00026: rfmxevdoprop/attr801012.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801012.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Method Property

ACP:Measurement Method Property

**Short Name:**ACP Meas Method

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the method for performing the adjacent channel power (ACP) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Normal**.

| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| --- | --- |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. The accuracy of the results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Num Analysis Threads 1 Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Averaging Count | >=1 |
| ACP Num Analysis Threads | 1 |
|  | Note For multi-span FFT, the averaging count should be 1. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Measurement Method |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801016.html language=enus -->
## TOPIC 00027: rfmxevdoprop/attr801016.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801016.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Enabled Property

ACP:Averaging:Enabled Property

**Short Name:**ACP Averaging Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable averaging for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The ACP measurement uses the Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80101d.html language=enus -->
## TOPIC 00028: rfmxevdoprop/attr80101d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80101d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80101d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:RBW Filter:Type Property

ACP:RBW Filter:Type Property

**Short Name:**ACP RBW Filter Type

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | An RBW with an FFT-based response is applied. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80101f.html language=enus -->
## TOPIC 00029: rfmxevdoprop/attr80101f.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80101f.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Sweep Time:Interval (s) Property

ACP:Sweep Time:Interval (s) Property

**Short Name:**ACP Sweep Time (s)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the sweep time when you set the [ACP Sweep Time Auto](attr80101e.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.00167 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801027.html language=enus -->
## TOPIC 00030: rfmxevdoprop/attr801027.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801027.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Carrier:Relative Power (dB) Property

ACP:Results:Carrier:Relative Power (dB) Property

**Short Name:**ACP Results Carrier Rel Pwr (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the relative measured carrier power. This value is expressed in dB.

Use "carrier*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80102d.html language=enus -->
## TOPIC 00031: rfmxevdoprop/attr80102d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80102d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Relative Power (dB) Property

ACP:Results:Lower Offset:Relative Power (dB) Property

**Short Name:**ACP Results Lower Offset Rel Pwr (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801033.html language=enus -->
## TOPIC 00032: rfmxevdoprop/attr801033.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801033.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Relative Power (dB) Property

ACP:Results:Upper Offset:Relative Power (dB) Property

**Short Name:**ACP Results Upper Offset Rel Pwr (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801035.html language=enus -->
## TOPIC 00033: rfmxevdoprop/attr801035.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801035.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Near IF Output Power Offset (dB) Property

ACP:Advanced:Near IF Output Power Offset (dB) Property

**Short Name:**ACP Near IF Output Power Offset (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the [ACP Meas Method](attr801012.html) property to **Dynamic Range** and set the [ACP IF Output Power Offset Auto](attr801034.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801036.html language=enus -->
## TOPIC 00034: rfmxevdoprop/attr801036.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801036.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Far IF Output Power Offset (dB) Property

ACP:Advanced:Far IF Output Power Offset (dB) Property

**Short Name:**ACP Far IF Output Power Offset (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the [ACP Meas Method](attr801012.html) property to **Dynamic Range** and set the [ACP IF Output Power Offset Auto](attr801034.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 20.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801038.html language=enus -->
## TOPIC 00035: rfmxevdoprop/attr801038.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801038.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Sequential FFT Size Property

ACP:Advanced:Sequential FFT Size Property

**Short Name:**ACP Sequential FFT Size

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the number of bins to use for FFT computation when the [ACP Meas Method](attr801012.html) property is set to **Sequential FFT**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 512.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr801039.html language=enus -->
## TOPIC 00036: rfmxevdoprop/attr801039.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr801039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr801039.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap Mode Property

ACP:FFT:Overlap Mode Property

**Short Name:**ACP FFT Overlap Mode

Property of [RFmxEVDO](crfmxevdo.html)

Specifies how the FFT overlap is applied to the acquired samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default Value is **Disabled**.

| Disabled (0) | Indicates that no overlapping is applied to the acquired samples. |
| --- | --- |
| Automatic (1) | Indicates that RFmx chooses optimal values of the ACP FFT Overlap (%) property based on the measurement configuration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80103a.html language=enus -->
## TOPIC 00037: rfmxevdoprop/attr80103a.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80103a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80103a.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap (%) Property

ACP:FFT:Overlap (%) Property

**Short Name:**ACP FFT Overlap (%)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the number of samples to overlap between consecutive chunks while performing FFT.

This value is expressed as a percentage of [ACP Sequential FFT Size](attr801038.html) property when you set the [ACP Meas Method](attr801012.html) property to **Sequential FFT**.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr803000.html language=enus -->
## TOPIC 00038: rfmxevdoprop/attr803000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr803000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr803000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CHP:Measurement Enabled Property

CHP:Measurement Enabled Property

**Short Name:**CHP Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the channel power (CHP) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr803006.html language=enus -->
## TOPIC 00039: rfmxevdoprop/attr803006.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr803006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr803006.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Count Property

CHP:Averaging:Count Property

**Short Name:**CHP Averaging Count

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](attr803007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO CHP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80300c.html language=enus -->
## TOPIC 00040: rfmxevdoprop/attr80300c.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80300c.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CHP:RBW Filter:Auto Bandwidth Property

CHP:RBW Filter:Auto Bandwidth Property

**Short Name:**CHP RBW Auto

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measurement computes the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the RBW that you specify in the CHP RBW (Hz) property. |
| --- | --- |
| True (1) | The measurement computes the RBW. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO CHP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80300e.html language=enus -->
## TOPIC 00041: rfmxevdoprop/attr80300e.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80300e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80300e.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CHP:RBW Filter:Type Property

CHP:RBW Filter:Type Property

**Short Name:**CHP RBW Filter Type

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | An RBW filter with an FFT-based response is applied. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO CHP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr803012.html language=enus -->
## TOPIC 00042: rfmxevdoprop/attr803012.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr803012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr803012.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CHP:Sweep Time:Interval (s) Property

CHP:Sweep Time:Interval (s) Property

**Short Name:**CHP Sweep Time (s)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the sweep time when you set the [CHP Sweep Time Auto](attr803011.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.00167 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO CHP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr803015.html language=enus -->
## TOPIC 00043: rfmxevdoprop/attr803015.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr803015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr803015.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CHP:Results:Carrier:Absolute Power (dBm) Property

CHP:Results:Carrier:Absolute Power (dBm) Property

**Short Name:**CHP Results Carrier Abs Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the absolute averaged channel power (CHP) for a specific carrier. This value is expressed in dBm.

Use "carrier*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO CHP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80600c.html language=enus -->
## TOPIC 00044: rfmxevdoprop/attr80600c.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80600c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80600c.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Auto Bandwidth Property

OBW:RBW Filter:Auto Bandwidth Property

**Short Name:**OBW RBW Auto

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measurement computes the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the RBW that you specify in the OBW RBW property. |
| --- | --- |
| True (1) | The measurement computes the RBW. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80600e.html language=enus -->
## TOPIC 00045: rfmxevdoprop/attr80600e.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80600e.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Type Property

OBW:RBW Filter:Type Property

**Short Name:**OBW RBW Filter Type

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | An RBW filter with an FFT-Based response is applied. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr806013.html language=enus -->
## TOPIC 00046: rfmxevdoprop/attr806013.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr806013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr806013.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Occupied Bandwidth (Hz) Property

OBW:Results:Occupied Bandwidth (Hz) Property

**Short Name:**OBW Results Occupied BW (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the bandwidth that occupies 99 percent of the total power of the signal. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80800c.html language=enus -->
## TOPIC 00047: rfmxevdoprop/attr80800c.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80800c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80800c.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Bandwidth Integral Property

SEM:Offset:Bandwidth Integral Property

**Short Name:**SEM Offset BW Integral

Property of [RFmxEVDO](crfmxevdo.html)

Returns the bandwidth integral for a specific offset segment.

A bandwidth integral greater than 1 indicates that an RBW filter of narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment. Use the following equation to calculate the value of offset segment RBW:

*Offset segment RBW* = *RBW* * *BW integral*.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80802d.html language=enus -->
## TOPIC 00048: rfmxevdoprop/attr80802d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80802d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80802d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Absolute Integrated Power (dBm) Property

SEM:Results:Carrier:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Carrier Abs Integrated Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the absolute carrier power measurement. This value is expressed in dBm.

Use "carrier<
n
>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808034.html language=enus -->
## TOPIC 00049: rfmxevdoprop/attr808034.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808034.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Absolute Integrated Power (dBm) Property

SEM:Results:Lower Offset:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Lower Offset Abs Integrated Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808035.html language=enus -->
## TOPIC 00050: rfmxevdoprop/attr808035.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808035.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Relative Integrated Power (dB) Property

SEM:Results:Lower Offset:Relative Integrated Power (dB) Property

**Short Name:**SEM Results Lower Offset Rel Integrated Pwr (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808036.html language=enus -->
## TOPIC 00051: rfmxevdoprop/attr808036.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808036.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Absolute Peak Power (dBm) Property

SEM:Results:Lower Offset:Absolute Peak Power (dBm) Property

**Short Name:**SEM Results Lower Offset Abs Pk Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808037.html language=enus -->
## TOPIC 00052: rfmxevdoprop/attr808037.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808037.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Relative Peak Power (dB) Property

SEM:Results:Lower Offset:Relative Peak Power (dB) Property

**Short Name:**SEM Results Lower Offset Rel Pk Pwr (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808038.html language=enus -->
## TOPIC 00053: rfmxevdoprop/attr808038.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808038.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Peak Frequency (Hz) Property

SEM:Results:Lower Offset:Peak Frequency (Hz) Property

**Short Name:**SEM Results Lower Offset Pk Freq (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808041.html language=enus -->
## TOPIC 00054: rfmxevdoprop/attr808041.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808041.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808041.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Absolute Integrated Power (dBm) Property

SEM:Results:Upper Offset:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Upper Offset Abs Integrated Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm.

Use "offset<
n
>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808047.html language=enus -->
## TOPIC 00055: rfmxevdoprop/attr808047.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808047.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808047.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Absolute Power (dBm) Property

SEM:Results:Upper Offset:Margin Absolute Power (dBm) Property

**Short Name:**SEM Results Upper Offset Margin Abs Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr808049.html language=enus -->
## TOPIC 00056: rfmxevdoprop/attr808049.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr808049.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr808049.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Frequency (Hz) Property

SEM:Results:Upper Offset:Margin Frequency (Hz) Property

**Short Name:**SEM Results Upper Offset Margin Freq (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.

Use "offset*<n>*" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80c000.html language=enus -->
## TOPIC 00057: rfmxevdoprop/attr80c000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80c000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Result Fetch Timeout (s) Property

Result Fetch Timeout (s) Property

**Short Name:**Result Fetch Timeout (s)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the time to wait before results are available in the RFmxEVDO Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxEVDO Property Node waits until the measurement is complete.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10 sec.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ACP Fetch, RFmxEVDO CHP Fetch, RFmxEVDO ModAcc Fetch, RFmxEVDO OBW Fetch, RFmxEVDO SEM Fetch |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr80d000.html language=enus -->
## TOPIC 00058: rfmxevdoprop/attr80d000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr80d000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr80d000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Auto Level Initial Reference Level (dBm) Property

Advanced:Auto Level Initial Reference Level (dBm) Property

**Short Name:**Auto Level Initial Ref Level (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the reference level at which the auto leveling process starts finding the optimal reference level. This value is expressed in dBm.

The default value is 30.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811000.html language=enus -->
## TOPIC 00059: rfmxevdoprop/attr811000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Enabled Property

ModAcc:Measurement Enabled Property

**Short Name:**ModAcc Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811002.html language=enus -->
## TOPIC 00060: rfmxevdoprop/attr811002.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811002.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Synchronization Mode Property

ModAcc:Synchronization Mode Property

**Short Name:**ModAcc Sync Mode

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measurement is performed from frame, slot, or symbol boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected and measurement is performed over the Measurement Length (slots) property value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) property. |
| --- | --- |
| Slot (1) | The slot boundary is detected and measurement is performed over the Measurement Length (slots) property value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) property. |
| Arbitrary (2) | The symbol boundary is detected and measurement is performed over the Measurement Length (slots) property value, starting at the offset from the frame boundary specified in the Measurement Offset (slots) property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811005.html language=enus -->
## TOPIC 00061: rfmxevdoprop/attr811005.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811005.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Length (slots) Property

ModAcc:Measurement Length (slots) Property

**Short Name:**ModAcc Meas Length (slots)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the duration of the modulation accuracy measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811006.html language=enus -->
## TOPIC 00062: rfmxevdoprop/attr811006.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811006.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Spectrum Inverted Property

ModAcc:Spectrum Inverted Property

**Short Name:**ModAcc Spectrum Inverted

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measured spectrum is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measured spectrum is not inverted. |
| --- | --- |
| True (1) | The measured spectrum is inverted. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811007.html language=enus -->
## TOPIC 00063: rfmxevdoprop/attr811007.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811007.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Offset Removal Enabled Property

ModAcc:IQ Offset Removal Enabled Property

**Short Name:**ModAcc IQ Offset Removal Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to remove the I/Q offset before the EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q offset is not removed before the EVM measurement. |
| --- | --- |
| True (1) | The I/Q offset is removed before the EVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811008.html language=enus -->
## TOPIC 00064: rfmxevdoprop/attr811008.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811008.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Multi Carrier Filter:Enabled Property

ModAcc:Multi Carrier Filter:Enabled Property

**Short Name:**ModAcc MC-Filter Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The multicarrier filter is disabled. |
| --- | --- |
| True (1) | The multicarrier filter is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxEVDO ModAcc Configure Multi Carrier Filter Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81100f.html language=enus -->
## TOPIC 00065: rfmxevdoprop/attr81100f.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81100f.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error (Hz) Property

ModAcc:Results:Frequency Error (Hz) Property

**Short Name:**ModAcc Results Freq Error (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the frequency error averaged over all measured slots. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811011.html language=enus -->
## TOPIC 00066: rfmxevdoprop/attr811011.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811011.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:I/Q Origin Offset (dB) Property

ModAcc:Results:I/Q Origin Offset (dB) Property

**Short Name:**ModAcc Results I/Q Origin Offset (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811012.html language=enus -->
## TOPIC 00067: rfmxevdoprop/attr811012.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811012.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:I/Q Gain Imbalance (dB) Property

ModAcc:Results:I/Q Gain Imbalance (dB) Property

**Short Name:**ModAcc Results I/Q Gain Imbalance (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811013.html language=enus -->
## TOPIC 00068: rfmxevdoprop/attr811013.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811013.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:I/Q Quadrature Error (deg) Property

ModAcc:Results:I/Q Quadrature Error (deg) Property

**Short Name:**ModAcc Results I/Q Quadrature Error (deg)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in

degrees.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811014.html language=enus -->
## TOPIC 00069: rfmxevdoprop/attr811014.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811014.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:RMS EVM (%) Property

ModAcc:Results:Uplink:RMS EVM (%) Property

**Short Name:**ModAcc Results UL RMS EVM (%)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. This

value is expressed as a percentage.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811016.html language=enus -->
## TOPIC 00070: rfmxevdoprop/attr811016.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811016.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:RMS Magnitude Error (%) Property

ModAcc:Results:Uplink:RMS Magnitude Error (%) Property

**Short Name:**ModAcc Results UL RMS Magnitude Error (%)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the RMS of the magnitude error. This value is expressed as a percentage.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811018.html language=enus -->
## TOPIC 00071: rfmxevdoprop/attr811018.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811018.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:Rho Property

ModAcc:Results:Uplink:Rho Property

**Short Name:**ModAcc Results UL Rho

Property of [RFmxEVDO](crfmxevdo.html)

Returns the measured Rho value of the analyzed signal.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81101b.html language=enus -->
## TOPIC 00072: rfmxevdoprop/attr81101b.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81101b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81101b.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:Peak CDE Walsh Code Number Property

ModAcc:Results:Uplink:Peak CDE Walsh Code Number Property

**Short Name:**ModAcc Results UL Pk CDE Walsh Code Number

Property of [RFmxEVDO](crfmxevdo.html)

Returns the Walsh code number of the channel corresponding to the [ModAcc:Uplink:Peak CDE (db)](attr811019.html) result.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr811023.html language=enus -->
## TOPIC 00073: rfmxevdoprop/attr811023.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr811023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr811023.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:Detected Channels:Branch Property

ModAcc:Results:Uplink:Detected Channels:Branch Property

**Short Name:**ModAcc Results UL Detected Branch

Property of [RFmxEVDO](crfmxevdo.html)

Returns the quadrature branch of a particular detected channel.

Use "channel*<n>*" as the selector string to read this property.

| I (0) | The detected channel occupies the in-phase branch. |
| --- | --- |
| Q (1) | The detected channel occupies the quadrature branch. |
| I and Q (2) | The detected channel occupies the in-phase branch and the quadrature branch. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81104d.html language=enus -->
## TOPIC 00074: rfmxevdoprop/attr81104d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81104d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81104d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:Peak CDE Branch Property

ModAcc:Results:Uplink:Peak CDE Branch Property

**Short Name:**ModAcc Results UL Pk CDE Branch

Property of [RFmxEVDO](crfmxevdo.html)

Returns the branch of the channel corresponding to the [Peak Active CDE (dB)](attr81101c.html) property result.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

| I (0) | Returns the in-phase branch of the peak CDE. |
| --- | --- |
| Q (1) | Returns the quadrature branch of the peak CDE. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxEVDO ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr8110a1.html language=enus -->
## TOPIC 00075: rfmxevdoprop/attr8110a1.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr8110a1.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr8110a1.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Gain Imbalance Removal Enabled Property

ModAcc:IQ Gain Imbalance Removal Enabled Property

**Short Name:**ModAcc IQ Gain Imbalance Removal Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to remove the I/Q gain imbalance before the EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q gain imbalance is not removed before the EVM measurement. |
| --- | --- |
| True (1) | The I/Q gain imbalance is removed before the EVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr8110a2.html language=enus -->
## TOPIC 00076: rfmxevdoprop/attr8110a2.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr8110a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr8110a2.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Quadrature Error Removal Enabled Property

ModAcc:IQ Quadrature Error Removal Enabled Property

**Short Name:**ModAcc IQ Quadrature Error Removal Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to remove the I/Q quadrature error before the EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q quadrature error is not removed before the EVM measurement. |
| --- | --- |
| True (1) | The I/Q quadrature error is removed before the EVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813000.html language=enus -->
## TOPIC 00077: rfmxevdoprop/attr813000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Enabled Property

CDA:Measurement Enabled Property

**Short Name:**CDA Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813003.html language=enus -->
## TOPIC 00078: rfmxevdoprop/attr813003.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813003.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Offset (slots) Property

CDA:Measurement Offset (slots) Property

**Short Name:**CDA Meas Offset (slots)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [CDA Sync Mode](attr813002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0,15]. The sum of CDA Meas Offset and CDA Meas Length is less than or equal to 16.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813005.html language=enus -->
## TOPIC 00079: rfmxevdoprop/attr813005.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813005.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Channel:Uplink:Walsh Code Length Property

CDA:Measurement Channel:Uplink:Walsh Code Length Property

**Short Name:**CDA Meas Ch UL Walsh Code Length

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the Walsh code length of the channel, subject to channel-specific analysis.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 16. Valid values are 2, 4, 8, 16, and 32.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813007.html language=enus -->
## TOPIC 00080: rfmxevdoprop/attr813007.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813007.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Channel:Uplink:Branch Property

CDA:Measurement Channel:Uplink:Branch Property

**Short Name:**CDA Meas Ch UL Branch

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the Walsh branch of the channel, subject to channel-specific analysis.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **I**.

| I (0) | Specifies the in-phase branch. |
| --- | --- |
| Q (1) | Specifies the quadrature branch. |
| I and Q (2) | Specifies the in-phase and quadrature branch. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813008.html language=enus -->
## TOPIC 00081: rfmxevdoprop/attr813008.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813008.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Power Unit Property

CDA:Power Unit Property

**Short Name:**CDA Pwr Unit

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the measurement unit of the code domain power results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **dB**.

| dB (0) | Specifies that the measurement unit is dB. |
| --- | --- |
| dBm (1) | Specifies that the measurement unit is dBm. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813009.html language=enus -->
## TOPIC 00082: rfmxevdoprop/attr813009.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813009.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Spectrum Inverted Property

CDA:Spectrum Inverted Property

**Short Name:**CDA Spectrum Inverted

Property of [RFmxEVDO](crfmxevdo.html)

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

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81300a.html language=enus -->
## TOPIC 00083: rfmxevdoprop/attr81300a.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81300a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81300a.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:IQ Offset Removal Enabled Property

CDA:IQ Offset Removal Enabled Property

**Short Name:**CDA IQ Offset Removal Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to remove the I/Q offset before the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q offset is not removed before the CDA measurement. |
| --- | --- |
| True (1) | The I/Q offset is removed before the CDA measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81300b.html language=enus -->
## TOPIC 00084: rfmxevdoprop/attr81300b.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81300b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81300b.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:IQ Gain Imbalance Removal Enabled Property

CDA:IQ Gain Imbalance Removal Enabled Property

**Short Name:**CDA IQ Gain Imbalance Removal Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to remove the I/Q gain imbalance before the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q gain imbalance is not removed before the CDA measurement. |
| --- | --- |
| True (1) | The I/Q gain imbalance is removed before the CDA measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81300c.html language=enus -->
## TOPIC 00085: rfmxevdoprop/attr81300c.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81300c.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:IQ Quadrature Error Removal Enabled Property

CDA:IQ Quadrature Error Removal Enabled Property

**Short Name:**CDA IQ Quadrature Error Removal Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to remove the I/Q quadrature error before the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The I/Q quadrature error is not removed before the CDA measurement. |
| --- | --- |
| True (1) | The I/Q quadrature error is removed before the CDA measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81300d.html language=enus -->
## TOPIC 00086: rfmxevdoprop/attr81300d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81300d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81300d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Receive Filter Enabled Property

CDA:Receive Filter Enabled Property

**Short Name:**CDA Receive Filter Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable receive filtering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Receive filtering is disabled. |
| --- | --- |
| True (1) | Receive filtering is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81300e.html language=enus -->
## TOPIC 00087: rfmxevdoprop/attr81300e.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81300e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81300e.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:All Traces Enabled Property

CDA:All Traces Enabled Property

**Short Name:**CDA All Traces Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the traces after performing the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813011.html language=enus -->
## TOPIC 00088: rfmxevdoprop/attr813011.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813011.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Frequency Error (Hz) Property

CDA:Results:Frequency Error (Hz) Property

**Short Name:**CDA Results Freq Error (Hz)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the frequency error. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813013.html language=enus -->
## TOPIC 00089: rfmxevdoprop/attr813013.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813013.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:I/Q Origin Offset (dB) Property

CDA:Results:I/Q Origin Offset (dB) Property

**Short Name:**CDA Results I/Q Origin Offset (dB)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the I/Q origin offset. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813015.html language=enus -->
## TOPIC 00090: rfmxevdoprop/attr813015.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813015.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:I/Q Quadrature Error (deg) Property

CDA:Results:I/Q Quadrature Error (deg) Property

**Short Name:**CDA Results I/Q Quadrature Error (deg)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the I/Q quadrature error. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813016.html language=enus -->
## TOPIC 00091: rfmxevdoprop/attr813016.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813016.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:RMS Symbol EVM (%) Property

CDA:Results:Uplink:RMS Symbol EVM (%) Property

**Short Name:**CDA Results UL RMS Symbol EVM (%)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813017.html language=enus -->
## TOPIC 00092: rfmxevdoprop/attr813017.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813017.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Peak Symbol EVM (%) Property

CDA:Results:Uplink:Peak Symbol EVM (%) Property

**Short Name:**CDA Results UL Pk Symbol EVM (%)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813019.html language=enus -->
## TOPIC 00093: rfmxevdoprop/attr813019.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813019.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:RMS Symbol Phase Error (deg) Property

CDA:Results:Uplink:RMS Symbol Phase Error (deg) Property

**Short Name:**CDA Results UL RMS Symbol Phase Error (deg)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81301a.html language=enus -->
## TOPIC 00094: rfmxevdoprop/attr81301a.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81301a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81301a.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Mean Symbol Power (dB or dBm) Property

CDA:Results:Uplink:Mean Symbol Power (dB or dBm) Property

**Short Name:**CDA Results UL Mean Symbol Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81301b.html language=enus -->
## TOPIC 00095: rfmxevdoprop/attr81301b.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81301b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81301b.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Total Power (dBm) Property

CDA:Results:Uplink:Total Power (dBm) Property

**Short Name:**CDA Results UL Total Pwr (dBm)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the mean power of the received signal. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81301c.html language=enus -->
## TOPIC 00096: rfmxevdoprop/attr81301c.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81301c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81301c.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Total Active Power (dB or dBm) Property

CDA:Results:Uplink:Total Active Power (dB or dBm) Property

**Short Name:**CDA Results UL Total Active Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the sum of the powers of all active code channels. If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81301d.html language=enus -->
## TOPIC 00097: rfmxevdoprop/attr81301d.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81301d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81301d.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Mean Active Power (dB or dBm) Property

CDA:Results:Uplink:Mean Active Power (dB or dBm) Property

**Short Name:**CDA Results UL Mean Active Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the average power of all active code channels. If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81301e.html language=enus -->
## TOPIC 00098: rfmxevdoprop/attr81301e.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81301e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81301e.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Peak Active Power (dB or dBm) Property

CDA:Results:Uplink:Peak Active Power (dB or dBm) Property

**Short Name:**CDA Results UL Pk Active Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the maximum power among all the active code channels. If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813020.html language=enus -->
## TOPIC 00099: rfmxevdoprop/attr813020.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813020.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Peak Inactive Power (dB or dBm) Property

CDA:Results:Uplink:Peak Inactive Power (dB or dBm) Property

**Short Name:**CDA Results UL Pk Inactive Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.

If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813021.html language=enus -->
## TOPIC 00100: rfmxevdoprop/attr813021.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813021.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:I Mean Active Power (dB or dBm) Property

CDA:Results:Uplink:I Mean Active Power (dB or dBm) Property

**Short Name:**CDA Results UL I Mean Active Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the average power of all active code channels measured on the I-branch. If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813022.html language=enus -->
## TOPIC 00101: rfmxevdoprop/attr813022.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813022.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:I Peak Inactive Power (dB or dBm) Property

CDA:Results:Uplink:I Peak Inactive Power (dB or dBm) Property

**Short Name:**CDA Results UL I Pk Inactive Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise.

If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813023.html language=enus -->
## TOPIC 00102: rfmxevdoprop/attr813023.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813023.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Q Mean Active Power (dB or dBm) Property

CDA:Results:Uplink:Q Mean Active Power (dB or dBm) Property

**Short Name:**CDA Results UL Q Mean Active Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the average power of all active code channels measured on the Q-branch. If you set the [CDA Power Unit](attr813008.html) property to **dBm**, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813024.html language=enus -->
## TOPIC 00103: rfmxevdoprop/attr813024.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813024.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813024.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Q Peak Inactive Power (dB or dBm) Property

CDA:Results:Uplink:Q Peak Inactive Power (dB or dBm) Property

**Short Name:**CDA Results UL Q Pk Inactive Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm.

The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813025.html language=enus -->
## TOPIC 00104: rfmxevdoprop/attr813025.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813025.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Mean Pilot Power (dB or dBm) Property

CDA:Results:Uplink:Mean Pilot Power (dB or dBm) Property

**Short Name:**CDA Results UL Mean Pilot Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr813026.html language=enus -->
## TOPIC 00105: rfmxevdoprop/attr813026.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr813026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr813026.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Uplink:Mean Auxiliary Pilot Power (dB or dBm) Property

CDA:Results:Uplink:Mean Auxiliary Pilot Power (dB or dBm) Property

**Short Name:**CDA Results UL Mean Aux Pilot Pwr

Property of [RFmxEVDO](crfmxevdo.html)

Returns the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr814000.html language=enus -->
## TOPIC 00106: rfmxevdoprop/attr814000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr814000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr814000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Enabled Property

SlotPower:Measurement Enabled Property

**Short Name:**SlotPower Enabled

Property of [RFmxEVDO](crfmxevdo.html)

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

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr814002.html language=enus -->
## TOPIC 00107: rfmxevdoprop/attr814002.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr814002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr814002.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Synchronization Mode Property

SlotPower:Synchronization Mode Property

**Short Name:**SlotPower Sync Mode

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measurement is performed from the frame or the slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at SlotPower Meas Offset slots from the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at SlotPower Meas Offset slots from the slot boundary. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr814003.html language=enus -->
## TOPIC 00108: rfmxevdoprop/attr814003.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr814003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr814003.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Offset (slots) Property

SlotPower:Measurement Offset (slots) Property

**Short Name:**SlotPower Meas Offset (slots)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPower Sync Mode](attr814002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr814004.html language=enus -->
## TOPIC 00109: rfmxevdoprop/attr814004.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr814004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr814004.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Length (slots) Property

SlotPower:Measurement Length (slots) Property

**Short Name:**SlotPower Meas Length (slots)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the duration of the SlotPower measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 16.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr814005.html language=enus -->
## TOPIC 00110: rfmxevdoprop/attr814005.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr814005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr814005.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Spectrum Inverted Property

SlotPower:Spectrum Inverted Property

**Short Name:**SlotPower Spectrum Inverted

Property of [RFmxEVDO](crfmxevdo.html)

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

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr814006.html language=enus -->
## TOPIC 00111: rfmxevdoprop/attr814006.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr814006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr814006.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Receive Filter Enabled Property

SlotPower:Receive Filter Enabled Property

**Short Name:**SlotPower Receive Filter Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable receive filtering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Receive filtering is disabled. |
| --- | --- |
| True (1) | Receive filtering is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815000.html language=enus -->
## TOPIC 00112: rfmxevdoprop/attr815000.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815000.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Measurement Enabled Property

SlotPhase:Measurement Enabled Property

**Short Name:**SlotPhase Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815002.html language=enus -->
## TOPIC 00113: rfmxevdoprop/attr815002.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815002.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Synchronization Mode Property

SlotPhase:Synchronization Mode Property

**Short Name:**SlotPhase Sync Mode

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether the measurement is performed from the frame or the slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the slot boundary. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815003.html language=enus -->
## TOPIC 00114: rfmxevdoprop/attr815003.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815003.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Measurement Offset (slots) Property

SlotPhase:Measurement Offset (slots) Property

**Short Name:**SlotPhase Meas Offset (slots)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPhase Sync Mode](attr815002.html)property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815004.html language=enus -->
## TOPIC 00115: rfmxevdoprop/attr815004.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815004.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Measurement Length (slots) Property

SlotPhase:Measurement Length (slots) Property

**Short Name:**SlotPhase Meas Length (slots)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the duration of the SlotPhase measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 16.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815005.html language=enus -->
## TOPIC 00116: rfmxevdoprop/attr815005.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815005.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Spectrum Inverted Property

SlotPhase:Spectrum Inverted Property

**Short Name:**SlotPhase Spectrum Inverted

Property of [RFmxEVDO](crfmxevdo.html)

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

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815006.html language=enus -->
## TOPIC 00117: rfmxevdoprop/attr815006.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815006.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Receive Filter Enabled Property

SlotPhase:Receive Filter Enabled Property

**Short Name:**SlotPhase Receive Filter Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable receive filtering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Receive filtering is disabled. |
| --- | --- |
| True (1) | Receive filtering is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815007.html language=enus -->
## TOPIC 00118: rfmxevdoprop/attr815007.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815007.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Transient Duration (s) Property

SlotPhase:Transient Duration (s) Property

**Short Name:**SlotPhase Transient Duration (s)

Property of [RFmxEVDO](crfmxevdo.html)

Specifies the transient duration for the SlotPhase measurement. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The transient duration is applied equally on either side of a half-slot boundary, that is, at the start and end of each half-slot.

Setting the transient duration equal to zero means that no transient period is considered, and the entire half-slot data is used to determine the phase error best-fit line used to compute the phase discontinuity at the half-slot boundaries.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr815008.html language=enus -->
## TOPIC 00119: rfmxevdoprop/attr815008.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr815008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr815008.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:All Traces Enabled Property

SlotPhase:All Traces Enabled Property

**Short Name:**SlotPhase All Traces Enabled

Property of [RFmxEVDO](crfmxevdo.html)

Specifies whether to enable the traces after performing the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/attr81500b.html language=enus -->
## TOPIC 00120: rfmxevdoprop/attr81500b.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/attr81500b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/attr81500b.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Results:Maximum Half Slot Phase Discontinuity (deg) Property

SlotPhase:Results:Maximum Half Slot Phase Discontinuity (deg) Property

**Short Name:**SlotPhase Results Max Half Slot Phase Disc (deg)

Property of [RFmxEVDO](crfmxevdo.html)

Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-evdo-prop path=rfmxevdoprop/crfmxevdo.html language=enus -->
## TOPIC 00121: rfmxevdoprop/crfmxevdo.html

- bundle_id: `rfmx-evdo-prop`
- source_path: `rfmxevdoprop/crfmxevdo.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-evdo-prop/raw/resource/enus/rfmxevdoprop/crfmxevdo.html
- document_id: `rfmx-evdo-prop`
- page_type: `leaf`
- content_type: ``

RFmxEVDO Properties

RFmxEVDO Properties

Use the RFmxEVDO properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node. Details |
| Selected Ports | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. Details |
| Center Frequency (Hz) | Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. Details |
| Reference Level | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. Details |
| External Attenuation (dB) | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Details |
| Reference Level Headroom | Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Details |
| Trigger:Type | Specifies the trigger type. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:IQ Power Edge:Source | Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level (dB or dBm) | Specifies the power level at which the device triggers. This value is expressed in dB when the IQ Power Edge Level Type property is set to Relative and in dBm when the IQ Power Edge Level Type property is set to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level Type | Specifies the reference for the IQ Power Edge Level property. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Slope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:Delay (s) | Specifies the trigger delay time. This value is expressed in seconds. Details |
| Trigger:Minimum Quiet Time:Mode | Specifies whether the measurement computes the minimum quiet time used for triggering. Details |
| Trigger:Minimum Quiet Time:Duration (s) | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope, the signal is quiet above the trigger level. Details |
| Band Class | Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0. Details |
| Carrier:Number of Carriers | Specifies the number of carriers in the signal. Details |
| Carrier:Frequency (Hz) | Specifies the carrier frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. Use "carrier<n>" as the Selector Strings to configure or read this property. The default value is 0. Details |
| Carrier:Physical Layer Subtype | Selects the EV-DO physical layer subtype. Details |
| Carrier:Channel:Configuration Mode | Specifies whether to detect the channels automatically or to use a specified channel configuration. Details |
| Carrier:Channel:User Defined:Uplink:Number of Channels | Specifies the number of user-defined channels. This property is used only when you set the Channel Configuration Mode property to User Defined. Details |
| Carrier:Channel:User Defined:Uplink:Data Modulation Type | Defines the modulation of the data channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Details |
| Carrier:Channel:User Defined:Uplink:Walsh Code Length | Specifies the Walsh Code Length of a specific user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the Selector Strings to configure or read this property. Details |
| Carrier:Channel:User Defined:Uplink:Walsh Code Number | Specifies the Walsh Code Number of a specific user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the Selector Strings to configure or read this property. Details |
| Carrier:Channel:User Defined:Uplink:Branch | Specifies the quadrature branch on which a specific user defined-channel is mapped. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the Selector Strings to configure or read this property. Details |
| Carrier:Spreading:Uplink:I mask | Specifies the long code mask of the in-phase (I) channel. The default value is 0x0. Details |
| Carrier:Spreading:Uplink:Q mask | Specifies the long code mask of the quadrature (Q) channel. The default value is 0x0. Details |
| ModAcc:Measurement Enabled | Specifies whether to enable the ModAcc measurement. Details |
| ModAcc:Synchronization Mode | Specifies whether the measurement is performed from frame, slot, or symbol boundary. Details |
| ModAcc:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the ModAcc Sync Mode property. Details |
| ModAcc:Measurement Length (slots) | Specifies the duration of the modulation accuracy measurement. Details |
| ModAcc:Spectrum Inverted | Specifies whether the measured spectrum is inverted. Details |
| ModAcc:IQ Offset Removal Enabled | Specifies whether to remove the I/Q offset before the EVM measurement. Details |
| ModAcc:IQ Gain Imbalance Removal Enabled | Specifies whether to remove the I/Q gain imbalance before the EVM measurement. Details |
| ModAcc:IQ Quadrature Error Removal Enabled | Specifies whether to remove the I/Q quadrature error before the EVM measurement. Details |
| ModAcc:Receive Filter Enabled | Specifies whether to enable receive filtering. Details |
| ModAcc:Multi Carrier Filter:Enabled | Enables the multi-carrier filter that can increase the multi-carrier interference suppression to improve ModAcc measurement quality in the presence of neighboring carriers. Details |
| ModAcc:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. Details |
| ModAcc:Results:Frequency Error (Hz) | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. Details |
| ModAcc:Results:Chip Rate Error (ppm) | Returns the chip rate error averaged over all measured slots. This value is expressed in parts per million (ppm). Details |
| ModAcc:Results:I/Q Origin Offset (dB) | Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. Details |
| ModAcc:Results:I/Q Gain Imbalance (dB) | Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. Details |
| ModAcc:Results:I/Q Quadrature Error (deg) | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. Details |
| ModAcc:Results:Uplink:RMS EVM (%) | Returns the RMS of the uplink error vector magnitude (EVM), averaged over all measured slots. This value is expressed as a percentage. Details |
| ModAcc:Results:Uplink:Peak EVM (%) | Returns the peak value of the uplink error vector magnitude (EVM), averaged over all measured slots. This value is expressed as a percentage. Details |
| ModAcc:Results:Uplink:RMS Magnitude Error (%) | Returns the RMS of the magnitude error. This value is expressed as a percentage. Details |
| ModAcc:Results:Uplink:RMS Phase Error (Deg) | Returns the RMS of the phase error. This value is expressed in degrees. Details |
| ModAcc:Results:Uplink:Rho | Returns the measured Rho value of the analyzed signal. Details |
| ModAcc:Results:Uplink:Peak CDE (dB) | Returns the peak uplink code domain error (CDE), expressed in dB. Details |
| ModAcc:Results:Uplink:Peak CDE Walsh Code Number | Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak CDE (db) result. Details |
| ModAcc:Results:Uplink:Peak CDE Branch | Returns the branch of the channel corresponding to the Peak Active CDE (dB) property result. Details |
| ModAcc:Results:Uplink:Peak Active CDE (dB) | Returns the peak code domain error (CDE) value among the active Walsh channels. This value is expressed in dB. Details |
| ModAcc:Results:Uplink:Peak Active CDE Walsh Code Length | The Walsh code length of the active Walsh channel for which the peak CDE has been observed. Details |
| ModAcc:Results:Uplink:Peak Active CDE Walsh Code Number | Returns the Walsh code number of the channel corresponding to the ModAcc:Uplink:Peak Active CDE (dB) result. Details |
| ModAcc:Results:Uplink:Peak Active CDE Branch | Returns the quadrature branch of the channel corresponding to the Peak Active CDE (dB) result. Details |
| ModAcc:Results:Uplink:Detected Data Modulation Type | Returns the modulation type of the uplink data channel. Details |
| ModAcc:Results:Uplink:Number of Detected Channels | Returns the total number of detected channels. Details |
| ModAcc:Results:Uplink:Detected Channels:Code Length | Returns the Walsh Code length of a detected channel. Use "channel<n>" as the selector string to read this property. Details |
| ModAcc:Results:Uplink:Detected Channels:Code Number | Returns the Walsh Code number of a detected channel. Use "channel<n>" as the selector string to read this property. Details |
| ModAcc:Results:Uplink:Detected Channels:Branch | Returns the quadrature branch of a particular detected channel. Use "channel<n>" as the selector string to read this property. Details |
| ACP:Measurement Enabled | Specifies whether to enable the ACP measurement. Details |
| ACP:Carrier:Integration Bandwidth (Hz) | Returns the ACP carrier integration bandwidth. This value is expressed in Hz. Details |
| ACP:Offset:Number of Offsets | Specifies the number of offset channels for the adjacent channel power (ACP) measurement. Details |
| ACP:Offset:Frequency (Hz) | Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. Details |
| ACP:Offset:Power Reference:Carrier | Specifies the carrier number that is used as the power reference to measure the offset channel relative power. Details |
| ACP:Offset:Power Reference:Specific | Specifies the index of the carrier used as the reference carrier. The power measured in this carrier is used as the power reference for measuring the offset channel relative power when you set the ACP Offset Pwr Ref Carrier property to Specific. Details |
| ACP:Offset:Integration Bandwidth (Hz) | Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. Details |
| ACP:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| ACP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the ACP RBW Auto property to False. This value is expressed in Hz. Details |
| ACP:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| ACP:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| ACP:Sweep Time:Interval (s) | Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| ACP:Measurement Method | Specifies the method for performing the adjacent channel power (ACP) measurement. Details |
| ACP:Noise Compensation Enabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Details |
| ACP:Averaging:Enabled | Specifies whether to enable averaging for the ACP measurement. Details |
| ACP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True. Details |
| ACP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. Details |
| ACP:FFT:Overlap Mode | Specifies how the FFT overlap is applied to the acquired samples. Details |
| ACP:FFT:Overlap (%) | Returns the number of samples to overlap between consecutive chunks while performing FFT. This value is expressed as a percentage of ACP Sequential FFT Size property when you set the ACP Meas Method property to Sequential FFT. Details |
| ACP:Advanced:IF Output Power Offset Auto | Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the adjacent channel power (ACP) measurement. This property is used only if you set the ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Near IF Output Power Offset (dB) | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False. Details |
| ACP:Advanced:Far IF Output Power Offset (dB) | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False. Details |
| ACP:Advanced:Sequential FFT Size | Specifies the number of bins to use for FFT computation when the ACP Meas Method property is set to Sequential FFT. Details |
| ACP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. Details |
| ACP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement. Details |
| ACP:Results:Total Carrier Power (dBm) | Returns the total carrier power measured by the adjacent channel power (ACP) measurement. This value is expressed in dBm. Details |
| ACP:Results:Carrier:Absolute Power (dBm) | Returns the absolute measured carrier power. This value is expressed in dBm. Use "carrier<n>" as the selector string to read this property. Details |
| ACP:Results:Carrier:Relative Power (dB) | Returns the relative measured carrier power. This value is expressed in dB. Use "carrier<n>" as the selector string to read this property. Details |
| ACP:Results:Lower Offset:Absolute Power (dBm) | Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| ACP:Results:Lower Offset:Relative Power (dB) | Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| ACP:Results:Upper Offset:Absolute Power (dBm) | Returns the absolute measured upper offset channel power. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| ACP:Results:Upper Offset:Relative Power (dB) | Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| CHP:Measurement Enabled | Specifies whether to enable the channel power (CHP) measurement. Details |
| CHP:Carrier Integration Bandwidth (Hz) | Returns the CHP carrier integration bandwidth. This value is expressed in Hz. Details |
| CHP:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| CHP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the CHP RBW Auto property to False. This value is expressed in Hz. Details |
| CHP:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| CHP:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| CHP:Sweep Time:Interval (s) | Specifies the sweep time when you set the CHP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| CHP:Averaging:Enabled | Specifies whether to enable averaging for the channel power (CHP) measurement. Details |
| CHP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. Details |
| CHP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the channel power (CHP) measurement. Details |
| CHP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the channel power (CHP) measurement. Details |
| CHP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the channel power (CHP) measurement. Details |
| CHP:Results:Total Carrier Power (dBm) | Returns the sum of all the active carrier powers. This value is expressed in dBm. Details |
| CHP:Results:Carrier:Absolute Power (dBm) | Returns the absolute averaged channel power (CHP) for a specific carrier. This value is expressed in dBm. Use "carrier<n>" as the selector string to read this property. Details |
| CHP:Results:Carrier:Relative Power (dB) | Returns the relative averaged channel power (CHP) for a specific carrier. This value is expressed in dB. Use "carrier<n>" as the selector string to read this property. Details |
| OBW:Measurement Enabled | Specifies whether to enable the occupied bandwidth (OBW) measurement. Details |
| OBW:Span (Hz) | Returns the frequency span of the OBW measurement. This value is expressed in Hz. Details |
| OBW:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| OBW:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the OBW RBW Auto property to False. This value is expressed in Hz. Details |
| OBW:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| OBW:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| OBW:Sweep Time:Interval (s) | Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. Details |
| OBW:Averaging:Enabled | Specifies whether to enable averaging for the occupied bandwidth (OBW) measurement. Details |
| OBW:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. Details |
| OBW:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for occupied bandwidth (OBW) measurement. Details |
| OBW:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the occupied bandwidth (OBW) measurement. Details |
| OBW:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the occupied bandwidth (OBW) measurement. Details |
| OBW:Results:Occupied Bandwidth (Hz) | Returns the bandwidth that occupies 99 percent of the total power of the signal. This value is expressed in Hz. Details |
| OBW:Results:Absolute Power (dBm) | Returns the absolute power measured in the occupied bandwidth (OBW). This value is expressed in dBm. Details |
| OBW:Results:Start Frequency (Hz) | Returns the start frequency of the occupied bandwidth (OBW). This value is expressed in Hz. Details |
| OBW:Results:Stop Frequency (Hz) | Returns the stop frequency of the occupied bandwidth (OBW). This value is expressed in Hz. Details |
| SEM:Measurement Enabled | Specifies whether to enable the spectral emissions mask (SEM) measurement. Details |
| SEM:Carrier:Integration Bandwidth (Hz) | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. Details |
| SEM:Offset:Number of Offsets | Returns the number of SEM offset segments. Details |
| SEM:Offset:Start Frequency (Hz) | Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. Details |
| SEM:Offset:Stop Frequency (Hz) | Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz. Details |
| SEM:Offset:RBW Filter:Bandwidth (Hz) | Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. Details |
| SEM:Offset:RBW Filter:Type | Returns the type of RBW filter used to sweep the offset segment. Details |
| SEM:Offset:Bandwidth Integral | Returns the bandwidth integral for a specific offset segment. Details |
| SEM:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| SEM:Sweep Time:Interval (s) | Specifies the sweep time when you set the SEM Sweep Time Auto property to False. This value is expressed in seconds. Details |
| SEM:Averaging:Enabled | Specifies whether to enable averaging for the spectral emissions mask (SEM) measurement. Details |
| SEM:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True. Details |
| SEM:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the spectral emissions mask (SEM) measurement. Details |
| SEM:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the spectral emissions mask (SEM) measurement. Details |
| SEM:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the spectral emissions mask (SEM) measurement. Details |
| SEM:Results:Total Carrier Power (dBm) | Returns the total carrier power of the selected carrier. This value is expressed in dBm. Details |
| SEM:Results:Composite Measurement Status | Indicates the overall measurement status based on the measurement limits and the failure criteria specified by the standard for each offset segment. Details |
| SEM:Results:Carrier:Relative Integrated Power (dB) | Returns the relative carrier power measurement. This value is expressed in dB. Use "carrier< n >" as the selector string to read this result. Details |
| SEM:Results:Carrier:Absolute Integrated Power (dBm) | Returns the absolute carrier power measurement. This value is expressed in dBm. Use "carrier< n >" as the selector string to read this result. Details |
| SEM:Results:Carrier:Absolute Peak Power (dBm) | Returns the peak absolute carrier power. This value is expressed in dBm. Use "carrier<n>" as the selector string to read this property. Details |
| SEM:Results:Carrier:Peak Frequency (Hz) | Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz. Use "carrier< n >" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Measurement Status | Indicates the lower offset segment measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Absolute Integrated Power (dBm) | Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Relative Integrated Power (dB) | Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Absolute Peak Power (dBm) | Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Relative Peak Power (dB) | Returns the peak power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Margin (dB) | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Margin Absolute Power (dBm) | Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Margin Relative Power (dB) | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Lower Offset:Margin Frequency (Hz) | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Measurement Status | Indicates the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Absolute Integrated Power (dBm) | Returns the absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset< n >" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Relative Integrated Power (dB) | Returns the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset< n >" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Absolute Peak Power (dBm) | Returns the peak absolute power measured in the upper (positive) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Relative Peak Power (dB) | Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Margin (dB) | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Margin Absolute Power (dBm) | Returns the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated power of the reference carrier. This value is expressed in dBm. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Margin Relative Power (dB) | Returns the power at which the margin occurred in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this property. Details |
| SEM:Results:Upper Offset:Margin Frequency (Hz) | Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Details |
| CDA:Measurement Enabled | Specifies whether to enable the CDA measurement. Details |
| CDA:Synchronization Mode | Specifies whether the measurement is performed from the frame, slot, or symbol boundary. Details |
| CDA:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the CDA Sync Mode property. Details |
| CDA:Measurement Length (slots) | Specifies the duration of the CDA measurement. This value is expressed in slots. Details |
| CDA:Measurement Channel:Uplink:Walsh Code Length | Specifies the Walsh code length of the channel, subject to channel-specific analysis. Details |
| CDA:Measurement Channel:Uplink:Walsh Code Number | Specifies the Walsh code number of the channel, subject to channel-specific analysis. Details |
| CDA:Measurement Channel:Uplink:Branch | Specifies the Walsh branch of the channel, subject to channel-specific analysis. Details |
| CDA:Power Unit | Specifies the measurement unit of the code domain power results. Details |
| CDA:Spectrum Inverted | Specifies whether the signal spectrum is inverted. Details |
| CDA:IQ Offset Removal Enabled | Specifies whether to remove the I/Q offset before the CDA measurement. Details |
| CDA:IQ Gain Imbalance Removal Enabled | Specifies whether to remove the I/Q gain imbalance before the CDA measurement. Details |
| CDA:IQ Quadrature Error Removal Enabled | Specifies whether to remove the I/Q quadrature error before the CDA measurement. Details |
| CDA:Receive Filter Enabled | Specifies whether to enable receive filtering. Details |
| CDA:All Traces Enabled | Specifies whether to enable the traces after performing the CDA measurement. Details |
| CDA:Results:Frequency Error (Hz) | Returns the frequency error. This value is expressed in Hz. Details |
| CDA:Results:Chip Rate Error (ppm) | Returns the chip rate error. This value is expressed in ppm. Details |
| CDA:Results:I/Q Origin Offset (dB) | Returns the I/Q origin offset. This value is expressed in dB. Details |
| CDA:Results:I/Q Gain Imbalance (dB) | Returns the I/Q gain imbalance. This value is expressed in dB. Details |
| CDA:Results:I/Q Quadrature Error (deg) | Returns the I/Q quadrature error. This value is expressed in degrees. Details |
| CDA:Results:Uplink:RMS Symbol EVM (%) | Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. Details |
| CDA:Results:Uplink:Peak Symbol EVM (%) | Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. Details |
| CDA:Results:Uplink:RMS Symbol Magnitude Error (%) | Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. Details |
| CDA:Results:Uplink:RMS Symbol Phase Error (deg) | Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. Details |
| CDA:Results:Uplink:Mean Symbol Power (dB or dBm) | Returns the mean symbol power of the configured measurement channel. This value is expressed in dB or dBm. Details |
| CDA:Results:Uplink:Total Power (dBm) | Returns the mean power of the received signal. This value is expressed in dBm. Details |
| CDA:Results:Uplink:Total Active Power (dB or dBm) | Returns the sum of the powers of all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:Mean Active Power (dB or dBm) | Returns the average power of all active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:Peak Active Power (dB or dBm) | Returns the maximum power among all the active code channels. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:Mean Inactive Power (dB or dBm) | Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:Peak Inactive Power (dB or dBm) | Returns the largest measured code power among the set of inactive channels in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:I Mean Active Power (dB or dBm) | Returns the average power of all active code channels measured on the I-branch. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:I Peak Inactive Power (dB or dBm) | Returns the largest measured code power among the set of inactive channels on the I-branch, and in the code domain of the base spreading factor. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1; 32 otherwise. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:Q Mean Active Power (dB or dBm) | Returns the average power of all active code channels measured on the Q-branch. If you set the CDA Power Unit property to dBm, the measurement returns the absolute measured power in dBm. Otherwise, the measurement returns the value relative to the total power in dB. Details |
| CDA:Results:Uplink:Q Peak Inactive Power (dB or dBm) | Returns the largest measured code power among the set of inactive channels on the Q-branch, and in the code domain of the base spreading factor. This value is expressed in dB or dBm. The base spreading factor depends on the configured physical layer subtype, and is 16 for subtype 0/1, and 32 otherwise. Details |
| CDA:Results:Uplink:Mean Pilot Power (dB or dBm) | Returns the mean power of the Reverse Pilot channel (R-PICH). This value is expressed in dB or dBm. Details |
| CDA:Results:Uplink:Mean Auxiliary Pilot Power (dB or dBm) | Returns the mean power of the Reverse Auxiliary Pilot Channel (R-APICH). This value is expressed in dB or dBm. Details |
| SlotPower:Measurement Enabled | Specifies whether to enable the SlotPower measurement. Details |
| SlotPower:Synchronization Mode | Specifies whether the measurement is performed from the frame or the slot boundary. Details |
| SlotPower:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode property. Details |
| SlotPower:Measurement Length (slots) | Specifies the duration of the SlotPower measurement. This value is expressed in slots. Details |
| SlotPower:Spectrum Inverted | Specifies whether the signal spectrum is inverted. Details |
| SlotPower:Receive Filter Enabled | Specifies whether to enable receive filtering. Details |
| SlotPhase:Measurement Enabled | Specifies whether to enable the SlotPhase measurement. Details |
| SlotPhase:Synchronization Mode | Specifies whether the measurement is performed from the frame or the slot boundary. Details |
| SlotPhase:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Modeproperty. Details |
| SlotPhase:Measurement Length (slots) | Specifies the duration of the SlotPhase measurement. This value is expressed in slots. Details |
| SlotPhase:Spectrum Inverted | Specifies whether the signal spectrum is inverted. Details |
| SlotPhase:Receive Filter Enabled | Specifies whether to enable receive filtering. Details |
| SlotPhase:Transient Duration (s) | Specifies the transient duration for the SlotPhase measurement. This value is expressed in seconds. Details |
| SlotPhase:All Traces Enabled | Specifies whether to enable the traces after performing the SlotPhase measurement. Details |
| SlotPhase:Results:Maximum Half Slot Phase Discontinuity (deg) | Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees. Details |
| Advanced:Auto Level Initial Reference Level (dBm) | Specifies the reference level at which the auto leveling process starts finding the optimal reference level. This value is expressed in dBm. Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. Details |
| Result Fetch Timeout (s) | Specifies the time to wait before results are available in the RFmxEVDO Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxEVDO Property Node waits until the measurement is complete. Details |
