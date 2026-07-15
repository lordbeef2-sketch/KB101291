# NI DOCUMENT BUNDLE: rfmxlte-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxlte-labview-api-ref start=1 end=106 -->
<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=menus/categories/measurement/rfmx/lte/configuration/rfmx-lte-mx-configuration-slotphase-mnu.html language=enus -->
## TOPIC 00001: SlotPhase

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/lte/configuration/rfmx-lte-mx-configuration-slotphase-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/lte/configuration/rfmx-lte-mx-configuration-slotphase-mnu.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure the SlotPhase measurements. You can also use the RFmxLTE Property Node to configure additional properties. icon

### SlotPhase

Use the VIs on this palette to configure the SlotPhase measurements. You can also use the [RFmxLTE Property Node](/csh?context=rfmxlte_rfmxltevi_rfmxlte_property_node) to configure additional properties.

[IMAGE alt='icon' src='rfmx-lte-mx-configuration-slotphase-mnu.png']

- [RFmxLTE SlotPhase Configure Synchronization Mode and Interval VI](../../../../../../vi-lib/rfmx/lte/mx/rfmxlte-llb/rfmxlte-slotphase-configure-synchronization-mode-and-interval-vi.html) Configures the Synchronization Mode , Measurement Offset , and Measurement Length parameters of SlotPhase measurement.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30000b.html language=enus -->
## TOPIC 00002: Trigger:Minimum Quiet Time:Mode

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30000b.html
- document_id: `rfmxlte-labview-api-ref`
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
| High-level VIs | RFmxLTE Configure Trigger |
| Resettable | Yes |

| Manual | 0 | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- | --- |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30000e.html language=enus -->
## TOPIC 00003: Uplink/Downlink Configuration

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30000e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the 3GPP TS 36.211 specification to configure the LTE frame. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to th

### Uplink/Downlink Configuration

Specifies the configuration of the LTE frame structure in the time division duplex (TDD) mode. Refer to table 4.2-2 of the *3GPP TS 36.211* specification to configure the LTE frame.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **0**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | UL/DL Configuration |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Duplex Scheme |
| Resettable | Yes |

| 0 | 0 | The configuration of the LTE frame structure in the TDD duplex mode is 0. |
| --- | --- | --- |
| 1 | 1 | The configuration of the LTE frame structure in the TDD duplex mode is 1. |
| 2 | 2 | The configuration of the LTE frame structure in the TDD duplex mode is 2. |
| 3 | 3 | The configuration of the LTE frame structure in the TDD duplex mode is 3. |
| 4 | 4 | The configuration of the LTE frame structure in the TDD duplex mode is 4. |
| 5 | 5 | The configuration of the LTE frame structure in the TDD duplex mode is 5. |
| 6 | 6 | The configuration of the LTE frame structure in the TDD duplex mode is 6. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300029.html language=enus -->
## TOPIC 00004: Link Direction

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300029.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300029.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the link direction of the received signal. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Uplink. Remarks The fo

### Link Direction

Specifies the link direction of the received signal.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Uplink**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Link Direction |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Frequency, RFmxLTE Configure Link Direction |
| Resettable | Yes |

| Downlink | 0 | The measurement uses 3GPP LTE downlink specification to measure the received signal. |
| --- | --- | --- |
| Uplink | 1 | The measurement uses 3GPP LTE uplink specification to measure the received signal. |
| Sidelink | 2 | The measurement uses 3GPP LTE sidelink specifications to measure the received signal. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300034.html language=enus -->
## TOPIC 00005: Component Carrier:Uplink:SRS:b_hop

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300034.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the SRS hopping bandwidth b[hop]. Frequency hopping for SRS signal is enabled when the value of SRS b_hop property is less than the value of SRS B_SRS property. If the given measurement interval is more than one frame, use the multi-frame generation with digital trigger at the start of the

### Component Carrier:Uplink:SRS:b_hop

Specifies the SRS hopping bandwidth b<sub>hop</sub>. Frequency hopping for SRS signal is enabled when the value of SRS b_hop property is less than the value of [SRS B_SRS](/csh?context=rfmxlte_rfmxlteprop_attr300030) property.

If the given measurement interval is more than one frame, use the multi-frame generation with digital trigger at the start of the first frame for accurate demodulation, since hopping pattern will vary across frames.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 3. Valid values are from 0 to 3, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SRS b_hop |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300036.html language=enus -->
## TOPIC 00006: Component Carrier:Uplink:SRS:Maximum UpPTS Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300036.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300036.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of 3GPP 36.211 specification for more details. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property

### Component Carrier:Uplink:SRS:Maximum UpPTS Enabled

Specifies SRS MaxUpPTS parameter which determines whether SRS is transmitted in all possible RBs of UpPTS symbols in LTE TDD. Refer to section 5.5.3.2 of *3GPP 36.211* specification for more details.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SRS MaxUpPTS Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | In special subframe, SRS is transmitted in RBs specified by SRS bandwidth configurations. |
| --- | --- | --- |
| True | 1 | In special subframe, SRS is transmitted in all possible RBs. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300037.html language=enus -->
## TOPIC 00007: Component Carrier:Uplink:SRS:Subframe1 N_RA

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300037.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300037.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Valid values are 0 to 6. Remarks The following table lists t

### Component Carrier:Uplink:SRS:Subframe1 N_RA

Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 1, first special subframe, in LTE TDD.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 6.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SRS Subframe1 N_RA |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300038.html language=enus -->
## TOPIC 00008: Component Carrier:Uplink:SRS:Subframe6 N_RA

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300038.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300038.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Valid va

### Component Carrier:Uplink:SRS:Subframe6 N_RA

Specifies the number of format 4 PRACH allocations in UpPTS for Subframe 6, second special subframe, in LTE TDD. It is ignored for UL/DL Configuration 3, 4, and 5.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 6.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SRS Subframe6 N_RA |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300039.html language=enus -->
## TOPIC 00009: Component Carrier:Uplink:SRS:Power (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300039.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300039.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Remarks The following table lists the characteristics of th

### Component Carrier:Uplink:SRS:Power (dB)

Specifies the average power of SRS transmission with respect to PUSCH DMRS power. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SRS Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30003c.html language=enus -->
## TOPIC 00010: Component Carrier:Downlink: Auto Cell ID Detection Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30003c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30003c.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using ModAcc Results DL Detected Cell ID property. You do not need to use a s

### Component Carrier:Downlink: Auto Cell ID Detection Enabled

Specifies whether to enable autodetection of the cell ID. If the signal being measured does not contain primary and secondary sync signal (PSS/SSS), autodetection of cell ID is not possible. Detected cell ID can be fetched using [ModAcc Results DL Detected Cell ID](/csh?topicname=attr304053.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DL Auto Cell ID Detection Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Downlink Auto Cell ID Detection Enabled |
| Resettable | Yes |

| False | 0 | The measurement uses the cell ID you configure. |
| --- | --- | --- |
| True | 1 | The measurement auto detects the cell ID. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30003d.html language=enus -->
## TOPIC 00011: Component Carrier:Downlink:Channel Configuration Mode

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30003d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30003d.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel configuration mode. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Test Model. Remarks The following

### Component Carrier:Downlink:Channel Configuration Mode

Specifies the channel configuration mode.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Test Model**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DL Ch Configuration Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Downlink Channel Configuration Mode |
| Resettable | Yes |

| User Defined | 1 | You have to manually set all the signals and channels. |
| --- | --- | --- |
| Test Model | 2 | You need to select a test model using the DL Test Model property, which will configure all the signals and channels automatically according to the 3GPP specification. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300040.html language=enus -->
## TOPIC 00012: Component Carrier:Downlink:User Defined:SSS Power (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300040.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300040.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Remarks The following

### Component Carrier:Downlink:User Defined:SSS Power (dB)

Specifies the power of secondary synchronization signal (SSS) relative to the power of cell-specific reference signal. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SSS Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Downlink Synchronization Signal |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300041.html language=enus -->
## TOPIC 00013: Component Carrier:Downlink:User Defined:PBCH Power (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300041.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Remarks The following table

### Component Carrier:Downlink:User Defined:PBCH Power (dB)

Specifies the power of physical broadcast channel (PBCH) relative to the power of cell-specific reference signal. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PBCH Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Downlink PBCH |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300045.html language=enus -->
## TOPIC 00014: Component Carrier:Downlink:User Defined:PCFICH:Power (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300045.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB. Use "subframe<l>" or "carrier<k>" or "subblock<n>" or "subblock<n>/carrier<k>/subframe<l>" as the selector string to configure or read thi

### Component Carrier:Downlink:User Defined:PCFICH:Power (dB)

Specifies the power of physical control format indicator channel (PCFICH) relative to the power of cell-specific reference signal. This value is expressed in dB.

Use "subframe<*l*>" or "carrier<*k*>" or "subblock<*n*>" or "subblock<*n*>/carrier<*k*>/subframe<*l*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PCFICH Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure PCFICH |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30004d.html language=enus -->
## TOPIC 00015: Component Carrier:Downlink:Test Model

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30004d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30004d.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the E-UTRA test model type when you set the DL Ch Configuration Mode property to Test Model. Refer to section 6.1.1 of the 3GPP 36.141 specification for more information regarding test model configurations. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or

### Component Carrier:Downlink:Test Model

Specifies the E-UTRA test model type when you set the [DL Ch Configuration Mode](/csh?context=rfmxlte_rfmxlteprop_attr30003d) property to **Test Model**. Refer to section 6.1.1 of the *3GPP 36.141* specification for more information regarding test model configurations.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **TM1.1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DL Test Model |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure Downlink Test Model, RFmxLTE Configure Downlink Test Model (Array) |
| Resettable | Yes |

| TM1.1 | 0 | Specifies an E-UTRA Test Model 1.1. |
| --- | --- | --- |
| TM1.2 | 1 | Specifies an E-UTRA Test Model 1.2. |
| TM2 | 2 | Specifies an E-UTRA Test Model 2. |
| TM2a | 3 | Specifies an E-UTRA Test Model 2a. |
| TM2b | 8 | Specifies an E-UTRA Test Model 2b. |
| TM3.1 | 4 | Specifies an E-UTRA Test Model 3.1. |
| TM3.1a | 7 | Specifies an E-UTRA Test Model 3.1a. |
| TM3.1b | 9 | Specifies an E-UTRA Test Model 3.1b. |
| TM3.2 | 5 | Specifies an E-UTRA Test Model 3.2. |
| TM3.3 | 6 | Specifies an E-UTRA Test Model 3.3. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300050.html language=enus -->
## TOPIC 00016: eNodeB Category

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300050.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300050.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the downlink eNodeB (Base station) category. Refer to the 3GPP 36.141 specification for more details. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for

### eNodeB Category

Specifies the downlink eNodeB (Base station) category. Refer to the *3GPP 36.141* specification for more details.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Wide Area Base Station - Category A**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | eNodeB Category |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Configure eNodeB Category |
| Resettable | Yes |

| Wide Area Base Station - Category A | 0 | Specifies eNodeB is Wide Area Base Station - Category A. |
| --- | --- | --- |
| Wide Area Base Station - Category B Option 1 | 1 | Specifies eNodeB is Wide Area Base Station - Category B Option1. |
| Wide Area Base Station - Category B Option 2 | 2 | Specifies eNodeB is Wide Area Base Station - Category B Option2. |
| Local Area Base Station | 3 | Specifies eNodeB is Local Area Base Station. |
| Home Base Station | 4 | Specifies eNodeB is Home Base Station. |
| Medium Range Base Station | 5 | Specifies eNodeB is Medium Range Base Station. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300051.html language=enus -->
## TOPIC 00017: Component Carrier:Uplink:PUSCH:DMRS OCC Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300051.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300051.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this property to TRUE for multi antenna cases. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. T

### Component Carrier:Uplink:PUSCH:DMRS OCC Enabled

Specifies whether orthogonal cover codes (OCCs) need to be used on the demodulation reference signal (DMRS) signal. The measurement internally sets this property to **TRUE** for multi antenna cases.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DMRS OCC Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement ignores the Cyclic Shift Field and uses the PUSCH n_DMRS_2 field for DMRS calculations. |
| --- | --- | --- |
| True | 1 | The measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the value of PUSCH n_DMRS_2 and [w(0) w(1)] for DMRS signal based on the values you set for the Cyclic Shift Field and Tx Antenna to Analyze. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300052.html language=enus -->
## TOPIC 00018: Component Carrier:Uplink:PUSCH:Cyclic Shift Field

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300052.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300052.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the cyclic shift field in uplink-related DCI format. When the DMRS OCC enabled property is set to True, the measurement uses the table 5.5.2.1.1-1 of 3GPP 36.211 specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with Tx Antenna

### Component Carrier:Uplink:PUSCH:Cyclic Shift Field

Specifies the cyclic shift field in uplink-related DCI format. When the [DMRS OCC enabled](/csh?topicname=attr300051.html) property is set to **True**,
 the measurement uses the table 5.5.2.1.1-1 of *3GPP 36.211* specification to decide the valued of n(2)DMRS and [w(0) w(1)] for DMRS signal based on Cyclic Shift Field along with [Tx Antenna to Analyze](/csh?topicname=attr30002c.html).

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 7, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Cyclic Shift Field |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300055.html language=enus -->
## TOPIC 00019: Component Carrier:Sidelink:PSSCH:Modulation Type

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300055.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300055.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is QPSK. Remarks The following table lists the characteristics of t

### Component Carrier:Sidelink:PSSCH:Modulation Type

Specifies the modulation scheme used in physical sidelink shared channel (PSSCH) of the signal being measured.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **QPSK**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PSSCH Mod Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| QPSK | 0 | Specifies a QPSK modulation scheme. |
| --- | --- | --- |
| 16 QAM | 1 | Specifies a 16-QAM modulation scheme. |
| 64 QAM | 2 | Specifies a 64-QAM modulation scheme. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr300056.html language=enus -->
## TOPIC 00020: Component Carrier:Sidelink:PSSCH:Resource Block Offset

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr300056.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr300056.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting resource block number of a physical sidelink shared channel (PSSCH) allocation. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Remarks The following table lists the characteristics of this propert

### Component Carrier:Sidelink:PSSCH:Resource Block Offset

Specifies the starting resource block number of a physical sidelink shared channel (PSSCH) allocation.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PSSCH RB Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr301040.html language=enus -->
## TOPIC 00021: ACP:Amplitude Correction Type

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr301040.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr301040.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. You do not need t

### ACP:Amplitude Correction Type

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_configure_external_attenuation_table) VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Amplitude Correction Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| RF Center Frequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| --- | --- | --- |
| Spectrum Frequency Bin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr301041.html language=enus -->
## TOPIC 00022: ACP:Advanced:Sequential FFT Size

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr301041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr301041.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT size, when you set the ACP Meas Method property to Sequential FFT. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default

