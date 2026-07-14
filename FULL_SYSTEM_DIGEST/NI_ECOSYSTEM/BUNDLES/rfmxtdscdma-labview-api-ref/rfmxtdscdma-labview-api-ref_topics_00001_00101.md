# NI DOCUMENT BUNDLE: rfmxtdscdma-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxtdscdma-labview-api-ref start=1 end=101 -->
<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70101e.html language=enus -->
## TOPIC 00001: ACP:Sweep Time:Auto

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70101e.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calculates the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks

### ACP:Sweep Time:Auto

Specifies whether the measurement calculates the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ACP Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the ACP Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses the default sweep time of .00066 seconds (s). |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70101f.html language=enus -->
## TOPIC 00002: ACP:Sweep Time:Interval (s)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70101f.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### ACP:Sweep Time:Interval (s)

Specifies the sweep time when you set the [ACP Sweep Time Auto](/csh?topicname=attr70101e.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.00066 s.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ACP Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr701020.html language=enus -->
## TOPIC 00003: ACP:Noise Compensation Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr701020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr701020.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax

### ACP:Noise Compensation Enabled

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Noise Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ACP Configure Noise Compensation Enabled |
| Resettable | Yes |

| False | 0 | Disables compensation of the channel powers for the signal analyzer noise floor. |
| --- | --- | --- |
| True | 1 | Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842/5860 |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr701021.html language=enus -->
## TOPIC 00004: ACP:All Traces Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr701021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr701021.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### ACP:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70102c.html language=enus -->
## TOPIC 00005: ACP:Results:Lower Offset:Absolute Power (dBm)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70102c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70102c.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name ACP Results Lower Offset Abs Pwr (dBm) Data type cdbl.png Permissio

### ACP:Results:Lower Offset:Absolute Power (dBm)

Returns the absolute measured lower offset channel power. This value is expressed in dBm.

Use "offset*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Results Lower Offset Abs Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ACP Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70300d.html language=enus -->
## TOPIC 00006: CHP:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70300d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70300d.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the CHP RBW Auto property to False. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic

### CHP:RBW Filter:Bandwidth (Hz)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [CHP RBW Auto](/csh?topicname=attr70300c.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 5.636 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure RBW Filter |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70300e.html language=enus -->
## TOPIC 00007: CHP:RBW Filter:Type

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70300e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70300e.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FFT Based. Remarks The follo

### CHP:RBW Filter:Type

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **FFT Based**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP RBW Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure RBW Filter |
| Resettable | Yes |

| FFT Based | 0 | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| --- | --- | --- |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr703011.html language=enus -->
## TOPIC 00008: CHP:Sweep Time:Auto

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr703011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr703011.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement calculates the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks

### CHP:Sweep Time:Auto

Specifies whether the measurement calculates the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA CHP Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time you specify in the CHP Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses the default sweep time of .00066 seconds (s). |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr703014.html language=enus -->
## TOPIC 00009: CHP:All Traces Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr703014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr703014.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### CHP:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706003.html language=enus -->
## TOPIC 00010: OBW:Number of Analysis Threads

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706003.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set might not be used in calculations. The actual number of threads used depends on the problem size, system resourc

### OBW:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the OBW measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set might not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706006.html language=enus -->
## TOPIC 00011: OBW:Averaging:Count

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706006.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### OBW:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](/csh?topicname=attr706007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA OBW Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70600e.html language=enus -->
## TOPIC 00012: OBW:RBW Filter:Type

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70600e.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the digital RBW filter. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Gaussian. Remarks The follow

### OBW:RBW Filter:Type

Specifies the shape of the digital RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Gaussian**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA OBW Configure RBW Filter |
| Resettable | Yes |

| FFT Based | 0 | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| --- | --- | --- |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706010.html language=enus -->
## TOPIC 00013: OBW:Sweep Time:Interval (s)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706010.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### OBW:Sweep Time:Interval (s)

Specifies the sweep time when you set the [OBW Sweep Time Auto](/csh?topicname=attr70600f.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.00066 s.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA OBW Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706012.html language=enus -->
## TOPIC 00014: OBW:All Traces Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706012.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable storage and retrieval of the traces after performing the OBW measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### OBW:All Traces Enabled

Specifies whether to enable storage and retrieval of the traces after performing the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706013.html language=enus -->
## TOPIC 00015: OBW:Results:Occupied Bandwidth (Hz)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706013.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals. R

### OBW:Results:Occupied Bandwidth (Hz)

Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Occupied BW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706015.html language=enus -->
## TOPIC 00016: OBW:Results:Start Frequency (Hz)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706015.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings top

### OBW:Results:Start Frequency (Hz)

Returns the start frequency of the OBW. This value is expressed in Hz.

The OBW is calculated using the following formula:

*OBW* = *Stop Frequency* - *Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Start Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706016.html language=enus -->
## TOPIC 00017: OBW:Results:Stop Frequency (Hz)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr706016.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topi

### OBW:Results:Stop Frequency (Hz)

Returns the stop frequency of the OBW. This value is expressed in Hz.

The OBW is calculated using the following formula:

*OBW* = *Stop Frequency* - *Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr707000.html language=enus -->
## TOPIC 00018: PVT:Measurement Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr707000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr707000.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the power versus time (PVT) measurement (Transmit ON/off time mask) according to the 3GPP TS 34.122 specification. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informat

### PVT:Measurement Enabled

Specifies whether to enable the power versus time (PVT) measurement (Transmit ON/off time mask) according to the 3GPP TS 34.122 specification.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr707002.html language=enus -->
## TOPIC 00019: PVT:Measurement Method

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr707002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr707002.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method for performing the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value i

### PVT:Measurement Method

Specifies the method for performing the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Normal**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Meas Method |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Normal | 0 | The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. |
| --- | --- | --- |
| Dynamic Range | 1 | The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842/5860 |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708043.html language=enus -->
## TOPIC 00020: SEM:Results:Upper Offset:Absolute Peak Power (dBm)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708043.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708043.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak absolute power measured in the upper (positive) offset segment. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Abs Pk Pwr (dBm) Data type cdbl.png Permissions Rea

### SEM:Results:Upper Offset:Absolute Peak Power (dBm)

Returns the peak absolute power measured in the upper (positive) offset segment.

Use "offset*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Abs Pk Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708044.html language=enus -->
## TOPIC 00021: SEM:Results:Upper Offset:Relative Peak Power (dB)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708044.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708044.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier. Use "offset<n>" as the selector string to read this result Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Rel

### SEM:Results:Upper Offset:Relative Peak Power (dB)

Returns the peak power measured in the upper (positive) offset segment relative to the integrated power of the reference carrier.

Use "offset*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Rel Pk Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708045.html language=enus -->
## TOPIC 00022: SEM:Results:Upper Offset:Peak Frequency (Hz)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr708045.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Pk Freq (Hz) Data

### SEM:Results:Upper Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.

Use "offset*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr709002.html language=enus -->
## TOPIC 00023: SlotPower:Measurement Length

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr709002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr709002.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that

### SlotPower:Measurement Length

Specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal.

NI recommends you set a measurement length as a multiple of the number of slots per subframe, that is a multiple of 7. For example, when you set this property to 28 slots, the SlotPower measurement would report results for the 4 active time slots within the specified measurement length. In this example, 28 slots = 4 subframes.

The start of the measurement is determined by the [Trigger Type](attr700004.html) property. Although all the values of the Trigger Type property are supported for this measurement, it is recommended to set the Trigger Type property to **Digital Edge** with the following options:

- Digital trigger at the start of active slot, with the Trigger Delay property set to 0 seconds
- Digital trigger at the start of the subframe, with the Trigger Delay property configured to a value which is equal to the time offset of the active time slot from the start of the subframe

The table shows the values of the Trigger Delay property, when you specify the following active slots values:

| Active Slot | Trigger Delay (microseconds) |
| --- | --- |
| TS0 | 0 |
| TS1 | 950 |
| TS2 | 1625 |
| TS3 | 2300 |
| TS4 | 2975 |
| TS5 | 3650 |
| TS6 | 4325 |

If you cannot provide a digital trigger, you can set Trigger Type property to **IQ Power Edge** to ensure that the measurement starts at the start of an active time slot. To ensure this trigger works properly, NI recommends you complete the following steps:

- Set the IQ Power Edge Level property to allow triggering for any of the power levels in the active slots
- Run the RFmx measurement just before generating your signal

If you set the Trigger type property to **None**, the measurement will automatically detect the start of the first burst and measure the traffic slot in that position in every subframe.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 28. The minimum value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Meas Length (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA SlotPower Configure Measurement Length |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70c000.html language=enus -->
## TOPIC 00024: Result Fetch Timeout (s)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70c000.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxTDSCDMA Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxTDSCDMA Property Node waits until the measurement is complete

### Result Fetch Timeout (s)

Specifies the time to wait before results are available in the [RFmxTDSCDMA Property Node](/csh?context=rfmxtdscdma_rfmxtdscdmavi_rfmxtdscdma_property_node). This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxTDSCDMA Property Node waits until the measurement is complete.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10 s.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Result Fetch Timeout (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ACP Fetch, RFmxTDSCDMA CHP Fetch, RFmxTDSCDMA ModAcc Fetch, RFmxTDSCDMA OBW Fetch, RFmxTDSCDMA SEM Fetch |
| Resettable | Yes |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70d003.html language=enus -->
## TOPIC 00025: Advanced:Limited Configuration Change

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70d003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr70d003.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this property to help achieve faster measurements.

### Advanced:Limited Configuration Change

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this property to help achieve faster measurements. When you set this property to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](limitations.html) topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFmxInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the selector string input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Limited Configuration Change |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Disabled | 0 | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| --- | --- | --- |
| No Change | 1 | Signal configuration is locked after the first Commit of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Frequency | 2 | Signal configuration, other than center frequency and external attenuation, is locked after first Commit of the named signal configuration. Thereafter, only the Center Frequency and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Reference Level | 3 | Signal configuration, other than the reference level, is locked after first Commit of the named signal configuration. Thereafter only the Reference Level property value change will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Freq and Ref Level | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level | 5 | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr711011.html language=enus -->
## TOPIC 00026: ModAcc:IQ Gain Imbalance Removal Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr711011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr711011.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default va

### ModAcc:IQ Gain Imbalance Removal Enabled

Specifies whether to remove the I/Q gain imbalance before the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc IQ Gain Imbalance Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | Yes |

| False | 0 | The I/Q gain imbalance is not removed before the ModAcc measurement. |
| --- | --- | --- |
| True | 1 | The I/Q gain imbalance is removed before the ModAcc measurement. |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr711013.html language=enus -->
## TOPIC 00027: ModAcc:RRC Filter Enabled

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr711013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr711013.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the RRC filter in the ModAcc measurement. Use this property to disable the filter if the received signal is already RRC-filtered. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings top

### ModAcc:RRC Filter Enabled

Specifies whether to enable the RRC filter in the ModAcc measurement. Use this property to disable the filter if the received signal is already RRC-filtered.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc RRC Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | Yes |

| False | 0 | Disables the RRC filter in the ModAcc measurement. |
| --- | --- | --- |
| True | 1 | Enables the RRC filter in the ModAcc measurement. |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr71108b.html language=enus -->
## TOPIC 00028: ModAcc:Results:Midamble:Peak EVM (%)

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr71108b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxtdscdma-rc/rfmxtdscdma/attr71108b.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: >Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. You do not need to use a selector string to read this property for the default signal and result instances. Refer to the Selector Strings topic for information about the s

### ModAcc:Results:Midamble:Peak EVM (%)

&gt;Returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk Midamble EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxTDSCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxTDSCDMA Properties

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-configure-noise-compensation-enabled-vi.html language=enus -->
## TOPIC 00029: RFmxTDSCDMA ACP Configure Noise Compensation Enabled VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-configure-noise-compensation-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-configure-noise-compensation-enabled-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures channel power compensation for the inherent noise floor of the signal analyzer. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default v

### RFmxTDSCDMA ACP Configure Noise Compensation Enabled VI

Configures channel power compensation for the inherent noise floor of the signal analyzer.

[IMAGE alt='icon' src='rfmxtdscdma-acp-configure-noise-compensation-enabled-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Noise Compensation Enabled — Noise Compensation Enabled enables the channel powers to compensate for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the signal analyzer noise floor. True (1) Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842/5860 error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| True (1) | Enables compensation of the channel powers for the signal analyzer noise floor. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are remeasured. Supported Devices: PXIe-5663/5665/5668R/5830/5831/5832/5842/5860 |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-configure-number-of-offsets-vi.html language=enus -->
## TOPIC 00030: RFmxTDSCDMA ACP Configure Number of Offsets VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-configure-number-of-offsets-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-configure-number-of-offsets-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offsets for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxTDSCDMA ACP Configure Number of Offsets VI

Configures the number of offsets for the ACP measurement.

[IMAGE alt='icon' src='rfmxtdscdma-acp-configure-number-of-offsets-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Offsets — Number of Offsets specifies the number of offset channels. The default value is 2. Valid values are constrained by the bandwidth of the signal analyzer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00031: RFmxTDSCDMA ACP Fetch Spectrum VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-spectrum-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxTDSCDMA ACP Fetch Spectrum VI

Fetches the spectrum used for the ACP measurement.

[IMAGE alt='icon' src='rfmxtdscdma-acp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |

Parent topic:

RFmxTDSCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-vi.html language=enus -->
## TOPIC 00032: RFmxTDSCDMA ACP Fetch VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ACP measurement results. icon

### RFmxTDSCDMA ACP Fetch VI

Fetches the ACP measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-acp-fetch-vi.png']

- [RFmxTDSCDMA ACP Fetch Carrier Absolute Power VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-carrier-absolute-power-vi.html) Returns the absolute carrier power.
- [RFmxTDSCDMA ACP Fetch Offset Measurement VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-offset-measurement-vi.html) Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.
- [RFmxTDSCDMA ACP Fetch Offset Measurement (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-offset-measurement-array-vi.html) Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the integrated power of the power reference carrier.
- [RFmxTDSCDMA ACP Fetch Spectrum VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-spectrum-vi.html) Fetches the spectrum used for the ACP measurement.
- [RFmxTDSCDMA ACP Fetch Relative Powers Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-relative-powers-trace-vi.html) Fetches the relative powers trace for the ACP measurement.
- [RFmxTDSCDMA ACP Fetch Absolute Powers Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-acp-fetch-absolute-powers-trace-vi.html) Fetches the absolute powers trace for ACP measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00033: RFmxTDSCDMA Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-analyze-iq-1-wfm-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in the IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recomme

### RFmxTDSCDMA Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in the **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmxTDSCDMA Commit

[IMAGE alt='icon' src='rfmxtdscdma-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to default result instance. Example: "" "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and the result name. The result name can be specified either through this input or through the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with the option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex I/Q waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for the first record and FALSE for the subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input for Fetch VIs when using named signal configurations or named results. error out — error out returns error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxTDSCDMA Analyze2 VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-build-channel-string-vi.html language=enus -->
## TOPIC 00034: RFmxTDSCDMA Build Channel String VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-build-channel-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-build-channel-string-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with channel-specific configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the s

### RFmxTDSCDMA Build Channel String VI

Creates a selector string to use with channel-specific configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxtdscdma-build-channel-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Channel Number — Channel Number specifies the channel number for building the selector string. Selector String Out — Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-build-segment-string-vi.html language=enus -->
## TOPIC 00035: RFmxTDSCDMA Build Segment String VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-build-segment-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-build-segment-string-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Selector String Selector String spec

### RFmxTDSCDMA Build Segment String VI

Creates the segment string to use as the selector string with the power versus time (PVT) segment configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxtdscdma-build-segment-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Segment Number — Segment Number specifies the segment number for building the selector string. Selector String Out — Selector String Out returns the selector string you can use in the Selector String input for configuration VIs, fetch VIs, or the RFmxTDSCDMA Initiate VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-maximum-code-domain-power-trace-vi.html language=enus -->
## TOPIC 00036: RFmxTDSCDMA CDA Fetch Maximum Code Domain Power Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-maximum-code-domain-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-maximum-code-domain-power-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum hold trace of the power measured in the code domain of the base spreading factor. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal inst

### RFmxTDSCDMA CDA Fetch Maximum Code Domain Power Trace VI

Fetches the maximum hold trace of the power measured in the code domain of the base spreading factor.

[IMAGE alt='icon' src='rfmxtdscdma-cda-fetch-maximum-code-domain-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Code Domain Powers (dB) — Maximum Code Domain Powers returns an array of the max hold traces of the code powers measured in the code domain of the base spreading factor. This value is expressed in dB. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-maximum-symbol-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00037: RFmxTDSCDMA CDA Fetch Maximum Symbol Magnitude Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-maximum-symbol-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-maximum-symbol-magnitude-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum hold trace of the symbol magnitude error for the code domain analysis (CDA) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default sign

### RFmxTDSCDMA CDA Fetch Maximum Symbol Magnitude Error Trace VI

Returns the maximum hold trace of the symbol magnitude error for the code domain analysis (CDA) measurement.

[IMAGE alt='icon' src='rfmxtdscdma-cda-fetch-maximum-symbol-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Symbol Magnitude Error (%) — Maximum Symbol Magnitude Error returns an array of the maximum hold traces of the symbol magnitude error for the CDA measurement. This value is expressed as a percentage. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-mean-symbol-phase-error-trace-vi.html language=enus -->
## TOPIC 00038: RFmxTDSCDMA CDA Fetch Mean Symbol Phase Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-mean-symbol-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-mean-symbol-phase-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the averaged symbol phase error trace for the code domain analysis (CDA) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is

### RFmxTDSCDMA CDA Fetch Mean Symbol Phase Error Trace VI

Fetches the averaged symbol phase error trace for the code domain analysis (CDA) measurement.

[IMAGE alt='icon' src='rfmxtdscdma-cda-fetch-mean-symbol-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Symbol Phase Error (deg) — Mean Symbol Phase Error returns an array of the averaged symbol phase error traces for the configured measurement channel. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-symbol-constellation-trace-vi.html language=enus -->
## TOPIC 00039: RFmxTDSCDMA CDA Fetch Symbol Constellation Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-symbol-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-symbol-constellation-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is

### RFmxTDSCDMA CDA Fetch Symbol Constellation Trace VI

Fetches the symbol constellation trace of the code domain analysis (CDA) measurement channel.

[IMAGE alt='icon' src='rfmxtdscdma-cda-fetch-symbol-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Constellation — Symbol Constellation returns an array of the symbol constellation traces of the configured measurement channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-symbol-evm-vi.html language=enus -->
## TOPIC 00040: RFmxTDSCDMA CDA Fetch Symbol EVM VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-symbol-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-cda-fetch-symbol-evm-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc related measurements for the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxTDSCDMA CDA Fetch Symbol EVM VI

Fetches the ModAcc related measurements for the configured measurement channel.

[IMAGE alt='icon' src='rfmxtdscdma-cda-fetch-symbol-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean RMS Symbol Magnitude Error (%) — Mean RMS Symbol Magnitude Error returns the RMS symbol magnitude error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. Chip Rate Error (ppm) — Chip Rate Error returns the chip rate error. This value is expressed in ppm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean RMS Symbol EVM (%) — Mean RMS Symbol EVM returns the RMS symbol EVM for the selected time slot and channel, averaged over all averaging iterations. This value is expressed as a percentage. Maximum Peak Symbol EVM (%) — Maximum Peak Symbol EVM returns the maximum value of the peak symbol EVMs, among all averaging iterations for the selected time slot and channel. This value is expressed as a percentage. Frequency Error (Hz) — Frequency Error returns the frequency error averaged over all measured slots. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. Mean RMS Symbol Phase Error (deg) — Mean RMS Symbol Phase Error returns the RMS symbol phase error for the selected time slot and channel, averaged over all averaging iterations. This value is expressed in degrees. Mean Symbol Power (dBm) — Mean Symbol Power returns the mean symbol power for the selected time slot and channel. This value is expressed in dB if you set the CDA Pwr Unit property to dB, and in dBm if you set the CDA Pwr Unit property to dBm. |
| --- |

Parent topic:

RFmxTDSCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-chp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00041: RFmxTDSCDMA CHP Fetch Spectrum VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-chp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-chp-fetch-spectrum-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxTDSCDMA CHP Fetch Spectrum VI

Fetches the spectrum used for the CHP measurement.

[IMAGE alt='icon' src='rfmxtdscdma-chp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |

Parent topic:

RFmxTDSCDMA CHP Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-external-attenuation-vi.html language=enus -->
## TOPIC 00042: RFmxTDSCDMA Configure External Attenuation VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-external-attenuation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-external-attenuation-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you

### RFmxTDSCDMA Configure External Attenuation VI

Specifies external attenuation to be considered by RFmx TD-SCDMA measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.

[IMAGE alt='icon' src='rfmxtdscdma-configure-external-attenuation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. External Attenuation (dB) — External Attenuation specifies the level of external attenuation that is considered by the selected measurement. This value is expressed in dB. The default value is 0. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-midamble-shift-vi.html language=enus -->
## TOPIC 00043: RFmxTDSCDMA Configure Midamble Shift VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-midamble-shift-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-midamble-shift-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Midamble Auto Detection Mode, Maximum Number of Users, and Midamble Shift parameters. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The

### RFmxTDSCDMA Configure Midamble Shift VI

Configures the **Midamble Auto Detection Mode**, **Maximum Number of Users**, and **Midamble Shift** parameters.

[IMAGE alt='icon' src='rfmxtdscdma-configure-midamble-shift-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Midamble Auto Detection Mode — Midamble Auto Detection Mode enables automatic midamble detection. The default value is Midamble Shift. Off (0) Automatic midamble detection is disabled. Midamble Shift (1) The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the Maximum Number of Users parameter. The K possible midamble shift values are: Midamble Shift = k * floor(P/K), where P = 128, is the length of the basic midamble code, and k is an integer from 0 to K-1. Maximum Number of Users — Maximum Number of Users configures the maximum number of users. The default value is 16. 2 (2) The maximum number of users are 2. 4 (4) The maximum number of users are 4. 6 (6) The maximum number of users are 6. 8 (8) The maximum number of users are 8. 10 (10) The maximum number of users are 10. 12 (12) The maximum number of users are 12. 14 (14) The maximum number of users are 14. 16 (16) The maximum number of users are 16. Midamble Shift (chips) — Midamble Shift specifies the midamble shift used when the Midamble Auto Detection Mode parameter is set to Off. This value is expressed in chips. The default value is 8. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| Off (0) | Automatic midamble detection is disabled. |
| Midamble Shift (1) | The midamble shift is automatically detected from K possible midamble shift values, where K is specified by the Maximum Number of Users parameter. The K possible midamble shift values are: Midamble Shift = k * floor(P/K), where P = 128, is the length of the basic midamble code, and k is an integer from 0 to K-1. |
| 2 (2) | The maximum number of users are 2. |
| 4 (4) | The maximum number of users are 4. |
| 6 (6) | The maximum number of users are 6. |
| 8 (8) | The maximum number of users are 8. |
| 10 (10) | The maximum number of users are 10. |
| 12 (12) | The maximum number of users are 12. |
| 14 (14) | The maximum number of users are 14. |
| 16 (16) | The maximum number of users are 16. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-reference-level-vi.html language=enus -->
## TOPIC 00044: RFmxTDSCDMA Configure Reference Level VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-reference-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-configure-reference-level-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxTDSCDMA Configure Reference Level VI

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

[IMAGE alt='icon' src='rfmxtdscdma-configure-reference-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Level — Reference Level specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-averaging-vi.html language=enus -->
## TOPIC 00045: RFmxTDSCDMA ModAcc Configure Averaging VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-averaging-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ModAcc measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "s

### RFmxTDSCDMA ModAcc Configure Averaging VI

Configures averaging for the ModAcc measurement.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the ModAcc measurement. The default value is False. False (0) Disables averaging for the ModAcc measurement. True (1) The ModAcc measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables averaging for the ModAcc measurement. |
| True (1) | The ModAcc measurement uses the Averaging Count parameter as the number of acquisitions over which the ModAcc measurement is averaged. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-slot-type-vi.html language=enus -->
## TOPIC 00046: RFmxTDSCDMA ModAcc Configure Slot Type VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-slot-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-slot-type-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the type of the Time Slot for ModAcc analysis. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxTDSCDMA ModAcc Configure Slot Type VI

Configures the type of the Time Slot for ModAcc analysis.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-configure-slot-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Slot Type — Slot Type specifies the type of the Time Slot for ModAcc analysis. The default value is Traffic. Traffic (0) The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. Pilot (1) The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| Traffic (0) | The measurement is performed on the traffic time slot. The composite, data, and midamble ModAcc results are obtained when you select this slot type. |
| Pilot (1) | The measurement is performed on the pilot time slot. The pilot ModAcc results are obtained when you select this slot type. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00047: RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The

### RFmxTDSCDMA ModAcc Configure Synchronization Mode and Interval VI

Configures the synchronization mode, measurement offset, and measurement length for ModAcc analysis.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies the synchronization mode for the ModAcc measurement. The default value is Slot. Slot (0) The measurement uses the slot synchronization mode. The first slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the slot from which the Measurement Offset parameter should be considered. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. Subframe (1) The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset from the boundary specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot slot. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The default value is 0. Measurement Length (slots) — Measurement Length specifies the duration of the ModAcc measurement. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| Slot (0) | The measurement uses the slot synchronization mode. The first slot boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the slot from which the Measurement Offset parameter should be considered. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, for this trigger type, the traffic time slot(s) in the received signal should be contiguous with the pilot time slot, if the pilot time slot is present. |
| Subframe (1) | The measurement uses the subframe synchronization mode. The first subframe boundary in the acquired signal is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter, starting at the offset from the boundary specified by the Measurement Offset parameter. If you set the Trigger Type property to Digital Edge, you should provide the trigger at the start of the subframe. If you set the Trigger Type property to IQ Power Edge, it is required that the received signal has either one traffic time slot or contiguous traffic time slots. Additionally, the traffic time slot should be contiguous with the active pilot slot. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-rcde-vi.html language=enus -->
## TOPIC 00048: RFmxTDSCDMA ModAcc Fetch Data RCDE VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-rcde-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-rcde-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the measured data relative code domain error (RCDE), along with the spreading factor and the channelization code of the corresponding channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and resul

### RFmxTDSCDMA ModAcc Fetch Data RCDE VI

Returns the maximum value of the measured data relative code domain error (RCDE), along with the spreading factor and the channelization code of the corresponding channel.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-data-rcde-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Peak Data RCDE (dB) — Maximum Peak Data RCDE returns the maximum value of the peak RDCEs among all active time slots and averaging iterations. This value is expressed in dB. RFmx calculates the RCDEs by projecting the descrambled error vector onto the codes of each active channel. The RCDE is the ratio of the mean power of the projection onto that code to the mean power of the corresponding active channel in the reference waveform. Peak Data RCDE Spreading Factor — Peak Data RCDE Spreading Factor returns the spreading factor of the channel corresponding to the value of the ModAcc Results Pk Data RCDE property. Peak Data RCDE Code — Peak Data RCDE Code returns the channelization code of the channel corresponding to the value of the ModAcc Results Pk Data RCDE Code property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-array-vi.html language=enus -->
## TOPIC 00049: RFmxTDSCDMA ModAcc Fetch Detected Channel (Array) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-array-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected channels. If you set the Channel Configuration Mode property to User Defined, the measurement returns the configured channels. If the averaging is enabled, this VI returns the array of detected channels of the last averaging iteration. icon Inputs/Outputs cstr.png Selector Strin

### RFmxTDSCDMA ModAcc Fetch Detected Channel (Array) VI

Returns the detected channels. If you set the [Channel Configuration Mode](/csh?context=rfmxtdscdma_rfmxtdscdmaprop_attr700010) property to **User Defined**, the measurement returns the configured channels. If the averaging is enabled, this VI returns the array of detected channels of the last averaging iteration.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-detected-channel-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Detected Channelization Code — Detected Channelization Code returns an array of channelization code numbers for the detected channels. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Detected Slot Index — Detected Slot Index returns an array of slot indexes of the detected channels. Detected Spreading Factor — Detected Spreading Factor returns an array of spreading factors of the detected channels. Detected Modulation Type — Detected Modulation Type returns an array of the modulation types for the detected channels. QPSK (0) The modulation type is QPSK. 8PSK (1) The modulation type is 8-PSK. 16QAM (2) The modulation type is 16-QAM. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| QPSK (0) | The modulation type is QPSK. |
| 8PSK (1) | The modulation type is 8-PSK. |
| 16QAM (2) | The modulation type is 16-QAM. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-vi.html language=enus -->
## TOPIC 00050: RFmxTDSCDMA ModAcc Fetch Detected Channel VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a detected channel by its channel name. Use "channel<n>" as the selector string to read results from this VI. If the averaging is enabled, the detected channels of the last averaging operation can be retrieved. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector

### RFmxTDSCDMA ModAcc Fetch Detected Channel VI

Returns a detected channel by its channel name.

Use "channel*<n>*" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read results from this VI.

If the averaging is enabled, the detected channels of the last averaging operation can be retrieved.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-detected-channel-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and channel number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "channel0" "signal::sig1/channel0" "result::r1/channel0" "signal::sig1/result::r1/channel0" You can use the RFmxTDSCDMA Build Channel String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Detected Channelization Code — Detected Channelization Code returns the channelization code of the detected channel. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Detected Slot Index — Detected Slot Index returns the slot index of the detected channel. Detected Spreading Factor — Detected Spreading Factor returns the spreading factor of the detected channel. Detected Modulation Type — Detected Modulation Type returns the modulation type for the detected channel. QPSK (0) The modulation type is QPSK. 8PSK (1) The modulation type is 8-PSK. 16QAM (2) The modulation type is16-QAM. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| QPSK (0) | The modulation type is QPSK. |
| 8PSK (1) | The modulation type is 8-PSK. |
| 16QAM (2) | The modulation type is16-QAM. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-evm-trace-vi.html language=enus -->
## TOPIC 00051: RFmxTDSCDMA ModAcc Fetch EVM Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-evm-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average of the EVM traces on the chip level. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxTDSCDMA ModAcc Fetch EVM Trace VI

Fetches the average of the EVM traces on the chip level.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. EVM (%) — EVM returns the average of the EVM traces on the chip level. x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns the EVM trace values as a real value array. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns the EVM trace values as a real value array. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00052: RFmxTDSCDMA ModAcc Fetch IQ Impairments VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-iq-impairments-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do n

### RFmxTDSCDMA ModAcc Fetch IQ Impairments VI

Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I/Q Origin Offset (dB) — I/Q Origin Offset returns the I/Q origin offset of the composite signal, averaged over all measured slots. This value is expressed in dB. I/Q Gain Imbalance (dB) — I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal, averaged over all measured slots. This value is expressed in dB. I/Q Quadrature Error (deg) — I/Q Quadrature Error returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00053: RFmxTDSCDMA ModAcc Fetch Magnitude Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-magnitude-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average of the magnitude error trace on the chip level. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specif

### RFmxTDSCDMA ModAcc Fetch Magnitude Error Trace VI

Fetches the average of the magnitude error trace on the chip level.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Magnitude Error (%) — Magnitude Error returns the data for a complex waveform including the start, delta, and actual values. x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns the magnitude trace error values as a real value array. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns the magnitude trace error values as a real value array. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-code-domain-error-trace-vi.html language=enus -->
## TOPIC 00054: RFmxTDSCDMA ModAcc Fetch Maximum Code Domain Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-code-domain-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-code-domain-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum code domain error trace among all active time slots and averaging iterations for the ModAcc measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name,

### RFmxTDSCDMA ModAcc Fetch Maximum Code Domain Error Trace VI

Fetches the maximum code domain error trace among all active time slots and averaging iterations for the ModAcc measurement.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-maximum-code-domain-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Code Domain Error (dB) — Maximum Code Domain Error returns an array of the maximum code domain error traces among all active time slots and averaging iterations. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-evm-trace-vi.html language=enus -->
## TOPIC 00055: RFmxTDSCDMA ModAcc Fetch Maximum EVM Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-evm-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum EVM trace values on the chip level. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result

### RFmxTDSCDMA ModAcc Fetch Maximum EVM Trace VI

Fetches the maximum EVM trace values on the chip level.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-maximum-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum EVM (%) — Maximum EVM returns the maximum EVM trace values on the chip level. x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns an array of the maximum EVM trace values on the chip level. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns an array of the maximum EVM trace values on the chip level. This value is expressed as a percentage. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00056: RFmxTDSCDMA ModAcc Fetch Maximum Magnitude Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-magnitude-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum magnitude error trace on the chip level. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the r

### RFmxTDSCDMA ModAcc Fetch Maximum Magnitude Error Trace VI

Fetches the maximum magnitude error trace on the chip level.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-maximum-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Magnitude Error (%) — Maximum Magnitude Error returns the maximum magnitude error trace on the chip level. x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns an array of maximum magnitude error trace on the chip level. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns an array of maximum magnitude error trace on the chip level. This value is expressed as a percentage. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-phase-error-trace-vi.html language=enus -->
## TOPIC 00057: RFmxTDSCDMA ModAcc Fetch Maximum Phase Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-phase-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase error trace on the chip level. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxTDSCDMA ModAcc Fetch Maximum Phase Error Trace VI

Fetches the maximum phase error trace on the chip level.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-maximum-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. — Maximum Phase Error returns the maximum phase error trace on the chip level. x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns an array of the maximum phase error traces on the chip level. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns an array of the maximum phase error traces on the chip level. This value is expressed in degrees. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-and-data-power-vi.html language=enus -->
## TOPIC 00058: RFmxTDSCDMA ModAcc Fetch Midamble and Data Power VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-and-data-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-and-data-power-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power of the midamble and the data channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result

### RFmxTDSCDMA ModAcc Fetch Midamble and Data Power VI

Returns the power of the midamble and the data channel.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-midamble-and-data-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Midamble Power (dBm) — Midamble Power returns the power of the midamble, averaged over all measured slots. This value is expressed in dBm. Data Field 1 Power (dBm) — Data Field 1 Power returns the power of the data field 1, averaged over all measured slots. This value is expressed in dBm. Data Field 2 Power (dBm) — Data Field 2 Power returns the power of the data field 2, averaged over all measured slots. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-evm-vi.html language=enus -->
## TOPIC 00059: RFmxTDSCDMA ModAcc Fetch Midamble EVM VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-evm-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the midamble EVM measurement results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the

### RFmxTDSCDMA ModAcc Fetch Midamble EVM VI

Returns the midamble EVM measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-midamble-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RMS Midamble Phase Error (deg) — RMS Midamble Phase Error returns the RMS of the midamble phase error, averaged over all active time slots and all averaging iterations. This value is expressed in degrees. RMS Midamble Magnitude Error (%) — RMS Midamble Magnitude Error returns the RMS of the midamble magnitude error, averaged over all active time slots and averaging iterations. This value is expressed as a percentage. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS Midamble EVM (%) — RMS Midamble EVM returns the RMS of the midamble EVM, averaged over all active time slots and all averaging iterations. This value is expressed as a percentage. Peak Midamble EVM (%) — Peak Midamble EVM returns the peak midamble EVM among all active time slots and averaging iterations. This value is expressed as a percentage. Midamble Rho — Midamble Rho returns the rho value of the midamble, averaged over all measured active time slots and averaging iterations. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-number-of-detected-channels-vi.html language=enus -->
## TOPIC 00060: RFmxTDSCDMA ModAcc Fetch Number of Detected Channels VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-number-of-detected-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-number-of-detected-channels-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of detected channels. If the averaging is enabled, it returns the number of detected channels of the last averaging iteration. If you set the Channel Configuration Mode property to User Defined, the measurement returns the number of configured channels. icon Inputs/Outputs cstr.pn

### RFmxTDSCDMA ModAcc Fetch Number of Detected Channels VI

Returns the number of detected channels. If the averaging is enabled, it returns the number of detected channels of the last averaging iteration. If you set the [Channel Configuration Mode](/csh?context=rfmxtdscdma_rfmxtdscdmaprop_attr700010) property to **User Defined**, the measurement returns the number of configured channels.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-number-of-detected-channels-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Number of Detected Channels — Number of Detected Channels returns the total number of the detected channels. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-phase-error-trace-vi.html language=enus -->
## TOPIC 00061: RFmxTDSCDMA ModAcc Fetch Phase Error Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-phase-error-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average of the phase error trace on the chip level. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify th

### RFmxTDSCDMA ModAcc Fetch Phase Error Trace VI

Returns the average of the phase error trace on the chip level.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Phase Error (deg) — Phase Error returns the data for a complex waveform including the start, delta, and actual values. x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns the phase error trace values as a real value array. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace. This value is expressed in seconds. dx — dx returns the sampling time of the trace. This value is expressed in seconds. y — y returns the phase error trace values as a real value array. This value is expressed in degrees. |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-pilot-evm-vi.html language=enus -->
## TOPIC 00062: RFmxTDSCDMA ModAcc Fetch Pilot EVM VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-pilot-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-pilot-evm-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM measurement of the pilot time slot. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result nam

### RFmxTDSCDMA ModAcc Fetch Pilot EVM VI

Fetches the EVM measurement of the pilot time slot.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-pilot-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. RMS Pilot Phase Error (deg) — RMS Pilot Phase Error returns the RMS of the pilot phase error, averaged over all averaging iterations. This value is expressed in degrees. RMS Pilot Magnitude Error (%) — RMS Pilot Magnitude Error returns the RMS of the pilot magnitude error, averaged over all the averaging iterations. This value is expressed as a percentage. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS Pilot EVM (%) — RMS Pilot EVM returns the RMS of the pilot EVM, averaged over all averaging iterations. This value is expressed as a percentage. Peak Pilot EVM (%) — Peak Pilot EVM returns the maximum of the peak pilot EVM among the averaging iterations. This value is expressed as a percentage. Pilot Rho — Pilot Rho returns the pilot Rho value, averaged over all averaging iterations. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-vi.html language=enus -->
## TOPIC 00063: RFmxTDSCDMA ModAcc Fetch VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc measurement results. icon

### RFmxTDSCDMA ModAcc Fetch VI

Fetches the ModAcc measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-modacc-fetch-vi.png']

- [RFmxTDSCDMA ModAcc Fetch Data EVM VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-evm-vi.html) Returns the EVM measurement of the data channel.
- [RFmxTDSCDMA ModAcc Fetch Midamble EVM VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-evm-vi.html) Returns the midamble EVM measurement results.
- [RFmxTDSCDMA ModAcc Fetch Data Active CDE VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-active-cde-vi.html) Returns the peak value among the code domain errors (CDEs) of the active channels, as well as the code number, spreading factor, and branch that correspond to this peak value.
- [RFmxTDSCDMA ModAcc Fetch Data CDE VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-cde-vi.html) Returns the maximum value of the measured data code domain errors (CDEs), along with the spreading factor and the channelization code of the corresponding channel.
- [RFmxTDSCDMA ModAcc Fetch Data RCDE VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-data-rcde-vi.html) Returns the maximum value of the measured data relative code domain error (RCDE), along with the spreading factor and the channelization code of the corresponding channel.
- [RFmxTDSCDMA ModAcc Fetch Pilot EVM VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-pilot-evm-vi.html) Fetches the EVM measurement of the pilot time slot.
- [RFmxTDSCDMA ModAcc Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-iq-impairments-vi.html) Returns the I/Q origin offset, I/Q gain imbalance, and I/Q quadrature error.
- [RFmxTDSCDMA ModAcc Fetch Midamble and Data Power VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-midamble-and-data-power-vi.html) Returns the power of the midamble and the data channel.
- [RFmxTDSCDMA ModAcc Fetch Number of Detected Channels VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-number-of-detected-channels-vi.html) Returns the number of detected channels. If the averaging is enabled, it returns the number of detected channels of the last averaging iteration. If you set the Channel Configuration Mode property to User Defined , the measurement returns the number of configured channels.
- [RFmxTDSCDMA ModAcc Fetch Composite EVM VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-composite-evm-vi.html) Returns the composite EVM of all the channels in the ModAcc measurement.
- [RFmxTDSCDMA ModAcc Fetch Detected Channel VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-vi.html) Returns a detected channel by its channel name.
- [RFmxTDSCDMA ModAcc Fetch Detected Channel (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-detected-channel-array-vi.html) Returns the detected channels. If you set the Channel Configuration Mode property to User Defined , the measurement returns the configured channels. If the averaging is enabled, this VI returns the array of detected channels of the last averaging iteration.
- [RFmxTDSCDMA ModAcc Fetch EVM Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-evm-trace-vi.html) Fetches the average of the EVM traces on the chip level.
- [RFmxTDSCDMA ModAcc Fetch Maximum EVM Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-evm-trace-vi.html) Fetches the maximum EVM trace values on the chip level.
- [RFmxTDSCDMA ModAcc Fetch Magnitude Error Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-magnitude-error-trace-vi.html) Fetches the average of the magnitude error trace on the chip level.
- [RFmxTDSCDMA ModAcc Fetch Maximum Magnitude Error Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-magnitude-error-trace-vi.html) Fetches the maximum magnitude error trace on the chip level.
- [RFmxTDSCDMA ModAcc Fetch Phase Error Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-phase-error-trace-vi.html) Returns the average of the phase error trace on the chip level.
- [RFmxTDSCDMA ModAcc Fetch Maximum Phase Error Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-phase-error-trace-vi.html) Fetches the maximum phase error trace on the chip level.
- [RFmxTDSCDMA ModAcc Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-constellation-trace-vi.html) Fetches the constellation trace of the received TD-SCDMA signal. If the averaging is enabled, this trace refers to the last averaging iteration..
- [RFmxTDSCDMA ModAcc Fetch Code Domain Error Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-code-domain-error-trace-vi.html) Fetches the value of the code domain error trace for the individual code channels in the domain of the base spreading factor. This value is averaged over all active time slots and averaging iterations.
- [RFmxTDSCDMA ModAcc Fetch Maximum Code Domain Error Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-modacc-fetch-maximum-code-domain-error-trace-vi.html) Fetches the maximum code domain error trace among all active time slots and averaging iterations for the ModAcc measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-averaging-vi.html language=enus -->
## TOPIC 00064: RFmxTDSCDMA OBW Configure Averaging VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-averaging-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "sign

### RFmxTDSCDMA OBW Configure Averaging VI

Configures averaging for the OBW measurement.

[IMAGE alt='icon' src='rfmxtdscdma-obw-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled enables averaging for spectrum measurements. The default value is False. False (0) Disables averaging for the OBW measurement. True (1) The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables averaging for the OBW measurement. |
| True (1) | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00065: RFmxTDSCDMA OBW Configure RBW Filter VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-rbw-filter-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxTDSCDMA OBW Configure RBW Filter VI

Configures the RBW filter.

[IMAGE alt='icon' src='rfmxtdscdma-obw-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW you specify. True (1) RFmx TD-SCDMA automatically determines the RBW. Refer to the RBW and Sweep Time section in the Spectrum topic for more information about RBW and sweep time. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 5.636 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is FFT Based. FFT Based (0) An RBW filter with a fast Fourier transform (FFT)-based response is applied. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW you specify. |
| True (1) | RFmx TD-SCDMA automatically determines the RBW. |
| FFT Based (0) | An RBW filter with a fast Fourier transform (FFT)-based response is applied. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-sweep-time-vi.html language=enus -->
## TOPIC 00066: RFmxTDSCDMA OBW Configure Sweep Time VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-configure-sweep-time-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxTDSCDMA OBW Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxtdscdma-obw-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of .00066 seconds (s). Refer to the RBW and Sweep Time section in the OBW topic for more details on RBW and sweep time. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-measurement-vi.html language=enus -->
## TOPIC 00067: RFmxTDSCDMA OBW Fetch Measurement VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-measurement-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result i

### RFmxTDSCDMA OBW Fetch Measurement VI

Returns the OBW measurement.

[IMAGE alt='icon' src='rfmxtdscdma-obw-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Stop Frequency (Hz) — Stop Frequency returns the stop frequency of the OBW. This value is expressed in Hz. Start Frequency (Hz) — Start Frequency returns the start frequency of the OBW. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Occupied Bandwidth (Hz) — Occupied Bandwidth returns the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency. Absolute Power (dBm) — Absolute Power returns the total integrated power of the averaged spectrum acquired by the OBW measurement. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA OBW Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-spectrum-vi.html language=enus -->
## TOPIC 00068: RFmxTDSCDMA OBW Fetch Spectrum VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-spectrum-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum trace used for the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxTDSCDMA OBW Fetch Spectrum VI

Fetches the spectrum trace used for the OBW measurement.

[IMAGE alt='icon' src='rfmxtdscdma-obw-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |

Parent topic:

RFmxTDSCDMA OBW Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-vi.html language=enus -->
## TOPIC 00069: RFmxTDSCDMA OBW Fetch VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the OBW measurement results. icon

### RFmxTDSCDMA OBW Fetch VI

Fetches the OBW measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-obw-fetch-vi.png']

- [RFmxTDSCDMA OBW Fetch Measurement VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-measurement-vi.html) Returns the OBW measurement.
- [RFmxTDSCDMA OBW Fetch Spectrum VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-obw-fetch-spectrum-vi.html) Fetches the spectrum trace used for the OBW measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-property-node-vi.html language=enus -->
## TOPIC 00070: RFmxTDSCDMA Property Node VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-property-node-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) RFmxTDSCDMA properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png er

### RFmxTDSCDMA Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) RFmxTDSCDMA properties.

[IMAGE alt='icon' src='rfmxtdscdma-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx TDSCDMA Property Node is used to get (read), set (write), or reset (set to default value) RFmx TDSCDMA properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

TDSCDMA

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-configure-averaging-vi.html language=enus -->
## TOPIC 00071: RFmxTDSCDMA PVT Configure Averaging VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-configure-averaging-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the power versus time (PVT) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string)

### RFmxTDSCDMA PVT Configure Averaging VI

Configures averaging for the power versus time (PVT) measurement.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the PVT measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The PVT measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the PVT measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the PVT measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged on a logarithmic scale. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The PVT measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the PVT measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged on a logarithmic scale. |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-configure-measurement-method-vi.html language=enus -->
## TOPIC 00072: RFmxTDSCDMA PVT Configure Measurement Method VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-configure-measurement-method-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-configure-measurement-method-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement method for the power versus time (PVT) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (

### RFmxTDSCDMA PVT Configure Measurement Method VI

Configures the measurement method for the power versus time (PVT) measurement.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-configure-measurement-method-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Method — Measurement Method specifies the method used for performing the PVT measurement. The default value is Normal. Normal (0) The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. Dynamic Range (1) The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842/5860. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| Normal (0) | The PVT measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when a higher measurement speed is preferred over a higher dynamic range. |
| Dynamic Range (1) | The PVT measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5644R/5645R/5646R/5840/5841/5842/5860. |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00073: RFmxTDSCDMA PVT Fetch Measurement Status VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-measurement-status-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall status of the power versus time (PVT) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not spe

### RFmxTDSCDMA PVT Fetch Measurement Status VI

Fetches the overall status of the power versus time (PVT) measurement.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the overall status of the PVT measurement. Fail (0) Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. Pass (1) Indicates that the test has passed and the measured power in all defined segments does not violate the limits. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |

Parent topic:

RFmxTDSCDMA PVT Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-powers-vi.html language=enus -->
## TOPIC 00074: RFmxTDSCDMA PVT Fetch Powers VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-powers-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the values of the Mean Absolute ON Power and Mean Absolute OFF Power parameters. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxTDSCDMA PVT Fetch Powers VI

Fetches the values of the **Mean Absolute ON Power** and **Mean Absolute OFF Power** parameters.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-fetch-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Absolute ON Power (dBm) — Mean Absolute ON Power returns the mean on power of the measured burst, or the averaged bursts. This value is expressed in dBm. Mean Absolute OFF Power (dBm) — Mean Absolute OFF Power returns the mean off power of the measured burst, or the averaged bursts. This value is expressed in dBm. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA PVT Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-array-vi.html language=enus -->
## TOPIC 00075: RFmxTDSCDMA PVT Fetch Segment Measurement (Array) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-array-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the status and measured powers for all the power versus time (PVT) measurement segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance

### RFmxTDSCDMA PVT Fetch Segment Measurement (Array) VI

Fetches the status and measured powers for all the power versus time (PVT) measurement segments.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-fetch-segment-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Segment Mean Absolute Power (dBm) — Segment Mean Absolute Power returns an array of the mean measured powers corresponding to the Segment Margin parameter. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Segment Status — Segment Status returns an array of the measurement status values for an individual PVT measurement segment. Fail (0) Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. Pass (1) Indicates that the test has passed and the measured power in all defined segments does not violate the limits. Segment Margin (dB) — Segment Margin returns an array of the power margins for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. Segment Margin Time (s) — Segment Margin Time returns an array of the positions in time corresponding to the Segment Margin parameter. This value is expressed in seconds. error out — error out returns error information. This output provides standard error out functionality. Segment Maximum Absolute Power (dBm) — Segment Maximum Absolute Power returns an array of the maximum measured powers of an individual PVT measurement segment. This value is expressed in dBm. Segment Minimum Absolute Power (dBm) — Segment Minimum Absolute Power returns an array of the minimum measured powers of an individual PVT measurement segment. This value is expressed in dBm. |  |
| --- | --- |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |

Parent topic:

RFmxTDSCDMA PVT Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-vi.html language=enus -->
## TOPIC 00076: RFmxTDSCDMA PVT Fetch Segment Measurement VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers. Use "segment<n>" as the selector string to read this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result

### RFmxTDSCDMA PVT Fetch Segment Measurement VI

Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers.

Use "segment<*n*>" as the [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this VI.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-fetch-segment-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and segment number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "segment0" "signal::sig1/segment0" "result::r1/segment0" "signal::sig1/result::r1/segment0" You can use the RFmxTDSCDMA Build Segment String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Segment Mean Absolute Power (dBm) — Segment Mean Absolute Power returns the mean measured power corresponding to the Segment Margin parameter. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Segment Status — Segment Status returns the measurement status for an individual PVT measurement segment. Fail (0) Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. Pass (1) Indicates that the test has passed and the measured power in all defined segments does not violate the limits. Segment Margin (dB) — Segment Margin returns the power margin for an individual PVT measurement segment, which is the minimum power distance to the power limit measured within the PVT measurement segment. This value is expressed in dB. Segment Margin Time (s) — Segment Margin Time returns the position in time corresponding to the Segment Margin parameter. This value is expressed in seconds. error out — error out returns error information. This output provides standard error out functionality. Segment Maximum Absolute Power (dBm) — Segment Maximum Absolute Power returns the maximum measured power of an individual PVT measurement segment. This value is expressed in dBm. Segment Minimum Absolute Power (dBm) — Segment Minimum Absolute Power returns the minimum measured power of an individual PVT measurement segment. This value is expressed in dBm. |  |
| --- | --- |
| Fail (0) | Indicates that the test has failed, and the measured power in at least one measurement segment violates the limit. |
| Pass (1) | Indicates that the test has passed and the measured power in all defined segments does not violate the limits. |

Parent topic:

RFmxTDSCDMA PVT Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-signal-power-trace-vi.html language=enus -->
## TOPIC 00077: RFmxTDSCDMA PVT Fetch Signal Power Trace VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-signal-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-signal-power-trace-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result

### RFmxTDSCDMA PVT Fetch Signal Power Trace VI

Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-fetch-signal-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Signal Power (dBm) — Signal Power returns the measured signal power over a specified period of time. x0 — x0 returns the start time of the trace relative to the start of the analyzed burst. dx — dx returns the time difference between successive trace samples. y — y returns an array of values for the signal power trace. These values are expressed in dBm. Absolute Limit (dBm) — Absolute Limit returns the power limit as defined by the transmit ON/OFF time mask in the 3GPP TS 34.122 specification. x0 — x0 returns the start time of the limit trace relative to the burst start. dx — dx returns the time difference between successive trace samples. y — y returns an array of values for the absolute power limit trace. These values are expressed in dBm. error out — error out returns error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time of the trace relative to the start of the analyzed burst. dx — dx returns the time difference between successive trace samples. y — y returns an array of values for the signal power trace. These values are expressed in dBm. |
| x0 — x0 returns the start time of the limit trace relative to the burst start. dx — dx returns the time difference between successive trace samples. y — y returns an array of values for the absolute power limit trace. These values are expressed in dBm. |

Parent topic:

RFmxTDSCDMA PVT Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-vi.html language=enus -->
## TOPIC 00078: RFmxTDSCDMA PVT Fetch VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power versus time (PVT) measurement results. icon

### RFmxTDSCDMA PVT Fetch VI

Fetches the power versus time (PVT) measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-pvt-fetch-vi.png']

- [RFmxTDSCDMA PVT Fetch Measurement Status VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-measurement-status-vi.html) Fetches the overall status of the power versus time (PVT) measurement.
- [RFmxTDSCDMA PVT Fetch Powers VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-powers-vi.html) Fetches the values of the Mean Absolute ON Power and Mean Absolute OFF Power parameters.
- [RFmxTDSCDMA PVT Fetch Segment Measurement VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-vi.html) Returns the status of a specific power versus time (PVT) measurement segment along with the measured segment powers.
- [RFmxTDSCDMA PVT Fetch Segment Measurement (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-segment-measurement-array-vi.html) Fetches the status and measured powers for all the power versus time (PVT) measurement segments.
- [RFmxTDSCDMA PVT Fetch Signal Power Trace VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-pvt-fetch-signal-power-trace-vi.html) Fetches the signal power trace and the absolute limit trace. The limit trace is defined by the transmit ON/off time mask measurement in the 3GPP TS 34.122 specification.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-reset-to-default-vi.html language=enus -->
## TOPIC 00079: RFmxTDSCDMA Reset to Default VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-reset-to-default-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig

### RFmxTDSCDMA Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxtdscdma-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00080: RFmxTDSCDMA Select Measurement (Multiple) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-multiple-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxTDSCDMA Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxtdscdma-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurements — Measurements specifies the measurement to perform. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. CDA (5) Enables the code domain analysis (CDA) measurement. PVT (6) Enables the power versus time (PVT) measurement. SlotPower (7) Enables the SlotPower measurement. The default is an empty array. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| CDA (5) | Enables the code domain analysis (CDA) measurement. |
| PVT (6) | Enables the power versus time (PVT) measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |

Parent topic:

RFmxTDSCDMA Select Measurement VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-single-vi.html language=enus -->
## TOPIC 00081: RFmxTDSCDMA Select Measurement (Single) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-single-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the measurement that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxTDSCDMA Select Measurement (Single) VI

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxtdscdma-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement — Measurement specifies the measurement to perform. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. CDA (5) Enables the code domain analysis (CDA) measurement. PVT (6) Enables the power versus time (PVT) measurement. SlotPower (7) Enables the SlotPower measurement. The default value is ModAcc. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| CDA (5) | Enables the code domain analysis (CDA) measurement. |
| PVT (6) | Enables the power versus time (PVT) measurement. |
| SlotPower (7) | Enables the SlotPower measurement. |

Parent topic:

RFmxTDSCDMA Select Measurement VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-vi.html language=enus -->
## TOPIC 00082: RFmxTDSCDMA Select Measurement VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select multiple measurements, use the Multiple Measurements instance. To select a single measurement, use the Single Measurement instance. icon

### RFmxTDSCDMA Select Measurement VI

Specifies the measurements that you want to enable. To select multiple measurements, use the **Multiple Measurements** instance. To select a single measurement, use the **Single Measurement** instance.

[IMAGE alt='icon' src='rfmxtdscdma-select-measurement-vi.png']

- [RFmxTDSCDMA Select Measurement (Single) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxTDSCDMA Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

TDSCDMA

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-configure-averaging-vi.html language=enus -->
## TOPIC 00083: RFmxTDSCDMA SEM Configure Averaging VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-configure-averaging-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "sign

### RFmxTDSCDMA SEM Configure Averaging VI

Configures averaging for the SEM measurement.

[IMAGE alt='icon' src='rfmxtdscdma-sem-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled enables averaging for spectrum measurements. The default value is False. False (0) Disables averaging for the SEM measurement. True (1) The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables averaging for the SEM measurement. |
| True (1) | The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-configure-sweep-time-vi.html language=enus -->
## TOPIC 00084: RFmxTDSCDMA SEM Configure Sweep Time VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-configure-sweep-time-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxTDSCDMA SEM Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxtdscdma-sem-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of .00066 seconds (s). Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00066 s. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of .00066 seconds (s). |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-carrier-absolute-integrated-power-vi.html language=enus -->
## TOPIC 00085: RFmxTDSCDMA SEM Fetch Carrier Absolute Integrated Power VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-carrier-absolute-integrated-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-carrier-absolute-integrated-power-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier integrated power of the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not spec

### RFmxTDSCDMA SEM Fetch Carrier Absolute Integrated Power VI

Returns the absolute carrier integrated power of the SEM measurement.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-carrier-absolute-integrated-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Carrier Absolute Integrated Power (dBm) — Carrier Absolute Integrated Power returns the carrier power. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-array-vi.html language=enus -->
## TOPIC 00086: RFmxTDSCDMA SEM Fetch Lower Offset Margin (Array) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-array-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default

### RFmxTDSCDMA SEM Fetch Lower Offset Margin (Array) VI

Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-lower-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the array of powers at which the margin occurs in each negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the array of powers at which the margin occurs in the negative offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the array of lower offset measurement statuses based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. Margin (dB) — Margin returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. The margin is defined as the minimum distance between the spectrum and the limit mask. Margin Frequency (Hz) — Margin Frequency returns the array of frequencies at which the margin occurs in each negative offset segment. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-vi.html language=enus -->
## TOPIC 00087: RFmxTDSCDMA SEM Fetch Lower Offset Margin VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name

### RFmxTDSCDMA SEM Fetch Lower Offset Margin VI

Returns the measurement status and margin from the limit line measured in the lower offset segment.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-lower-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power at which the margin occurs in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power at which the margin occurs in the negative offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the lower offset measurement status based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. Margin (dB) — Margin returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. Margin Frequency (Hz) — Margin Frequency returns the frequency at which the margin occurs in the negative offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-array-vi.html language=enus -->
## TOPIC 00088: RFmxTDSCDMA SEM Fetch Lower Offset Power (Array) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-array-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the

### RFmxTDSCDMA SEM Fetch Lower Offset Power (Array) VI

Returns the arrays of lower offset segment power measurements.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-lower-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the array of peak powers in the lower (negative) offset segment relative to the integrated power of the reference carrier. Peak Frequency (Hz) — Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the array of lower (negative) offset segment powers measured. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the array of powers in each negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns the array of peak powers measured in each lower (negative) offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-vi.html language=enus -->
## TOPIC 00089: RFmxTDSCDMA SEM Fetch Lower Offset Power VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the

### RFmxTDSCDMA SEM Fetch Lower Offset Power VI

Returns the lower offset segment power measurements.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-lower-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the peak power in the lower (negative) offset segment relative to the integrated power of the reference carrier. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the lower (negative) offset segment power measured. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the power in the negative offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00090: RFmxTDSCDMA SEM Fetch Measurement Status VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-measurement-status-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM measurement status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default r

### RFmxTDSCDMA SEM Fetch Measurement Status VI

Returns the SEM measurement status.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the status of the measurement based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-spectrum-vi.html language=enus -->
## TOPIC 00091: RFmxTDSCDMA SEM Fetch Spectrum VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-spectrum-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxTDSCDMA SEM Fetch Spectrum VI

Fetches the spectrum used for the SEM measurement.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. Relative Mask (dB) — Relative Mask returns the trace of power levels representing the relative mask in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. Absolute Mask (dBm) — Absolute Mask returns the data for a real waveform including the start, delta, and actual values. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm. |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-array-vi.html language=enus -->
## TOPIC 00092: RFmxTDSCDMA SEM Fetch Upper Offset Margin (Array) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-array-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal insta

### RFmxTDSCDMA SEM Fetch Upper Offset Margin (Array) VI

Returns the measurement status and margin from the limit line measured in the upper offset segments.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-upper-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the array of powers at which the margin occurs in each positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the array of powers at which the margin occurs in each positive offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. Margin (dB) — Margin returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. The margin is defined as the minimum distance between the spectrum and the limit mask. Margin Frequency (Hz) — Margin Frequency returns the array of frequencies at which the margin occurs in each positive offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-vi.html language=enus -->
## TOPIC 00093: RFmxTDSCDMA SEM Fetch Upper Offset Margin VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segment. Use "offset<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name

### RFmxTDSCDMA SEM Fetch Upper Offset Margin VI

Returns the measurement status and margin from the limit line measured in the upper offset segment.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-upper-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power at which the margin occurs in the positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power at which the margin occurs in the positive offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the upper offset measurement status based on measurement limits and the failure criteria specified by the standard. Fail (0) The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. Pass (1) The signal does not exceed the spectrum emission limits. Margin (dB) — Margin returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum distance between the spectrum and the limit mask. Margin Frequency (Hz) — Margin Frequency returns the frequency at which the margin occurs in the positive offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The signal exceeds the limits given by 3GPP TS 251.02 v11.6.0 standard, table 6.5A ff. |
| Pass (1) | The signal does not exceed the spectrum emission limits. |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-array-vi.html language=enus -->
## TOPIC 00094: RFmxTDSCDMA SEM Fetch Upper Offset Power (Array) VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-array-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of upper offset segment power measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the

### RFmxTDSCDMA SEM Fetch Upper Offset Power (Array) VI

Returns the arrays of upper offset segment power measurements.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-upper-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the array of peak powers measured in each upper (positive) offset segment relative to the integrated power of the reference carrier. Peak Frequency (Hz) — Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the array of upper (positive) offset segment powers measured. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the array of powers measured in each positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns the array of peak powers measured in each upper (positive) offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-vi.html language=enus -->
## TOPIC 00095: RFmxTDSCDMA SEM Fetch Upper Offset Power VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the upper offset segment power measurements. Use "offset<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the

### RFmxTDSCDMA SEM Fetch Upper Offset Power VI

Returns the upper offset segment power measurements.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-upper-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxTDSCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the peak power in the upper (positive) offset segment relative to the integrated power of the reference carrier. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the upper (positive) offset segment power measured. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the power in the positive offset segment relative to the integrated power of the reference carrier. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-vi.html language=enus -->
## TOPIC 00096: RFmxTDSCDMA SEM Fetch VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SEM measurement results. icon

### RFmxTDSCDMA SEM Fetch VI

Fetches the SEM measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-sem-fetch-vi.png']

- [RFmxTDSCDMA SEM Fetch Measurement Status VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-measurement-status-vi.html) Returns the SEM measurement status.
- [RFmxTDSCDMA SEM Fetch Carrier Absolute Integrated Power VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-carrier-absolute-integrated-power-vi.html) Returns the absolute carrier integrated power of the SEM measurement.
- [RFmxTDSCDMA SEM Fetch Lower Offset Power VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-vi.html) Returns the lower offset segment power measurements.
- [RFmxTDSCDMA SEM Fetch Lower Offset Power (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-power-array-vi.html) Returns the arrays of lower offset segment power measurements.
- [RFmxTDSCDMA SEM Fetch Upper Offset Power VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-vi.html) Returns the upper offset segment power measurements.
- [RFmxTDSCDMA SEM Fetch Upper Offset Power (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-power-array-vi.html) Returns the arrays of upper offset segment power measurements.
- [RFmxTDSCDMA SEM Fetch Lower Offset Margin VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-vi.html) Returns the measurement status and margin from the limit line measured in the lower offset segment.
- [RFmxTDSCDMA SEM Fetch Lower Offset Margin (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-lower-offset-margin-array-vi.html) Returns the array of measurement statuses and margins from the limit line measured in the lower offset segments.
- [RFmxTDSCDMA SEM Fetch Upper Offset Margin VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-vi.html) Returns the measurement status and margin from the limit line measured in the upper offset segment.
- [RFmxTDSCDMA SEM Fetch Upper Offset Margin (Array) VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-upper-offset-margin-array-vi.html) Returns the measurement status and margin from the limit line measured in the upper offset segments.
- [RFmxTDSCDMA SEM Fetch Spectrum VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-sem-fetch-spectrum-vi.html) Fetches the spectrum used for the SEM measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00097: RFmxTDSCDMA Send Software Edge Trigger VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-send-software-edge-trigger-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxTDSCDMA Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure

### RFmxTDSCDMA Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxTDSCDMA Configure Trigger](/csh?topicname=rfmxtdscdma-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxTDSCDMA Initiate VI.

[IMAGE alt='icon' src='rfmxtdscdma-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-configure-measurement-length-vi.html language=enus -->
## TOPIC 00098: RFmxTDSCDMA SlotPower Configure Measurement Length VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-configure-measurement-length-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-configure-measurement-length-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement length for the SlotPower measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).

### RFmxTDSCDMA SlotPower Configure Measurement Length VI

Configures the measurement length for the SlotPower measurement.

[IMAGE alt='icon' src='rfmxtdscdma-slotpower-configure-measurement-length-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Length (slots) — Measurement Length specifies the measurement length for the SlotPower measurement. This value is expressed in slots. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal. NI recommends you set a measurement length as a multiple of the number of slots per subframe, that is a multiple of 7. For example, when you set this property to 28 slots, the SlotPower measurement would report results for the 4 active time slots within the specified measurement length. In this example, 28 slots = 4 subframes. The start of the measurement is determined by the Trigger Type property. Although all the values of the Trigger Type property are supported for this measurement, it is recommended to set the Trigger Type property to Digital Edge with the following options: Digital trigger at the start of active slot, with the Trigger Delay property set to 0 seconds Digital trigger at the start of the subframe, with the Trigger Delay property configured to a value which is equal to the time offset of the active time slot from the start of the subframe The table shows the values of the Trigger Delay property, when you specify the following active slots values: Active Slot Trigger Delay (microseconds) TS0 0 TS1 950 TS2 1625 TS3 2300 TS4 2975 TS5 3650 TS6 4325 If you cannot provide a digital trigger, you can set Trigger Type property to IQ Power Edge to ensure that the measurement starts at the start of an active time slot. To ensure this trigger works properly, NI recommends you complete the following steps: Set the IQ Power Edge Level property to allow triggering for any of the power levels in the active slots Run the RFmx measurement just before generating your signal If you set the Trigger type property to None, the measurement will automatically detect the start of the first burst and measure the traffic slot in that position in every subframe. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 28. The minimum value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |  |
| --- | --- |
| Active Slot | Trigger Delay (microseconds) |
| TS0 | 0 |
| TS1 | 950 |
| TS2 | 1625 |
| TS3 | 2300 |
| TS4 | 2975 |
| TS5 | 3650 |
| TS6 | 4325 |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-powers-vi.html language=enus -->
## TOPIC 00099: RFmxTDSCDMA SlotPower Fetch Powers VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-powers-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Slot Power and Slot Power Delta values. The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received s

### RFmxTDSCDMA SlotPower Fetch Powers VI

Fetches the **Slot Power** and **Slot Power Delta** values.

The SlotPower measurement assumes that there is only one active traffic time slot per subframe, and that the position of this active time slot is the same in each subframe. Additionally, it assumes that there are no pilots present in the received signal.

[IMAGE alt='icon' src='rfmxtdscdma-slotpower-fetch-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Slot Power (dBm) — Slot Power returns an array of mean powers of the active traffic time slots being measured. This value is expressed in dBm. The power of each traffic slot is measured by first excluding the gap period of 12.5 microseconds at the end of the time slot, and then excluding the transient duration of 25 microseconds at the start and the end of the remaining portion of the slot. Slot Power Delta (dB) — Slot Power Delta returns an array of the power differences between active traffic slots in adjacent subframes. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxTDSCDMA SlotPower Fetch VI

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-vi.html language=enus -->
## TOPIC 00100: RFmxTDSCDMA SlotPower Fetch VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SlotPower measurement results. icon

### RFmxTDSCDMA SlotPower Fetch VI

Fetches the SlotPower measurement results.

[IMAGE alt='icon' src='rfmxtdscdma-slotpower-fetch-vi.png']

- [RFmxTDSCDMA SlotPower Fetch Powers VI](../../../../../vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-slotpower-fetch-powers-vi.html) Fetches the Slot Power and Slot Power Delta values.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxtdscdma-labview-api-ref path=vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00101: RFmxTDSCDMA Wait for Measurement Complete VI

- bundle_id: `rfmxtdscdma-labview-api-ref`
- source_path: `vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxtdscdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/tdscdma/mx/rfmxtdscdma-llb/rfmxtdscdma-wait-for-measurement-complete-vi.html
- document_id: `rfmxtdscdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number of seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxTDSCDMA Wait for Measurement Complete VI

Waits for the specified number of seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxtdscdma-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxTDSCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out returns error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility
