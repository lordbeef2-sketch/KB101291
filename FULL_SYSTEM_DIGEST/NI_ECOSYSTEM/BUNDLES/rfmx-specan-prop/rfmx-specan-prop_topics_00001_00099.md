# NI DOCUMENT BUNDLE: rfmx-specan-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-specan-prop start=1 end=99 -->
<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100001.html language=enus -->
## TOPIC 00001: Center Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100001.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100001.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Center Frequency (Hz) Property

**Short Name:**Center Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the expected carrier frequency of the RF signal that needs to be acquired. This value is expressed in Hz. The signal analyzer tunes to this frequency.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Configure Frequency |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100002.html language=enus -->
## TOPIC 00002: Reference Level Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100002.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Reference Level Property

**Short Name:**Reference Level

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the reference level which represents the maximum expected power of the RF input signal. This value is configured in dBm for RF devices and as V<sub>pk-pk</sub> for baseband devices.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Configure Reference Level |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100003.html language=enus -->
## TOPIC 00003: External Attenuation (dB) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100003.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

External Attenuation (dB) Property

**Short Name:**External Attenuation (dB)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the attenuation of a switch (or cable) connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Configure External Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100005.html language=enus -->
## TOPIC 00004: Trigger:Digital Edge:Source Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100005.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](attr100004.html) property to **Digital Edge**.

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
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100006.html language=enus -->
## TOPIC 00005: Trigger:Digital Edge:Edge Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100006.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the active edge for the trigger. This property is used only when you set the [Trigger Type](attr100004.html) property to **Digital Edge**.

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
| High-level VIs | RFmxSpecAn Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10000a.html language=enus -->
## TOPIC 00006: Trigger:Delay (s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10000a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100ff7.html language=enus -->
## TOPIC 00007: List:Step:Timer Offset (s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100ff7.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100ff7.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

List:Step:Timer Offset (s) Property

**Short Name:**List Step Timer Offset (s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the time offset from the start of the step for which the measurements are computed. This value is expressed in seconds. This property is valid only when you set the [Digital Edge Source](attr100005.html) property to **TimerEvent**.

You need to use a selector string to configure or read this property for the list step instance.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100ffd.html language=enus -->
## TOPIC 00008: Selected Ports Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100ffd.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxSpecAn](crfmxspecan.html)

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

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr100fff.html language=enus -->
## TOPIC 00009: Trigger:IQ Power Edge:Level Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr100fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr100fff.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level Type Property

**Short Name:**IQ Power Edge Level Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the reference for the [IQ Power Edge Level](attr100008.html) property. The IQ Power Edge Level Type property is used only when you set the [Trigger Type](attr100004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Absolute**.

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

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101000.html language=enus -->
## TOPIC 00010: ACP:Measurement Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101000.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Measurement Enabled Property

**Short Name:**ACP Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101002.html language=enus -->
## TOPIC 00011: ACP:Carrier:Number of Carriers Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101002.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Carrier:Number of Carriers Property

**Short Name:**ACP Num Carriers

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the number of carriers.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn ACP Configure Number of Carriers |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10100a.html language=enus -->
## TOPIC 00012: ACP:Offset:Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10100a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Frequency (Hz) Property

**Short Name:**ACP Offset Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the center or edge frequency of the offset channel, relative to the center frequency of the closest carrier as determined by the [ACP Offset Freq Definition](attr101037.html) property. This value is expressed in Hz. The sign of offset frequency is ignored and the [ACP Offset Sideband](attr10100b.html) property determines whether the upper, lower, or both offsets are measured.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn ACP Configure Offset, RFmxSpecAn ACP Configure Offset (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10100e.html language=enus -->
## TOPIC 00013: ACP:Offset:Integration Bandwidth (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10100e.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:Integration Bandwidth (Hz) Property

**Short Name:**ACP Offset IBW (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn ACP Configure Carrier and Offsets, RFmxSpecAn ACP Configure Offset Integration Bandwidth, RFmxSpecAn ACP Configure Offset Integration Bandwidth (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101011.html language=enus -->
## TOPIC 00014: ACP:Offset:RRC Filter:Alpha Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101011.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Offset:RRC Filter:Alpha Property

**Short Name:**ACP Offset RRC Alpha

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the roll-off factor for the root-raised-cosine (RRC) filter.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn ACP Configure Offset RRC Filter, RFmxSpecAn ACP Configure Offset RRC Filter (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101018.html language=enus -->
## TOPIC 00015: ACP:Averaging:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101018.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Averaging:Type Property

**Short Name:**ACP Averaging Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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
| High-level VIs | RFmxSpecAn ACP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101020.html language=enus -->
## TOPIC 00016: ACP:Noise Compensation:Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101020.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101020.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Noise Compensation:Enabled Property

**Short Name:**ACP Noise Comp Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether RFmx compensates for the instrument noise while performing the measurement when you set the [ACP Noise Cal Mode](attr101041.html) property to **Auto**, or when you set the ACP Noise Cal Mode property to **Manual** and [ACP Meas Mode](attr10103d.html) to **Measure**. Refer to the [Noise Compensation Algorithm](/csh?topicname=rfmxspecan/noise_compensation_algorithm.html) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Disables noise compensation. |
| --- | --- |
| True (1) | Enables noise compensation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn ACP Configure Noise Compensation Enabled |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101022.html language=enus -->
## TOPIC 00017: ACP:Results:Total Carrier Power (dBm or dBm/Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101022.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Total Carrier Power (dBm or dBm/Hz) Property

**Short Name:**ACP Results Total Carrier Pwr

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the total integrated power, in dBm, of all the active carriers measured when you set the [ACP Power Units](attr101013.html) property to **dBm**.

Returns the power spectral density, in dBm/Hz, based on the power in all the active carriers measured when you set the ACP Power Units property to **dBm/Hz**.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn ACP Fetch Total Carrier Power |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101023.html language=enus -->
## TOPIC 00018: ACP:Results:Frequency Resolution (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101023.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Frequency Resolution (Hz) Property

**Short Name:**ACP Results Freq Resolution (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the frequency bin spacing of the spectrum acquired by the measurement. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn ACP Fetch Frequency Resolution |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr101026.html language=enus -->
## TOPIC 00019: ACP:Results:Carrier:Absolute Power (dBm or dBm/Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr101026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr101026.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Carrier:Absolute Power (dBm or dBm/Hz) Property

**Short Name:**ACP Results Carrier Abs Pwr

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the measured carrier power.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

The carrier power is reported in dBm when you set the [ACP Power Units](attr101013.html) property to **dBm**, and in dBm/Hz when you set the ACP Power Units property to **dBm/Hz**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn ACP Fetch Carrier Measurement |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10102f.html language=enus -->
## TOPIC 00020: ACP:Results:Upper Offset:Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10102f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10102f.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Upper Offset:Frequency (Hz) Property

**Short Name:**ACP Results Upper Offset Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the center frequency of the upper offset channel relative to the center frequency of the closest carrier. The offset frequency has a positive value.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10103a.html language=enus -->
## TOPIC 00021: ACP:Advanced:Sequential FFT Size Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10103a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10103a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

ACP:Advanced:Sequential FFT Size Property

**Short Name:**ACP Sequential FFT Size

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the FFT size when you set the
 [ACP Meas Method](attr101012.html) property to **Sequential FFT**.

The default value is 512.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr102000.html language=enus -->
## TOPIC 00022: CCDF:Measurement Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr102000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr102000.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

CCDF:Measurement Enabled Property

**Short Name:**CCDF Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable the CCDF measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr102002.html language=enus -->
## TOPIC 00023: CCDF:Measurement Interval (s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr102002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr102002.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

CCDF:Measurement Interval (s) Property

**Short Name:**CCDF Meas Interval (s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the acquisition time for the CCDF measurement. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.001.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn CCDF Configure Measurement Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr102003.html language=enus -->
## TOPIC 00024: CCDF:Number of Analysis Threads Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr102003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr102003.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

CCDF:Number of Analysis Threads Property

**Short Name:**CCDF Num Analysis Threads

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the maximum number of threads used for parallelism for CCDF measurement.

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

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10200b.html language=enus -->
## TOPIC 00025: CCDF:Threshold:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10200b.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

CCDF:Threshold:Type Property

**Short Name:**CCDF Threshold Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the reference for the power level used for thresholding.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Relative**.

| Relative (0) | The threshold is relative to the peak power of the acquired samples. |
| --- | --- |
| Absolute (1) | The threshold is the absolute power, in dBm. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn CCDF Configure Threshold |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10200d.html language=enus -->
## TOPIC 00026: CCDF:All Traces Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10200d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10200d.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

CCDF:All Traces Enabled Property

**Short Name:**CCDF All Traces Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable the traces to be stored and retrieved after performing the CCDF measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10200e.html language=enus -->
## TOPIC 00027: CCDF:Results:Mean Power (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10200e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10200e.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

CCDF:Results:Mean Power (dBm) Property

**Short Name:**CCDF Results Mean Pwr (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the average power of all the samples. This value is expressed in dBm. If you set the [CCDF Threshold Enabled](attr102009.html) property to **True**, samples above the threshold are measured.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn CCDF Fetch Measurement |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10700d.html language=enus -->
## TOPIC 00028: PAVT:Measurement Bandwidth (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10700d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10700d.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

PAVT:Measurement Bandwidth (Hz) Property

**Short Name:**PAVT Meas Bandwidth (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the bandwidth over which the signal is measured. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10 MHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr107014.html language=enus -->
## TOPIC 00029: PAVT:Results:Frequency Error Mean(Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr107014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr107014.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

PAVT:Results:Frequency Error Mean(Hz) Property

**Short Name:**PAVT Results Freq Error Mean (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the mean frequency error of the segment. This value is expressed in Hz

Use "segment<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108006.html language=enus -->
## TOPIC 00030: SEM:Carrier:RBW Filter:Auto Bandwidth Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108006.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Carrier:RBW Filter:Auto Bandwidth Property

**Short Name:**SEM Carrier RBW Auto

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether the measurement computes the resolution bandwidth (RBW) of the carrier.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **True**.

| False (0) | The measurement uses the RBW that you specify in the SEM Carrier RBW property. |
| --- | --- |
| True (1) | The measurement computes the RBW. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Carrier RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108008.html language=enus -->
## TOPIC 00031: SEM:Carrier:RBW Filter:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108008.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Carrier:RBW Filter:Type Property

**Short Name:**SEM Carrier RBW Filter Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Gaussian**.

| FFT Based (0) | No RBW filtering is performed. |
| --- | --- |
| Gaussian (1) | The RBW filter has a Gaussian response. |
| Flat (2) | The RBW filter has a flat response. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Carrier RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10800a.html language=enus -->
## TOPIC 00032: SEM:Carrier:RRC Filter:Alpha Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10800a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10800a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Carrier:RRC Filter:Alpha Property

**Short Name:**SEM Carrier RRC Alpha

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the roll-off factor for the root-raised-cosine (RRC) filter to apply on the acquired carrier channel before measuring the carrier channel power.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Carrier RRC Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10800e.html language=enus -->
## TOPIC 00033: SEM:Offset:Relative Attenuation (dB) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10800e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10800e.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Relative Attenuation (dB) Property

**Short Name:**SEM Offset Rel Attn (dB)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the attenuation relative to the external attenuation specified by the [External Attenuation](attr100003.html) property. This value is expressed in dB. Use the SEM Offset Rel Attn property to compensate for the variations in external attenuation when offset segments are spread wide in frequency.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Offset Relative Attenuation, RFmxSpecAn SEM Configure Offset Relative Attenuation (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10800f.html language=enus -->
## TOPIC 00034: SEM:Offset:Absolute Limit:Mode Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10800f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10800f.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Absolute Limit:Mode Property

**Short Name:**SEM Offset Abs Limit Mode

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether the absolute limit mask is a flat line or a line with a slope.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Couple**.

| Manual (0) | The line specified by the SEM Offset Abs Limit Start and SEM Offset Abs Limit Stop property values as the two ends is considered as the mask. |
| --- | --- |
| Couple (1) | The two ends of the line are coupled to the value of the SEM Offset Abs Limit Start property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Offset Absolute Limit, RFmxSpecAn SEM Configure Offset Absolute Limit (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108010.html language=enus -->
## TOPIC 00035: SEM:Offset:Absolute Limit:Start (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108010.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Absolute Limit:Start (dBm) Property

**Short Name:**SEM Offset Abs Limit Start (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the absolute power limit corresponding to the beginning of the offset segment. This value is expressed in dBm. This power limit is also set as the stop limit for the offset segment when you set the [SEM Offset Abs Limit Mode](attr10800f.html) property to **Couple**.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is -10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Offset Absolute Limit, RFmxSpecAn SEM Configure Offset Absolute Limit (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108011.html language=enus -->
## TOPIC 00036: SEM:Offset:Absolute Limit:Stop (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108011.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Absolute Limit:Stop (dBm) Property

**Short Name:**SEM Offset Abs Limit Stop (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the absolute power limit corresponding to the end of the offset segment. This value is expressed in dBm. The measurement ignores this property when you set the [SEM Offset Abs Limit Mode](attr10800f.html) property to **Couple**.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is -10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Offset Absolute Limit, RFmxSpecAn SEM Configure Offset Absolute Limit (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108013.html language=enus -->
## TOPIC 00037: SEM:Offset:Sideband Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108013.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Sideband Property

**Short Name:**SEM Offset Sideband

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether the offset segment is present on one side, or on both sides of the carrier.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Both**.

| Neg (0) | Configures a lower offset segment to the left of the leftmost carrier. |
| --- | --- |
| Pos (1) | Configures an upper offset segment to the right of the rightmost carrier. |
| Both (2) | Configures both negative and positive offset segments. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Offset Frequency, RFmxSpecAn SEM Configure Offset Frequency (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108018.html language=enus -->
## TOPIC 00038: SEM:Offset:RBW Filter:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108018.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:RBW Filter:Type Property

**Short Name:**SEM Offset RBW Filter Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Gaussian**.

| FFT Based (0) | No RBW filtering is performed. |
| --- | --- |
| Gaussian (1) | The RBW filter has a Gaussian response. |
| Flat (2) | The RBW filter has a flat response. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn SEM Configure Offset RBW Filter, RFmxSpecAn SEM Configure Offset RBW Filter (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108021.html language=enus -->
## TOPIC 00039: SEM:Averaging:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108021.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Type Property

**Short Name:**SEM Averaging Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

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
| High-level VIs | RFmxSpecAn SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10802c.html language=enus -->
## TOPIC 00040: SEM:Results:Carrier:Integration Bandwidth (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10802c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10802c.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Integration Bandwidth (Hz) Property

**Short Name:**SEM Results Carrier IBW (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the frequency range, over which the measurement integrates the carrier power. This value is expressed in Hz.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10802d.html language=enus -->
## TOPIC 00041: SEM:Results:Carrier:Absolute Power (dBm or dBm/Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10802d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10802d.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Absolute Power (dBm or dBm/Hz) Property

**Short Name:**SEM Results Carrier Abs Pwr

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the carrier power.

The carrier power is reported in dBm when you set the [SEM Power Units](attr10801c.html) property to **dBm**, and in dBm/Hz when you set the SEM Power Units property to **dBm/Hz**.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Carrier Measurement |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10802e.html language=enus -->
## TOPIC 00042: SEM:Results:Carrier:Total Relative Power (dB) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10802e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10802e.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Total Relative Power (dB) Property

**Short Name:**SEM Results Carrier Total Rel Pwr (dB)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the carrier power relative to the total carrier power of all enabled carriers. This value is expressed in dB.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Carrier Measurement |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10802f.html language=enus -->
## TOPIC 00043: SEM:Results:Carrier:Peak Absolute Power (dBm or dBm/Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10802f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10802f.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Peak Absolute Power (dBm or dBm/Hz) Property

**Short Name:**SEM Results Carrier Pk Abs Pwr

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the peak power in the carrier channel.

The power is reported in dBm when you set the [SEM Power Units](attr10801c.html) property to **dBm**, and in dBm/Hz when you set the SEM Power Units property to **dBm/Hz**.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Carrier Measurement |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108030.html language=enus -->
## TOPIC 00044: SEM:Results:Carrier:Peak Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108030.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Carrier:Peak Frequency (Hz) Property

**Short Name:**SEM Results Carrier Pk Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the frequency at which the peak power occurs in the carrier channel. This value is expressed in Hz.

Use "carrier<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Carrier Measurement |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108032.html language=enus -->
## TOPIC 00045: SEM:Results:Lower Offset:Stop Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108032.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108032.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Stop Frequency (Hz) Property

**Short Name:**SEM Results Lower Offset Stop Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the stop frequency of the lower (negative) offset segment. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108033.html language=enus -->
## TOPIC 00046: SEM:Results:Lower Offset:Power Reference Carrier Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108033.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108033.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Power Reference Carrier Property

**Short Name:**SEM Results Lower Offset Pwr Ref Carrier

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the index of the carrier that was used as the power reference to define the lower (negative) offset segment relative power. The reference carrier is the carrier that has an offset closest to the offset segment.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108038.html language=enus -->
## TOPIC 00047: SEM:Results:Lower Offset:Peak Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108038.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Lower Offset:Peak Frequency (Hz) Property

**Short Name:**SEM Results Lower Offset Pk Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Lower Offset Power, RFmxSpecAn SEM Fetch Lower Offset Power (Array) |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr108041.html language=enus -->
## TOPIC 00048: SEM:Results:Upper Offset:Total Absolute Power (dBm or dBm/Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr108041.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr108041.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Total Absolute Power (dBm or dBm/Hz) Property

**Short Name:**SEM Results Upper Offset Total Abs Pwr

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the offset segment power measured in the upper (positive) offset segment.

The power is reported in dBm when you set the [SEM Power Units](attr10801c.html) property to **dBm**, and in dBm/Hz when you set the SEM Power Units property to **dBm/Hz**.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Upper Offset Power, RFmxSpecAn SEM Fetch Upper Offset Power (Array) |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10804a.html language=enus -->
## TOPIC 00049: SEM:Results:Upper Offset:Measurement Status Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10804a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10804a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Upper Offset:Measurement Status Property

**Short Name:**SEM Results Upper Offset Meas Status

Property of [RFmxSpecAn](crfmxspecan.html)

Indicates the upper offset measurement status based on measurement limits and the fail criteria that you specify in the [SEM Offset Limit Fail Mask](attr10800d.html) property.

Use "offset<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

| Fail (0) | Indicates that the measurement has failed. |
| --- | --- |
| Pass (1) | Indicates that the measurement has passed. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn SEM Fetch Upper Offset Margin, RFmxSpecAn SEM Fetch Upper Offset Margin (Array) |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr109002.html language=enus -->
## TOPIC 00050: Spectrum:Number of Analysis Threads Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr109002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr109002.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spectrum:Number of Analysis Threads Property

**Short Name:**Spectrum Num Analysis Threads

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the maximum number of threads used for parallelism for spectrum measurement.

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

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr109006.html language=enus -->
## TOPIC 00051: Spectrum:Averaging:Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr109006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr109006.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spectrum:Averaging:Enabled Property

**Short Name:**Spectrum Averaging Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable averaging for the spectrum measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The spectrum measurement uses the Spectrum Averaging Count property as the number of acquisitions over which the spectrum measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spectrum Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr109018.html language=enus -->
## TOPIC 00052: Spectrum:Detector:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr109018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr109018.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spectrum:Detector:Type Property

**Short Name:**Spectrum Detector Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the type of detector to be used.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **None**.

Refer to [Spectral Measurements](/csh?topicname=rfmxspecan/spectral_measurements_concepts.html) topic for more information on detector types.

| None (0) | The detector is disabled. |
| --- | --- |
| Sample (1) | The middle sample in the bucket is detected. |
| Normal (2) | The maximum value of the samples within the bucket is detected if the signal only rises or if the signal only falls. If the signal, within a bucket, both rises and falls, then the maximum and minimum values of the samples are detected in alternate buckets. |
| Peak (3) | The maximum value of the samples in the bucket is detected. |
| Negative Peak (4) | The minimum value of the samples in the bucket is detected. |
| Average RMS (5) | The average RMS of all the samples in the bucket is detected. |
| Average Voltage (6) | The average voltage of all the samples in the bucket is detected. |
| Average Log (7) | The average log of all the samples in the bucket is detected. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10901b.html language=enus -->
## TOPIC 00053: Spectrum:VBW Filter:Bandwidth (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10901b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10901b.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spectrum:VBW Filter:Bandwidth (Hz) Property

**Short Name:**Spectrum VBW (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the video bandwidth (VBW) in Hz when you set the [Spectrum VBW Auto](attr10901a.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 30000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10901c.html language=enus -->
## TOPIC 00054: Spectrum:VBW Filter:VBW to RBW Ratio Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10901c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10901c.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spectrum:VBW Filter:VBW to RBW Ratio Property

**Short Name:**Spectrum VBW to RBW Ratio

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the VBW to RBW Ratio when you set the [Spectrum VBW Auto](attr10901a.html) property to **True** .

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 3.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a004.html language=enus -->
## TOPIC 00055: Spur:Range:Number of Ranges Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a004.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Range:Number of Ranges Property

**Short Name:**Spur Num Ranges

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the number of ranges.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Number of Ranges |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a007.html language=enus -->
## TOPIC 00056: Spur:Range:Number of Spurs to Report Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a007.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Range:Number of Spurs to Report Property

**Short Name:**Spur Range Num Spurs to Report

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the number of spurious emissions (Spur) that the measurement should report in the frequency range.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 10.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Range Number of Spurs to Report, RFmxSpecAn Spur Configure Range Number of Spurs to Report (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a008.html language=enus -->
## TOPIC 00057: Spur:Range:Start Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a008.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Range:Start Frequency (Hz) Property

**Short Name:**Spur Range Start Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the start of the frequency range for the measurement. This value is expressed in Hz.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 500 MHz.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Range Frequency, RFmxSpecAn Spur Configure Range Frequency (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a009.html language=enus -->
## TOPIC 00058: Spur:Range:Stop Frequency (Hz) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a009.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Range:Stop Frequency (Hz) Property

**Short Name:**Spur Range Stop Freq (Hz)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the stop of the frequency range for the measurement. This value is expressed in Hz.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is 1.5 GHz.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Range Frequency, RFmxSpecAn Spur Configure Range Frequency (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a00a.html language=enus -->
## TOPIC 00059: Spur:Averaging:Count Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a00a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a00a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Averaging:Count Property

**Short Name:**Spur Averaging Count

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the number of acquisitions used for averaging when you set the [Spur Averaging Enabled](attr10a00b.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a011.html language=enus -->
## TOPIC 00060: Spur:Range:Absolute Limit:Start (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a011.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Range:Absolute Limit:Start (dBm) Property

**Short Name:**Spur Range Abs Limit Start (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the absolute power limit corresponding to the beginning of the frequency range. This value is expressed in dBm. This power limit is also set as the absolute power limit for the range when you set the [Spur Range Abs Limit Mode](attr10a010.html) property to **Couple**.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is -10.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Range Absolute Limit, RFmxSpecAn Spur Configure Range Absolute Limit (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a015.html language=enus -->
## TOPIC 00061: Spur:Range:RBW Filter:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a015.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Range:RBW Filter:Type Property

**Short Name:**Spur Range RBW Filter Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the shape of the digital resolution bandwidth (RBW) filter.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to configure or read this property.

The default value is **Gaussian**.

**Supported devices**: PXIe-5665/5668

| FFT Based (0) | No RBW filtering is performed. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxSpecAn Spur Configure Range RBW (Array), RFmxSpecAn Spur Configure Range RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a01b.html language=enus -->
## TOPIC 00062: Spur:Results:Range:Spur:Amplitude (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a01b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a01b.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Results:Range:Spur:Amplitude (dBm) Property

**Short Name:**Spur Results Spur Amplitude (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the amplitude of the detected spurious emissions (Spur). This value is expressed in dBm.

Use "range<*n*>/spur<*k*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn Spur Fetch Spur Measurement, RFmxSpecAn Spur Fetch Spur Measurement (Array) |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a01e.html language=enus -->
## TOPIC 00063: Spur:Results:Range:Measurement Status Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a01e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a01e.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Results:Range:Measurement Status Property

**Short Name:**Spur Results Range Meas Status

Property of [RFmxSpecAn](crfmxspecan.html)

Indicates the measurement status for the frequency range.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

**Supported devices**: PXIe-5665/5668

| Fail (0) | The amplitude of the detected spurs is greater than the value of the Spur Results Spur Abs Limit property. |
| --- | --- |
| Pass (1) | The amplitude of the detected spurs is lower than the value of the Spur Results Spur Abs Limit property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn Spur Fetch Range Status, RFmxSpecAn Spur Fetch Range Status (Array) |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10a01f.html language=enus -->
## TOPIC 00064: Spur:Results:Range:Spur:Number of Detected Spurs Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10a01f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10a01f.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

Spur:Results:Range:Spur:Number of Detected Spurs Property

**Short Name:**Spur Results Spur Num Detected Spurs

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the number of detected spurious emissions (Spur) in the specified frequency range.

Use "range<*n*>" as the [selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this result.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxSpecAn Spur Fetch Range Status, RFmxSpecAn Spur Fetch Range Status (Array) |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e003.html language=enus -->
## TOPIC 00065: AMPM:AM to AM Curve Fit:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e003.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:AM to AM Curve Fit:Type Property

**Short Name:**AMPM AM to AM Curve Fit Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Least Absolute Residual**.

| Least Square (0) | The measurement minimizes the energy of the polynomial approximation error. |
| --- | --- |
| Least Absolute Residual (1) | The measurement minimizes the magnitude of the polynomial approximation error. |
| Bisquare (2) | The measurement excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e004.html language=enus -->
## TOPIC 00066: AMPM:AM to PM Curve Fit:Order Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e004.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:AM to PM Curve Fit:Order Property

**Short Name:**AMPM AM to PM Curve Fit Order

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the degree of the polynomial used to approximate the AM-to-PM characteristic of the device under test.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 7.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e005.html language=enus -->
## TOPIC 00067: AMPM:AM to PM Curve Fit:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e005.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:AM to PM Curve Fit:Type Property

**Short Name:**AMPM AM to PM Curve Fit Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the polynomial approximation cost-function of the device under test AM-to-PM characteristic.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Least Absolute Residual**.

| Least Square (0) | The measurement minimizes the energy of the polynomial approximation error. |
| --- | --- |
| Least Absolute Residual (1) | The measurement minimizes the magnitude of the polynomial approximation error. |
| Bisquare (2) | The measurement excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e006.html language=enus -->
## TOPIC 00068: AMPM:Averaging:Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e006.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Averaging:Enabled Property

**Short Name:**AMPM Averaging Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable averaging for the AMPM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The AMPM measurement uses the AMPM Averaging Count property as the number of acquisitions over which the signal for the AMPM measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e007.html language=enus -->
## TOPIC 00069: AMPM:Averaging:Count Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e007.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Averaging:Count Property

**Short Name:**AMPM Averaging Count

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the number of acquisitions used for averaging when you set the [AMPM Averaging Enabled](attr10e006.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e009.html language=enus -->
## TOPIC 00070: AMPM:Measurement Interval (s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e009.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Measurement Interval (s) Property

**Short Name:**AMPM Meas Interval (s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the duration of the reference waveform considered for the AMPM measurement. When the reference waveform contains an idle duration, the AMPM measurement neglects the idle samples in the reference waveform leading up to the start of the first active portion of the reference waveform. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 100E-6.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e00a.html language=enus -->
## TOPIC 00071: AMPM:Signal Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e00a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e00a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Signal Type Property

**Short Name:**AMPM Signal Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether the reference waveform is a modulated signal or a combination of one or more sinusoidal signals. To time-align the sinusoidal reference waveform to the acquired signal, set the AMPM Signal Type property to **Tones**, which switches the AMPM measurement alignment algorithm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Modulated**.

| Modulated (0) | The reference waveform is a cellular or connectivity standard signal. |
| --- | --- |
| Tones (1) | The reference waveform is a continuous signal comprising of one or more tones. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e00b.html language=enus -->
## TOPIC 00072: AMPM:Measurement Sample Rate:Mode Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e00b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e00b.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Measurement Sample Rate:Mode Property

**Short Name:**AMPM Meas Sample Rate Mode

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether the acquisition sample rate is based on the reference waveform.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Reference Waveform**.

| User (0) | The acquisition sample rate is defined by the value of the AMPM Meas Sample Rate property. |
| --- | --- |
| Reference Waveform (1) | The acquisition sample rate is set to match the sample rate of the reference waveform. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e00c.html language=enus -->
## TOPIC 00073: AMPM:Measurement Sample Rate:Sample Rate (S/s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e00c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e00c.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Measurement Sample Rate:Sample Rate (S/s) Property

**Short Name:**AMPM Meas Sample Rate (S/s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the acquisition sample rate when you set the [AMPM Meas Sample Rate Mode](attr10e00b.html) property to **User**. This value is expressed in samples per second (S/s).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 120,000,000.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e010.html language=enus -->
## TOPIC 00074: AMPM:DUT Average Input Power (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e010.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:DUT Average Input Power (dBm) Property

**Short Name:**AMPM DUT Avg Input Pwr (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the average power of the signal at the input port of the device under test. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is -20 dBm.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e011.html language=enus -->
## TOPIC 00075: AMPM:All Traces Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e011.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:All Traces Enabled Property

**Short Name:**AMPM All Traces Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable the traces to be stored and retrieved after performing the AMPM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e012.html language=enus -->
## TOPIC 00076: AMPM:Number of Analysis Threads Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e012.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Number of Analysis Threads Property

**Short Name:**AMPM Num Analysis Threads

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the maximum number of threads used for parallelism for the AMPM measurement.

The number of threads can range from 1 to the number of physical cores. However, the number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e01b.html language=enus -->
## TOPIC 00077: AMPM:Results:Gain Error Range (dB) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e01b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e01b.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Results:Gain Error Range (dB) Property

**Short Name:**AMPM Results Gain Error Range (dB)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the peak-to-peak deviation of the device under test gain. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e01c.html language=enus -->
## TOPIC 00078: AMPM:Results:Phase Error Range (deg) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e01c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e01c.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Results:Phase Error Range (deg) Property

**Short Name:**AMPM Results Phase Error Range (deg)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the peak-to-peak deviation of the phase distortion of the acquired signal relative to the reference waveform caused by the device under test. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e022.html language=enus -->
## TOPIC 00079: AMPM:Max Timing Error (s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e022.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e022.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Max Timing Error (s) Property

**Short Name:**AMPM Max Timing Error (s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the maximum time alignment error expected between the acquired and the reference waveforms. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.00002.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e023.html language=enus -->
## TOPIC 00080: AMPM:Reference Power Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e023.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e023.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Reference Power Type Property

**Short Name:**AMPM Ref Pwr Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the reference power used for AM to AM and AM to PM traces.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Input**.

| Input (0) | The instantaneous powers at the input port of device under test (DUT) forms the x-axis of AM to AM and AM to PM traces. |
| --- | --- |
| Output (1) | The instantaneous powers at the output port of DUT forms the x-axis of AM to AM and AM to PM traces. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e025.html language=enus -->
## TOPIC 00081: AMPM:Compression Point:Level (dB) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e025.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Compression Point:Level (dB) Property

**Short Name:**AMPM Compression Point Level (dB)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the compression levels for which the compression points are computed when you set the [AMPM Compression Point Enabled](attr10e024.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e027.html language=enus -->
## TOPIC 00082: AMPM:Results:Compression Point:Output Compression Point (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e027.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Results:Compression Point:Output Compression Point (dBm) Property

**Short Name:**AMPM Results Output Compression Point (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the theoretical output power at which the gain of the device drops by a compression level, specified through the [AMPM Compression Point Level](attr10e025.html) property, from a gain reference computed based on the value that you specify for the [AMPM Compression Point Gain Ref](attr10e034.html) property. This value is expressed in dBm.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e029.html language=enus -->
## TOPIC 00083: AMPM:IQ Origin Offset Correction Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e029.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:IQ Origin Offset Correction Enabled Property

**Short Name:**AMPM IQ Origin Offset Correction Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Enables IQ origin offset correction for the measurement.

When you set this property is set to **True**, the measurement computes and corrects any origin offset between the reference and the acquired waveforms. When you set this property to **False**, origin offset correction is not performed.

The default value is **True**.

| False (0) | Disables IQ origin offset correction. |
| --- | --- |
| True (1) | Enables IQ origin offset correction. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e034.html language=enus -->
## TOPIC 00084: AMPM:Compression Point:Gain:Reference Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e034.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e034.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Compression Point:Gain:Reference Property

**Short Name:**AMPM Compression Point Gain Ref

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the gain reference for compression point calculation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Auto**.

| Auto (0) | Measurement computes the gain reference to be used for compression point calculation. The computed gain reference is also returned as AMPM Results Mean Linear Gain result. |
| --- | --- |
| Reference Power (1) | Measurement uses the gain corresponding to the reference power that you specify for the AMPM Compression Point Gain Ref Pwr property as gain reference. The reference power can be configured as either input or output power based on the value of the AMPM Ref Pwr Type property. |
| Max Gain (2) | Measurement uses the maximum gain as gain reference for compression point calculation. |
| User Defined (3) | Measurement uses the gain that you specify for the AMPM Compression Point User Gain property as gain reference for compression point calculation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10e039.html language=enus -->
## TOPIC 00085: AMPM:Results:Peak Reference Power Gain (dB) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10e039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10e039.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

AMPM:Results:Peak Reference Power Gain (dB) Property

**Short Name:**AMPM Results Peak Ref Pwr Gain (dB)

Property of [RFmxSpecAn](crfmxspecan.html)

Returns the gain at the peak reference power. This value is expressed in dB.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f004.html language=enus -->
## TOPIC 00086: DPD:Measurement Interval (s) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f004.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Measurement Interval (s) Property

**Short Name:**DPD Meas Interval (s)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the duration of the reference waveform considered for the DPD measurement. When the reference waveform contains an idle duration, the DPD measurement neglects the idle samples in the reference waveform leading up to the start of the first active portion of the reference waveform. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 100E-6.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f007.html language=enus -->
## TOPIC 00087: DPD:DUT Average Input Power (dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f007.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:DUT Average Input Power (dBm) Property

**Short Name:**DPD DUT Avg Input Pwr (dBm)

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the average power of the signal at the device under test input port. This value is expressed in dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is -20 dBm.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f008.html language=enus -->
## TOPIC 00088: DPD:Model Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f008.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Model Property

**Short Name:**DPD Model

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the DPD model used by the DPD measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Lookup Table**.

| Lookup Table (0) | This model computes the complex gain coefficients applied when performing digital predistortion to linearize systems with negligible memory effects. |
| --- | --- |
| Memory Polynomial (1) | This model computes the memory polynomial predistortion coefficients used to linearize systems with moderate memory effects. |
| Generalized Memory Polynomial (2) | This model computes the generalized memory polynomial predistortion coefficients used to linearize systems with significant memory effects. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f009.html language=enus -->
## TOPIC 00089: DPD:Lookup Table:AM to AM Curve Fit:Order Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f009.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Lookup Table:AM to AM Curve Fit:Order Property

**Short Name:**DPD LUT AM to AM Curve Fit Order

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the degree of the polynomial used to approximate the device under test AM-to-AM characteristic when you set the [DPD Model](attr10f008.html) property to **Lookup Table**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 7.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f00a.html language=enus -->
## TOPIC 00090: DPD:Lookup Table:AM to AM Curve Fit:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f00a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f00a.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Lookup Table:AM to AM Curve Fit:Type Property

**Short Name:**DPD LUT AM to AM Curve Fit Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the polynomial approximation cost-function of the device under test AM-to-AM characteristic when you set the [DPD Model](attr10f008.html) property to **Lookup Table**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Least Absolute Residual**.

| Least Square (0) | Minimizes the energy of the polynomial approximation error. |
| --- | --- |
| Least Absolute Residual (1) | Minimizes the magnitude of the polynomial approximation error. |
| Bisquare (2) | Excludes the effect of data outliers while minimizing the energy of the polynomial approximation error. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f00d.html language=enus -->
## TOPIC 00091: DPD:Lookup Table:Threshold:Enabled Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f00d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f00d.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Lookup Table:Threshold:Enabled Property

**Short Name:**DPD LUT Threshold Enabled

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies whether to enable thresholding of the acquired samples to be used for the DPD measurement when you set the [DPD Model](attr10f008.html) property to **Lookup Table**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | All samples are considered for the DPD measurement. |
| --- | --- |
| True (1) | Only samples above the threshold level which you specify in the DPD LUT Threshold Level property are considered for the DPD measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f00f.html language=enus -->
## TOPIC 00092: DPD:Lookup Table:Threshold:Level (dB or dBm) Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f00f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f00f.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Lookup Table:Threshold:Level (dB or dBm) Property

**Short Name:**DPD LUT Threshold Level

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies either the relative or absolute threshold power level based on the value of the [DPD LUT Threshold Type](attr10f00e.html) property. This value is expressed in dB or dBm.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is -20.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f014.html language=enus -->
## TOPIC 00093: DPD:Memory Polynomial:Cross Terms:Lag Order Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f014.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Memory Polynomial:Cross Terms:Lag Order Property

**Short Name:**DPD Mem Poly Lag Order

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the lag order cross term of the DPD polynomial when you set the [DPD Model](attr10f008.html) property to **Generalized Memory Polynomial**. This term value corresponds to *K<sub>b</sub>* in the [equation](/csh?topicname=rfmxspecan/dpd.html) for the generalized memory polynomial.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f02b.html language=enus -->
## TOPIC 00094: DPD:Apply DPD:User:Memory Polynomial:Memory Depth Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f02b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f02b.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Apply DPD:User:Memory Polynomial:Memory Depth Property

**Short Name:**DPD Apply DPD User Mem Poly Mem Depth

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the memory depth of the DPD polynomial when you set the [DPD Apply DPD User DPD Model](attr10f026.html) property to **Memory Polynomial** or **Generalized Memory Polynomial** and set the [DPD Apply DPD Config Input](attr10f021.html) property to **User**. This value corresponds to Q<sub>a</sub> in the [equation](/csh?topicname=rfmxspecan/dpd.html) for generalized memory polynomial.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f02c.html language=enus -->
## TOPIC 00095: DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Lead Order Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f02c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f02c.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Lead Order Property

**Short Name:**DPD Apply DPD User Mem Poly Lead Order

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the lead order cross term of the DPD polynomial when you set the [DPD Apply DPD User DPD Model](attr10f026.html) property to **Generalized Memory Polynomial** and set the [DPD Apply DPD Config Input](attr10f021.html) property to **User**. This value corresponds to K<sub>c</sub> in the [equation](/csh?topicname=rfmxspecan/dpd.html) for the generalized memory polynomial.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f02d.html language=enus -->
## TOPIC 00096: DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Lag Order Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f02d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f02d.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Lag Order Property

**Short Name:**DPD Apply DPD User Mem Poly Lag Order

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the lag order cross term of the DPD polynomial when you set the [DPD Apply DPD User DPD Model](attr10f026.html) property to **Generalized Memory Polynomial** and set the [DPD Apply DPD Config Input](attr10f021.html) property to **User**. This value corresponds to K<sub>b</sub> in the [equation](/csh?topicname=rfmxspecan/dpd.html) for the generalized memory polynomial.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f02f.html language=enus -->
## TOPIC 00097: DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Lag Memory Depth Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f02f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f02f.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Lag Memory Depth Property

**Short Name:**DPD Apply DPD User Mem Poly Lag Mem Depth

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the lag memory depth cross term of the DPD polynomial when you set the [DPD Apply DPD User DPD Model](attr10f026.html) property to **Memory Polynomial** or **Generalized Memory Polynomial** and set the [DPD Apply DPD Config Input](attr10f021.html) property to **User**. This value corresponds to Q<sub>b</sub> in the [equation](/csh?topicname=rfmxspecan/dpd.html) for the generalized memory polynomial.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f030.html language=enus -->
## TOPIC 00098: DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Maximum Lead Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f030.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f030.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Apply DPD:User:Memory Polynomial:Cross Terms:Maximum Lead Property

**Short Name:**DPD Apply DPD User Mem Poly Max Lead

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the maximum lead stagger cross term of the DPD polynomial when you set the [DPD Apply DPD User DPD Model](attr10f026.html) property to **Memory Polynomial** or **Generalized Memory Polynomial** and set the [DPD Apply DPD Config Input](attr10f021.html) property to **User**. This value corresponds to M<sub>c</sub> in the [equation](/csh?topicname=rfmxspecan/dpd.html) for the generalized memory polynomial.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-specan-prop path=rfmxspecanprop/attr10f038.html language=enus -->
## TOPIC 00099: DPD:Lookup Table:Type Property

- bundle_id: `rfmx-specan-prop`
- source_path: `rfmxspecanprop/attr10f038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-specan-prop/raw/resource/enus/rfmxspecanprop/attr10f038.html
- document_id: `rfmx-specan-prop`
- page_type: `leaf`
- content_type: ``

DPD:Lookup Table:Type Property

**Short Name:**DPD LUT Type

Property of [RFmxSpecAn](crfmxspecan.html)

Specifies the type of the DPD lookup table (LUT).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Log**.

| Log (0) | Input powers in the LUT are specified in dBm. |
| --- | --- |
| Linear (1) | Input powers in the LUT are specified in watts. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |
