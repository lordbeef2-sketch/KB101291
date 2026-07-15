# NI DOCUMENT BUNDLE: rfmx-tdscdma-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-tdscdma-prop start=1 end=80 -->
<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr700006.html language=enus -->
## TOPIC 00001: rfmxtdscdmaprop/attr700006.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr700006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr700006.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the active edge for the trigger. This property is used only when you set the [Trigger Type](attr700004.html) property to **Digital Edge**.

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
| High-level VIs | RFmxTDSCDMA Configure Trigger |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr700010.html language=enus -->
## TOPIC 00002: rfmxtdscdmaprop/attr700010.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr700010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr700010.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

Channel:Configuration Mode Property

Channel:Configuration Mode Property

**Short Name:**Channel Configuration Mode

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to detect the channels automatically or to use a specified channel configuration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

| Auto Detect (0) | RFmx TD-SCDMA detects the channels automatically. |
| --- | --- |
| User Defined (1) | The channel configuration is defined manually. This mode increases measurement speed because no time is spent on channel detection. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Configure Channel Configuration Mode |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr700019.html language=enus -->
## TOPIC 00003: rfmxtdscdmaprop/attr700019.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr700019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr700019.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

Channel:User Defined:Channelization Code Property

Channel:User Defined:Channelization Code Property

**Short Name:**Channelization Code

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the channelization code of the user-defined channel. This property is used only when you set the [Channel Configuration Mode](attr700010.html) property to **User Defined**.

Use "channel*<n>*" as the selector string to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Configure User Defined Channel, RFmxTDSCDMA Configure User Defined Channel (Array) |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr701026.html language=enus -->
## TOPIC 00004: rfmxtdscdmaprop/attr701026.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr701026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr701026.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Carrier:Absolute Power (dBm) Property

ACP:Results:Carrier:Absolute Power (dBm) Property

**Short Name:**ACP Results Carrier Abs Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the absolute measured carrier power. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70102c.html language=enus -->
## TOPIC 00005: rfmxtdscdmaprop/attr70102c.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70102c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70102c.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ACP:Results:Lower Offset:Absolute Power (dBm) Property

ACP:Results:Lower Offset:Absolute Power (dBm) Property

**Short Name:**ACP Results Lower Offset Abs Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the absolute measured lower offset channel power. This value is expressed in dBm.

Use "offset*<n>*" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ACP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703002.html language=enus -->
## TOPIC 00006: rfmxtdscdmaprop/attr703002.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703002.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Integration Bandwidth (Hz) Property

CHP:Integration Bandwidth (Hz) Property

**Short Name:**CHP IBW (Hz)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the CHP carrier integration bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703006.html language=enus -->
## TOPIC 00007: rfmxtdscdmaprop/attr703006.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703006.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Count Property

CHP:Averaging:Count Property

**Short Name:**CHP Averaging Count

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](attr703007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703009.html language=enus -->
## TOPIC 00008: rfmxtdscdmaprop/attr703009.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703009.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Averaging:Type Property

CHP:Averaging:Type Property

**Short Name:**CHP Averaging Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **RMS**.

| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- |
| Log (1) | The power spectrum is averaged on a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70300c.html language=enus -->
## TOPIC 00009: rfmxtdscdmaprop/attr70300c.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70300c.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:RBW Filter:Auto Bandwidth Property

CHP:RBW Filter:Auto Bandwidth Property

**Short Name:**CHP RBW Auto

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether the measurement calculates the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the RBW you specify. |
| --- | --- |
| True (1) | RFmx TD-SCDMA automatically calculates the RBW. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70300d.html language=enus -->
## TOPIC 00010: rfmxtdscdmaprop/attr70300d.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70300d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70300d.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:RBW Filter:Bandwidth (Hz) Property

CHP:RBW Filter:Bandwidth (Hz) Property

**Short Name:**CHP RBW (Hz)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [CHP RBW Auto](attr70300c.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 5.636 kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70300e.html language=enus -->
## TOPIC 00011: rfmxtdscdmaprop/attr70300e.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70300e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70300e.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:RBW Filter:Type Property

CHP:RBW Filter:Type Property

**Short Name:**CHP RBW Filter Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **FFT Based**.

| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703011.html language=enus -->
## TOPIC 00012: rfmxtdscdmaprop/attr703011.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703011.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Sweep Time:Auto Property

CHP:Sweep Time:Auto Property

**Short Name:**CHP Sweep Time Auto

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether the measurement calculates the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time you specify in the CHP Sweep Time property. |
| --- | --- |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703012.html language=enus -->
## TOPIC 00013: rfmxtdscdmaprop/attr703012.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703012.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Sweep Time:Interval (s) Property

CHP:Sweep Time:Interval (s) Property

**Short Name:**CHP Sweep Time (s)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the sweep time when you set the [CHP Sweep Time Auto](attr703011.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.00066 s.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703014.html language=enus -->
## TOPIC 00014: rfmxtdscdmaprop/attr703014.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703014.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:All Traces Enabled Property

CHP:All Traces Enabled Property

**Short Name:**CHP All Traces Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr703015.html language=enus -->
## TOPIC 00015: rfmxtdscdmaprop/attr703015.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr703015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr703015.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CHP:Results:Carrier Absolute Power (dBm) Property

CHP:Results:Carrier Absolute Power (dBm) Property

**Short Name:**CHP Results Carrier Abs Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CHP Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706000.html language=enus -->
## TOPIC 00016: rfmxtdscdmaprop/attr706000.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706000.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Measurement Enabled Property

OBW:Measurement Enabled Property

**Short Name:**OBW Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to enable the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706003.html language=enus -->
## TOPIC 00017: rfmxtdscdmaprop/attr706003.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706003.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Number of Analysis Threads Property

OBW:Number of Analysis Threads Property

**Short Name:**OBW Num Analysis Threads

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the maximum number of threads used for parallelism for the OBW measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set might not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706004.html language=enus -->
## TOPIC 00018: rfmxtdscdmaprop/attr706004.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706004.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Span (Hz) Property

OBW:Span (Hz) Property

**Short Name:**OBW Span (Hz)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the frequency span of the OBW measurement. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal result instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706006.html language=enus -->
## TOPIC 00019: rfmxtdscdmaprop/attr706006.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706006.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Count Property

OBW:Averaging:Count Property

**Short Name:**OBW Averaging Count

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](attr706007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706007.html language=enus -->
## TOPIC 00020: rfmxtdscdmaprop/attr706007.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706007.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Enabled Property

OBW:Averaging:Enabled Property

**Short Name:**OBW Averaging Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

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
| High-level VIs | RFmxTDSCDMA OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706009.html language=enus -->
## TOPIC 00021: rfmxtdscdmaprop/attr706009.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706009.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Averaging:Type Property

OBW:Averaging:Type Property

**Short Name:**OBW Averaging Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **RMS**.

| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- |
| Log (1) | The power spectrum is averaged on a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA OBW Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70600e.html language=enus -->
## TOPIC 00022: rfmxtdscdmaprop/attr70600e.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70600e.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:RBW Filter:Type Property

OBW:RBW Filter:Type Property

**Short Name:**OBW RBW Filter Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Gaussian**.

| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| --- | --- |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA OBW Configure RBW Filter |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706012.html language=enus -->
## TOPIC 00023: rfmxtdscdmaprop/attr706012.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706012.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:All Traces Enabled Property

OBW:All Traces Enabled Property

**Short Name:**OBW All Traces Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to enable storage and retrieval of the traces after performing the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Select Measurement |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr706014.html language=enus -->
## TOPIC 00024: rfmxtdscdmaprop/attr706014.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr706014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr706014.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

OBW:Results:Absolute Power (dBm) Property

OBW:Results:Absolute Power (dBm) Property

**Short Name:**OBW Results Abs Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the absolute power measured in the OBW. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA OBW Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707000.html language=enus -->
## TOPIC 00025: rfmxtdscdmaprop/attr707000.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707000.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Measurement Enabled Property

PVT:Measurement Enabled Property

**Short Name:**PVT Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to enable the power versus time (PVT) measurement (Transmit ON/off time mask) according to the 3GPP TS 34.122 specification.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707005.html language=enus -->
## TOPIC 00026: rfmxtdscdmaprop/attr707005.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707005.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:RRC Filter Enabled Property

PVT:RRC Filter Enabled Property

**Short Name:**PVT RRC Filter Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

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

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707006.html language=enus -->
## TOPIC 00027: rfmxtdscdmaprop/attr707006.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707006.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Averaging:Enabled Property

PVT:Averaging:Enabled Property

**Short Name:**PVT Averaging Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to enable averaging for the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The PVT measurement uses the value of the PVT Averaging Count property as the number of acquisitions over which the PVT measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70700a.html language=enus -->
## TOPIC 00028: rfmxtdscdmaprop/attr70700a.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70700a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70700a.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Number of Analysis Threads Property

PVT:Number of Analysis Threads Property

**Short Name:**PVT Num Analysis Threads

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement.

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

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70700c.html language=enus -->
## TOPIC 00029: rfmxtdscdmaprop/attr70700c.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70700c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70700c.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Number of Segments Property

PVT:Number of Segments Property

**Short Name:**PVT Number of Segments

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the number of segments defined for the power versus time (PVT) measurement.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 6.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70700d.html language=enus -->
## TOPIC 00030: rfmxtdscdmaprop/attr70700d.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70700d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70700d.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Segment:Start (s) Property

PVT:Segment:Start (s) Property

**Short Name:**PVT Segment Start (s)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the start time of a specific power versus time (PVT) measurement segment. This value is expressed in seconds. The start time is defined relative to the burst start.

Use "segment<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70700e.html language=enus -->
## TOPIC 00031: rfmxtdscdmaprop/attr70700e.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70700e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70700e.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Segment:Stop (s) Property

PVT:Segment:Stop (s) Property

**Short Name:**PVT Segment Stop (s)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the stop time of a specific power versus time (PVT) measurement segment. This value is expressed in seconds. The start time is defined relative to the burst start.

Use "segment<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70700f.html language=enus -->
## TOPIC 00032: rfmxtdscdmaprop/attr70700f.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70700f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70700f.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Measurement Status Property

PVT:Results:Measurement Status Property

**Short Name:**PVT Results Meas Status

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the overall status of the power versus time (PVT) measurement.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| --- | --- |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707010.html language=enus -->
## TOPIC 00033: rfmxtdscdmaprop/attr707010.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707010.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Mean Absolute ON Power (dBm) Property

PVT:Results:Mean Absolute ON Power (dBm) Property

**Short Name:**PVT Results Mean Abs ON Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the mean ON power of the measured burst, or the averaged bursts. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707011.html language=enus -->
## TOPIC 00034: rfmxtdscdmaprop/attr707011.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707011.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Mean Absolute OFF Power (dBm) Property

PVT:Results:Mean Absolute OFF Power (dBm) Property

**Short Name:**PVT Results Mean Abs OFF Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the mean OFF power of the measured burst, or the averaged bursts. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707012.html language=enus -->
## TOPIC 00035: rfmxtdscdmaprop/attr707012.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707012.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Maximum Absolute Power (dBm) Property

PVT:Results:Maximum Absolute Power (dBm) Property

**Short Name:**PVT Results Max Abs Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the maximum power of the measured burst, or the averaged bursts. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707013.html language=enus -->
## TOPIC 00036: rfmxtdscdmaprop/attr707013.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707013.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Minimum Absolute Power (dBm) Property

PVT:Results:Minimum Absolute Power (dBm) Property

**Short Name:**PVT Results Min Abs Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the minimum observed power of the measured burst, or the averaged bursts. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707014.html language=enus -->
## TOPIC 00037: rfmxtdscdmaprop/attr707014.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707014.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Burst Width (s) Property

PVT:Results:Burst Width (s) Property

**Short Name:**PVT Results Burst Width (s)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the time interval between the time positions where the signal amplitude has reached 90 percent of the full amplitude. This value is expressed in seconds.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr707018.html language=enus -->
## TOPIC 00038: rfmxtdscdmaprop/attr707018.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr707018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr707018.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Segment:Margin (dB) Property

PVT:Results:Segment:Margin (dB) Property

**Short Name:**PVT Results Segment Margin (dB)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the power margin for an individual power versus time (PVT) measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB.

Use "segment<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70701b.html language=enus -->
## TOPIC 00039: rfmxtdscdmaprop/attr70701b.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70701b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70701b.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

PVT:Results:Segment:Mean Absolute Power (dBm) Property

PVT:Results:Segment:Mean Absolute Power (dBm) Property

**Short Name:**PVT Results Segment Mean Absolute Power (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the mean measured power corresponding to the [PVT Results Segment Margin](attr707018.html) property. This value is expressed in dBm.

Use "segment<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA PVT Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70800b.html language=enus -->
## TOPIC 00040: rfmxtdscdmaprop/attr70800b.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70800b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70800b.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Number of Offsets Property

SEM:Offset:Number of Offsets Property

**Short Name:**SEM Num Offsets

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the number of SEM offset segments.

You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708015.html language=enus -->
## TOPIC 00041: rfmxtdscdmaprop/attr708015.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708015.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:Stop Frequency (Hz) Property

SEM:Offset:Stop Frequency (Hz) Property

**Short Name:**SEM Offset Stop Freq (Hz)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the stop frequency of an SEM offset segment, relative to the carrier frequency. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708017.html language=enus -->
## TOPIC 00042: rfmxtdscdmaprop/attr708017.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708017.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:RBW Filter:Bandwidth (Hz) Property

SEM:Offset:RBW Filter:Bandwidth (Hz) Property

**Short Name:**SEM Offset RBW (Hz)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708018.html language=enus -->
## TOPIC 00043: rfmxtdscdmaprop/attr708018.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708018.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Offset:RBW Filter:Type Property

SEM:Offset:RBW Filter:Type Property

**Short Name:**SEM Offset RBW Filter Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the type of RBW filter used to sweep the offset segment.

Use "offset<*n*>" as the selector string to read this property.

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

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70801e.html language=enus -->
## TOPIC 00044: rfmxtdscdmaprop/attr70801e.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70801e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70801e.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Count Property

SEM:Averaging:Count Property

**Short Name:**SEM Averaging Count

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the number of acquisitions used for averaging when you set the [SEM Averaging Enabled](attr70801f.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70801f.html language=enus -->
## TOPIC 00045: rfmxtdscdmaprop/attr70801f.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70801f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70801f.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Enabled Property

SEM:Averaging:Enabled Property

**Short Name:**SEM Averaging Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

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
| High-level VIs | RFmxTDSCDMA SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708021.html language=enus -->
## TOPIC 00046: rfmxtdscdmaprop/attr708021.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708021.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708021.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Averaging:Type Property

SEM:Averaging:Type Property

**Short Name:**SEM Averaging Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **RMS**.

| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- |
| Log (1) | The power spectrum is averaged on a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA SEM Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708025.html language=enus -->
## TOPIC 00047: rfmxtdscdmaprop/attr708025.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708025.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708025.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Sweep Time:Auto Property

SEM:Sweep Time:Auto Property

**Short Name:**SEM Sweep Time Auto

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether the measurement calculates the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **True**.

| False (0) | The measurement uses the sweep time that you specify in the SEM Sweep Time property. |
| --- | --- |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA SEM Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708026.html language=enus -->
## TOPIC 00048: rfmxtdscdmaprop/attr708026.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708026.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Sweep Time:Interval (s) Property

SEM:Sweep Time:Interval (s) Property

**Short Name:**SEM Sweep Time (s)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the sweep time when you set the [SEM Sweep Time Auto](attr708025.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.00066 s.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA SEM Configure Sweep Time |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr708029.html language=enus -->
## TOPIC 00049: rfmxtdscdmaprop/attr708029.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr708029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr708029.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

SEM:Results:Measurement Status Property

SEM:Results:Measurement Status Property

**Short Name:**SEM Results Meas Status

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Indicates the overall measurement status based on the measurement limits specified by the standard for each offset segment.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

| Fail (0) | The measurement failed according to the measurement limits and criteria you set. |
| --- | --- |
| Pass (1) | The measurement passed according to the measurement limits and criteria you set. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA SEM Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr70d003.html language=enus -->
## TOPIC 00050: rfmxtdscdmaprop/attr70d003.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr70d003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr70d003.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Limited Configuration Change Property

Advanced:Limited Configuration Change Property

**Short Name:**Limited Configuration Change

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this property to help achieve faster measurements. When you set this property to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](limitations.html) topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFmxInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| --- | --- |
| No Change (1) | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency (2) | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Reference Level (3) | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the Reference Level property value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Freq and Ref Level (4) | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level (5) | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711000.html language=enus -->
## TOPIC 00051: rfmxtdscdmaprop/attr711000.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711000.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Enabled Property

ModAcc:Measurement Enabled Property

**Short Name:**ModAcc Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

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

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711002.html language=enus -->
## TOPIC 00052: rfmxtdscdmaprop/attr711002.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711002.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Synchronization Mode Property

ModAcc:Synchronization Mode Property

**Short Name:**ModAcc Sync Mode

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the synchronization mode for the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Slot**.

| Slot (0) | The measurement uses the slot synchronization mode. The slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the ModAcc Meas Length property, starting at the offset from the boundary specified by the ModAcc Meas Offset property. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the slot from which the ModAcc Meas Offset property should be considered. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. |
| --- | --- |
| Subframe (1) | The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the ModAcc Meas Length property, starting at the offset from the boundary specified by the ModAcc Meas Offset property. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot time slot. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711003.html language=enus -->
## TOPIC 00053: rfmxtdscdmaprop/attr711003.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711003.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Offset (slots) Property

ModAcc:Measurement Offset (slots) Property

**Short Name:**ModAcc Meas Offset (slots)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the [ModAcc Sync Mode](attr711002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711004.html language=enus -->
## TOPIC 00054: rfmxtdscdmaprop/attr711004.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711004.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Measurement Length (slots) Property

ModAcc:Measurement Length (slots) Property

**Short Name:**ModAcc Meas Length (slots)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the measurement length for the ModAcc measurement. This value is expressed in traffic slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711006.html language=enus -->
## TOPIC 00055: rfmxtdscdmaprop/attr711006.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711006.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Slot Type Property

ModAcc:Slot Type Property

**Short Name:**ModAcc Slot Type

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the type of the time slot for the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **Traffic**.

| Traffic (0) | The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. |
| --- | --- |
| Pilot (1) | The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Configure Slot Type |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711009.html language=enus -->
## TOPIC 00056: rfmxtdscdmaprop/attr711009.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711009.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711009.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

Midamble:Shift (chips) Property

Midamble:Shift (chips) Property

**Short Name:**Midamble Shift (chips)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the midamble shift used when you set the [Midamble Auto Detection Mode](attr711007.html) property to **Off**. This value is expressed in chips.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 8.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71100b.html language=enus -->
## TOPIC 00057: rfmxtdscdmaprop/attr71100b.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71100b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71100b.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Averaging:Enabled Property

ModAcc:Averaging:Enabled Property

**Short Name:**ModAcc Averaging Enabled

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies whether to enable averaging for the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The ModAcc measurement uses the value of the ModAcc Averaging Count property as the number of acquisitions over which the ModAcc measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Configure Averaging |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71108a.html language=enus -->
## TOPIC 00058: rfmxtdscdmaprop/attr71108a.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71108a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71108a.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Midamble:RMS EVM (%) Property

ModAcc:Results:Midamble:RMS EVM (%) Property

**Short Name:**ModAcc Results RMS Midamble EVM (%)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71108b.html language=enus -->
## TOPIC 00059: rfmxtdscdmaprop/attr71108b.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71108b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71108b.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Midamble:Peak EVM (%) Property

ModAcc:Results:Midamble:Peak EVM (%) Property

**Short Name:**ModAcc Results Pk Midamble EVM (%)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

&gt;Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71108c.html language=enus -->
## TOPIC 00060: rfmxtdscdmaprop/attr71108c.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71108c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71108c.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Midamble:RMS Magnitude Error (%) Property

ModAcc:Results:Midamble:RMS Magnitude Error (%) Property

**Short Name:**ModAcc Results RMS Midamble Magnitude Error (%)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71108f.html language=enus -->
## TOPIC 00061: rfmxtdscdmaprop/attr71108f.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71108f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71108f.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Midamble:Power (dBm) Property

ModAcc:Results:Midamble:Power (dBm) Property

**Short Name:**ModAcc Results Midamble Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the midamble power, averaged over all measured slots. This value is expressed in dBm.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711090.html language=enus -->
## TOPIC 00062: rfmxtdscdmaprop/attr711090.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711090.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711090.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Midamble:Code Property

ModAcc:Results:Midamble:Code Property

**Short Name:**ModAcc Results Midamble Code

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the midamble code.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711091.html language=enus -->
## TOPIC 00063: rfmxtdscdmaprop/attr711091.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711091.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711091.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Midamble:Shift (chips) Property

ModAcc:Results:Midamble:Shift (chips) Property

**Short Name:**ModAcc Results Midamble Shift (chips)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the midamble code shift. This value is expressed in chips.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711094.html language=enus -->
## TOPIC 00064: rfmxtdscdmaprop/attr711094.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711094.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711094.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:RMS Magnitude Error (%) Property

ModAcc:Results:Data:RMS Magnitude Error (%) Property

**Short Name:**ModAcc Results RMS Data Magnitude Error (%)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711096.html language=enus -->
## TOPIC 00065: rfmxtdscdmaprop/attr711096.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711096.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711096.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Rho Property

ModAcc:Results:Data:Rho Property

**Short Name:**ModAcc Results Data Rho

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the data rho value, averaged over all active time slots and all averaging iterations.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711097.html language=enus -->
## TOPIC 00066: rfmxtdscdmaprop/attr711097.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711097.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711097.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Peak CDE (dB) Property

ModAcc:Results:Data:Peak CDE (dB) Property

**Short Name:**ModAcc Results Pk Data CDE (dB)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the value of the peak code domain error (CDE) among all active time slots. This value is expressed in dB. The peak CDE value is averaged over all averaging iterations.

The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor.

The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform.

A fixed spreading factor of 16 is used. The CDEs are calculated separately for I and Q branches.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr711099.html language=enus -->
## TOPIC 00067: rfmxtdscdmaprop/attr711099.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr711099.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr711099.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Peak CDE Code Property

ModAcc:Results:Data:Peak CDE Code Property

**Short Name:**ModAcc Results Pk Data CDE Code

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the peak channelization code of the channel corresponding to the measured value of the [ModAcc Results Max Pk Data CDE](attr7110bf.html) property.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71109d.html language=enus -->
## TOPIC 00068: rfmxtdscdmaprop/attr71109d.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71109d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71109d.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Peak Active CDE Number of Channels Property

ModAcc:Results:Data:Peak Active CDE Number of Channels Property

**Short Name:**ModAcc Results Pk Data Active CDE Num Channels

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the number of channels used to determine the peak active code domain error (CDE).

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71109e.html language=enus -->
## TOPIC 00069: rfmxtdscdmaprop/attr71109e.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71109e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71109e.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Field 1 Power (dBm) Property

ModAcc:Results:Data:Field 1 Power (dBm) Property

**Short Name:**ModAcc Results Data Field 1 Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the data field 1 power, averaged over all measured active time slots. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71109f.html language=enus -->
## TOPIC 00070: rfmxtdscdmaprop/attr71109f.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71109f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71109f.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Field 2 Power (dBm) Property

ModAcc:Results:Data:Field 2 Power (dBm) Property

**Short Name:**ModAcc Results Data Field 2 Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the data field 2 power, averaged over all measured active time slots. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr7110a0.html language=enus -->
## TOPIC 00071: rfmxtdscdmaprop/attr7110a0.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr7110a0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr7110a0.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

ModAcc:Results:Data:Peak RCDE (dB) Property

ModAcc:Results:Data:Peak RCDE (dB) Property

**Short Name:**ModAcc Results Pk Data RCDE (dB)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the value of the peak data relative code domain error (RCDE) among all active time slots. This value is expressed in dB. The peak RCDE value is averaged over all averaging iterations.

The CDEs are calculated by projecting the descrambled error vector onto the codes of each active channel.

The RCDE is the ratio of the mean power of the projection onto that code to the mean power of the corresponding active channel in the reference waveform.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr713010.html language=enus -->
## TOPIC 00072: rfmxtdscdmaprop/attr713010.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr713010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr713010.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Mean RMS Symbol EVM (%) Property

CDA:Results:Mean RMS Symbol EVM (%) Property

**Short Name:**CDA Results Mean RMS Symbol EVM (%)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr713013.html language=enus -->
## TOPIC 00073: rfmxtdscdmaprop/attr713013.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr713013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr713013.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Mean RMS Symbol Phase Error (deg) Property

CDA:Results:Mean RMS Symbol Phase Error (deg) Property

**Short Name:**CDA Results Mean RMS Symbol Phase Error (deg)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr713014.html language=enus -->
## TOPIC 00074: rfmxtdscdmaprop/attr713014.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr713014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr713014.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:I/Q Origin Offset (dB) Property

CDA:Results:I/Q Origin Offset (dB) Property

**Short Name:**CDA Results I/Q Origin Offset (dB)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr713015.html language=enus -->
## TOPIC 00075: rfmxtdscdmaprop/attr713015.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr713015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr713015.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:I/Q Gain Imbalance (dB) Property

CDA:Results:I/Q Gain Imbalance (dB) Property

**Short Name:**CDA Results I/Q Gain Imbalance (dB)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr713016.html language=enus -->
## TOPIC 00076: rfmxtdscdmaprop/attr713016.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr713016.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr713016.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:I/Q Quadrature Error (deg) Property

CDA:Results:I/Q Quadrature Error (deg) Property

**Short Name:**CDA Results I/Q Quadrature Error (deg)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr713019.html language=enus -->
## TOPIC 00077: rfmxtdscdmaprop/attr713019.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr713019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr713019.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Mean Total Power (dBm) Property

CDA:Results:Mean Total Power (dBm) Property

**Short Name:**CDA Results Mean Total Pwr (dBm)

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71301a.html language=enus -->
## TOPIC 00078: rfmxtdscdmaprop/attr71301a.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71301a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71301a.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Results:Mean Total Active Power (dB or dBm) Property

CDA:Results:Mean Total Active Power (dB or dBm) Property

**Short Name:**CDA Results Mean Total Active Pwr

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the [CDA Pwr Unit](attr71300b.html) property to **dB**, or in dBm, if you set the CDA Pwr Unit property to **dBm**. The total active code power is averaged over all averaging iterations.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA CDA Fetch |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/attr71302c.html language=enus -->
## TOPIC 00079: rfmxtdscdmaprop/attr71302c.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/attr71302c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/attr71302c.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

CDA:Averaging:Count Property

CDA:Averaging:Count Property

**Short Name:**CDA Averaging Count

Property of [RFmxTDSCDMA](crfmxtdscdma.html)

Specifies the number of acquisitions used for averaging when you set the [CDA Averaging Enabled](attr71302a.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-tdscdma-prop path=rfmxtdscdmaprop/crfmxtdscdma.html language=enus -->
## TOPIC 00080: rfmxtdscdmaprop/crfmxtdscdma.html

- bundle_id: `rfmx-tdscdma-prop`
- source_path: `rfmxtdscdmaprop/crfmxtdscdma.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-tdscdma-prop/raw/resource/enus/rfmxtdscdmaprop/crfmxtdscdma.html
- document_id: `rfmx-tdscdma-prop`
- page_type: `leaf`
- content_type: ``

RFmxTDSCDMA Properties

RFmxTDSCDMA Properties

Use the RFmxTDSCDMA properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the Selector Strings used to access all subsequent properties in this instance of the property node. Details |
| Selected Ports | Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. Details |
| Center Frequency (Hz) | Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. Details |
| Reference Level | Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. Details |
| External Attenuation (dB) | Specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. Details |
| Reference Level Headroom | Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level. Details |
| Trigger:Type | Specifies the trigger type. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:IQ Power Edge:Source | Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Level | Specifies the threshold above or below which the signal analyzer triggers, depending on the value of the IQ Power Edge Slope property. This value is expressed in dB when the IQ Power Edge Level Type property is set to Relative or in dBm when the IQ Power Edge Level Type property is set to Absolute. Details |
| Trigger:IQ Power Edge:Level Type | Specifies the reference for the IQ Power Edge Level property. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:IQ Power Edge:Slope | Specifies whether the device asserts the trigger when the signal power is rising or when the signal power is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. Details |
| Trigger:Delay (s) | Specifies the trigger delay time. This value is expressed in seconds. Details |
| Trigger:Minimum Quiet Time:Mode | Specifies whether the measurement calculates the minimum quiet time used for triggering. Details |
| Trigger:Minimum Quiet Time:Duration (s) | Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to Falling Slope, the signal is quiet above the trigger level. Details |
| Channel:Configuration Mode | Specifies whether to detect the channels automatically or to use a specified channel configuration. Details |
| Channel:User Defined:Number of Channels | Specifies the number of user-defined channels. This property is used only when you set the Channel Configuration Mode property to User Defined. Details |
| Channel:User Defined:Channel Type | Specifies the channel type of the user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the selector string to configure or read this property. Details |
| Channel:User Defined:Slot Index | Specifies the slot index of the user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the selector string to configure or read this property. Details |
| Channel:User Defined:Modulation Type | Specifies the modulation type of the user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the selector string to configure or read this property. Details |
| Channel:User Defined:Slot Format | Specifies the spreading factor, the number of TFCI code words, the number of transmit power control bits, and the number of synchronization shift bits. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the selector string to configure or read this property. Details |
| Channel:User Defined:Channelization Code | Specifies the channelization code of the user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel<n>" as the selector string to configure or read this property. Details |
| Scrambling:Uplink:Code | Specifies the scrambling code and the basic midamble code for uplink transmission. Details |
| Midamble:Auto Detection Mode | Specifies the midamble auto detection mode. Details |
| Midamble:Shift (chips) | Specifies the midamble shift used when you set the Midamble Auto Detection Mode property to Off. This value is expressed in chips. Details |
| Maximum Number of Users | Configures the maximum number of users. Details |
| Pilot Code | Specifies the SYNC-UL code used by the uplink pilot time slot (UpPTS). This property is used when the ModAcc Sync Mode property is set to Subframe, or the ModAcc Slot Type property is set to Pilot. Details |
| ModAcc:Measurement Enabled | Specifies whether to enable the ModAcc measurement. Details |
| ModAcc:Synchronization Mode | Specifies the synchronization mode for the ModAcc measurement. Details |
| ModAcc:Slot Type | Specifies the type of the time slot for the ModAcc measurement. Details |
| ModAcc:Measurement Offset (slots) | Specifies the measurement offset that is skipped by the ModAcc measurement from the synchronization boundary. This value is expressed in traffic slots. The synchronization boundary is specified by the ModAcc Sync Mode property. Details |
| ModAcc:Measurement Length (slots) | Specifies the measurement length for the ModAcc measurement. This value is expressed in traffic slots. Details |
| ModAcc:Spectrum Inverted | Specifies whether the spectrum of the signal is inverted. Details |
| ModAcc:IQ Offset Removal Enabled | Specifies whether to remove the I/Q offset before the ModAcc measurement. Details |
| ModAcc:IQ Gain Imbalance Removal Enabled | Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement. Details |
| ModAcc:IQ Quadrature Error Removal Enabled | Specifies whether to remove the I/Q quadrature error before the ModAcc measurement. Details |
| ModAcc:RRC Filter Enabled | Specifies whether to enable the RRC filter in the ModAcc measurement. Use this property to disable the filter if the received signal is already RRC-filtered. Details |
| ModAcc:Averaging:Enabled | Specifies whether to enable averaging for the ModAcc measurement. Details |
| ModAcc:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ModAcc Averaging Enabled property to True. Details |
| ModAcc:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ModAcc measurement. Details |
| ModAcc:Results:RMS Composite EVM (%) | Returns the value of the time-slot based RMS of the composite EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Peak Composite EVM (%) | Returns the peak composite EVM among all active time slots and averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:RMS Composite Magnitude Error (%) | Returns the RMS of the composite magnitude error averaged over all active time slots and averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:RMS Composite Phase Error (deg) | Returns the RMS of the composite phase error, averaged over all active time slots and averaging iterations. This value is expressed in degrees. Details |
| ModAcc:Results:I/Q Origin Offset (dB) | Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. Details |
| ModAcc:Results:I/Q Gain Imbalance (dB) | Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. Details |
| ModAcc:Results:I/Q Quadrature Error (deg) | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. Details |
| ModAcc:Results:Frequency Error (Hz) | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. Details |
| ModAcc:Results:Chip Rate Error (ppm) | Returns the chip rate error. This value is expressed in ppm. Details |
| ModAcc:Results:Composite Rho | Returns the composite value of rho, averaged over all active time slots and all averaging iterations. Details |
| ModAcc:Results:Maximum Composite Rho | Returns the maximum value of the composite rho among all active time slots and averaging iterations. Details |
| ModAcc:Results:Midamble:RMS EVM (%) | Returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Midamble:Peak EVM (%) | >Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Midamble:RMS Magnitude Error (%) | Returns the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Midamble:RMS Phase Error (deg) | Returns the RMS of the midamble phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. Details |
| ModAcc:Results:Midamble:Rho | Returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations. Details |
| ModAcc:Results:Midamble:Power (dBm) | Returns the midamble power, averaged over all measured slots. This value is expressed in dBm. Details |
| ModAcc:Results:Midamble:Code | Returns the midamble code. Details |
| ModAcc:Results:Midamble:Shift (chips) | Returns the midamble code shift. This value is expressed in chips. Details |
| ModAcc:Results:Data:RMS EVM (%) | Returns the RMS of the data EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Data:Peak EVM (%) | Returns the peak data EVM among all active time slots and averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Data:RMS Magnitude Error (%) | Returns the RMS of the data magnitude error, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Data:RMS Phase Error (deg) | Returns the RMS of the data phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. Details |
| ModAcc:Results:Data:Rho | Returns the data rho value, averaged over all active time slots and all averaging iterations. Details |
| ModAcc:Results:Data:Peak CDE (dB) | Returns the value of the peak code domain error (CDE) among all active time slots. This value is expressed in dB. The peak CDE value is averaged over all averaging iterations. Details |
| ModAcc:Results:Data:Maximum Peak CDE (dB) | Returns the maximum peak code domain error (CDE) among all active time slots and averaging iterations. This value is expressed in dB. Details |
| ModAcc:Results:Data:Peak CDE Spreading Factor | Returns the spreading factor used to retrieve the peak code domain error (CDE) of the channel corresponding to measured value of the ModAcc Results Max Pk Data CDE property. Details |
| ModAcc:Results:Data:Peak CDE Code | Returns the peak channelization code of the channel corresponding to the measured value of the ModAcc Results Max Pk Data CDE property. Details |
| ModAcc:Results:Data:Peak Active CDE (dB) | Returns the value of the peak data active code domain error (CDE) among all physical channels and active time slots. This value is expressed in dB. The peak data active CDEs are averaged over all averaging iterations. Details |
| ModAcc:Results:Data:Maximum Peak Active CDE (dB) | Returns the maximum value of the peak data active code domain error (CDE) among all active physical channels, active time slots and averaging iterations. This value is expressed in dB. Details |
| ModAcc:Results:Data:Peak Active CDE Spreading Factor | Returns the spreading factor used to retrieve the peak code domain error (CDE) of the active physical channel corresponding to the measured value of the ModAcc Results Max Pk Data Active CDE property. Details |
| ModAcc:Results:Data:Peak Active CDE Code | Returns the peak channelization code of the channel corresponding to the measured value of the ModAcc Results Max Pk Data Active CDE property. Details |
| ModAcc:Results:Data:Peak Active CDE Number of Channels | Returns the number of channels used to determine the peak active code domain error (CDE). Details |
| ModAcc:Results:Data:Peak RCDE (dB) | Returns the value of the peak data relative code domain error (RCDE) among all active time slots. This value is expressed in dB. The peak RCDE value is averaged over all averaging iterations. Details |
| ModAcc:Results:Data:Maximum Peak RCDE (dB) | Returns the maximum value of the peak relative code domain error (RDCE) among all active time slots and averaging iterations. This value is expressed in dB. Details |
| ModAcc:Results:Data:Peak RCDE Spreading Factor | Returns the spreading factor of the channel corresponding to the value of the measured ModAcc Results Max Pk Data RCDE property. Details |
| ModAcc:Results:Data:Peak RCDE Code | Returns the channelization code of the channel corresponding to the value of the measured ModAcc Results Max Pk Data RCDE property. Details |
| ModAcc:Results:Data:Field 1 Power (dBm) | Returns the data field 1 power, averaged over all measured active time slots. This value is expressed in dBm. Details |
| ModAcc:Results:Data:Field 2 Power (dBm) | Returns the data field 2 power, averaged over all measured active time slots. This value is expressed in dBm. Details |
| ModAcc:Results:Detected Channel:Number of Detected Channels | Returns the number of detected active channels. If the averaging is enabled, this property returns the number of detected channels of the last averaging iteration. Details |
| ModAcc:Results:Detected Channel:Slot Index | Returns the slot index of the detected channel within the set of active channels. If the averaging is enabled, this property refers to the last averaging iteration. Use "channel<n>" as the selector string to read this result. Details |
| ModAcc:Results:Detected Channel:Spreading Factor | Returns the spreading factor of the selected channel within the set of active channels. If the averaging is enabled, this property refers to the last averaging iteration. Use "channel<n>" as the selector string to read this result. Details |
| ModAcc:Results:Detected Channel:Modulation Type | Returns the modulation type of the selected channel within the set of active channels. If the averaging is enabled, this property refers to the last averaging iteration. Use "channel<n>" as the selector string to read this result. Details |
| ModAcc:Results:Detected Channel:Channelization Code | Returns the channelization code of the selected channel within the set of active channels. If the averaging is enabled, this property refers to the last averaging iteration. Use "channel<n>" as the selector string to read this result. Details |
| ModAcc:Results:Pilot:RMS EVM (%) | Returns the RMS of the pilot EVM, averaged over all averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Pilot:Peak EVM (%) | Returns the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Pilot:RMS Magnitude Error (%) | Returns the RMS of the pilot magnitude error, averaged over all the averaging iterations. This value is expressed as a percentage. Details |
| ModAcc:Results:Pilot:RMS Phase Error (deg) | Returns the RMS of the pilot phase error, averaged over all averaging iterations. This value is expressed in degrees. Details |
| ModAcc:Results:Pilot:Rho | Returns the pilot Rho value, averaged over all averaging iterations. Details |
| ACP:Measurement Enabled | Specifies whether to enable the ACP measurement. Details |
| ACP:Carrier:Integration Bandwidth (Hz) | Returns the ACP carrier integration bandwidth. This value is expressed in Hz. Details |
| ACP:Offset:Number of Offsets | Specifies the number of offsets for the ACP measurement. Details |
| ACP:Offset:Frequency (Hz) | Returns the frequency of an ACP offset channel, relative to the carrier frequency. This value is expressed in Hz. Details |
| ACP:Offset:Integration Bandwidth (Hz) | Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. Details |
| ACP:RBW Filter:Auto Bandwidth | Specifies whether the measurement calculates the RBW. Details |
| ACP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the ACP RBW Auto property to False. This value is expressed in Hz. Details |
| ACP:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| ACP:Sweep Time:Auto | Specifies whether the measurement calculates the sweep time. Details |
| ACP:Sweep Time:Interval (s) | Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| ACP:Measurement Method | Specifies the method for performing the ACP measurement. Details |
| ACP:Noise Compensation Enabled | Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Details |
| ACP:Averaging:Enabled | Specifies whether to enable averaging for the ACP measurement. Details |
| ACP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True. Details |
| ACP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. Details |
| ACP:FFT:Overlap Mode | Specifies how overlapping is applied when computing the FFT of the acquired samples. Details |
| ACP:FFT:Overlap (%) | Returns the number of samples to overlap between consecutive chunks while performing FFT. Details |
| ACP:Advanced:IF Output Power Offset Auto | Specifies whether the measurement calculates an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This property is used only if you set the ACP Meas Method property to Dynamic Range. Details |
| ACP:Advanced:Near IF Output Power Offset (dB) | Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False. Details |
| ACP:Advanced:Far IF Output Power Offset (dB) | Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False. Details |
| ACP:Advanced:Sequential FFT Size | Specifies the FFT size when you set the ACP Meas Method property to Sequential FFT. Details |
| ACP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. Details |
| ACP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the ACP measurement. Details |
| ACP:Results:Carrier:Absolute Power (dBm) | Returns the absolute measured carrier power. This value is expressed in dBm. Details |
| ACP:Results:Lower Offset:Absolute Power (dBm) | Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| ACP:Results:Lower Offset:Relative Power (dB) | Returns the lower offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Details |
| ACP:Results:Upper Offset:Absolute Power (dBm) | Returns the absolute measured upper offset channel power. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| ACP:Results:Upper Offset:Relative Power (dB) | Returns the upper offset channel power measured relative to the integrated power of the power reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Details |
| CHP:Measurement Enabled | Specifies whether to enable the CHP measurement. Details |
| CHP:Integration Bandwidth (Hz) | Returns the CHP carrier integration bandwidth. This value is expressed in Hz. Details |
| CHP:RBW Filter:Auto Bandwidth | Specifies whether the measurement calculates the RBW. Details |
| CHP:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the CHP RBW Auto property to False. This value is expressed in Hz. Details |
| CHP:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| CHP:Sweep Time:Auto | Specifies whether the measurement calculates the sweep time. Details |
| CHP:Sweep Time:Interval (s) | Specifies the sweep time when you set the CHP Sweep Time Auto property to False. This value is expressed in seconds. Details |
| CHP:Averaging:Enabled | Specifies whether to enable averaging for the CHP measurement. Details |
| CHP:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. Details |
| CHP:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. Details |
| CHP:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. Details |
| CHP:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the CHP measurement. Details |
| CHP:Results:Carrier Absolute Power (dBm) | Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. Details |
| OBW:Measurement Enabled | Specifies whether to enable the OBW measurement. Details |
| OBW:Span (Hz) | Returns the frequency span of the OBW measurement. This value is expressed in Hz. Details |
| OBW:RBW Filter:Auto Bandwidth | Specifies whether the measurement calculates the RBW. Details |
| OBW:RBW Filter:Bandwidth (Hz) | Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the OBW RBW Auto property to False. This value is expressed in Hz. Details |
| OBW:RBW Filter:Type | Specifies the shape of the digital RBW filter. Details |
| OBW:Sweep Time:Auto | Specifies whether the measurement calculates the sweep time. Details |
| OBW:Sweep Time:Interval (s) | Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. Details |
| OBW:Averaging:Enabled | Specifies whether to enable averaging for the OBW measurement. Details |
| OBW:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. Details |
| OBW:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. Details |
| OBW:All Traces Enabled | Specifies whether to enable storage and retrieval of the traces after performing the OBW measurement. Details |
| OBW:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the OBW measurement. Details |
| OBW:Results:Occupied Bandwidth (Hz) | Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. Details |
| OBW:Results:Absolute Power (dBm) | Returns the absolute power measured in the OBW. This value is expressed in dBm. Details |
| OBW:Results:Start Frequency (Hz) | Returns the start frequency of the OBW. This value is expressed in Hz. Details |
| OBW:Results:Stop Frequency (Hz) | Returns the stop frequency of the OBW. This value is expressed in Hz. Details |
| SEM:Measurement Enabled | Specifies whether to enable the SEM measurement. Details |
| SEM:Carrier:Integration Bandwidth (Hz) | Returns the SEM carrier integration bandwidth. This value is expressed in Hz. Details |
| SEM:Offset:Number of Offsets | Returns the number of SEM offset segments. Details |
| SEM:Offset:Start Frequency (Hz) | Returns the start frequency of an SEM offset segment, relative to the carrier frequency. This value is expressed in Hz. Details |
| SEM:Offset:Stop Frequency (Hz) | Returns the stop frequency of an SEM offset segment, relative to the carrier frequency. This value is expressed in Hz. Details |
| SEM:Offset:RBW Filter:Bandwidth (Hz) | Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz. Details |
| SEM:Offset:RBW Filter:Type | Returns the type of RBW filter used to sweep the offset segment. Details |
| SEM:Offset:Bandwidth Integral | Returns the bandwidth integral for a specific offset segment. A bandwidth integral greater than 1 indicates that an RBW filter of a narrower bandwidth is used for the offset segment measurement, and digital processing is used to achieve the RBW defined for the offset segment. The offset segment RBW is calculated using the following formula: offset segment RBW = RBW * BW integral Details |
| SEM:Sweep Time:Auto | Specifies whether the measurement calculates the sweep time. Details |
| SEM:Sweep Time:Interval (s) | Specifies the sweep time when you set the SEM Sweep Time Auto property to False. This value is expressed in seconds. Details |
| SEM:Averaging:Enabled | Specifies whether to enable averaging for the SEM measurement. Details |
| SEM:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True. Details |
| SEM:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. Details |
| SEM:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. Details |
| SEM:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the SEM measurement. Details |
| SEM:Results:Measurement Status | Indicates the overall measurement status based on the measurement limits specified by the standard for each offset segment. Details |
| SEM:Results:Carrier:Absolute Integrated Power (dBm) | Returns the measurement absolute carrier power. This value is expressed in dBm. Details |
| SEM:Results:Lower Offset:Measurement Status | Indicates the lower offset segment measurement status based on the measurement limits specified by the standard. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Absolute Integrated Power (dBm) | Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Relative Integrated Power (dB) | Returns the power measured in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Absolute Peak Power (dBm) | Returns the peak absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Relative Peak Power (dB) | Returns the peak power measured in the lower (negative) offset segment relative to the peak power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Margin (dB) | Returns the margin from the limit mask. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Margin Absolute Power (dBm) | Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Margin Relative Power (dB) | Returns the power at which the margin occurred in the lower (negative) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Lower Offset:Margin Frequency (Hz) | Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Measurement Status | Indicates the upper offset measurement status based on measurement limits specified by the standard. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Absolute Integrated Power (dBm) | Returns the absolute power measured in the upper (positive) offset segment. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Relative Integrated Power (dB) | Returns the power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Absolute Peak Power (dBm) | Returns the peak absolute power measured in the upper (positive) offset segment. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Relative Peak Power (dB) | Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. Use "offset<n>" as the selector string to read this result Details |
| SEM:Results:Upper Offset:Peak Frequency (Hz) | Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Margin (dB) | Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Margin Absolute Power (dBm) | Returns the power at which the margin occurred in the upper (positive) offset segment, relative to the integrated or peak power of the reference carrier. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Margin Relative Power (dB) | Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Details |
| SEM:Results:Upper Offset:Margin Frequency (Hz) | Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Details |
| CDA:Measurement Enabled | Specifies whether to enable the code domain analysis (CDA) measurement. Details |
| CDA:Synchronization Mode | Specifies the synchronization mode for the code domain analysis (CDA) measurement. Currently, only the Slot mode is supported. Details |
| CDA:Measurement Offset (slots) | Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the CDA Sync Mode property. Details |
| CDA:Base Spreading Factor | Specifies the base spreading factor for code domain analysis. Details |
| CDA:Measurement Channel Spreading Factor | Specifies the spreading factor of the channel on which to perform the code domain analysis (CDA) measurement. Details |
| CDA:Measurement Channel Channelization Code | Specifies the channelization code of the code domain analysis (CDA) measurement channel. Details |
| CDA:Spectrum Inverted | Specifies whether the spectrum of the signal is inverted. Details |
| CDA:IQ Offset Removal Enabled | Specifies whether to remove the I/Q offset before the code domain analysis (CDA) measurement. Details |
| CDA:IQ Gain Imbalance Removal Enabled | Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. Details |
| CDA:IQ Quadrature Error Removal Enabled | Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. Details |
| CDA:Power Unit | Specifies the measurement unit of the code domain power (CDP) results. Details |
| CDA:RRC Filter Enabled | Specifies whether to enable the RRC filter. Details |
| CDA:Averaging:Enabled | Specifies whether to enable averaging for the code domain analysis (CDA) measurement. Details |
| CDA:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the CDA Averaging Enabled property to True. Details |
| CDA:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA) measurement. Details |
| CDA:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the code domain analysis (CDA) measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. Details |
| CDA:Results:Mean Symbol Power (dB or dBm) | Returns the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the CDA Pwr Unit property to dB, or in dBm if you set the CDA Pwr Unit property to dBm. Details |
| CDA:Results:Mean RMS Symbol EVM (%) | Returns the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. Details |
| CDA:Results:Maximum Peak Symbol EVM (%) | Returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage. Details |
| CDA:Results:Mean RMS Symbol Magnitude Error (%) | Returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. Details |
| CDA:Results:Mean RMS Symbol Phase Error (deg) | Returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees. Details |
| CDA:Results:I/Q Origin Offset (dB) | Returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. Details |
| CDA:Results:I/Q Gain Imbalance (dB) | Returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. Details |
| CDA:Results:I/Q Quadrature Error (deg) | Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. Details |
| CDA:Results:Frequency Error (Hz) | Returns the frequency error averaged over all measured slots. This value is expressed in Hz. Details |
| CDA:Results:Chip Rate Error (ppm) | Returns the chip rate error. This value is expressed in ppm. Details |
| CDA:Results:Mean Total Power (dBm) | Returns the total power measured in the code domain of the base spreading factor, averaged over all averaging iterations. This value is expressed in dBm. Details |
| CDA:Results:Maximum Total Power (dBm) | Returns the maximum value of the power measured in the code domain of the base spreading factor among all averaging iterations. This value is expressed in dBm. Details |
| CDA:Results:Mean Total Active Power (dB or dBm) | Returns the total active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. The total active code power is averaged over all averaging iterations. Details |
| CDA:Results:Maximum Total Active Power (dB or dBm) | Returns the maximum value, among all averaging iterations, of total power measured in the code domain of the base spreading factor normalized to the total code domain power. This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. Details |
| CDA:Results:Mean Active Power (dB or dBm) | Returns the average of the active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. Details |
| CDA:Results:Maximum Peak Active Power (dB or dBm) | Returns the maximum value among all averaging iterations of the maximum active code power measured in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. Details |
| CDA:Results:Mean Inactive Power (dB or dBm) | Returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. Details |
| CDA:Results:Maximum Peak Inactive Power (dB or dBm) | Returns the maximum value among all averaging iterations of the highest measured code power among the set of inactive channels in the code domain of the base spreading factor, normalized to the total code domain power (CDP). This value is expressed in dB, if you set the CDA Pwr Unit property to dB, or in dBm, if you set the CDA Pwr Unit property to dBm. Details |
| PVT:Measurement Enabled | Specifies whether to enable the power versus time (PVT) measurement (Transmit ON/off time mask) according to the 3GPP TS 34.122 specification. Details |
| PVT:Measurement Method | Specifies the method for performing the power versus time (PVT) measurement. Details |
| PVT:RRC Filter Enabled | Specifies whether to enable the RRC filter. Use this property to disable the filter if the received signal is already RRC-filtered. Details |
| PVT:Averaging:Enabled | Specifies whether to enable averaging for the power versus time (PVT) measurement. Details |
| PVT:Averaging:Count | Specifies the number of acquisitions used for averaging when you set the PVT Averaging Enabled property to True. Details |
| PVT:Averaging:Type | Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the power versus time (PVT) measurement. Details |
| PVT:All Traces Enabled | Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. Details |
| PVT:Number of Analysis Threads | Specifies the maximum number of threads used for parallelism for the power versus time (PVT) measurement. Details |
| PVT:Number of Segments | Returns the number of segments defined for the power versus time (PVT) measurement. Details |
| PVT:Segment:Start (s) | Returns the start time of a specific power versus time (PVT) measurement segment. This value is expressed in seconds. The start time is defined relative to the burst start. Details |
| PVT:Segment:Stop (s) | Returns the stop time of a specific power versus time (PVT) measurement segment. This value is expressed in seconds. The start time is defined relative to the burst start. Details |
| PVT:Results:Measurement Status | Returns the overall status of the power versus time (PVT) measurement. Details |
| PVT:Results:Mean Absolute ON Power (dBm) | Returns the mean ON power of the measured burst, or the averaged bursts. This value is expressed in dBm. Details |
| PVT:Results:Mean Absolute OFF Power (dBm) | Returns the mean OFF power of the measured burst, or the averaged bursts. This value is expressed in dBm. Details |
| PVT:Results:Maximum Absolute Power (dBm) | Returns the maximum power of the measured burst, or the averaged bursts. This value is expressed in dBm. Details |
| PVT:Results:Minimum Absolute Power (dBm) | Returns the minimum observed power of the measured burst, or the averaged bursts. This value is expressed in dBm. Details |
| PVT:Results:Burst Width (s) | Returns the time interval between the time positions where the signal amplitude has reached 90 percent of the full amplitude. This value is expressed in seconds. Details |
| PVT:Results:Segment:Status | Returns the measurement status for an individual power versus time (PVT) measurement segment. Details |
| PVT:Results:Segment:Margin (dB) | Returns the power margin for an individual power versus time (PVT) measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. Details |
| PVT:Results:Segment:Margin Time (s) | Returns the position in time corresponding to the PVT Results Segment Margin property. This value is expressed in seconds. Details |
| PVT:Results:Segment:Mean Absolute Power (dBm) | Returns the mean measured power corresponding to the PVT Results Segment Margin property. This value is expressed in dBm. Details |
| PVT:Results:Segment:Maximum Absolute Power (dBm) | Returns the maximum measured power of an individual power versus time (PVT) measurement segment. This value is expressed in dBm. Details |
| PVT:Results:Segment:Minimum Absolute Power (dBm) | Returns the minimum measured power of an individual power versus time (PVT) measurement segment. This value is expressed in dBm. Details |
| PVT:Results:Midamble:Code | Returns the midamble code used for slot synchronization. Details |
| PVT:Results:Midamble:Shift (chips) | Returns the midamble code shift used for slot synchronization. This value is expressed in chips. Details |
| SlotPower:Measurement Enabled | Specifies whether to enable the SlotPower measurement. Details |
| SlotPower:Measurement Length | Specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal. Details |
| SlotPower:Spectrum Inverted | Specifies whether the spectrum of the signal is inverted. Details |
| SlotPower:RRC Filter Enabled | Specifies whether the RRC filter should be enabled or not. Details |
| Advanced:Auto Level Initial Reference Level (dBm) | Specifies the initial reference level that the RFmxTDSCDMA Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm. Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by RFmx in the locked signal configuration state. Details |
| Result Fetch Timeout (s) | Specifies the time to wait before results are available in the RFmxTDSCDMA Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxTDSCDMA Property Node waits until the measurement is complete. Details |
