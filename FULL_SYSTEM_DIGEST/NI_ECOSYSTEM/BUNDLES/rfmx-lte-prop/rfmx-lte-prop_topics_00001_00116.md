# NI DOCUMENT BUNDLE: rfmx-lte-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-lte-prop start=1 end=116 -->
<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300001.html language=enus -->
## TOPIC 00001: Center Frequency (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300001.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxLTE](crfmxlte.html)

Specifies the center frequency of the acquired RF signal for a single carrier.

For intra-band carrier aggregation, this property specifies the reference frequency of the subblock. This value is expressed in Hz.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300002.html language=enus -->
## TOPIC 00002: Reference Level Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300002.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxLTE](crfmxlte.html)

Specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Reference Level, RFmxLTE Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300003.html language=enus -->
## TOPIC 00003: External Attenuation (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300003.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxLTE](crfmxlte.html)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help* for more information about attenuation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure External Attenuation, RFmxLTE Configure RF |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300004.html language=enus -->
## TOPIC 00004: Trigger:Type Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300004.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxLTE](crfmxlte.html)

Specifies the trigger type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300005.html language=enus -->
## TOPIC 00005: Trigger:Digital Edge:Source Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300005.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxLTE](crfmxlte.html)

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](attr300004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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
| TimerEvent (TimerEvent) | The trigger is received from the Timer Event. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300007.html language=enus -->
## TOPIC 00006: Trigger:IQ Power Edge:Source Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300007.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Source Property

**Short Name:**IQ Power Edge Source

Property of [RFmxLTE](crfmxlte.html)

Specifies the channel from which the device monitors the trigger. This property is used only when you set the [Trigger Type](attr300004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300008.html language=enus -->
## TOPIC 00007: Trigger:IQ Power Edge:Level (dB or dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300008.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level (dB or dBm) Property

**Short Name:**IQ Power Edge Level

Property of [RFmxLTE](crfmxlte.html)

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [IQ Power Edge Level Type](attr300fff.html) property to **Relative** and in dBm when you set the IQ Power Edge Level Type property to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the [Trigger Type](attr300004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300009.html language=enus -->
## TOPIC 00008: Trigger:IQ Power Edge:Slope Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300009.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Slope Property

**Short Name:**IQ Power Edge Slope

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the [Trigger Type](attr300004.html) property to **IQ Power Edge**.

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
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30000a.html language=enus -->
## TOPIC 00009: Trigger:Delay (s) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30000a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxLTE](crfmxlte.html)

Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30000b.html language=enus -->
## TOPIC 00010: Trigger:Minimum Quiet Time:Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30000b.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Mode Property

**Short Name:**Trigger Min Quiet Time Mode

Property of [RFmxLTE](crfmxlte.html)

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
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30000c.html language=enus -->
## TOPIC 00011: Trigger:Minimum Quiet Time:Duration (s) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30000c.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Minimum Quiet Time:Duration (s) Property

**Short Name:**Trigger Min Quiet Time (s)

Property of [RFmxLTE](crfmxlte.html)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

If you set the [IQ Power Edge Slope](attr300009.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30000d.html language=enus -->
## TOPIC 00012: Duplex Scheme Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30000d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Duplex Scheme Property

**Short Name:**Duplex Scheme

Property of [RFmxLTE](crfmxlte.html)

Specifies the duplexing technique of the signal being measured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **FDD**.

| FDD (0) | Specifies that the duplexing technique is frequency-division duplexing. |
| --- | --- |
| TDD (1) | Specifies that the duplexing technique is time-division duplexing. |
| LAA (2) | Specifies that the duplexing technique is license assisted access. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Duplex Scheme |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30000f.html language=enus -->
## TOPIC 00013: Component Carrier:Number of Component Carriers Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30000f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30000f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Number of Component Carriers Property

**Short Name:**Num CCs

Property of [RFmxLTE](crfmxlte.html)

Specifies the number of component carriers configured within a subblock.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Number of Component Carriers, RFmxLTE Configure Number of PUSCH Resource Block Clusters |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300012.html language=enus -->
## TOPIC 00014: Component Carrier:Cell ID Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300012.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Cell ID Property

**Short Name:**Cell ID

Property of [RFmxLTE](crfmxlte.html)

Specifies a physical layer cell identity.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 503, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300015.html language=enus -->
## TOPIC 00015: Component Carrier:Cyclic Prefix Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300015.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Cyclic Prefix Mode Property

**Short Name:**Cyclic Prefix Mode

Property of [RFmxLTE](crfmxlte.html)

Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Normal (0) | The CP duration is 4.67 microseconds, and the number of symbols in a slot is 7. |
| --- | --- |
| Extended (1) | The CP duration is 16.67 microseconds, and the number of symbols in a slot is 6. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30001e.html language=enus -->
## TOPIC 00016: Component Carrier:Uplink:PUSCH:Resource Block Offset Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30001e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30001e.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Uplink:PUSCH:Resource Block Offset Property

**Short Name:**PUSCH RB Offset

Property of [RFmxLTE](crfmxlte.html)

Specifies the starting resource block number of a physical uplink shared channel (PUSCH) cluster.

Use "cluster<*l*>" or "carrier<*k*>" or "subblock<*n*>/carrier<*k*>"/cluster<*l*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure PUSCH Resource Blocks |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30001f.html language=enus -->
## TOPIC 00017: Component Carrier:Uplink:PUSCH:n_DMRS_1 Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30001f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30001f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Uplink:PUSCH:n_DMRS_1 Property

**Short Name:**PUSCH n_DMRS_1

Property of [RFmxLTE](crfmxlte.html)

Specifies the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. The valid values for this property are defined in table 5.5.2.1.1-2 of the *3GPP TS 36.211* specification.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300028.html language=enus -->
## TOPIC 00018: Component Carrier:Auto DMRS Detection Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300028.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Auto DMRS Detection Enabled Property

**Short Name:**Auto DMRS Detection Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether you configure the values of the demodulation reference signal (DMRS) parameters, such as [UL Group Hopping Enabled](attr300019.html), [UL Sequence Hopping Enabled](attr30001a.html), [Cell ID](attr300012.html), [PUSCH n_DMRS_1](attr30001f.html), [PUSCH n_DMRS_2](attr300020.html), and [PUSCH Delta SS](attr300021.html) properties, or if the values of these properties are auto-detected by the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The user-specified DMRS parameters are used. |
| --- | --- |
| True (1) | The values of the DMRS parameters are automatically detected. Measurement returns an error if you set the ModAcc Sync Mode property to Frame, since it is not possible to get the frame boundary when RFmx detects DMRS parameters automatically. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Auto DMRS Detection Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30002e.html language=enus -->
## TOPIC 00019: Component Carrier:Uplink:SRS:Subframe Configuration Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30002e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30002e.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Uplink:SRS:Subframe Configuration Property

**Short Name:**SRS Subframe Configuration

Property of [RFmxLTE](crfmxlte.html)

Specifies the SRS subframe configuration specified in the Table 5.5.3.3-1 of *3GPP 36.211* specification. It is a cell-specific property. This property defines the subframes that are reserved for SRS transmission in a given cell.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. When you set the [Duplex Scheme](attr30000d.html) property to **FDD**, valid values are from 0 to 14, and when you set the Duplex Scheme property to **TDD**, valid values are from 0 to 13.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300033.html language=enus -->
## TOPIC 00020: Component Carrier:Uplink:SRS:n_SRS_CS Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300033.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Uplink:SRS:n_SRS_CS Property

**Short Name:**SRS n_SRS_CS

Property of [RFmxLTE](crfmxlte.html)

Specifies the cyclic shift value *n<sub>SRS</sub>
 <sup>CS</sup>* used for generating SRS base sequence. Refer to section 5.5.3.2 of *3GPP 36.211* specification for more details.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are from 0 to 7, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300042.html language=enus -->
## TOPIC 00021: Component Carrier:Downlink:User Defined:PDCCH Power (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300042.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300042.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Downlink:User Defined:PDCCH Power (dB) Property

**Short Name:**PDCCH Pwr (dB)

Property of [RFmxLTE](crfmxlte.html)

Specifies the power of physical downlink control channel (PDCCH) relative to the power of cell-specific reference signal. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Downlink PDCCH |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30004b.html language=enus -->
## TOPIC 00022: Component Carrier:Downlink:User Defined:PDSCH:RB Allocation Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30004b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30004b.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Downlink:User Defined:PDSCH:RB Allocation Property

**Short Name:**PDSCH RB Allocation

Property of [RFmxLTE](crfmxlte.html)

Specifies the resource blocks of the physical downlink shared channel (PDSCH) allocation.

The following string formats are supported for this property:

1) *RB*
 <sub>StartValue1</sub>-*RB*
 <sub>StopValue1</sub>,*RB*
 <sub>StartValue2</sub>-*RB*
 <sub>StopValue2</sub>

2) *RB*
 <sub>1</sub>,*RB*
 <sub>2</sub>

3) *RB*
 <sub>StartValue1</sub>-*RB*
 <sub>StopValue1</sub>, *RB*
 <sub>1</sub>,*RB*
 <sub>StartValue2</sub>-*RB*
 <sub>StopValue2</sub>,*RB*
 <sub>2</sub>

For example: If the RB allocation is 0-5,7,8,10-15, the RB allocation string specifies contiguous resource blocks from 0 to 5, resource block 7, resource block 8, and contiguous resource blocks from 10 to 15.

Use "PDSCH<*m*>" or "subframe<*l*>" or "carrier<*k*>" or "subblock<*n*>/carrier<*k*>/subframe<*l*>/PDSCH<*m*>" as the selector string to configure or read this property.

The default value is 0-49.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure PDSCH |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300050.html language=enus -->
## TOPIC 00023: eNodeB Category Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300050.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300050.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

eNodeB Category Property

**Short Name:**eNodeB Category

Property of [RFmxLTE](crfmxlte.html)

Specifies the downlink eNodeB (Base station) category. Refer to the *3GPP 36.141* specification for more details.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Wide Area Base Station - Category A**.

| Wide Area Base Station - Category A (0) | Specifies eNodeB is Wide Area Base Station - Category A. |
| --- | --- |
| Wide Area Base Station - Category B Option 1 (1) | Specifies eNodeB is Wide Area Base Station - Category B Option1. |
| Wide Area Base Station - Category B Option 2 (2) | Specifies eNodeB is Wide Area Base Station - Category B Option2. |
| Local Area Base Station (3) | Specifies eNodeB is Local Area Base Station. |
| Home Base Station (4) | Specifies eNodeB is Home Base Station. |
| Medium Range Base Station (5) | Specifies eNodeB is Medium Range Base Station. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure eNodeB Category |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300052.html language=enus -->
## TOPIC 00024: Component Carrier:Uplink:PUSCH:Cyclic Shift Field Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300052.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300052.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Uplink:PUSCH:Cyclic Shift Field Property

**Short Name:**Cyclic Shift Field

Property of [RFmxLTE](crfmxlte.html)

Specifies the cyclic shift field in uplink-related DCI format. When the [DMRS OCC enabled](attr300051.html) property is set to **True**,
 the measurement uses the table 5.5.2.1.1-1 of *3GPP 36.211* specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with [Tx Antenna to Analyze](attr30002c.html).

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 7, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300059.html language=enus -->
## TOPIC 00025: Subblock Frequency (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300059.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300059.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Subblock Frequency (Hz) Property

**Short Name:**Subblock Freq (Hz)

Property of [RFmxLTE](crfmxlte.html)

Specifies the offset of the subblock from the center frequency. This value is expressed in Hz.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300ff6.html language=enus -->
## TOPIC 00026: List:Step:Timer Unit Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300ff6.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300ff6.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

List:Step:Timer Unit Property

**Short Name:**List Step Timer Unit

Property of [RFmxLTE](crfmxlte.html)

Specifies the units in which [List Step Timer Duration](attr300ff9.html) and [List Step Timer Offset](attr300ff7.html) are specified.

You need to use a selector string to configure or read this property for the list step instance.

The default value is **Slot**.

| Slot (1) | List Step Timer Duration and List Step Timer Offset are specified in units of slots. |
| --- | --- |
| Time (6) | List Step Timer Duration and List Step Timer Offset are specified in seconds. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300ff7.html language=enus -->
## TOPIC 00027: List:Step:Timer Offset Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300ff7.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300ff7.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

List:Step:Timer Offset Property

**Short Name:**List Step Timer Offset

Property of [RFmxLTE](crfmxlte.html)

Specifies the offset from the start of the step for which the measurements are computed. The unit for this property is specified by [List Step Timer Unit](attr300ff6.html). This property is valid only when you set the [Digital Edge Source](attr300005.html) property to **TimerEvent**.

You need to use a selector string to configure or read this property for the list step instance.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300ff8.html language=enus -->
## TOPIC 00028: List:Number of Steps Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300ff8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300ff8.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

List:Number of Steps Property

**Short Name:**Num List Steps

Property of [RFmxLTE](crfmxlte.html)

Specifies the number of active steps in a list.

You need to use a selector string to configure or read this property for the list instance.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr300ff9.html language=enus -->
## TOPIC 00029: List:Step:Timer Duration Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr300ff9.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr300ff9.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

List:Step:Timer Duration Property

**Short Name:**List Step Timer Duration

Property of [RFmxLTE](crfmxlte.html)

Specifies the duration of a given list step in units specified by [List Step Timer Unit](attr300ff6.html).

You need to use a selector string to configure or read this property for the list step instance.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30100a.html language=enus -->
## TOPIC 00030: ACP:Offset:Frequency (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30100a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Frequency (Hz) Property

**Short Name:**ACP Offset Freq (Hz)

Property of [RFmxLTE](crfmxlte.html)

Specifies the offset frequency of an offset channel. This value is expressed in Hz. When you set the [Link Direction](attr300029.html) property to **Uplink**, the offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel.
 When you set the Link Direction property to **Downlink**, the offset frequency is computed from the center of the closest component carrier to the center of the nearest RBW filter of the offset channel.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

The default value is 10 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301012.html language=enus -->
## TOPIC 00031: ACP:Measurement Method Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301012.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Method Property

**Short Name:**ACP Meas Method

Property of [RFmxLTE](crfmxlte.html)

Specifies the method for performing the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Normal**.

| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| --- | --- |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668 |
| Sequential FFT (2) | The ACP measurement acquires all the samples specified by the ACP Sweep Time property and divides them in to smaller chunks of equal size defined by the ACP Sequential FFT Size property. FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Sequential FFT method should be used for the following scenarios. While performing fast ACP measurements by utilizing smaller FFT sizes. However, accuracy of the results may be reduced. When measuring signals with time-varying spectral characteristics, sequential FFT with overlap mode set to Automatic should be used. For accurate power measurements when the power characteristics of the signal vary over time averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Num Analysis Threads 1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Averaging Count | >=1 |
| ACP Num Analysis Threads | 1 |
| ACP Amplitude Correction Type | RF Center Frequency |
|  | Note For multi-span FFT, the averaging count should be 1. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ACP Configure Measurement Method |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301014.html language=enus -->
## TOPIC 00032: ACP:Number of Analysis Threads Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301014.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Number of Analysis Threads Property

**Short Name:**ACP Num Analysis Threads

Property of [RFmxLTE](crfmxlte.html)

Specifies the maximum number of threads used for parallelism for the ACP measurement.

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

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301020.html language=enus -->
## TOPIC 00033: ACP:Noise Compensation:Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301020.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Noise Compensation:Enabled Property

**Short Name:**ACP Noise Comp Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether RFmx compensates for the instrument noise while performing the measurement when you set the [ACP Noise Cal Mode](attr30104b.html) property to **Auto**, or when you set the ACP Noise Cal Mode property to **Manual** and the [ACP Meas Mode](attr301047.html) property to **Measure**. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?topicname=rfmxspecan/noise_compensation_algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| --- | --- |
| True (1) | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If the signal analyzer or the measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668, PXIe-5830/5831/5832/5842 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ACP Configure Noise Compensation Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301021.html language=enus -->
## TOPIC 00034: ACP:All Traces Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301021.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:All Traces Enabled Property

**Short Name:**ACP All Traces Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301033.html language=enus -->
## TOPIC 00035: ACP:Results:Upper Offset:Relative Power (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301033.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Relative Power (dB) Property

**Short Name:**ACP Results Upper Offset Rel Pwr (dB)

Property of [RFmxLTE](crfmxlte.html)

Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned.. Refer to the *3GPP TS 36.521* specification for more information about the applicability of the offset channel.

Refer to the [LTE Uplink Adjacent Channel Power](/csh?topicname=rfmxlte/lte_adjacent_channel_power.html) and [LTE Downlink Adjacent Channel Power](/csh?topicname=rfmxlte/lte_downlink_adjacent_channel_power.html) topics for more information about ACP offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30103a.html language=enus -->
## TOPIC 00036: ACP:Offset:Number of UTRA Offsets Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30103a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30103a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Number of UTRA Offsets Property

**Short Name:**ACP Num UTRA Offsets

Property of [RFmxLTE](crfmxlte.html)

Specifies the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the [ACP Configurable Number of Offset Enabled](attr301044.html) property to **True**.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 1, when you set the [CC Bandwidth](attr300010.html) to **200.0 k**.

The default value is 0, when you set the [Band](attr300017.html) property to 46 or [Duplex Scheme](attr301043.html) property to **LAA**.

The default value is 2 for all other configurations.

|  | Note In case of downlink, only 3GPP specification defined values are supported. In case of non-contiguous carrier aggregation, the configured value will be used only for the outer offsets and the offset channels in the gap region are defined as per the 3GPP specification. Offset power reference for the outer UTRA offsets are set according to the value of ACP EUTRA Offset Definition property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ACP Configure Number of UTRA Offsets |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301042.html language=enus -->
## TOPIC 00037: ACP:Offset:Number of GSM Offsets Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301042.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301042.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Number of GSM Offsets Property

**Short Name:**ACP Num GSM Offsets

Property of [RFmxLTE](crfmxlte.html)

Specifies the number of GSM adjacent channel offsets to be configured when you set the [CC Bandwidth](attr300010.html) to **200.0 k** and the [ACP Configurable Number of Offset Enabled](attr301044.html) property to **True**.

The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 1, when you set the CC Bandwidth property to is **200.0 k**. The default value is 0, otherwise.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301045.html language=enus -->
## TOPIC 00038: ACP:FFT:Overlap Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301045.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301045.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap Mode Property

**Short Name:**ACP FFT Overlap Mode

Property of [RFmxLTE](crfmxlte.html)

Specifies the overlap mode when you set the [ACP Meas Method](attr301012.html) property to **Sequential FFT**. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | Disables the overlap between the FFT chunks. |
| --- | --- |
| Automatic (1) | Measurement sets the number of overlapped samples between consecutive FFT chunks to 50% of the ACP Sequential FFT Size property value. |
| User Defined (2) | Measurement uses the overlap that you specify in the ACP FFT Overlap property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301046.html language=enus -->
## TOPIC 00039: ACP:FFT:Overlap (%) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301046.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301046.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap (%) Property

**Short Name:**ACP FFT Overlap (%)

Property of [RFmxLTE](crfmxlte.html)

Specifies the samples to overlap between the consecutive chunks as a percentage of the [ACP Sequential FFT Size](attr301041.html) property value when you set the [ACP Meas Method](attr301012.html) property to **Sequential FFT** and the [ACP FFT Overlap Mode](attr301045.html) property to **User Defined**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr301047.html language=enus -->
## TOPIC 00040: ACP:Measurement Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr301047.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr301047.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Mode Property

**Short Name:**ACP Meas Mode

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?topicname=rfmxspecan/noise_compensation_algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Measure**.

| Measure (0) | ACP measurement is performed on the acquired signal. |
| --- | --- |
| Calibrate Noise Floor (1) | Manual noise calibration of the signal analyzer is performed for the ACP measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30104b.html language=enus -->
## TOPIC 00041: ACP:Noise Calibration:Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30104b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30104b.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ACP:Noise Calibration:Mode Property

**Short Name:**ACP Noise Cal Mode

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?topicname=rfmxspecan/noise_compensation_algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Manual (0) | When you set the ACP Meas Mode property to Calibrate Noise Floor, you can initiate instrument noise calibration for ACP measurement manually. When you set the ACP Meas Mode property to Measure, you can initiate the ACP measurement manually. |
| --- | --- |
| Auto (1) | When you set the ACP Noise Comp Enabled property to True, RFmx sets the Input Isolation Enabled property to Enabled and calibrates the instrument noise in the current state of the instrument. RFmx then resets Input Isolation Enabled property and performs the ACP measurement including compensation for the noise contribution of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set ACP Noise Comp Enabled to False, RFmx does not calibrate instrument noise and performs the ACP measurement without compensating for the noise contribution of the instrument. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr303000.html language=enus -->
## TOPIC 00042: CHP:Measurement Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr303000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr303000.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

CHP:Measurement Enabled Property

**Short Name:**CHP Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable the channel power measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr303003.html language=enus -->
## TOPIC 00043: CHP:Number of Analysis Threads Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr303003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr303003.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

CHP:Number of Analysis Threads Property

**Short Name:**CHP Num Analysis Threads

Property of [RFmxLTE](crfmxlte.html)

Specifies the maximum number of threads used for parallelism for the CHP measurement.

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

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr303007.html language=enus -->
## TOPIC 00044: CHP:Averaging:Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr303007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr303007.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Enabled Property

**Short Name:**CHP Averaging Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable averaging for the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The CHP measurement uses the value of the CHP Averaging Count property as the number of acquisitions over which the CHP measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE CHP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30301d.html language=enus -->
## TOPIC 00045: CHP:Results:Subblock Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30301d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30301d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

CHP:Results:Subblock Power (dBm) Property

**Short Name:**CHP Results Subblock Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE CHP Fetch, RFmxLTE CHP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr303022.html language=enus -->
## TOPIC 00046: CHP:Subblock Integration Bandwidth (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr303022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr303022.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

CHP:Subblock Integration Bandwidth (Hz) Property

**Short Name:**CHP Subblock IBW (Hz)

Property of [RFmxLTE](crfmxlte.html)

Specifies the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock.

Use "subblock<*n*>" as the selector string to read this result.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304000.html language=enus -->
## TOPIC 00047: ModAcc:Measurement Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304000.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Enabled Property

**Short Name:**ModAcc Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304007.html language=enus -->
## TOPIC 00048: ModAcc:FFT Window Offset (%CP) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304007.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:FFT Window Offset (%CP) Property

**Short Name:**ModAcc FFT Window Offset (%CP)

Property of [RFmxLTE](crfmxlte.html)

Specifies the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this property to 0, the EVM window starts at the end of cyclic prefix. If you set this property to 100, the EVM window starts at the beginning of cyclic prefix.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 50. Valid values are 0 to 100, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ModAcc Configure FFT Window Offset, RFmxLTE ModAcc Configure FFT Window Position |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304009.html language=enus -->
## TOPIC 00049: ModAcc:Common Clock Source Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304009.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Common Clock Source Enabled Property

**Short Name:**ModAcc Common Clock Source Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error.

The ModAcc measurement ignores this property, when you set the [Link Direction](attr300029.html) property to **Downlink**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The Sample Clock error is estimated independently. |
| --- | --- |
| True (1) | The Sample Clock error is estimated from carrier frequency offset. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ModAcc Configure Common Clock Source Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30400b.html language=enus -->
## TOPIC 00050: ModAcc:Averaging:Count Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30400b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30400b.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Averaging:Count Property

**Short Name:**ModAcc Averaging Count

Property of [RFmxLTE](crfmxlte.html)

Specifies the number of acquisitions used for averaging when you set the [ModAcc Averaging Enabled](attr30400a.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ModAcc Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30400f.html language=enus -->
## TOPIC 00051: ModAcc:Results:Mean RMS Composite EVM (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30400f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30400f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Mean RMS Composite EVM (% or dB) Property

**Short Name:**ModAcc Results Mean RMS Composite EVM

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304015.html language=enus -->
## TOPIC 00052: ModAcc:Results:Peak Composite EVM Subcarrier Index Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304015.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak Composite EVM Subcarrier Index Property

**Short Name:**ModAcc Results Pk Composite EVM Subcarrier Index

Property of [RFmxLTE](crfmxlte.html)

Returns the subcarrier index where the [maximum peak composite EVM](attr304010.html) for ModAcc occurs.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304028.html language=enus -->
## TOPIC 00053: ModAcc:Results:Mean Symbol Clock Error (ppm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304028.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Mean Symbol Clock Error (ppm) Property

**Short Name:**ModAcc Results Mean Symbol Clock Error (ppm)

Property of [RFmxLTE](crfmxlte.html)

Returns the estimated symbol clock error averaged over the slots specified by the [ModAcc Meas Length](attr304005.html) property. This value is expressed in ppm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30402d.html language=enus -->
## TOPIC 00054: ModAcc:Results:Spectral Flatness:Range2-Max to Range2-Min (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30402d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30402d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Spectral Flatness:Range2-Max to Range2-Min (dB) Property

**Short Name:**ModAcc Results Spectral Flatness Range2-Max to Range2-Min (dB)

Property of [RFmxLTE](crfmxlte.html)

Returns the peak-to-peak ripple of the EVM equalizer coefficients within the frequency *Measurement Offset* parameter. This value is expressed in dB.

The frequency *Measurement Offset* parameter is defined in section 6.5.2.4.5 of the *3GPP TS 36.521* specification.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30402e.html language=enus -->
## TOPIC 00055: ModAcc:Results:Spectral Flatness:Range1-Max to Range2-Min (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30402e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30402e.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Spectral Flatness:Range1-Max to Range2-Min (dB) Property

**Short Name:**ModAcc Results Spectral Flatness Range1-Max to Range2-Min (dB)

Property of [RFmxLTE](crfmxlte.html)

Returns the peak-to-peak ripple of the EVM equalizer coefficients from the frequency *Range1* to the frequency *Measurement Offset* parameter. The frequency *Range1* and frequency *Measurement Offset* parameter are defined in the section 6.5.2.4.5 of the *3GPP TS 36.521* specification. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304039.html language=enus -->
## TOPIC 00056: ModAcc:FFT Window Length (%CP) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304039.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:FFT Window Length (%CP) Property

**Short Name:**ModAcc FFT Window Length (%CP)

Property of [RFmxLTE](crfmxlte.html)

Specifies the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This property is used when you set the [ModAcc FFT Window Type](attr304038.html) property to **3GPP**, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of *3GPP 36.521* specification for more information.

Refer to the [LTE Modulation Accuracy (ModAcc)](/csh?topicname=rfmxlte/lte_modulation_accuracy.html) topic for more information about FFT Window Length.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is as given in the 3GPP specification. The default value is 91.7 %CP for 10M bandwidth. Valid values range from -1 to 100, inclusive.

When this property is set to -1, RFmx populates the FFT Window Length based on carrier bandwidth automatically, as given in the Annexe E.5.1 of *3GPP 36.104* specification.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ModAcc Configure FFT Window Position |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30403a.html language=enus -->
## TOPIC 00057: ModAcc:Results:Mean RMS Composite Magnitude Error (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30403a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30403a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Mean RMS Composite Magnitude Error (% or dB) Property

**Short Name:**ModAcc Results Mean RMS Composite Magnitude Error

Property of [RFmxLTE](crfmxlte.html)

Returns the RMS mean value of the composite magnitude error calculated over the slots specified by the [ModAcc Meas Length](attr304005.html) property on all the configured channels.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink**.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30403c.html language=enus -->
## TOPIC 00058: ModAcc:Results:Mean RMS Composite Phase Error (deg) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30403c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30403c.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Mean RMS Composite Phase Error (deg) Property

**Short Name:**ModAcc Results Mean RMS Composite Phase Error (deg)

Property of [RFmxLTE](crfmxlte.html)

Returns the RMS mean value of the composite phase error calculated over the slots specified by the [ModAcc Meas Length](attr304005.html) property on all the configured channels. This value is expressed in degrees.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink**.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30403d.html language=enus -->
## TOPIC 00059: ModAcc:Results:Maximum Peak Composite Phase Error (deg) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30403d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30403d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Maximum Peak Composite Phase Error (deg) Property

**Short Name:**ModAcc Results Max Pk Composite Phase Error (deg)

Property of [RFmxLTE](crfmxlte.html)

Returns the peak value of phase error calculated over the slots specified by the [ModAcc Meas Length](attr304005.html) property on all thee configured channels. This value is expressed in degrees.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink**.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30403e.html language=enus -->
## TOPIC 00060: ModAcc:Results:Uplink:Subblock In-Band Emission Margin (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30403e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30403e.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:Subblock In-Band Emission Margin (dB) Property

**Short Name:**ModAcc Results Subblock In-Band Emission Margin (dB)

Property of [RFmxLTE](crfmxlte.html)

Returns the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB.

The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2A.3 of the *3GPP TS 36.521* specification.

The in-band emissions are a measure of the interference falling into the non-allocated resources blocks. The result of this property is valid only when you set the [Transmitter Architecture](../rfmxlteprop/attr30d002.html) property to **LO per Subblock**.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30403f.html language=enus -->
## TOPIC 00061: ModAcc:Results:Subblock Mean IQ Origin Offset (dBc) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30403f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30403f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Subblock Mean IQ Origin Offset (dBc) Property

**Short Name:**ModAcc Results Subblock Mean IQ Origin Offset (dBc)

Property of [RFmxLTE](crfmxlte.html)

Returns the estimated I/Q origin offset averaged over the slots specified by the [ModAcc Meas Length](attr304005.html) property in the subblock. This value is expressed in dBc.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink** and the [Transmitter Architecture](attr30d002.html) property to **LO per Subblock**.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304040.html language=enus -->
## TOPIC 00062: ModAcc:Results:Subblock Mean IQ Gain Imbalance (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304040.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304040.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Subblock Mean IQ Gain Imbalance (dB) Property

**Short Name:**ModAcc Results Subblock Mean IQ Gain Imbalance (dB)

Property of [RFmxLTE](crfmxlte.html)

Returns the estimated I/Q gain imbalance averaged over the slots specified by the [ModAcc Meas Length](attr304005.html) property. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink** and the [Transmitter Architecture](../rfmxlteprop/attr30d002.html) property to **LO per Subblock**. Otherwise, this parameter returns NaN, as measurement of this result is currently not supported.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30404f.html language=enus -->
## TOPIC 00063: ModAcc:Results:Downlink:Mean RMS PHICH EVM (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30404f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30404f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Downlink:Mean RMS PHICH EVM (% or dB) Property

**Short Name:**ModAcc Results Mean RMS PHICH EVM

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of RMS EVMs calculated on PHICH channel over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304051.html language=enus -->
## TOPIC 00064: ModAcc:Results:Downlink:RS Transmit Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304051.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304051.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Downlink:RS Transmit Power (dBm) Property

**Short Name:**ModAcc Results DL RS Tx Power (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the [ModAcc Meas Length](attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304052.html language=enus -->
## TOPIC 00065: ModAcc:Results:Downlink:OFDM Symbol Tx Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304052.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304052.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Downlink:OFDM Symbol Tx Power (dBm) Property

**Short Name:**ModAcc Results DL OFDM Symbol Tx Power (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of power calculated in one OFDM symbol over the slots specified by the [ModAcc Meas Length](attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304054.html language=enus -->
## TOPIC 00066: Component Carrier:Downlink:Auto PDSCH Channel Detection Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304054.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304054.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:Downlink:Auto PDSCH Channel Detection Enabled Property

**Short Name:**Auto PDSCH Channel Detection Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the values of the [PDSCH RB Allocation](attr30004b.html) property, the corresponding [PDSCH CW0 Modulation Type](attr30004a.html) property, and the [PDSCH Power](attr30004c.html) property are auto-detected by the measurement or user-specified. This property is not valid, when you set the [DL Ch Configuration Mode](attr30003d.html) property to **Test Model**. The measurement ignores this property, when you set the [Link Direction](attr300029.html)
 property to **Uplink**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the values of the PDSCH RB Allocation property, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power property that you specify. |
| --- | --- |
| True (1) | The measurement uses the values of the PDSCH RB Allocation property, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power property that are auto-detected. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304059.html language=enus -->
## TOPIC 00067: Component Carrier:LAA:Uplink Start Position Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304059.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304059.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:LAA:Uplink Start Position Property

**Short Name:**LAA UL Start Position

Property of [RFmxLTE](crfmxlte.html)

Specifies the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the *3GPP 36.211* specification for more information regarding LAA uplink start position.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **00**.

| 00 (0) | The symbol 0 in the first subframe of an LAA uplink burst is completely occupied. There is no idle duration. |
| --- | --- |
| 01 (1) | The starting position of symbol 0 in the first subframe of an LAA uplink burst is calculated as per section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |
| 10 (2) | The starting position of symbol 0 in the first subframe of an LAA uplink burst is calculated as per section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |
| 11 (3) | The symbol 0 in the first subframe of an LAA uplink burst is completely idle. Symbol 0 is not transmitted in this case. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30405d.html language=enus -->
## TOPIC 00068: ModAcc:Results:Downlink:PDSCH:Mean RMS 1024QAM EVM (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30405d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30405d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Downlink:PDSCH:Mean RMS 1024QAM EVM (% or dB) Property

**Short Name:**ModAcc Results PDSCH Mean RMS 1024QAM EVM

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30405f.html language=enus -->
## TOPIC 00069: Component Carrier:NB-IoT:Uplink Subcarrier Spacing Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30405f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30405f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:NB-IoT:Uplink Subcarrier Spacing Property

**Short Name:**NB-IoT UL Subcarrier Spacing

Property of [RFmxLTE](crfmxlte.html)

Specifies the subcarrier bandwidth of an NB-IoT signal. This property specifies the spacing between adjacent subcarriers.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **15 kHz**.

| 15 kHz (0) | The subcarrier spacing is 15 kHz. |
| --- | --- |
| 3.75 kHz (1) | The subcarrier spacing is 3.75 kHz. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304064.html language=enus -->
## TOPIC 00070: Component Carrier:NB-IoT:NPUSCH:Modulation Type Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304064.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304064.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:NB-IoT:NPUSCH:Modulation Type Property

**Short Name:**NPUSCH Mod Type

Property of [RFmxLTE](crfmxlte.html)

Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). This property is valid when [NPUSCH Num Tones](attr304063.html) is equal to 1 and [NPUSCH Format](attr304061.html) is equal to 1. The modulation type for other configurations is defined in Table 10.1.3.2-1 of the *3GPP TS 36.211* specification.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **BPSK**.

| BPSK (0) | Specifies a BPSK modulation scheme. |
| --- | --- |
| QPSK (1) | Specifies a QPSK modulation scheme. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304065.html language=enus -->
## TOPIC 00071: Component Carrier:NB-IoT:NPUSCH:DMRS Base Sequence Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304065.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304065.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:NB-IoT:NPUSCH:DMRS Base Sequence Mode Property

**Short Name:**NPUSCH DMRS Base Sequence Mode

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the [NPUSCH DMRS Base Sequence Index](attr304066.html) property is computed by the measurement or specified by you. This property is valid when you set the [NPUSCH Group Hopping Enabled](attr304069.html) property to **False**, the [NPUSCH Format](attr304061.html) property to 1, and the [NPUSCH Num Tones](attr304063.html) property to 3, 6, or 12.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **Auto**.

| Manual (0) | The measurement uses the value that you specify for the NPUSCH DMRS Base Sequence Index property. |
| --- | --- |
| Auto (1) | The measurement uses the value of NCell ID property to compute the NPUSCH DMRS Base Sequence Index as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30406c.html language=enus -->
## TOPIC 00072: ModAcc:Results:Uplink:NPUSCH:Mean RMS DMRS EVM (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30406c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30406c.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:NPUSCH:Mean RMS DMRS EVM (% or dB) Property

**Short Name:**ModAcc Results NPUSCH Mean RMS DMRS EVM

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the result is returned as a percentage, and when you set the ModAcc EVM Unit property to **dB**, the result is returned in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30406f.html language=enus -->
## TOPIC 00073: ModAcc:Results:Uplink:NPUSCH:Mean DMRS Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30406f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30406f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Uplink:NPUSCH:Mean DMRS Power (dBm) Property

**Short Name:**ModAcc Results NPUSCH Mean DMRS Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304072.html language=enus -->
## TOPIC 00074: Component Carrier:NB-IoT:NPUSCH:Starting Slot Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304072.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304072.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Component Carrier:NB-IoT:NPUSCH:Starting Slot Property

**Short Name:**NPUSCH Starting Slot

Property of [RFmxLTE](crfmxlte.html)

Specifies the starting slot number of the NPUSCH burst.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304073.html language=enus -->
## TOPIC 00075: ModAcc:Results:Sidelink:PSSCH:Mean RMS Data EVM (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304073.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304073.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Sidelink:PSSCH:Mean RMS Data EVM (% or dB) Property

**Short Name:**ModAcc Results PSSCH Mean RMS Data EVM

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of the RMS EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304074.html language=enus -->
## TOPIC 00076: ModAcc:Results:Sidelink:PSSCH:Maximum Peak Data EVM (% or dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304074.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304074.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Sidelink:PSSCH:Maximum Peak Data EVM (% or dB) Property

**Short Name:**ModAcc Results PSSCH Max Pk Data EVM

Property of [RFmxLTE](crfmxlte.html)

Returns the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [ModAcc Meas Length](attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304077.html language=enus -->
## TOPIC 00077: ModAcc:Results:Sidelink:PSSCH:Mean Data Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304077.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304077.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Sidelink:PSSCH:Mean Data Power (dBm) Property

**Short Name:**ModAcc Results PSSCH Mean Data Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [ModAcc Meas Length](attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304078.html language=enus -->
## TOPIC 00078: ModAcc:Results:Sidelink:PSSCH:Mean DMRS Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304078.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304078.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Sidelink:PSSCH:Mean DMRS Power (dBm) Property

**Short Name:**ModAcc Results PSSCH Mean DMRS Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the [ModAcc Meas Length](attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr304079.html language=enus -->
## TOPIC 00079: ModAcc:IQ Impairments:IQ Origin Offset Estimation Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr304079.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr304079.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Impairments:IQ Origin Offset Estimation Enabled Property

**Short Name:**ModAcc IQ Origin Offset Estimation Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to estimate IQ origin offset.

|  | Note IQ origin offset estimation is supported only when you set the Link direction property to Uplink or Sidelink. |
| --- | --- |

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | IQ origin offset estimation and correction is disabled. |
| --- | --- |
| True (1) | IQ origin offset estimation and correction is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30407a.html language=enus -->
## TOPIC 00080: ModAcc:IQ Impairments:IQ Mismatch Estimation Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30407a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30407a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Impairments:IQ Mismatch Estimation Enabled Property

**Short Name:**ModAcc IQ Mismatch Estimation Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to estimate IQ mismatch such as gain imbalance, quadrature skew, and timing skew.

|  | Note Timing skew value is estimated only when you set the Link direction property to Uplink. |
| --- | --- |

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | IQ mismatch estimation is disabled. |
| --- | --- |
| True (1) | IQ mismatch estimation is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30407c.html language=enus -->
## TOPIC 00081: ModAcc:IQ Impairments:IQ Quadrature Error Correction Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30407c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30407c.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Impairments:IQ Quadrature Error Correction Enabled Property

**Short Name:**ModAcc IQ Quadrature Error Correction Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable IQ quadrature error correction.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | IQ quadrature error correction is disabled. |
| --- | --- |
| True (1) | IQ quadrature error correction is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr306003.html language=enus -->
## TOPIC 00082: OBW:Number of Analysis Threads Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr306003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr306003.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:Number of Analysis Threads Property

**Short Name:**OBW Num Analysis Threads

Property of [RFmxLTE](crfmxlte.html)

Specifies the maximum number of threads used for parallelism for the OBW measurement.

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

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30600c.html language=enus -->
## TOPIC 00083: OBW:RBW Filter:Auto Bandwidth Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30600c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30600c.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Auto Bandwidth Property

**Short Name:**OBW RBW Auto

Property of [RFmxLTE](crfmxlte.html)

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
| High-level VIs | RFmxLTE OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30600d.html language=enus -->
## TOPIC 00084: OBW:RBW Filter:Bandwidth (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30600d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30600d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Bandwidth (Hz) Property

**Short Name:**OBW RBW (Hz)

Property of [RFmxLTE](crfmxlte.html)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the [OBW RBW Auto](attr30600c.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30600e.html language=enus -->
## TOPIC 00085: OBW:RBW Filter:Type Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30600e.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Type Property

**Short Name:**OBW RBW Filter Type

Property of [RFmxLTE](crfmxlte.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | No RBW filtering is performed. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30600f.html language=enus -->
## TOPIC 00086: OBW:Sweep Time:Auto Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30600f.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:Sweep Time:Auto Property

**Short Name:**OBW Sweep Time Auto

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- |
| True (1) | The measurement uses a sweep time of 1 ms. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr306010.html language=enus -->
## TOPIC 00087: OBW:Sweep Time:Interval (s) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr306010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr306010.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:Sweep Time:Interval (s) Property

**Short Name:**OBW Sweep Time (s)

Property of [RFmxLTE](crfmxlte.html)

Specifies the sweep time when you set the [OBW Sweep Time Auto](attr30600f.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1 ms.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr306013.html language=enus -->
## TOPIC 00088: OBW:Results:Occupied Bandwidth (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr306013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr306013.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Occupied Bandwidth (Hz) Property

**Short Name:**OBW Results Occupied BW (Hz)

Property of [RFmxLTE](crfmxlte.html)

Returns the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz.

Refer to the [LTE Occupied Bandwidth](/csh?topicname=rfmxlte/lte_occupied_bandwidth_obw.html) topic for more information.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308010.html language=enus -->
## TOPIC 00089: SEM:Offset:Absolute Limit:Start (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308010.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Absolute Limit:Start (dBm) Property

**Short Name:**SEM Offset Abs Limit Start (dBm)

Property of [RFmxLTE](crfmxlte.html)

Specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this property.

The default value is -16.5.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Offset Absolute Limit |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308027.html language=enus -->
## TOPIC 00090: SEM:All Traces Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308027.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:All Traces Enabled Property

**Short Name:**SEM All Traces Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308028.html language=enus -->
## TOPIC 00091: SEM:Results:Total Aggregated Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308028.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Total Aggregated Power (dBm) Property

**Short Name:**SEM Results Total Aggregated Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308029.html language=enus -->
## TOPIC 00092: SEM:Results:Measurement Status Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308029.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Measurement Status Property

**Short Name:**SEM Results Meas Status

Property of [RFmxLTE](crfmxlte.html)

Returns the overall measurement status based on the standard mask type that you configure in the [SEM Standard Mask Type](attr30804c.html) property.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

| Fail (0) | Indicates that the measurement has failed. |
| --- | --- |
| Pass (1) | Indicates that the measurement has passed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308034.html language=enus -->
## TOPIC 00093: SEM:Results:Lower Offset:Absolute Integrated Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308034.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Lower Offset Abs Integrated Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information about SEM offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308035.html language=enus -->
## TOPIC 00094: SEM:Results:Lower Offset:Relative Integrated Power (dB) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308035.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Relative Integrated Power (dB) Property

**Short Name:**SEM Results Lower Offset Rel Integrated Pwr (dB)

Property of [RFmxLTE](crfmxlte.html)

Returns the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information about SEM offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308036.html language=enus -->
## TOPIC 00095: SEM:Results:Lower Offset:Absolute Peak Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308036.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Absolute Peak Power (dBm) Property

**Short Name:**SEM Results Lower Offset Abs Pk Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information about SEM offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30803a.html language=enus -->
## TOPIC 00096: SEM:Results:Lower Offset:Margin Absolute Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30803a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30803a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Margin Absolute Power (dBm) Property

**Short Name:**SEM Results Lower Offset Margin Abs Pwr (dBm)

Property of [RFmxLTE](crfmxlte.html)

Returns the power at which the margin occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information about SEM offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30803c.html language=enus -->
## TOPIC 00097: SEM:Results:Lower Offset:Margin Frequency (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30803c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30803c.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Margin Frequency (Hz) Property

**Short Name:**SEM Results Lower Offset Margin Freq (Hz)

Property of [RFmxLTE](crfmxlte.html)

Returns the frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information about SEM offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30803d.html language=enus -->
## TOPIC 00098: SEM:Results:Lower Offset:Measurement Status Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30803d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30803d.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Measurement Status Property

**Short Name:**SEM Results Lower Offset Meas Status

Property of [RFmxLTE](crfmxlte.html)

Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the [SEM Standard Mask Type](attr30804c.html) property.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_spectral_emission_mask_sem.html) and [LTE Downlink Spectral Emission Mask](/csh?topicname=rfmxlte/lte_downlink_spectral_emission_mask_sem.html) topics for more information about SEM mask.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

| Fail (0) | Indicates that the measurement has failed. |
| --- | --- |
| Pass (1) | Indicates that the measurement has passed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30804e.html language=enus -->
## TOPIC 00099: SEM:Results:Subblock Integration Bandwidth (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30804e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30804e.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Subblock Integration Bandwidth (Hz) Property

**Short Name:**SEM Results Subblock IBW (Hz)

Property of [RFmxLTE](crfmxlte.html)

Returns the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308056.html language=enus -->
## TOPIC 00100: SEM:Component Carrier:Maximum Output Power (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308056.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308056.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Component Carrier:Maximum Output Power (dBm) Property

**Short Name:**SEM CC Max Output Power (dBm)

Property of [RFmxLTE](crfmxlte.html)

Specifies the maximum output power, P<sub>max,c</sub>, per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of *3GPP 36.141* specification.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are within 38, inclusive.

|  | Note This property is considered only when you set the Link Direction property to Downlink, eNodeB Category property to Medium Range Base Station, and SEM DL Mask Type property to eNodeB Category Based. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Component Carrier Maximum Output Power |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr308057.html language=enus -->
## TOPIC 00101: SEM:Amplitude Correction Type Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr308057.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr308057.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SEM:Amplitude Correction Type Property

**Short Name:**SEM Amplitude Correction Type

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?topicname=rfmxinstrvi/rfmxinstr_configure_external_attenuation_table.html) VI to configure the external attenuation table.

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

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr309014.html language=enus -->
## TOPIC 00102: PVT:Results:Burst Width (s) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr309014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr309014.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Burst Width (s) Property

**Short Name:**PVT Results Burst Width (s)

Property of [RFmxLTE](crfmxlte.html)

Returns the width of the captured burst. This value is expressed in seconds.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxLTE PvT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30a000.html language=enus -->
## TOPIC 00103: SlotPhase:Measurement Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30a000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30a000.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Measurement Enabled Property

**Short Name:**SlotPhase Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30a002.html language=enus -->
## TOPIC 00104: SlotPhase:Measurement Offset (slots) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30a002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30a002.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Measurement Offset (slots) Property

**Short Name:**SlotPhase Meas Offset (slots)

Property of [RFmxLTE](crfmxlte.html)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPhase Sync Mode](attr30a006.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0. Valid values are 0 to 19, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30a006.html language=enus -->
## TOPIC 00105: SlotPhase:Synchronization Mode Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30a006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30a006.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Synchronization Mode Property

**Short Name:**SlotPhase Sync Mode

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the measurement is performed from the frame or the slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Slot**.

| Frame (0) | The frame boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property, starting at the offset from the boundary specified by the SlotPhase Meas Offset property. When the Trigger Type property is set to Digital, the measurement expects a trigger at the frame boundary. |
| --- | --- |
| Slot (1) | The slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property, starting at the offset from the boundary specified by the SlotPhase Meas Offset property. When the Trigger Type property is set to Digital, the measurement expects a trigger at any slot boundary. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30a007.html language=enus -->
## TOPIC 00106: SlotPhase:Exclusion Period Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30a007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30a007.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPhase:Exclusion Period Enabled Property

**Short Name:**SlotPhase Exclusion Period Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to exclude some portions of the slots when calculating the phase. This property is valid only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the *3GPP 36.521-1* specification for more information about the exclusion.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Phase is calculated on complete slots. |
| --- | --- |
| True (1) | Phase is calculated on truncated slots. The power changes at the slot boundaries are detected by the measurement, and the defined 3GPP specification period is excluded from the slots being measured. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30b003.html language=enus -->
## TOPIC 00107: SlotPower:Measurement Length (subframes) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30b003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30b003.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Measurement Length (subframes) Property

**Short Name:**SlotPower Meas Length (subframes)

Property of [RFmxLTE](crfmxlte.html)

Specifies the number of subframes to be measured. This value is expressed in subframe.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SlotPower Configure Measurement Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30b006.html language=enus -->
## TOPIC 00108: SlotPower:Spectrum Inverted Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30b006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30b006.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:Spectrum Inverted Property

**Short Name:**SlotPower Spectrum Inverted

Property of [RFmxLTE](crfmxlte.html)

Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The spectrum of the measured signal is not inverted. |
| --- | --- |
| True (1) | The measured signal is inverted and the measurement corrects the signal by swapping the I and the Q components. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30b00a.html language=enus -->
## TOPIC 00109: SlotPower:All Traces Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30b00a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30b00a.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

SlotPower:All Traces Enabled Property

**Short Name:**SlotPower All Traces Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether to enable the traces to be stored and retrieved after performing the SlotPower measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30c000.html language=enus -->
## TOPIC 00110: Result Fetch Timeout (s) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30c000.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Result Fetch Timeout (s) Property

**Short Name:**Result Fetch Timeout (s)

Property of [RFmxLTE](crfmxlte.html)

Specifies the time to wait before results are available in the [RFmxLTE Property Node](/csh?topicname=rfmxltevi/rfmxlte_property_node.html). This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30d000.html language=enus -->
## TOPIC 00111: Advanced:Auto Level Initial Reference Level (dBm) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30d000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30d000.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Auto Level Initial Reference Level (dBm) Property

**Short Name:**Auto Level Initial Ref Level (dBm)

Property of [RFmxLTE](crfmxlte.html)

Specifies the initial reference level that the [RFmxLTE Auto Level](/csh?topicname=rfmxltevi/rfmxlte_auto_level.html) VI uses to estimate the peak power of the input signal. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 30.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Auto Level |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30d001.html language=enus -->
## TOPIC 00112: Advanced:Acquisition Bandwidth Optimization Enabled Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30d001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30d001.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Acquisition Bandwidth Optimization Enabled Property

**Short Name:**Acq BW Optimization Enabled

Property of [RFmxLTE](crfmxlte.html)

Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

Refer to the [Acquisition Bandwidth Optimization Enabled](/csh?topicname=rfmxlte/acquisition_bandwidth.html) topic for more information.

The default value is **True**.

| False (0) | RFmx does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the Center Frequency that you configure. |
| --- | --- |
| True (1) | RFmx positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this property disabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30d002.html language=enus -->
## TOPIC 00113: Advanced:Transmitter Architecture Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30d002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30d002.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Transmitter Architecture Property

**Short Name:**Transmitter Architecture

Property of [RFmxLTE](crfmxlte.html)

Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

The measurement ignores this property when you set the [Link Direction](attr300029.html) property to **Downlink**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **LO per Component Carrier**.

| LO per Component Carrier (0) | IQ impairments and In-band emission are calculated per component carrier. |
| --- | --- |
| LO per Subblock (1) | Additional subblock based results such as Subblock IQ Offset and Subblock In band emission are calculated apart from per carrier results. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30d003.html language=enus -->
## TOPIC 00114: Advanced:Limited Configuration Change Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30d003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30d003.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Limited Configuration Change Property

**Short Name:**Limited Configuration Change

Property of [RFmxLTE](crfmxlte.html)

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this property can help achieve faster measurements. When you set this property to a value other than **Disabled**, RFmx will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](limitations.html) topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to pre-compute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFmxInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| --- | --- |
| No Change (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Reference Level (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the Reference Level property value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Freq and Ref Level (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type property to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level (5) | Signal configuration, other than Selected Ports, Center frequency, Reference level, External attenuation, and RFmxInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type property to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/attr30d004.html language=enus -->
## TOPIC 00115: Advanced: Center Frequency for Limits (Hz) Property

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/attr30d004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/attr30d004.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

Advanced: Center Frequency for Limits (Hz) Property

**Short Name:**Center Freq for Limits (Hz)

Property of [RFmxLTE](crfmxlte.html)

Specifies the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this property, the measurement internally uses the [Center Frequency](attr300001.html) for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-lte-prop path=rfmxlteprop/crfmxlte.html language=enus -->
## TOPIC 00116: RFmxLTE Properties

- bundle_id: `rfmx-lte-prop`
- source_path: `rfmxlteprop/crfmxlte.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-lte-prop/raw/resource/enus/rfmxlteprop/crfmxlte.html
- document_id: `rfmx-lte-prop`
- page_type: `leaf`
- content_type: ``

RFmxLTE Properties

Use the RFmxLTE properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the selector string used to access all subsequent properties. Details |
| Selected Ports | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. Details |
| Center Frequency (Hz) | Specifies the center frequency of the acquired RF signal for a single carrier. Details |
| Reference Level | Specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as Vpk-pk for baseband devices. Details |
| External Attenuation (dB) | Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. Refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help for more information about attenuation. Details |
| Reference Level Headroom | Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Details |
| Trigger:Type | Specifies the trigger type. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:IQ Power Edge:Source | Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level (dB or dBm) | Specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type property to Relative and in dBm when you set the IQ Power Edge Level Type property to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level Type | Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Slope | Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:Delay (s) | Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples. Details |
| Trigger:Minimum Quiet Time:Mode | Specifies whether the measurement computes the minimum quiet time used for triggering. Details |
| Trigger:Minimum Quiet Time:Duration (s) | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope, the signal is quiet above the trigger level. Details |
| Link Direction | Specifies the link direction of the received signal. Details |
| Duplex Scheme | Specifies the duplexing technique of the signal being measured. Details |
| Uplink/Downlink Configuration | Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. Details |
| eNodeB Category | Specifies the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. Details |
| Special Subframe Configuration | Specifies the special subframe configuration index. It defines the length of DwPTS, GP, and UpPTS for TDD transmission as defined in the section 4.2 of 3GPP 36.211 specification. Details |
| Number of DUT Antennas | Specifies the number of physical antennas available at the DUT for transmission in a MIMO setup. Details |
| Tx Antenna to Analyze | Specifies the physical antenna connected to the analyzer. Details |
| Number of Subblocks | Specifies the number of subblocks that are configured in intra-band non-contiguous carrier aggregation. Details |
| Subblock Frequency (Hz) | Specifies the offset of the subblock from the center frequency. This value is expressed in Hz. Details |
| Band | Specifies the evolved universal terrestrial radio access (E-UTRA) operating frequency band of a subblock, as defined in section 5.2 of the 3GPP TS 36.521 specification. Details |
| Component Carrier Spacing Type | Specifies the spacing between two adjacent component carriers within a subblock. Refer to the Channel Spacing and Carrier Frequency Offset Definition and Reference Frequency topics for more information about component carrier spacing. Details |
| Component Carrier at Center Frequency | Specifies the index of the component carrier having its center at the user-configured center frequency. RFmx LTE uses this property along with CC Spacing Type property to calculate the value of the CC Freq. Details |
| Component Carrier:Number of Component Carriers | Specifies the number of component carriers configured within a subblock. Details |
| Component Carrier:Bandwidth (Hz) | Specifies the channel bandwidth of the signal being measured. This value is expressed in Hz. Details |
| Component Carrier:Frequency (Hz) | Specifies the offset of the component carrier from the subblock center frequency that you configure in the Center Frequency property. This value is expressed in Hz. This property is valid only when you set the CC Spacing Type property to User. Details |
| Component Carrier:Cell ID | Specifies a physical layer cell identity. Details |
| Component Carrier:Cyclic Prefix Mode | Specifies the cyclic prefix (CP) duration and the number of symbols in a slot for the signal being measured. Details |
| Component Carrier:Downlink: Auto Cell ID Detection Enabled | Specifies whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using ModAcc Results DL Detected Cell ID property. Details |
| Component Carrier:Downlink:Channel Configuration Mode | Specifies the channel configuration mode. Details |
| Component Carrier:Downlink:Auto PDSCH Channel Detection Enabled | Specifies whether the values of the PDSCH RB Allocation property, the corresponding PDSCH CW0 Modulation Type property, and the PDSCH Power property are auto-detected by the measurement or user-specified. This property is not valid, when you set the DL Ch Configuration Mode property to Test Model. The measurement ignores this property, when you set the Link Direction property to Uplink. Details |
| Component Carrier:Downlink:Auto Control Channel Power Detection Enabled | Specifies whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power property is not supported. This property is not valid, when you set the DL Ch Configuration Mode property to Test Model. The measurement ignores this property, when you set the Link Direction property to Uplink. Details |
| Component Carrier:Downlink:Auto PCFICH CFI Detection Enabled | Specifies whether the value of PCFICH CFI property is auto-detected by the measurement or user-specified. This property is not valid, when you set the DL Ch Configuration Mode property to Test Model. The measurement ignores this property, when you set the Link Direction property to Uplink. Details |
| Component Carrier:Downlink:Mi Configuration | Specifies whether the Mi parameter is specified by section 6.1.2.6 of 3GPP TS 36.141 specification for testing E-TMs or in the Table 6.9-1 of 3GPP TS 36.211 specification. The Mi parameter determines the number of PHICH groups in each downlink subframe, when you set the Duplex Scheme property to TDD. Details |
| Component Carrier:Downlink:User Defined:Cell Specific Ratio | Specifies the ratio Rhob/Rhoa for the cell-specific ratio of one, two, or four cell-specific antenna ports as described in Table 5.2-1 in section 5.2 of the 3GPP TS 36.213 specification. This property determines the power of the channel resource element (RE) in the symbols that do not contain the reference symbols. Details |
| Component Carrier:Downlink:User Defined:PSS Power (dB) | Specifies the power of primary synchronization signal (PSS) relative to the power of cell-specific reference signal. This value is expressed in dB. Details |
| Component Carrier:Downlink:User Defined:SSS Power (dB) | Specifies the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB. Details |
| Component Carrier:Downlink:User Defined:PBCH Power (dB) | Specifies the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB. Details |
| Component Carrier:Downlink:User Defined:PDCCH Power (dB) | Specifies the power of physical downlink control channel (PDCCH) relative to the power of cell-specific reference signal. This value is expressed in dB. Details |
| Component Carrier:Downlink:User Defined:Number of Subframes | Specifies the number of unique subframes transmitted by the DUT. If you set the DL Ch Configuration Mode property to Test Model, this property will be set to 10 for FDD and 20 for TDD by default. Details |
| Component Carrier:Downlink:User Defined:PCFICH:CFI | Specifies the control format indicator (CFI) carried by physical control format indicator channel (PCFICH). CFI is used to compute the number of OFDM symbols which will determine the size of physical downlink control channel (PDCCH) within a subframe. Details |
| Component Carrier:Downlink:User Defined:PCFICH:Power (dB) | Specifies the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. Details |
| Component Carrier:Downlink:User Defined:PHICH:Resource (Ng) | Specifies the physical channel hybridARQ indicator channel (PHICH) resource value. This value is expressed in Ng. This property is used to calculate number of PHICH resource groups. Refer to section 6.9 of the 3GPP 36.211 specification for more information about PHICH. Details |
| Component Carrier:Downlink:User Defined:PHICH:Duration | Specifies the physical hybrid-ARQ indicator channel (PHICH) duration. Details |
| Component Carrier:Downlink:User Defined:PHICH:Power (dB) | Specifies the power of all BPSK symbols in a physical hybrid-ARQ indicator channel (PHICH) sequence. This value is expressed in dB. Details |
| Component Carrier:Downlink:User Defined:PDSCH:Number of PDSCHs | Specifies the number of physical downlink shared channel (PDSCH) allocations in a subframe. Details |
| Component Carrier:Downlink:User Defined:PDSCH:CW0 Modulation Type | Specifies the modulation type of codeword0 PDSCH allocation. Details |
| Component Carrier:Downlink:User Defined:PDSCH:RB Allocation | Specifies the resource blocks of the physical downlink shared channel (PDSCH) allocation. Details |
| Component Carrier:Downlink:User Defined:PDSCH:Power (dB) | Specifies the physical downlink shared channel (PDSCH) power level (Ra) relative to the power of the cell-specific reference signal. This value is expressed in dB. Measurement uses the Cell Specific Ratio property to calculate the Rb. Refer to section 3.3 of the 3GPP 36.521 specification for more information about Ra. Details |
| Component Carrier:Downlink:Test Model | Specifies the E-UTRA test model type when you set the DL Ch Configuration Mode property to Test Model. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. Details |
| Component Carrier:Auto Resource Block Detection Enabled | Specifies whether the values of the PUSCH Mod Type, PUSCH Num RB Clusters, PUSCH RB Offset, and PUSCH Num RBs properties are auto-detected by the measurement or if you specify the values of these properties. The measurement ignores this property, when you set the Link Direction property to Downlink. Details |
| Component Carrier:Auto DMRS Detection Enabled | Specifies whether you configure the values of the demodulation reference signal (DMRS) parameters, such as UL Group Hopping Enabled, UL Sequence Hopping Enabled, Cell ID, PUSCH n_DMRS_1, PUSCH n_DMRS_2, and PUSCH Delta SS properties, or if the values of these properties are auto-detected by the measurement. Details |
| Component Carrier:Uplink:Group Hopping Enabled | Specifies whether the sequence group number hopping for demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. Details |
| Component Carrier:Uplink:Sequence Hopping Enabled | Specifies whether the base sequence number hopping for the demodulation reference signal (DMRS) is enabled, as defined in section 5.5.1.3 of the 3GPP TS 36.211 specification. This property is only valid only when you set the PUSCH Num RBs property to a value greater than 5. Details |
| Component Carrier:Uplink:PUSCH:DMRS OCC Enabled | Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this property to TRUE for multi antenna cases. Details |
| Component Carrier:Uplink:PUSCH:n_DMRS_1 | Specifies the n_DMRS_1 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a frame. Details |
| Component Carrier:Uplink:PUSCH:Delta Sequence Shift | Specifies the physical uplink shared channel (PUSCH) delta sequence shift, which is used to calculate cyclic shift of the demodulation reference signal (DMRS). Refer to section 5.5.2.1.1 of the 3GPP TS 36.211 specification for more information about the PUSCH delta sequence shift. Details |
| Component Carrier:Uplink:PUSCH:Modulation Type | Specifies the modulation scheme used in the physical uplink shared channel (PUSCH) of the signal being measured. Details |
| Component Carrier:Uplink:PUSCH:Number of Resource Block Clusters | Specifies the number of resource allocation clusters, with each cluster including one or more consecutive resource blocks. Refer to 5.5.2.1.1 of the 3GPP TS 36.213 specification for more information about the number of channels in the physical uplink shared channel (PUSCH). Details |
| Component Carrier:Uplink:PUSCH:Resource Block Offset | Specifies the starting resource block number of a physical uplink shared channel (PUSCH) cluster. Details |
| Component Carrier:Uplink:PUSCH:Number of Resource Blocks | Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. Details |
| Component Carrier:Uplink:PUSCH:n_DMRS_2 | Specifies the n_DMRS_2 value, which is used to calculate the cyclic shift of the demodulation reference signal (DMRS) in a slot. The valid values for this property are, as defined in table 5.5.2.1.1-1 of the 3GPP TS 36.211 specification. Details |
| Component Carrier:Uplink:PUSCH:Cyclic Shift Field | Specifies the cyclic shift field in uplink-related DCI format. When the DMRS OCC enabled property is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with Tx Antenna to Analyze. Details |
| Component Carrier:Uplink:PUSCH:Power (dB) | Specifies the power of the physical uplink shared channel (PUSCH) data relative to PUSCH DMRS for a component carrier. This value is expressed in dB. Details |
| Component Carrier:Uplink:SRS:Enabled | Specifies whether the LTE signal getting measured contains SRS transmission. Details |
| Component Carrier:Uplink:SRS:Subframe Configuration | Specifies the SRS subframe configuration specified in the Table 5.5.3.3-1 of 3GPP 36.211 specification. It is a cell-specific property. This property defines the subframes that are reserved for SRS transmission in a given cell. Details |
| Component Carrier:Uplink:SRS:C_SRS | Specifies the cell-specific SRS bandwidth configuration CSRS . Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. Details |
| Component Carrier:Uplink:SRS:B_SRS | Specifies the UE specific SRS bandwidth configuration BSRS . Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. Details |
| Component Carrier:Uplink:SRS:I_SRS | Specifies the SRS configuration index ISRS . It is used to determine the SRS periodicity and SRS subframe offset. It is a UE specific attribute which defines whether the SRS is transmitted in the subframe reserved for SRS by SRS subframe configuration. Refer to 3GPP 36.213 specification for more details. Details |
| Component Carrier:Uplink:SRS:n_RRC | Specifies the SRS frequency domain position nRRC . Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. Details |
| Component Carrier:Uplink:SRS:n_SRS_CS | Specifies the cyclic shift value nSRS CS used for generating SRS base sequence. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. Details |
| Component Carrier:Uplink:SRS:b_hop | Specifies the SRS hopping bandwidth bhop. Frequency hopping for SRS signal is enabled when the value of SRS b_hop property is less than the value of SRS B_SRS property. Details |
| Component Carrier:Uplink:SRS:k_TC | Specifies the transmission comb index. If you set this property to 0, SRS is transmitted on the even subcarriers in the allocated region. If you set this property to 1, SRS is transmitted on the odd subcarriers in the allocated region. Details |
| Component Carrier:Uplink:SRS:Maximum UpPTS Enabled | Specifies SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. Details |
| Component Carrier:Uplink:SRS:Subframe1 N_RA | Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD. Details |
| Component Carrier:Uplink:SRS:Subframe6 N_RA | Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. Details |
| Component Carrier:Uplink:SRS:Power (dB) | Specifies the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. Details |
| Component Carrier:Sidelink:PSSCH:Modulation Type | Specifies the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. Details |
| Component Carrier:Sidelink:PSSCH:Resource Block Offset | Specifies the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. Details |
| Component Carrier:Sidelink:PSSCH:Number of Resource Blocks | Specifies the number of consecutive resource blocks in a physical sidelink shared channel (PSSCH) allocation. Details |
| Component Carrier:Sidelink:PSSCH:Power (dB) | Specifies the power of the physical sidelink shared channel (PSSCH) data relative to PSSCH DMRS for a component carrier. This value is expressed in dB. Details |
| Component Carrier:LAA:Starting Subframe | Specifies the starting subframe of an LAA burst. Details |
| Component Carrier:LAA:Number of Subframes | Specifies the number of subframes in an LAA burst including the starting subframe. Details |
| Component Carrier:LAA:Uplink Start Position | Specifies the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the 3GPP 36.211 specification for more information regarding LAA uplink start position. Details |
| Component Carrier:LAA:Uplink Ending Symbol | Specifies the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP 36.212 specification for more information regarding LAA uplink ending symbol. Details |
| Component Carrier:LAA:Downlink Starting Symbol | Specifies the starting symbol number in the first subframe of an LAA downlink burst. Refer to section 13A of the 3GPP 36.213 specification for more information regarding LAA downlink starting symbol. Details |
| Component Carrier:LAA:Downlink Number of Ending Symbols | Specifies the number of ending symbols in the last subframe of an LAA downlink burst. Refer to section 4.3 of the 3GPP 36.211 specification for more information regarding LAA downlink number of ending symbols. Details |
| Component Carrier:NB-IoT:NCell ID | Specifies the narrowband physical layer cell identity. Details |
| Component Carrier:NB-IoT:Uplink Subcarrier Spacing | Specifies the subcarrier bandwidth of an NB-IoT signal. This property specifies the spacing between adjacent subcarriers. Details |
| Component Carrier:NB-IoT:Auto NPUSCH Channel Detection Enabled | Specifies whether the values of the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties are auto-detected by the measurement or specified by you. Details |
| Component Carrier:NB-IoT:NPUSCH:Format | Specifies the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information. Details |
| Component Carrier:NB-IoT:NPUSCH:Starting Slot | Specifies the starting slot number of the NPUSCH burst. Details |
| Component Carrier:NB-IoT:NPUSCH:Tone Offset | Specifies the location of the starting subcarrier (tone) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). Details |
| Component Carrier:NB-IoT:NPUSCH:Number of Tones | Specifies the number of subcarriers (tones) within the 200 kHz bandwidth that is allocated to the narrowband physical uplink shared channel (NPUSCH). Details |
| Component Carrier:NB-IoT:NPUSCH:Modulation Type | Specifies the modulation type that is used by the narrowband physical uplink shared channel (NPUSCH). This property is valid when NPUSCH Num Tones is equal to 1 and NPUSCH Format is equal to 1. The modulation type for other configurations is defined in Table 10.1.3.2-1 of the 3GPP TS 36.211 specification. Details |
| Component Carrier:NB-IoT:NPUSCH:DMRS Base Sequence Mode | Specifies whether the NPUSCH DMRS Base Sequence Index property is computed by the measurement or specified by you. This property is valid when you set the NPUSCH Group Hopping Enabled property to False, the NPUSCH Format property to 1, and the NPUSCH Num Tones property to 3, 6, or 12. Details |
| Component Carrier:NB-IoT:NPUSCH:DMRS Base Sequence Index | Specifies the base sequence index of the Narrowband Physical Uplink Shared Channel (NPUSCH) DMRS as defined in section 10.1.4.1.2 of the 3GPP TS 36.211 specification. This property is valid when you set the NPUSCH Group Hopping Enabled property to False, the NPUSCH DMRS Base Sequence Mode property to Manual, and the NPUSCH Num Tones property to 3, 6, or 12. Details |
| Component Carrier:NB-IoT:NPUSCH:DMRS Cyclic Shift | Specifies the cyclic shift of the narrowband physical uplink shared channel (NPUSCH) DMRS as defined in Table 10.1.4.1.2-3 of the 3GPP TS 36.211 specification. This property is valid when you set the NPUSCH Num Tones property to 3 or 6. If the value of NPUSCH Num Tones property is 12, the NPUSCH DMRS Cyclic Shift property has a fixed value of 0. Details |
| Component Carrier:NB-IoT:NPUSCH:DMRS Group Hopping Enabled | Specifies whether the group hopping is enabled for narrowband physical uplink shared channel (NPUSCH) DMRS. This property is valid only when the NPUSCH Format is 1. Details |
| Component Carrier:NB-IoT:NPUSCH:DMRS Delta Sequence Shift | Specifies the delta sequence shift of the narrowband physical uplink shared channel (NPUSCH) DMRS, which is used to calculate the sequence shift pattern. This value is used to compute the sequence group number as defined in section 10.1.4.1.3 of the 3GPP TS 36.211 specification. This property is valid when you set the NPUSCH DMRS Group Hopping Enabled property to True. Details |
| Component Carrier:eMTC Analysis Enabled | Specifies whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. Details |
| List:Number of Steps | Specifies the number of active steps in a list. Details |
| List:Step:Timer Unit | Specifies the units in which List Step Timer Duration and List Step Timer Offset are specified. Details |
| List:Step:Timer Duration | Specifies the duration of a given list step in units specified by List Step Timer Unit. Details |
| List:Step:Timer Offset | Specifies the offset from the start of the step for which the measurements are computed. The unit for this property is specified by List Step Timer Unit. This property is valid only when you set the Digital Edge Source property to TimerEvent. Details |
| ModAcc:Measurement Enabled | Specifies whether to enable the ModAcc measurement. Details |
| ModAcc:Multicarrier Filter Enabled | Specifies whether to use a filter to suppress the interference from out of band emissions into the carriers being measured. Details |
| ModAcc:Multicarrier Time Synchronization Mode | Specifies the time synchronization mode used in uplink in the case of carrier aggregation. Details |
| ModAcc:Synchronization Mode | Specifies whether the measurement is performed from the frame or the slot boundary. Details |
| ModAcc:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the ModAcc Sync Mode property. This value is expressed in slots. Details |
| ModAcc:Measurement Length (slots) | Specifies the number of slots to be measured. This value is expressed in slots. Details |
| ModAcc:IQ Impairments:IQ Origin Offset Estimation Enabled | Specifies whether to estimate IQ origin offset. Details |
| ModAcc:IQ Impairments:IQ Mismatch Estimation Enabled | Specifies whether to estimate IQ mismatch such as gain imbalance, quadrature skew, and timing skew. Details |
| ModAcc:IQ Impairments:IQ Gain Imbalance Correction Enabled | Specifies whether to enable IQ gain imbalance correction. Details |
| ModAcc:IQ Impairments:IQ Quadrature Error Correction Enabled | Specifies whether to enable IQ quadrature error correction. Details |
| ModAcc:IQ Impairments:IQ Timing Skew Correction Enabled | Specifies whether to enable IQ timing skew correction. Details |
| ModAcc:Spectrum Inverted | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. Details |
| ModAcc:Channel Estimation Type | Specifies the method used for the channel estimation for the ModAcc measurement. The measurement ignores this property, when you set the Link Direction property to Downlink. Details |
| ModAcc:EVM Unit | Specifies the units of the EVM results. Details |
| ModAcc:FFT Window Type | Specifies the FFT window type used for the EVM calculation for the ModAcc measurement. Details |
| ModAcc:FFT Window Offset (%CP) | Specifies the position of the FFT window used to calculate the EVM. The offset is expressed as a percentage of the cyclic prefix length. If you set this property to 0, the EVM window starts at the end of cyclic prefix. If you set this property to 100, the EVM window starts at the beginning of cyclic prefix. Details |
| ModAcc:FFT Window Length (%CP) | Specifies the FFT window length (W). This value is expressed as a percentage of the cyclic prefix length. This property is used when you set the ModAcc FFT Window Type property to 3GPP, where it is needed to calculate the EVM using two different FFT window positions, Delta_C-W/2, and Delta_C+W/2. Refer to the Annexe E.3.2 of 3GPP 36.521 specification for more information. Details |
| ModAcc:Common Clock Source Enabled | Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. Details |
| ModAcc:EVM with Exclusion Period Enabled | Specifies whether to exclude some portion of the slots when calculating the EVM. This property is valid only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP TS 36.521-1 specification for more information about exclusion. The measurement ignores this property, when you set the Link Direction property to Downlink. Details |
| ModAcc:Spectral Flatness Condition | Specifies the frequency ranges at which to measure spectral flatness. The measurement ignores this property, when you set the Link Direction property to Downlink. Details |
| ModAcc:In-Band Emission Mask Type | Specifies the in-band emissions mask type to be used for measuring in-band emission margin (dB) and subblock in-Band emission margin (dB) results. Details |
| ModAcc:Averaging:Enabled | Specifies whether to enable averaging for the ModAcc measurement. Details |
| ModAcc:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ModAcc Averaging Enabled property to True. Details |
| ModAcc:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. Details |
| ModAcc:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| ModAcc:Pre-FFT Error Estimation Interval | Specifies the interval used for Pre-FFT Error Estimation. Details |
| ModAcc:Symbol Clock Error Estimation Enabled | Specifies whether to estimate symbol clock error. Details |
| ModAcc:Timing Tracking Enabled | Specifies whether timing tracking is enabled. Details |
| ModAcc:Phase Tracking Enabled | Specifies whether phase tracking is enabled. Details |
| ModAcc:Results:Mean RMS Composite EVM (% or dB) | Returns the mean value of the RMS EVMs calculated on all the configured channels, over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Maximum Peak Composite EVM (% or dB) | Returns the maximum value of the peak EVMs calculated on all the configured channels over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Mean RMS Composite Magnitude Error (% or dB) | Returns the RMS mean value of the composite magnitude error calculated over the slots specified by the ModAcc Meas Length property on all the configured channels. Details |
| ModAcc:Results:Maximum Peak Composite Magnitude Error (% or dB) | Returns the peak value of the composite magnitude error calculated over the slots specified by the ModAcc Meas Length property on all the configured channels. Details |
| ModAcc:Results:Mean RMS Composite Phase Error (deg) | Returns the RMS mean value of the composite phase error calculated over the slots specified by the ModAcc Meas Length property on all the configured channels. This value is expressed in degrees. This result is valid only when you set the Link Direction property to Uplink. Details |
| ModAcc:Results:Maximum Peak Composite Phase Error (deg) | Returns the peak value of phase error calculated over the slots specified by the ModAcc Meas Length property on all thee configured channels. This value is expressed in degrees. Details |
| ModAcc:Results:Peak Composite EVM Slot Index | Returns the slot index where the ModAcc maximum peak composite EVM occurs. Details |
| ModAcc:Results:Peak Composite EVM Symbol Index | Returns the symbol index of the ModAcc Results Max Pk Composite EVM property. Details |
| ModAcc:Results:Peak Composite EVM Subcarrier Index | Returns the subcarrier index where the maximum peak composite EVM for ModAcc occurs. Details |
| ModAcc:Results:Downlink:PDSCH:Mean RMS EVM (% or dB) | Returns the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:PDSCH:Mean RMS QPSK EVM (% or dB) | Returns the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:PDSCH:Mean RMS 16QAM EVM (% or dB) | Returns the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:PDSCH:Mean RMS 64QAM EVM (% or dB) | Returns the mean value of RMS EVMs calculated on all 64 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:PDSCH:Mean RMS 256QAM EVM (% or dB) | Returns the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:PDSCH:Mean RMS 1024QAM EVM (% or dB) | Returns the mean value of RMS EVMs calculated on all 1024 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS CSRS EVM (% or dB) | Returns the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS PSS EVM (% or dB) | Returns the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS SSS EVM (% or dB) | Returns the mean value of RMS EVMs calculated on secondary synchronization signal (SSS) channel over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS PBCH EVM (% or dB) | Returns the mean value of RMS EVMs calculated on PBCH channel over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS PCFICH EVM (% or dB) | Returns the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS PDCCH EVM (% or dB) | Returns the mean value of RMS EVMs calculated on PDCCH channel over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:Mean RMS PHICH EVM (% or dB) | Returns the mean value of RMS EVMs calculated on PHICH channel over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Downlink:RS Transmit Power (dBm) | Returns the mean value of power calculated on cell-specific reference signal (CSRS) resource elements over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Downlink:OFDM Symbol Tx Power (dBm) | Returns the mean value of power calculated in one OFDM symbol over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Downlink:Detected Cell ID | Returns the detected cell ID value. Details |
| ModAcc:Results:In-Band Emission Margin (dB) | Returns the in-band emission margin. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range1-Max to Range1-Min (dB) | Returns the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Range1. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range2-Max to Range2-Min (dB) | Returns the peak-to-peak ripple of the EVM equalizer coefficients within the frequency Measurement Offset parameter. This value is expressed in dB. Details |
| ModAcc:Results:Spectral Flatness:Range1-Max to Range2-Min (dB) | Returns the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed in dB. Details |
| ModAcc:Results:Uplink:PUSCH:Mean RMS Data EVM (% or dB) | Returns the mean value of the RMS EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:PUSCH:Maximum Peak Data EVM (% or dB) | Returns the maximum value of the peak EVMs calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:PUSCH:Mean RMS DMRS EVM (% or dB) | Returns the mean value of the RMS EVMs calculated on the PUSCH DMRS over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:PUSCH:Maximum Peak DMRS EVM (% or dB) | Returns the maximum value of the peak EVMs calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:PUSCH:Mean Data Power (dBm) | Returns the mean value of the power calculated on the physical uplink shared channel (PUSCH) data symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Uplink:PUSCH:Mean DMRS Power (dBm) | Returns the mean value of the power calculated on the PUSCH DMRS over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Uplink:SRS:Mean RMS EVM (% or dB) | Returns the mean value of RMS EVMs calculated on the SRS symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:SRS:Mean Power (dBm) | Returns the mean value of power calculated on SRS over the slots specified by the ModAcc Meas Length property. This values is expressed in dBm. Details |
| ModAcc:Results:Uplink:NPUSCH:Mean RMS Data EVM (% or dB) | Returns the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:NPUSCH:Maximum Peak Data EVM (% or dB) | Returns the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:NPUSCH:Mean RMS DMRS EVM (% or dB) | Returns the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:NPUSCH:Maximum Peak DMRS EVM (% or dB) | Returns the maximum value of peak EVMs calculated on NPUSCH DMRS over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Uplink:NPUSCH:Mean Data Power (dBm) | Returns the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Uplink:NPUSCH:Mean DMRS Power (dBm) | Returns the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) DMRS over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Uplink:Spectral Flatness:Range2-Max to Range1-Min (dB) | Returns the peak-to-peak ripple of the EVM equalizer coefficients from frequency Measurement Offset parameter to frequency Range1. This value is expressed in dB. Details |
| ModAcc:Results:Uplink:Subblock In-Band Emission Margin (dB) | Returns the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB. Details |
| ModAcc:Results:Sidelink:PSSCH:Mean RMS Data EVM (% or dB) | Returns the mean value of the RMS EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Sidelink:PSSCH:Maximum Peak Data EVM (% or dB) | Returns the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Sidelink:PSSCH:Mean RMS DMRS EVM (% or dB) | Returns the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Sidelink:PSSCH:Maximum Peak DMRS EVM (% or dB) | Returns the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length property. Details |
| ModAcc:Results:Sidelink:PSSCH:Mean Data Power (dBm) | Returns the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Sidelink:PSSCH:Mean DMRS Power (dBm) | Returns the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Details |
| ModAcc:Results:Mean Frequency Error (Hz) | Returns the estimated carrier frequency offset averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in Hz. Details |
| ModAcc:Results:Maximum Peak Frequency Error (Hz) | Returns the estimated maximum carrier frequency offset per slot in case of Uplink and per subframe in case of Downlink over the slots specified by the ModAcc Meas Length property. This value is expressed in Hz. Details |
| ModAcc:Results:Mean IQ Origin Offset (dBc) | Returns the estimated I/Q origin offset averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in dBc. Details |
| ModAcc:Results:Maximum Peak IQ Origin Offset (dBc) | Returns the estimated maximum IQ origin offset over the slots specified by the ModAcc Meas Length property. This value is expressed in dBc. Details |
| ModAcc:Results:Mean IQ Gain Imbalance (dB) | Returns the estimated I/Q gain imbalance averaged over the measurement length. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured. This value is expressed in dB. Details |
| ModAcc:Results:Mean Quadrature Error (deg) | Returns the estimated quadrature error averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in degrees. Details |
| ModAcc:Results:Mean IQ Timing Skew (s) | Returns the estimated IQ timing skew averaged over measured length. IQ timing skew is the difference between the group delay of the in-phase (I) and quadrature (Q) components of the signal. This value is expressed in seconds. Details |
| ModAcc:Results:Mean Time Offset (s) | Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of ModAcc Sync Mode property. This value is expressed in seconds. Details |
| ModAcc:Results:Mean Symbol Clock Error (ppm) | Returns the estimated symbol clock error averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in ppm. Details |
| ModAcc:Results:Subblock Mean IQ Origin Offset (dBc) | Returns the estimated I/Q origin offset averaged over the slots specified by the ModAcc Meas Length property in the subblock. This value is expressed in dBc. Details |
| ModAcc:Results:Subblock Mean IQ Gain Imbalance (dB) | Returns the estimated I/Q gain imbalance averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in dB. The I/Q gain imbalance is the ratio of the amplitude of the I component to the Q component of the I/Q signal being measured in the subblock. This result is valid only when you set the Link Direction property to Uplink and the Transmitter Architecture property to LO per Subblock. Otherwise, this parameter returns NaN, as measurement of this result is currently not supported. Details |
| ModAcc:Results:Subblock Mean Quadrature Error (deg) | Returns the estimated quadrature error averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in degrees. Quadrature error is a measure of the skewness of the I component with respect to the Q component of the I/Q signal being measured in the subblock. Details |
| ACP:Measurement Enabled | Specifies whether to enable the ACP measurement. Details |
| ACP:Subblock Integration Bandwidth (Hz) | Specifies the integration bandwidth of the subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Details |
| ACP:Component Carrier:Integration Bandwidth (Hz) | Specifies the integration bandwidth of the component carrier (CC). This value is expressed in Hz. Details |
| ACP:Offset:Configurable Number of Offsets Enabled | Specifies whether the number of offsets is computed by measurement or configured by you. Details |
| ACP:Offset:Number of UTRA Offsets | Specifies the number of universal terrestrial radio access (UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled property to True. Details |
| ACP:Offset:Number of EUTRA Offsets | Specifies the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions, when you set the ACP Configurable Number of Offset Enabled property to True. Details |
| ACP:Offset:EUTRA Offset Definition | Specifies the evolved universal terrestrial radio access (E-UTRA) offset channel definition. Details |
| ACP:Offset:Number of GSM Offsets | Specifies the number of GSM adjacent channel offsets to be configured when you set the CC Bandwidth to 200.0 k and the ACP Configurable Number of Offset Enabled property to True. Details |
| ACP:Offset:Frequency (Hz) | Specifies the offset frequency of an offset channel. This value is expressed in Hz. When you set the Link Direction property to Uplink, the offset frequency is computed from the center of a reference component carrier/subblock to the center of the nearest RBW filter of the offset channel. When you set the Link Direction property to Downlink, the offset frequency is computed from the center of the closest component carrier to the center of the nearest RBW filter of the offset channel. Details |
| ACP:Offset:Integration Bandwidth (Hz) | Specifies the integration bandwidth of an offset carrier. This value is expressed in Hz. Details |
| ACP:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| ACP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the ACP RBW Auto property to False. This value is expressed in Hz. Details |
| ACP:RBW Filter:Type | Specifies the shape of the RBW filter. Details |
| ACP:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| ACP:Sweep Time:Interval (s) | Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| ACP:Power Units | Specifies the units for absolute power. Details |
| ACP:Measurement Method | Specifies the method for performing the ACP measurement. Details |
| ACP:Noise Calibration:Mode | Specifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:Noise Calibration:Averaging:Auto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. Details |
| ACP:Noise Calibration:Averaging:Count | Specifies the averaging count used for noise calibration when you set the ACP Noise Cal Averaging Auto property to False. Details |
| ACP:Noise Compensation:Enabled | Specifies whether RFmx compensates for the instrument noise while performing the measurement when you set the ACP Noise Cal Mode property to Auto, or when you set the ACP Noise Cal Mode property to Manual and the ACP Meas Mode property to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:Noise Compensation:Type | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:Averaging:Enabled | Specifies whether to enable averaging for the ACP measurement. Details |
| ACP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True. Details |
| ACP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. Details |
| ACP:Measurement Mode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the ACP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| ACP:FFT:Overlap Mode | Specifies the overlap mode when you set the ACP Meas Method property to Sequential FFT. In Sequential FFT method, the measurement divides all the acquired samples into smaller FFT chunks of equal size. Then the FFT is computed for each chunk. The resultant FFTs are averaged to get the spectrum used to compute the ACP. Details |
| ACP:FFT:Overlap (%) | Specifies the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property value when you set the ACP Meas Method property to Sequential FFT and the ACP FFT Overlap Mode property to User Defined. Details |
| ACP:Advanced:IF Output Power Offset Auto | Specifies whether the measurement computes an appropriate IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This property is valid only when you set the ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Near IF Output Power Offset (dB) | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is valid only when you set the ACP IF Output Pwr Offset Auto property to False and ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Far IF Output Power Offset (dB) | Specifies the offset that is needed to adjust the IF output power levels for the offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is valid only when you set the ACP IF Output Pwr Offset Auto property to False and ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Sequential FFT Size | Specifies the FFT size, when you set the ACP Meas Method property to Sequential FFT. Details |
| ACP:Amplitude Correction Type | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| ACP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. Details |
| ACP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| ACP:Results:Total Aggregated Power (dBm or dBm/Hz) | Returns the sum of powers of all the frequency bins over the integration bandwidths of all subblocks. The sum includes the power in inter-carrier gaps within a subblock but it does not include the power in subblock gaps. Details |
| ACP:Results:Subblock Center Frequency (Hz) | Returns the absolute center frequency of the subblock, which is the center of the subblock integration bandwidth. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Details |
| ACP:Results:Subblock Integration Bandwidth (Hz) | Returns the integration bandwidth used in calculating the power of the subblock. This value is expressed in Hz. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Details |
| ACP:Results:Subblock Power (dBm or dBm/Hz) | Returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. Details |
| ACP:Results:Component Carrier:Absolute Power (dBm or dBm/Hz) | Returns the power measured over the integration bandwidth of the carrier. The carrier power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Component Carrier:Relative Power (dB) | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Details |
| ACP:Results:Lower Offset:Absolute Power (dBm or dBm/Hz) | Returns the lower (negative) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Lower Offset:Relative Power (dB) | Returns the power in lower (negative) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. Details |
| ACP:Results:Upper Offset:Absolute Power (dBm or dBm/Hz) | Returns the upper (positive) offset channel power. If this offset is not applicable for the intra-band non-contiguous type of carrier aggregation, a NaN is returned. The offset channel power is reported in dBm when you set the ACP Pwr Units property to dBm, and in dBm/Hz when you set the ACP Pwr Units property to dBm/Hz. Details |
| ACP:Results:Upper Offset:Relative Power (dB) | Returns the power in the upper (positive) offset channel relative to the total aggregated power. This value is expressed in dB. If this offset is not applicable for the intra band non contagious type of carrier aggregation, a Nan is returned.. Refer to the 3GPP TS 36.521 specification for more information about the applicability of the offset channel. Details |
| CHP:Measurement Enabled | Specifies whether to enable the channel power measurement. Details |
| CHP:Integration Bandwidth Type | Specifies the integration bandwidth (IBW) type used to measure the power of the acquired signal. Integration bandwidth is the frequency interval over which the power in each frequency bin is added to measure the total power in that interval. Details |
| CHP:Subblock Integration Bandwidth (Hz) | Specifies the integration bandwidth of a subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Details |
| CHP:Component Carrier:Integration Bandwidth (Hz) | Specifies the integration bandwidth of a component carrier. This value is expressed in Hz. Details |
| CHP:RBW Filter:Auto Bandwidth | Specifies whether the CHP measurement computes the RBW. Details |
| CHP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the CHP RBW Auto property to False. This value is expressed in Hz. Details |
| CHP:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| CHP:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| CHP:Sweep Time:Interval (s) | Specifies the sweep time when you set the CHP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| CHP:Noise Calibration:Mode | Specifies whether the noise calibration and measurement is performed automatically by the measurement or initiated by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Noise Calibration:Averaging:Auto | Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. Details |
| CHP:Noise Calibration:Averaging:Count | Specifies the averaging count used for noise calibration when you set the CHP Noise Cal Averaging Auto property to False. Details |
| CHP:Noise Compensation:Enabled | Specifies whether RFmx compensates for the instrument noise when performing the measurement. To compensate for instrument noise when performing a CHP measurement, set the CHP Noise Cal Mode property to Auto, or set the CHP Noise Cal Mode property to Manual and the CHP Meas Mode property to Measure. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Noise Compensation:Type | Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Averaging:Enabled | Specifies whether to enable averaging for the CHP measurement. Details |
| CHP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. Details |
| CHP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for CHP measurement. Details |
| CHP:Measurement Mode | Specifies whether the measurement calibrates the noise floor of analyzer or performs the CHP measurement. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. Details |
| CHP:Amplitude Correction Type | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| CHP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. Details |
| CHP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| CHP:Results:Total Aggregated Power (dBm) | Returns the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps. Details |
| CHP:Results:Subblock Frequency (Hz) | Returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock<n>" as the selector string to read this result. Details |
| CHP:Results:Subblock Integration Bandwidth (Hz) | Returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Details |
| CHP:Results:Subblock Power (dBm) | Returns the sum of total power of all the frequency bins over the integration bandwidth of the subblock. This value includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Details |
| CHP:Results:Component Carrier:Absolute Power (dBm) | Returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Details |
| CHP:Results:Component Carrier:Relative Power (dB) | Returns the component carrier power relative to its subblock power. This value is expressed in dB. Details |
| OBW:Measurement Enabled | Specifies whether to enable the OBW measurement. Details |
| OBW:Span (Hz) | Returns the frequency search space to find the OBW. This value is expressed in Hz. Details |
| OBW:RBW Filter:Auto Bandwidth | Specifies whether the measurement computes the RBW. Details |
| OBW:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter used to sweep the acquired signal, when you set the OBW RBW Auto property to False. This value is expressed in Hz. Details |
| OBW:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| OBW:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| OBW:Sweep Time:Interval (s) | Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. Details |
| OBW:Averaging:Enabled | Specifies whether to enable averaging for the OBW measurement. Details |
| OBW:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. Details |
| OBW:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. Details |
| OBW:Amplitude Correction Type | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| OBW:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. Details |
| OBW:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| OBW:Results:Occupied Bandwidth (Hz) | Returns the bandwidth that occupies 99 percentage of the total power of the signal within a carrier/subblock. This value is expressed in Hz. Details |
| OBW:Results:Absolute Power (dBm) | Returns the total power measured in the carrier/subblock. This value is expressed in dBm. Details |
| OBW:Results:Start Frequency (Hz) | Returns the start frequency of the carrier/subblock. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation: Stop frequency - Start frequency = Occupied bandwidth Details |
| OBW:Results:Stop Frequency (Hz) | Returns the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Details |
| SEM:Measurement Enabled | Specifies whether to enable the SEM measurement. Details |
| SEM:Uplink Mask Type | Specifies the spectrum emission mask used in the measurement for uplink. Each mask type refers to a different Network Signalled (NS) value. General CA Class B, CA_NS_04, CA_NC_NS_01, CA_NS_09, and CA_NS_10 refers to the carrier aggregation case. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2.1 of the 3GPP 36.521 specification for more information about standard-defined mask types. Details |
| SEM:Downlink Mask Type | Specifies the limits to be used in the measurement for downlink. Refer to section 6.6.3 of the 3GPP 36.141 specification for more information about standard-defined mask types. Details |
| SEM:Sidelink Mask Type | Specifies the spectrum emission mask used in the measurement for sidelink. Each mask type refers to a different Network Signalled (NS) value. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.6.2 of the 3GPP 36.521 specification for more information about standard-defined mask types. Details |
| SEM:Downlink:Delta F_Maximum (Hz) | Specifies the stop frequency for the last offset segment to be used in the measurement. This value is expressed in Hz. Details |
| SEM:Downlink:Aggregated Maximum Power (dBm) | Specifies the aggregated maximum output power of all transmit antenna connectors. This value is expressed in dBm. Refer to the Section 6.6.3 of 3GPP 36.141 specification for more details. Details |
| SEM:Subblock Integration Bandwidth (Hz) | Returns the integration bandwidth of the subblock. This value is expressed in Hz. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. Details |
| SEM:Subblock Aggregated Channel Bandwidth (Hz) | Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. Details |
| SEM:Component Carrier:Integration Bandwidth (Hz) | Returns the integration bandwidth of a component carrier. This value is expressed in Hz. Details |
| SEM:Component Carrier:Maximum Output Power (dBm) | Specifies the maximum output power, Pmax,c, per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of 3GPP 36.141 specification. Details |
| SEM:Offset:Number of Offsets | Specifies the number of SEM offset segments. Details |
| SEM:Offset:Start Frequency (Hz) | Specifies the start frequency of an offset segment relative to the CC Bandwidth edge (single carrier) or SEM Subblock Aggregated Ch BW edge (multi-carrier). This value is expressed in Hz. Details |
| SEM:Offset:Stop Frequency (Hz) | Specifies the stop frequency of an offset segment relative to the CC Bandwidth edge (single carrier) or SEM Subblock Aggregated Ch BW edge (multi-carrier). This value is expressed in Hz. Details |
| SEM:Offset:Sideband | Specifies whether the offset segment is present either on one side or on both sides of a carrier. Details |
| SEM:Offset:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of an RBW filter used to sweep an acquired offset segment. This value is expressed in Hz. Details |
| SEM:Offset:RBW Filter:Type | Specifies the shape of a digital RBW filter. Details |
| SEM:Offset:Bandwidth Integral | Specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. Details |
| SEM:Offset:Limit Fail Mask | Specifies the criteria to determine the measurement fail status. Details |
| SEM:Offset:Absolute Limit:Start (dBm) | Specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. Details |
| SEM:Offset:Absolute Limit:Stop (dBm) | Specifies the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. Details |
| SEM:Offset:Relative Limit:Start (dB) | Specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. Details |
| SEM:Offset:Relative Limit:Stop (dB) | Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. Details |
| SEM:Sweep Time:Auto | Specifies whether the measurement computes the sweep time. Details |
| SEM:Sweep Time:Interval (s) | Specifies the sweep time when you set the SEM Sweep Time Auto property to False. This value is expressed in seconds. Details |
| SEM:Averaging:Enabled | Specifies whether to enable averaging for the SEM measurement. Details |
| SEM:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True. Details |
| SEM:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. Details |
| SEM:Amplitude Correction Type | Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. Details |
| SEM:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. Details |
| SEM:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| SEM:Results:Total Aggregated Power (dBm) | Returns the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. Details |
| SEM:Results:Measurement Status | Returns the overall measurement status based on the standard mask type that you configure in the SEM Standard Mask Type property. Details |
| SEM:Results:Subblock Center Frequency (Hz) | Returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from the left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Details |
| SEM:Results:Subblock Integration Bandwidth (Hz) | Returns the integration bandwidth of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Details |
| SEM:Results:Subblock Power (dBm) | Returns the power measured over the integration bandwidth of the subblock. This value is expressed in dBm. Details |
| SEM:Results:Component Carrier:Absolute Integrated Power (dBm) | Returns the sum of powers of all the frequency bins over the integration bandwidth of the carrier. This value is expressed in dBm. Details |
| SEM:Results:Component Carrier:Relative Integrated Power (dB) | Returns the sum of powers of all the frequency bins over the integration bandwidth of the component carrier power relative to its subblock power. This value is expressed in dB. Details |
| SEM:Results:Component Carrier:Absolute Peak Power (dBm) | Returns the peak power in the component carrier. This value is expressed in dBm. Details |
| SEM:Results:Component Carrier:Peak Frequency (Hz) | Returns the frequency at which the peak power occurs in the component carrier. This value is expressed in Hz. Details |
| SEM:Results:Lower Offset:Measurement Status | Indicates the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM Standard Mask Type property. Details |
| SEM:Results:Lower Offset:Absolute Integrated Power (dBm) | Returns the lower (negative) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Relative Integrated Power (dB) | Returns the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Absolute Peak Power (dBm) | Returns the peak power in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Relative Peak Power (dB) | Returns the peak power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Details |
| SEM:Results:Lower Offset:Margin (dB) | Returns the margin from the standard-defined absolute limit mask for the lower (negative) offset. Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Margin Absolute Power (dBm) | Returns the power at which the margin occurs in the lower (negative) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Margin Relative Power (dB) | Returns the power at which the margin occurs in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Lower Offset:Margin Frequency (Hz) | Returns the frequency at which the margin occurs in the lower (negative) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Details |
| SEM:Results:Upper Offset:Measurement Status | Returns the measurement status based on the user-configured standard measurement limits and the failure criteria specified by Limit Fail Mask for the upper (positive) offset. For intra-band non-contiguous case, the offset segment may be truncated or discarded based on offset overlap rules defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. Details |
| SEM:Results:Upper Offset:Absolute Integrated Power (dBm) | Returns the upper (positive) offset segment power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Details |
| SEM:Results:Upper Offset:Relative Integrated Power (dB) | Returns the power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Absolute Peak Power (dBm) | Returns the power in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Details |
| SEM:Results:Upper Offset:Relative Peak Power (dB) | Returns the peak power in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Details |
| SEM:Results:Upper Offset:Margin (dB) | Returns the margin from the absolute limit mask for the upper (positive) offset. The Margin is defined as the minimum difference between the limit mask and the spectrum. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Details |
| SEM:Results:Upper Offset:Margin Absolute Power (dBm) | Returns the power at which the margin occurs in the upper (positive) offset segment. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dBm. Details |
| SEM:Results:Upper Offset:Margin Relative Power (dB) | Returns the power at which the margin occurs in the upper (positive) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB. Details |
| SEM:Results:Upper Offset:Margin Frequency (Hz) | Returns the frequency at which the margin occurs in the upper (positive) offset. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in Hz. Details |
| PVT:Measurement Enabled | Specifies whether to enable the power versus time (PVT) measurement. Details |
| PVT:Measurement Method | Specifies the method for performing the power versus time (PVT) measurement. Details |
| PVT:Averaging:Enabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. Details |
| PVT:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the PVT Averaging Enabled property to True. Details |
| PVT:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement. Details |
| PVT:OFF Power Exclusion Before (s) | Specifies the time excluded from the Off region before the burst. This value is expressed in seconds. Details |
| PVT:OFF Power Exclusion After (s) | Specifies the time excluded from the Off region after the burst. This value is expressed in seconds. Details |
| PVT:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. Details |
| PVT:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| PVT:Results:Measurement Status | Returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Details |
| PVT:Results:Mean Absolute OFF Power Before (dBm) | Returns the mean power in the segment before the captured burst. The segment is defined as one subframe prior to the burst for the FDD mode and 10 SC-FDMA symbols prior to the burst for the TDD mode. This value is expressed in dBm. Details |
| PVT:Results:Mean Absolute OFF Power After (dBm) | Returns the mean power in the segment after the captured burst. This value is expressed in dBm. The segment is defined as one subframe long, excluding a transient period of 20 micro seconds at the beginning. Details |
| PVT:Results:Mean Absolute ON Power | Returns the average power of the subframes within the captured burst. This value is expressed in dBm. The average power excludes the transient period of 20 micro seconds at the beginning. Details |
| PVT:Results:Burst Width (s) | Returns the width of the captured burst. This value is expressed in seconds. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Details |
| SlotPhase:Measurement Enabled | Specifies whether to enable the SlotPhase measurement. Details |
| SlotPhase:Synchronization Mode | Specifies whether the measurement is performed from the frame or the slot boundary. Details |
| SlotPhase:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Mode property. Details |
| SlotPhase:Measurement Length (slots) | Specifies the number of slots to be measured. This value is expressed in slots. Details |
| SlotPhase:Exclusion Period Enabled | Specifies whether to exclude some portions of the slots when calculating the phase. This property is valid only when there is a power change at the slot boundary. Refer to section 6.5.2.1A of the 3GPP 36.521-1 specification for more information about the exclusion. Details |
| SlotPhase:Common Clock Source Enabled | Specifies whether the same Reference Clock is used for local oscillator and the digital-to-analog converter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. Details |
| SlotPhase:Spectrum Inverted | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. Details |
| SlotPhase:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. Details |
| SlotPhase:Results:Maximum Phase Discontinuity (deg) | Returns the maximum value of phase difference at the slot boundaries within the SlotPhase Meas Length. This values is expressed in degrees. Details |
| SlotPower:Measurement Enabled | Specifies whether to enable the SlotPower measurement. Details |
| SlotPower:Measurement Offset (subframes) | Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. Details |
| SlotPower:Measurement Length (subframes) | Specifies the number of subframes to be measured. This value is expressed in subframe. Details |
| SlotPower:Common Clock Source Enabled | Specifies whether the same Reference Clock is used for the local oscillator and the digital-to-analog converter in the transmitter. When the same Reference Clock is used, the carrier frequency offset is proportional to Sample Clock error. Details |
| SlotPower:Spectrum Inverted | Specifies whether the spectrum of the measured signal is inverted. The inversion happens when the I and the Q components of the baseband complex signal are swapped. Details |
| SlotPower:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. Details |
| Advanced:Auto Level Initial Reference Level (dBm) | Specifies the initial reference level that the RFmxLTE Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm. Details |
| Advanced:Acquisition Bandwidth Optimization Enabled | Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. Details |
| Advanced:Transmitter Architecture | Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. Details |
| Advanced: Center Frequency for Limits (Hz) | Specifies the frequency that determines the SEM mask, IBE limits, and spectral flatness ranges. If you do not set a value for this property, the measurement internally uses the Center Frequency for determining SEM mask, IBE limits, and spectral flatness ranges. This value is expressed in Hz. Details |
| Result Fetch Timeout (s) | Specifies the time to wait before results are available in the RFmxLTE Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. Details |
