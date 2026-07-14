# NI DOCUMENT BUNDLE: rfmx-for-bluetooth-test-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-for-bluetooth-test-prop start=1 end=129 -->
<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00000.html language=enus -->
## TOPIC 00001: Selector String Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00000.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

**Short Name:**Selector String

Property of [RFmxBT](crfmxbt.html)

Specifies the active channel string used to access all subsequent channel-based properties in this instance of the property node.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00001.html language=enus -->
## TOPIC 00002: Center Frequency (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00001.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxBT](crfmxbt.html)

Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is hardware dependent. The default value for the devices PXIe-5645/5820 is 0 Hz. The default value for devices PXIe-5644/5646/5840/5663/5663E/5665/5668R is 2.402 GHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00002.html language=enus -->
## TOPIC 00003: Reference Level Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00002.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxBT](crfmxbt.html)

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00003.html language=enus -->
## TOPIC 00004: External Attenuation (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00003.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxBT](crfmxbt.html)

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

For more information about attenuation, refer to the *Attenuation and Signal Levels* topic for your device in the *NI RF Vector Signal Analyzers Help*.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00004.html language=enus -->
## TOPIC 00005: Trigger:Type Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00004.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxBT](crfmxbt.html)

Specifies the type of trigger to be used for signal acquisition.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **IQ Power Edge**.

| None (0) | No reference trigger is used for signal acquisition. |
| --- | --- |
| Digital Edge (1) | A digital-edge trigger is used for signal acquisition. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge (2) | An I/Q power-edge trigger is used for signal acquisition, which is configured using the IQ Power Edge Slope property. |
| Software (3) | A software trigger is used for signal acquisition. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00005.html language=enus -->
## TOPIC 00006: Trigger:Digital Edge:Source Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxBT](crfmxbt.html)

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](attrb00004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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
| PXI_STAR (PXI_STAR) | The trigger is received on PXI star trigger line. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00006.html language=enus -->
## TOPIC 00007: Trigger:Digital Edge:Edge Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00006.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxBT](crfmxbt.html)

Specifies the active edge for the trigger. This property is valid only when you set the [Trigger Type](attrb00004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Rising Edge**.

| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| --- | --- |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00007.html language=enus -->
## TOPIC 00008: Trigger:IQ Power Edge:Source Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00007.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Source Property

**Short Name:**IQ Power Edge Source

Property of [RFmxBT](crfmxbt.html)

Specifies the channel from which the device monitors the trigger. This property is valid only when you set the [Trigger Type](attrb00004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00008.html language=enus -->
## TOPIC 00009: Trigger:IQ Power Edge:Level (dB or dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00008.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level (dB or dBm) Property

**Short Name:**IQ Power Edge Level

Property of [RFmxBT](crfmxbt.html)

Specifies the power level at which the device triggers. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope.

This value is expressed in dB when you set the [IQ Power Edge Level Type](attrb00fff.html) property to **Relative** and in dBm when you set the IQ Power Edge Level Type property to **Absolute**. This property is valid only when you set the [Trigger Type](attrb00004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00009.html language=enus -->
## TOPIC 00010: Trigger:IQ Power Edge:Slope Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00009.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Slope Property

**Short Name:**IQ Power Edge Slope

Property of [RFmxBT](crfmxbt.html)

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the [Trigger Type](attrb00004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| --- | --- |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0000a.html language=enus -->
## TOPIC 00011: Trigger:Delay (s) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0000a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxBT](crfmxbt.html)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires posttrigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0000b.html language=enus -->
## TOPIC 00012: Trigger:Minimum Quiet Time:Mode Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0000b.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Mode Property

**Short Name:**Trigger Min Quiet Time Mode

Property of [RFmxBT](crfmxbt.html)

Specifies whether the measurement computes the minimum quiet time used for triggering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Manual (0) | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0000c.html language=enus -->
## TOPIC 00013: Trigger:Minimum Quiet Time:Duration (s) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0000c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Duration (s) Property

**Short Name:**Trigger Min Quiet Time (s)

Property of [RFmxBT](crfmxbt.html)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

If you set the [IQ Power Edge Slope](attrb00009.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0000d.html language=enus -->
## TOPIC 00014: Packet:Type Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0000d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Type Property

**Short Name:**Packet Type

Property of [RFmxBT](crfmxbt.html)

Specifies the type of the Bluetooth packet to be measured.

In this document, packet type is sometimes referred to by the Bluetooth physical layer (PHY) it belongs to. Supported Bluetooth physical layers are basic rate (BR), enhanced data rate (EDR), low energy (LE) and low energy - channel sounding (LE-CS).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **DH1**.

| DH1 (0) | Specifies that the packet type is DH1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.2, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| --- | --- |
| DH3 (1) | Specifies that the packet type is DH3. The packet belongs to BR PHY. Refer to section 6.5.4.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DH5 (2) | Specifies that the packet type is DH5. The packet belongs to BR PHY. Refer to section 6.5.4.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM1 (3) | Specifies that the packet type is DM1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.1, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM3 (4) | Specifies that the packet type is DM3. The packet belongs to BR PHY. Refer to section 6.5.4.3, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM5 (5) | Specifies that the packet type is DM5. The packet belongs to BR PHY. Refer to section 6.5.4.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH1 (6) | Specifies that the packet type is 2-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.8, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH3 (7) | Specifies that the packet type is 2-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.9, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH5 (8) | Specifies that the packet type is 2-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.10, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH1 (9) | Specifies that the packet type is 3-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.11, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH3 (10) | Specifies that the packet type is 3-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.12, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH5 (11) | Specifies that the packet type is 3-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.13, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-EV3 (12) | Specifies that the packet type is 2-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-EV5 (13) | Specifies that the packet type is 2-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-EV3 (14) | Specifies that the packet type is 3-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-EV5 (15) | Specifies that the packet type is 3-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.7, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| LE (16) | Specifies that the packet type is LE. The packet belongs to LE PHY. Refer to sections 2.1 and 2.2, Part B, Volume 6 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| LE-CS (17) | Specifies that the packet type is LE-CS. The packet belongs to LE-CS PHY. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0000e.html language=enus -->
## TOPIC 00015: Packet:Data Rate (bps) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0000e.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Data Rate (bps) Property

**Short Name:**Data Rate (bps)

Property of [RFmxBT](crfmxbt.html)

Specifies the data rate of the LE or LE-CS packet transmitted by the device under test (DUT). This value is expressed in bps. This property is applicable only to LE or LE-CS packet type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **1M**.

| 125K (125000) | The date rate is 125 Kbps. |
| --- | --- |
| 500K (500000) | The date rate is 500 Kbps. |
| 1M (1000000) | The date rate is 1 Mbps. |
| 2M (2000000) | The date rate is 2 Mbps. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0000f.html language=enus -->
## TOPIC 00016: Packet:BD Address:LAP Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0000f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0000f.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:BD Address:LAP Property

**Short Name:**BD Address LAP

Property of [RFmxBT](crfmxbt.html)

Specifies the 24-bit lower address part (LAP) of the bluetooth device address (BD_ADDR).

This value is used to generate the sync word if you set the burst synchronization type property in TXP, ACP, or ModAcc measurements to **Sync Word**. This property is applicable only to BR and EDR packet types.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00011.html language=enus -->
## TOPIC 00017: Packet:Access Address Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00011.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Access Address Property

**Short Name:**Access Address

Property of [RFmxBT](crfmxbt.html)

Specifies the 32-bit LE access address.

This value is used to synchronize to the start of the packet if you set the burst synchronization type property in TXP, ACP, or ModAcc measurements to **Sync Word** and the
 [Packet Type](attrb0000d.html) property to **LE** or **LE-CS**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0x71764129 as specified by the bluetooth standard.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00012.html language=enus -->
## TOPIC 00018: Packet:Payload Bit Pattern Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00012.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Payload Bit Pattern Property

**Short Name:**Payload Bit Pattern

Property of [RFmxBT](crfmxbt.html)

Specifies the bit pattern present in the payload of the packet. This value is used to determine the set of ModAcc measurements to be performed.

The following table shows the measurements applicable for different Payload Bit Pattern:

| Bluetooth PHY | Data Rate | Standard | 11110000 | 10101010 |
| --- | --- | --- | --- | --- |
| BR | NA | Error | df1 | df2 and BR frequency error |
| EDR | NA | DEVM (The measurement considers PN9 as payload pattern) | Error | Error |
| LE | 1 Mbps | Error | df1 and LE frequency errors on the constant tone extension (CTE) field within the direction finding packets. | df2 and LE frequency error |
| LE | 2 Mbps | Error | df1 and LE frequency errors on the constant tone extension (CTE) field within the direction finding packets. | df2 and LE frequency error |
| LE | 125 kbps | df1 and LE frequency error (The measurement considers 11111111 as payload pattern) | Error | Error |
| LE | 500 kbps | df2 and LE frequency error (The measurement considers 11111111 as payload pattern) | Error | Error |
| LE-CS | 1 Mbps | Error | df1 | df2 and LE frequency error |
| LE-CS | 2 Mbps | Error | df1 | df2 and LE frequency error |

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Standard Defined**.

| Standard Defined (0) | Specifies that the payload bit pattern is Standard Defined. |
| --- | --- |
| 11110000 (1) | Specifies that the payload bit pattern is 11110000. |
| 10101010 (2) | Specifies that the payload bit pattern is 10101010. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00013.html language=enus -->
## TOPIC 00019: Packet:Payload Length Mode Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00013.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Payload Length Mode Property

**Short Name:**Payload Length Mode

Property of [RFmxBT](crfmxbt.html)

Specifies the payload length mode of the signal to be measured. The payload length mode and [Payload Length](attrb00014.html) properties decide the length of the payload to be used for measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Manual (0) | Enables the value specified by the Payload Length property. The acquisition and measurement durations will be decided based on this value. |
| --- | --- |
| Auto (1) | Enables the standard defined maximum payload length for the selected packet type. If this property is set to Auto, the maximum standard defined payload length for the selected Packet Type is chosen. For LE, the maximum payload length that a device under test(DUT) can generate varies from 37 to 255 bytes. When you set the payload length mode for the LE packet type to Auto, RFmx chooses 37 bytes as the payload length. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00014.html language=enus -->
## TOPIC 00020: Packet:Payload Length (bytes) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00014.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Payload Length (bytes) Property

**Short Name:**Payload Length (bytes)

Property of [RFmxBT](crfmxbt.html)

Specifies the payload length of the signal in bytes. This property is applicable only when you set the [Payload Length Mode](attrb00013.html) property to **Manual**. This property returns the payload length used for measurement if you set the Payload Length Mode property to **Auto**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00017.html language=enus -->
## TOPIC 00021: Channel Number Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00017.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Channel Number Property

**Short Name:**Channel Number

Property of [RFmxBT](crfmxbt.html)

Specifies the RF channel number of the signal generated by the device under test (DUT), as defined in the bluetooth specification. This property is applicable when you enable the ACP measurement and when you set the [ACP Offset Channel Mode](attrb05002.html) property to **In-band**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00019.html language=enus -->
## TOPIC 00022: Auto Detect Signal:Detected Packet Type Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00019.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Auto Detect Signal:Detected Packet Type Property

**Short Name:**Detected Packet Type

Property of [RFmxBT](crfmxbt.html)

Returns the packet type detected by the RFmxBT Auto Detect Signal VI. This property can be queried only after calling the RFmxBT Auto Detect Signal VI.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Unknown**.

| Unknown (-1) | Specifies that no valid bluetooth packet is detected in the signal to be measured. |
| --- | --- |
| DH1 (0) | Specifies that the detected packet type is DH1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.2, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DH3 (1) | Specifies that the detected packet type is DH3. The packet belongs to BR PHY. Refer to section 6.5.4.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DH5 (2) | Specifies that the detected packet type is DH5. The packet belongs to BR PHY. Refer to section 6.5.4.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM1 (3) | Specifies that the detected packet type is DM1. The packet belongs to BR PHY. Refer to sections 6.5.1.5 and 6.5.4.1, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM3 (4) | Specifies that the detected packet type is DM3. The packet belongs to BR PHY. Refer to section 6.5.4.3, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| DM5 (5) | Specifies that the detected packet type is DM5. The packet belongs to BR PHY. Refer to section 6.5.4.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH1 (6) | Specifies that the detected packet type is 2-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.8, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH3 (7) | Specifies that the detected packet type is 2-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.9, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-DH5 (8) | Specifies that the detected packet type is 2-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.10, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH1 (9) | Specifies that the detected packet type is 3-DH1. The packet belongs to EDR PHY. Refer to section 6.5.4.11, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH3 (10) | Specifies that the detected packet type is 3-DH3. The packet belongs to EDR PHY. Refer to section 6.5.4.12, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-DH5 (11) | Specifies that the detected packet type is 3-DH5. The packet belongs to EDR PHY. Refer to section 6.5.4.13, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-EV3 (12) | Specifies that the detected packet type is 2-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.4, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 2-EV5 (13) | Specifies that the detected packet type is 2-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.5, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-EV3 (14) | Specifies that the detected packet type is 3-EV3. The packet belongs to EDR PHY. Refer to section 6.5.3.6, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| 3-EV5 (15) | Specifies that the detected packet type is 3-EV5. The packet belongs to EDR PHY. Refer to section 6.5.3.7, Part B, Volume 2 of the Bluetooth Core Specification v5.1 for more information about this packet. |
| LE (16) | Specifies that the detected packet belongs to LE PHY. Refer to sections 2.1 and 2.2, Part B, Volume 6 of the Bluetooth Core Specification v5.1 for more information about this packet. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0002a.html language=enus -->
## TOPIC 00023: Auto Detect Signal:Detected Data Rate Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0002a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0002a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Auto Detect Signal:Detected Data Rate Property

**Short Name:**Detected Data Rate

Property of [RFmxBT](crfmxbt.html)

Returns the data rate detected by the RFmxBT Auto Detect Signal VI. This property returns a valid data rate only if the Detected Packet Type property returns LE. This property can be queried only after calling the RFmxBT Auto Detect Signal VI.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Not Applicable**.

| Not Applicable (-1) | Specifies that the Data Rate property is not applicable for the packet type detected. |
| --- | --- |
| 125K (125000) | Specifies that the detected data rate of the LE packet is 125 Kbps. |
| 500K (500000) | Specifies that the detected data rate of the LE packet is 500 Kbps. |
| 1M (1000000) | Specifies that the detected data rate of the LE packet is 1 Mbps. |
| 2M (2000000) | Specifies that the detected data rate of the LE packet is 2 Mbps. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0002c.html language=enus -->
## TOPIC 00024: Packet:Direction Finding:Mode Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0002c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0002c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Direction Finding:Mode Property

**Short Name:**Direction Finding Mode

Property of [RFmxBT](crfmxbt.html)

Specifies the mode of direction finding.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | Specifies that the LE packet does not have fields required for direction finding. |
| --- | --- |
| Angle of Arrival (1) | Specifies that the LE packets uses the Angle of Arrival method of direction finding. |
| Angle of Departure (2) | Specifies that the LE packets uses the Angle of Departure method of direction finding. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0002d.html language=enus -->
## TOPIC 00025: Packet:Direction Finding:CTE Length (s) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0002d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0002d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Direction Finding:CTE Length (s) Property

**Short Name:**CTE Length (s)

Property of [RFmxBT](crfmxbt.html)

Specifies the length of the constant tone extension (CTE) field in the generated signal. This value is expressed in seconds. This property is applicable only when you set the [Direction Finding Mode](attrb0002c.html) property to either **Angle of Arrival** or **Angle of Departure**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 160 microseconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00032.html language=enus -->
## TOPIC 00026: Packet:Channel Sounding:Phase Measurement Period Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00032.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Channel Sounding:Phase Measurement Period Property

**Short Name:**CS Phase Measurement Period

Property of [RFmxBT](crfmxbt.html)

Specifies the Channel Sounding Phase Measurement Period for the LE-CS packet. This property is applicable only when you set the [Packet Type](attrb0000d.html) property to **LE-CS** and the [CS Packet Format](attrb00030.html) property to any value other than **SYNC**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **10 us**.

| 10 us (0.00001) | Specifies that the phase measurement period is 10 us for the LE-CS packet. |
| --- | --- |
| 20 us (0.00002) | Specifies that the phase measurement period is 20 us for the LE-CS packet. |
| 40 us (0.00004) | Specifies that the phase measurement period is 40 us for the LE-CS packet. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00034.html language=enus -->
## TOPIC 00027: Packet:Bandwidth Bit Period Product Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00034.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Packet:Bandwidth Bit Period Product Property

**Short Name:**Bandwidth Bit Period Product

Property of [RFmxBT](crfmxbt.html)

Specifies the bandwidth bit period product of GFSK modulation for LE-CS packet type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.5.

| 0.5 (0.5) | Specifies that the bandwidth bit period product is 0.5. |
| --- | --- |
| 2 (2.0) | Specifies that the bandwidth bit period product is 2. This value can be used only for data rate 2 Mbps. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00ffc.html language=enus -->
## TOPIC 00028: Reference Level Headroom Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00ffc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00ffc.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Headroom Property

**Short Name:**Reference Level Headroom

Property of [RFmxBT](crfmxbt.html)

Specifies the margin RFmx adds to the [Reference Level](attrb00002.html) property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.

RFmx configures the input gain to avoid clipping and associated overflow warnings provided the instantaneous power of the input signal remains within the Reference Level plus the Reference Level Headroom. If you know the input power of the signal precisely or previously included the margin in the Reference Level, you could improve the signal-to-noise ratio by reducing the Reference Level Headroom.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb00ffd.html language=enus -->
## TOPIC 00029: Selected Ports Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb00ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb00ffd.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxBT](crfmxbt.html)

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr Get Available Ports](/csh?topicname=rfmxinstrvi/rfmxinstr_get_available_ports.html) VI to get the valid port names.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01000.html language=enus -->
## TOPIC 00030: TXP:Measurement Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01000.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Measurement Enabled Property

**Short Name:**TXP Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable the transmit power (TxP) measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01002.html language=enus -->
## TOPIC 00031: TXP:Averaging:Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01002.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Averaging:Enabled Property

**Short Name:**TXP Averaging Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable averaging for the transmit power (TxP) measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the TXP Averaging Count property as the number of acquisitions over which the TXP measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01003.html language=enus -->
## TOPIC 00032: TXP:Averaging:Count Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01003.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Averaging:Count Property

**Short Name:**TXP Averaging Count

Property of [RFmxBT](crfmxbt.html)

Specifies the number of acquisitions used for averaging when you set the [TXP Averaging Enabled](attrb01002.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01004.html language=enus -->
## TOPIC 00033: TXP:All Traces Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01004.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:All Traces Enabled Property

**Short Name:**TXP All Traces Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable all the traces used for transmit power (TxP) measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01005.html language=enus -->
## TOPIC 00034: TXP:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Number of Analysis Threads Property

**Short Name:**TXP Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

Specifies the maximum number of threads used for parallelism for TXP measurement.

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01007.html language=enus -->
## TOPIC 00035: TXP:Results:Average Power Mean (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01007.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:Average Power Mean (dBm) Property

**Short Name:**TXP Results Avg Pwr Mean (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power computed over the measurement interval. When you set the [Direction Finding Mode](attrb01002.html) property to **Angle of Departure** for LE packets, it will exclude guard period and all the switching slots for the average power computation. This value is expressed in dBm. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the average power results computed for each averaging count.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01008.html language=enus -->
## TOPIC 00036: TXP:Results:Average Power Maximum (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01008.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:Average Power Maximum (dBm) Property

**Short Name:**TXP Results Avg Pwr Max (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power computed over the measurement interval. When you set the [Direction Finding Mode](attrb01002.html) property to **Angle of Departure** for LE packets, it will exclude guard period and all the switching slots for the average power computation. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the maximum of the average power results computed for each averaging count. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0100a.html language=enus -->
## TOPIC 00037: TXP:Results:Peak Power Maximum (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0100a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:Peak Power Maximum (dBm) Property

**Short Name:**TXP Results Pk Pwr Max (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the peak power computed over the measurement interval. When you set the [Direction Finding Mode](attrb01002.html) property to **Angle of Departure** for LE packets, it will exclude guard period and all the switching slots for the peak power computation. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the maximum of the peak power results computed for each averaging count. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0100b.html language=enus -->
## TOPIC 00038: TXP:Results:Peak to Average Power Ratio Maximum (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0100b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0100b.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:Peak to Average Power Ratio Maximum (dB) Property

**Short Name:**TXP Results Pk to Avg Pwr Ratio Max (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the peak to average power ratio computed over the measurement interval. When you set the [Direction Finding Mode](attrb01002.html) property to **Angle of Departure** for LE packets, it will exclude guard period and all the switching slots for the peak to average power ratio computation. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the maximum of the peak to average power ratio results computed for each averaging count. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0100c.html language=enus -->
## TOPIC 00039: TXP:Results:EDR GFSK Average Power Mean (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0100c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0100c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:EDR GFSK Average Power Mean (dBm) Property

**Short Name:**TXP Results EDR GFSK Avg Pwr Mean (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power of the GFSK portion of the EDR packet. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the GFSK average power results computed for each averaging count. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0100d.html language=enus -->
## TOPIC 00040: TXP:Results:EDR DPSK Average Power Mean (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0100d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:EDR DPSK Average Power Mean (dBm) Property

**Short Name:**TXP Results EDR DPSK Avg Pwr Mean (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power of the DPSK portion of the EDR packet. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the DPSK average power results computed for each averaging count. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01010.html language=enus -->
## TOPIC 00041: TXP:Burst Synchronization Type Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01010.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Burst Synchronization Type Property

**Short Name:**TXP Burst Sync Type

Property of [RFmxBT](crfmxbt.html)

Specifies the type of synchronization used for detecting the start of packet in the transmit power (TXP) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Preamble**.

| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| --- | --- |
| Preamble (1) | Specifies that the measurement uses the preamble field to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01013.html language=enus -->
## TOPIC 00042: TXP:Results:EDR DPSK GFSK Average Power Ratio Mean (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01013.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:EDR DPSK GFSK Average Power Ratio Mean (dB) Property

**Short Name:**TXP Results EDR DPSK GFSK Avg Pwr Ratio Mean (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the ratio of the average power of the DPSK portion to the average power of the GFSK portion of the EDR packet. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the DPSK GFSK average power ratio results computed for each averaging count. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01014.html language=enus -->
## TOPIC 00043: TXP:Results:LE CTE Reference Period Average Power Mean (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01014.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:LE CTE Reference Period Average Power Mean (dBm) Property

**Short Name:**TXP Results LE CTE Ref Period Avg Pwr Mean (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power computed over the reference period in the CTE portion of the LE packet. This result is applicable only when you set the [Direction Finding Mode](attrb0002c.html) property to **Angle of Departure**. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the CTE reference period average power results computed for each averaging count. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01015.html language=enus -->
## TOPIC 00044: TXP:Results:LE CTE Reference Period Peak Absolute Power Deviation Maximum (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01015.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:LE CTE Reference Period Peak Absolute Power Deviation Maximum (%) Property

**Short Name:**TXP Results LE CTE Ref Period Pk Abs Pwr Deviation Max (%)

Property of [RFmxBT](crfmxbt.html)

Returns the peak absolute power deviation computed over the reference period in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power with respect to the average power in the reference period. This result is applicable only when you set the [Direction Finding Mode](attrb0002c.html) property to **Angle of Departure**. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the maximum of the CTE reference period absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01016.html language=enus -->
## TOPIC 00045: TXP:Results:LE CTE Transmit Slot Average Power Mean (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01016.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:LE CTE Transmit Slot Average Power Mean (dBm) Property

**Short Name:**TXP Results LE CTE Tx Slot Avg Pwr Mean (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power computed over each transmit slot in CTE portion of the LE packet. This result is applicable only when you set the [Direction Finding Mode](attrb0002c.html) property to **Angle of Departure**. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the CTE transmit slot average power results computed for each averaging count. This value is expressed in dBm.

Use "slot<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01017.html language=enus -->
## TOPIC 00046: TXP:Results:LE CTE Transmit Slot Peak Absolute Power Deviation Maximum (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01017.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:LE CTE Transmit Slot Peak Absolute Power Deviation Maximum (%) Property

**Short Name:**TXP Results LE CTE Tx Slot Pk Abs Pwr Deviation Max (%)

Property of [RFmxBT](crfmxbt.html)

Returns the peak absolute power deviation computed over each transmit slot in the CTE portion of the LE packet. The peak absolute power deviation is the deviation of peak power in each transmit slot with respect to the average power in that transmit slot. This result is applicable only when you set the [Direction Finding Mode](attrb0002c.html) property to **Angle of Departure**. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the maximum of the CTE transmit slot absolute power deviation results computed for each averaging count. This value is expressed as a percentage.

Use "slot<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb01018.html language=enus -->
## TOPIC 00047: TXP:Results:LE CS Phase Measurement Period Average Power Mean (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb01018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb01018.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

TXP:Results:LE CS Phase Measurement Period Average Power Mean (dBm) Property

**Short Name:**TXP Results LE CS Phase Meas Period Avg Pwr Mean (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the average power computed over each antenna path during phase measurement period of the LE-CS packet. This result is applicable only when you set the [Packet Type](attrb0000d.html) property to **LE-CS** and the [CS Packet Format](attrb00030.html) property to any value other than **SYNC**. When you set the [TXP Averaging Enabled](attrb01002.html) property to **True**, it returns the mean of the phase measurement period average power results computed for each averaging count. This value is expressed in dBm.

Use "slot<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02000.html language=enus -->
## TOPIC 00048: 20dBBandwidth:Measurement Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02000.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Measurement Enabled Property

**Short Name:**20dBBandwidth Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable the 20dBBandwidth measurement specified in section 4.5.5 of the *Bluetooth Test Specification v5.1.0*. The measurement uses a span of 3 MHz internally. This measurement is valid only for basic rate (BR) packets.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02002.html language=enus -->
## TOPIC 00049: 20dBBandwidth:Averaging:Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02002.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Averaging:Enabled Property

**Short Name:**20dBBandwidth Averaging Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable averaging for the 20dBBandwidth measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The 20dBBandwidth measurement uses the 20dBBandwidth Averaging Count property as the number of acquisitions over which the 20dBBandwidth measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02003.html language=enus -->
## TOPIC 00050: 20dBBandwidth:Averaging:Count Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02003.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Averaging:Count Property

**Short Name:**20dBBandwidth Averaging Count

Property of [RFmxBT](crfmxbt.html)

Specifies the number of acquisitions used for averaging when you set the [20dBBandwidth Averaging Enabled](attrb02002.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02004.html language=enus -->
## TOPIC 00051: 20dBBandwidth:All Traces Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02004.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:All Traces Enabled Property

**Short Name:**20dBBandwidth All Traces Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable all the traces for the 20dBBandwidth measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02005.html language=enus -->
## TOPIC 00052: 20dBBandwidth:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Number of Analysis Threads Property

**Short Name:**20dBBandwidth Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

Specifies the maximum number of threads used for parallelism for the 20dB bandwidth measurement.

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02007.html language=enus -->
## TOPIC 00053: 20dBBandwidth:Results:Peak Power (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02007.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Results:Peak Power (dBm) Property

**Short Name:**20dBBandwidth Results Pk Pwr (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the peak power of the measured spectrum. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02008.html language=enus -->
## TOPIC 00054: 20dBBandwidth:Results:Bandwidth (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02008.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Results:Bandwidth (Hz) Property

**Short Name:**20dBBandwidth Results Bandwidth (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the 20dB bandwidth of the received signal. It is computed as the difference between 20dBBandwidth Results High Freq and 20dBBandwidth Results Low Freq. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb02009.html language=enus -->
## TOPIC 00055: 20dBBandwidth:Results:High Frequency (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb02009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb02009.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Results:High Frequency (Hz) Property

**Short Name:**20dBBandwidth Results High Freq (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the highest frequency above the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0200a.html language=enus -->
## TOPIC 00056: 20dBBandwidth:Results:Low Frequency (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0200a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0200a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

20dBBandwidth:Results:Low Frequency (Hz) Property

**Short Name:**20dBBandwidth Results Low Freq (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the lowest frequency below the center frequency at which the transmit power drops 20 dB below the peak power. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03000.html language=enus -->
## TOPIC 00057: FrequencyRange:Measurement Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03000.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Measurement Enabled Property

**Short Name:**FrequencyRange Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable the FrequencyRange measurement specified in the section 4.5.4 of the *Bluetooth Test Specification v5.1.0*. This measurement is valid only for basic rate (BR) packets.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03002.html language=enus -->
## TOPIC 00058: FrequencyRange:Span (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03002.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Span (Hz) Property

**Short Name:**FrequencyRange Span (Hz)

Property of [RFmxBT](crfmxbt.html)

Specifies the span for the FrequencyRange measurement. This value is expressed in Hz. You must adjust the span according the center frequency as specified in section 4.5.4 of the *Bluetooth Test Specification v5.1.0*. It is recommended to use the span of 6 MHz for a center frequency of 2.402 GHz and 10 MHz for a center frequency of 2.48 GHz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03003.html language=enus -->
## TOPIC 00059: FrequencyRange:Averaging:Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03003.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Averaging:Enabled Property

**Short Name:**FrequencyRange Averaging Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable averaging for the FrequencyRange measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The FrequencyRange measurement uses the FrequencyRange Averaging Count property as the number of acquisitions over which the FrequencyRange measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03004.html language=enus -->
## TOPIC 00060: FrequencyRange:Averaging:Count Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03004.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Averaging:Count Property

**Short Name:**FrequencyRange Averaging Count

Property of [RFmxBT](crfmxbt.html)

Specifies the number of acquisitions used for averaging when you set the [FrequencyRange Averaging Enabled](attrb03003.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03005.html language=enus -->
## TOPIC 00061: FrequencyRange:All Traces Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:All Traces Enabled Property

**Short Name:**FrequencyRange All Traces Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable all the traces for FrequencyRange measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03006.html language=enus -->
## TOPIC 00062: FrequencyRange:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03006.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Number of Analysis Threads Property

**Short Name:**FrequencyRange Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

Specifies the maximum number of threads used for parallelism for the frequency range measurement.

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03008.html language=enus -->
## TOPIC 00063: FrequencyRange:Results:High Frequency (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03008.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Results:High Frequency (Hz) Property

**Short Name:**FrequencyRange Results High Freq (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the highest frequency above the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb03009.html language=enus -->
## TOPIC 00064: FrequencyRange:Results:Low Frequency (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb03009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb03009.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

FrequencyRange:Results:Low Frequency (Hz) Property

**Short Name:**FrequencyRange Results Low Freq (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the lowest frequency below the center frequency at which the transmit power drops below -30 dBm measured in a 100 kHz bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04000.html language=enus -->
## TOPIC 00065: ModAcc:Measurement Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04000.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Enabled Property

**Short Name:**ModAcc Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable the ModAcc measurements. You can use this property to determine the modulation quality of the bluetooth transmitter.

You can perform the following sub-measurements when ModAcc measurement is enabled:

- DEVM, on EDR packets
- df1, on BR and LE packets
- df2, on BR and LE packets
- Frequency Error, on BR, EDR, LE and LE-CS packets

The listed sub-measurements are enabled or disabled based on the value of the [Payload Bit Pattern](attrb00012.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the
 [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04003.html language=enus -->
## TOPIC 00066: ModAcc:EDR:I/Q Origin Offset Correction Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04003.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:EDR:I/Q Origin Offset Correction Enabled Property

**Short Name:**ModAcc I/Q Origin Offset Correction Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable the I/Q origin offset correction for EDR packets. If you set this property to **True**, the DEVM results are computed after correcting for the I/Q origin offset.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables the I/Q origin offset correction for EDR packets. |
| --- | --- |
| True (1) | Enables the I/Q origin offset correction for EDR packets. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04004.html language=enus -->
## TOPIC 00067: ModAcc:Averaging:Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04004.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Averaging:Enabled Property

**Short Name:**ModAcc Averaging Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable averaging for the ModAcc measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the ModAcc Averaging Count property as the number of acquisitions over which the ModAcc measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04005.html language=enus -->
## TOPIC 00068: ModAcc:Averaging:Count Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Averaging:Count Property

**Short Name:**ModAcc Averaging Count

Property of [RFmxBT](crfmxbt.html)

Specifies the number of acquisitions used for averaging when you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04006.html language=enus -->
## TOPIC 00069: ModAcc:All Traces Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04006.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:All Traces Enabled Property

**Short Name:**ModAcc All Traces Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable all the traces computed by ModAcc measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04007.html language=enus -->
## TOPIC 00070: ModAcc:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04007.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Number of Analysis Threads Property

**Short Name:**ModAcc Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04009.html language=enus -->
## TOPIC 00071: ModAcc:Results:df1:df1avg Mean (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04009.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df1:df1avg Mean (Hz) Property

**Short Name:**ModAcc Results df1avg Mean (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the df1avg value computed on the signal. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the df1avg results computed for each averaging count. This value is expressed in Hz

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0400a.html language=enus -->
## TOPIC 00072: ModAcc:Results:df1:df1avg Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0400a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0400a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df1:df1avg Maximum (Hz) Property

**Short Name:**ModAcc Results df1avg Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the df1avg value computed on the signal. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the df1avg results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0400b.html language=enus -->
## TOPIC 00073: ModAcc:Results:df1:df1avg Minimum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0400b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0400b.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df1:df1avg Minimum (Hz) Property

**Short Name:**ModAcc Results df1avg Min (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the df1avg value computed on the signal. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the minimum of the df1avg results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0400c.html language=enus -->
## TOPIC 00074: ModAcc:Results:df1:Peak df1max Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0400c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0400c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df1:Peak df1max Maximum (Hz) Property

**Short Name:**ModAcc Results Pk df1max Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the peak value. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the peak df1max results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0400d.html language=enus -->
## TOPIC 00075: ModAcc:Results:df1:Minimum df1max Minimum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0400d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0400d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df1:Minimum df1max Minimum (Hz) Property

**Short Name:**ModAcc Results Min df1max Min (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the minimum df1max value computed on the signal. The measurement computes df1max deviation values on a packet and reports the minimum value. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the minimum of the Min df1max results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0400e.html language=enus -->
## TOPIC 00076: ModAcc:Results:df2:df2avg Mean (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0400e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0400e.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df2:df2avg Mean (Hz) Property

**Short Name:**ModAcc Results df2avg Mean (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the df2avg value computed on the signal. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the df2avg results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0400f.html language=enus -->
## TOPIC 00077: ModAcc:Results:df2:df2avg Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0400f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0400f.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df2:df2avg Maximum (Hz) Property

**Short Name:**ModAcc Results df2avg Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the df2avg value computed on the signal. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the df2avg results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04010.html language=enus -->
## TOPIC 00078: ModAcc:Results:df2:df2avg Minimum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04010.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df2:df2avg Minimum (Hz) Property

**Short Name:**ModAcc Results df2avg Min (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the df2avg value computed on the signal. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the minimum of the df2avg results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04011.html language=enus -->
## TOPIC 00079: ModAcc:Results:df2:Peak df2max Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04011.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df2:Peak df2max Maximum (Hz) Property

**Short Name:**ModAcc Results Pk df2max Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the peak value. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the peak df2max results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04012.html language=enus -->
## TOPIC 00080: ModAcc:Results:df2:Minimum df2max Minimum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04012.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df2:Minimum df2max Minimum (Hz) Property

**Short Name:**ModAcc Results Min df2max Min (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the minimum df2max value computed on the signal. The measurement computes df2max deviation values on a packet and reports the minimum value. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the minimum of the Min df2max results computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04013.html language=enus -->
## TOPIC 00081: ModAcc:Results:df2:Percentage of Symbols above df2max Threshold (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04013.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df2:Percentage of Symbols above df2max Threshold (%) Property

**Short Name:**ModAcc Results Percentage of Symbols above df2max Threshold (%)

Property of [RFmxBT](crfmxbt.html)

Returns the percentage of symbols with df2max values that are greater than the df2max threshold defined by the standard. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it computes this result using the df2max values from all averaging counts. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04014.html language=enus -->
## TOPIC 00082: ModAcc:Results:Frequency Error:BR:Initial Frequency Error Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04014.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:BR:Initial Frequency Error Maximum (Hz) Property

**Short Name:**ModAcc Results BR Initial Freq Error Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the initial frequency error value computed on the preamble portion of the BR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04015.html language=enus -->
## TOPIC 00083: ModAcc:Results:Frequency Error:BR:Peak Frequency Drift Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04015.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:BR:Peak Frequency Drift Maximum (Hz) Property

**Short Name:**ModAcc Results BR Pk Freq Drift Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak frequency drift value computed on the BR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04016.html language=enus -->
## TOPIC 00084: ModAcc:Results:Frequency Error:BR:Peak Frequency Drift Rate Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04016.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:BR:Peak Frequency Drift Rate Maximum (Hz) Property

**Short Name:**ModAcc Results BR Pk Freq Drift Rate Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak frequency drift rate value computed on the BR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04017.html language=enus -->
## TOPIC 00085: ModAcc:Results:Frequency Error:EDR:Header Frequency Error wi Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04017.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:EDR:Header Frequency Error wi Maximum (Hz) Property

**Short Name:**ModAcc Results EDR Header Freq Error wi Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the frequency error value computed on the header of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute header frequency error values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04018.html language=enus -->
## TOPIC 00086: ModAcc:Results:Frequency Error:EDR:Peak Frequency Error wi+w0 Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04018.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:EDR:Peak Frequency Error wi+w0 Maximum (Hz) Property

**Short Name:**ModAcc Results EDR Pk Freq Error wi+w0 Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak frequency error value computed on the EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute peak frequency error values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04019.html language=enus -->
## TOPIC 00087: ModAcc:Results:Frequency Error:EDR:Peak Frequency Error w0 Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04019.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:EDR:Peak Frequency Error w0 Maximum (Hz) Property

**Short Name:**ModAcc Results EDR Pk Freq Error w0 Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak frequency error value computed on the EDR portion of the EDR packet, relative to the header frequency error. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum absolute of the peak frequency error values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0401a.html language=enus -->
## TOPIC 00088: ModAcc:Results:Frequency Error:LE:Peak Frequency Error Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0401a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0401a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:LE:Peak Frequency Error Maximum (Hz) Property

**Short Name:**ModAcc Results LE Pk Freq Error Max (Hz)

Property of [RFmxBT](crfmxbt.html)

When you set the [Direction Finding Mode](attrb0002c.html) property to **Disabled**, it returns the peak frequency error value computed on the preamble and payload portion of the LE or LE-CS packet. When you set the Direction Finding Mode property to **Angle of Arrival**, it returns the peak frequency error value computed on the Constant tone extension field of the LE packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of absolute the peak frequency error values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0401b.html language=enus -->
## TOPIC 00089: ModAcc:Results:Frequency Error:LE:Initial Frequency Drift Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0401b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0401b.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:LE:Initial Frequency Drift Maximum (Hz) Property

**Short Name:**ModAcc Results LE Initial Freq Drift Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the initial frequency drift value computed on the LE packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute initial frequency drift values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0401c.html language=enus -->
## TOPIC 00090: ModAcc:Results:Frequency Error:LE:Peak Frequency Drift Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0401c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0401c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:LE:Peak Frequency Drift Maximum (Hz) Property

**Short Name:**ModAcc Results LE Pk Freq Drift Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak frequency drift value computed on the LE packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute peak frequency drift values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0401d.html language=enus -->
## TOPIC 00091: ModAcc:Results:Frequency Error:LE:Peak Frequency Drift Rate Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0401d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0401d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:LE:Peak Frequency Drift Rate Maximum (Hz) Property

**Short Name:**ModAcc Results LE Pk Freq Drift Rate Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the peak frequency drift rate value computed on the LE packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the value corresponding to the maximum of the absolute peak frequency drift rate values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0401e.html language=enus -->
## TOPIC 00092: ModAcc:Results:DEVM:Peak RMS DEVM Maximum (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0401e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0401e.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Peak RMS DEVM Maximum (%) Property

**Short Name:**ModAcc Results Pk RMS DEVM Max (%)

Property of [RFmxBT](crfmxbt.html)

Returns the peak of the RMS differential EVM (DEVM) values computed on each 50us block of the EDR portion of the EDR packet. When you set [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the peak RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the EDR Differential EVM concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0401f.html language=enus -->
## TOPIC 00093: ModAcc:Results:DEVM:RMS DEVM Mean (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0401f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0401f.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:RMS DEVM Mean (%) Property

**Short Name:**ModAcc Results RMS DEVM Mean (%)

Property of [RFmxBT](crfmxbt.html)

Returns the RMS differential EVM (DEVM) value computed on the EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the RMS differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the EDR Differential EVM concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04020.html language=enus -->
## TOPIC 00094: ModAcc:Results:DEVM:Peak DEVM Maximum (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04020.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Peak DEVM Maximum (%) Property

**Short Name:**ModAcc Results Pk DEVM Max (%)

Property of [RFmxBT](crfmxbt.html)

Returns the peak of the differential EVM (DEVM) values computed on symbols in the EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the peak symbol differential EVM (DEVM) values computed for each averaging count. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04021.html language=enus -->
## TOPIC 00095: ModAcc:Results:DEVM:99% DEVM (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04021.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:99% DEVM (%) Property

**Short Name:**ModAcc Results 99% DEVM (%)

Property of [RFmxBT](crfmxbt.html)

Returns the 99th percentile of the differential EVM (DEVM) values computed on symbols of the EDR portion of all measured EDR packets. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04022.html language=enus -->
## TOPIC 00096: ModAcc:Results:DEVM:Percentage of Symbols below 99% DEVM Limit (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04022.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Percentage of Symbols below 99% DEVM Limit (%) Property

**Short Name:**ModAcc Results Percentage of Symbols below 99% DEVM Limit (%)

Property of [RFmxBT](crfmxbt.html)

Returns the percentage of symbols in the EDR portion of all the measured EDR packets with differential EVM (DEVM) less than or equal to 99% DEVM threshold as defined in section 4.5.11 of the *Bluetooth Test Specification v5.1.0.*. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it computes this result using the symbol DEVM values from all averaging counts. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04023.html language=enus -->
## TOPIC 00097: ModAcc:Results:I/Q Origin Offset Mean (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04023.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:I/Q Origin Offset Mean (dB) Property

**Short Name:**ModAcc Results I/Q Origin Offset Mean (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the I/Q origin offset estimated over the EDR portion of the EDR packets. This value is expressed in dB. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the I/Q origin offset values computed for each averaging count.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0402b.html language=enus -->
## TOPIC 00098: ModAcc:Burst Synchronization Type Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0402b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0402b.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Burst Synchronization Type Property

**Short Name:**ModAcc Burst Sync Type

Property of [RFmxBT](crfmxbt.html)

Specifies the type of synchronization used for detecting the start of packet in ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Preamble**.

| None (0) | Specifies that the measurement does not perform synchronization to detect the start of the packet. |
| --- | --- |
| Preamble (1) | Specifies that the measurement uses the preamble field to detect the start of the packet. |
| Sync Word (2) | Specifies that the measurement uses sync word for the BR/EDR packets and access address for the LE/LE-CS packets to detect the start of the packet. For BR /EDR packets, the sync word is derived from the BD Address LAP property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0402c.html language=enus -->
## TOPIC 00099: ModAcc:Results:df1:Percentage of Symbols above df1max Threshold (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0402c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0402c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:df1:Percentage of Symbols above df1max Threshold (%) Property

**Short Name:**ModAcc Results Percentage of Symbols above df1max Threshold (%)

Property of [RFmxBT](crfmxbt.html)

Returns the percentage of symbols with df1max values that are greater than the df1max threshold defined by the standard. This result is valid only for the LE packet with a data rate of 125 Kbps. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it computes this result using the df1max values from all averaging counts. This value expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [df1 and df2](/csh?topicname=rfmxbt/df1_and_df2.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0402d.html language=enus -->
## TOPIC 00100: ModAcc:Results:DEVM:Magnitude Error:Average RMS Magnitude Error Mean (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0402d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0402d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Magnitude Error:Average RMS Magnitude Error Mean (%) Property

**Short Name:**ModAcc Results Avg RMS Magnitude Error Mean (%)

Property of [RFmxBT](crfmxbt.html)

Returns the average of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the average RMS magnitude error values computed for each averaging count. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0402e.html language=enus -->
## TOPIC 00101: ModAcc:Results:DEVM:Magnitude Error:Peak RMS Magnitude Error Maximum (%) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0402e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0402e.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Magnitude Error:Peak RMS Magnitude Error Maximum (%) Property

**Short Name:**ModAcc Results Pk RMS Magnitude Error Max (%)

Property of [RFmxBT](crfmxbt.html)

Returns the peak of the RMS magnitude error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the peak RMS Magnitude error values computed for each averaging count. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0402f.html language=enus -->
## TOPIC 00102: ModAcc:Results:DEVM:Phase Error:Average RMS Phase Error Mean (deg) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0402f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0402f.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Phase Error:Average RMS Phase Error Mean (deg) Property

**Short Name:**ModAcc Results Avg RMS Phase Error Mean (deg)

Property of [RFmxBT](crfmxbt.html)

Return the average of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the average RMS phase error values computed for each averaging count. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04030.html language=enus -->
## TOPIC 00103: ModAcc:Results:DEVM:Phase Error:Peak RMS Phase Error Maximum (deg) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04030.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:DEVM:Phase Error:Peak RMS Phase Error Maximum (deg) Property

**Short Name:**ModAcc Results Pk RMS Phase Error Max (deg)

Property of [RFmxBT](crfmxbt.html)

Return the peak of the RMS phase error values computed on each 50 us block of EDR portion of the EDR packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the maximum of the peak RMS phase error values computed for each averaging count. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04031.html language=enus -->
## TOPIC 00104: ModAcc:Results:Frequency Error:LE:Initial Frequency Error Maximum (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04031.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Frequency Error:LE:Initial Frequency Error Maximum (Hz) Property

**Short Name:**ModAcc Results LE Initial Freq Error Max (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the initial frequency error value computed on the preamble portion of the LE or LE-CS packet. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns a value corresponding to the maximum of the absolute initial frequency error values computed for each averaging count. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

Refer to the [Frequency Error Measurement](/csh?topicname=rfmxbt/frequency_error_measurement.html) concept topic for more details.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04032.html language=enus -->
## TOPIC 00105: ModAcc:Results:Clock Drift Mean (ppm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04032.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Clock Drift Mean (ppm) Property

**Short Name:**ModAcc Results Clock Drift Mean (ppm)

Property of [RFmxBT](crfmxbt.html)

Returns the clock drift estimated over the LE-CS packet. This value is expressed in ppm. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the clock drift values computed for each averaging count.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb04033.html language=enus -->
## TOPIC 00106: ModAcc:Results:Preamble Start Time Mean (s) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb04033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb04033.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Preamble Start Time Mean (s) Property

**Short Name:**ModAcc Results Preamble Start Time Mean (s)

Property of [RFmxBT](crfmxbt.html)

Returns the start time of the preamble of LE-CS packet. This value is expressed in seconds. When you set the [ModAcc Averaging Enabled](attrb04004.html) property to **True**, it returns the mean of the preamble start time values computed for each averaging count.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05000.html language=enus -->
## TOPIC 00107: ACP:Measurement Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05000.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Enabled Property

**Short Name:**ACP Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable the ACP measurement.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05002.html language=enus -->
## TOPIC 00108: ACP:Offset Channel Mode Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05002.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset Channel Mode Property

**Short Name:**ACP Offset Channel Mode

Property of [RFmxBT](crfmxbt.html)

Specifies which offset channels are used for the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Symmetric**.

| Symmetric (0) | Specifies that the offset channels are symmetrically located around the reference channel. The number of offsets on either side of the reference channel is specified by the ACP Num Offsets property. In symmetric mode, the Center Frequency property specifies the frequency of the reference channel, expressed in Hz. |
| --- | --- |
| In-band (1) | Specifies that the measurement is performed over all the channels as specified by the standard. For BR and EDR packets, 79 channels starting from 2.402GHz to 2.48GHz are used for the measurement. For LE packets, 81 channels starting from 2.401GHz to 2.481GHz are used for the measurement. In In-band mode, the Center Frequency property specifies the frequency of acquisition which must be equal to 2.441GHz. Configure the Channel Number property to specify the frequency of the reference channel. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05003.html language=enus -->
## TOPIC 00109: ACP:Number of Offsets Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05003.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Number of Offsets Property

**Short Name:**ACP Num Offsets

Property of [RFmxBT](crfmxbt.html)

Specifies the number of offset channels used on either side of the reference channel for the adjacent channel power (ACP) measurement when you set the [ACP Offset Channel Mode](attrb05002.html) property to **Symmetric**. This property also returns the actual number of offsets used in the ACP measurement when you set the ACP Offset Channel Mode property to **In-band**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 5. Valid values are 0 to 100, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05004.html language=enus -->
## TOPIC 00110: ACP:Offset Frequency (Hz) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05004.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset Frequency (Hz) Property

**Short Name:**ACP Offset Freq (Hz)

Property of [RFmxBT](crfmxbt.html)

Returns the frequency of the offset channel with respect to the reference channel frequency. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05005.html language=enus -->
## TOPIC 00111: ACP:Averaging:Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Enabled Property

**Short Name:**ACP Averaging Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable averaging for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05006.html language=enus -->
## TOPIC 00112: ACP:Averaging:Count Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05006.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Count Property

**Short Name:**ACP Averaging Count

Property of [RFmxBT](crfmxbt.html)

Specifies the number of acquisitions used for averaging when you set the [ACP Averaging Enabled](attrb05005.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05007.html language=enus -->
## TOPIC 00113: ACP:All Traces Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05007.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:All Traces Enabled Property

**Short Name:**ACP All Traces Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable all traces for the adjacent channel power (ACP) measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05008.html language=enus -->
## TOPIC 00114: ACP:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05008.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Number of Analysis Threads Property

**Short Name:**ACP Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

Specifies the maximum number of threads used for parallelism for adjacent channel power (ACP) measurement.

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0500a.html language=enus -->
## TOPIC 00115: ACP:Results:Measurement Status Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0500a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0500a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Measurement Status Property

**Short Name:**ACP Results Meas Status

Property of [RFmxBT](crfmxbt.html)

Indicates the overall measurement status based on the measurement limits specified by the standard when you set the [ACP Offset Channel Mode](attrb05002.html) property to **In-band**.

The standard defines two masks, mask with exception and mask without exception. Mask with exception is more stringent than mask without exception.

The mask with exception limits are as follows:

| PHY | Data Rate (bps) | Offset 0 | Offset 1 | Offset 2 | Offset 3 | Offset 4 | Offset (greater than or equal to 5) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| BR | NA | NA | less than or equal to -20 dBm | less than or equal to -40 dBm | less than or equal to -40 dBm | less than or equal to -40 dBm | less than or equal to -40 dBm |
| EDR | NA | less than or equal to (Reference Channel Power (dBm) - 26) | less than or equal to -20 dBm | less than or equal to -40 dBm | less than or equal to -40 dBm | less than or equal to -40 dBm | less than or equal to -40 dBm |
| LE | 1 Mbps | NA | less than or equal to -20 dBm | less than or equal to -30 dBm | less than or equal to -30 dBm | less than or equal to -30 dBm | less than or equal to -30 dBm |
| LE | 2 Mbps | NA | NA | NA | less than or equal to -20 dBm | less than or equal to -20 dBm | less than or equal to -30 dBm |

The mask without exception limits for all packet type are as follows:

| PHY | Data Rate (bps) | Offset (2) to Offset (4) | Offset (greater than or equal to 5) |
| --- | --- | --- | --- |
| BR | NA | less than or equal to -20 dBm | less than or equal to -20 dBm |
| EDR | NA | less than or equal to -20 dBm | less than or equal to -20 dBm |
| LE | 1 Mbps | less than or equal to -20 dBm | less than or equal to -20 dBm |
| LE | 2 Mbps | NA | less than or equal to -20 dBm |

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

| Not Applicable (-1) | This property returns Not Applicable when you set the ACP Offset Channel Mode property to Symmetric. |
| --- | --- |
| Fail (0) | This property returns Fail if more than 3 offsets from offset 3 onwards fail the mask with exception or any offset channel fails the mask without exception. |
| Pass (1) | This property returns Pass if all offsets except up to a maximum of 3 from offset 3 onwards do not fail the mask with exception and all offset channels do not fail the mask without exception. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0500b.html language=enus -->
## TOPIC 00116: ACP:Results:Reference Channel Power (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0500b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0500b.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Reference Channel Power (dBm) Property

**Short Name:**ACP Results Reference Channel Pwr (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the measured power of the reference channel. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0500c.html language=enus -->
## TOPIC 00117: ACP:Results:Lower Offset:Absolute Power (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0500c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0500c.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Absolute Power (dBm) Property

**Short Name:**ACP Results Lower Offset Abs Pwr (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the absolute power measured in the lower offset channel. This value is expressed in dBm.

Use "offset<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0500d.html language=enus -->
## TOPIC 00118: ACP:Results:Lower Offset:Relative Power (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0500d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0500d.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Relative Power (dB) Property

**Short Name:**ACP Results Lower Offset Rel Pwr (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the relative power in the lower offset channel measured with respect to the reference channel power. This value is expressed in dB.

Use "offset<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0500e.html language=enus -->
## TOPIC 00119: ACP:Results:Lower Offset:Margin (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0500e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0500e.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Margin (dB) Property

**Short Name:**ACP Results Lower Offset Margin (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the margin from the limit specified by the mask with exception for lower offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the [ACP Offset Channel Mode](attrb05002.html) property to **In-band**. This property returns NaN if you set the ACP Offset Channel Mode property to **Symmetric**.

Use "offset<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0500f.html language=enus -->
## TOPIC 00120: ACP:Results:Upper Offset:Absolute Power (dBm) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0500f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0500f.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Absolute Power (dBm) Property

**Short Name:**ACP Results Upper Offset Abs Pwr (dBm)

Property of [RFmxBT](crfmxbt.html)

Returns the absolute power measured in the upper offset channel. This value is expressed in dBm.

Use "offset<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05010.html language=enus -->
## TOPIC 00121: ACP:Results:Upper Offset:Relative Power (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05010.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Relative Power (dB) Property

**Short Name:**ACP Results Upper Offset Rel Pwr (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the relative power in the upper offset channel measured with respect to the reference channel power. This value is expressed in dB.

Use "offset<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05011.html language=enus -->
## TOPIC 00122: ACP:Results:Upper Offset:Margin (dB) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05011.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Margin (dB) Property

**Short Name:**ACP Results Upper Offset Margin (dB)

Property of [RFmxBT](crfmxbt.html)

Returns the margin from the limit specified by the mask with exception for upper offsets. This value is expressed in dB. Margin is defined as the difference between the offset absolute power and mask with exception. This result is valid only if you set the [ACP Offset Channel Mode](attrb05002.html) property to **In-band**. This property returns NaN if you set the ACP Offset Channel Mode property to **Symmetric**.

Use "offset<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb05016.html language=enus -->
## TOPIC 00123: ACP:Reference Channel Bandwidth Mode Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb05016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb05016.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ACP:Reference Channel Bandwidth Mode Property

**Short Name:**ACP Reference Channel Bandwidth Mode

Property of [RFmxBT](crfmxbt.html)

| Auto (0) |  |
| --- | --- |
| Manual (1) |  |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0e005.html language=enus -->
## TOPIC 00124: PowerRamp:Averaging:Enabled Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0e005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0e005.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Averaging:Enabled Property

**Short Name:**PowerRamp Averaging Enabled

Property of [RFmxBT](crfmxbt.html)

Specifies whether to enable averaging for PowerRamp measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the PowerRamp Averaging Count property as the number of acquisitions over which the PowerRamp measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0e006.html language=enus -->
## TOPIC 00125: PowerRamp:Averaging:Count Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0e006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0e006.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Averaging:Count Property

**Short Name:**PowerRamp Averaging Count

Property of [RFmxBT](crfmxbt.html)

Specifies the number of acquisitions used for averaging when you set the [PowerRamp Averaging Enabled](attrb0e005.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0e007.html language=enus -->
## TOPIC 00126: PowerRamp:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0e007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0e007.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Number of Analysis Threads Property

**Short Name:**PowerRamp Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

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

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0e009.html language=enus -->
## TOPIC 00127: PowerRamp:Results:Rise Time Mean (s) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0e009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0e009.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Results:Rise Time Mean (s) Property

**Short Name:**PowerRamp Results Rise Time Mean (s)

Property of [RFmxBT](crfmxbt.html)

Rise Time returns the rise time of the acquired signal that is the amount of time taken for the power envelope to rise from a level of 10 percent to 90 percent. When you set the [PowerRamp Averaging Enabled](attrb0e005.html) property to **True**, this parameter returns the mean of the rise time computed for each averaging count. This value is expressed in seconds.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0e00a.html language=enus -->
## TOPIC 00128: PowerRamp:Results:Fall Time Mean (s) Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0e00a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0e00a.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

PowerRamp:Results:Fall Time Mean (s) Property

**Short Name:**PowerRamp Results Fall Time Mean (s)

Property of [RFmxBT](crfmxbt.html)

Fall Time returns the fall time of the acquired signal that is the amount of time taken for the power envelope to fall from a level of 90 percent to 10 percent. When you set the [PowerRamp Averaging Enabled](attrb0e005.html) property to **True**,this parameter returns the mean of the fall time computed for each averaging countt. This value is expressed in seconds.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-for-bluetooth-test-prop path=rfmxbtprop/attrb0f006.html language=enus -->
## TOPIC 00129: ModSpectrum:Number of Analysis Threads Property

- bundle_id: `rfmx-for-bluetooth-test-prop`
- source_path: `rfmxbtprop/attrb0f006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-for-bluetooth-test-prop/raw/resource/enus/rfmxbtprop/attrb0f006.html
- document_id: `rfmx-for-bluetooth-test-prop`
- page_type: `leaf`
- content_type: ``

ModSpectrum:Number of Analysis Threads Property

**Short Name:**ModSpectrum Num Analysis Threads

Property of [RFmxBT](crfmxbt.html)

Specifies the maximum number of threads used for parallelism for ModSpectrum measurement.

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
