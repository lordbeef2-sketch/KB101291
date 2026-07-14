# NI DOCUMENT BUNDLE: rfmx-cdma2k-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-cdma2k-prop start=1 end=104 -->
<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600000.html language=enus -->
## TOPIC 00001: rfmxcdma2kprop/attr600000.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600000.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

Selector String Property

**Short Name:**Selector String

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the selector strings used to access all subsequent properties in this instance of the property node.

For configuration properties, you can specify the signal name and any required repeated capability instances, such as "offset0", for the property.

For results, you can specify the signal name, result name, and any required repeated capability instances for the result.

Examples:

"channel0"

"signal::sig1/channel0"

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

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600001.html language=enus -->
## TOPIC 00002: rfmxcdma2kprop/attr600001.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600001.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Frequency |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600002.html language=enus -->
## TOPIC 00003: rfmxcdma2kprop/attr600002.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600002.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Reference Level |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600003.html language=enus -->
## TOPIC 00004: rfmxcdma2kprop/attr600003.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600003.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0 dB.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure External Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600004.html language=enus -->
## TOPIC 00005: rfmxcdma2kprop/attr600004.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600004.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the trigger type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **None**.

| None (0) | No Reference Trigger is configured. |
| --- | --- |
| Digital Edge (1) | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge (2) | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Source property. |
| Software (3) | The Reference Trigger is not asserted until a software trigger occurs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600008.html language=enus -->
## TOPIC 00006: rfmxcdma2kprop/attr600008.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600008.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level Property

Trigger:IQ Power Edge:Level Property

**Short Name:**IQ Power Edge Level

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the power level at which the device triggers. This value is expressed in dB when the [IQ Power Edge Level Type](attr600fff.html) property is set to **Relative** and in dBm when the IQ Power Edge Level Type property is set to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the [Trigger Type](attr600004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60000d.html language=enus -->
## TOPIC 00007: rfmxcdma2kprop/attr60000d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60000d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Link Direction Property

Link Direction Property

**Short Name:**Link Direction

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the link direction of the received signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Uplink**.

| Downlink (0) | CDMA2k measurement uses 3GPP CDMA2k forward link direction also known as downlink direction to measure the received signal. |
| --- | --- |
| Uplink (1) | CDMA2k measurement uses 3GPP CDMA2k reverse link direction also known as uplink direction to measure the received signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600011.html language=enus -->
## TOPIC 00008: rfmxcdma2kprop/attr600011.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600011.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Radio Configuration Property

Radio Configuration Property

**Short Name:**Radio Configuration

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the radio configuration for the channel.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **RC3**.

| RC1 (0) | If Link Direction property is set to Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and reverse supplemental code channels (R-SCCHs). If Link Direction property is set to Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |
| --- | --- |
| RC2 (1) | If Link Direction property is set to Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and R-SCCHs. If Link Direction property is set to Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |
| RC3 (2) | If Link Direction property is set to Uplink, Radio configuration 3 includes BPSK, R-FCH, and reverse supplemental channels (R-SCHs). If Link Direction property is set to Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |
| RC4 (3) | If Link Direction property is set to Uplink, Radio configuration 4 includes BPSK, R-FCH, and R-SCHs. If Link Direction property is set to Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |
| RC5 (4) | If Link Direction property is set to Uplink, Radio configuration 5 is not supported and gives invalid results. If Link Direction property is set to Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Radio Configuration |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600012.html language=enus -->
## TOPIC 00009: rfmxcdma2kprop/attr600012.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600012.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Channel:Configuration Mode Property

Channel:Configuration Mode Property

**Short Name:**Channel Configuration Mode

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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
| High-level VIs | RFmxCDMA2k Configure Channel Configuration Mode |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600016.html language=enus -->
## TOPIC 00010: rfmxcdma2kprop/attr600016.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600016.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Channel:User Defined:Number of Channels Property

Channel:User Defined:Number of Channels Property

**Short Name:**Num Channels

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of user-defined channels. This property is used only when you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Number of Channels |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600017.html language=enus -->
## TOPIC 00011: rfmxcdma2kprop/attr600017.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600017.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Channel:User Defined:Walsh Code Length Property

Channel:User Defined:Walsh Code Length Property

**Short Name:**Walsh Code Length

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This property is used only when you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**.

Use "channel<
n
>" as the Selector Strings to configure or read this property.

The default value is 64.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure User Defined Channel |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600018.html language=enus -->
## TOPIC 00012: rfmxcdma2kprop/attr600018.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600018.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Channel:User Defined:Walsh Code Number Property

Channel:User Defined:Walsh Code Number Property

**Short Name:**Walsh Code Number

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the Walsh code number of a specific user-defined channel. This property is used only when you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**.

Use "channel<
n
>" as the Selector Strings to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure User Defined Channel |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600019.html language=enus -->
## TOPIC 00013: rfmxcdma2kprop/attr600019.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600019.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Channel:User Defined:Branch Property

Channel:User Defined:Branch Property

**Short Name:**Branch

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the branch on which a specific user-defined channel is mapped. This property is used only when you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**.

Use "channel<
n
>" as the Selector Strings to configure or read this property.

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
| High-level VIs | RFmxCDMA2k Configure User Defined Channel |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60001e.html language=enus -->
## TOPIC 00014: rfmxcdma2kprop/attr60001e.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60001e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60001e.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Spreading:Uplink:Long Code Mask Property

Spreading:Uplink:Long Code Mask Property

**Short Name:**UL Spreading Long Code Mask

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the long code mask for reverse link spreading.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Uplink Spreading |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600020.html language=enus -->
## TOPIC 00015: rfmxcdma2kprop/attr600020.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600020.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Spreading:Downlink:PN Offset (64 chips) Property

Spreading:Downlink:PN Offset (64 chips) Property

**Short Name:**DL Spreading PN Offset (64 chips)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specified the PN offset in increments of 64 chips for forward link.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr600ffd.html language=enus -->
## TOPIC 00016: rfmxcdma2kprop/attr600ffd.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr600ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr600ffd.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601000.html language=enus -->
## TOPIC 00017: rfmxcdma2kprop/attr601000.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601000.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Enabled Property

ACP:Measurement Enabled Property

**Short Name:**ACP Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601008.html language=enus -->
## TOPIC 00018: rfmxcdma2kprop/attr601008.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601008.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Number of Offsets Property

ACP:Offset:Number of Offsets Property

**Short Name:**ACP Num Offsets

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of offset channels.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 2.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Number of Offsets |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60100e.html language=enus -->
## TOPIC 00019: rfmxcdma2kprop/attr60100e.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60100e.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Integration Bandwidth (Hz) Property

ACP:Offset:Integration Bandwidth (Hz) Property

**Short Name:**ACP Offset IBW (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601012.html language=enus -->
## TOPIC 00020: rfmxcdma2kprop/attr601012.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601012.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Method Property

ACP:Measurement Method Property

**Short Name:**ACP Meas Method

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the method for performing the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Normal**.

| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| --- | --- |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| Sequential FFT (2) | The ACP measurement acquires I/Q the samples specified by the ACP Sweep Time. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed for each these chunks. The resultant FFTs are averaged to get the spectrum used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Use this method to optimize the ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Properties Supported Values ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Num Analysis Threads 1 Note For multi-span FFT, the averaging count should be 1. |
| Properties | Supported Values |
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
| High-level VIs | RFmxCDMA2k ACP Configure Measurement Method |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601014.html language=enus -->
## TOPIC 00021: rfmxcdma2kprop/attr601014.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601014.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Number of Analysis Threads Property

ACP:Number of Analysis Threads Property

**Short Name:**ACP Num Analysis Threads

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the maximum number of threads used for parallelism for the ACP measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601015.html language=enus -->
## TOPIC 00022: rfmxcdma2kprop/attr601015.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601015.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Count Property

ACP:Averaging:Count Property

**Short Name:**ACP Averaging Count

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of acquisitions used for averaging when you set the [ACP Averaging Enabled](attr601016.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601016.html language=enus -->
## TOPIC 00023: rfmxcdma2kprop/attr601016.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601016.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Enabled Property

ACP:Averaging:Enabled Property

**Short Name:**ACP Averaging Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable averaging for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The ACP measurement uses the value of the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601018.html language=enus -->
## TOPIC 00024: rfmxcdma2kprop/attr601018.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601018.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Type Property

ACP:Averaging:Type Property

**Short Name:**ACP Averaging Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

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
| High-level VIs | RFmxCDMA2k ACP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60101b.html language=enus -->
## TOPIC 00025: rfmxcdma2kprop/attr60101b.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60101b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60101b.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:RBW Filter:Auto Bandwidth Property

ACP:RBW Filter:Auto Bandwidth Property

**Short Name:**ACP RBW Auto

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether the measurement computes the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the RBW that you specify in the ACP RBW property. |
| --- | --- |
| True (1) | The measurement computes the RBW. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60101c.html language=enus -->
## TOPIC 00026: rfmxcdma2kprop/attr60101c.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60101c.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:RBW Filter:Bandwidth (Hz) Property

ACP:RBW Filter:Bandwidth (Hz) Property

**Short Name:**ACP RBW (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [ACP RBW Auto](attr60101b.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60101d.html language=enus -->
## TOPIC 00027: rfmxcdma2kprop/attr60101d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60101d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60101d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:RBW Filter:Type Property

ACP:RBW Filter:Type Property

**Short Name:**ACP RBW Filter Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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
| High-level VIs | RFmxCDMA2k ACP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60101e.html language=enus -->
## TOPIC 00028: rfmxcdma2kprop/attr60101e.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60101e.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Sweep Time:Auto Property

ACP:Sweep Time:Auto Property

**Short Name:**ACP Sweep Time Auto

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time that you specify in the ACP Sweep Time property. |
| --- | --- |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60101f.html language=enus -->
## TOPIC 00029: rfmxcdma2kprop/attr60101f.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60101f.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Sweep Time:Interval (s) Property

ACP:Sweep Time:Interval (s) Property

**Short Name:**ACP Sweep Time (s)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the sweep time when you set the [ACP Sweep Time Auto](attr60101e.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.0016667 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60102d.html language=enus -->
## TOPIC 00030: rfmxcdma2kprop/attr60102d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60102d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Relative Power (dB) Property

ACP:Results:Lower Offset:Relative Power (dB) Property

**Short Name:**ACP Results Lower Offset Rel Pwr (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the lower offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601035.html language=enus -->
## TOPIC 00031: rfmxcdma2kprop/attr601035.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601035.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Near IF Output Power Offset (dB) Property

ACP:Advanced:Near IF Output Power Offset (dB) Property

**Short Name:**ACP Near IF Output Power Offset (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the [ACP Meas Method](attr601012.html) property to **Dynamic Range** and set the [ACP IF Output Power Offset Auto](attr601034.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10 dB.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601038.html language=enus -->
## TOPIC 00032: rfmxcdma2kprop/attr601038.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601038.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Sequential FFT Size Property

ACP:Advanced:Sequential FFT Size Property

**Short Name:**ACP Sequential FFT Size

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the FFT size, when you set the [ACP Meas Method](attr601012.html) property to **Sequential FFT**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 512.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr601039.html language=enus -->
## TOPIC 00033: rfmxcdma2kprop/attr601039.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr601039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr601039.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap Mode Property

ACP:FFT:Overlap Mode Property

**Short Name:**ACP FFT Overlap Mode

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60103a.html language=enus -->
## TOPIC 00034: rfmxcdma2kprop/attr60103a.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60103a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60103a.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ACP:FFT:Overlap (%) Property

ACP:FFT:Overlap (%) Property

**Short Name:**ACP FFT Overlap (%)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the number of samples to overlap between consecutive chunks while performing FFT.

This value is expressed as a percentage of [ACP Sequential FFT Size](attr601038.html) property when you set the [ACP Meas Method](attr601012.html) property to **Sequential FFT**.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr603000.html language=enus -->
## TOPIC 00035: rfmxcdma2kprop/attr603000.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr603000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr603000.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

CHP:Measurement Enabled Property

CHP:Measurement Enabled Property

**Short Name:**CHP Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr603002.html language=enus -->
## TOPIC 00036: rfmxcdma2kprop/attr603002.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr603002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr603002.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

CHP:Integration Bandwidth (Hz) Property

CHP:Integration Bandwidth (Hz) Property

**Short Name:**CHP IBW (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the CHP carrier integration bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606004.html language=enus -->
## TOPIC 00037: rfmxcdma2kprop/attr606004.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606004.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Span (Hz) Property

OBW:Span (Hz) Property

**Short Name:**OBW Span (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the frequency span of the OBW measurement. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606006.html language=enus -->
## TOPIC 00038: rfmxcdma2kprop/attr606006.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606006.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Count Property

OBW:Averaging:Count Property

**Short Name:**OBW Averaging Count

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](attr606007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606007.html language=enus -->
## TOPIC 00039: rfmxcdma2kprop/attr606007.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606007.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Enabled Property

OBW:Averaging:Enabled Property

**Short Name:**OBW Averaging Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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
| High-level VIs | RFmxCDMA2k OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606009.html language=enus -->
## TOPIC 00040: rfmxcdma2kprop/attr606009.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606009.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Type Property

OBW:Averaging:Type Property

**Short Name:**OBW Averaging Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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
| High-level VIs | RFmxCDMA2k OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60600d.html language=enus -->
## TOPIC 00041: rfmxcdma2kprop/attr60600d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60600d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60600d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Bandwidth (Hz) Property

OBW:RBW Filter:Bandwidth (Hz) Property

**Short Name:**OBW RBW (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [OBW RBW Auto](attr60600c.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 30 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60600e.html language=enus -->
## TOPIC 00042: rfmxcdma2kprop/attr60600e.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60600e.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Type Property

OBW:RBW Filter:Type Property

**Short Name:**OBW RBW Filter Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | No RBW filtering is performed. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a Flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606010.html language=enus -->
## TOPIC 00043: rfmxcdma2kprop/attr606010.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606010.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Sweep Time:Interval (s) Property

OBW:Sweep Time:Interval (s) Property

**Short Name:**OBW Sweep Time (s)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the sweep time when you set the [OBW Sweep Time Auto](attr60600f.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.001667 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606013.html language=enus -->
## TOPIC 00044: rfmxcdma2kprop/attr606013.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606013.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Occupied Bandwidth (Hz) Property

OBW:Results:Occupied Bandwidth (Hz) Property

**Short Name:**OBW Results Occupied BW (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606014.html language=enus -->
## TOPIC 00045: rfmxcdma2kprop/attr606014.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606014.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Absolute Power (dBm) Property

OBW:Results:Absolute Power (dBm) Property

**Short Name:**OBW Results Abs Pwr (dBm)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the absolute power measured in the OBW. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606015.html language=enus -->
## TOPIC 00046: rfmxcdma2kprop/attr606015.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606015.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Start Frequency (Hz) Property

OBW:Results:Start Frequency (Hz) Property

**Short Name:**OBW Results Start Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the start frequency of the OBW. This value is expressed in Hz.

The OBW is calculated using the following formula: *OBW = Stop Frequency - Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr606016.html language=enus -->
## TOPIC 00047: rfmxcdma2kprop/attr606016.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr606016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr606016.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Stop Frequency (Hz) Property

OBW:Results:Stop Frequency (Hz) Property

**Short Name:**OBW Results Stop Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the stop frequency of the OBW. This value is expressed in Hz.

The OBW is calculated using the following formula: *OBW = Stop Frequency - Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608000.html language=enus -->
## TOPIC 00048: rfmxcdma2kprop/attr608000.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608000.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Measurement Enabled Property

SEM:Measurement Enabled Property

**Short Name:**SEM Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608005.html language=enus -->
## TOPIC 00049: rfmxcdma2kprop/attr608005.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608005.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Carrier:Integration Bandwidth (Hz) Property

SEM:Carrier:Integration Bandwidth (Hz) Property

**Short Name:**SEM Carrier IBW (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the SEM carrier integration bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60800b.html language=enus -->
## TOPIC 00050: rfmxcdma2kprop/attr60800b.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60800b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60800b.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Number of Offsets Property

SEM:Offset:Number of Offsets Property

**Short Name:**SEM Num Offsets

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the number of SEM offset segments.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60800c.html language=enus -->
## TOPIC 00051: rfmxcdma2kprop/attr60800c.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60800c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60800c.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Bandwidth Integral Property

SEM:Offset:Bandwidth Integral Property

**Short Name:**SEM Offset BW Integral

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the bandwidth integral for a specific offset segment.

A bandwidth integral greater than 1 indicates a RBW filter of a narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment.

Use the following equation to calculate the value of the offset segment RBW: *offset segment RBW* = *RBW* * *BW integral*

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608014.html language=enus -->
## TOPIC 00052: rfmxcdma2kprop/attr608014.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608014.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Start Frequency (Hz) Property

SEM:Offset:Start Frequency (Hz) Property

**Short Name:**SEM Offset Start Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608015.html language=enus -->
## TOPIC 00053: rfmxcdma2kprop/attr608015.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608015.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Stop Frequency (Hz) Property

SEM:Offset:Stop Frequency (Hz) Property

**Short Name:**SEM Offset Stop Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608018.html language=enus -->
## TOPIC 00054: rfmxcdma2kprop/attr608018.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608018.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:RBW Filter:Type Property

SEM:Offset:RBW Filter:Type Property

**Short Name:**SEM Offset RBW Filter Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the type of RBW filter used to sweep the offset segment.

Use "offset<
n
>" as the Selector Strings to read this result.

The default value is **Gaussian**.

| FFT Based (0) | No RBW filtering is performed. |
| --- | --- |
| Gaussian (1) | The RBW filter has a Gaussian response. |
| Flat (2) | The RBW filter has a flat response. |
| Synch Tuned - 4 (3) | The RBW filter has a response of a 4-pole synchronously tuned filter. |
| Synch Tuned - 5 (4) | The RBW filter has a response of a 5-pole synchronously tuned filter. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60801e.html language=enus -->
## TOPIC 00055: rfmxcdma2kprop/attr60801e.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60801e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60801e.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Count Property

SEM:Averaging:Count Property

**Short Name:**SEM Averaging Count

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of acquisitions used for averaging when you set the [SEM Averaging Enabled](attr60801f.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60801f.html language=enus -->
## TOPIC 00056: rfmxcdma2kprop/attr60801f.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60801f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60801f.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Enabled Property

SEM:Averaging:Enabled Property

**Short Name:**SEM Averaging Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

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
| High-level VIs | RFmxCDMA2k SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608021.html language=enus -->
## TOPIC 00057: rfmxcdma2kprop/attr608021.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608021.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Type Property

SEM:Averaging:Type Property

**Short Name:**SEM Averaging Type

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **RMS**.

| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608026.html language=enus -->
## TOPIC 00058: rfmxcdma2kprop/attr608026.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608026.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Sweep Time:Interval (s) Property

SEM:Sweep Time:Interval (s) Property

**Short Name:**SEM Sweep Time (s)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the sweep time when you set the [SEM Sweep Time Auto](attr608025.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.001667 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SEM Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608027.html language=enus -->
## TOPIC 00059: rfmxcdma2kprop/attr608027.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608027.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:All Traces Enabled Property

SEM:All Traces Enabled Property

**Short Name:**SEM All Traces Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608029.html language=enus -->
## TOPIC 00060: rfmxcdma2kprop/attr608029.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608029.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Measurement Status Property

SEM:Results:Measurement Status Property

**Short Name:**SEM Results Meas Status

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |
| --- | --- |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60802d.html language=enus -->
## TOPIC 00061: rfmxcdma2kprop/attr60802d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60802d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60802d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Absolute Integrated Power (dBm) Property

SEM:Results:Carrier:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Carrier Abs Integrated Pwr (dBm)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60803b.html language=enus -->
## TOPIC 00062: rfmxcdma2kprop/attr60803b.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60803b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60803b.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Margin Relative Power (dB) Property

SEM:Results:Lower Offset:Margin Relative Power (dB) Property

**Short Name:**SEM Results Lower Offset Margin Rel Pwr (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60803c.html language=enus -->
## TOPIC 00063: rfmxcdma2kprop/attr60803c.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60803c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60803c.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Margin Frequency (Hz) Property

SEM:Results:Lower Offset:Margin Frequency (Hz) Property

**Short Name:**SEM Results Lower Offset Margin Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60803d.html language=enus -->
## TOPIC 00064: rfmxcdma2kprop/attr60803d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60803d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60803d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Measurement Status Property

SEM:Results:Lower Offset:Measurement Status Property

**Short Name:**SEM Results Lower Offset Meas Status

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Indicates the lower offset segment measurement status based on measurement limits specified by the standard.

Use "offset<
n
>" as the Selector Strings to read this result.

| Fail (0) | The lower offset segment measurement fails according to the measurement limits specified by the standard. |
| --- | --- |
| Pass (1) | The lower offset segment measurement passes according to the measurement limits specified by the standard. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608041.html language=enus -->
## TOPIC 00065: rfmxcdma2kprop/attr608041.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608041.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608041.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Absolute Integrated Power (dBm) Property

SEM:Results:Upper Offset:Absolute Integrated Power (dBm) Property

**Short Name:**SEM Results Upper Offset Abs Integrated Pwr (dBm)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the power measured in the upper (positive) offset segment. This value is expressed in dB.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608043.html language=enus -->
## TOPIC 00066: rfmxcdma2kprop/attr608043.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608043.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608043.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Absolute Peak Power (dBm) Property

SEM:Results:Upper Offset:Absolute Peak Power (dBm) Property

**Short Name:**SEM Results Upper Offset Abs Pk Pwr (dBm)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608044.html language=enus -->
## TOPIC 00067: rfmxcdma2kprop/attr608044.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608044.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608044.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Relative Peak Power (dB) Property

SEM:Results:Upper Offset:Relative Peak Power (dB) Property

**Short Name:**SEM Results Upper Offset Rel Pk Pwr (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608045.html language=enus -->
## TOPIC 00068: rfmxcdma2kprop/attr608045.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608045.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608045.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Peak Frequency (Hz) Property

SEM:Results:Upper Offset:Peak Frequency (Hz) Property

**Short Name:**SEM Results Upper Offset Pk Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608046.html language=enus -->
## TOPIC 00069: rfmxcdma2kprop/attr608046.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608046.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608046.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin (dB) Property

SEM:Results:Upper Offset:Margin (dB) Property

**Short Name:**SEM Results Upper Offset Margin (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).

Use "offset<
n
>" as the Selector Strings to read this result.

| Setting Specified by the Standard | Margin Description |
| --- | --- |
| Absolute | Returns the margin with reference to the absolute limit mask. |
| Relative | Returns the margin with reference to the relative limit mask. |
| Abs AND Rel | Returns the margin as the maximum of the margin referenced to the absolute and relative limit masks. |
| Abs OR Rel | Returns the margin as the minimum of the margin referenced to the absolute and relative limit masks. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608047.html language=enus -->
## TOPIC 00070: rfmxcdma2kprop/attr608047.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608047.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608047.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Absolute Power (dBm) Property

SEM:Results:Upper Offset:Margin Absolute Power (dBm) Property

**Short Name:**SEM Results Upper Offset Margin Abs Pwr (dBm)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr608049.html language=enus -->
## TOPIC 00071: rfmxcdma2kprop/attr608049.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr608049.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr608049.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Margin Frequency (Hz) Property

SEM:Results:Upper Offset:Margin Frequency (Hz) Property

**Short Name:**SEM Results Upper Offset Margin Freq (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.

Use "offset<
n
>" as the Selector Strings to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr60804a.html language=enus -->
## TOPIC 00072: rfmxcdma2kprop/attr60804a.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr60804a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr60804a.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Measurement Status Property

SEM:Results:Upper Offset:Measurement Status Property

**Short Name:**SEM Results Upper Offset Meas Status

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Indicates the upper offset measurement status based on measurement limits set by the standard.

Use "offset<
n
>" as the Selector Strings to read this result.

| Fail (0) | The lower offset segment measurement fails according to the measurement limits specified by this standard. |
| --- | --- |
| Pass (1) | The lower offset segment measurement passes according to the measurement limits specified by this standard. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611006.html language=enus -->
## TOPIC 00073: rfmxcdma2kprop/attr611006.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611006.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Offset (slots) Property

ModAcc:Measurement Offset (slots) Property

**Short Name:**ModAcc Meas Offset (slots)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [ModAcc Sync Mode](attr611005.html) property. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0. The valid values are 1 to 16, inclusive. The sum of the ModAcc measurement offset and the ModAcc measurement length must be less than or equal to 16.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611008.html language=enus -->
## TOPIC 00074: rfmxcdma2kprop/attr611008.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611008.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:IQ Offset Removal Enabled Property

ModAcc:IQ Offset Removal Enabled Property

**Short Name:**ModAcc IQ Offset Removal Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to remove the I/Q offset before an EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | I/Q offset is not removed before the EVM measurement. |
| --- | --- |
| True (1) | I/Q offset is removed before the EVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611010.html language=enus -->
## TOPIC 00075: rfmxcdma2kprop/attr611010.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611010.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Multi Carrier Filter:Enabled Property

ModAcc:Multi Carrier Filter:Enabled Property

**Short Name:**ModAcc MC-Filter Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables multi carrier filter for ModAcc measurement. |
| --- | --- |
| True (1) | Enables multi carrier filter for ModAcc measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611020.html language=enus -->
## TOPIC 00076: rfmxcdma2kprop/attr611020.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611020.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:RMS EVM (%) Property

ModAcc:Results:RMS EVM (%) Property

**Short Name:**ModAcc Results RMS EVM (%)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the RMS EVM of the composite signal. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61102d.html language=enus -->
## TOPIC 00077: rfmxcdma2kprop/attr61102d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61102d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak Active CDE Walsh Code Length Property

ModAcc:Results:Peak Active CDE Walsh Code Length Property

**Short Name:**ModAcc Results Pk Active CDE Walsh Code Length

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the Walsh code length of the channel corresponding to the value that the [ModAcc Results Pk Active CDE](attr61102c.html) property returns.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61102f.html language=enus -->
## TOPIC 00078: rfmxcdma2kprop/attr61102f.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61102f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61102f.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak Active CDE Walsh Code Number Property

ModAcc:Results:Peak Active CDE Walsh Code Number Property

**Short Name:**ModAcc Results Pk Active CDE Walsh Code Number

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the Walsh code number of the channel corresponding to the value that the [ModAcc Results Pk Active CDE](attr61102c.html) property returns.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611030.html language=enus -->
## TOPIC 00079: rfmxcdma2kprop/attr611030.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611030.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Slot Timing Error (s) Property

ModAcc:Results:Slot Timing Error (s) Property

**Short Name:**ModAcc Results Slot Timing Error (s)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the measured timing error from the beginning of the acquisition to the location of the first slot acquired. This value is expressed in seconds.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611033.html language=enus -->
## TOPIC 00080: rfmxcdma2kprop/attr611033.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611033.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Chip Rate Error (ppm) Property

ModAcc:Results:Chip Rate Error (ppm) Property

**Short Name:**ModAcc Results Chip Rate Error (ppm)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the chip rate error. This value is expressed in parts per million (ppm).

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611035.html language=enus -->
## TOPIC 00081: rfmxcdma2kprop/attr611035.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611035.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Walsh Code Length Property

ModAcc:Results:Detected Channel:Walsh Code Length Property

**Short Name:**ModAcc Results Detected Walsh Code Length

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the Walsh code length of the detected channel. If you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**, the property returns the Walsh code length of the configured channel.

Use "channel<
n
>" as the Selector Strings to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611036.html language=enus -->
## TOPIC 00082: rfmxcdma2kprop/attr611036.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611036.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611036.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Walsh Code Number Property

ModAcc:Results:Detected Channel:Walsh Code Number Property

**Short Name:**ModAcc Results Detected Walsh Code Number

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the Walsh code number of the detected channel. If you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**, the property returns the Walsh code number of the configured channel.

Use "channel<
n
>" as the Selector Strings to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611037.html language=enus -->
## TOPIC 00083: rfmxcdma2kprop/attr611037.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611037.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Detected Channel:Branch Property

ModAcc:Results:Detected Channel:Branch Property

**Short Name:**ModAcc Results Detected Branch

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the branch of the detected channel. If you set the [Channel Configuration Mode](attr600012.html) property to **User Defined**, the property returns the branch of the configured channel.

Use "channel<
n
>" as the Selector Strings to read this property.

| I (0) | The signal modulated on the in-phase branch. |
| --- | --- |
| Q (1) | The signal modulated on the quadrature branch. |
| I and Q (2) | The signal modulated on the in-phase branch and quadrature branch. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr611039.html language=enus -->
## TOPIC 00084: rfmxcdma2kprop/attr611039.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr611039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr611039.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Peak Active CDE Branch Property

ModAcc:Results:Peak Active CDE Branch Property

**Short Name:**ModAcc Results Pk Active CDE Branch

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the branch of the channel corresponding to the value that the [ModAcc Results Pk Active CDE](attr61102c.html) property returns.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results.

| I (0) | The signal is modulated on the in-phase branch. |
| --- | --- |
| Q (1) | The signal is modulated on the quadrature branch. |
| I and Q (2) | Complex modulated signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612002.html language=enus -->
## TOPIC 00085: rfmxcdma2kprop/attr612002.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612002.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Measurement Length (chips) Property

QEVM:Measurement Length (chips) Property

**Short Name:**QEVM Meas Length (chips)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of chips used for a single measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1536. The valid values are 700 to 2500, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k QEVM Configure Measurement Length |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612003.html language=enus -->
## TOPIC 00086: rfmxcdma2kprop/attr612003.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612003.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Averaging:Enabled Property

QEVM:Averaging:Enabled Property

**Short Name:**QEVM Averaging Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable averaging for the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The averaging is disabled for the measurement. |
| --- | --- |
| True (1) | The averaging is enabled for the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k QEVM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612004.html language=enus -->
## TOPIC 00087: rfmxcdma2kprop/attr612004.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612004.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Averaging:Count Property

QEVM:Averaging:Count Property

**Short Name:**QEVM Averaging Count

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the number of measurements used for averaging when you set the [QEVM Averaging Enabled](../rfmxcdma2kprop/attr612003.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default values is 10. The valid values are 1 to 10000, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k QEVM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612005.html language=enus -->
## TOPIC 00088: rfmxcdma2kprop/attr612005.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612005.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Spectrum Inverted Property

QEVM:Spectrum Inverted Property

**Short Name:**QEVM Spectrum Inverted

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement spectrum is normal. |
| --- | --- |
| True (1) | The measurement spectrum is inverted. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612006.html language=enus -->
## TOPIC 00089: rfmxcdma2kprop/attr612006.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612006.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:IQ Offset Removal Enabled Property

QEVM:IQ Offset Removal Enabled Property

**Short Name:**QEVM IQ Offset Removal Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to remove I/Q offset before QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | I/Q offset is not removed before the QEVM measurement. |
| --- | --- |
| True (1) | I/Q offset is removed before the QEVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612007.html language=enus -->
## TOPIC 00090: rfmxcdma2kprop/attr612007.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612007.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:IQ Gain Imbalance Removal Enabled Property

QEVM:IQ Gain Imbalance Removal Enabled Property

**Short Name:**QEVM IQ Gain Imbalance Removal Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to remove I/Q gain imbalance before QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | I/Q gain imbalance is not removed before the QEVM measurement. |
| --- | --- |
| True (1) | I/Q gain imbalance is removed before the QEVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612008.html language=enus -->
## TOPIC 00091: rfmxcdma2kprop/attr612008.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612008.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:IQ Quadrature Error Removal Enabled Property

QEVM:IQ Quadrature Error Removal Enabled Property

**Short Name:**QEVM IQ Quadrature Error Removal Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to remove I/Q quadrature error before QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | I/Q quadrature error is not removed before the QEVM measurement. |
| --- | --- |
| True (1) | I/Q quadrature error is removed before the QEVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612009.html language=enus -->
## TOPIC 00092: rfmxcdma2kprop/attr612009.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612009.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Receive Filter Enabled Property

QEVM:Receive Filter Enabled Property

**Short Name:**QEVM Receive Filter Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the received filter for the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | Disables received filtering for the QEVM measurement. |
| --- | --- |
| True (1) | Enables received filtering for the QEVM measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61200a.html language=enus -->
## TOPIC 00093: rfmxcdma2kprop/attr61200a.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61200a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61200a.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:All Traces Enabled Property

QEVM:All Traces Enabled Property

**Short Name:**QEVM All Traces Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61200b.html language=enus -->
## TOPIC 00094: rfmxcdma2kprop/attr61200b.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61200b.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Number of Analysis Threads Property

QEVM:Number of Analysis Threads Property

**Short Name:**QEVM Num Analysis Threads

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the maximum number of threads used for parallelism for the QEVM measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

The default value is 1. Valid values range from 0 to 10, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61200d.html language=enus -->
## TOPIC 00095: rfmxcdma2kprop/attr61200d.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61200d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61200d.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean RMS EVM (%) Property

QEVM:Results:Mean RMS EVM (%) Property

**Short Name:**QEVM Results Mean RMS EVM (%)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the mean averaged RMS EVM of the received signal. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61200e.html language=enus -->
## TOPIC 00096: rfmxcdma2kprop/attr61200e.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61200e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61200e.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum RMS EVM (%) Property

QEVM:Results:Maximum RMS EVM (%) Property

**Short Name:**QEVM Results Max RMS EVM (%)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the maximum RMS EVM of the received signal. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61200f.html language=enus -->
## TOPIC 00097: rfmxcdma2kprop/attr61200f.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61200f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61200f.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean Peak EVM (%) Property

QEVM:Results:Mean Peak EVM (%) Property

**Short Name:**QEVM Results Mean Pk EVM (%)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612010.html language=enus -->
## TOPIC 00098: rfmxcdma2kprop/attr612010.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612010.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum Peak EVM (%) Property

QEVM:Results:Maximum Peak EVM (%) Property

**Short Name:**QEVM Results Max Pk EVM (%)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the maximum peak EVM of the received signal. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612015.html language=enus -->
## TOPIC 00099: rfmxcdma2kprop/attr612015.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612015.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Mean Frequency Error (Hz) Property

QEVM:Results:Mean Frequency Error (Hz) Property

**Short Name:**QEVM Results Mean Freq Error (Hz)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the mean averaged frequency error of the received signal. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr612018.html language=enus -->
## TOPIC 00100: rfmxcdma2kprop/attr612018.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr612018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr612018.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum I/Q Origin Offset (dB) Property

QEVM:Results:Maximum I/Q Origin Offset (dB) Property

**Short Name:**QEVM Results Max I/Q Origin Offset (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the maximum origin offset of the received signal. This value is expressed in dB.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61201a.html language=enus -->
## TOPIC 00101: rfmxcdma2kprop/attr61201a.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61201a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61201a.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

QEVM:Results:Maximum I/Q Gain Imbalance (dB) Property

QEVM:Results:Maximum I/Q Gain Imbalance (dB) Property

**Short Name:**QEVM Results Max I/Q Gain Imbalance (dB)

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr613005.html language=enus -->
## TOPIC 00102: rfmxcdma2kprop/attr613005.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr613005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr613005.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

CDA:Base Spreading Factor Property

CDA:Base Spreading Factor Property

**Short Name:**CDA Base Spreading Factor

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the base spreading factor used to calculate the code domain power traces.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr613007.html language=enus -->
## TOPIC 00103: rfmxcdma2kprop/attr613007.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr613007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr613007.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

CDA:Measurement Channel:Walsh Code Number Property

CDA:Measurement Channel:Walsh Code Number Property

**Short Name:**CDA Meas Ch Walsh Code Number

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies the Walsh code number of a channel subject to channel specific analysis.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0. The valid values are 0 to 63, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k CDA Configure Measurement Channel |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-cdma2k-prop path=rfmxcdma2kprop/attr61300b.html language=enus -->
## TOPIC 00104: rfmxcdma2kprop/attr61300b.html

- bundle_id: `rfmx-cdma2k-prop`
- source_path: `rfmxcdma2kprop/attr61300b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-cdma2k-prop/raw/resource/enus/rfmxcdma2kprop/attr61300b.html
- document_id: `rfmx-cdma2k-prop`
- page_type: `leaf`
- content_type: ``

CDA:IQ Offset Removal Enabled Property

CDA:IQ Offset Removal Enabled Property

**Short Name:**CDA IQ Offset Removal Enabled

Property of [RFmxCDMA2k](crfmxcdma2k.html)

Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | I/Q offset is not removed before the CDA measurement. |
| --- | --- |
| True (1) | I/Q offset is removed before the CDA measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |
