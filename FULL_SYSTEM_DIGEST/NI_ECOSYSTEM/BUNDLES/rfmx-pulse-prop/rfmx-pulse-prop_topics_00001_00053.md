# NI DOCUMENT BUNDLE: rfmx-pulse-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-pulse-prop start=1 end=53 -->
<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00006.html language=enus -->
## TOPIC 00001: Trigger:Digital Edge:Edge Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00006.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxPulse](crfmxpulse.html)

Specifies the active edge for the trigger. This property is used only when you set the [Trigger Type](attrc00004.html) property to **Digital Edge**.

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

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00008.html language=enus -->
## TOPIC 00002: Trigger:IQ Power Edge:Level (dB or dBm) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00008.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level (dB or dBm) Property

**Short Name:**IQ Power Edge Level

Property of [RFmxPulse](crfmxpulse.html)

Specifies the power level at which the device triggers. This value is expressed in dB when you set the [IQ Power Edge Level Type](attrc00fff.html) property to **Relative** and in dBm when you set the IQ Power Edge Level Type property to **Absolute**. The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the [Trigger Type](attrc00004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0000a.html language=enus -->
## TOPIC 00003: Trigger:Delay (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0000a.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Delay (s) Property

**Short Name:**Trigger Delay (s)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0000d.html language=enus -->
## TOPIC 00004: Advanced:Auto Level Initial Reference Level (dBm) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0000d.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Auto Level Initial Reference Level (dBm) Property

**Short Name:**Auto Level Initial Ref Level (dBm)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the initial reference level, in dBm, which the [RFmxPulse Auto Level](/csh?topicname=rfmxpulsevi/rfmxpulse_auto_level.html) VI uses to estimate the peak power of the input signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 30.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00011.html language=enus -->
## TOPIC 00005: Acquisition Length (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00011.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Acquisition Length (s) Property

**Short Name:**Acquisition Length (s)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the acquisition length for the pulse measurement. This value is expressed in seconds.

You configure this property when you set the [Segmented Acquisition Enabled](attrc00014.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.001 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00013.html language=enus -->
## TOPIC 00006: Maximum Pulse Count:Value Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00013.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Maximum Pulse Count:Value Property

**Short Name:**Max Pulse Count

Property of [RFmxPulse](crfmxpulse.html)

Specifies the maximum number of pulses to be measured when you set the [Max Pulse Count Enabled](attrc00012.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 100. Valid values are 1 to 10000, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00015.html language=enus -->
## TOPIC 00007: Segmented Acquisition:Number of Segments Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00015.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Segmented Acquisition:Number of Segments Property

**Short Name:**Num Segments

Property of [RFmxPulse](crfmxpulse.html)

Specifies the number of segments to acquire when you set the [Segmented Acquisition Enabled](attrc00014.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1. Valid values are 1 to 10000, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00016.html language=enus -->
## TOPIC 00008: Segmented Acquisition:Length (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00016.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Segmented Acquisition:Length (s) Property

**Short Name:**Segmented Acquisition Length (s)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the acquisition length for the pulse measurement when you set the [Segmented Acquisition Enabled](attrc00014.html) property to **True**. This value is expressed in seconds.

You must set this property to a value slightly higher than the desired pulse ON duration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.00001 seconds.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00017.html language=enus -->
## TOPIC 00009: Measurement Bandwidth (Hz) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00017.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Measurement Bandwidth (Hz) Property

**Short Name:**Measurement Bandwidth (Hz)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the bandwidth of the filter used for the required sample rate. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **80 MHz**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00018.html language=enus -->
## TOPIC 00010: Measurement Filter Type Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00018.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Measurement Filter Type Property

**Short Name:**Measurement Filter Type

Property of [RFmxPulse](crfmxpulse.html)

Specifies the demodulation filter type to be used in the measurements.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| Rectangular (0) | The Rectangular filter is applied. |
| --- | --- |
| Gaussian (1) | The Gaussian filter is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00ffd.html language=enus -->
## TOPIC 00011: Selected Ports Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00ffd.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Selected Ports Property

**Short Name:**Selected Ports

Property of [RFmxPulse](crfmxpulse.html)

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

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc00fff.html language=enus -->
## TOPIC 00012: Trigger:IQ Power Edge:Level Type Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc00fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc00fff.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Trigger:IQ Power Edge:Level Type Property

**Short Name:**IQ Power Edge Level Type

Property of [RFmxPulse](crfmxpulse.html)

Specifies the reference for the [IQ Power Edge Level](attrc00008.html) property. The IQ Power Edge Level Type property is used only when you set the [Trigger Type](attrc00004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Absolute**.

| Relative (0) | The value of the IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01000.html language=enus -->
## TOPIC 00013: Pulse:Measurement Enabled Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01000.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Measurement Enabled Property

**Short Name:**Pulse Enabled

Property of [RFmxPulse](crfmxpulse.html)

Specifies whether pulse measurements are enabled..

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **FALSE**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01002.html language=enus -->
## TOPIC 00014: Pulse:Detection:Reference Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01002.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Detection:Reference Property

**Short Name:**Pulse Detection Reference

Property of [RFmxPulse](crfmxpulse.html)

Specifies the reference used for [Pulse Detection Threshold](attrc01003.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **Ref Level**.

| Ref Level (0) | The threshold is relative to the reference level of the samples. |
| --- | --- |
| Absolute (1) | The threshold is the absolute power, in dBm. |
| Peak (2) | The threshold is relative to the peak level of the samples. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0100b.html language=enus -->
## TOPIC 00015: Pulse:Level:Width Threshold (%) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0100b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0100b.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Level:Width Threshold (%) Property

**Short Name:**Pulse Width Threshold Level (%)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the middle threshold level as a percentage of the pulse amplitude used to signify the mid-transition level between pulse states used for pulse width computation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 50. Valid values are 0 to 100, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0100c.html language=enus -->
## TOPIC 00016: Pulse:Level:Lower Threshold (%) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0100c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0100c.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Level:Lower Threshold (%) Property

**Short Name:**Pulse Lower Threshold Level (%)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the lower threshold level as a percentage of the pulse amplitude used to signify the start of a rising or end of a falling edge.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 10. Valid values are 0 to 100, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0100d.html language=enus -->
## TOPIC 00017: Pulse:Level:Droop Compensation Enabled Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0100d.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Level:Droop Compensation Enabled Property

**Short Name:**Pulse Droop Comp Enabled

Property of [RFmxPulse](crfmxpulse.html)

Specifies whether to compensate the droop detected in pulse level when applying thresholds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | Droop Compensation is disabled. |
| --- | --- |
| True (1) | Droop Compensation is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01018.html language=enus -->
## TOPIC 00018: Pulse:Results:Level:Base Level Minimum (dBm) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01018.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Level:Base Level Minimum (dBm) Property

**Short Name:**Pulse Results Base Level Min (dBm)

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum base level across the measured pulses. This value is expressed in dBm.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0104e.html language=enus -->
## TOPIC 00019: Pulse:Results:Time:Duty Cycle Maximum (%) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0104e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0104e.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time:Duty Cycle Maximum (%) Property

**Short Name:**Pulse Results Duty Cycle Max (%)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum duty cycle across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0104f.html language=enus -->
## TOPIC 00020: Pulse:Results:Time:Duty Cycle Minimum (%) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0104f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0104f.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time:Duty Cycle Minimum (%) Property

**Short Name:**Pulse Results Duty Cycle Min (%)

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum duty cycle across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01050.html language=enus -->
## TOPIC 00021: Pulse:Results:Time:Duty Cycle Standard Deviation (%) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01050.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01050.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time:Duty Cycle Standard Deviation (%) Property

**Short Name:**Pulse Results Duty Cycle SD (%)

Property of [RFmxPulse](crfmxpulse.html)

Returns the standard deviation of duty cycle values across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01051.html language=enus -->
## TOPIC 00022: Pulse:Results:Time:Pulse Repetition Interval (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01051.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01051.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time:Pulse Repetition Interval (s) Property

**Short Name:**Pulse Results PRI (s)

Property of [RFmxPulse](crfmxpulse.html)

Returns the pulse period values for all measured pulses. Period values are the time difference between two consecutive transitions of the same polarity, either positive or negative, where the transitions occur at crossings of the width threshold.
 This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01052.html language=enus -->
## TOPIC 00023: Pulse:Results:Time:Pulse Repetition Interval Mean (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01052.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01052.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time:Pulse Repetition Interval Mean (s) Property

**Short Name:**Pulse Results PRI Mean (s)

Property of [RFmxPulse](crfmxpulse.html)

Returns the mean of pulse period values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01054.html language=enus -->
## TOPIC 00024: Pulse:Results:Time:Pulse Repetition Interval Minimum (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01054.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01054.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time:Pulse Repetition Interval Minimum (s) Property

**Short Name:**Pulse Results PRI Min (s)

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum pulse period across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0105b.html language=enus -->
## TOPIC 00025: Pulse:Results:Frequency and Phase:Average Phase (deg) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0105b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0105b.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Average Phase (deg) Property

**Short Name:**Pulse Results Avg Phase (deg)

Property of [RFmxPulse](crfmxpulse.html)

Returns the average phase for all measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0105d.html language=enus -->
## TOPIC 00026: Pulse:Results:Frequency and Phase:Average Phase Maximum (deg) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0105d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0105d.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Average Phase Maximum (deg) Property

**Short Name:**Pulse Results Avg Phase Max (deg)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0105e.html language=enus -->
## TOPIC 00027: Pulse:Results:Frequency and Phase:Average Phase Minimum (deg) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0105e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0105e.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Average Phase Minimum (deg) Property

**Short Name:**Pulse Results Avg Phase Min (deg)

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0105f.html language=enus -->
## TOPIC 00028: Pulse:Results:Frequency and Phase:Average Phase Standard Deviation (deg) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0105f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0105f.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Average Phase Standard Deviation (deg) Property

**Short Name:**Pulse Results Avg Phase SD (deg)

Property of [RFmxPulse](crfmxpulse.html)

Returns the standard deviation of the average phase across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01064.html language=enus -->
## TOPIC 00029: Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Standard Deviation (deg) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01064.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01064.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Pulse to Pulse Phase Difference Standard Deviation (deg) Property

**Short Name:**Pulse Results Pulse to Pulse Phase Diff SD (deg)

Property of [RFmxPulse](crfmxpulse.html)

Returns the standard deviation of the pulse-to-pulse phase difference across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01067.html language=enus -->
## TOPIC 00030: Pulse:Results:Frequency and Phase:Phase Deviation Maximum (deg) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01067.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01067.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Phase Deviation Maximum (deg) Property

**Short Name:**Pulse Results Phase Dev Max (deg)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0106e.html language=enus -->
## TOPIC 00031: Pulse:Results:Frequency and Phase:Average Frequency Standard Deviation (Hz) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0106e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0106e.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Average Frequency Standard Deviation (Hz) Property

**Short Name:**Pulse Results Avg Freq SD (Hz)

Property of [RFmxPulse](crfmxpulse.html)

Returns the standard deviation of the average frequency across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0106f.html language=enus -->
## TOPIC 00032: Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference (Hz) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0106f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0106f.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Pulse to Pulse Frequency Difference (Hz) Property

**Short Name:**Pulse Results Pulse to Pulse Freq Diff (Hz)

Property of [RFmxPulse](crfmxpulse.html)

Returns the frequency difference of the pulses with respect to the frequency of the first pulse. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01076.html language=enus -->
## TOPIC 00033: Pulse:Results:Frequency and Phase:Frequency Deviation Maximum (Hz) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01076.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01076.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Frequency and Phase:Frequency Deviation Maximum (Hz) Property

**Short Name:**Pulse Results Freq Dev Max (Hz)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum peak-to-peak phase deviation across the measured pulses. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0107a.html language=enus -->
## TOPIC 00034: Pulse:Results:Stability:Amplitude Mean (dB) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0107a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0107a.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Stability:Amplitude Mean (dB) Property

**Short Name:**Pulse Results Amplitude Stability Mean (dB)

Property of [RFmxPulse](crfmxpulse.html)

Returns the mean of the amplitude stability values across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0107b.html language=enus -->
## TOPIC 00035: Pulse:Results:Stability:Amplitude Maximum (dB) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0107b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0107b.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Stability:Amplitude Maximum (dB) Property

**Short Name:**Pulse Results Amplitude Stability Max (dB)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum amplitude stability across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0107f.html language=enus -->
## TOPIC 00036: Pulse:Results:Stability:Phase Mean (dB) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0107f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0107f.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Stability:Phase Mean (dB) Property

**Short Name:**Pulse Results Phase Stability Mean (dB)

Property of [RFmxPulse](crfmxpulse.html)

Returns the mean of the phase stability values across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01085.html language=enus -->
## TOPIC 00037: Pulse:Results:Stability:Total Maximum (dB) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01085.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01085.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Stability:Total Maximum (dB) Property

**Short Name:**Pulse Results Total Stability Max (dB)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum total stability across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01088.html language=enus -->
## TOPIC 00038: Pulse:Number of Analysis Threads Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01088.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01088.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Number of Analysis Threads Property

**Short Name:**Pulse Num Analysis Threads

Property of [RFmxPulse](crfmxpulse.html)

Specifies the maximum number of threads used for parallelism for the pulse measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1. Valid values are 1 to 10, inclusive.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0108c.html language=enus -->
## TOPIC 00039: Pulse:Measurement Point:Averaging Duration (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0108c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0108c.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Measurement Point:Averaging Duration (s) Property

**Short Name:**Pulse Meas Point Avg Duration (s)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the length of the averaging window centered at the measurement point. A minimum of 1 sample is used internally.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc0108f.html language=enus -->
## TOPIC 00040: Pulse:Frequency and Phase:Deviation Range:Edge Start (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc0108f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc0108f.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Frequency and Phase:Deviation Range:Edge Start (s) Property

**Short Name:**Pulse Freq Phase Dev Range Edge Start (s)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the start of the pulse data used for the phase/frequency deviation and error measurements when you set the [Pulse Freq Phase Dev Range Reference](attrc0108d.html) property to **Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01090.html language=enus -->
## TOPIC 00041: Pulse:Frequency and Phase:Deviation Range:Edge Stop (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01090.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01090.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Frequency and Phase:Deviation Range:Edge Stop (s) Property

**Short Name:**Pulse Freq Phase Dev Range Edge Stop (s)

Property of [RFmxPulse](crfmxpulse.html)

Specifies the stop of the pulse data used for the phase/frequency deviation and error measurements when you set the [Pulse Freq Phase Dev Range Reference](attrc0108d.html) property to **Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01092.html language=enus -->
## TOPIC 00042: Pulse:Stability:Measurement Offset Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01092.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01092.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Stability:Measurement Offset Property

**Short Name:**Pulse Stability Meas Offset

Property of [RFmxPulse](crfmxpulse.html)

Specifies the offset in number of pulses to be used for pulse stability measurement. This property is applicable for average stability results and pulse-to-pulse stabilty trace.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01093.html language=enus -->
## TOPIC 00043: Pulse:Stability:Reference Offset Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01093.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01093.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Stability:Reference Offset Property

**Short Name:**Pulse Stability Ref Offset

Property of [RFmxPulse](crfmxpulse.html)

Specifies the offset in number of pulses used for pulse stability reference computation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01094.html language=enus -->
## TOPIC 00044: Pulse:Stability:Pulse To Pulse Offset Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01094.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01094.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Stability:Pulse To Pulse Offset Property

**Short Name:**Pulse Stability Pulse To Pulse Offset

Property of [RFmxPulse](crfmxpulse.html)

Specifies the offset in number of pulses used for pulse-to-pulse stability measurement trace.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc010f4.html language=enus -->
## TOPIC 00045: Pulse:Results:Time Sidelobe:Delay Minimum (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc010f4.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc010f4.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Delay Minimum (s) Property

**Short Name:**Pulse Results Sidelobe Delay Min (s)

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum sidelobe delay across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc010f5.html language=enus -->
## TOPIC 00046: Pulse:Results:Time Sidelobe:Delay Standard Deviation (s) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc010f5.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc010f5.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Delay Standard Deviation (s) Property

**Short Name:**Pulse Results Sidelobe Delay SD (s)

Property of [RFmxPulse](crfmxpulse.html)

Returns the standard deviation of the sidelobe delay values across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc010f7.html language=enus -->
## TOPIC 00047: Pulse:Results:Time Sidelobe:Peak Sidelobe Level Mean (dB) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc010f7.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc010f7.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Peak Sidelobe Level Mean (dB) Property

**Short Name:**Pulse Results Pk Sidelobe Level Mean (dB)

Property of [RFmxPulse](crfmxpulse.html)

Returns the mean of the peak sidelobe level values across the measured pulses. This value is expressed in dB.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc010f8.html language=enus -->
## TOPIC 00048: Pulse:Results:Time Sidelobe:Peak Sidelobe Level Maximum (dB) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc010f8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc010f8.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Peak Sidelobe Level Maximum (dB) Property

**Short Name:**Pulse Results Pk Sidelobe Level Max (dB)

Property of [RFmxPulse](crfmxpulse.html)

Returns the maximum peak sidelobe level across the measured pulses. This value is expressed in seconds.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc010fe.html language=enus -->
## TOPIC 00049: Pulse:Results:Time Sidelobe:Compression Ratio Minimum (%) Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc010fe.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc010fe.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Compression Ratio Minimum (%) Property

**Short Name:**Pulse Results Compression Ratio Min (%)

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum compression ratio across the measured pulses. This value is expressed as a percentage.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01100.html language=enus -->
## TOPIC 00050: Pulse:Results:Time Sidelobe:Peak Correlation Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01100.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01100.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Peak Correlation Property

**Short Name:**Pulse Results Pk Correlation

Property of [RFmxPulse](crfmxpulse.html)

Returns the peak correlation for all measured pulses. Peak correlation is the normalized peak power of the correlated output by both measured and reference pulse powers. This values ranges in between 0 to 1.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01101.html language=enus -->
## TOPIC 00051: Pulse:Results:Time Sidelobe:Peak Correlation Mean Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01101.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01101.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Peak Correlation Mean Property

**Short Name:**Pulse Results Pk Correlation Mean

Property of [RFmxPulse](crfmxpulse.html)

Returns the mean of the peak correlation values across the measured pulses.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01103.html language=enus -->
## TOPIC 00052: Pulse:Results:Time Sidelobe:Peak Correlation Minimum Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01103.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01103.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Peak Correlation Minimum Property

**Short Name:**Pulse Results Pk Correlation Min

Property of [RFmxPulse](crfmxpulse.html)

Returns the minimum peak correlation across the measured pulses.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-pulse-prop path=rfmxpulseprop/attrc01104.html language=enus -->
## TOPIC 00053: Pulse:Results:Time Sidelobe:Peak Correlation Standard Deviation Property

- bundle_id: `rfmx-pulse-prop`
- source_path: `rfmxpulseprop/attrc01104.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-pulse-prop/raw/resource/enus/rfmxpulseprop/attrc01104.html
- document_id: `rfmx-pulse-prop`
- page_type: `leaf`
- content_type: ``

Pulse:Results:Time Sidelobe:Peak Correlation Standard Deviation Property

**Short Name:**Pulse Results Pk Correlation SD

Property of [RFmxPulse](crfmxpulse.html)

Returns the standard deviation of the peak correlation values across the measured pulses.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |
