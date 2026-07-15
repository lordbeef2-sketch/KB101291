# NI DOCUMENT BUNDLE: rfmx-vna-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-vna-prop start=1 end=64 -->
<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00000.html language=enus -->
## TOPIC 00001: Selector String Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00000.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

**Short Name:**Selector String

Property of [RFmxVNA](crfmxvna.html)

Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node.

If the property you want to use is channel-based, you must first set the [Selector String](../rfmxvnaprop/attrd00000.html) property and then set the channel-based property in the same property node. If a property is not channel-based, and you set the Selector String property in this instance of the property node, RFmxVNA returns an error.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00002.html language=enus -->
## TOPIC 00002: Sweep:Frequency List (Hz) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00002.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Frequency List (Hz) Property

**Short Name:**Freq List (Hz)

Property of [RFmxVNA](crfmxvna.html)

Specifies the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz.

The default value is an empty array.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00003.html language=enus -->
## TOPIC 00003: Sweep:Power Level (dBm) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00003.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Power Level (dBm) Property

**Short Name:**Power Level (dBm)

Property of [RFmxVNA](crfmxvna.html)

Specifies the source power level for the VNA port. This value is expressed in dBm.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure same power level for all VNA ports.

The default value is -10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00004.html language=enus -->
## TOPIC 00004: Sweep:IF Bandwidth (Hz) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00004.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:IF Bandwidth (Hz) Property

**Short Name:**IF Bandwidth (Hz)

Property of [RFmxVNA](crfmxvna.html)

Specifies the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth.

The default value is 100kHz.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00005.html language=enus -->
## TOPIC 00005: Sweep:Timing:Sweep Delay (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00005.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Timing:Sweep Delay (s) Property

**Short Name:**Sweep Delay (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the sweep delay. This value is expressed in seconds.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00006.html language=enus -->
## TOPIC 00006: Sweep:Timing:Dwell Time (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00006.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Timing:Dwell Time (s) Property

**Short Name:**Dwell Time (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the time for which the analyzer waits before acquiring the signal for each measured frequency point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00007.html language=enus -->
## TOPIC 00007: Averaging:Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00007.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Averaging:Enabled Property

**Short Name:**Averaging Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable averaging for the VNA measurement.

The default value is **False**.

| False (0) | The measurement is performed on a single acquisition. |
| --- | --- |
| True (1) | The measurement uses the Averaging Count property as the number of acquisitions over which the measurement is averaged. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00008.html language=enus -->
## TOPIC 00008: Averaging:Count Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00008.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Averaging:Count Property

**Short Name:**Averaging Count

Property of [RFmxVNA](crfmxvna.html)

Specifies the number of acquisitions used for averaging when you set the [Averaging Enabled](../rfmxvnaprop/attrd00007.html) property to **True**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0000a.html language=enus -->
## TOPIC 00009: Sweep:Test Receiver Attenuation (dB) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0000a.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Test Receiver Attenuation (dB) Property

**Short Name:**Test Receiver Attn (dB)

Property of [RFmxVNA](crfmxvna.html)

Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure same test receiver attenuation for all VNA ports.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0000b.html language=enus -->
## TOPIC 00010: Correction:Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0000b.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Enabled Property

**Short Name:**Correction Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable error correction for VNA measurement.

The default value is **False**.

| False (0) | The measurement disables error corection. |
| --- | --- |
| True (1) | The measurement enables error correction. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0000e.html language=enus -->
## TOPIC 00011: Correction:Port Subset:Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0000e.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Port Subset:Enabled Property

**Short Name:**Correction Port Subset Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable correction for a subset of set of ports for which calibration data is avaialble.

Enable port subset when calibration or loaded calset contains error correction terms for more ports than the number of ports in device under test (DUT), and achieve faster measurement speed by avoiding extra acquisitions.

The default value is **False**.

| False (0) | The measurement disables port-subsetting for error correction. |
| --- | --- |
| True (1) | The measurement enabes port-subsetting for error correction. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0000f.html language=enus -->
## TOPIC 00012: Correction:Port Subset:Ports Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0000f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0000f.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Port Subset:Ports Property

**Short Name:**Correction Port Subset Ports

Property of [RFmxVNA](crfmxvna.html)

Specifies the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to **True**.

The default value is an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00010.html language=enus -->
## TOPIC 00013: Correction:Calibration:Ports Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00010.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Ports Property

**Short Name:**Cal Ports

Property of [RFmxVNA](crfmxvna.html)

Specifies the ports requested for calibration. Use comma-separated list of ports to specify multiple ports.

The default value is an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00011.html language=enus -->
## TOPIC 00014: Correction:Calibration:Connector Type Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00011.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00011.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Connector Type Property

**Short Name:**Connector Type

Property of [RFmxVNA](crfmxvna.html)

Specifies the connector type of the DUT. The specified connector type must match be same as that of the selected calkit.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure same connector type for VNA ports.

The default value is an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00012.html language=enus -->
## TOPIC 00015: Correction:Calibration:Calkit:Type Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00012.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00012.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Calkit:Type Property

**Short Name:**Calkit Type

Property of [RFmxVNA](crfmxvna.html)

Specifies the type of calkit used for calibration.

The default value is **Electronic**.

| Electronic (0) | Use electronic calkit module for calibration. Supported device: NI-5501. |
| --- | --- |
| Mechanical (1) | Use mechanical calkit standards for calibration. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00013.html language=enus -->
## TOPIC 00016: Correction:Calibration:Calkit:Electronic:Resource Name Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00013.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00013.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Calkit:Electronic:Resource Name Property

**Short Name:**vCal Resource Name

Property of [RFmxVNA](crfmxvna.html)

Specifies the resource name of the electronic calibration module (vCal) used for calibration.

Use "port::all" as the selector string to specify the same resource name for all VNA ports. Use "port::<*portname*>" as the selector string to read this property for a specific VNA port.

**Supported devices**: NI-5501

The default value is an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00014.html language=enus -->
## TOPIC 00017: Correction:Calibration:Calkit:Mechanical:Name Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00014.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00014.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Calkit:Mechanical:Name Property

**Short Name:**Calkit Name

Property of [RFmxVNA](crfmxvna.html)

Specifies the name of the mechanical calkit used for measurement calibration when you set [Calkit Type](../rfmxvnaprop/attrd00012.html) property to **Mechanical**.

The default value is an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00015.html language=enus -->
## TOPIC 00018: Correction:Calibration:Method Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00015.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00015.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Method Property

**Short Name:**Cal Method

Property of [RFmxVNA](crfmxvna.html)

Specifies the calibration method.

The default value is **SOL**.

| SOL (0) | Full 1-port calibration using atleast three distinct reflection standards, typically named Short, Open and Load. |
| --- | --- |
| SOLT (1) | Full 2-port calibration by performing two SOL calibrations on the two ports using atleast three distinct reflection standards, and a Thru cal using a transmission standard connecting the two ports. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00017.html language=enus -->
## TOPIC 00019: Correction:Calibration:Thru:Method Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00017.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00017.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Thru:Method Property

**Short Name:**Thru Method

Property of [RFmxVNA](crfmxvna.html)

Specifies the Thru calibration method when [Calibration Method](../rfmxvnaprop/attrd00015.html) property is set to **SOLT**.

The default value is **Auto**.

| Auto (0) | Measurement selects the appropriate Thru calibration method based on the value of Calkit Type property specified by you. If Calkit Type is Electronic, then Delay Thru Using Defined Thru is selected. If Calkit Type is Mechanical, then Undefined Thru is selected. |
| --- | --- |
| Defined Thru (1) | The Thru definition from calkit definition is used based on the value of Calkit Type property specified by you. If Calkit Type is Electronic, the Thru definition from the electronic calkit EPROM is used. If Calkit Type is Mechanical, the Thru definition from the calkit definition file is used. |
| Flush Thru (2) | Indicates a direct connection of the test ports when Calkit Type is Mechanical. The measured Thru is treated as flush Thru ignoring the Thru definition from the Calkit file. This method is not supported when Calkit Type is Electronic. |
| Undefined Thru (3) | Indicates connection of a Thru without a stored definition when Calkit Type is Mechanical. The measured Thru is treated as unknown Thru ignoring the Thru definition from the Calkit file. If a delay is configured, the delay will be utilized for the calibration. This method is not supported when Calkit Type is Electronic. |
| Undefined Thru Using Defined Thru (4) | The Thru from the electronical Calkit is used for Thru measurement but treated as unknown Thru in the calibration, that is, the definition of the Thru is being ignored. This method is not supported when Calkit Type is Mechanical. |
| Delay Thru Using Defined Thru (5) | The Thru from the electronical Calkit is used for Thru measurement. For the calibration only the inherent delay information from the Thru defnintion is used. This method is not supported when Calkit Type is Mechanical. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00018.html language=enus -->
## TOPIC 00020: Correction:Calibration:Thru:Coax:Delay (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00018.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00018.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Thru:Coax:Delay (s) Property

**Short Name:**Thru Coax Delay (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the delay of the Thru mechanical standard when [Calkit Type](../rfmxvnaprop/attrd00012.html) property is set to **Mechanical** and Thru Method property is set to **Auto** or **Undefined Thru**. This value is expressed in seconds.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00019.html language=enus -->
## TOPIC 00021: Correction:Calibration:Step:Count Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00019.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00019.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Step:Count Property

**Short Name:**Cal Step Count

Property of [RFmxVNA](crfmxvna.html)

Returns the number of steps required to perform calibration.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0001a.html language=enus -->
## TOPIC 00022: Correction:Calibration:Step:Description Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0001a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0001a.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Step:Description Property

**Short Name:**Cal Step Description

Property of [RFmxVNA](crfmxvna.html)

Returns the description the calibration step.

Use "calstep<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0001e.html language=enus -->
## TOPIC 00023: Correction:Calibration:Calkit:Electronic:Orientation Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0001e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0001e.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Calkit:Electronic:Orientation Property

**Short Name:**vCal Orientation

Property of [RFmxVNA](crfmxvna.html)

Specifies the orientation of the vCal fixture ports with respect to vCal ports.

Use "portA:portname, portB:portname" format to specify vCal orientation.

When using NI-PXIe 5633 without an NI switch module, if vCal orientation is not specified, it is assumed to be "portA:port1, portB:port2".

When using NI-PXIe 5633 with an NI switch module, vCal orientation must be specified for all the [Calibration Ports](../rfmxvnaprop/attrd00010.html) set by you.

The default value is an empty string.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00026.html language=enus -->
## TOPIC 00024: Correction:Port Extension:Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00026.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00026.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Port Extension:Enabled Property

**Short Name:**Port Extension Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable port extension for the VNA port.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure for all VNA ports.

The default value is **False**.

| False (0) | The measurement disables port extension for the VNA port. |
| --- | --- |
| True (1) | The measurement enables port extension for the VNA port. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00027.html language=enus -->
## TOPIC 00025: Correction:Port Extension:Delay (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00027.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00027.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Port Extension:Delay (s) Property

**Short Name:**Port Extension Delay (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure the same delay value for all VNA ports.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00028.html language=enus -->
## TOPIC 00026: Correction:Port Extension:Loss:DC Loss Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00028.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00028.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Port Extension:Loss:DC Loss Enabled Property

**Short Name:**Port Extension DC Loss Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to compensate for the frequency independent loss when Port Extension Enabled is set to **True**.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure for all VNA ports.

The default value is **False**.

| False (0) | The measurement disables the compensation of DC Loss of the port extension. |
| --- | --- |
| True (1) | The measurement compensates for the DC loss based on the value of Port Extension DC Loss (dB) specified by you. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00029.html language=enus -->
## TOPIC 00027: Correction:Port Extension:Loss:DC Loss (dB) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00029.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00029.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Port Extension:Loss:DC Loss (dB) Property

**Short Name:**Port Extension DC Loss (dB)

Property of [RFmxVNA](crfmxvna.html)

Specifies the frequency independent loss to compensate when Port Extension Enabled is set to **True** and Port Extension DC Loss Enabled is set to **True**. This value is expressed in dB.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure same value of DC loss for all VNA ports.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00031.html language=enus -->
## TOPIC 00028: Sweep:Pulse:Mode Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00031.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00031.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Mode Enabled Property

**Short Name:**Pulse Mode Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable pulse mode for VNA measurement.

The default value is **False**.

| False (0) | The measurement disables pulse mode. |
| --- | --- |
| True (1) | The measurement enables pulse mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00035.html language=enus -->
## TOPIC 00029: Sweep:Pulse:Period (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00035.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00035.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Period (s) Property

**Short Name:**Pulse Period (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the interval after which the pulse repeats when you set the [Pulse Mode Enabled](../rfmxvnaprop/attrd00031.html) property to **True**. This value is expressed in seconds.

The default value is 0.001s.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00037.html language=enus -->
## TOPIC 00030: Sweep:Pulse:Modulator:Delay (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00037.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00037.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Modulator:Delay (s) Property

**Short Name:**Pulse Modulator Delay (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the [Pulse Mode Enabled](../rfmxvnaprop/attrd00031.html) property to **True**. This value is expressed in seconds.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00038.html language=enus -->
## TOPIC 00031: Sweep:Pulse:Modulator:Width (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00038.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00038.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Modulator:Width (s) Property

**Short Name:**Pulse Modulator Width (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the duration for which the pulse is in ON state when you set the [Pulse Mode Enabled](../rfmxvnaprop/attrd00031.html) property to **True**. This value is expressed in seconds.

The default value is 0.0001s.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00039.html language=enus -->
## TOPIC 00032: Sweep:Pulse:Acquisition:Auto Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00039.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00039.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Acquisition:Auto Property

**Short Name:**Pulse Acquisition Auto

Property of [RFmxVNA](crfmxvna.html)

Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the [Pulse Mode Enabled](../rfmxvnaprop/attrd00031.html) property to **True**.

The default value is **True**.

| False (0) |  |
| --- | --- |
| True (1) | The measurement uses the Pulse Modulator Width property to compute pulse acquisition delay and pulse acquisition width. Approximately 20% of the pulse modulator width is set as the pulse acquisition delay and approximately 75% of Pulse Modulator Width is set as the pulse acquisition width. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0003a.html language=enus -->
## TOPIC 00033: Sweep:Pulse:Acquisition:Delay (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0003a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0003a.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Acquisition:Delay (s) Property

**Short Name:**Pulse Acquisition Delay (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the [Pulse Mode Enabled](../rfmxvnaprop/attrd00031.html) property to **True** and the [Pulse Acquisition Auto](../rfmxvnaprop/attrd00039.html) property to **True** . This value is expressed in seconds.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0003b.html language=enus -->
## TOPIC 00034: Sweep:Pulse:Acquisition:Width (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0003b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0003b.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Pulse:Acquisition:Width (s) Property

**Short Name:**Pulse Acquisition Width (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the width of pulse acquisition when you set the [Pulse Mode Enabled](../rfmxvnaprop/attrd00031.html) property to **True** and the [Pulse Acquisition Auto](../rfmxvnaprop/attrd00039.html) property to **True**. This value is expressed in seconds.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00042.html language=enus -->
## TOPIC 00035: Trigger:Type Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00042.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00042.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Type Property

**Short Name:**Trigger Type

Property of [RFmxVNA](crfmxvna.html)

Specifies the trigger type.

The default value is **None**.

| None (0) | No trigger is configured. |
| --- | --- |
| Digital Edge (1) | The trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| Software (2) | The trigger is not asserted until a software trigger occurs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00043.html language=enus -->
## TOPIC 00036: Trigger:Digital Edge:Source Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00043.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00043.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Source Property

**Short Name:**Digital Edge Source

Property of [RFmxVNA](crfmxvna.html)

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](../rfmxvnaprop/attrd00042.html) property to **Digital Edge**.

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

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00044.html language=enus -->
## TOPIC 00037: Trigger:Digital Edge:Edge Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00044.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00044.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Digital Edge:Edge Property

**Short Name:**Digital Edge

Property of [RFmxVNA](crfmxvna.html)

Specifies the active edge for the trigger. This property is used only when you set the [Trigger Type](../rfmxvnaprop/attrd00042.html) property to **Digital Edge**.

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

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00045.html language=enus -->
## TOPIC 00038: Trigger:Mode Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00045.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00045.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Mode Property

**Short Name:**Trigger Mode

Property of [RFmxVNA](crfmxvna.html)

Specifies the trigger mode.

The default value is **Signal**.

| Signal (0) | A single trigger completes all the acquisitions associated with the signal. |
| --- | --- |
| Sweep (1) | Each trigger performs all the acquisitions from one source port. For example, when measuring S11 and S22 for 10 frequency points, a total of 2 triggers will be needed to complete all the acquisitions. |
| Point (2) | Each trigger measures one frequency point from one source port. For example, when measuring S11 and S22 for 10 frequency points, a total of 20 triggers will be needed to complete all the acquisitions. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00046.html language=enus -->
## TOPIC 00039: Sweep:Auto IF Bandwidth Scaling Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00046.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00046.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Sweep:Auto IF Bandwidth Scaling Enabled Property

**Short Name:**Auto IF Bandwidth Scaling Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether IF Bandwidth is scaled down at low frequencies.

The default value is **True**.

| False (0) | Disables IFBW scaling at low frequencies. The IF Bandwidth specified by you using IF Bandwidth property is used for all the frequencies. |
| --- | --- |
| True (1) | Enables scaling of IF Bandwidth at low frequencies. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd00800.html language=enus -->
## TOPIC 00040: Correction:Calibration:Estimated Thru Delay (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd00800.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd00800.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Correction:Calibration:Estimated Thru Delay (s) Property

**Short Name:**Cal Est Thru Delay (s)

Property of [RFmxVNA](crfmxvna.html)

Returns the estimated Thru Delay when Thru Method is set to **Undefined Thru** or **Undefined Thru Using Defined Thru**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01000.html language=enus -->
## TOPIC 00041: SParams:Measurement Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01000.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Measurement Enabled Property

**Short Name:**SParams Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable the Sparams measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the selector string topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01002.html language=enus -->
## TOPIC 00042: SParams:Number of S-Parameters Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01002.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Number of S-Parameters Property

**Short Name:**SParams Num SParams

Property of [RFmxVNA](crfmxvna.html)

Specifies the number of S-Parameters to measure.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector String](../rfmxvnaprop/attrd00000.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01003.html language=enus -->
## TOPIC 00043: SParams:Receiver Port Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01003.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Receiver Port Property

**Short Name:**SParams Receiver Port

Property of [RFmxVNA](crfmxvna.html)

Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by "S_<*receiver port name*>_<*source port name*>".

For example, to measure S_port2_port1, set this property to "port2".

Use "sparam<*n*>" as the selector string to configure or read this property.

The default value is "port1".

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01004.html language=enus -->
## TOPIC 00044: SParams:Source Port Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01004.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Source Port Property

**Short Name:**SParams Source Port

Property of [RFmxVNA](crfmxvna.html)

Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_<*receiver port name*>_<*source port name*>".

For example, to measure S_port2_port1, set this property to "port1".

Use "sparam<*n*>" as the selector string to configure or read this property.

The default value is "port1".

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01005.html language=enus -->
## TOPIC 00045: SParams:Format Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01005.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Format Property

**Short Name:**SParams Format

Property of [RFmxVNA](crfmxvna.html)

Specifies the format of S-Parameter measurement.

Use "sparam<*n*>" as the selector string to configure or read this property.

The default value is **Magnitude**.

| Magnitude (0) | The magnitude of the S-Parameter is reported. Specify the magnitude unit by configuring SParams Magnitude Units property. |
| --- | --- |
| Phase (1) | The phase of the S-Parameter is reported in degrees. Specify the phase type by configuring Sparams Phase Trace Type property. |
| Complex (2) | The complex S-Parameter values are reported. Use RFmxVNA Fetch Complex Data method to fetch the result in this format. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01006.html language=enus -->
## TOPIC 00046: SParams:Magnitude Units Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01006.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Magnitude Units Property

**Short Name:**SParams Magnitude Units

Property of [RFmxVNA](crfmxvna.html)

Specifies the magnitude units for all S-Parameters for which [Sparams Format](../rfmxvnaprop/attrd01005.html) property is set to **Magnitude**.

The default value is **dB**.

| dB (0) | S-Parameter magnitude is reported in dB. |
| --- | --- |
| Linear (1) | S-Parameters magnitude is reported in linear scale. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01007.html language=enus -->
## TOPIC 00047: SParams:Phase Trace Type Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01007.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

SParams:Phase Trace Type Property

**Short Name:**SParams Phase Trace Type

Property of [RFmxVNA](crfmxvna.html)

Specifies the phase type for all S-Parameters for which [Sparams Format](../rfmxvnaprop/attrd01005.html) property is set to **Phase**.

The default value is **Wrapped**.

| Wrapped (0) | The reported S-Parameter phase is wrapped between -180 degress to +180 degrees. |
| --- | --- |
| Unwrapped (1) | The reported S-Parameter phase is unwrapped. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0100a.html language=enus -->
## TOPIC 00048: IQ:Measurement Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0100a.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

IQ:Measurement Enabled Property

**Short Name:**IQ Enabled

Property of [RFmxVNA](crfmxvna.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0100d.html language=enus -->
## TOPIC 00049: IQ:Acquisition Time (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0100d.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

IQ:Acquisition Time (s) Property

**Short Name:**IQ Acquisition Time (s)

Property of [RFmxVNA](crfmxvna.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0100f.html language=enus -->
## TOPIC 00050: IQ:Receiver Port Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0100f.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

IQ:Receiver Port Property

**Short Name:**IQ Receiver Port

Property of [RFmxVNA](crfmxvna.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd01010.html language=enus -->
## TOPIC 00051: IQ:Source Port Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd01010.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd01010.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

IQ:Source Port Property

**Short Name:**IQ Source Port

Property of [RFmxVNA](crfmxvna.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02000.html language=enus -->
## TOPIC 00052: Waves:Measurement Enabled Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02000.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Measurement Enabled Property

**Short Name:**Waves Enabled

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to enable the Waves measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector String](../rfmxvnaprop/attrd00000.html) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02002.html language=enus -->
## TOPIC 00053: Waves:Number of Waves Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02002.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02002.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Number of Waves Property

**Short Name:**Waves Num Waves

Property of [RFmxVNA](crfmxvna.html)

Specifies the number of waves to be measured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector String](../rfmxvnaprop/attrd00000.html) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02003.html language=enus -->
## TOPIC 00054: Waves:Receiver Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02003.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02003.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Receiver Property

**Short Name:**Waves Receiver

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port.

Incident and scattered waves are denoted by "a_<*receiver port name*>_<*source port name*>" and "b_<*receiver port name*>_<*source port name*>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.

For example, to measure 'b_port2_port1', set this property to **Test (0)**, [Waves Receiver Port](../rfmxvnaprop/attrd02004.html) to "port2" and [Waves Source Port](../rfmxvnaprop/attrd02005.html) to "port1".

Use "wave<*n*>" as the selector string to configure or read this property.

The default value is **Test**.

| Test (0) | Measures the wave on the test receiver. |
| --- | --- |
| Reference (1) | Measures the wave on the reference receiver. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02004.html language=enus -->
## TOPIC 00055: Waves:Receiver Port Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02004.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02004.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Receiver Port Property

**Short Name:**Waves Receiver Port

Property of [RFmxVNA](crfmxvna.html)

Specifies the receiver port name for wave measurement.

Incident and scattered waves are denoted by "a_<*receiver port name*>_<*source port name*>" and "b_<*receiver port name*>_<*source port name*>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.

For example, to measure 'b_port2_port1', set [Waves Receiver](../rfmxvnaprop/attrd02003.html) to **Test (0)**, set this property to "port2" and [Waves Source Port](../rfmxvnaprop/attrd02005.html) to "port1".

Use "wave<*n*>" as the selector string to configure or read this property.

The default value is "port1".

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02005.html language=enus -->
## TOPIC 00056: Waves:Source Port Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02005.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02005.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Source Port Property

**Short Name:**Waves Source Port

Property of [RFmxVNA](crfmxvna.html)

Specifies the source port name for wave measurement.

Incident and scattered waves are denoted by "a_<*receiver port name*>_<*source port name*>" and "b_<*receiver port name*>_<*source port name*>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.

For example, to measure 'b_port2_port1', set [Waves Receiver](../rfmxvnaprop/attrd02003.html) to **Test (0)**, [Waves Receiver Port](../rfmxvnaprop/attrd02004.html) to "port2" and set this property to "port1".

Use "wave<*n*>" as the selector string to configure or read this property.

The default value is "port1".

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02006.html language=enus -->
## TOPIC 00057: Waves:Format Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02006.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02006.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Format Property

**Short Name:**Waves Format

Property of [RFmxVNA](crfmxvna.html)

Specifies the format for wave measurement.

Use "wave<*n*>" as the selector string to configure or read this property.

Use RFmxVNA Waves Fetch Real Data to fetch the waves for which you configured this property to either **Magnitude (0)** or **Phase (1)**. Use RFmxVNA Waves Fetch Complex Data to fetch the waves for which you configured this property to **Complex (2)**.

The default value is **Magnitude**.

| Magnitude (0) | The magnitude of the wave is reported. Specify the magnitude unit by configuring Wave Magnitude Units property. |
| --- | --- |
| Phase (1) | The phase of the wave is reported in degrees. Specify the phase type by configuring Wave Phase Trace Type property. |
| Complex (2) | The complex wave values are reported. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02007.html language=enus -->
## TOPIC 00058: Waves:Magnitude Units Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02007.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02007.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Magnitude Units Property

**Short Name:**Waves Magnitude Units

Property of [RFmxVNA](crfmxvna.html)

Specifies the magnitude units for all waves for which [Waves Format](../rfmxvnaprop/attrd02006.html) property is set to **Magnitude**.

The default value is **dBm**.

| dBm (0) | Wave magnitude is reported in dBm. |
| --- | --- |
| dBmV (1) | Wave magnitude is reported in dBmV. |
| dBuV (2) | Wave magnitude is reported in dBuV. |
| dBmA (3) | Wave magnitude is reported in dBmA. |
| W (4) | Wave magnitude is reported in watts. |
| V (5) | Wave magnitude is reported in volts. |
| A (6) | Wave magnitude is reported in ampere. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd02008.html language=enus -->
## TOPIC 00059: Waves:Phase Trace Type Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd02008.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd02008.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Waves:Phase Trace Type Property

**Short Name:**Waves Phase Trace Type

Property of [RFmxVNA](crfmxvna.html)

Specifies the phase type for all waves for which [Sparams Format](../rfmxvnaprop/attrd01005.html) property is set to **Phase**.

The default value is **Wrapped**.

| Wrapped (0) | The reported wave phase is wrapped between -180 degress to +180 degrees. |
| --- | --- |
| Unwrapped (1) | The reported wave phase is unwrapped. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0200b.html language=enus -->
## TOPIC 00060: Advanced:Limited Configuration Change Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0200b.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Limited Configuration Change Property

**Short Name:**Limited Configuration Change

Property of [RFmxVNA](crfmxvna.html)

Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies and/or power levels repeatedly, enabling this property will help achieve faster measurements. When you set this property to a value other than Disabled, the RFmx driver will use an optimized code path and skip some checks.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than Disabled for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

Specify the named signal configuration you are setting this property in the [Selector String](../rfmxvnaprop/attrd00000.html) input. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Disabled**.

| Disabled (0) | This is the normal mode of RFmx operation. All configuration changes in RFmxInstr properties or in personality properties will be applied during RFmx Commit. |
| --- | --- |
| No Change (1) | Signal configuration and RFmxInstr configuration are locked after the first Commit or Initiate of the named signal configuration. Any configuration change thereafter either in RFmxInstr properties or personality properties will not be considered by subsequent RFmx Commits or Initiates of this signal. Use No Change if you have created named signal configurations for all measurement configurations but are setting some RFmxInstr properties. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0200c.html language=enus -->
## TOPIC 00061: Advanced:Source Power Mode Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0200c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0200c.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Source Power Mode Property

**Short Name:**Source Power Mode

Property of [RFmxVNA](crfmxvna.html)

Specifies whether to make VNA measurements with source turned off.

The default value is **Auto**.

| Auto (0) | The source is turned on when making the measurement. |
| --- | --- |
| Off (1) | The source is turned off for all the ports when making the measurements. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0200d.html language=enus -->
## TOPIC 00062: Advanced:Ground Terminated Ports Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0200d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0200d.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Ground Terminated Ports Property

**Short Name:**Grounded Ports

Property of [RFmxVNA](crfmxvna.html)

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/attrd0c000.html language=enus -->
## TOPIC 00063: Result Fetch Timeout (s) Property

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/attrd0c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/attrd0c000.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

Result Fetch Timeout (s) Property

**Short Name:**Result Fetch Timeout (s)

Property of [RFmxVNA](crfmxvna.html)

Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete.

The default value is 10.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-vna-prop path=rfmxvnaprop/crfmxvna.html language=enus -->
## TOPIC 00064: RFmxVNA Properties

- bundle_id: `rfmx-vna-prop`
- source_path: `rfmxvnaprop/crfmxvna.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-prop/raw/resource/enus/rfmxvnaprop/crfmxvna.html
- document_id: `rfmx-vna-prop`
- page_type: `leaf`
- content_type: ``

RFmxVNA Properties

Use the RFmxVNA properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node. Details |
| Trigger:Type | Specifies the trigger type. Details |
| Trigger:Digital Edge:Source | Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Digital Edge:Edge | Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge. Details |
| Trigger:Mode | Specifies the trigger mode. Details |
| Sweep:Frequency List (Hz) | Specifies the list of frequencies at which VNA calibration or measurement (OR just 'VNA measurement') is performed. The frequencies must be in increasing order and must not contain duplicates. This value is expressed in Hz. Details |
| Sweep:Power Level (dBm) | Specifies the source power level for the VNA port. This value is expressed in dBm. Details |
| Sweep:IF Bandwidth (Hz) | Specifies the digital IF filter bandwidth. List of supported IF Bandwidths are {1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M}. This value is expressed in Hz. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth. Details |
| Sweep:Auto IF Bandwidth Scaling Enabled | Specifies whether IF Bandwidth is scaled down at low frequencies. Details |
| Sweep:Timing:Sweep Delay (s) | Specifies the sweep delay. This value is expressed in seconds. Details |
| Sweep:Timing:Dwell Time (s) | Specifies the time for which the analyzer waits before acquiring the signal for each measured frequency point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds. Details |
| Sweep:Test Receiver Attenuation (dB) | Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. Lower attenuation For each VNA port, the receiver that measures waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB. Details |
| Sweep:Pulse:Mode Enabled | Specifies whether to enable pulse mode for VNA measurement. Details |
| Sweep:Pulse:Period (s) | Specifies the interval after which the pulse repeats when you set the Pulse Mode Enabled property to True. This value is expressed in seconds. Details |
| Sweep:Pulse:Modulator:Delay (s) | Specifies the delay in the start of the pulse ON state relative to the internal pulse trigger when you set the Pulse Mode Enabled property to True. This value is expressed in seconds. Details |
| Sweep:Pulse:Modulator:Width (s) | Specifies the duration for which the pulse is in ON state when you set the Pulse Mode Enabled property to True. This value is expressed in seconds. Details |
| Sweep:Pulse:Acquisition:Auto | Specifies whether the measurement computes the pulse acquisition delay and pulse acquisition width when you set the Pulse Mode Enabled property to True. Details |
| Sweep:Pulse:Acquisition:Delay (s) | Specifies the delay in the start of the pulse acquisition relative to the internal pulse trigger when you set the Pulse Mode Enabled property to True and the Pulse Acquisition Auto property to True . This value is expressed in seconds. Details |
| Sweep:Pulse:Acquisition:Width (s) | Specifies the width of pulse acquisition when you set the Pulse Mode Enabled property to True and the Pulse Acquisition Auto property to True. This value is expressed in seconds. Details |
| Averaging:Enabled | Specifies whether to enable averaging for the VNA measurement. Details |
| Averaging:Count | Specifies the number of acquisitions used for averaging when you set the Averaging Enabled property to True. Details |
| Correction:Enabled | Specifies whether to enable error correction for VNA measurement. Details |
| Correction:Port Subset:Enabled | Specifies whether to enable correction for a subset of set of ports for which calibration data is avaialble. Details |
| Correction:Port Subset:Ports | Specifies the subset of ports to be corrected as a comma-separated list of port names when Correction Port Subset Enabled is set to True. Details |
| Correction:Port Extension:Enabled | Specifies whether to enable port extension for the VNA port. Details |
| Correction:Port Extension:Delay (s) | Specifies the electrical delay of port extension when Port Extension Enabled is set to True. This value is expressed in seconds. Details |
| Correction:Port Extension:Loss:DC Loss Enabled | Specifies whether to compensate for the frequency independent loss when Port Extension Enabled is set to True. Details |
| Correction:Port Extension:Loss:DC Loss (dB) | Specifies the frequency independent loss to compensate when Port Extension Enabled is set to True and Port Extension DC Loss Enabled is set to True. This value is expressed in dB. Details |
| Correction:Calibration:Ports | Specifies the ports requested for calibration. Use comma-separated list of ports to specify multiple ports. Details |
| Correction:Calibration:Connector Type | Specifies the connector type of the DUT. The specified connector type must match be same as that of the selected calkit. Details |
| Correction:Calibration:Calkit:Type | Specifies the type of calkit used for calibration. Details |
| Correction:Calibration:Calkit:Electronic:Resource Name | Specifies the resource name of the electronic calibration module (vCal) used for calibration. Details |
| Correction:Calibration:Calkit:Electronic:Orientation | Specifies the orientation of the vCal fixture ports with respect to vCal ports. Details |
| Correction:Calibration:Calkit:Mechanical:Name | Specifies the name of the mechanical calkit used for measurement calibration when you set Calkit Type property to Mechanical. Details |
| Correction:Calibration:Method | Specifies the calibration method. Details |
| Correction:Calibration:Thru:Method | Specifies the Thru calibration method when Calibration Method property is set to SOLT. Details |
| Correction:Calibration:Thru:Coax:Delay (s) | Specifies the delay of the Thru mechanical standard when Calkit Type property is set to Mechanical and Thru Method property is set to Auto or Undefined Thru. This value is expressed in seconds. Details |
| Correction:Calibration:Step:Count | Returns the number of steps required to perform calibration. Details |
| Correction:Calibration:Step:Description | Returns the description the calibration step. Details |
| Correction:Calibration:Estimated Thru Delay (s) | Returns the estimated Thru Delay when Thru Method is set to Undefined Thru or Undefined Thru Using Defined Thru. Details |
| SParams:Measurement Enabled | Specifies whether to enable the Sparams measurement. Details |
| SParams:Number of S-Parameters | Specifies the number of S-Parameters to measure. Details |
| SParams:Receiver Port | Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by "S_<receiver port name>_<source port name>". For example, to measure S_port2_port1, set this property to "port2". Details |
| SParams:Source Port | Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_<receiver port name>_<source port name>". For example, to measure S_port2_port1, set this property to "port1". Details |
| SParams:Format | Specifies the format of S-Parameter measurement. Details |
| SParams:Magnitude Units | Specifies the magnitude units for all S-Parameters for which Sparams Format property is set to Magnitude. Details |
| SParams:Phase Trace Type | Specifies the phase type for all S-Parameters for which Sparams Format property is set to Phase. Details |
| Waves:Measurement Enabled | Specifies whether to enable the Waves measurement. Details |
| Waves:Number of Waves | Specifies the number of waves to be measured. Details |
| Waves:Receiver | Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port. Incident and scattered waves are denoted by "a_<receiver port name>_<source port name>" and "b_<receiver port name>_<source port name>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure 'b_port2_port1', set this property to Test (0), Waves Receiver Port to "port2" and Waves Source Port to "port1". Details |
| Waves:Receiver Port | Specifies the receiver port name for wave measurement. Incident and scattered waves are denoted by "a_<receiver port name>_<source port name>" and "b_<receiver port name>_<source port name>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure 'b_port2_port1', set Waves Receiver to Test (0), set this property to "port2" and Waves Source Port to "port1". Details |
| Waves:Source Port | Specifies the source port name for wave measurement. Incident and scattered waves are denoted by "a_<receiver port name>_<source port name>" and "b_<receiver port name>_<source port name>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively. For example, to measure 'b_port2_port1', set Waves Receiver to Test (0), Waves Receiver Port to "port2" and set this property to "port1". Details |
| Waves:Format | Specifies the format for wave measurement. Details |
| Waves:Magnitude Units | Specifies the magnitude units for all waves for which Waves Format property is set to Magnitude. Details |
| Waves:Phase Trace Type | Specifies the phase type for all waves for which Sparams Format property is set to Phase. Details |
| IQ:Measurement Enabled | Details |
| IQ:Acquisition Time (s) | Details |
| IQ:Receiver Port | Details |
| IQ:Source Port | Details |
| Advanced:Limited Configuration Change | Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state. Details |
| Advanced:Source Power Mode | Specifies whether to make VNA measurements with source turned off. Details |
| Advanced:Ground Terminated Ports | Details |
| Result Fetch Timeout (s) | Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete. Details |