### ACP:Advanced:Sequential FFT Size

Specifies the FFT size, when you set the [ACP Meas Method](/csh?topicname=attr301012.html) property to **Sequential FFT**.

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

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr301042.html language=enus -->
## TOPIC 00023: ACP:Offset:Number of GSM Offsets

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr301042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr301042.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of GSM adjacent channel offsets to be configured when you set the CC Bandwidth to 200.0 k and the ACP Configurable Number of Offset Enabled property to True. The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GP

### ACP:Offset:Number of GSM Offsets

Specifies the number of GSM adjacent channel offsets to be configured when you set the [CC Bandwidth](/csh?topicname=attr300010.html) to **200.0 k** and the [ACP Configurable Number of Offset Enabled](/csh?topicname=attr301044.html) property to **True**.

The frequency offset from the center of NB-IOT carrier to the center of the first offset is 300 kHz as defined in the 3GPP specification. The center of every other offset is placed at 200 kHz from the previous offset's center.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 1, when you set the CC Bandwidth property to is **200.0 k** and Link Direction to **Uplink**. The default value is 0, otherwise.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Num GSM Offsets |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30104b.html language=enus -->
## TOPIC 00024: ACP:Noise Calibration:Mode

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30104b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30104b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this property for

### ACP:Noise Calibration:Mode

Specifies whether the noise calibration and measurement is performed automatically by the measurement or by you. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?context=rfmxspecan_rfmxspecan_noise_compensation_algorithm) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Noise Cal Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Manual | 0 | When you set the ACP Meas Mode property to Calibrate Noise Floor, you can initiate instrument noise calibration for ACP measurement manually. When you set the ACP Meas Mode property to Measure, you can initiate the ACP measurement manually. |
| --- | --- | --- |
| Auto | 1 | When you set the ACP Noise Comp Enabled property to True, RFmx sets the Input Isolation Enabled property to Enabled and calibrates the instrument noise in the current state of the instrument. RFmx then resets Input Isolation Enabled property and performs the ACP measurement including compensation for the noise contribution of the instrument. RFmx skips noise calibration in this mode if valid noise calibration data is already cached. When you set ACP Noise Comp Enabled to False, RFmx does not calibrate instrument noise and performs the ACP measurement without compensating for the noise contribution of the instrument. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303000.html language=enus -->
## TOPIC 00025: CHP:Measurement Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303000.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the channel power measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks T

### CHP:Measurement Enabled

Specifies whether to enable the channel power measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303002.html language=enus -->
## TOPIC 00026: CHP:Component Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303002.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the integration bandwidth of a component carrier. This value is expressed in Hz. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. The default value is 9 MHz. Remarks The following table lists the characteristics of this property. Short Name CHP CC IB

### CHP:Component Carrier:Integration Bandwidth (Hz)

Specifies the integration bandwidth of a component carrier. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

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

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303003.html language=enus -->
## TOPIC 00027: CHP:Number of Analysis Threads

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303003.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the CHP measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources

### CHP:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the CHP measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303006.html language=enus -->
## TOPIC 00028: CHP:Averaging:Count

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303006.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### CHP:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](/csh?topicname=attr303007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE CHP Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303007.html language=enus -->
## TOPIC 00029: CHP:Averaging:Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303007.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the CHP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remar

### CHP:Averaging:Enabled

Specifies whether to enable averaging for the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE CHP Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The CHP measurement uses the value of the CHP Averaging Count property as the number of acquisitions over which the CHP measurement is averaged. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303019.html language=enus -->
## TOPIC 00030: CHP:Results:Total Aggregated Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303019.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include

### CHP:Results:Total Aggregated Power (dBm)

Returns the total power of all the subblocks. This value is expressed in dBm. The power in each subblock is the sum of powers of all the frequency bins over the integration bandwidth of the subblocks. This value includes the power in the inter-carrier gaps within a subblock, but it does not include the power within the subblock gaps.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Results Total Aggregated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE CHP Fetch, RFmxLTE CHP Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30301b.html language=enus -->
## TOPIC 00031: CHP:Results:Subblock Frequency (Hz)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30301b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30301b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock

### CHP:Results:Subblock Frequency (Hz)

Returns the absolute center frequency of the subblock. This value is the center of the subblock integration bandwidth. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Results Subblock Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE CHP Fetch, RFmxLTE CHP Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30301c.html language=enus -->
## TOPIC 00032: CHP:Results:Subblock Integration Bandwidth (Hz)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30301c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30301c.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz. Use "subblock<n>" as the selector string to read th

### CHP:Results:Subblock Integration Bandwidth (Hz)

Returns the integration bandwidth used in calculating the power of the subblock. Integration bandwidth is the span from left edge of the leftmost carrier to the right edge of the rightmost carrier within the subblock. This value is expressed in Hz.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Results Subblock IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303026.html language=enus -->
## TOPIC 00033: CHP:Noise Compensation:Type

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303026.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the noise compensation type. Refer to the measurement guidelines section in the Noise Compensation Algorithm topic for more information. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for info

### CHP:Noise Compensation:Type

Specifies the noise compensation type. Refer to the measurement guidelines section in the [Noise Compensation Algorithm](/csh?context=rfmxspecan_rfmxspecan_noise_compensation_algorithm) topic for more information.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Analyzer and Termination**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Noise Comp Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Analyzer and Termination | 0 | Compensates for noise from the analyzer and the 50 ohm termination. The measured power values are in excess of the thermal noise floor. |
| --- | --- | --- |
| Analyzer Only | 1 | Compensates only for analyzer noise. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr303027.html language=enus -->
## TOPIC 00034: CHP:Noise Calibration:Averaging:Count

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr303027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr303027.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging count used for noise calibration when you set the CHP Noise Cal Averaging Auto property to False. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string

### CHP:Noise Calibration:Averaging:Count

Specifies the averaging count used for noise calibration when you set the [CHP Noise Cal Averaging Auto](/csh?topicname=attr303028.html) property to **False**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 32.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Noise Cal Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304014.html language=enus -->
## TOPIC 00035: ModAcc:Results:Peak Composite EVM Symbol Index

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304014.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol index of the ModAcc Results Max Pk Composite EVM property. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Pk Composite EVM Symbol Index Data

### ModAcc:Results:Peak Composite EVM Symbol Index

Returns the symbol index of the [ModAcc Results Max Pk Composite EVM](/csh?topicname=attr304010.html) property.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk Composite EVM Symbol Index |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304018.html language=enus -->
## TOPIC 00036: ModAcc:Results:Uplink:PUSCH:Mean RMS DMRS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304018.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of the RMS EVMs calculated on the PUSCH DMRS over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurem

### ModAcc:Results:Uplink:PUSCH:Mean RMS DMRS EVM (% or dB)

Returns the mean value of the RMS EVMs calculated on the PUSCH DMRS over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PUSCH Mean RMS DMRS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304019.html language=enus -->
## TOPIC 00037: ModAcc:Results:Uplink:PUSCH:Maximum Peak DMRS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304019.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak EVMs calculated on PUSCH DMRS over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurem

### ModAcc:Results:Uplink:PUSCH:Maximum Peak DMRS EVM (% or dB)

Returns the maximum value of the peak EVMs calculated on PUSCH DMRS over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PUSCH Max Pk DMRS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304022.html language=enus -->
## TOPIC 00038: ModAcc:Results:Mean Frequency Error (Hz)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304022.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304022.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated carrier frequency offset averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in Hz. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of this p

### ModAcc:Results:Mean Frequency Error (Hz)

Returns the estimated carrier frequency offset averaged over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304023.html language=enus -->
## TOPIC 00039: ModAcc:Results:Mean IQ Origin Offset (dBc)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304023.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated I/Q origin offset averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in dBc. This result is valid only when you set the Link Direction property to Uplink or Sidelink or NB-IoT Downlink. Use "carrier<k>" or "subblock<n>/carrier<k>" as t

### ModAcc:Results:Mean IQ Origin Offset (dBc)

Returns the estimated I/Q origin offset averaged over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in dBc.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink** or **Sidelink** or **NB-IoT Downlink**.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean IQ Origin Offset (dBc) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304027.html language=enus -->
## TOPIC 00040: ModAcc:Results:Mean Time Offset (s)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304027.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of ModAcc Sync Mode property. This value is expressed in seconds. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The fol

### ModAcc:Results:Mean Time Offset (s)

Returns the time difference between the detected slot or frame boundary and the reference trigger location depending on the value of [ModAcc Sync Mode](/csh?topicname=attr304003.html) property. This value is expressed in seconds.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean Time Offset (s) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304028.html language=enus -->
## TOPIC 00041: ModAcc:Results:Mean Symbol Clock Error (ppm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304028.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304028.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated symbol clock error averaged over the slots specified by the ModAcc Meas Length property. This value is expressed in ppm. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of this proper

### ModAcc:Results:Mean Symbol Clock Error (ppm)

Returns the estimated symbol clock error averaged over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in ppm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean Symbol Clock Error (ppm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30402b.html language=enus -->
## TOPIC 00042: ModAcc:Results:In-Band Emission Margin (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30402b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30402b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the in-band emission margin. This value is expressed in dB. The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2.3.5 of the 3GPP TS 36.521 specification. The in-band emissions are a measure of the interf

### ModAcc:Results:In-Band Emission Margin (dB)

Returns the in-band emission margin. This value is expressed in dB.

The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2.3.5 of the *3GPP TS 36.521* specification.

The in-band emissions are a measure of the interference falling into the non-allocated resources blocks.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results In-Band Emission Margin (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30402e.html language=enus -->
## TOPIC 00043: ModAcc:Results:Spectral Flatness:Range1-Max to Range2-Min (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30402e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30402e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak-to-peak ripple of the EVM equalizer coefficients from the frequency Range1 to the frequency Measurement Offset parameter. The frequency Range1 and frequency Measurement Offset parameter are defined in the section 6.5.2.4.5 of the 3GPP TS 36.521 specification. This value is expressed

### ModAcc:Results:Spectral Flatness:Range1-Max to Range2-Min (dB)

Returns the peak-to-peak ripple of the EVM equalizer coefficients from the frequency *Range1* to the frequency *Measurement Offset* parameter. The frequency *Range1* and frequency *Measurement Offset* parameter are defined in the section 6.5.2.4.5 of the *3GPP TS 36.521* specification. This value is expressed in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Spectral Flatness Range1-Max to Range2-Min (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30403b.html language=enus -->
## TOPIC 00044: ModAcc:Results:Maximum Peak Composite Magnitude Error (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30403b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30403b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak value of the composite magnitude error calculated over the slots specified by the ModAcc Meas Length property on all the configured channels. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Uni

### ModAcc:Results:Maximum Peak Composite Magnitude Error (% or dB)

Returns the peak value of the composite magnitude error calculated over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property on all the configured channels.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink**.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Max Pk Composite Magnitude Error |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30403e.html language=enus -->
## TOPIC 00045: ModAcc:Results:Uplink:Subblock In-Band Emission Margin (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30403e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30403e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB. The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2A.3 of the 3GPP TS 36.521 specification. The in-band emi

### ModAcc:Results:Uplink:Subblock In-Band Emission Margin (dB)

Returns the in-band emission margin of a subblock aggregated bandwidth. This value is expressed in dB.

The margin is the lowest difference between the in-band emission measurement trace and the limit trace. The limit is defined in section 6.5.2A.3 of the *3GPP TS 36.521* specification.

The in-band emissions are a measure of the interference falling into the non-allocated resources blocks. The result of this property is valid only when you set the [Transmitter Architecture](/csh?context=rfmxlte_rfmxlteprop_attr30d002) property to **LO per Subblock**.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Subblock In-Band Emission Margin (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30403f.html language=enus -->
## TOPIC 00046: ModAcc:Results:Subblock Mean IQ Origin Offset (dBc)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30403f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30403f.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated I/Q origin offset averaged over the slots specified by the ModAcc Meas Length property in the subblock. This value is expressed in dBc. This result is valid only when you set the Link Direction property to Uplink and the Transmitter Architecture property to LO per Subblock. Use

### ModAcc:Results:Subblock Mean IQ Origin Offset (dBc)

Returns the estimated I/Q origin offset averaged over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property in the subblock. This value is expressed in dBc.

This result is valid only when you set the [Link Direction](attr300029.html) property to **Uplink** and the [Transmitter Architecture](attr30d002.html) property to **LO per Subblock**.

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Subblock Mean IQ Origin Offset (dBc) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304043.html language=enus -->
## TOPIC 00047: ModAcc:Results:Uplink:SRS:Mean Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304043.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304043.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of power calculated on SRS over the slots specified by the ModAcc Meas Length property. This values is expressed in dBm. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of this prope

### ModAcc:Results:Uplink:SRS:Mean Power (dBm)

Returns the mean value of power calculated on SRS over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This values is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean SRS Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304044.html language=enus -->
## TOPIC 00048: ModAcc:Results:Downlink:PDSCH:Mean RMS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304044.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304044.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurem

### ModAcc:Results:Downlink:PDSCH:Mean RMS EVM (% or dB)

Returns the mean value of RMS EVMs calculated on PDSCH data symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PDSCH Mean RMS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304045.html language=enus -->
## TOPIC 00049: ModAcc:Results:Downlink:PDSCH:Mean RMS QPSK EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304045.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit proper

### ModAcc:Results:Downlink:PDSCH:Mean RMS QPSK EVM (% or dB)

Returns the mean value of RMS EVMs calculated on all QPSK modulated PDSCH resource blocks over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PDSCH Mean RMS QPSK EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304046.html language=enus -->
## TOPIC 00050: ModAcc:Results:Downlink:PDSCH:Mean RMS 16QAM EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304046.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304046.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit prope

### ModAcc:Results:Downlink:PDSCH:Mean RMS 16QAM EVM (% or dB)

Returns the mean value of RMS EVMs calculated on all 16QAM modulated PDSCH resource blocks over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PDSCH Mean RMS 16QAM EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304048.html language=enus -->
## TOPIC 00051: ModAcc:Results:Downlink:PDSCH:Mean RMS 256QAM EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304048.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304048.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit pro

### ModAcc:Results:Downlink:PDSCH:Mean RMS 256QAM EVM (% or dB)

Returns the mean value of RMS EVMs calculated on all 256 QAM modulated PDSCH resource blocks over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PDSCH Mean RMS 256QAM EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304049.html language=enus -->
## TOPIC 00052: ModAcc:Results:Downlink:Mean RMS CSRS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304049.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304049.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measur

### ModAcc:Results:Downlink:Mean RMS CSRS EVM (% or dB)

Returns the mean value of RMS EVMs calculated on RS resource elements over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean RMS CSRS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30404a.html language=enus -->
## TOPIC 00053: ModAcc:Results:Downlink:Mean RMS PSS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30404a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30404a.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit pr

### ModAcc:Results:Downlink:Mean RMS PSS EVM (% or dB)

Returns the mean value of RMS EVMs calculated on primary synchronization signal (PSS) channel over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean RMS PSS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30404c.html language=enus -->
## TOPIC 00054: ModAcc:Results:Downlink:Mean RMS PBCH EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30404c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30404c.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on PBCH channel over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement re

### ModAcc:Results:Downlink:Mean RMS PBCH EVM (% or dB)

Returns the mean value of RMS EVMs calculated on PBCH channel over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean RMS PBCH EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30404d.html language=enus -->
## TOPIC 00055: ModAcc:Results:Downlink:Mean RMS PCFICH EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30404d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30404d.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the measurement

### ModAcc:Results:Downlink:Mean RMS PCFICH EVM (% or dB)

Returns the mean value of RMS EVMs calculated on PCFICH channel over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean RMS PCFICH EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304052.html language=enus -->
## TOPIC 00056: ModAcc:Results:Downlink:OFDM Symbol Tx Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304052.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304052.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of power calculated in one OFDM symbol over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of

### ModAcc:Results:Downlink:OFDM Symbol Tx Power (dBm)

Returns the mean value of power calculated in one OFDM symbol over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results DL OFDM Symbol Tx Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304053.html language=enus -->
## TOPIC 00057: ModAcc:Results:Downlink:Detected Cell ID

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304053.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304053.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the detected cell ID value. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results DL Detected Cell ID Data type ci32.png Permissions Read Only High-level VIs R

### ModAcc:Results:Downlink:Detected Cell ID

Returns the detected cell ID value.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results DL Detected Cell ID |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304054.html language=enus -->
## TOPIC 00058: Component Carrier:Downlink:Auto PDSCH Channel Detection Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304054.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304054.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the values of the PDSCH RB Allocation property, the corresponding PDSCH CW0 Modulation Type property, and the PDSCH Power property are auto-detected by the measurement or user-specified. This property is not valid, when you set the DL Ch Configuration Mode property to Test Model. T

### Component Carrier:Downlink:Auto PDSCH Channel Detection Enabled

Specifies whether the values of the [PDSCH RB Allocation](/csh?topicname=attr30004b.html) property, the corresponding [PDSCH CW0 Modulation Type](/csh?topicname=attr30004a.html) property, and the [PDSCH Power](/csh?topicname=attr30004c.html) property are auto-detected by the measurement or user-specified. This property is not valid, when you set the [DL Ch Configuration Mode](/csh?topicname=attr30003d.html) property to **Test Model**. The measurement ignores this property, when you set the [Link Direction](/csh?topicname=attr300029.html)
 property to **Uplink**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto PDSCH Channel Detection Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement uses the values of the PDSCH RB Allocation property, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power property that you specify. |
| --- | --- | --- |
| True | 1 | The measurement uses the values of the PDSCH RB Allocation property, the corresponding values of PDSCH CW0 Modulation Type, and the PDSCH Power property that are auto-detected. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304055.html language=enus -->
## TOPIC 00059: Component Carrier:Downlink:Auto Control Channel Power Detection Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304055.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304055.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the value of PSS Power, SSS Power, PBCH Power, PDCCH Power, and PCFICH Power properties are auto-detected by the measurement or user-specified. Currently, auto-detection of PHICH Power property is not supported. This property is not valid, when you set the DL Ch Configuration Mode

### Component Carrier:Downlink:Auto Control Channel Power Detection Enabled

Specifies whether the value of [PSS Power](/csh?topicname=attr30003f.html), [SSS Power](/csh?topicname=attr300040.html), [PBCH Power](/csh?topicname=attr300041.html), [PDCCH Power](/csh?topicname=attr300042.html), and [PCFICH Power](/csh?topicname=attr300045.html) properties are auto-detected by the measurement or user-specified. Currently, auto-detection of [PHICH Power](/csh?topicname=attr300048.html) property is not supported. This property is not valid, when you set the [DL Ch Configuration Mode](/csh?topicname=attr30003d.html) property to **Test Model**. The measurement ignores this property, when you set the [Link Direction](/csh?topicname=attr300029.html)
 property to **Uplink**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Control Channel Pwr Detection Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, PHICH Power, and PCFICH Power properties that you specify are used for the measurement. |
| --- | --- | --- |
| True | 1 | The value of the PSS Power, SSS Power, PDCCH Power, PBCH Power, and PCFICH Power properties are auto-detected and used for the measurement. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304059.html language=enus -->
## TOPIC 00060: Component Carrier:LAA:Uplink Start Position

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304059.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304059.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the 3GPP 36.211 specification for more information regarding LAA uplink start position. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this prop

### Component Carrier:LAA:Uplink Start Position

Specifies the starting position of symbol 0 in the first subframe of an LAA uplink burst. Refer to section 5.6 of the *3GPP 36.211* specification for more information regarding LAA uplink start position.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **00**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LAA UL Start Position |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 00 | 0 | The symbol 0 in the first subframe of an LAA uplink burst is completely occupied. There is no idle duration. |
| --- | --- | --- |
| 01 | 1 | The starting position of symbol 0 in the first subframe of an LAA uplink burst is calculated as per section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |
| 10 | 2 | The starting position of symbol 0 in the first subframe of an LAA uplink burst is calculated as per section 5.6 (frame structure type 3) of the 3GPP 36.211 specification. The symbol is partially occupied. |
| 11 | 3 | The symbol 0 in the first subframe of an LAA uplink burst is completely idle. Symbol 0 is not transmitted in this case. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30405a.html language=enus -->
## TOPIC 00061: Component Carrier:LAA:Uplink Ending Symbol

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30405a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30405a.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the 3GPP 36.212 specification for more information regarding LAA uplink ending symbol. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property

### Component Carrier:LAA:Uplink Ending Symbol

Specifies the ending symbol number in the last subframe of an LAA uplink burst. Refer to section 5.3.3.1.1A of the *3GPP 36.212* specification for more information regarding LAA uplink ending symbol.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **13**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LAA UL Ending Symbol |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 12 | 12 | The last subframe of an LAA uplink burst ends at symbol 12. |
| --- | --- | --- |
| 13 | 13 | The last subframe of an LAA uplink burst ends at symbol 13. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30405e.html language=enus -->
## TOPIC 00062: Component Carrier:NB-IoT:NCell ID

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30405e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30405e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the narrowband physical layer cell identity. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 0. Valid values are 0 to 503, inclusive. Remarks The following table lists the characteristics of this property. Short N

### Component Carrier:NB-IoT:NCell ID

Specifies the narrowband physical layer cell identity.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 503, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NCell ID |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30405f.html language=enus -->
## TOPIC 00063: Component Carrier:NB-IoT:Uplink Subcarrier Spacing

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30405f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30405f.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the subcarrier bandwidth of an NB-IoT signal. This property specifies the spacing between adjacent subcarriers. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is 15 kHz. Remarks The following table lists the charact

### Component Carrier:NB-IoT:Uplink Subcarrier Spacing

Specifies the subcarrier bandwidth of an NB-IoT signal. This property specifies the spacing between adjacent subcarriers.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **15 kHz**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NB-IoT UL Subcarrier Spacing |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| 15 kHz | 0 | The subcarrier spacing is 15 kHz. |
| --- | --- | --- |
| 3.75 kHz | 1 | The subcarrier spacing is 3.75 kHz. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304060.html language=enus -->
## TOPIC 00064: Component Carrier:NB-IoT:Auto NPUSCH Channel Detection Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304060.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304060.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the values of the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties are auto-detected by the measurement or specified by you. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector

### Component Carrier:NB-IoT:Auto NPUSCH Channel Detection Enabled

Specifies whether the values of the [NPUSCH Tone Offset](/csh?topicname=attr304062.html), [NPUSCH Number of Tones](/csh?topicname=attr304063.html), and [NPUSCH Mod Type](/csh?topicname=attr304064.html) properties are auto-detected by the measurement or specified by you.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto NPUSCH Channel Detection Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement uses the values that you specify for the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties. |
| --- | --- | --- |
| True | 1 | The measurement uses the values of the NPUSCH Tone Offset, NPUSCH Number of Tones, and NPUSCH Mod Type properties that are auto-detected. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304061.html language=enus -->
## TOPIC 00065: Component Carrier:NB-IoT:NPUSCH:Format

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304061.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304061.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read t

### Component Carrier:NB-IoT:NPUSCH:Format

Specifies the NPUSCH format. A value of 1 indicates that narrowband physical uplink shared channel (NPUSCH) carries user data (UL-SCH) and a value of 2 indicates that NPUSCH carries uplink control information.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | NPUSCH Format |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30406a.html language=enus -->
## TOPIC 00066: ModAcc:Results:Uplink:NPUSCH:Mean RMS Data EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30406a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30406a.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to percentage, the result is returned as a percentage, and when you set the ModA

### ModAcc:Results:Uplink:NPUSCH:Mean RMS Data EVM (% or dB)

Returns the mean value of RMS EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **percentage**, the result is returned as a percentage, and when you set the ModAcc EVM Unit property to **dB**, the result is returned in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results NPUSCH Mean RMS Data EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30406b.html language=enus -->
## TOPIC 00067: ModAcc:Results:Uplink:NPUSCH:Maximum Peak Data EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30406b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30406b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to percentage, the result is returned as a percentage, and when you set the

### ModAcc:Results:Uplink:NPUSCH:Maximum Peak Data EVM (% or dB)

Returns the maximum value of peak EVMs calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **percentage**, the result is returned as a percentage, and when you set the ModAcc EVM Unit property to **dB**, the result is returned in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results NPUSCH Max Pk Data EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30406e.html language=enus -->
## TOPIC 00068: ModAcc:Results:Uplink:NPUSCH:Mean Data Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30406e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30406e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result.

### ModAcc:Results:Uplink:NPUSCH:Mean Data Power (dBm)

Returns the mean value of the power calculated on the narrowband physical uplink shared channel (NPUSCH) data symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results NPUSCH Mean Data Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304070.html language=enus -->
## TOPIC 00069: Component Carrier:eMTC Analysis Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304070.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304070.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or read this property. The default value is False. Remarks The following table lists the characteris

### Component Carrier:eMTC Analysis Enabled

Specifies whether the component carrier contains enhanced machine type communications (Cat-M1 or Cat-M2) transmission.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | eMTC Analysis Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement considers the signal as LTE FDD/TDD transmission. |
| --- | --- | --- |
| True | 1 | Detects the eMTC half duplex pattern, narrow band hopping, and eMTC guard symbols present in the uplink transmission. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304074.html language=enus -->
## TOPIC 00070: ModAcc:Results:Sidelink:PSSCH:Maximum Peak Data EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304074.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304074.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set t

### ModAcc:Results:Sidelink:PSSCH:Maximum Peak Data EVM (% or dB)

Returns the maximum value of the peak EVMs calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PSSCH Max Pk Data EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304075.html language=enus -->
## TOPIC 00071: ModAcc:Results:Sidelink:PSSCH:Mean RMS DMRS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304075.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304075.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the

### ModAcc:Results:Sidelink:PSSCH:Mean RMS DMRS EVM (% or dB)

Returns the mean value of the RMS EVMs calculated on the PSSCH DMRS symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PSSCH Mean RMS DMRS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304076.html language=enus -->
## TOPIC 00072: ModAcc:Results:Sidelink:PSSCH:Maximum Peak DMRS EVM (% or dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304076.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304076.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length property. When you set the ModAcc EVM Unit property to Percentage, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to dB, the

### ModAcc:Results:Sidelink:PSSCH:Maximum Peak DMRS EVM (% or dB)

Returns the maximum value of the peak EVMs calculated on PSSCH DMRS symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property.

When you set the [ModAcc EVM Unit](attr304006.html) property to **Percentage**, the measurement returns this result as a percentage. When you set the ModAcc EVM Unit property to **dB**, the measurement returns this result in dB.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PSSCH Max Pk DMRS EVM |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304077.html language=enus -->
## TOPIC 00073: ModAcc:Results:Sidelink:PSSCH:Mean Data Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304077.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304077.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks Th

### ModAcc:Results:Sidelink:PSSCH:Mean Data Power (dBm)

Returns the mean value of the power calculated on the physical sidelink shared channel (PSSCH) data symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PSSCH Mean Data Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr304078.html language=enus -->
## TOPIC 00074: ModAcc:Results:Sidelink:PSSCH:Mean DMRS Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr304078.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr304078.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the ModAcc Meas Length property. This value is expressed in dBm. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Remarks The following table lists the charact

### ModAcc:Results:Sidelink:PSSCH:Mean DMRS Power (dBm)

Returns the mean value of the power calculated on the PSSCH DMRS symbols over the slots specified by the [ModAcc Meas Length](/csh?topicname=attr304005.html) property. This value is expressed in dBm.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results PSSCH Mean DMRS Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30407e.html language=enus -->
## TOPIC 00075: ModAcc:Multicarrier Time Synchronization Mode

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30407e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30407e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time synchronization mode used in uplink in the case of carrier aggregation. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The d

### ModAcc:Multicarrier Time Synchronization Mode

Specifies the time synchronization mode used in uplink in the case of carrier aggregation.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Common**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Multicarrier Time Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Common | 0 | Specifies that a common time synchronization value is used for synchronization of all the component carriers and time synchronization value is obtained from the synchronization of the first active component carrier of the first subblock. |
| --- | --- | --- |
| Per Carrier | 1 | Specifies that time synchronization is performed on each component carrier. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr306006.html language=enus -->
## TOPIC 00076: OBW:Averaging:Count

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr306006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr306006.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### OBW:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](/csh?topicname=attr306007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr306007.html language=enus -->
## TOPIC 00077: OBW:Averaging:Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr306007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr306007.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the OBW measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remar

### OBW:Averaging:Enabled

Specifies whether to enable averaging for the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr306009.html language=enus -->
## TOPIC 00078: OBW:Averaging:Type

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr306009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr306009.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the

### OBW:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30600f.html language=enus -->
## TOPIC 00079: OBW:Sweep Time:Auto

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30600f.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks Th

### OBW:Sweep Time:Auto

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr306010.html language=enus -->
## TOPIC 00080: OBW:Sweep Time:Interval (s)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr306010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr306010.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### OBW:Sweep Time:Interval (s)

Specifies the sweep time when you set the [OBW Sweep Time Auto](/csh?topicname=attr30600f.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 ms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE OBW Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr306016.html language=enus -->
## TOPIC 00081: OBW:Results:Stop Frequency (Hz)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr306016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr306016.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation: Occupied bandwidth = Stop frequency - Start frequency Use "subblock<n>" as the selector string to read this result. Remarks The following table lists the

### OBW:Results:Stop Frequency (Hz)

Returns the stop frequency of the carrier/subblock. This value is expressed in Hz. Occupied bandwidth is calculated using the following equation:

*Occupied bandwidth* = *Stop frequency* - *Start frequency*

Use "subblock<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE OBW Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30601b.html language=enus -->
## TOPIC 00082: OBW:Amplitude Correction Type

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30601b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30601b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation Table VI to configure the external attenuation table. You do not need t

### OBW:Amplitude Correction Type

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation Table](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_configure_external_attenuation_table) VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Amplitude Correction Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| RF Center Frequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| --- | --- | --- |
| Spectrum Frequency Bin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308000.html language=enus -->
## TOPIC 00083: SEM:Measurement Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308000.html
- document_id: `rfmxlte-labview-api-ref`
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
| High-level VIs | RFmxLTE Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308005.html language=enus -->
## TOPIC 00084: SEM:Component Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308005.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of a component carrier. This value is expressed in Hz. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. The default value is 9 MHz. Remarks The following table lists the characteristics of this property. Short Name SEM CC IBW

### SEM:Component Carrier:Integration Bandwidth (Hz)

Returns the integration bandwidth of a component carrier. This value is expressed in Hz.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

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

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30800b.html language=enus -->
## TOPIC 00085: SEM:Offset:Number of Offsets

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30800b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30800b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of SEM offset segments. Use "subblock<n>" as the selector string to configure or read this property. The default value is 1. Remarks The following table lists the characteristics of this property. Short Name SEM Num Offsets Data type ci32.png Permissions Read/Write High-level VI

### SEM:Offset:Number of Offsets

Specifies the number of SEM offset segments.

Use "subblock<*n*>" as the selector string to configure or read this property.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Num Offsets |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Number of Offsets |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30801a.html language=enus -->
## TOPIC 00086: SEM:Offset:Relative Limit:Start (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30801a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30801a.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB. This property is considered only when you set the Link Direction property to Downlink. Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to configure or read this p

### SEM:Offset:Relative Limit:Start (dB)

Specifies the relative power limit corresponding to the beginning of the offset segment. This value is expressed in dB.

This property is considered only when you set the [Link Direction](attr300029.html) property to **Downlink**.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this property.

The default value is -51.5.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Rel Limit Start (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Offset Relative Limit |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30801b.html language=enus -->
## TOPIC 00087: SEM:Offset:Relative Limit:Stop (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30801b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30801b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB. This property is considered only when you set the Link Direction property to Downlink. Use "offset<k>" or "subblock<n>/offset<k>" as the selector string to configure or read this propert

### SEM:Offset:Relative Limit:Stop (dB)

Specifies the relative power limit corresponding to the end of the offset segment. This value is expressed in dB.

This property is considered only when you set the [Link Direction](attr300029.html) property to **Downlink**.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to configure or read this property.

The default value is -58.5.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Rel Limit Stop (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Offset Relative Limit |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30801d.html language=enus -->
## TOPIC 00088: SEM:Number of Analysis Threads

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30801d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30801d.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the SEM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources

### SEM:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the SEM measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30801e.html language=enus -->
## TOPIC 00089: SEM:Averaging:Count

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30801e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30801e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### SEM:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [SEM Averaging Enabled](/csh?topicname=attr30801f.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30801f.html language=enus -->
## TOPIC 00090: SEM:Averaging:Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30801f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30801f.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the SEM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remar

### SEM:Averaging:Enabled

Specifies whether to enable averaging for the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308021.html language=enus -->
## TOPIC 00091: SEM:Averaging:Type

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308021.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the str

### SEM:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308025.html language=enus -->
## TOPIC 00092: SEM:Sweep Time:Auto

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308025.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the sweep time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks Th

### SEM:Sweep Time:Auto

Specifies whether the measurement computes the sweep time.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Sweep Time Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the SEM Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses a sweep time of 1 ms. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308026.html language=enus -->
## TOPIC 00093: SEM:Sweep Time:Interval (s)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308026.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the SEM Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### SEM:Sweep Time:Interval (s)

Specifies the sweep time when you set the [SEM Sweep Time Auto](/csh?topicname=attr308025.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 ms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308035.html language=enus -->
## TOPIC 00094: SEM:Results:Lower Offset:Relative Integrated Power (dB)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308035.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308035.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the 3GPP TS 36.521 specification. If the o

### SEM:Results:Lower Offset:Relative Integrated Power (dB)

Returns the power in the lower (negative) offset segment relative to the total aggregated power. For the intra-band non-contiguous type of carrier aggregation, the offset segment may be truncated or discarded based on the offset overlap rules, as defined in the *3GPP TS 36.521* specification. If the offset segment is truncated, the measurement is performed on the updated offset segment. If the offset segment is discarded, a NaN is returned. This value is expressed in dB.

Refer to the [LTE Uplink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_spectral_emission_mask_sem) and [LTE Downlink Spectral Emission Mask](/csh?context=rfmxlte_rfmxlte_lte_downlink_spectral_emission_mask_sem) topics for more information about SEM offsets.

Use "offset<*k*>" or "subblock<*n*>/offset<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Rel Integrated Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE SEM Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr308056.html language=enus -->
## TOPIC 00095: SEM:Component Carrier:Maximum Output Power (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr308056.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr308056.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum output power, P[max,c], per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of 3GPP 36.141 specification. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to configure or re

### SEM:Component Carrier:Maximum Output Power (dBm)

Specifies the maximum output power, P<sub>max,c</sub>, per carrier that is used only to choose the limit table for Medium Range Base Station. For more details please refer to the section 6.6.3 of *3GPP 36.141* specification.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to configure or read this property.

The default value is 0. Valid values are within 38, inclusive.

Note

Link Direction

Downlink

eNodeB Category

Medium Range Base Station

SEM DL Mask Type

eNodeB Category Based

200k

max,c

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM CC Max Output Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SEM Configure Component Carrier Maximum Output Power |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr309000.html language=enus -->
## TOPIC 00096: PVT:Measurement Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr309000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr309000.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE.

### PVT:Measurement Enabled

Specifies whether to enable the power versus time (PVT) measurement.

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

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr309002.html language=enus -->
## TOPIC 00097: PVT:Measurement Method

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr309002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr309002.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method for performing the power versus time (PVT) measurement. Refer to the LTE PVT (Power Vs Time) Measurement topic for more information about multi acquisition PVT. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to

### PVT:Measurement Method

Specifies the method for performing the power versus time (PVT) measurement.

Refer to the [LTE PVT (Power Vs Time) Measurement](/csh?context=rfmxlte_rfmxlte_pvt) topic for more information about multi acquisition PVT.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Normal**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Meas Method |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE PvT Configure Measurement Method |
| Resettable | Yes |

| Normal | 0 | The measurement is performed using a single acquisition. Use this method when a high dynamic range is not required. |
| --- | --- | --- |
| Dynamic Range | 1 | The measurement is performed using two acquisitions. Use this method when a higher dynamic range is desirable over the measurement speed. Supported Devices: PXIe-5644/5645/5646, PXIe-5840/5841/5842/5860 |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr309007.html language=enus -->
## TOPIC 00098: PVT:Averaging:Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr309007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr309007.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default v

### PVT:Averaging:Enabled

Specifies whether to enable averaging for the power versus time (PVT) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE PvT Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The PVT measurement uses the value of the PVT Averaging Count property as the number of acquisitions over which the PVT measurement is averaged. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30900e.html language=enus -->
## TOPIC 00099: PVT:Results:Measurement Status

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30900e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30900e.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status indicating whether the power before and after the burst is within the standard defined limit. Refer to the LTE PVT (Power Vs Time) Measurement topic for more information about measurement status. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to re

### PVT:Results:Measurement Status

Returns the measurement status indicating whether the power before and after the burst is within the standard defined limit.

Refer to the [LTE PVT (Power Vs Time) Measurement](/csh?context=rfmxlte_rfmxlte_pvt) topic for more information about measurement status.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Results Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE PvT Fetch |
| Resettable | No |

| Fail | 0 | Indicates that the measurement has failed. |
| --- | --- | --- |
| Pass | 1 | Indicates that the measurement has passed. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr309011.html language=enus -->
## TOPIC 00100: PVT:Results:Mean Absolute OFF Power After (dBm)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr309011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr309011.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power in the segment after the captured burst. This value is expressed in dBm. The segment is defined as one subframe long, excluding a transient period of 20 micro seconds at the beginning. Use "carrier<k>" or "subblock<n>/carrier<k>" as the selector string to read this result. Ref

### PVT:Results:Mean Absolute OFF Power After (dBm)

Returns the mean power in the segment after the captured burst. This value is expressed in dBm. The segment is defined as one subframe long, excluding a transient period of 20 micro seconds at the beginning.

Use "carrier<*k*>" or "subblock<*n*>/carrier<*k*>" as the selector string to read this result.

Refer to the [LTE PVT (Power Vs Time) Measurement](/csh?context=rfmxlte_rfmxlte_pvt) topic for more information about OFF Power.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | PVT Results Mean Abs OFF Pwr After (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxLTE PvT Fetch |
| Resettable | No |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30a00b.html language=enus -->
## TOPIC 00101: SlotPhase:All Traces Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30a00b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30a00b.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for n

### SlotPhase:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30b002.html language=enus -->
## TOPIC 00102: SlotPower:Measurement Offset (subframes)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30b002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30b002.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for inform

### SlotPower:Measurement Offset (subframes)

Specifies the measurement offset to skip from the frame boundary or the marker (external trigger) location. This value is expressed in subframe.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Meas Offset (subframes) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SlotPower Configure Measurement Interval |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30b003.html language=enus -->
## TOPIC 00103: SlotPower:Measurement Length (subframes)

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30b003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30b003.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of subframes to be measured. This value is expressed in subframe. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defau

### SlotPower:Measurement Length (subframes)

Specifies the number of subframes to be measured. This value is expressed in subframe.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Meas Length (subframes) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxLTE SlotPower Configure Measurement Interval |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30b00a.html language=enus -->
## TOPIC 00104: SlotPower:All Traces Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30b00a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30b00a.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the SlotPower measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for n

### SlotPower:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the SlotPower measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30d001.html language=enus -->
## TOPIC 00105: Advanced:Acquisition Bandwidth Optimization Enabled

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30d001.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30d001.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured. You do not need to use a selector string to configure or read this property for the default signal instance. Refer

### Advanced:Acquisition Bandwidth Optimization Enabled

Specifies whether RFmx optimizes the acquisition bandwidth. This may cause acquisition center frequency or local oscillator (LO) to be placed at different position than you configured.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

Refer to the [Acquisition Bandwidth Optimization Enabled](/csh?context=rfmxlte_rfmxlte_acquisition_bandwidth) topic for more information.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Acq BW Optimization Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | RFmx does not optimize acquisition bandwidth and will be based on the Nyquist criterion. The value of the acquisition center frequency is the same as the value of the Center Frequency that you configure. |
| --- | --- | --- |
| True | 1 | RFmx positions the acquisition center frequency to acquire the least bandwidth based on the configuration and span needed for the measurement. This helps in reducing the amount of data to process for the measurement, thus improving the speed. However this might cause the LO to be positioned at a non-dc subcarrier position, hence the measurement sensitive to it should have this property disabled. |

Parent topic:

RFmxLTE Properties

<!--NI_TOPIC bundle=rfmxlte-labview-api-ref path=resource/objmgr/rfmxlte-rc/rfmxlte/attr30d002.html language=enus -->
## TOPIC 00106: Advanced:Transmitter Architecture

- bundle_id: `rfmxlte-labview-api-ref`
- source_path: `resource/objmgr/rfmxlte-rc/rfmxlte/attr30d002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxlte-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxlte-rc/rfmxlte/attr30d002.html
- document_id: `rfmxlte-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated. The measurement i

### Advanced:Transmitter Architecture

Specifies the RF architecture at the transmitter in case of a multicarrier. 3GPP defines different options, each component carriers within a subblock can have separate LO or one common LO for an entire subblock. Based upon the selected option, the additional results are calculated.

The measurement ignores this property when you set the [Link Direction](attr300029.html) property to **Downlink**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **LO per Component Carrier**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Transmitter Architecture |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| LO per Component Carrier | 0 | IQ impairments and In-band emission are calculated per component carrier. |
| --- | --- | --- |
| LO per Subblock | 1 | Additional subblock based results such as Subblock IQ Offset and Subblock In band emission are calculated apart from per carrier results. |

Parent topic:

RFmxLTE Properties
