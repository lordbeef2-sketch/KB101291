# NI DOCUMENT BUNDLE: rfmxnr-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxnr-labview-api-ref start=1 end=190 -->
<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=menus/categories/measurement/rfmx/nr/dir-mnu.html language=enus -->
## TOPIC 00001: NR

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/nr/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/nr/dir-mnu.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to perform NR measurements. You can use the RFmxNR Property Node to configure additional properties. © 2018–2026 National Instruments Corporation. All rights reserved. icon

### NR

Use the VIs on this palette to perform NR measurements. You can use the [RFmxNR Property Node](/csh?context=rfmxnr_rfmxnrvi_rfmxnr_property_node) to configure additional properties.

© 2018–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [Configuration](../../../../../menus/categories/measurement/rfmx/nr/configuration/dir-mnu.html) Use the VIs on this palette to configure RFmxNR measurements. You can use the RFmxNR Property Node to configure additional properties.
- [RFmxNR Select Measurement VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-vi.html) Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.
- [RFmxNR Initiate VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-initiate-vi.html) Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxNR Wait for Measurement Complete VI or RFmxNR Check Measurement Status VI.
- [Fetch](../../../../../menus/categories/measurement/rfmx/nr/rfmx-nr-mx-fetch-mnu.html) Use the VIs on this palette to fetch measurement results and traces.
- [Utility](../../../../../menus/categories/measurement/rfmx/nr/utility/dir-mnu.html) Use the VIs on this palette to configure RFmx NR utilities.
- [RFmxNR Property Node VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-property-node-vi.html) Gets (reads), sets (writes), or resets (sets to default value) RFmxNR properties.
- [Advanced](../../../../../menus/categories/measurement/rfmx/nr/rfmx-nr-mx-advanced-mnu.html) Use the VIs on this palette to use advanced features.
- [Build String](../../../../../menus/categories/measurement/rfmx/nr/utility/rfmx-nr-mx-utility-build-string-mnu.html) Use the VIs on this palette to create strings for configurations and results that require a selector string.

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=menus/categories/measurement/rfmx/nr/utility/dir-mnu.html language=enus -->
## TOPIC 00002: Utility

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/nr/utility/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/nr/utility/dir-mnu.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure RFmx NR utilities. icon

### Utility

Use the VIs on this palette to configure RFmx NR utilities.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxNR Commit VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-commit-vi.html) Commits settings to the hardware. Calling this VI is optional. RFmxNR commits settings to the hardware when you call the RFmxNR Initiate VI.
- [RFmxNR Reset to Default VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-reset-to-default-vi.html) Resets a signal to the default values.
- [RFmxNR Wait for Measurement Complete VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-wait-for-measurement-complete-vi.html) Waits for the specified number for seconds for all the measurements to complete.
- [RFmxNR Check Measurement Status VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-check-measurement-status-vi.html) Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.
- [RFmxNR Load from Generation Configuration File VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-load-from-generation-configuration-file-vi.html) Loads the attributes saved in an RFWS/TDMS file onto the RFmx session. This file can be saved using the NR Modulation Scheme in RFmx Waveform Creator. Make sure to select the 'store configuration' option while saving the TDMS file.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=menus/categories/measurement/rfmx/nr/utility/rfmx-nr-mx-utility-build-string-mnu.html language=enus -->
## TOPIC 00003: Build String

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/nr/utility/rfmx-nr-mx-utility-build-string-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/nr/utility/rfmx-nr-mx-utility-build-string-mnu.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to create strings for configurations and results that require a selector string. icon

### Build String

Use the VIs on this palette to create strings for configurations and results that require a selector string.

[IMAGE alt='icon' src='rfmx-nr-mx-utility-build-string-mnu.png']

- [RFmxNR Build Signal String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-signal-string-vi.html) Creates selector string.
- [RFmxNR Build Carrier String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-carrier-string-vi.html) Creates the carrier string.
- [RFmxNR Build Bandwidth Part String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-bandwidth-part-string-vi.html) Creates the bandwidth part string.
- [RFmxNR Build User String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-user-string-vi.html) Creates the user number string.
- [RFmxNR Build PUSCH String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-pusch-string-vi.html) Creates the PUSCH string.
- [RFmxNR Build PUSCH Cluster String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-pusch-cluster-string-vi.html) Creates a PUSCH Cluster string.
- [RFmxNR Build PDSCH String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-pdsch-string-vi.html) Creates the PDSCH string.
- [RFmxNR Build PDSCH Cluster String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-pdsch-cluster-string-vi.html) Creates a PDSCH Cluster string.
- [RFmxNR Build CORESET String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-coreset-string-vi.html) Creates the coreset string.
- [RFmxNR Build CORESET Cluster String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-coreset-cluster-string-vi.html) Creates the coreset cluster string.
- [RFmxNR Build PDCCH String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-pdcch-string-vi.html) Creates the PDCCH string.
- [RFmxNR Build Chain String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-chain-string-vi.html) Creates a chain string.
- [RFmxNR Build Layer String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-layer-string-vi.html) Creates a layer string.
- [RFmxNR Build Subblock String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-subblock-string-vi.html) Creates the subblock string.
- [RFmxNR Build Offset String VI](../../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-offset-string-vi.html) Creates the offset string.

Parent topic:

Fetch

Parent topic:

NR

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900004.html language=enus -->
## TOPIC 00004: Trigger:Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900004.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of trigger to be used for signal acquisition. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is None. Rema

### Trigger:Type

Specifies the type of trigger to be used for signal acquisition.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **None**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| None | 0 | No Reference Trigger is configured. |
| --- | --- | --- |
| Digital Edge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Slope property. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90000a.html language=enus -->
## TOPIC 00005: Trigger:Delay (s)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90000a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples. You do not need to use a selector string to configure or read this property for the d

### Trigger:Delay (s)

Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pre-trigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Delay (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90000b.html language=enus -->
## TOPIC 00006: Trigger:Minimum Quiet Time:Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90000b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defau

### Trigger:Minimum Quiet Time:Mode

Specifies whether the measurement computes the minimum quiet time used for triggering.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Min Quiet Time Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Manual | 0 | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- | --- |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900012.html language=enus -->
## TOPIC 00007: Band

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900012.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the evolved universal terrestrial radio access (E-UTRA) or NR operating frequency band of a subblock as specified in section 5.2 of the 3GPP 38.101-1/2/3 specification. Band determines the spectral flatness mask and spectral emission mask. Use "subblock<n>" as the Selector Strings to confi

### Band

Specifies the evolved universal terrestrial radio access (E-UTRA) or NR operating frequency band of a subblock as specified in section 5.2 of the *3GPP 38.101-1/2/3* specification. Band determines the spectral flatness mask and spectral emission mask.

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 78.

Valid values for frequency range 1 are 1, 2, 3, 5, 7, 8, 12, 13, 14, 18, 20, 24, 25, 26, 28, 29, 30, 31, 34, 38, 39, 40, 41, 46, 47, 48, 50, 51, 53, 54, 65, 66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104, 105, 106, 109, 110, 247, 248, 250, 251, 252, 253, 254, 255, and 256.

Valid values for frequency range 2-1 are 257, 258, 259, 260, 261, and 262.

Valid values for frequency range 2-2 are 263.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Band |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900013.html language=enus -->
## TOPIC 00008: Component Carrier Spacing Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900013.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spacing between adjacent component carriers (CCs) within a subblock. Use "subblock<n>" as the Selector Strings to configure or read this property. The default value is Nominal. Remarks The following table lists the characteristics of this property. Short Name CC Spacing Type Data type

### Component Carrier Spacing Type

Specifies the spacing between adjacent component carriers (CCs) within a subblock.

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Nominal**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CC Spacing Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Nominal | 0 | Calculates the frequency spacing between component carriers as defined in section 5.4A.1 in the 3GPP 38.101-1/2 specification and section 5.4.1.2 in the 3GPP TS 38.104 specification and sets the CC Freq property. |
| --- | --- | --- |
| User | 2 | The component carrier frequency that you configure in the CC Freq property is used. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900029.html language=enus -->
## TOPIC 00009: Component Carrier:Bandwidth Part:User:PUSCH:Number of Resource Blocks

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900029.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900029.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This property is ignored if you set the Auto RB Detection Enabled property to True. Use "puschcluster<s>" or "pusch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/c

### Component Carrier:Bandwidth Part:User:PUSCH:Number of Resource Blocks

Specifies the number of consecutive resource blocks in a physical uplink shared channel (PUSCH) cluster. This property is ignored if you set the [Auto RB Detection Enabled](/csh?topicname=attr90001f.html) property to **True**.

Use "puschcluster<*s*>" or "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>/puschcluster<*s*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is -1. If you set this property to -1, all available resource blocks for the specified bandwidth are configured.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PUSCH Num RBs |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90002f.html language=enus -->
## TOPIC 00010: ModAcc:DC Subcarrier Removal Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90002f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90002f.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the DC subcarrier is removed from the EVM results. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True.

### ModAcc:DC Subcarrier Removal Enabled

Specifies whether the DC subcarrier is removed from the EVM results.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc DC Subcarrier Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The DC subcarrier is present in the EVM results. |
| --- | --- | --- |
| True | 1 | The DC subcarrier is removed from the EVM results. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900031.html language=enus -->
## TOPIC 00011: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Configuration Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900031.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900031.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configuration type of DMRS. Use "pusch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pusch<r>" as the Selector Strings to configure or read this property. The default value is Type 1. Remarks The following table lists the charac

### Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Mapping:DMRS Configuration Type

Specifies the configuration type of DMRS.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Type 1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PUSCH DMRS Configuration Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Type 1 | 0 | One DMRS subcarrier alternates with one data subcarrier. |
| --- | --- | --- |
| Type 2 | 1 | Two consecutive DMRS subcarriers alternate with four consecutive data subcarriers. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900044.html language=enus -->
## TOPIC 00012: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Pseudo Random Sequence:Scrambling ID Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900044.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900044.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation. Use "pusch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pusch<r>" as the Selector Strings to configure or read this property. T

### Component Carrier:Bandwidth Part:User:PUSCH:DMRS:Pseudo Random Sequence:Scrambling ID Mode

Specifies whether the configured Scrambling ID is honored or the Cell ID is used for reference signal generation.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Cell ID**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PUSCH DMRS Scrambling ID Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Cell ID | 0 | The value of PUSCH DMRS Scrambling ID is based on Cell ID property. |
| --- | --- | --- |
| User Defined | 1 | The value of PUSCH DMRS Scrambling ID is specified by you. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900051.html language=enus -->
## TOPIC 00013: Component Carrier:Bandwidth Part:User:PUSCH:DMRS:DMRS Power Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900051.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900051.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the value of PUSCH DMRS Pwr property is calculated based on the PUSCH DMRS Num CDM Groups property or specified by you. Use "pusch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pusch<r>" as the Selector Strings to configure

### Component Carrier:Bandwidth Part:User:PUSCH:DMRS:DMRS Power Mode

Specifies whether the value of [PUSCH DMRS Pwr](/csh?topicname=attr900030.html) property is calculated based on the [PUSCH DMRS Num CDM Groups](/csh?topicname=attr900042.html) property or specified by you.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **CDM Groups**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PUSCH DMRS Pwr Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| CDM Groups | 0 | The value of PUSCH DMRS Pwr is calculated based on PDSCH DMRS Num CDM Groups property. |
| --- | --- | --- |
| User Defined | 1 | The value of PUSCH DMRS Pwr is specified by you. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900057.html language=enus -->
## TOPIC 00014: Component Carrier:Bandwidth Part:User:PUSCH:PTRS:PTRS Power Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900057.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900057.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the PUSCH PTRS power scaling is calculated as defined in 3GPP specification or specified by you. This property is valid only if you set the PUSCH PTRS Enabled property to True. Use "pusch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m

### Component Carrier:Bandwidth Part:User:PUSCH:PTRS:PTRS Power Mode

Specifies whether the PUSCH PTRS power scaling is calculated as defined in 3GPP specification or specified by you. This property is valid only if you set the [PUSCH PTRS Enabled](/csh?topicname=attr900055.html) property to **True**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Standard**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PUSCH PTRS Pwr Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Standard | 0 | The PUSCH PTRS Pwr scaling is calculated as defined in the Table 6.2.3.1-1 of 3GPP TS 38.214 specification. |
| --- | --- | --- |
| User Defined | 1 | The PTRS RE power scaling is given by the value of PUSCH PTRS Pwr property. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90005d.html language=enus -->
## TOPIC 00015: Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS Frequency Density

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90005d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90005d.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the density of PTRS in frequency domain. This property is valid only if you set the PUSCH PTRS Enabled property to True and PUSCH Transform Precoding Enabled property to False. Use "pusch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l

### Component Carrier:Bandwidth Part:User:PUSCH:PTRS:Mapping:PUSCH PTRS Frequency Density

Specifies the density of PTRS in frequency domain. This property is valid only if you set the [PUSCH PTRS Enabled](/csh?topicname=attr900055.html) property to **True** and [PUSCH Transform Precoding Enabled](/csh?topicname=attr90001e.html) property to **False**.

Use "pusch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pusch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **2**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PUSCH PTRS Freq Density |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 2 | 2 | The density of PTRS in frequency domain is 2. |
| --- | --- | --- |
| 4 | 4 | The density of PTRS in frequency domain is 4. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900070.html language=enus -->
## TOPIC 00016: Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Pseudo Random Sequence:Scrambling ID

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900070.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900070.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value of scrambling ID used for reference signal generation. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The foll

### Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Pseudo Random Sequence:Scrambling ID

Specifies the value of scrambling ID used for reference signal generation.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH DMRS Scrambling ID |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900074.html language=enus -->
## TOPIC 00017: Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Configuration Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900074.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900074.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configuration type of DMRS. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property. The default value is Type 1. Remarks The following table lists the charac

### Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Configuration Type

Specifies the configuration type of DMRS.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Type 1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH DMRS Configuration Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Type 1 | 0 | One DMRS subcarrier alternates with one data subcarrier. |
| --- | --- | --- |
| Type 2 | 1 | Two consecutive DMRS subcarriers alternate with four consecutive data subcarriers. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900075.html language=enus -->
## TOPIC 00018: Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:PDSCH Mapping Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900075.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900075.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the mapping type of DMRS. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property. The default value is Type A. Remarks The following table lists the characterist

### Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:PDSCH Mapping Type

Specifies the mapping type of DMRS.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Type A**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH Mapping Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Type A | 0 | The first DMRS symbol index in a slot is either 2 or 3. |
| --- | --- | --- |
| Type B | 1 | The first DMRS symbol index in a slot is 0. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900078.html language=enus -->
## TOPIC 00019: Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Additional Positions

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900078.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900078.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of additional sets of consecutive DMRS symbols in a slot. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The

### Component Carrier:Bandwidth Part:User:PDSCH:DMRS:Mapping:DMRS Additional Positions

Specifies the number of additional sets of consecutive DMRS symbols in a slot.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **0**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH DMRS Additional Positions |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 0 | 0 | No additional DMRS symbol set is present in the slot. |
| --- | --- | --- |
| 1 | 1 | One additional DMRS symbol set is present in the slot. |
| 2 | 2 | Two additional DMRS symbol sets are present in the slot. |
| 3 | 3 | Three additional DMRS symbol sets are present in the slot. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900079.html language=enus -->
## TOPIC 00020: Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900079.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether PT-RS is present in the transmitted signal. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property. The default value is False. Remarks The following tab

### Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Enabled

Specifies whether PT-RS is present in the transmitted signal.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH PTRS Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Detection of PTRS in the transmitted signal is disabled. |
| --- | --- | --- |
| True | 1 | Detection of PTRS in the transmitted signal is enabled. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90007a.html language=enus -->
## TOPIC 00021: Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Antenna Ports

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90007a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90007a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the DMRS Antenna Ports associated with PTRS transmission. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The following t

### Component Carrier:Bandwidth Part:User:PDSCH:PTRS:Antenna Ports

Specifies the DMRS Antenna Ports associated with PTRS transmission.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH PTRS Antenna Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90007b.html language=enus -->
## TOPIC 00022: Component Carrier:Bandwidth Part:User:PDSCH:PTRS:PTRS Power Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90007b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90007b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the configured PDSCH PTRS Pwr is calculated as defined in 3GPP specification or configured by you. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>/pdsch<r>" as the Selector Strings to configure or read this property

### Component Carrier:Bandwidth Part:User:PDSCH:PTRS:PTRS Power Mode

Specifies whether the configured [PDSCH PTRS Pwr](/csh?topicname=attr90007c.html) is calculated as defined in 3GPP specification or configured by you.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Standard**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH PTRS Pwr Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Standard | 0 | The PTRS RE power scaling is computed as defined in the Table 4.1-2 of 3GPP TS 38.214 specification using the value of EPRE Ratio Port property.. |
| --- | --- | --- |
| User Defined | 1 | The PTRS RE power scaling is given by the value of PDSCH PTRS Pwr property. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90007c.html language=enus -->
## TOPIC 00023: Component Carrier:Bandwidth Part:User:PDSCH:PTRS:PTRS Power (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90007c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90007c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this property is taken as an input when you set the PDSCH PTRS Pwr Mode property to User Defined. If you set the PDSCH PTRS Pwr Mode property to Standard, the value is com

### Component Carrier:Bandwidth Part:User:PDSCH:PTRS:PTRS Power (dB)

Specifies the factor by which the PDSCH PTRS REs are boosted, compared to PDSCH REs. This value is expressed in dB. The value of this property is taken as an input when you set the [PDSCH PTRS Pwr Mode](/csh?topicname=attr90007b.html) property to **User Defined**. If you set the PDSCH PTRS Pwr Mode property to **Standard**, the value is computed from other parameters.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH PTRS Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900080.html language=enus -->
## TOPIC 00024: Component Carrier:Bandwidth Part:User:PDSCH:Slot Allocation

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900080.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900080.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots. The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the following format: Single unsigned integer values or last A range of single unsigned int

### Component Carrier:Bandwidth Part:User:PDSCH:Slot Allocation

Specifies the slot allocation in NR Frame. This defines the indices of the allocated slots.

The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the following format:
 Single unsigned integer values or last
 A range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 <= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.

Examples: 2,5 will expand to {2,5}

1:3,7 will expand to {1,2,3,7}.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0-Last. Valid values are from 0 to (Maximum number of slots in frame - 1), inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH Slot Allocation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900081.html language=enus -->
## TOPIC 00025: Component Carrier:Bandwidth Part:User:PDSCH:Symbol Allocation

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900081.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900081.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the symbol allocation of each slot allocation. The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the following format: Single unsigned integer values or last A range of single unsigned integer values given as i0:i1, where i

### Component Carrier:Bandwidth Part:User:PDSCH:Symbol Allocation

Specifies the symbol allocation of each slot allocation.

The format is defined by range format specifiers. The range format specifier is a comma separated list of entries in the following format:
 Single unsigned integer values or last
 A range of single unsigned integer values given as i0:i1, where i0 represents the first and i1 the last value in the range, with i0 <= i1. The keyword last expands to the largest allowed value, depending on the context of the range specification.

Examples: 2,5 will expand to {2,5}

1:3,7 will expand to {1,2,3,7}.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0-Last. Valid values are from 0 to 13, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PDSCH Symbol Allocation |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900086.html language=enus -->
## TOPIC 00026: Component Carrier:SSB:PSS Power (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900086.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900086.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB. Use "carrier<k>" or "subblock<n>carrier<k>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The following table lists the characte

### Component Carrier:SSB:PSS Power (dB)

Specifies the power scaling value for the primary synchronization symbol in the SS/PBCH block. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PSS Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900087.html language=enus -->
## TOPIC 00027: Component Carrier:SSB:SSS Power (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900087.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900087.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB. Use "carrier<k>" or "subblock<n>carrier<k>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The following table lists the charac

### Component Carrier:SSB:SSS Power (dB)

Specifies the power scaling value for the secondary synchronization symbol in the SS/PBCH block. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SSS Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900088.html language=enus -->
## TOPIC 00028: Component Carrier:SSB:PBCH Power (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900088.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900088.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power scaling value for the PBCH REs in the SS/PBCH block. This value is expressed in dB. Use "carrier<k>" or "subblock<n>carrier<k>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The following table lists the characteristics of this proper

### Component Carrier:SSB:PBCH Power (dB)

Specifies the power scaling value for the PBCH REs in the SS/PBCH block. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PBCH Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90008c.html language=enus -->
## TOPIC 00029: Signal Detection:Auto Cell ID Detection Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90008c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90008c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the autodetection of the cell ID. When you set the Link Direction property to Downlink, autodetection of the Cell ID is not possible if the signal measured does not contain SSB with PSS/SSS, or if the PDSCH does not include enough allocated Resource Blocks. When you set t

### Signal Detection:Auto Cell ID Detection Enabled

Specifies whether to enable the autodetection of the cell ID.

When you set the [Link Direction](attr90000e.html) property to **Downlink**, autodetection of the Cell ID is not possible if the signal measured does not contain SSB with PSS/SSS, or if the PDSCH does not include enough allocated Resource Blocks.

When you set the Link Direction property to **Uplink**, autodetection of the Cell ID is not possible if the PUSCH [Transform Precoding Enabled](attr90001e.html) property is set to True, or if the PUSCH does not include enough allocated Resource Blocks.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Cell ID Detection Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | User-configured Cell ID is used. |
| --- | --- | --- |
| True | 1 | Measurement tries to autodetect the Cell ID. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900090.html language=enus -->
## TOPIC 00030: Component Carrier:Bandwidth Part:User:PDSCH:Number of PDSCH Configurations

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900090.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900090.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of PDSCH slot configurations. Use "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>" as the Selector Strings to configure or read this property. The default value is 1. Remarks The following table lists the characteristics of this p

### Component Carrier:Bandwidth Part:User:PDSCH:Number of PDSCH Configurations

Specifies the number of PDSCH slot configurations.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Num PDSCH Configurations |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900092.html language=enus -->
## TOPIC 00031: Component Carrier:Bandwidth Part:User:PDSCH:PTRS:EPRE Ratio Port

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900092.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900092.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of 3GPP TS 38.214 specification when you set the PDSCH PTRS Power Mode property to Standard. Use "pdsch<r>" or "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier

### Component Carrier:Bandwidth Part:User:PDSCH:PTRS:EPRE Ratio Port

Specifies the EPRE Ratio Port used to determine the PDSCH PT-RS RE power scaling as defined in the Table 4.1-2 of *3GPP TS 38.214* specification when you set the [PDSCH PTRS Power Mode](/csh?topicname=attr90007b.html) property to **Standard**.

Use "pdsch<*r*>" or "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>/pdsch<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | EPRE Ratio Port |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900095.html language=enus -->
## TOPIC 00032: Component Carrier:SSB:SSB Active Blocks

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900095.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900095.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SSB burst(s) indices for the SSB pattern that needs to be transmitted. Use "carrier<k>" or "subblock<n>carrier<k>" as the Selector Strings to configure or read this property. The default value is 0 - Last. Remarks The following table lists the characteristics of this property. Short Na

### Component Carrier:SSB:SSB Active Blocks

Specifies the SSB burst(s) indices for the SSB pattern that needs to be transmitted.

Use "carrier<*k*>" or "subblock<*n*>carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0 - Last.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SSB Active Blocks |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900096.html language=enus -->
## TOPIC 00033: Component Carrier:Bandwidth Part:Grid Start

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900096.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900096.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resource grid start relative to Reference Point A in terms of resource block offset when you set the Reference Grid Alignment Mode property to Manual. Use "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>" as the Selector Strings to configure or read this prop

### Component Carrier:Bandwidth Part:Grid Start

Specifies the resource grid start relative to Reference Point A in terms of resource block offset when you set the [Reference Grid Alignment Mode](/csh?topicname=attr900037.html) property to **Manual**.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Grid Start |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900108.html language=enus -->
## TOPIC 00034: Component Carrier:Bandwidth Part:CORESET:Number of Symbols

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900108.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900108.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of symbols allotted to CORESET in each slot. Use "coreset<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/coreset<l>" as the Selector Strings to configure or read this property. The default value is 1. Remarks The following table lists the char

### Component Carrier:Bandwidth Part:CORESET:Number of Symbols

Specifies the number of symbols allotted to CORESET in each slot.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CORESET Num Symbols |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90010c.html language=enus -->
## TOPIC 00035: Component Carrier:Bandwidth Part:CORESET:Precoding Granularity

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90010c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90010c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the precoding granularity of the CORESET. Use "coreset<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/coreset<l>" as the Selector Strings to configure or read this property. The default value is Same As REG Bundle. Remarks The following table lists the c

### Component Carrier:Bandwidth Part:CORESET:Precoding Granularity

Specifies the precoding granularity of the CORESET.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Same As REG Bundle**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CORESET Precoding Granularity |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Same As REG Bundle | 0 | Precoding granularity is set to Same As REG Bundle. |
| --- | --- | --- |
| All Contiguous Resource Blocks | 1 | Precoding granularity is set to All Contiguous Resource Blocks. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900110.html language=enus -->
## TOPIC 00036: Component Carrier:Bandwidth Part:CORESET:Shift Index

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900110.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900110.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shift index of CORESET for interleaved CCE to REG mapping. Use "coreset<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/coreset<l>" as the Selector Strings to configure or read this property. The default value is 0. Remarks The following table lists t

### Component Carrier:Bandwidth Part:CORESET:Shift Index

Specifies the shift index of CORESET for interleaved CCE to REG mapping.

Use "coreset<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/coreset<*l*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CORESET Shift Index |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90011a.html language=enus -->
## TOPIC 00037: Component Carrier:SSB:Grid Start

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90011a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90011a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SSB resource grid start relative to Reference Point A in terms of resource block offset. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector Strings to configure or read this property. Remarks The following table lists the characteristics of this property. Sho

### Component Carrier:SSB:Grid Start

Specifies the SSB resource grid start relative to Reference Point A in terms of resource block offset.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SSB Grid Start |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90011d.html language=enus -->
## TOPIC 00038: Component Carrier:Downlink Test Model Modulation Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90011d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90011d.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models NR-FR2-TM3.1 and NR-FR2-TM2. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector Strings to configure or read this property. The default va

### Component Carrier:Downlink Test Model Modulation Type

Specifies the modulation type to be used with the selected test model. Selecting the modulation type is supported only for test models *NR-FR2-TM3.1* and *NR-FR2-TM2*.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **Standard**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DL Test Model Mod Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Standard | 0 | Specifies a standard modulation scheme. |
| --- | --- | --- |
| QPSK | 1 | Specifies a QPSK modulation scheme. |
| 16 QAM | 2 | Specifies a 16 QAM modulation scheme. |
| 64 QAM | 3 | Specifies a 64 QAM modulation scheme. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90043b.html language=enus -->
## TOPIC 00039: Advanced:Transmitter Architecture

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90043b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90043b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RF architecture at the transmitter, whether each component carriers have a separate LO or one common LO for the entire subblock. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informat

### Advanced:Transmitter Architecture

Specifies the RF architecture at the transmitter, whether each component carriers have a separate LO or one common LO for the entire subblock.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **LO per Subblock**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Transmitter Architecture |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| LO per Component Carrier | 0 | The Carrier IQ Origin Offset Mean (dBc) and the In-Band Emission Margin (dB) are calculated as the LO per Component Carrier, the Subblock IQ Origin Offset Mean (dBc) and the Subblock In-Band Emission Margin (dB) will not be returned. |
| --- | --- | --- |
| LO per Subblock | 1 | The Subblock IQ Origin Offset Mean (dBc) and the Subblock In-Band Emission Margin (dB) are calculated as the LO per Subblock, the Carrier IQ Origin Offset Mean (dBc), and the In-Band Emission Margin (dB) will be NaN. In the case of a single carrier, the measurement returns the same value of IQ Origin Offset and In-Band Emission Margin for both components carrier and subblock results. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900ff9.html language=enus -->
## TOPIC 00040: List:Step:Timer Duration

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900ff9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900ff9.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of a given list step in units specified by List Step Timer Unit. You need to use a selector string to configure or read this property for the list step instance. The default value is 0. Remarks The following table lists the characteristics of this property. Short Name List Ste

### List:Step:Timer Duration

Specifies the duration of a given list step in units specified by [List Step Timer Unit](/csh?topicname=attr900ff6.html).

You need to use a selector string to configure or read this property for the list step instance.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | List Step Timer Duration |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr900fff.html language=enus -->
## TOPIC 00041: Trigger:IQ Power Edge:Level Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr900fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr900fff.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector

### Trigger:IQ Power Edge:Level Type

Specifies the reference for the [IQ Power Edge Level](/csh?topicname=attr900008.html) property. The IQ Power Edge Level Type property is used only when you set the [Trigger Type](/csh?topicname=attr900004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Relative**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Power Edge Level Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Relative | 0 | The IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- | --- |
| Absolute | 1 | The IQ Power Edge Level property specifies the absolute power. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90100a.html language=enus -->
## TOPIC 00042: ACP:Offset:Number of EUTRA Offsets

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90100a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions when the ACP Channel Configuration Type property is set to Standard or NS_29 or Standard Rel 16 or Standard Rel 18. For uplink ACP measurement, and for downlink A

### ACP:Offset:Number of EUTRA Offsets

Specifies the number of evolved universal terrestrial radio access (E-UTRA) adjacent channel offsets to be configured at offset positions when the [ACP Channel Configuration Type](/csh?topicname=attr90104d.html) property is set to **Standard** or **NS_29** or **Standard Rel 16** or **Standard Rel 18**. For uplink ACP measurement, and for downlink ACP measurement in frequency range 2-1 and frequency range 2-2, this property has to be 0.

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is dependent on 3GPP specification.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Num EUTRA Offsets |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90100c.html language=enus -->
## TOPIC 00043: ACP:Offset:Number of Offsets

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90100c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90100c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of configured offset channels when the ACP Channel Configuration Type property is set to Custom Use "subblock<n>" as the selector string to configure or read this property. The default value is 1. Remarks The following table lists the characteristics of this property. Short Name

### ACP:Offset:Number of Offsets

Specifies the number of configured offset channels when the [ACP Channel Configuration Type](/csh?topicname=attr90104d.html) property is set to **Custom**

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Num Offsets |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90100f.html language=enus -->
## TOPIC 00044: ACP:Offset: Sideband

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90100f.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sideband measured for the offset channel. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selector Strings to read this result. The default value is Both. Remarks The following table lists the characteristics of this property. Short Name ACP Offset Sideband Data type

### ACP:Offset: Sideband

Specifies the sideband measured for the offset channel.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

The default value is **Both**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Offset Sideband |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Neg | 0 | Configures a lower offset segment to the left of the leftmost carrier. |
| --- | --- | --- |
| Pos | 1 | Configures an upper offset segment to the right of the rightmost carrier. |
| Both | 2 | Configures both the negative and the positive offset segments. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901017.html language=enus -->
## TOPIC 00045: ACP:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901017.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the ACP RBW Auto property to False. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings top

### ACP:RBW Filter:Bandwidth (Hz)

Specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the [ACP RBW Auto](/csh?topicname=attr901016.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 30 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901018.html language=enus -->
## TOPIC 00046: ACP:RBW Filter:Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901018.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the shape of the RBW filter. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FFT Based. Remarks The following tab

### ACP:RBW Filter:Type

Specifies the shape of the RBW filter.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **FFT Based**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP RBW Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| FFT Based | 0 | No RBW filtering is performed. |
| --- | --- | --- |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901019.html language=enus -->
## TOPIC 00047: ACP:Sweep Time:Auto

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901019.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement sets the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks The fo

### ACP:Sweep Time:Auto

Specifies whether the measurement sets the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the ACP Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90101a.html language=enus -->
## TOPIC 00048: ACP:Sweep Time:Interval (s)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90101a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90101a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### ACP:Sweep Time:Interval (s)

Specifies the sweep time when you set the [ACP Sweep Time Auto](/csh?topicname=attr901019.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 ms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90101b.html language=enus -->
## TOPIC 00049: ACP:Power Units

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90101b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90101b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit for absolute power. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is dBm. Remarks The following table lis

### ACP:Power Units

Specifies the unit for absolute power.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **dBm**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Pwr Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| dBm | 0 | Indicates that the absolute power is expressed in dBm. |
| --- | --- | --- |
| dBm/Hz | 1 | Indicates that the absolute power is expressed in dBm/Hz. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90101c.html language=enus -->
## TOPIC 00050: ACP:Measurement Method

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90101c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method for performing the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Normal. Remarks Th

### ACP:Measurement Method

Specifies the method for performing the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Normal**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Meas Method |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| --- | --- | --- |
| Dynamic Range | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe 5665/5668R |
| Sequential FFT | 2 | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and the FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used for the measurement. Use this method to optimize ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Num Analysis Threads >=1 ACP Amplitude Correction Type RF Center Frequency |
| Property | Supported Value |  |
| ACP RBW Auto | True |  |
| ACP RBW Filter Type | FFT Based |  |
| ACP Averaging Count | >=1 |  |
| ACP Num Analysis Threads | >=1 |  |
| ACP Amplitude Correction Type | RF Center Frequency |  |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90101d.html language=enus -->
## TOPIC 00051: ACP:Noise Compensation:Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90101d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90101d.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx compensates for the instrument noise when performing the measurement when you set ACP Noise Cal Mode property to Auto, or when you set ACP Noise Cal Mode to Manual and ACP Meas Mode property to Measure Refer to the measurement guidelines section in the Noise Compensation Algor

### ACP:Noise Compensation:Enabled

Specifies whether RFmx compensates for the instrument noise when performing the measurement when you set [ACP Noise Cal Mode](/csh?topicname=attr90104c.html) property to **Auto**, or when you set ACP Noise Cal Mode to **Manual** and [ACP Meas Mode](/csh?topicname=attr901048.html) property to **Measure**

Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?context=rfmxspecan_rfmxspecan_noise_compensation_algorithm) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Noise Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables noise compensation. |
| --- | --- | --- |
| True | 1 | Enables noise compensation. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90101e.html language=enus -->
## TOPIC 00052: ACP:Averaging:Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90101e.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remar

### ACP:Averaging:Enabled

Specifies whether to enable averaging for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The ACP measurement uses the value of the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90101f.html language=enus -->
## TOPIC 00053: ACP:Averaging:Count

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90101f.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### ACP:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [ACP Averaging Enabled](/csh?topicname=attr90101e.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901021.html language=enus -->
## TOPIC 00054: ACP:Averaging:Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901021.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the str

### ACP:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

Default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901027.html language=enus -->
## TOPIC 00055: ACP:Advanced:Sequential FFT Size

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901027.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of bins to be used for FFT computation, when you set the ACP Meas Method property to Sequential FFT. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string

### ACP:Advanced:Sequential FFT Size

Specifies the number of bins to be used for FFT computation, when you set the [ACP Meas Method](/csh?topicname=attr90101c.html) property to **Sequential FFT**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 512.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Sequential FFT Size |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901029.html language=enus -->
## TOPIC 00056: ACP:All Traces Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901029.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901029.html
- document_id: `rfmxnr-labview-api-ref`
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
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90102a.html language=enus -->
## TOPIC 00057: ACP:Number of Analysis Threads

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90102a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90102a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the ACP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources

### ACP:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the ACP measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr901047.html language=enus -->
## TOPIC 00058: ACP:FFT:Overlap (%)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr901047.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr901047.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the samples to overlap between the consecutive chunks as a percentage of the ACP Sequential FFT Size property when you set the ACP Meas Method property to Sequential FFT and the ACP FFT Overlap Mode property to User Defined. This value is expressed as a percentage. You do not need to use a

### ACP:FFT:Overlap (%)

Specifies the samples to overlap between the consecutive chunks as a percentage of the [ACP Sequential FFT Size](/csh?topicname=attr901027.html) property when you set the [ACP Meas Method](/csh?topicname=attr90101c.html) property to **Sequential FFT** and the [ACP FFT Overlap Mode](/csh?topicname=attr901046.html) property to **User Defined**. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP FFT Overlap (%) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90104e.html language=enus -->
## TOPIC 00059: ACP:Subblock Offset (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90104e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90104e.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset of the subblock measurement relative to the subblock center. This value is expressed in Hz. Use "subblock<n>" as the Selector Strings to read this result. The default value is 0. Remarks The following table lists the characteristics of this property. Short Name ACP Subblock Offs

### ACP:Subblock Offset (Hz)

Specifies the offset of the subblock measurement relative to the subblock center. This value is expressed in Hz.

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Subblock Offset (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr903005.html language=enus -->
## TOPIC 00060: CHP:Subblock Integration Bandwidth (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr903005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr903005.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of the subblock. This value is expressed in Hz. It is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock. Use "subblock<n>" as the Selector Strings

### CHP:Subblock Integration Bandwidth (Hz)

Specifies the integration bandwidth of the subblock. This value is expressed in Hz. It is the span from left edge of the integration bandwidth of the leftmost carrier to the right edge of the integration bandwidth of the rightmost carrier within a subblock.

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Subblock IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr903006.html language=enus -->
## TOPIC 00061: CHP:Component Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr903006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr903006.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of a component carrier (CC). This value is expressed in Hz. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector Strings to read this result. The default value is 9 MHz. Remarks The following table lists the characteristics of this propert

### CHP:Component Carrier:Integration Bandwidth (Hz)

Specifies the integration bandwidth of a component carrier (CC). This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

The default value is 9 MHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP CC IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr903009.html language=enus -->
## TOPIC 00062: CHP:RBW Filter:Auto Bandwidth

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr903009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr903009.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks The follo

### CHP:RBW Filter:Auto Bandwidth

Specifies whether the measurement computes the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP RBW Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement uses the RBW that you specify in the CHP RBW (Hz) property. |
| --- | --- | --- |
| True | 1 | The measurement computes the RBW. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr903013.html language=enus -->
## TOPIC 00063: CHP:All Traces Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr903013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr903013.html
- document_id: `rfmxnr-labview-api-ref`
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
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr903025.html language=enus -->
## TOPIC 00064: CHP:Noise Calibration:Averaging:Auto

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr903025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr903025.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named

### CHP:Noise Calibration:Averaging:Auto

Specifies whether RFmx automatically computes the averaging count used for instrument noise calibration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Noise Cal Averaging Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | RFmx uses the averages that you set for CHP Noise Cal Averaging Count property. |
| --- | --- | --- |
| True | 1 | RFmx uses a noise calibration averaging count of 32. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904002.html language=enus -->
## TOPIC 00065: ModAcc:Multicarrier Filter Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904002.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this property, if number of carriers is set to more than 1 or if you set the Acq BW Optimization Enabled property to False, where in the multi carrier filter will always be

### ModAcc:Multicarrier Filter Enabled

Specifies whether to use the filter in single carrier configurations to minimize leakage into the carrier. Measurement ignores this property, if number of carriers is set to more than 1 or if you set the [Acq BW Optimization Enabled](/csh?topicname=attr90d001.html) property to **False**, where in the multi carrier filter will always be used.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Multicarrier Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Measurement doesn't use the filter. |
| --- | --- | --- |
| True | 1 | Measurement filters out unwanted emissions. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904004.html language=enus -->
## TOPIC 00066: ModAcc:Synchronization Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904004.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from slot or frame boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is

### ModAcc:Synchronization Mode

Specifies whether the measurement is performed from slot or frame boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Slot | 1 | The measurement is performed over the ModAcc Meas Length starting at the ModAcc Meas Offset from the slot boundary. If you set the Trigger Type property to Digital Edge, the measurement expects the digital trigger at the slot boundary. |
| --- | --- | --- |
| Frame | 5 | The measurement is performed over the ModAcc Meas Length starting at ModAcc Meas Offset from the frame boundary. If you set the Trigger Type property to Digital Edge, the measurement expects the digital trigger from the frame boundary. |
| SSB Start Frame | 7 | The measurement is performed over the ModAcc Meas Length starting at ModAcc Meas Offset from the frame boundary. If you set the Trigger Type property to Digital Edge, the measurement expects the digital trigger from the boundary of the frame having SSB. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904011.html language=enus -->
## TOPIC 00067: ModAcc:Averaging:Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904011.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables averaging for the measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks The following table l

### ModAcc:Averaging:Enabled

Enables averaging for the measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the ModAcc Averaging Count property. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904027.html language=enus -->
## TOPIC 00068: ModAcc:Results:In-Band Emission Margin (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904027.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns In-Band Emission Margin of the component carrier. This value is expressed in dB. Margin is the smallest difference between In-Band Emission measurement trace and limit trace. The limit is defined in section 6.4.2.3 and section 6.4F.2.3 of 3GPP 38.101-1 specification and section 6.4.2.3 of 3G

### ModAcc:Results:In-Band Emission Margin (dB)

Returns In-Band Emission Margin of the component carrier. This value is expressed in dB.

Margin is the smallest difference between In-Band Emission measurement trace and limit trace. The limit is defined in section 6.4.2.3 and section 6.4F.2.3 of *3GPP 38.101-1* specification and section 6.4.2.3 of *3GPP 38.101-2* specification. In-Band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. For NR bands, the margin is not returned in case of clustered PUSCH allocation, or when there is full allocation of resource blocks. For NR unlicensed bands, the margin is returned only for RIV=1 and RIV=5 mentioned in the section 6.4F.2.3 of *3GPP 38.101-1* specification.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/chain<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results In-Band Emission Margin (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90402c.html language=enus -->
## TOPIC 00069: ModAcc:Results:Subblock In-Band Emission Margin (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90402c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90402c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns In-Band Emission Margin of the subblock's aggregated bandwidth. This value is expressed in dB. Margin is the smallest difference between In-Band Emission measurement trace and the limit trace. The limit is defined in section 6.4A.2.2.2 of 3GPP 38.101-1 specification and section 6.4A.2.3 of 3

### ModAcc:Results:Subblock In-Band Emission Margin (dB)

Returns In-Band Emission Margin of the subblock's aggregated bandwidth. This value is expressed in dB.

Margin is the smallest difference between In-Band Emission measurement trace and the limit trace. The limit is defined in section 6.4A.2.2.2 of *3GPP 38.101-1* specification and section 6.4A.2.3 of *3GPP 38.101-2* specification. In-Band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The margin is not returned in case of clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated or when the number of carriers is greater than 2.

Use "subblock<*n*>" or "subblock<*n*>/chain<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Subblock In-Band Emission Margin (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904030.html language=enus -->
## TOPIC 00070: ModAcc:Results:Component Carrier Quadrature Error Mean (deg)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904030.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904030.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated quadrature error averaged over measurement length. This value is expressed in degrees. Quadrature error is the measure of skewness in degree of the I component with respect to the Q component of the IQ signal being measured. Use "carrier<k>" or "subblock<n>" or "subblock<n>/car

### ModAcc:Results:Component Carrier Quadrature Error Mean (deg)

Returns the estimated quadrature error averaged over measurement length. This value is expressed in degrees. Quadrature error is the measure of skewness in degree of the I component with respect to the Q component of the IQ signal being measured.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results CC Quadrature Error Mean (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904036.html language=enus -->
## TOPIC 00071: ModAcc:Results:Subblock IQ Origin Offset Mean (dBc)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904036.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904036.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the Transmitter Architecture property to LO per Subblock. Use "subblock<n>" or "subblock<n>/chain<r>" as the Selector Strings to read this r

### ModAcc:Results:Subblock IQ Origin Offset Mean (dBc)

Returns the estimated IQ origin offset averaged over measurement length in the subblock. This value is expressed in dBc. This result is valid only when you set the [Transmitter Architecture](/csh?topicname=attr90043b.html) property to **LO per Subblock**.

Use "subblock<*n*>" or "subblock<*n*>/chain<*r*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Subblock IQ Origin Offset Mean (dBc) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904080.html language=enus -->
## TOPIC 00072: ModAcc:Results:SSB:PBCH DMRS Peak EVM Maximum (% or dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904080.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904080.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns this resul

### ModAcc:Results:SSB:PBCH DMRS Peak EVM Maximum (% or dB)

Returns the maximum value calculated over measurement length of peak EVMs calculated on PBCH DMRS symbols.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PBCH DMRS Pk EVM Max |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904081.html language=enus -->
## TOPIC 00073: ModAcc:EVM Reference Data Symbols Mode

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904081.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904081.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about th

### ModAcc:EVM Reference Data Symbols Mode

Specifies whether to either use a reference waveform or an acquired waveform to create reference data symbols for EVM computation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Acquired Waveform**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc EVM Reference Data Symbols Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Acquired Waveform | 0 | Indicates that reference data symbols for EVM computation are created using the acquired waveform. |
| --- | --- | --- |
| Reference Waveform | 1 | Indicates that reference data symbols for EVM computation are created using the reference waveform. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904089.html language=enus -->
## TOPIC 00074: ModAcc:Results:Spectral Flatness:Range1-Max (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904089.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904089.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum magnitude of the EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed i

### ModAcc:Results:Spectral Flatness:Range1-Max (dB)

Returns the maximum magnitude of the EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Spectral Flatness Range1-Max (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90408a.html language=enus -->
## TOPIC 00075: ModAcc:Results:Spectral Flatness:Range1-Min (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90408a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90408a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB

### ModAcc:Results:Spectral Flatness:Range1-Min (dB)

Returns the minimum magnitude of EVM equalizer coefficients within Range1 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Spectral Flatness Range1-Min (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90408b.html language=enus -->
## TOPIC 00076: ModAcc:Results:Spectral Flatness:Range2-Max (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90408b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90408b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB

### ModAcc:Results:Spectral Flatness:Range2-Max (dB)

Returns the maximum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Spectral Flatness Range2-Max (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90408c.html language=enus -->
## TOPIC 00077: ModAcc:Results:Spectral Flatness:Range2-Min (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90408c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90408c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of 3GPP 38.101-1 specification and section 6.4.2.4.1 of 3GPP 38.101-2 specification. The value is expressed in dB

### ModAcc:Results:Spectral Flatness:Range2-Min (dB)

Returns the minimum magnitude of EVM equalizer coefficients within Range2 for the measurement unit with the worst ripple margin among all four ripple results defined in section 6.4.2.4.1 of *3GPP 38.101-1* specification and section 6.4.2.4.1 of *3GPP 38.101-2* specification. The value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Spectral Flatness Range2-Min (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr904092.html language=enus -->
## TOPIC 00078: ModAcc:Noise Compensation:Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr904092.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr904092.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the contribution of the instrument noise is compensated for EVM computation. You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use. You do not need to

### ModAcc:Noise Compensation:Enabled

Specifies whether the contribution of the instrument noise is compensated for EVM computation.

You must measure the noise floor before applying the noise compensation. The instrument noise floor is measured for the RF path used by the ModAcc measurement and cached for future use.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

Supported devices are NI 5831 and NI 5840/41. The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Noise Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Noise compensation is disabled for the measurement. |
| --- | --- | --- |
| True | 1 | Noise compensation is enabled for the measurement. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr9040a5.html language=enus -->
## TOPIC 00079: ModAcc:Transient:Power Change Threshold (dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr9040a5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr9040a5.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies transient period power change threshold level in dB. If a mean slot power has changed by more than this value from one slot to another, this slot boundary is handled as transient period. Note also that if RB mapping or modulation format has changed from one slot to another, this slot bound

### ModAcc:Transient:Power Change Threshold (dB)

Specifies transient period power change threshold level in dB.

If a mean slot power has changed by more than this value from one slot to another, this slot boundary is handled as transient period. Note also that if RB mapping or modulation format has changed from one slot to another, this slot boundary is handled as transient period as well, even though the mean power has not changed.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Transient Power Change Threshold (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr9040ac.html language=enus -->
## TOPIC 00080: ModAcc:Results:PDSCH:PDSCH Data RE Power Mean (dBm)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr9040ac.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr9040ac.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value (over Meas Length) of power calculated on PDSCH data REs. Use "user<l>" or "bwp<m>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/bwp<m>/user<l>" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property.

### ModAcc:Results:PDSCH:PDSCH Data RE Power Mean (dBm)

Returns the mean value (over Meas Length) of power calculated on PDSCH data REs.

Use "user<*l*>" or "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>/user<*l*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PDSCH Data RE Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr9040b2.html language=enus -->
## TOPIC 00081: ModAcc:Results:PDSCH:PDSCH 4096 QAM RMS EVM Mean (% or dB)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr9040b2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr9040b2.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated over measurement length on all 4096 QAM modulated PDSCH data symbols. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement returns t

### ModAcc:Results:PDSCH:PDSCH 4096 QAM RMS EVM Mean (% or dB)

Returns the mean value of RMS EVMs calculated over measurement length on all 4096 QAM modulated PDSCH data symbols.

When you set the [ModAcc EVM Unit](attr90400a.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "bwp<*m*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/bwp<*m*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PDSCH 4096 QAM RMS EVM Mean |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr906000.html language=enus -->
## TOPIC 00082: OBW:Measurement Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr906000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr906000.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the OBW measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The followi

### OBW:Measurement Enabled

Specifies whether to enable the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr906009.html language=enus -->
## TOPIC 00083: OBW:Sweep Time:Auto

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr906009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr906009.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement sets the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks The fo

### OBW:Sweep Time:Auto

Specifies whether the measurement sets the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement calculates the sweep time internally. For DL, the sweep time is calculated based on the value of the OBW RBW property, and for UL, it uses a sweep time of 1 ms. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90600f.html language=enus -->
## TOPIC 00084: OBW:FFT:Window

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90600f.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT window type to be used to reduce spectral leakage. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Flat T

### OBW:FFT:Window

Specifies the FFT window type to be used to reduce spectral leakage.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Flat Top**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW FFT Window |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| None | 0 | No spectral leakage. |
| --- | --- | --- |
| Flat Top | 1 | Spectral leakage is reduced using flat top window type. |
| Hanning | 2 | Spectral leakage is reduced using Hanning window type. |
| Hamming | 3 | Spectral leakage is reduced using Hamming window type. |
| Gaussian | 4 | Spectral leakage is reduced using Gaussian window type. |
| Blackman | 5 | Spectral leakage is reduced using Blackman window type. |
| Blackman-Harris | 6 | Spectral leakage is reduced using Blackman-Harris window type. |
| Kaiser-Bessel | 7 | Spectral leakage is reduced using Kaiser-Bessel window type. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr906015.html language=enus -->
## TOPIC 00085: OBW:Results:Subblock:Occupied Bandwidth (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr906015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr906015.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Use "subblock<n>" as the Selector Strings to read thi

### OBW:Results:Subblock:Occupied Bandwidth (Hz)

Returns the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation:

*Occupied bandwidth* = *Stop frequency* - *Start frequency*

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Occupied BW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr906018.html language=enus -->
## TOPIC 00086: OBW:Results:Subblock:Stop Frequency (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr906018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr906018.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Use "subblock<n>" as the Selector Strings to read this result. Remarks The fol

### OBW:Results:Subblock:Stop Frequency (Hz)

Returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:

*Occupied bandwidth* = *Stop frequency* - *Start frequency*

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr906020.html language=enus -->
## TOPIC 00087: OBW:Power Integration Method

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr906020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr906020.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies if the OBW measurement window is centered around the center of the channel. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defaul

### OBW:Power Integration Method

Specifies if the OBW measurement window is centered around the center of the channel.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Normal**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Power Integration Method |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Normal | 0 | The OBW measurement window is centered around the signal in the channel. |
| --- | --- | --- |
| From Center | 1 | The OBW measurement window is centered around the RF Center Frequency. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr907002.html language=enus -->
## TOPIC 00088: TXP:Measurement Offset

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr907002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr907002.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about

### TXP:Measurement Offset

Specifies the measurement offset to skip from the start of acquired waveform for TXP measurement. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TXP Meas Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr907004.html language=enus -->
## TOPIC 00089: TXP:Averaging:Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr907004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr907004.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for TXP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks T

### TXP:Averaging:Enabled

Specifies whether to enable averaging for TXP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TXP Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The number of acquisitions is 1. |
| --- | --- | --- |
| True | 1 | The measurement uses the Averaging Count for the number of acquisitions over which the measurement is averaged. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr907007.html language=enus -->
## TOPIC 00090: TXP:All Traces Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr907007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr907007.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the traces to be stored and retrieved after the TXP measurement is performed. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defaul

### TXP:All Traces Enabled

Enables the traces to be stored and retrieved after the TXP measurement is performed.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is False.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TXP All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90700a.html language=enus -->
## TOPIC 00091: TXP:Results:Average Power Mean (dBm)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90700a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90700a.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of the acquired signal. When you set the Averaging Enabled property to True, it returns the max of the peak power computed for each averaging count. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Sel

### TXP:Results:Average Power Mean (dBm)

Returns the average power of the acquired signal.

When you set the [Averaging Enabled](attr907004.html) property to **True**, it returns the max of the peak power computed for each averaging count.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **dBm**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TXP Results Avg Pwr Mean (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908000.html language=enus -->
## TOPIC 00092: SEM:Measurement Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908000.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SEM measurement. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results. The default value

### SEM:Measurement Enabled

Specifies whether to enable the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908002.html language=enus -->
## TOPIC 00093: SEM:Uplink Mask Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908002.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the spectrum emission mask used in the measurement for uplink. You must set the mask type to Custom to configure the custom offset masks. Refer to section 6.5.2 of the 3GPP 38.101 specification for more information about standard-defined mask types. You do not need to use a selector string

### SEM:Uplink Mask Type

Specifies the spectrum emission mask used in the measurement for uplink.

You must set the mask type to **Custom** to configure the custom offset masks. Refer to section 6.5.2 of the *3GPP 38.101* specification for more information about standard-defined mask types.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **General**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM UL Mask Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| General | 0 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.2-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification, Table 6.5.2.1-1 and 6.5A.2.1-1 in section 6.5.2 of the 3GPP TS 38.101-2 specification and Table 6.5B.2.1.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.1.5-1, 6.6.2.1.5-2, 6.6.2.1A.1.5-1, and 6.6.2.1A.1.5-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. If the band value is set to 46 or 96 or 102, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.5F.2.2-1 in section 6.5F.2 of the 3GPP TS 38.101-1 Specification. If the band value is set to NTN bands 254, 255 or 256, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.2.1 in section 6.5.2 of the 3GPP 38.101-5 specification. |
| --- | --- | --- |
| NS_35 | 1 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.1-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification and Table 6.5B.2.1.2.1-1 in section 6.5B of the 3GPP TS 38.101-3 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.5-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| Custom | 2 | You need to configure the SEM Num Offsets, SEM Offset Start Freq, SEM Offset Stop Freq, SEM Offset Abs Limit Start, SEM Offset Abs Limit Stop, SEM Offset Sideband, SEM Offset RBW, SEM Offset RBW Filter Type, and SEM Offset BW Integral properties for each offset. |
| NS_03 | 3 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_04 | 4 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.2-3 in section 6.5.2 of the 3GPP TS 38.101-1 specification. Subcarrier spacing can be configured through BWP Subcarrier Spacing property. Subcarrier spacing corresponding to first bandwidth part is used for computing mask. Transform precoding can be configured through PUSCH Transform Precoding Enabled property. Transform precoding corresponding to first bandwidth part is used for computing mask. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.2-3 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_06 | 5 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_21 | 6 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.1-1 and 6.6.2.2.5.1-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_27 | 7 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.8-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of intra-band contiguous CA consisting of at least one subblock with all NR carriers, for the NR subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.2A.2.3.2.1-1 in section 6.5A.2.3 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.3.4-1 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_07 | 8 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.4-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. In case of non-contiguous EN-DC consisting of at least one subblock with all E-UTRA carriers, for the E-UTRA subblock, the measurement selects the offset frequencies and limits for the SEM, as defined in Table 6.6.2.2.5.3-1 and Table 6.6.2.2.5.3-2 in section 6.6.2 of the 3GPP TS 36.521-1 specification. |
| NS_03U | 9 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. |
| NS_21 Rel 17 Onwards | 10 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.9-1 in section 6.5.2 of the 3GPP TS 38.101-1 specification. |
| NS_04N | 11 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.1-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS_05N | 12 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.2-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS_09N | 13 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS_10N | 14 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.3-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS_11N | 15 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.1-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |
| NS_12N | 16 | The measurement selects the offset frequencies and limits for SEM as defined in Table 6.5.2.3.2-1 in section 6.5.2.3 of the 3GPP TS 38.101-5 specification. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908004.html language=enus -->
## TOPIC 00094: SEM:Subblock Aggregated Channel Bandwidth (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908004.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth. Use "subblock<n>" as the Selector Strings to r

### SEM:Subblock Aggregated Channel Bandwidth (Hz)

Returns the aggregated channel bandwidth of a configured subblock. This value is expressed in Hz. The aggregated channel bandwidth is the sum of the subblock integration bandwidth and the guard bands on either side of the subblock integration bandwidth.

Use "subblock<*n*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Subblock Aggregated Ch BW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908005.html language=enus -->
## TOPIC 00095: SEM:Component Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908005.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of a component carrier. This value is expressed in Hz. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector Strings to read this result. The default value is 9 MHz. Remarks The following table lists the characteristics of this property. Shor

### SEM:Component Carrier:Integration Bandwidth (Hz)

Returns the integration bandwidth of a component carrier. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

The default value is 9 MHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM CC IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90800c.html language=enus -->
## TOPIC 00096: SEM:Offset:Bandwidth Integral

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90800c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90800c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW. When you set this property to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is eq

### SEM:Offset:Bandwidth Integral

Specifies the resolution of a spectrum to compare with the spectral mask limits as an integer multiple of the RBW.

When you set this property to a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of a bandwidth integral and a RBW.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset BW Integral |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90800e.html language=enus -->
## TOPIC 00097: SEM:Offset:Absolute Limit:Start (dBm)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90800e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90800e.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selector Strings to configure or read this property. The default value is -21. Remarks The following table lists

### SEM:Offset:Absolute Limit:Start (dBm)

Specifies the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is -21.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Abs Limit Start (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908012.html language=enus -->
## TOPIC 00098: SEM:Sweep Time:Auto

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908012.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement sets the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks The fo

### SEM:Sweep Time:Auto

Specifies whether the measurement sets the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the SEM Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90801b.html language=enus -->
## TOPIC 00099: SEM:Results:Total Aggregated Power (dBm)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90801b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90801b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm. You do not need to use a selector string to read this property for the default signal instance.

### SEM:Results:Total Aggregated Power (dBm)

Returns the sum of powers of all the subblocks. This value includes the power in the inter-carrier gap within a subblock, but it excludes power in the inter-subblock gaps. This value is expressed in dBm.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Total Aggregated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90801c.html language=enus -->
## TOPIC 00100: SEM:Results:Measurement Status

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90801c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90801c.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall measurement status based on the standard mask type that you configure in the SEM UL Mask Type property. You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for

### SEM:Results:Measurement Status

Returns the overall measurement status based on the standard mask type that you configure in the [SEM UL Mask Type](/csh?topicname=attr908002.html) property.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Fail | 0 | Indicates that the measurement has failed. |
| --- | --- | --- |
| Pass | 1 | Indicates that the measurement has passed. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908024.html language=enus -->
## TOPIC 00101: SEM:Results:Lower Offset:Measurement Status

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908024.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the SEM UL Mask Type property. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selector Strings to read this result. Remarks The following table lists the c

### SEM:Results:Lower Offset:Measurement Status

Returns the measurement status based on the spectrum emission limits defined by the standard mask type that you configure in the [SEM UL Mask Type](/csh?topicname=attr908002.html) property.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| Fail | 0 | Indicates that the measurement has failed. |
| --- | --- | --- |
| Pass | 1 | Indicates that the measurement has passed. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908029.html language=enus -->
## TOPIC 00102: SEM:Results:Lower Offset:Peak Frequency (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908029.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908029.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property.

### SEM:Results:Lower Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power occurs in the lower (negative) offset segment. This value is expressed in Hz.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908033.html language=enus -->
## TOPIC 00103: SEM:Results:Upper Offset:Peak Frequency (Hz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908033.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908033.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property.

### SEM:Results:Upper Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power occurs in the upper (positive)offset segment. This value is expressed in Hz.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908038.html language=enus -->
## TOPIC 00104: SEM:Downlink Mask Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908038.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908038.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the limits to be used in the measurement for Downlink. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Standard.

### SEM:Downlink Mask Type

Specifies the limits to be used in the measurement for Downlink.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Standard**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM DL Mask Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Standard | 0 | The measurement selects the offset frequencies and limits for SEM, as defined in Table 6.6.4.2.1-1, Table 6.6.4.2.1-2, Table 6.6.4.2.2.1-1, Table 6.6.4.2.2.1-2, Table 6.6.4.2.2.2-1, Table 6.6.4.2.3-1, Table 6.6.4.2.3-2, and Table 6.6.4.2.4-1 in section 6.6.4 and Table 9.7.4.3.2-1, 9.7.4.3.2-2, 9.7.4.3.3-1 and 9.7.4.3.3-2 in section 9.7.4 of the 3GPP TS 38.104 Specification. If the band value is set to 46 or 96 or 102 the measurement selects the offset frequencies and limits for SEM as defined in Table 6.6.4.5.5A-1, Table 6.6.4.5.5A-2, Table 6.6.4.5.5A-3, and Table 6.6.4.5.5A-4, in section 6.6.4.5 of the 3GPP TS 38.141-1 Specification. If the band value is set to NTN bands 254, 255 or 256, the measurement selects the offset frequencies and limits for SEM as defined in Table 6.6.4.2-1 in section 6.6.4 of the 3GPP 38.108 specification. The offset frequencies in Table 9.7.4.3.2-1, 9.7.4.3.2-2, 9.7.4.3.3-1 and 9.7.4.3.3-2 are relative to the contiguous transmission bandwidth edge. The measurement converts these offset frequencies to make them relative to the subblock edge before applying the masks. For frequency range 1, the gNodeB Category property can be set to any of the following values: Wide Area Base Station - Category A, Wide Area Base Station - Category B Option1, Wide Area Base Station - Category B Option2, Local Area Base Station, or Medium Range Base Station. Set the Band property for selecting limits table within a gNodeB category. For frequency range 2-1 and frequency range 2-2, the gNodeB Category property can be set to any of the following values: FR2 Category A or FR2 Category B. Set the Band property for selecting limits table. |
| --- | --- | --- |
| Custom | 2 | Specifies that limits are applied based on user-defined offset segments. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr908042.html language=enus -->
## TOPIC 00105: SEM:Offset:Frequency Definition

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr908042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr908042.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the definition of the the start frequency and stop frequency of the offset segments. If this property is not configured, the following values are used based on other configurations - Carrier Edge to Meas BW Center for a single-carrier configuration, Subblock Edge to Meas BW Center for a mu

### SEM:Offset:Frequency Definition

Specifies the definition of the the start frequency and stop frequency of the offset segments.

If this property is not configured, the following values are used based on other configurations - Carrier Edge to Meas BW Center for a single-carrier configuration, Subblock Edge to Meas BW Center for a multi-carrier configuration, and Carrier Center to Meas BW Center for a single-carrier configuration in the bands n46, n96, and n102 as defined in the 3GPP TS 37.213 for the shared spectrum channel access.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Frequency Definition |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Carrier Center to Meas BW Center | 0 | The start frequency and stop frequency are defined from the center of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. |
| --- | --- | --- |
| Carrier Edge to Meas BW Center | 2 | The start frequency and stop frequency are defined from the nearest edge of the closest carrier channel bandwidth to the center of the offset segment measurement bandwidth. |
| Subblock Edge to Meas BW Center | 6 | The start frequency and stop frequency are defined from the subblock edge of the closest subblock bandwidth to the center of the offset segment measurement bandwidth. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909000.html language=enus -->
## TOPIC 00106: PVT:Measurement Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909000.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the PVT measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The followi

### PVT:Measurement Enabled

Specifies whether to enable the PVT measurement.

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

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909004.html language=enus -->
## TOPIC 00107: PVT:Averaging:Count

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909004.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the PVT Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### PVT:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [PVT Averaging Enabled](/csh?topicname=attr909003.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909005.html language=enus -->
## TOPIC 00108: PVT:Averaging:Type

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909005.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement averaging type. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RMS. Remarks The following table

### PVT:Averaging:Type

Specifies the measurement averaging type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909009.html language=enus -->
## TOPIC 00109: PVT:All Traces Enabled

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909009.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the strin

### PVT:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90900b.html language=enus -->
## TOPIC 00110: PVT:Number of Analysis Threads

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90900b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90900b.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism inside the PVT measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resour

### PVT:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism inside the PVT measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909014.html language=enus -->
## TOPIC 00111: PVT:Measurement Interval Auto

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909014.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement interval is computed by the measurement or configured by the user through Measurement Interval property. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information

### PVT:Measurement Interval Auto

Specifies whether the measurement interval is computed by the measurement or configured by the user through [Measurement Interval](/csh?topicname=attr909015.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

Setting this property to **FALSE** is supported for downlink only. The default value is **True**. Refer to measurement guidelines details in the [NR Power Vs Time](/csh?context=rfmxnr_rfmxnr_pvt) concept help for more information.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Meas Interval Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Measurement Interval is defined by the Measurement Interval property. |
| --- | --- | --- |
| True | 1 | Measurement Inteval is computed by the measurement. |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909016.html language=enus -->
## TOPIC 00112: PVT:Results:Peak Windowed OFF Power (dBm/MHz)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909016.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NaN for the uplink direction, while it returns the peak power value of 70/N us windowed power during all OFF regions in the measurement interval. This value is expressed in dBm/MHz. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the Selector Strings to read this result.

### PVT:Results:Peak Windowed OFF Power (dBm/MHz)

Returns the NaN for the uplink direction, while it returns the peak power value of 70/N us windowed power during all OFF regions in the measurement interval. This value is expressed in dBm/MHz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Results Pk Windowed OFF Pwr (dBm/MHz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr909018.html language=enus -->
## TOPIC 00113: PVT:Results:Peak Windowed OFF Power Time (s)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr909018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr909018.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NaN for the uplink direction, while it returns the time offset of the PVT Results Pk Windowed OFF Pwr. This value is expressed in seconds. Remarks The following table lists the characteristics of this property. Short Name PVT Results Pk Windowed OFF Pwr Time (s) Data type cdbl.png Permis

### PVT:Results:Peak Windowed OFF Power Time (s)

Returns the NaN for the uplink direction, while it returns the time offset of the [PVT Results Pk Windowed OFF Pwr](/csh?topicname=attr909016.html). This value is expressed in seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Results Pk Windowed OFF Pwr Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=resource/objmgr/rfmxnr-rc/rfmxnr/attr90c000.html language=enus -->
## TOPIC 00114: Result Fetch Timeout (s)

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `resource/objmgr/rfmxnr-rc/rfmxnr/attr90c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxnr-rc/rfmxnr/attr90c000.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxNR Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete. The defaul

### Result Fetch Timeout (s)

Specifies the time to wait before results are available in the RFmxNR Property Node. This value is expressed in seconds.

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmx Property Node waits until the measurement is complete.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Result Fetch Timeout (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxNR Properties

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-analyze-n-wfms-iq-vi.html language=enus -->
## TOPIC 00115: RFmxNR Analyze N Wfms (IQ) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-analyze-n-wfms-iq-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-analyze-n-wfms-iq-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform(s) that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommen

### RFmxNR Analyze N Wfms (IQ) VI

Performs the enabled measurements on the I/Q complex waveform(s) that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

When using the Analysis-Only mode in RFmxNR, the RFmx driver ignores the RFmx hardware settings such as reference level and attenuation. The only RF hardware settings that are not ignored are the center frequency and trigger type, since it is needed for spectral measurement traces as well as some measurements such as ModAcc, ACP, and SEM.

Note

RFmxInstr Property Node

RFmx NR Commit

[IMAGE alt='icon' src='rfmxnr-analyze-n-wfms-iq-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. IQ — IQ specifies the waveform array where each element contains data for a complex waveform including start, delta, and actual values. x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxNR Analyze2 VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-analyze-n-wfms-spectrum-vi.html language=enus -->
## TOPIC 00116: RFmxNR Analyze N Wfms (Spectrum) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-analyze-n-wfms-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-analyze-n-wfms-spectrum-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum(s) that you specify in the Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommende

### RFmxNR Analyze N Wfms (Spectrum) VI

Performs the enabled measurements on the spectrum(s) that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **Spectral** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx NR Commit

[IMAGE alt='icon' src='rfmxnr-analyze-n-wfms-spectrum-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Spectrum — Spectrum specifies the waveform array where each element contains data for a spectrum waveform including start, delta, and actual values. x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y specifies the array of real-value power spectrum. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y specifies the array of real-value power spectrum. |

Parent topic:

RFmxNR Analyze2 VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-chain-string-vi.html language=enus -->
## TOPIC 00117: RFmxNR Build Chain String VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-chain-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-chain-string-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a chain string. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result n

### RFmxNR Build Chain String VI

Creates a chain string.

[IMAGE alt='icon' src='rfmxnr-build-chain-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "signal::sig1/result::r1/subblock0/carrier0" "result::r1/subblock0/carrier0" You can use the RFmxNR Build Subblock String VI to build the selector string. Chain Number — Chain Number specifies the chain number for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-layer-string-vi.html language=enus -->
## TOPIC 00118: RFmxNR Build Layer String VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-layer-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-build-layer-string-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a layer string. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result n

### RFmxNR Build Layer String VI

Creates a layer string.

[IMAGE alt='icon' src='rfmxnr-build-layer-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" "result::r1/subblock0/carrier0" You can use the RFmxNR Build Subblock String VI to build the selector string. Layer Number — Layer Number specifies the layer number for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-commit-vi.html language=enus -->
## TOPIC 00119: RFmxNR Commit VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-commit-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this VI is optional. RFmxNR commits settings to the hardware when you call the RFmxNR Initiate VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name,

### RFmxNR Commit VI

Commits settings to the hardware. Calling this VI is optional. RFmxNR commits settings to the hardware when you call the [RFmxNR Initiate](/csh?context=rfmxnr_rfmxnrvi_rfmxnr_initiate) VI.

[IMAGE alt='icon' src='rfmxnr-commit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00120: RFmxNR Configure Digital Edge Trigger VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-digital-edge-trigger-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. Spectral measurements are sometimes implemented with multiple acquisitions and therefore will require that digital triggers are sent for each acquisition. Multiple factors, including the desi

### RFmxNR Configure Digital Edge Trigger VI

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

Spectral measurements are sometimes implemented with multiple acquisitions and therefore will require that digital triggers are sent for each acquisition. Multiple factors, including the desired span versus the realtime bandwidth of the hardware, affect the number of acquisitions. NI recommends repeating the generation until the measurement is completed in order to ensure that all the acquisitions are triggered.

[IMAGE alt='icon' src='rfmxnr-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital edge trigger. This parameter is used when you set the Trigger Type property to Digital Edge. The default value of this parameter is hardware dependent. PFI0 (0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. Digital Edge — Digital Edge specifies the source terminal for the digital edge trigger. This parameter is used when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| PFI0 (0) | The trigger is received on PFI 0. |
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
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

RFmxNR Configure Trigger VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-frequency-frequency-vi.html language=enus -->
## TOPIC 00121: RFmxNR Configure Frequency (Frequency) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-frequency-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-frequency-frequency-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, t

### RFmxNR Configure Frequency (Frequency) VI

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxnr-configure-frequency-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the expected carrier frequency, in Hz, of the RF signal to acquire. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-multiple-vi.html language=enus -->
## TOPIC 00122: RFmxNR Configure Selected Ports (Multiple) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-multiple-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the selected ports to each chain based on the values you set in Num Receive Chains property. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used.

### RFmxNR Configure Selected Ports (Multiple) VI

Configures the selected ports to each chain based on the values you set in [Num Receive Chains](/csh?context=rfmxnr_rfmxnrprop_attr90d003) property.

[IMAGE alt='icon' src='rfmxnr-configure-selected-ports-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Selected Ports — Selected Ports specifies the list of MIMO ports to be configured. Use "port::<deviceName>/<channelNumber>" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::<deviceName>/<channelNumber>/<instrPort>". Example: port::myrfsa1/0/if1 You can use the RFmxInstr Build Port String VI to build the selected port. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR Configure Selected Ports VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-single-vi.html language=enus -->
## TOPIC 00123: RFmxNR Configure Selected Ports (Single) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-single-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the selected ports. You do not need to use the Selector String parameter to configure this VI for the default signal instance if the session is initialized with RFmxInstr Initialize NIRFSA VI. On a MIMO session, use "subblock<n>/chain<k>" as the selector string. To perform a MIMO measurem

### RFmxNR Configure Selected Ports (Single) VI

Configures the selected ports.

You do not need to use the **Selector String** parameter to configure this VI for the default signal instance if the session is initialized with [RFmxInstr Initialize NIRFSA](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_initialize_nirfsa) VI.

On a MIMO session, use "subblock<*n*>/chain<*k*>" as the selector string. To perform a MIMO measurement, you must configure the [Selected Ports](/csh?context=rfmxnr_rfmxnrprop_attr900ffd) property for the configured number of subblocks and chains.

[IMAGE alt='icon' src='rfmxnr-configure-selected-ports-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and chain number. If you do not specify the signal name, the default signal instance is used. The default value is "chain0". Example: "chain0" "signal::sig1/chain0" You can use the RFmxNR Build Chain String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Selected Ports — Selected Ports specifies the instrument port to be configured to acquire a signal. On a MIMO session, this value specifies one of the initialized devices. Use "port::<deviceName>/<channelNumber>" as the format for the selected port. For PXIe-5830/5831/5832 devices on a MIMO session, the selected port includes the instrument port in the format "port::<deviceName>/<channelNumber>/<instrPort>". Example: port::myrfsa1/0/if1 You can use the RFmxInstr Build Port String VI to build the selected port. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR Configure Selected Ports VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-vi.html language=enus -->
## TOPIC 00124: RFmxNR Configure Selected Ports VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the instrument port to acquire a signal. Use the RFmxInstr Get Available Ports VI to get the valid port names. icon

### RFmxNR Configure Selected Ports VI

Configures the instrument port to acquire a signal. Use the [RFmxInstr Get Available Ports](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_get_available_ports) VI to get the valid port names.

[IMAGE alt='icon' src='rfmxnr-configure-selected-ports-vi.png']

- [RFmxNR Configure Selected Ports (Single) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-single-vi.html) Configures the selected ports.
- [RFmxNR Configure Selected Ports (Multiple) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-configure-selected-ports-multiple-vi.html) Configures the selected ports to each chain based on the values you set in Num Receive Chains property.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-create-list-step-vi.html language=enus -->
## TOPIC 00125: RFmxNR Create List Step VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-create-list-step-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-create-list-step-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new list step instance in a list. Supported devices:PXIe-5840/5841/5842/5860 icon Inputs/Outputs cstr.png Selector String Selector String specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" You

### RFmxNR Create List Step VI

Creates a new list step instance in a list.

**Supported devices:**PXIe-5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxnr-create-list-step-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" You can use the RFmxNR Build List String VI to build the selector string or use the Selector String Out parameter from the RFmxNR Create List VI. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of the configure and fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

List

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-configure-measurement-mode-vi.html language=enus -->
## TOPIC 00126: RFmxNR ModAcc Configure Measurement Mode VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-configure-measurement-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-configure-measurement-mode-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement mode for the ModAcc measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "

### RFmxNR ModAcc Configure Measurement Mode VI

Configures the measurement mode for the ModAcc measurement.

[IMAGE alt='icon' src='rfmxnr-modacc-configure-measurement-mode-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Mode — Measurement Mode specifies whether the measurement should calibrate the noise floor of the analyzer or perform the ModAcc measurement. The default value is Measure. Measure (0) The ModAcc measurement is performed on the acquired signal. Calibrate Noise Floor (1) The ModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Measure (0) | The ModAcc measurement is performed on the acquired signal. |
| Calibrate Noise Floor (1) | The ModAcc measurement measures the noise floor of the instrument across the frequency range of interest determined by the carrier frequency and channel bandwidth. In this mode, the measurement expects that the signal generator to be turned off and checks whether no signal power is detected at the RF In port of the analyzer beyond a certain threshold. All scalar results and traces are invalid in this mode. Even if the instrument noise floor is previously calibrated, the measurement performs all the required acquisitions and overwrites any pre-existing noise floor calibration data. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-mean-vi.html language=enus -->
## TOPIC 00127: RFmxNR ModAcc Fetch Frequency Error Mean VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-mean-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-mean-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<q>" as the selector string to read this result. icon Inputs/Outputs cstr.png Selector String

### RFmxNR ModAcc Fetch Frequency Error Mean VI

Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read this result.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-frequency-error-mean-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency Error Mean (Hz) — Frequency Error Mean returns the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-per-slot-maximum-trace-vi.html language=enus -->
## TOPIC 00128: RFmxNR ModAcc Fetch Frequency Error per Slot Maximum Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-per-slot-maximum-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-per-slot-maximum-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<q>" as the selector string to read

### RFmxNR ModAcc Fetch Frequency Error per Slot Maximum Trace VI

Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read this result.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-frequency-error-per-slot-maximum-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency Error per Slot Maximum (Hz) — Frequency Error per Slot Maximum returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz. x0 — x0 returns the index of the first active slot. dx — dx returns the increment value. This is always set to one slot. y — y returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the index of the first active slot. dx — dx returns the increment value. This is always set to one slot. y — y returns an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-in-band-emission-trace-vi.html language=enus -->
## TOPIC 00129: RFmxNR ModAcc Fetch In-Band Emission Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-in-band-emission-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-in-band-emission-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier l

### RFmxNR ModAcc Fetch In-Band Emission Trace VI

Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4.2.3 of *3GPP 38.101-1*, and section 6.4.2.3 of *3GPP 38.101-2*. The trace is not returned when there is full allocation of bandwidth, or there is clustered PUSCH or there is more than one active component carrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/chain<*r*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-in-band-emission-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/chain0". Example: "subblock0/carrier0/chain0" "signal::sig1/subblock0/carrier0/chain0" "result::r1/subblock0/carrier0/chain0" "signal::sig1/result::r1/subblock0/carrier0/chain0" You can use the RFmxNR Build Carrier String and RFmxNR Build Chain StringVIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. In Band Emission (dBm) — In Band Emission returns the in-band emission margin. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. In Band Emission Mask (dB) — In Band Emission Mask returns the in-band emission mask. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the in-band emission limit value as an array for each of the resource blocks. The in-band emission limit for regions such as general, carrier leakage and IQ image, are evaluated according to the method defined in the 3GPP specification and concatenated to form a composite limit trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the in-band emission value as an array for each of the resource blocks. In-band emission is the interference falling into non-allocated resource blocks. This value is expressed in dB. |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the in-band emission limit value as an array for each of the resource blocks. The in-band emission limit for regions such as general, carrier leakage and IQ image, are evaluated according to the method defined in the 3GPP specification and concatenated to form a composite limit trace. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00130: RFmxNR ModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean value of IQ Quadrature Error. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subbl

### RFmxNR ModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace VI

Fetches the mean value of IQ Quadrature Error.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. IQ Quadrature Error per Subcarrier Mean (deg) — IQ Quadrature Error per Subcarrier Mean returns the mean value of IQ Quadrature Error. This value is expressed in degrees. x0 — x0 returns the start point of the of the resource grid. dx — dx returns the sampling duration of the analyzed signal. y — y returns the mean value of IQ Quadrature Error. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource grid. dx — dx returns the sampling duration of the analyzed signal. y — y returns the mean value of IQ Quadrature Error. This value is expressed in degrees. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00131: RFmxNR ModAcc Fetch PBCH Data RMS EVM per Subcarrier Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH data RMS EVM of each subcarrier. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result nam

### RFmxNR ModAcc Fetch PBCH Data RMS EVM per Subcarrier Mean Trace VI

Fetches the mean PBCH data RMS EVM of each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pbch-data-rms-evm-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PBCH Data RMS EVM per Subcarrier Mean (% or dB) — PBCH Data RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PBCH data within the Meas Length property. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 — x0 returns the start point of the of the resource grid. dx — dx returns the subcarrier spacing of SSB. y — y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH data within the measurement length. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource grid. dx — dx returns the subcarrier spacing of SSB. y — y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH data within the measurement length. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00132: RFmxNR ModAcc Fetch PBCH Data RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH data RMS EVM for each symbol. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name,

### RFmxNR ModAcc Fetch PBCH Data RMS EVM per Symbol Mean Trace VI

Fetches the mean PBCH data RMS EVM for each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pbch-data-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PBCH Data RMS EVM per Symbol Mean (% or dB) — PBCH Data RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the allocated subcarriers allocated with PBCH data within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 — x0 returns the start symbol index from the frame start in terms of SSB numerology. dx — dx returns the width in terms of symbols. y — y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH data within symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index from the frame start in terms of SSB numerology. dx — dx returns the width in terms of symbols. y — y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH data within symbol. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-constellation-trace-vi.html language=enus -->
## TOPIC 00133: RFmxNR ModAcc Fetch PBCH DMRS Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifie

### RFmxNR ModAcc Fetch PBCH DMRS Constellation Trace VI

Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pbch-dmrs-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PBCH DMRS Constellation — PBCH DMRS Constellation returns the PBCH DMRS trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00134: RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Subcarrier Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH DMRS RMS EVM for each subcarrier. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result na

### RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Subcarrier Mean Trace VI

Fetches the mean PBCH DMRS RMS EVM for each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PBCH DMRS RMS EVM per Subcarrier Mean (% or dB) — PBCH DMRS RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with PBCH DMRS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 — x0 returns the start point of the of the resource grid. dx — dx returns the subcarrier spacing of SSB. y — y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH DMRS within the measurement length. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource grid. dx — dx returns the subcarrier spacing of SSB. y — y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with PBCH DMRS within the measurement length. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00135: RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean PBCH DMRS RMS EVM for each symbol. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name,

### RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Symbol Mean Trace VI

Fetches the mean PBCH DMRS RMS EVM for each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PBCH DMRS RMS EVM per Symbol Mean (% or dB) — PBCH DMRS RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 — x0 returns the start symbol index from the frame start in terms of SSB numerology. dx — dx returns the width in terms of symbols. y — y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index from the frame start in terms of SSB numerology. dx — dx returns the width in terms of symbols. y — y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with PBCH DMRS within symbol. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-1024qam-constellation-trace-vi.html language=enus -->
## TOPIC 00136: RFmxNR ModAcc Fetch PDSCH 1024QAM Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-1024qam-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-1024qam-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PDSCH 1024 QAM constellation trace. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subb

### RFmxNR ModAcc Fetch PDSCH 1024QAM Constellation Trace VI

Fetches the PDSCH 1024 QAM constellation trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-1024qam-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. 1024 QAM Constellation — 1024 QAM Constellation returns the 1024 QAM constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-16qam-constellation-trace-vi.html language=enus -->
## TOPIC 00137: RFmxNR ModAcc Fetch PDSCH 16QAM Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-16qam-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-16qam-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 16 QAM trace. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subblock number, and car

### RFmxNR ModAcc Fetch PDSCH 16QAM Constellation Trace VI

Fetches PDSCH 16 QAM trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-16qam-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. 16 QAM Constellation — 16 QAM Constellation returns the 16 QAM constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-256qam-constellation-trace-vi.html language=enus -->
## TOPIC 00138: RFmxNR ModAcc Fetch PDSCH 256QAM Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-256qam-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-256qam-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 256 QAM trace. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subblock number, and ca

### RFmxNR ModAcc Fetch PDSCH 256QAM Constellation Trace VI

Fetches PDSCH 256 QAM trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-256qam-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. 256 QAM Constellation — 256 QAM Constellation returns the 256 QAM constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-8psk-constellation-trace-vi.html language=enus -->
## TOPIC 00139: RFmxNR ModAcc Fetch PDSCH 8PSK Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-8psk-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-8psk-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH 8 PSK constellation trace. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subblock nu

### RFmxNR ModAcc Fetch PDSCH 8PSK Constellation Trace VI

Fetches PDSCH 8 PSK constellation trace.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-8psk-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. 8 PSK Constellation — 8 PSK Constellation returns the PDSCH 8 PSK constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-data-constellation-trace-vi.html language=enus -->
## TOPIC 00140: RFmxNR ModAcc Fetch PDSCH Data Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-data-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-data-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated. Use "user<k>" or "carrier<l>" or "subblock<n>" or "subblock<n>/carrier<l>/user<k>" as the selector string to read this VI. icon Inputs/Outputs cstr.png Select

### RFmxNR ModAcc Fetch PDSCH Data Constellation Trace VI

Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-data-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PDSCH Data Constellation — PDSCH Data Constellation returns the PDSCH data constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-demodulated-bits-vi.html language=enus -->
## TOPIC 00141: RFmxNR ModAcc Fetch PDSCH Demodulated Bits VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-demodulated-bits-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-demodulated-bits-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String s

### RFmxNR ModAcc Fetch PDSCH Demodulated Bits VI

Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-demodulated-bits-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Bits — Bits returns an array of the recovered bits during EVM calculation. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-dmrs-constellation-trace-vi.html language=enus -->
## TOPIC 00142: RFmxNR ModAcc Fetch PDSCH DMRS Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-dmrs-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-dmrs-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated. Use "user<k>" or "carrier<l>" or "subblock<n>" or "subblock<n>/carrier<l>/user<k>" as the selector string to read this VI. icon Inputs/Outputs cstr.png Selector String Selector String spe

### RFmxNR ModAcc Fetch PDSCH DMRS Constellation Trace VI

Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" as the selector string to read this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pdsch-dmrs-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and user number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0". Example: "subblock0/carrier0/user0" "signal::sig1/subblock0/carrier0/user0" "result::r1/subblock0/carrier0/user0" "signal::sig1/result::r1/subblock0/carrier0/user0" You can use the RFmxNR Build User String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PDSCH DMRS Constellation — PDSCH DMRS Constellation returns the PDSCH DMRS constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-per-symbol-maximum-trace-vi.html language=enus -->
## TOPIC 00143: RFmxNR ModAcc Fetch Peak EVM per Symbol Maximum Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-per-symbol-maximum-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-per-symbol-maximum-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak value of EVM for each symbol computed across all the allocated subcarriers. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<q>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector S

### RFmxNR ModAcc Fetch Peak EVM per Symbol Maximum Trace VI

Fetches the peak value of EVM for each symbol computed across all the allocated subcarriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-peak-evm-per-symbol-maximum-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Peak EVM per Symbol Maximum (% or dB) — Peak EVM per Symbol Maximum returns the peak value of EVM for each symbol computed across all the allocated subcarriers. x0 — x0 returns the starting OFDM symbol position corresponding to the Modacc meas offset property. dx — dx returns 1 as the value. y — y returns an array the the peak value of EVM for each symbol computed across all the allocated subcarriers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol position corresponding to the Modacc meas offset property. dx — dx returns 1 as the value. y — y returns an array the the peak value of EVM for each symbol computed across all the allocated subcarriers. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-ptrs-constellation-trace-vi.html language=enus -->
## TOPIC 00144: RFmxNR ModAcc Fetch PUSCH PTRS Constellation Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-ptrs-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-ptrs-constellation-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated. Use "user<k>" or "carrier<l>" or "subblock<n>" or "subblock<n>/carrier<l>/user<k>" or "subblock<n>/carrier<k>/user<k>/layer<q>" as the selector string to read this VI. icon Inputs/Outputs

### RFmxNR ModAcc Fetch PUSCH PTRS Constellation Trace VI

Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated.

Use "user<*k*>" or "carrier<*l*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*l*>/user<*k*>" or "subblock<*n*>/carrier<*k*>/user<*k*>/layer<*q*>" as the selector string to read this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-pusch-ptrs-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, user number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/user0/layer0". Example: "subblock0/carrier0/user0/layer0" "signal::sig1/subblock0/carrier0/user0/layer0" "result::r1/subblock0/carrier0/user0/layer0" "signal::sig1/result::r1/subblock0/carrier0/user0/layer0" You can use the RFmxNR Build User String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. PUSCH PTRS Constellation — PUSCH PTRS Constellation returns the PUSCH PTRS constellation trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-slot-mean-trace-vi.html language=enus -->
## TOPIC 00145: RFmxNR ModAcc Fetch RMS EVM per Slot Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-slot-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-slot-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<q>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Select

### RFmxNR ModAcc Fetch RMS EVM per Slot Mean Trace VI

Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-rms-evm-per-slot-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RMS EVM per Slot Mean (% or dB) — RMS EVM per Slot Mean returns the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00146: RFmxNR ModAcc Fetch RMS EVM per Subcarrier Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<q>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector St

### RFmxNR ModAcc Fetch RMS EVM per Subcarrier Mean Trace VI

Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-rms-evm-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RMS EVM per Subcarrier Mean (% or dB) — RMS EVM per Subcarrier Mean returns the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array the EVM of each allocated subcarrier averaged across all the symbols within the measurement length. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00147: RFmxNR ModAcc Fetch RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" or "subblock<n>/carrier<k>/layer<q>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector St

### RFmxNR ModAcc Fetch RMS EVM per Symbol Mean Trace VI

Fetches the EVM on each symbol within the measurement length averaged across all the allocated subcarriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. RMS EVM per Symbol Mean (% or dB) — RMS EVM per Symbol Mean returns the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. x0 — x0 returns the starting OFDM symbol position corresponding to the Modacc meas offset property. dx — dx returns 1 as the value. y — y returns an array the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the starting OFDM symbol position corresponding to the Modacc meas offset property. dx — dx returns 1 as the value. y — y returns an array the EVM on each symbol within the measurement length averaged across all the allocated subcarriers. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-spectral-flatness-trace-vi.html language=enus -->
## TOPIC 00148: RFmxNR ModAcc Fetch Spectral Flatness Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-spectral-flatness-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-spectral-flatness-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of 3GPP TS 38.521-1 specification. Use "carrier<k>" or "subblock<n>" or "subblock<n>/c

### RFmxNR ModAcc Fetch Spectral Flatness Trace VI

Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of *3GPP TS 38.521-1* specification.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" or "subblock<*n*>/carrier<*k*>/layer<*q*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-spectral-flatness-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number and layer number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0/layer0". Example: "subblock0/carrier0/layer0" "signal::sig1/subblock0/carrier0/layer0" "result::r1/subblock0/carrier0/layer0" "signal::sig1/result::r1/subblock0/carrier0/layer0" You can use the RFmxNR Build Carrier String and RFmxNR Build Layer String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spectral Flatness (dB) — Spectral Flatness returns the spectral flatness. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the spectral flatness values at each allocated subcarrier. Spectral Flatness Lower Mask (dB) — Spectral Flatness Lower Mask returns the lower mask of the spectral flatness. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the lower mask values for the spectral flatness. Spectral Flatness Upper Mask (dB) — Spectral Flatness Upper Mask returns the upper mask of the spectral flatness. x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the upper mask values for the spectral flatness. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the spectral flatness values at each allocated subcarrier. |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the lower mask values for the spectral flatness. |
| x0 — x0 returns the start point of the of the resource block. dx — dx returns the subcarrier spacing. y — y returns an array of the upper mask values for the spectral flatness. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-subcarrier-mean-trace-vi.html language=enus -->
## TOPIC 00149: RFmxNR ModAcc Fetch SSS RMS EVM per Subcarrier Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-subcarrier-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-subcarrier-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean SSS RMS EVM of each subcarrier. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, sub

### RFmxNR ModAcc Fetch SSS RMS EVM per Subcarrier Mean Trace VI

Fetches the mean SSS RMS EVM of each subcarrier.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-sss-rms-evm-per-subcarrier-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. SSS RMS EVM per Subcarrier Mean (% or dB) — SSS RMS EVM per Subcarrier Mean returns the RMS EVM of each subcarrier averaged across all the OFDM symbols allocated with SSS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 — x0 returns the start point of the of the resource grid. dx — dx returns the subcarrier spacing of SSB. y — y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with SSS within the measurement length. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start point of the of the resource grid. dx — dx returns the subcarrier spacing of SSB. y — y returns an array which the EVM of each allocated subcarrier averaged across all the symbols allocated with SSS within the measurement length. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-symbol-mean-trace-vi.html language=enus -->
## TOPIC 00150: RFmxNR ModAcc Fetch SSS RMS EVM per Symbol Mean Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-symbol-mean-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-symbol-mean-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean SSS RMS EVM of each symbol. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, subbloc

### RFmxNR ModAcc Fetch SSS RMS EVM per Symbol Mean Trace VI

Fetches the mean SSS RMS EVM of each symbol.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-sss-rms-evm-per-symbol-mean-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. SSS RMS EVM per Symbol Mean (% or dB) — SSS RMS EVM per Symbol Mean returns the RMS EVM on each OFDM symbol averaged across all the defined subcarriers allocated with SSS within the Meas Length. The unit of this EVM value is specified by the ModAcc EVM Unit property. x0 — x0 returns the start symbol index from the frame start in terms of SSB numerology. dx — dx returns the width in terms of symbols. y — y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with SSS within symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index from the frame start in terms of SSB numerology. dx — dx returns the width in terms of symbols. y — y returns an array which the EVM of each symbol averaged across all the allocated subcarriers allocated with SSS within symbol. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-subblock-in-band-emission-trace-vi.html language=enus -->
## TOPIC 00151: RFmxNR ModAcc Fetch Subblock In-Band Emission Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-subblock-in-band-emission-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-subblock-in-band-emission-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (ge

### RFmxNR ModAcc Fetch Subblock In-Band Emission Trace VI

Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4A.2.2.2 of *3GPP 38.101-1*, and section 6.4A.2.3 of *3GPP 38.101-2*. The trace is not returned when there is clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated, or when the number of carriers is greater than 2.

Use "subblock<*n*>" or "subblock<*n*>/chain<*r*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-subblock-in-band-emission-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number and chain number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/chain0". Example: "subblock0/chain0" "signal::sig1/subblock0/chain0" "result::r1/subblock0/chain0" "signal::sig1/result::r1/subblock0/chain0" You can use the RFmxNR Build Subblock String and RFmxNR Build Chain String VIs to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Subblock In-Band Emission (dB) — Subblock In-Band Emission returns the array of subblock in-band emission measurement trace. Subblock In-Band Emission Mask (dB) — Subblock In-Band Emission Mask returns the array of subblock in-band emission mask trace. Subblock In-Band Emission RB Indices — Subblock In-Band Emission RB Indices returns the array of resource block indices for the subblock in-band emission trace. It can have non integer values depending upon the spacing between carriers. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-transient-period-locations-trace-vi.html language=enus -->
## TOPIC 00152: RFmxNR ModAcc Fetch Transient Period Locations Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-transient-period-locations-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-transient-period-locations-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol indices that were identified to have a transient period. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. The length of the trace is equal to the number of symbols within the measurement length. The trace returns a

### RFmxNR ModAcc Fetch Transient Period Locations Trace VI

Returns the symbol indices that were identified to have a transient period.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

The length of the trace is equal to the number of symbols within the measurement length.

The trace returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0.

The trace is intended to be used as additional context information for the following traces:
 
 RMS EVM per Symbol Mean Trace
 RMS EVM-High per Symbol Mean Trace
 RMS EVM-Low per Symbol Mean Trace

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-transient-period-locations-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Transient Period Locations — Transient Period Locations returns the symbol indices that were identified to have a transient period. x0 — x0 returns the start symbol index from the frame start. dx — dx returns the width in terms of symbols. y — y returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start symbol index from the frame start. dx — dx returns the width in terms of symbols. y — y returns a 1 for the symbol index that was identified to have a transient period; otherwise returns a 0. |

Parent topic:

RFmxNR ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-vi.html language=enus -->
## TOPIC 00153: RFmxNR ModAcc Fetch VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc measurements. icon

### RFmxNR ModAcc Fetch VI

Fetches the ModAcc measurements.

[IMAGE alt='icon' src='rfmxnr-modacc-fetch-vi.png']

- [RFmxNR ModAcc Fetch Composite EVM VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-composite-evm-vi.html) Fetches the composite EVM for ModAcc measurements.
- [RFmxNR ModAcc Fetch Frequency Error Mean VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-mean-vi.html) Fetches the estimated carrier frequency offset averaged over measurement length. This value is expressed in Hz.
- [RFmxNR ModAcc Fetch Frequency Error per Slot Maximum Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-frequency-error-per-slot-maximum-trace-vi.html) Fetches an array of the maximum value across averaging counts of the frequency error per slot for all slots within the measurement length. This value is expressed in Hz.
- [RFmxNR ModAcc Fetch RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the EVM of each allocated subcarrier averaged across all the symbols within the measurement length.
- [RFmxNR ModAcc Fetch Peak EVM per Subcarrier Maximum Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-per-subcarrier-maximum-trace-vi.html) Fetches the peak value of EVM for each allocated subcarrier computed across all the symbols within the measurement length.
- [RFmxNR ModAcc Fetch RMS EVM per Slot Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-slot-mean-trace-vi.html) Fetches the EVM of each slot averaged across all the symbols and all the allocated subcarriers within each slot.
- [RFmxNR ModAcc Fetch Peak EVM per Slot Maximum Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-per-slot-maximum-trace-vi.html) Fetches the peak value of EVM for each slot computed across all the symbols and all the allocated subcarriers.
- [RFmxNR ModAcc Fetch RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-per-symbol-mean-trace-vi.html) Fetches the EVM on each symbol within the measurement length averaged across all the allocated subcarriers.
- [RFmxNR ModAcc Fetch Peak EVM per Symbol Maximum Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-per-symbol-maximum-trace-vi.html) Fetches the peak value of EVM for each symbol computed across all the allocated subcarriers.
- [RFmxNR ModAcc Fetch RMS EVM-High per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-high-per-symbol-mean-trace-vi.html) Fetches the EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C+W/2.
- [RFmxNR ModAcc Fetch Peak EVM-High per Symbol Maximum Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-high-per-symbol-maximum-trace-vi.html) Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C+W/2.
- [RFmxNR ModAcc Fetch RMS EVM-Low per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-rms-evm-low-per-symbol-mean-trace-vi.html) Fetches the EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2.
- [RFmxNR ModAcc Fetch Peak EVM-Low per Symbol Maximum Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-peak-evm-low-per-symbol-maximum-trace-vi.html) Fetches the peak EVM per symbol trace for all confgured slots. The EVM is obtained by using FFT window position Delta_C-W/2.
- [RFmxNR ModAcc Fetch Transient Period Locations Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-transient-period-locations-trace-vi.html) Returns the symbol indices that were identified to have a transient period.
- [RFmxNR ModAcc Fetch Spectral Flatness Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-spectral-flatness-trace-vi.html) Returns the spectral flatness, upper mask, and lower mask traces. Spectral flatness is the magnitude of equalizer coefficients at each allocated subcarrier. Lower and upper masks are derived from section 6.5.2.4.5 of 3GPP TS 38.521-1 specification.
- [RFmxNR ModAcc Fetch Subblock In-Band Emission Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-subblock-in-band-emission-trace-vi.html) Returns the in-band emission trace and limit trace for the the subblocks aggregated bandwidth. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4A.2.2.2 of 3GPP 38.101-1 , and section 6.4A.2.3 of 3GPP 38.101-2 . The trace is not returned when there is clustered PUSCH allocation, or when there is more than one active carrier, or when there is full allocation of resource blocks, or when carriers with different sub-carrier spacing are aggregated, or when the number of carriers is greater than 2.
- [RFmxNR ModAcc Fetch In-Band Emission Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-in-band-emission-trace-vi.html) Fetches the in-band emission trace and limits trace for the component carrier. In-band emission is measured as the ratio of the power in non-allocated resource blocks to the power in the allocated resource blocks averaged over the measurement interval. The IBE for various regions (general, carrier leakage, and I/Q Image) are obtained and concatenated to form a composite trace and the limits are defined in section 6.4.2.3 of 3GPP 38.101-1 , and section 6.4.2.3 of 3GPP 38.101-2 . The trace is not returned when there is full allocation of bandwidth, or there is clustered PUSCH or there is more than one active component carrier.
- [RFmxNR ModAcc Fetch IQ Gain Imbalance per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-iq-gain-imbalance-per-subcarrier-mean-trace-vi.html) Fetches mean value of IQ Gain Imbalance.
- [RFmxNR ModAcc Fetch IQ Quadrature Error per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-iq-quadrature-error-per-subcarrier-mean-trace-vi.html) Fetches the mean value of IQ Quadrature Error.
- [RFmxNR ModAcc Fetch PUSCH Data Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-data-constellation-trace-vi.html) Fetches PUSCH Data Constellation trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PUSCH DMRS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-dmrs-constellation-trace-vi.html) Fetches PUSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PUSCH PTRS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-ptrs-constellation-trace-vi.html) Fetches PUSCH PTRS trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PUSCH Phase Offset Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-phase-offset-trace-vi.html) Returns the phase offset for the slots with respect to the reference slot.
- [RFmxNR ModAcc Fetch PUSCH Demodulated Bits VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pusch-demodulated-bits-vi.html) Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated.
- [RFmxNR ModAcc Fetch PDSCH Data Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-data-constellation-trace-vi.html) Fetches the recovered PDSCH data constellation points. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PDSCH DMRS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-dmrs-constellation-trace-vi.html) Fetches PDSCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PDSCH PTRS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-ptrs-constellation-trace-vi.html) Fetches PDSCH PTRS trace.
- [RFmxNR ModAcc Fetch PDSCH QPSK Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-qpsk-constellation-trace-vi.html) Fetches PDSCH QPSK trace.
- [RFmxNR ModAcc Fetch PDSCH 16QAM Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-16qam-constellation-trace-vi.html) Fetches PDSCH 16 QAM trace.
- [RFmxNR ModAcc Fetch PDSCH 64QAM Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-64qam-constellation-trace-vi.html) Fetches PDSCH 64 QAM trace.
- [RFmxNR ModAcc Fetch PDSCH 256QAM Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-256qam-constellation-trace-vi.html) Fetches PDSCH 256 QAM trace.
- [RFmxNR ModAcc Fetch PDSCH 1024QAM Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-1024qam-constellation-trace-vi.html) Fetches the PDSCH 1024 QAM constellation trace.
- [RFmxNR ModAcc Fetch PDSCH 8PSK Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-8psk-constellation-trace-vi.html) Fetches PDSCH 8 PSK constellation trace.
- [RFmxNR ModAcc Fetch PDSCH Demodulated Bits VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pdsch-demodulated-bits-vi.html) Fetches the recovered bits during EVM calculation. The bits of different slots in the measurement length are concatenated.
- [RFmxNR ModAcc Fetch PSS RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pss-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the mean PSS RMS EVM of each subcarrier.
- [RFmxNR ModAcc Fetch SSS RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the mean SSS RMS EVM of each subcarrier.
- [RFmxNR ModAcc Fetch PBCH Data RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the mean PBCH data RMS EVM of each subcarrier.
- [RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Subcarrier Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-subcarrier-mean-trace-vi.html) Fetches the mean PBCH DMRS RMS EVM for each subcarrier.
- [RFmxNR ModAcc Fetch PSS RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pss-rms-evm-per-symbol-mean-trace-vi.html) Fetches the mean PSS RMS EVM of each symbol.
- [RFmxNR ModAcc Fetch SSS RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-rms-evm-per-symbol-mean-trace-vi.html) Fetches the mean SSS RMS EVM of each symbol.
- [RFmxNR ModAcc Fetch PBCH Data RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-rms-evm-per-symbol-mean-trace-vi.html) Fetches the mean PBCH data RMS EVM for each symbol.
- [RFmxNR ModAcc Fetch PBCH DMRS RMS EVM per Symbol Mean Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-rms-evm-per-symbol-mean-trace-vi.html) Fetches the mean PBCH DMRS RMS EVM for each symbol.
- [RFmxNR ModAcc Fetch PSS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pss-constellation-trace-vi.html) Fetches the PSS constellation trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch SSS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-sss-constellation-trace-vi.html) Fetches the SSS constellation trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PBCH Data Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-data-constellation-trace-vi.html) Fetches the PBCH data trace. The constellation points of different slots in the measurement length is concatenated.
- [RFmxNR ModAcc Fetch PBCH DMRS Constellation Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-modacc-fetch-pbch-dmrs-constellation-trace-vi.html) Fetches the PBCH DMRS trace. The constellation points of different slots in the measurement length is concatenated.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00154: RFmxNR OBW Configure RBW Filter VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-configure-rbw-filter-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the resolution bandwidth (RBW) filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::si

### RFmxNR OBW Configure RBW Filter VI

Configures the resolution bandwidth (RBW) filter.

[IMAGE alt='icon' src='rfmxnr-obw-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. The default value is True. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. RBW (Hz) — RBW specifies the bandwidth of the RBW filter, used to sweep the acquired signal, when you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-measurement-vi.html language=enus -->
## TOPIC 00155: RFmxNR OBW Fetch Measurement VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-measurement-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock. Use "subblock<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the si

### RFmxNR OBW Fetch Measurement VI

Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-obw-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Stop Frequency (Hz) — Stop Frequency returns the stop frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Start Frequency (Hz) — Start Frequency returns the start frequency of the occupied bandwidth of carrier/subblock. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Occupied Bandwidth (Hz) — Occupied Bandwidth returns the bandwidth that occupies the specified percentage of the total power of the signal. This value is expressed in Hz. The occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Absolute Power (dBm) — Absolute Power returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR OBW Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-spectrum-vi.html language=enus -->
## TOPIC 00156: RFmxNR OBW Fetch Spectrum VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-spectrum-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for OBW measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result nam

### RFmxNR OBW Fetch Spectrum VI

Fetches the spectrum used for OBW measurements.

[IMAGE alt='icon' src='rfmxnr-obw-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the spectrum. x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |

Parent topic:

RFmxNR OBW Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-vi.html language=enus -->
## TOPIC 00157: RFmxNR OBW Fetch VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the OBW measurements. icon

### RFmxNR OBW Fetch VI

Fetches the OBW measurements.

[IMAGE alt='icon' src='rfmxnr-obw-fetch-vi.png']

- [RFmxNR OBW Fetch Measurement VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-measurement-vi.html) Returns the occupied bandwidth, absolute power, start frequency, and stop frequency of a component carrier or subblock.
- [RFmxNR OBW Fetch Spectrum VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-obw-fetch-spectrum-vi.html) Fetches the spectrum used for OBW measurements.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-property-node-vi.html language=enus -->
## TOPIC 00158: RFmxNR Property Node VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-property-node-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) RFmxNR properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png error i

### RFmxNR Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) RFmxNR properties.

[IMAGE alt='icon' src='rfmxnr-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx NR Property Node is used to get (read), set (write), or reset (set to default value) RFmx NR properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NR

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-averaging-vi.html language=enus -->
## TOPIC 00159: RFmxNR PVT Configure Averaging VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-averaging-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the PVT measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1"

### RFmxNR PVT Configure Averaging VI

Configures averaging for the PVT measurement.

[IMAGE alt='icon' src='rfmxnr-pvt-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-measurement-method-vi.html language=enus -->
## TOPIC 00160: RFmxNR PVT Configure Measurement Method VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-measurement-method-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-measurement-method-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement method for PVT measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signa

### RFmxNR PVT Configure Measurement Method VI

Configures the measurement method for PVT measurement.

[IMAGE alt='icon' src='rfmxnr-pvt-configure-measurement-method-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Method — Measurement Method specifies the method for performing the PVT measurement. The default value is Normal. Normal (0) The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. Dynamic Range (1) The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644R/5645R/5646R, PXIe-5840/5841/5842/5860. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Normal (0) | The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. |
| Dynamic Range (1) | The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644R/5645R/5646R, PXIe-5840/5841/5842/5860. |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-off-power-exclusion-periods-vi.html language=enus -->
## TOPIC 00161: RFmxNR PVT Configure OFF Power Exclusion Periods VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-off-power-exclusion-periods-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-configure-off-power-exclusion-periods-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the time excluded from the off region before and after the burst. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty st

### RFmxNR PVT Configure OFF Power Exclusion Periods VI

Configures the time excluded from the off region before and after the burst.

[IMAGE alt='icon' src='rfmxnr-pvt-configure-off-power-exclusion-periods-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. OFF Power Exclusion Before (s) — OFF Power Exclusion Before specifies the time excluded from the Off region before the burst. This value is expressed in seconds. The default value is 0. OFF Power Exclusion After (s) — OFF Power Exclusion After specifies the time excluded from the Off region after the burst. This value is expressed in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-measurement-vi.html language=enus -->
## TOPIC 00162: RFmxNR PVT Fetch Measurement VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-measurement-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches PVT ON and OFF powers along with measurement status and burst width. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name,

### RFmxNR PVT Fetch Measurement VI

Fetches PVT ON and OFF powers along with measurement status and burst width.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read from this VI.

[IMAGE alt='icon' src='rfmxnr-pvt-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Burst Width (s) — Burst Width returns the width of the captured burst. This value is expressed in seconds. Absolute ON Power (dBm) — Absolute ON Power returns the power of the subframes within the captured burst. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns the measurement status indicating whether the off power before and after is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. Absolute OFF Power Before (dBm) — Absolute OFF Power Before returns the OFF power in the segment before the captured burst. The segment is defined as one slot prior to a short transient segment and the burst. This value is expressed in dBm. Absolute OFF Power After (dBm) — Absolute OFF Power After returns the OFF power in the segment after the captured burst. The segment is defined as one slot after the burst and a short transient segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |

Parent topic:

RFmxNR PVT Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-signal-power-trace-vi.html language=enus -->
## TOPIC 00163: RFmxNR PVT Fetch Signal Power Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-signal-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-signal-power-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string

### RFmxNR PVT Fetch Signal Power Trace VI

Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='icon' src='rfmxnr-pvt-fetch-signal-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Signal Power (dBm or dBm/MHz) — Signal Power returns an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz. x0 — x0 returns start time of the signal. This value is expressed in seconds. dx — dx returns the time bin spacing. This value is expressed in seconds. y — y returns the instantaneous signal power trace. This value is expressed in dBm. Absolute Limit (dBm or dBm/MHz) — Absolute Limit returns absolute limit for each segment in the trace as specified in section 6.5.2.4.5 of the 3GPP 36.521 specification. This value is expressed in dBm or dBm/MHz. x0 — x0 returns start time of the signal. This value is expressed in seconds. dx — dx returns the time bin spacing. This value is expressed in seconds. y — y returns an array of the absolute limit for each segment in the trace. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns start time of the signal. This value is expressed in seconds. dx — dx returns the time bin spacing. This value is expressed in seconds. y — y returns the instantaneous signal power trace. This value is expressed in dBm. |
| x0 — x0 returns start time of the signal. This value is expressed in seconds. dx — dx returns the time bin spacing. This value is expressed in seconds. y — y returns an array of the absolute limit for each segment in the trace. |

Parent topic:

RFmxNR PVT Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-vi.html language=enus -->
## TOPIC 00164: RFmxNR PVT Fetch VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PVT measurements. icon

### RFmxNR PVT Fetch VI

Fetches the PVT measurements.

[IMAGE alt='icon' src='rfmxnr-pvt-fetch-vi.png']

- [RFmxNR PVT Fetch Measurement VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-measurement-vi.html) Fetches PVT ON and OFF powers along with measurement status and burst width.
- [RFmxNR PVT Fetch Measurement (Array) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-measurement-array-vi.html) Fetches an array of PVT ON and OFF powers along with measurement status and burst width.
- [RFmxNR PVT Fetch Signal Power Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-signal-power-trace-vi.html) Fetches an instantanous signal power trace along with the absolute limit for each segment in the trace. For uplink, the power unit of the returned traces is dBm, while for downlink, the power unit of the returned traces is dBm/MHz.
- [RFmxNR PVT Fetch Windowed Signal Power Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-windowed-signal-power-trace-vi.html) Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-windowed-signal-power-trace-vi.html language=enus -->
## TOPIC 00165: RFmxNR PVT Fetch Windowed Signal Power Trace VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-windowed-signal-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-pvt-fetch-windowed-signal-power-trace-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising

### RFmxNR PVT Fetch Windowed Signal Power Trace VI

Fetches the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='icon' src='rfmxnr-pvt-fetch-windowed-signal-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Windowed Signal Power (dBm/MHz) — Windowed Signal Power returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. x0 — x0 returns start time of the signal. This value is expressed in seconds. dx — dx returns the time bin spacing. This value is expressed in seconds. y — y returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns start time of the signal. This value is expressed in seconds. dx — dx returns the time bin spacing. This value is expressed in seconds. y — y returns the 70/N us windowed power trace in dBm/MHz for Downlink, while an empty trace is returned for Uplink. |

Parent topic:

RFmxNR PVT Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-reset-to-default-vi.html language=enus -->
## TOPIC 00166: RFmxNR Reset to Default VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-reset-to-default-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can

### RFmxNR Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxnr-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00167: RFmxNR Select Measurement (Multiple) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-multiple-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance i

### RFmxNR Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxnr-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurements — Measurements specifies the measurements to perform. You can specify one or more of the following measurements. The default value is an empty array. ModAcc (0) Enables the ModAcc measurement. SEM (1) Enables the SEM measurement. ACP (2) Enables the ACP measurement. CHP (3) Enables the CHP measurement. OBW (4) Enables the OBW measurement. PVT (5) Enables the PVT measurement. TXP (6) Enables the TXP measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the ModAcc measurement. |
| SEM (1) | Enables the SEM measurement. |
| ACP (2) | Enables the ACP measurement. |
| CHP (3) | Enables the CHP measurement. |
| OBW (4) | Enables the OBW measurement. |
| PVT (5) | Enables the PVT measurement. |
| TXP (6) | Enables the TXP measurement. |

Parent topic:

RFmxNR Select Measurement VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-single-vi.html language=enus -->
## TOPIC 00168: RFmxNR Select Measurement (Single) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-single-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the measurement that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxNR Select Measurement (Single) VI

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxnr-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement — Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is ModAcc. ModAcc (0) Enables the ModAcc measurement. SEM (1) Enables the SEM measurement. ACP (2) Enables the ACP measurement. CHP (3) Enables the CHP measurement. OBW (4) Enables the OBW measurement. PVT (5) Enables the PVT measurement. TXP (6) Enables the TXP measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the ModAcc measurement. |
| SEM (1) | Enables the SEM measurement. |
| ACP (2) | Enables the ACP measurement. |
| CHP (3) | Enables the CHP measurement. |
| OBW (4) | Enables the OBW measurement. |
| PVT (5) | Enables the PVT measurement. |
| TXP (6) | Enables the TXP measurement. |

Parent topic:

RFmxNR Select Measurement VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-vi.html language=enus -->
## TOPIC 00169: RFmxNR Select Measurement VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. icon

### RFmxNR Select Measurement VI

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

[IMAGE alt='icon' src='rfmxnr-select-measurement-vi.png']

- [RFmxNR Select Measurement (Single) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxNR Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurement parameter and disables all other measurements.

Parent topic:

NR

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-averaging-vi.html language=enus -->
## TOPIC 00170: RFmxNR SEM Configure Averaging VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-averaging-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1"

### RFmxNR SEM Configure Averaging VI

Configures averaging for the SEM measurement.

[IMAGE alt='icon' src='rfmxnr-sem-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. The number of acquisitions is obtained by the Averaging Count parameter. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations, but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-component-carrier-rated-output-power-vi.html language=enus -->
## TOPIC 00171: RFmxNR SEM Configure Component Carrier Rated Output Power VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-component-carrier-rated-output-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-component-carrier-rated-output-power-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the rated output power (P[rated], x) of the component carrier. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure this VI. This VI is valid when you set the Link Direction property to Downlink, SEM DL Mask Type property to Standard, and gNodeB Category proper

### RFmxNR SEM Configure Component Carrier Rated Output Power VI

Configures the rated output power (P<sub>rated</sub>, x) of the component carrier.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure this VI.

Note

Link Direction

Downlink

SEM DL Mask Type

Standard

gNodeB Category

Medium Range Base Station

3GPP 38.104

[IMAGE alt='icon' src='rfmxnr-sem-configure-component-carrier-rated-output-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, subblock number and carrier number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Component Carrier Rated Output Power (dBm) — Component Carrier Rated Output Power specifies the rated output power (Prated, x), which is used only to choose the limit table for medium range base station, FR2 Category A and FR2 Category B. This value is expressed in dBm. This parameter will be considered when you set the Link Direction property to Downlink, SEM DL Mask Type property to Standard, and gNodeB Category property to Medium Range Base Station or FR2 Category A or FR2 Category B. For more details please refer to section 6.6.4 and section 9.7.4 of 3GPP 38.104 specification. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-number-of-offsets-vi.html language=enus -->
## TOPIC 00172: RFmxNR SEM Configure Number of Offsets VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-number-of-offsets-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-number-of-offsets-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offset segments for the SEM measurement. Use "subblock<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not speci

### RFmxNR SEM Configure Number of Offsets VI

Configures the number of offset segments for the SEM measurement.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-configure-number-of-offsets-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Offsets — Number of Offsets specifies the number of SEM offset segments. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-absolute-limit-array-vi.html language=enus -->
## TOPIC 00173: RFmxNR SEM Configure Offset Absolute Limit (Array) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-absolute-limit-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-absolute-limit-array-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the start limit and the stop limit of the offset segments. Use "subblock<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the subblock number. If you do n

### RFmxNR SEM Configure Offset Absolute Limit (Array) VI

Configures an array of the start limit and the stop limit of the offset segments.

Use "subblock<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxnr-sem-configure-offset-absolute-limit-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the subblock number. If you do not specify the signal name, the default signal instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Absolute Limit Start (dBm) — Absolute Limit Start specifies an array of the absolute power limit corresponding to the beginning of an offset segment. This value is expressed in dBm. The default value is -21. Absolute Limit Stop (dBm) — Absolute Limit Stop specifies an array of the absolute power limit corresponding to the end of an offset segment. This value is expressed in dBm. The default value is -21. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

SEM Array VIs

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-frequency-vi.html language=enus -->
## TOPIC 00174: RFmxNR SEM Configure Offset Frequency VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-frequency-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the start and stop frequencies and the sideband of an offset segment. Use "offset<k>" or "subblock<n>" or "subblock<n>/offset<k>" as the selector string to configure or read this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the

### RFmxNR SEM Configure Offset Frequency VI

Configures the start and stop frequencies and the sideband of an offset segment.

Use "offset<*k*>" or "subblock<*n*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this VI.

[IMAGE alt='icon' src='rfmxnr-sem-configure-offset-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Offset Start Frequency (Hz) — Offset Start Frequency specifies the start frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 0. Offset Stop Frequency (Hz) — Offset Stop Frequency specifies the stop frequency of an offset segment relative to the component carrier bandwidth edge (single carrier) or subblock aggregated channel bandwidth edge (multi-carrier). This value is expressed in Hz. The default value is 1 MHz. Offset Sideband — Offset Sideband specifies whether the offset segment is present either on one side or on both sides of a carrier. The default value is Both. Neg (0) Configures a lower offset segment to the left of the leftmost carrier. Pos (1) Configures an upper offset segment to the right of the rightmost carrier. Both (2) Configures both the negative and the positive offset segments. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Neg (0) | Configures a lower offset segment to the left of the leftmost carrier. |
| Pos (1) | Configures an upper offset segment to the right of the rightmost carrier. |
| Both (2) | Configures both the negative and the positive offset segments. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-limit-fail-mask-vi.html language=enus -->
## TOPIC 00175: RFmxNR SEM Configure Offset Limit Fail Mask VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-limit-fail-mask-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-configure-offset-limit-fail-mask-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status. Use "offset<n>" or "subblock<n>/"offset<n>" as the selector string to configure or read this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector

### RFmxNR SEM Configure Offset Limit Fail Mask VI

Configures the limit fail mask of the offset segments that specify the criteria to determine the measurement fail status.

Use "offset<*n*>" or "subblock<*n*>/"offset<*n*>" as the selector string to configure or read this VI.

[IMAGE alt='icon' src='rfmxnr-sem-configure-offset-limit-fail-mask-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, subblock number, and offset number. If you do not specify the signal name, the default signal instance is used. Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Limit Fail Mask — Limit Fail Mask specifies the criteria to determine the measurement fail status. The default value is Absolute. Abs AND Rel (0) Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks. Abs OR Rel (1) Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask. Absolute (2) Specifies that the measurement fails if the power in the segment exceeds the absolute mask. Relative (3) Specifies that the measurement fails if the power in the segment exceeds the relative mask. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Abs AND Rel (0) | Specifies that the measurement fails if the power in the segment exceeds both the absolute and relative masks. |
| Abs OR Rel (1) | Specifies that the measurement fails if the power in the segment exceeds either the absolute or relative mask. |
| Absolute (2) | Specifies that the measurement fails if the power in the segment exceeds the absolute mask. |
| Relative (3) | Specifies that the measurement fails if the power in the segment exceeds the relative mask. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-component-carrier-measurement-vi.html language=enus -->
## TOPIC 00176: RFmxNR SEM Fetch Component Carrier Measurement VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-component-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-component-carrier-measurement-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the component carriers. Use "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the s

### RFmxNR SEM Fetch Component Carrier Measurement VI

Returns the absolute and relative powers measured in the component carriers.

Use "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-component-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0/carrier0". Example: "subblock0/carrier0" "signal::sig1/subblock0/carrier0" "result::r1/subblock0/carrier0" "signal::sig1/result::r1/subblock0/carrier0" You can use the RFmxNR Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Power (dB) — Relative Power returns the component carrier power relative to its subblock power. This value is expressed in dB. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Absolute Power (dBm) — Absolute Power returns the power measured over the integration bandwidth of the component carrier. This value is expressed in dBm. Peak Absolute Power (dBm) — Peak Absolute Power returns the peak power in the component carrier. This value is expressed in dBm. Peak Frequency (Hz) — Peak Frequency returns the frequency at which peak power occurs in the component carrier. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-power-vi.html language=enus -->
## TOPIC 00177: RFmxNR SEM Fetch Lower Offset Power VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-power-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power. Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read resul

### RFmxNR SEM Fetch Lower Offset Power VI

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-lower-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns the peak power in the lower offset segment relative to total aggregated power. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurs in the lower offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns the lower (negative) offset segment power. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns the power in the lower offset segment relative to total aggregated power. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns the peak power in the lower offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00178: RFmxNR SEM Fetch Measurement Status VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-measurement-status-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the overall measurement status based on the standard mask type that you configure. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is

### RFmxNR SEM Fetch Measurement Status VI

Returns the overall measurement status based on the standard mask type that you configure.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-spectrum-vi.html language=enus -->
## TOPIC 00179: RFmxNR SEM Fetch Spectrum VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-spectrum-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for SEM measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result nam

### RFmxNR SEM Fetch Spectrum VI

Fetches the spectrum used for SEM measurements.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the spectrum. x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. Composite Mask (dBm) — Composite Mask returns the composite mask trace used for the channel. x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of composite mask used for the channel. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of averaged power measured at each frequency bin. This value is expressed in dBm. |
| x0 — x0 returns the start frequency of the channel. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of composite mask used for the channel. This value is expressed in dBm. |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-subblock-measurement-vi.html language=enus -->
## TOPIC 00180: RFmxNR SEM Fetch Subblock Measurement VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-subblock-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-subblock-measurement-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power, integration bandwidth, and center frequency of the subblock. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance

### RFmxNR SEM Fetch Subblock Measurement VI

Fetches the power, integration bandwidth, and center frequency of the subblock.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-subblock-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "subblock0". Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Subblock Power (dBm) — Subblock Power returns the sum of powers of all the frequency bins over the integration bandwidth of the subblock. This includes the power in inter-carrier gaps within a subblock. This value is expressed in dBm. Integration Bandwidth (Hz) — Integration Bandwidth returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within a subblock. This value is expressed in Hz. Frequency (Hz) — Frequency returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-array-vi.html language=enus -->
## TOPIC 00181: RFmxNR SEM Fetch Upper Offset Margin (Array) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-array-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power. Use "subblock<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Sel

### RFmxNR SEM Fetch Upper Offset Margin (Array) VI

Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-upper-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns an array of the power at which the margin occurs in the upper (positive) offset segment. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns an array of the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns an array of the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. Margin (dB) — Margin returns an array of the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. Margin Frequency (Hz) — Margin Frequency returns an array of the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-vi.html language=enus -->
## TOPIC 00182: RFmxNR SEM Fetch Upper Offset Margin VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power. Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read results from this VI. icon Input

### RFmxNR SEM Fetch Upper Offset Margin VI

Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-upper-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power at which the margin occurs in the upper offset segment. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power at which the margin occurs in the upper offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Measurement Status — Measurement Status returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Fail (0) Indicates that the measurement has failed. Pass (1) Indicates that the measurement has passed. Margin (dB) — Margin returns the margin from the absolute limit mask for upper (positive) offset. Margin is defined as the minimum difference between the spectrum and the limit mask. This value is expressed in dB. Margin Frequency (Hz) — Margin Frequency returns the frequency at which the margin occurs in the upper offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | Indicates that the measurement has failed. |
| Pass (1) | Indicates that the measurement has passed. |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-array-vi.html language=enus -->
## TOPIC 00183: RFmxNR SEM Fetch Upper Offset Power (Array) VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-array-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power. Use "subblock<n>" as the selector string to read results from this VI. icon Inputs/

### RFmxNR SEM Fetch Upper Offset Power (Array) VI

Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power.

Use "subblock<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-upper-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and subblock number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0" "signal::sig1/subblock0" "result::r1/subblock0" "signal::sig1/result::r1/subblock0" You can use the RFmxNR Build Subblock String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns an array of the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns an array of the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns an array of the upper segment power. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns an array of the power in the upper offset segment relative to total aggregated power. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns an array of the peak power in the upper offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-vi.html language=enus -->
## TOPIC 00184: RFmxNR SEM Fetch Upper Offset Power VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power. Use "offset<n>" or "subblock<n>/offset<n>" as the selector string to read resul

### RFmxNR SEM Fetch Upper Offset Power VI

Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power.

Use "offset<*n*>" or "subblock<*n*>/offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-upper-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, subblock number, carrier number, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "subblock0/offset0" "signal::sig1/subblock0/offset0" "signal::sig1/result::r1/subblock0/offset0" "result::r1/subblock0/offset0" You can use the RFmxNR Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak Relative Power (dB) — Peak Relative Power returns the peak power in the upper offset segment relative to total aggregated power. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurs in the upper offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Total Absolute Power (dBm) — Total Absolute Power returns the upper (positive) offset segment power. This value is expressed in dBm. Total Relative Power (dB) — Total Relative Power returns the power in the upper offset segment relative to total aggregated power. This value is expressed in dB. Peak Absolute Power (dBm) — Peak Absolute Power returns the peak power in the upper offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR SEM Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-vi.html language=enus -->
## TOPIC 00185: RFmxNR SEM Fetch VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SEM measurements. icon

### RFmxNR SEM Fetch VI

Fetches the SEM measurements.

[IMAGE alt='icon' src='rfmxnr-sem-fetch-vi.png']

- [RFmxNR SEM Fetch Total Aggregated Power VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-total-aggregated-power-vi.html) Returns the sum of powers in all the subblocks.
- [RFmxNR SEM Fetch Measurement Status VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-measurement-status-vi.html) Returns the overall measurement status based on the standard mask type that you configure.
- [RFmxNR SEM Fetch Subblock Measurement VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-subblock-measurement-vi.html) Fetches the power, integration bandwidth, and center frequency of the subblock.
- [RFmxNR SEM Fetch Component Carrier Measurement VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-component-carrier-measurement-vi.html) Returns the absolute and relative powers measured in the component carriers.
- [RFmxNR SEM Fetch Lower Offset Margin VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-margin-vi.html) Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for lower offset segments. The relative power is relative to the total aggregated power.
- [RFmxNR SEM Fetch Lower Offset Power VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-power-vi.html) Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the lower offset segment. The relative power is relative to the total aggregated power.
- [RFmxNR SEM Fetch Upper Offset Margin VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-vi.html) Returns the measurement status, margin, frequency at margin, absolute, and relative powers at the margin for upper offset segments. The relative power is relative to the total aggregated power.
- [RFmxNR SEM Fetch Upper Offset Power VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-vi.html) Returns the total absolute and relative powers, peak, absolute, and relative powers, and the frequency at the peak absolute power of the upper offset segment. The relative power is relative to the total aggregated power.
- [RFmxNR SEM Fetch Component Carrier Measurement (Array) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-component-carrier-measurement-array-vi.html) Returns an array of the absolute and relative powers measured in the component carriers.
- [RFmxNR SEM Fetch Lower Offset Margin (Array) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-margin-array-vi.html) Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for lower offset segments. The relative power is relative to the total aggregated power.
- [RFmxNR SEM Fetch Lower Offset Power (Array) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-lower-offset-power-array-vi.html) Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of lower offset segments. The relative power is relative to total aggregated power.
- [RFmxNR SEM Fetch Upper Offset Margin (Array) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-margin-array-vi.html) Returns an array of measurement status, margin, frequency at margin, absolute, and relative power at margin for upper offset segments. The relative power is relative to the total aggregated power.
- [RFmxNR SEM Fetch Upper Offset Power (Array) VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-upper-offset-power-array-vi.html) Returns an array of total absolute and relative powers, peak, absolute, and relative powers, and frequencies at peak absolute powers of upper offset segments. The relative power is relative to total aggregated power.
- [RFmxNR SEM Fetch Spectrum VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-sem-fetch-spectrum-vi.html) Fetches the spectrum used for SEM measurements.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00186: RFmxNR Send Software Edge Trigger VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-send-software-edge-trigger-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxNR Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure an i

### RFmxNR Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxNR Configure Trigger](/csh?topicname=rfmxnr-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxNR Initiate VI.

[IMAGE alt='icon' src='rfmxnr-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-measurement-vi.html language=enus -->
## TOPIC 00187: RFmxNR TXP Fetch Measurement VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-measurement-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the average power and peak power of the the signal over which power measurments are performed. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the s

### RFmxNR TXP Fetch Measurement VI

Fetches the average power and peak power of the the signal over which power measurments are performed.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

[IMAGE alt='icon' src='rfmxnr-txp-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Average Power Mean (dBm) — Average Power Mean returns the average power of the the signal over which power measurments are performed. This value is expressed in dBm. Peak Power Maximum (dBm) — Peak Power Maximum returns the peak power of the the signal over which power measurments are performed. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxNR TXP Fetch VI

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-vi.html language=enus -->
## TOPIC 00188: RFmxNR TXP Fetch VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the TXP measurements. icon

### RFmxNR TXP Fetch VI

Fetches the TXP measurements.

[IMAGE alt='icon' src='rfmxnr-txp-fetch-vi.png']

- [RFmxNR TXP Fetch Power Trace VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-power-trace-vi.html) Fetches power versus time trace.
- [RFmxNR TXP Fetch Measurement VI](../../../../../vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-txp-fetch-measurement-vi.html) Fetches the average power and peak power of the the signal over which power measurments are performed.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00189: RFmxNR Wait for Measurement Complete VI

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/rfmxnr-wait-for-measurement-complete-vi.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If

### RFmxNR Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxnr-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxNR Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxnr-labview-api-ref path=vi-lib/rfmx/nr/mx/rfmxnr-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00190: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxnr-labview-api-ref`
- source_path: `vi-lib/rfmx/nr/mx/rfmxnr-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxnr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/nr/mx/rfmxnr-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxnr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error

### Using the Standard Functionality for error in Parameters

Many LabVIEW nodes such as VIs contain error in parameters you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard error in behavior is as follows

Note

error in

error in

|  | error in describes error conditions that occur before this node runs. The default is no error. If an error occurred before this node runs, the node passes the error in value to error out. This node runs normally only if no error occurred before this node runs. If an error occurs while this node runs, it runs normally and sets its own error status in error out. Use error in and error out to check errors and to specify execution order by wiring error out from one node to error in of the next node. |
| --- | --- |

The error in cluster contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran. The default is FALSE. |
| --- | --- |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. The default is an empty string. |
