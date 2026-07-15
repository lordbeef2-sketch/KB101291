# NI DOCUMENT BUNDLE: rfmxwcdma-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxwcdma-labview-api-ref start=1 end=230 -->
<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-acp-mnu.html language=enus -->
## TOPIC 00001: ACP

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-acp-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-acp-mnu.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure ACP measurements. You can use the RFmxWCDMA Property Node to configure additional properties. icon

### ACP

Use the VIs on this palette to configure ACP measurements. You can use the RFmxWCDMA Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-wcdma-mx-configuration-acp-mnu.png']

- [RFmxWCDMA ACP Configure Averaging VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-averaging-vi.html) Configures averaging for the ACP measurement.
- [RFmxWCDMA ACP Configure Sweep Time VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-sweep-time-vi.html) Configures the sweep time interval.
- [RFmxWCDMA ACP Configure Number of Offsets VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-number-of-offsets-vi.html) Configures the number of offsets for the ACP measurement.
- [RFmxWCDMA ACP Configure Offset Power Reference VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-offset-power-reference-vi.html) Configures the power reference to use for measuring the relative power of the offset channel.
- [RFmxWCDMA ACP Configure Measurement Method VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-measurement-method-vi.html) Configures the method for performing the ACP measurement.
- [RFmxWCDMA ACP Configure Noise Compensation Enabled VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-noise-compensation-enabled-vi.html) Configures the compensation of the channel power for the inherent noise floor of the signal analyzer.
- [RFmxWCDMA ACP Configure RBW Filter VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-rbw-filter-vi.html) Configures the RBW filter.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-array-vis-mnu.html language=enus -->
## TOPIC 00002: Array VIs

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-array-vis-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-array-vis-mnu.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure array VIs. You can also use the RFmxWCDMA Property Node to configure additional properties. icon

### Array VIs

Use the VIs on this palette to configure array VIs. You can also use the [RFmxWCDMA Property Node](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_property_node) to configure additional properties.

[IMAGE alt='icon' src='rfmx-wcdma-mx-configuration-array-vis-mnu.png']

- [RFmxWCDMA Configure Carrier Frequency (Array) VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-carrier-frequency-array-vi.html) Configures an array of the center frequencies of the carriers, relative to the RF center frequency.
- [RFmxWCDMA Configure Uplink Test Model (Array) VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-array-vi.html) Configures the uplink test model for all the carriers.
- [RFmxWCDMA Configure Number of Channels (Array) VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-array-vi.html) Configures the number of user-defined channels for all the carriers in the measurement. This VI is used when you set the Channel Configuration Mode property to User Defined . Call this VI before you call the RFmxWCDMA Configure User Defined Channel (Array) VI or the RFmxWCDMA Configure User Defined Channel VI.
- [RFmxWCDMA Configure User Defined Channel (Array) VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-array-vi.html) Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this VI, you must configure the Num Channels property with the appropriate number of user-defined channels.
- [RFmxWCDMA Configure Uplink Scrambling (Array) VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-scrambling-array-vi.html) Configures the scrambling code and the scrambling code type for all the carriers.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-cda-mnu.html language=enus -->
## TOPIC 00003: CDA

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-cda-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/wcdma/configuration/rfmx-wcdma-mx-configuration-cda-mnu.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure CDA measurements. You can also use the RFmxWCDMA Property Node to configure additional properties. icon

### CDA

Use the VIs on this palette to configure CDA measurements. You can also use the RFmxWCDMA Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-wcdma-mx-configuration-cda-mnu.png']

- [RFmxWCDMA CDA Configure Synchronization Mode and Interval VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-synchronization-mode-and-interval-vi.html) Configures the synchronization mode, measurement offset, and measurement length.
- [RFmxWCDMA CDA Configure Measurement Channel VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-measurement-channel-vi.html) Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.
- [RFmxWCDMA CDA Configure Power Unit VI](../../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-power-unit-vi.html) Configures the power unit for all code domain power results, except Total Power (dBm).

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=menus/categories/measurement/rfmx/wcdma/dir-mnu.html language=enus -->
## TOPIC 00004: WCDMA

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/wcdma/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/wcdma/dir-mnu.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to perform WCDMA measurements. You can use the RFmxWCDMA Property Node to configure additional properties. © 2015–2026 National Instruments. All rights reserved. icon

### WCDMA

Use the VIs on this palette to perform WCDMA measurements. You can use the RFmxWCDMA Property Node to configure additional properties.

© 2015–2026 National Instruments. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [Configuration](../../../../../menus/categories/measurement/rfmx/wcdma/configuration/dir-mnu.html) Use the VIs on this palette to configure RFmxWCDMA measurements. You can use the RFmxWCDMA Property Node to configure additional properties.
- [RFmxWCDMA Select Measurement VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-vi.html) Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.
- [RFmxWCDMA Initiate VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-initiate-vi.html) Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the RFmxWCDMA Property Node.
- [Fetch](../../../../../menus/categories/measurement/rfmx/wcdma/rfmx-wcdma-mx-fetch-mnu.html) Use the VIs on this palette to fetch measurement results and traces.
- [Utility](../../../../../menus/categories/measurement/rfmx/wcdma/utility/dir-mnu.html) Use the VIs on this palette to configure the RFmx WCDMA utilities.
- [RFmxWCDMA Property Node VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-property-node-vi.html) Sets (writes) or gets (reads) RFmxWCDMA properties.
- [Advanced](../../../../../menus/categories/measurement/rfmx/wcdma/rfmx-wcdma-mx-advanced-mnu.html) Use the VIs on this palette to use advanced features.
- [Build String](../../../../../menus/categories/measurement/rfmx/wcdma/utility/rfmx-wcdma-mx-utility-build-string-mnu.html) Use the VIs on this palette to create strings for configurations and results that require a selector string.

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=menus/categories/measurement/rfmx/wcdma/rfmx-wcdma-mx-advanced-mnu.html language=enus -->
## TOPIC 00005: Advanced

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/wcdma/rfmx-wcdma-mx-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/wcdma/rfmx-wcdma-mx-advanced-mnu.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. icon

### Advanced

Use the VIs on this palette to use advanced features.

[IMAGE alt='icon' src='rfmx-wcdma-mx-advanced-mnu.png']

- [RFmxWCDMA Abort Measurements VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-abort-measurements-vi.html) Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxWCDMA Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.
- [RFmxWCDMA Analyze2 VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze2-vi.html) Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.
- [RFmxWCDMA Create Signal Configuration VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-create-signal-configuration-vi.html) Creates a new instance of a signal.
- [RFmxWCDMA Clone Signal Configuration VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clone-signal-configuration-vi.html) Creates a new instance of a signal by copying all the property values from an existing signal instance.
- [RFmxWCDMA Delete Signal Configuration VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-delete-signal-configuration-vi.html) Deletes an instance of a signal that you specify in the Signal Name parameter.
- [RFmxWCDMA Get All Named Result Names VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-get-all-named-result-names-vi.html) Returns the named result names of the signal that you specify in the Selector String parameter.
- [RFmxWCDMA Clear Named Result VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-named-result-vi.html) Clears a result instance specified by the result name in the Selector String parameter.
- [RFmxWCDMA Clear All Named Results VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-all-named-results-vi.html) Clears all results for the signal that you specify in the Selector String parameter.

Parent topic:

WCDMA

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500003.html language=enus -->
## TOPIC 00006: External Attenuation (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500003.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information abou

### External Attenuation (dB)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.

This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Attenuation (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure External Attenuation |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500004.html language=enus -->
## TOPIC 00007: Trigger:Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500004.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is None. Remarks The following table lists the cha

### Trigger:Type

Specifies the trigger type.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **None**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Trigger |
| Resettable | Yes |

| None | 0 | No Reference Trigger is configured. |
| --- | --- | --- |
| Digital Edge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Slope property. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500005.html language=enus -->
## TOPIC 00008: Trigger:Digital Edge:Source

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500005.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informat

### Trigger:Digital Edge:Source

Specifies the source terminal for the digital edge trigger.

This property is used only when you set the [Trigger Type](attr500004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Trigger |
| Resettable | Yes |

| PFI0 | PFI0 | The trigger is received on PFI 0. For the PXIe-5841 with PXIe-5655, the trigger is received on the PXIe-5841 PFI 0. |
| --- | --- | --- |
| PFI1 | PFI1 | The trigger is received on PFI 1. |
| PXI_Trig0 | PXI_Trig0 | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | The trigger is received on PXI trigger line 7. |
| PXI_STAR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarB | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid only on the PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| TimerEvent | TimerEvent | The trigger is received from the Timer event. This value is valid only on the PXIe-5820/5840/5841/5842/5860 and for digital edge Advance Triggers on the PXIe-5663E/5665. |
| PulseIn | PulseIn | The trigger is received from the PULSE IN terminal. This value is valid only on the PXIe-5842. |
| DIO/PFI0 | DIO/PFI0 | The trigger is received on PFI 0 of the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | The trigger is received on PFI 1 of the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | The trigger is received on PFI 2 of the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | The trigger is received on PFI 3 of the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | The trigger is received on PFI 4 of the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | The trigger is received on PFI 5 of the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | The trigger is received on PFI 6 of the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | The trigger is received on PFI 7 of the DIO front panel connector. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500009.html language=enus -->
## TOPIC 00009: Trigger:IQ Power Edge:Slope

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500009.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge. You

### Trigger:IQ Power Edge:Slope

Specifies whether the device asserts the trigger when the signal power is rising or when it is falling.

The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the [Trigger Type](attr500004.html) property to **IQ Power Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Rising Slope**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Power Edge Slope |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Trigger |
| Resettable | Yes |

| Rising Slope | 0 | The trigger asserts when the signal power is rising. |
| --- | --- | --- |
| Falling Slope | 1 | The trigger asserts when the signal power is falling. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500010.html language=enus -->
## TOPIC 00010: Carrier:Channel:Configuration Mode

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500010.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the channel configuration mode. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Auto Detect. Remarks The followin

### Carrier:Channel:Configuration Mode

Specifies the channel configuration mode.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Configuration Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Channel Configuration Mode |
| Resettable | Yes |

| Auto Detect | 0 | The measurement detects the channels. |
| --- | --- | --- |
| User Defined | 1 | Configure the channels using the Num Channels property and the RFmxWCDMA Configure User Defined Channel (Array) VI. |
| Test Model | 2 | Choose from the standard-defined channel configurations using the UL Test Model property. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500019.html language=enus -->
## TOPIC 00011: Carrier:Channel:Uplink Test Model

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500019.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the uplink test model when the user sets the Channel Configuration Mode property to Test Model. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C

### Carrier:Channel:Uplink Test Model

Specifies the uplink test model when the user sets the [Channel Configuration Mode](/csh?topicname=attr500010.html) property to **Test Model**.

Each test model is a set of channel configurations defined by the standard.

Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the *3GPP TS 34.121-1* specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<*n*>, where *n* is the oldest release number with a given set of channel configurations.

Use "carrier<*n*>" as the selector string to configure or read this property.

The default value is **R6 C.2.1**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | UL Test Model |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Configure Uplink Test Model |
| Resettable | Yes |

| R6 C.2.1 | 0 | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| --- | --- | --- |
| R6 C.2.2 | 1 | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.3 | 2 | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.4 | 3 | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.5 | 4 | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.10.1.4 Subtest1 | 5 | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest2 | 6 | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest3 | 7 | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest4 | 8 | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest5 | 9 | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest6 | 10 | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7 C.10.1.4 Subtest1 | 11 | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest2 | 12 | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest3 | 13 | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest4 | 14 | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest1 | 15 | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest2 | 16 | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest3 | 17 | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest4 | 18 | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest5 | 19 | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8 C.11.1.3 Subtest1 | 20 | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest2 | 21 | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest3 | 22 | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest4 | 23 | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest5 | 24 | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.4 Subtest1 | 25 | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50001a.html language=enus -->
## TOPIC 00012: Carrier:Channel:Downlink Test Model

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50001a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50001a.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the symbol boundary synchronization method. Use "carrier<n>" as the selector string to configure or read this property. Remarks The following table lists the characteristics of this property. Short Name DL Test Model Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable Y

### Carrier:Channel:Downlink Test Model

Specifies the symbol boundary synchronization method.

Use "carrier<*n*>" as the selector string to configure or read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DL Test Model |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Test Model 1 - 16 DPCH | 0 | Test Model 1 with 16 DPCH is used for synchronization. |
| --- | --- | --- |
| Test Model 1 - 32 DPCH | 1 | Test Model 1 with 32 DPCH is used for synchronization. |
| Test Model 1 - 64 DPCH | 2 | Test Mode 1 with 64 DPCH is used for synchronization. |
| Test Model 1 - 16 DPCH/S-CCPCH | 3 | Test Model 1 with 16 DPCH and S-CCPCH is used for synchronization. |
| Test Model 1 - 32 DPCH/S-CCPCH | 4 | Test Model 1 with 32 DPCH and S-CCPCH is used for synchronization. |
| Test Model 1 - 64 DPCH/S-CCPCH | 5 | Test Model 1 with 64 DPCH and S-CCPCH is used for synchronization. |
| Test Model 2 | 6 | Test Model 2 is used for synchronization. |
| Test Model 2 - S-CCPCH | 7 | Test Model 2 with a S-CCPCH is used for synchronization. |
| Test Model 3 - 16 DPCH | 8 | Test Mode 3 with 16 DPCH is used for synchronization. |
| Test Model 3 - 32 DPCH | 9 | Test Mode 3 with 32 DPCH is used for synchronization. |
| Test Model 3 - 16 DPCH/S-CCPCH | 10 | Test Model 3 with 16 DPCH/S-CCPCH is used for synchronization. |
| Test Model 3 - 32 DPCH/S-CCPCH | 11 | Test Model 3 with 16 DPCH/S-CCPCH is used for synchronization. |
| Test Model 4 | 12 | Test Model 4 is used for synchronization. |
| Test Model 4 - P-CPICH | 13 | Test Model 4 with P-CPICH is used for synchronization. |
| Test Model 5 - 2 HS-PDSCH [16QAM] | 14 | Test Model 5 with 2 HS-PDSCH [16QAM] is used for synchronization. |
| Test Model 5 - 4 HS-PDSCH / 4DPCH [16QAM] | 15 | Test Model 5 with 4 HS-PDSCH / 4DPCH [16QAM] is used for synchronization. |
| Test Model 5 - 4 HS-PDSCH / 14DPCH [16QAM] | 16 | Test Model 5 with 4 HS-PDSCH / 14DPCH [16QAM] is used for synchronization. |
| Test Model 5 - 8 HS-PDSCH [16QAM] | 17 | Test Model 5 with 8 HS-PDSCH [16QAM] is used for synchronization. |
| Test Model 6 - 4 HS-PDSCH [64QAM] | 18 | Test Model 6 with 4 HS-PDSCH [64QAM] is used for synchronization. |
| Test Model 6 - 8 HS-PDSCH [64QAM] | 19 | Test Model 6 with 8 HS-PDSCH [64QAM] is used for synchronization. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500ffd.html language=enus -->
## TOPIC 00013: Selected Ports

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500ffd.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr500ffd.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about

### Selected Ports

Specifies the instrument port to be configured to acquire a signal. Use [RFmxInstr Get Available Ports](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_get_available_ports) VI to get the valid port names.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

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

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selected Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50100e.html language=enus -->
## TOPIC 00014: ACP:Offset:Integration Bandwidth (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50100e.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ACP Offset IBW (Hz) Data type c

### ACP:Offset:Integration Bandwidth (Hz)

Returns the frequency range, over which the measurement integrates the offset channel power. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Offset IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501012.html language=enus -->
## TOPIC 00015: ACP:Measurement Method

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501012.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA ACP Configure Measurement Method |
| Resettable | Yes |

| Normal | 0 | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| --- | --- | --- |
| Dynamic Range | 1 | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R |
| Sequential FFT | 2 | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Num Analysis Threads >=1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |  |
| ACP RBW Auto | True |  |
| ACP RBW Filter Type | FFT Based |  |
| ACP Sweep Time Auto | False |  |
| ACP Averaging Count | >=1 |  |
| ACP Num Analysis Threads | >=1 |  |
| ACP Amplitude Correction Type | RF Center Frequency |  |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501014.html language=enus -->
## TOPIC 00016: ACP:Number of Analysis Threads

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501014.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The number

### ACP:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501015.html language=enus -->
## TOPIC 00017: ACP:Averaging:Count

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501015.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### ACP:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [ACP Averaging Enabled](/csh?topicname=attr501016.html) to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501016.html language=enus -->
## TOPIC 00018: ACP:Averaging:Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501016.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA ACP Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The ACP measurement uses the value of the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501018.html language=enus -->
## TOPIC 00019: ACP:Averaging:Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501018.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging the spectrum of multiple acquisitions. The averaged spectrum is used for ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about

### ACP:Averaging:Type

Specifies the averaging type for averaging the spectrum of multiple acquisitions. The averaged spectrum is used for ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ACP Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501039.html language=enus -->
## TOPIC 00020: ACP:Advanced:Sequential FFT Size

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501039.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr501039.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of bins to use for FFT computation when the ACP Meas Method property is set to Sequential FFT. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax

### ACP:Advanced:Sequential FFT Size

Specifies the number of bins to use for FFT computation when the [ACP Meas Method](/csh?topicname=attr501012.html) property is set to **Sequential FFT**.

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

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr503003.html language=enus -->
## TOPIC 00021: CHP:Number of Analysis Threads

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr503003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr503003.html
- document_id: `rfmxwcdma-labview-api-ref`
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

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr503006.html language=enus -->
## TOPIC 00022: CHP:Averaging:Count

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr503006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr503006.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### CHP:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](/csh?topicname=attr503007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CHP Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506003.html language=enus -->
## TOPIC 00023: OBW:Number of Analysis Threads

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506003.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the OBW measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources

### OBW:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the OBW measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

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

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506004.html language=enus -->
## TOPIC 00024: OBW:Span (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506004.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for

### OBW:Span (Hz)

Returns the frequency range around the center frequency, to acquire for the measurement. This value is expressed in Hz.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Span (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506006.html language=enus -->
## TOPIC 00025: OBW:Averaging:Count

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506006.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### OBW:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](/csh?topicname=attr506007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506007.html language=enus -->
## TOPIC 00026: OBW:Averaging:Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506007.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA OBW Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506009.html language=enus -->
## TOPIC 00027: OBW:Averaging:Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506009.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA OBW Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600c.html language=enus -->
## TOPIC 00028: OBW:RBW Filter:Auto Bandwidth

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600c.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. This property is valid only if you set the OBW RBW Filter Type property to Gaussian or Flat. If you set the OBW RBW Filter Type property to FFT Based, the measurement calculates the RBW regardless of the setting of this property. You do not need to

### OBW:RBW Filter:Auto Bandwidth

Specifies whether the measurement computes the RBW.

This property is valid only if you set the [OBW RBW Filter Type](attr50600e.html) property to **Gaussian** or **Flat**.

If you set the OBW RBW Filter Type property to **FFT Based**, the measurement calculates the RBW regardless of the setting of this property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure RBW Filter |
| Resettable | Yes |

| False | 0 | The measurement uses the RBW that you specify in the OBW RBW property. |
| --- | --- | --- |
| True | 1 | The measurement uses an RBW value of 30 kHz. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600d.html language=enus -->
## TOPIC 00029: OBW:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600d.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the OBW RBW Auto property to False. This property is valid only if you set the OBW RBW Filter Type property to Gaussian or Flat. This value is expressed in Hz. You do not need to use a selector string to configu

### OBW:RBW Filter:Bandwidth (Hz)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [OBW RBW Auto](/csh?topicname=attr50600c.html) property to **False**.

This property is valid only if you set the [OBW RBW Filter Type](attr50600e.html) property to **Gaussian** or **Flat**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 30 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure RBW Filter |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600e.html language=enus -->
## TOPIC 00030: OBW:RBW Filter:Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600e.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA OBW Configure RBW Filter |
| Resettable | Yes |

| FFT Based | 0 | No RBW filtering is applied. |
| --- | --- | --- |
| Gaussian | 1 | An RBW filter with a Gaussian response is applied. |
| Flat | 2 | An RBW filter with a flat response is applied. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600f.html language=enus -->
## TOPIC 00031: OBW:Sweep Time:Auto

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50600f.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA OBW Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses a sweep time value of one slot duration. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506010.html language=enus -->
## TOPIC 00032: OBW:Sweep Time:Interval (s)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506010.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### OBW:Sweep Time:Interval (s)

Specifies the sweep time when you set the [OBW Sweep Time Auto](/csh?topicname=attr50600f.html) property to **False**.

This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA OBW Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506012.html language=enus -->
## TOPIC 00033: OBW:All Traces Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506012.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### OBW:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the OBW measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506013.html language=enus -->
## TOPIC 00034: OBW:Results:Occupied Bandwidth (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506013.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers. This value is expressed in Hz. OBW Results Occupied BW = OBW Results Stop Frequency - OBW Results Start Frequency. You do not need to use a selector string to read this result

### OBW:Results:Occupied Bandwidth (Hz)

Returns the bandwidth containing 99% of the total integrated power of the acquired signal around the center of the carriers.

This value is expressed in Hz.

*OBW Results Occupied BW* = *OBW Results Stop Frequency* - *OBW Results Start Frequency*.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Occupied BW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506014.html language=enus -->
## TOPIC 00035: OBW:Results:Absolute Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506014.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total integrated power of the acquired signal. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named

### OBW:Results:Absolute Power (dBm)

Returns the total integrated power of the acquired signal.

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Abs Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506015.html language=enus -->
## TOPIC 00036: OBW:Results:Start Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506015.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the occupied bandwidth. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named resu

### OBW:Results:Start Frequency (Hz)

Returns the start frequency of the [occupied bandwidth](/csh?topicname=attr506013.html).

This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Start Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506016.html language=enus -->
## TOPIC 00037: OBW:Results:Stop Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr506016.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the occupied bandwidth. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named resul

### OBW:Results:Stop Frequency (Hz)

Returns the stop frequency of the [occupied bandwidth](/csh?topicname=attr506013.html).

This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA OBW Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50601a.html language=enus -->
## TOPIC 00038: OBW:Amplitude Correction Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50601a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50601a.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation VI to configure the external attenuation table. You do not need to use

### OBW:Amplitude Correction Type

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_configure_external_attenuation_table) VI to configure the external attenuation table.

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

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508000.html language=enus -->
## TOPIC 00039: SEM:Measurement Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508000.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SEM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The followi

### SEM:Measurement Enabled

Specifies whether to enable the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508005.html language=enus -->
## TOPIC 00040: SEM:Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508005.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name SEM Carrier IBW (Hz) Data type cdbl.pn

### SEM:Carrier:Integration Bandwidth (Hz)

Returns the frequency range over which the measurement integrates the carrier power. This value is expressed in Hz.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Carrier IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50800b.html language=enus -->
## TOPIC 00041: SEM:Offset:Number of Offsets

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50800b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50800b.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of offset segments. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and results. Remarks The following table lists the characteristics

### SEM:Offset:Number of Offsets

Returns the number of offset segments.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Num Offsets |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50800c.html language=enus -->
## TOPIC 00042: SEM:Offset:Bandwidth Integral

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50800c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50800c.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW. Use "offset<n>" as the selector string to read this property. If this property returns a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then proces

### SEM:Offset:Bandwidth Integral

Returns the resolution of the spectrum to compare with spectral mask limits as an integer multiple of the RBW.

Use "offset<*n*>" as the selector string to read this property.

If this property returns a value greater than 1, the measurement acquires the spectrum with a narrow resolution and then processes it digitally to get a wider resolution that is equal to the product of the bandwidth integral and the RBW.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset BW Integral |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508014.html language=enus -->
## TOPIC 00043: SEM:Offset:Start Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508014.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name SEM Offset Start Freq

### SEM:Offset:Start Frequency (Hz)

Returns the start frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Start Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508015.html language=enus -->
## TOPIC 00044: SEM:Offset:Stop Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508015.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name SEM Offset Stop Freq (H

### SEM:Offset:Stop Frequency (Hz)

Returns the stop frequency of the offset segment relative to the center frequency of the carrier(s). This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508017.html language=enus -->
## TOPIC 00045: SEM:Offset:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508017.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name SEM Offset RBW (Hz) Data type cdbl.png Pe

### SEM:Offset:RBW Filter:Bandwidth (Hz)

Returns the bandwidth of the RBW filter used to sweep the acquired offset segment. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508018.html language=enus -->
## TOPIC 00046: SEM:Offset:RBW Filter:Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508018.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the shape of the digital RBW filter. Use "offset<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name SEM Offset RBW Filter Type Data type ci32.png Permissions Read Only High-level VIs N/A Resettable No FFT Based

### SEM:Offset:RBW Filter:Type

Returns the shape of the digital RBW filter.

Use "offset<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Offset RBW Filter Type |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

| FFT Based | 0 | No RBW filtering is performed. |
| --- | --- | --- |
| Gaussian | 1 | The RBW filter has a Gaussian response. |
| Flat | 2 | The RBW filter has a flat response. |
| Synch Tuned - 4 | 3 | The RBW filter has a response of a 4-pole synchronously tuned filter. |
| Synch Tuned - 5 | 4 | The RBW filter has a response of a 5-pole synchronously tuned filter. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801d.html language=enus -->
## TOPIC 00047: SEM:Number of Analysis Threads

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801d.html
- document_id: `rfmxwcdma-labview-api-ref`
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

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801e.html language=enus -->
## TOPIC 00048: SEM:Averaging:Count

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801e.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### SEM:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [SEM Averaging Enabled](/csh?topicname=attr50801f.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SEM Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801f.html language=enus -->
## TOPIC 00049: SEM:Averaging:Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50801f.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA SEM Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508021.html language=enus -->
## TOPIC 00050: SEM:Averaging:Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508021.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the

### SEM:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions.

The averaged spectrum is used for the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SEM Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508025.html language=enus -->
## TOPIC 00051: SEM:Sweep Time:Auto

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508025.html
- document_id: `rfmxwcdma-labview-api-ref`
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
| High-level VIs | RFmxWCDMA SEM Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the SEM Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses a sweep time value of one slot duration. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508026.html language=enus -->
## TOPIC 00052: SEM:Sweep Time:Interval (s)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508026.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the SEM Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### SEM:Sweep Time:Interval (s)

Specifies the sweep time when you set the [SEM Sweep Time Auto](/csh?topicname=attr508025.html) property to **False**.

This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 666.66666700000007 microseconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SEM Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508027.html language=enus -->
## TOPIC 00053: SEM:All Traces Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508027.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### SEM:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508028.html language=enus -->
## TOPIC 00054: SEM:Results:Total Carrier Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508028.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508028.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr property. For a single-carrier measurement, total carrier power is the same as carrier absolute power. This value is expressed in dBm. You do not need to use a selector

### SEM:Results:Total Carrier Power (dBm)

Returns the sum of all active carrier powers, where each carrier power corresponds to the value of the [SEM Results Carrier Abs Pwr](/csh?topicname=attr50802d.html) property. For a single-carrier measurement, total carrier power is the same as carrier absolute power.

This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Total Carrier Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508030.html language=enus -->
## TOPIC 00055: SEM:Results:Carrier:Peak Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508030.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508030.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power is observed in the carrier channel. This value is expressed in Hz. Use "carrier<k>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Carrier Pk Freq (Hz) Data type

### SEM:Results:Carrier:Peak Frequency (Hz)

Returns the frequency at which the peak power is observed in the carrier channel.

This value is expressed in Hz.

Use "carrier<*k*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Carrier Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508034.html language=enus -->
## TOPIC 00056: SEM:Results:Lower Offset:Absolute Integrated Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508034.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower, or negative, offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to configure or read this property. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Abs Integrated

### SEM:Results:Lower Offset:Absolute Integrated Power (dBm)

Returns the power measured in the lower, or negative, offset segment.

This value is expressed in dBm.

Use "offset<*n*>" as the selector string to configure or read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Abs Integrated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508035.html language=enus -->
## TOPIC 00057: SEM:Results:Lower Offset:Relative Integrated Power (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508035.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508035.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name S

### SEM:Results:Lower Offset:Relative Integrated Power (dB)

Returns the power measured in the lower, or negative, offset segment relative to the [SEM Results Total Carrier Pwr](/csh?topicname=attr508028.html) property.

This value is expressed in dB.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Rel Integrated Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508036.html language=enus -->
## TOPIC 00058: SEM:Results:Lower Offset:Absolute Peak Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508036.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508036.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the lower, or negative, offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Abs Peak Pwr (dBm) Data t

### SEM:Results:Lower Offset:Absolute Peak Power (dBm)

Returns the peak power measured in the lower, or negative, offset segment.

This value is expressed in dBm.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Abs Peak Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508037.html language=enus -->
## TOPIC 00059: SEM:Results:Lower Offset:Relative Peak Power (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508037.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508037.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short N

### SEM:Results:Lower Offset:Relative Peak Power (dB)

Returns the peak power measured in the lower, or negative, offset segment relative to the [SEM Results Total Carrier Pwr](/csh?topicname=attr508028.html) property.

This value is expressed in dB.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Rel Peak Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508038.html language=enus -->
## TOPIC 00060: SEM:Results:Lower Offset:Peak Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508038.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508038.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power is observed in the lower offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Pk Freq (Hz) D

### SEM:Results:Lower Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power is observed in the lower offset segment.

This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50803c.html language=enus -->
## TOPIC 00061: SEM:Results:Lower Offset:Margin Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50803c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50803c.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency corresponding to the SEM Results Lower Offset Margin property. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Margin Freq (Hz)

### SEM:Results:Lower Offset:Margin Frequency (Hz)

Returns the frequency corresponding to the [SEM Results Lower Offset Margin](/csh?topicname=attr508039.html) property.

This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Margin Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50803d.html language=enus -->
## TOPIC 00062: SEM:Results:Lower Offset:Measurement Status

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50803d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50803d.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the measurement status based on the SEM Results Lower Offset Margin property. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Meas Status Data type ci32.png Permissions R

### SEM:Results:Lower Offset:Measurement Status

Indicates the measurement status based on the [SEM Results Lower Offset Margin](/csh?topicname=attr508039.html) property.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

| Fail | 0 | Indicates that the value of the SEM Results Lower Offset Margin property is positive. |
| --- | --- | --- |
| Pass | 1 | Indicates that the value of the SEM Results Lower Offset Margin property is zero or negative. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508041.html language=enus -->
## TOPIC 00063: SEM:Results:Upper Offset:Absolute Integrated Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508041.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper, or positive, offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Abs Integrated Pwr (dBm) Data

### SEM:Results:Upper Offset:Absolute Integrated Power (dBm)

Returns the power measured in the upper, or positive, offset segment.

This value is expressed in dBm.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Abs Integrated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508042.html language=enus -->
## TOPIC 00064: SEM:Results:Upper Offset:Relative Integrated Power (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508042.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name S

### SEM:Results:Upper Offset:Relative Integrated Power (dB)

Returns the power measured in the upper, or positive, offset segment relative to the [SEM Results Total Carrier Pwr](/csh?topicname=attr508028.html) property.

This value is expressed in dB.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Rel Integrated Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508043.html language=enus -->
## TOPIC 00065: SEM:Results:Upper Offset:Absolute Peak Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508043.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508043.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper, or positive, offset segment. This value is expressed in dBm. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Abs Peak Pwr (dBm) Data t

### SEM:Results:Upper Offset:Absolute Peak Power (dBm)

Returns the peak power measured in the upper, or positive, offset segment.

This value is expressed in dBm.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Abs Peak Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508044.html language=enus -->
## TOPIC 00066: SEM:Results:Upper Offset:Relative Peak Power (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508044.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508044.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak power measured in the upper, or positive, offset segment relative to the value of the SEM Results Total Carrier Pwr property. This value is expressed in dB. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this prop

### SEM:Results:Upper Offset:Relative Peak Power (dB)

Returns the peak power measured in the upper, or positive, offset segment relative to the value of the [SEM Results Total Carrier Pwr](/csh?topicname=attr508028.html) property.

This value is expressed in dB.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Rel Peak Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508045.html language=enus -->
## TOPIC 00067: SEM:Results:Upper Offset:Peak Frequency (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr508045.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power is observed in the upper offset segment. This value is expressed in Hz. Use "offset<n>" as the selector string to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Pk Freq (Hz) D

### SEM:Results:Upper Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power is observed in the upper offset segment.

This value is expressed in Hz.

Use "offset<*n*>" as the selector string to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA SEM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50804c.html language=enus -->
## TOPIC 00068: SEM:Amplitude Correction Type

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50804c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50804c.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the RFmxInstr Configure External Attenuation VI to configure the external attenuation table. You do not need to use

### SEM:Amplitude Correction Type

Specifies whether the amplitude of the frequency bins, used in measurements, is corrected for external attenuation at the RF center frequency, or at the individual frequency bins. Use the [RFmxInstr Configure External Attenuation](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_configure_external_attenuation_table) VI to configure the external attenuation table.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RF Center Frequency**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Amplitude Correction Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| RF Center Frequency | 0 | All the frequency bins in the spectrum are compensated with a single external attenuation value that corresponds to the RF center frequency. |
| --- | --- | --- |
| Spectrum Frequency Bin | 1 | An individual frequency bin in the spectrum is compensated with the external attenuation value corresponding to that frequency. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50c000.html language=enus -->
## TOPIC 00069: Result Fetch Timeout (s)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50c000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50c000.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time to wait before results are available in the RFmxWCDMA Property Node. This value is expressed in seconds. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWCDMA Property Node waits until the measurement is complete. Yo

### Result Fetch Timeout (s)

Specifies the time to wait before results are available in the [RFmxWCDMA Property Node](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_property_node).

This value is expressed in seconds.

Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxWCDMA Property Node waits until the measurement is complete.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

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

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50d000.html language=enus -->
## TOPIC 00070: Advanced:Auto Level Initial Reference Level (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50d000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50d000.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial reference level that the RFmxWCDMA Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm. The default value is 30. Remarks The following table lists the characteristics of this property. Short Name Auto Level Initial Ref Level (dBm) D

### Advanced:Auto Level Initial Reference Level (dBm)

Specifies the initial reference level that the [RFmxWCDMA Auto Level](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_auto_level) VI uses to estimate the peak power of the input signal.

This value is expressed in dBm.

The default value is 30.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Level Initial Ref Level (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50d003.html language=enus -->
## TOPIC 00071: Advanced:Limited Configuration Change

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50d003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr50d003.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the set of properties that are considered by RFmx in the locked signal configuration state. If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this property to help achieve faster measurements.

### Advanced:Limited Configuration Change

Specifies the set of properties that are considered by RFmx in the locked signal configuration state.

If your test system performs the same measurement at different selected ports, multiple frequencies, and/or power levels repeatedly, you can enable this property to help achieve faster measurements. When you set this property to a value other than **Disabled**, the RFmx driver will use an optimized code path and skip some checks. Because RFmx skips some checks when you use this property, you need to be aware of the limitations of this feature, which are listed in the [Limitations of the Limited Configuration Change Property](limitations.html) topic.

You can also use this property to lock a specific instrument configuration for a signal so that every time that you initiate the signal, RFmx applies the RFmxInstr properties from a locked configuration.

NI recommends you use this property in conjunction with named signal configurations. Create named signal configurations for each measurement configuration in your test program and set this property to a value other than **Disabled** for one or more of the named signal configurations. This allows RFmx to precompute the acquisition settings for your measurement configurations and re-use the precomputed settings each time you initiate the measurement. You do not need to use this property if you create named signals for all the measurement configurations in your test program during test sequence initialization and do not change any RFInstr or personality properties while testing each device under test. RFmx automatically optimizes that use case.

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
| Freq and Ref Level | 4 | Signal configuration, other than center frequency, reference level, and external attenuation, is locked after first Commit of the named signal configuration. Thereafter only the Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends that you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |
| Selected Ports, Freq and Ref Level | 5 | Signal configuration, other than selected ports, center frequency, reference level, external attenuation, and RFInstr configuration, is locked after first Commit or Initiate of the named signal configuration. Thereafter only Selected Ports, Center Frequency, Reference Level, and External Attenuation property value changes will be considered by subsequent driver Commits or Initiates of this signal. If you have configured this signal to use an IQ Power Edge Trigger, NI recommends you set the IQ Power Edge Level Type to Relative so that the trigger level is automatically adjusted as you adjust the reference level. Refer to the Limitations of the Limited Configuration Change Property topic for more details about the limitations of using this mode. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511000.html language=enus -->
## TOPIC 00072: ModAcc:Measurement Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511000.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ModAcc measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The foll

### ModAcc:Measurement Enabled

Specifies whether to enable the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511002.html language=enus -->
## TOPIC 00073: ModAcc:Synchronization Mode

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511002.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame, slot, or symbol boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The def

### ModAcc:Synchronization Mode

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement Offset slots from the slot boundary. |
| Arbitrary | 2 | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement Offset slots from the symbol boundary. |
| Marker | 3 | The measurement is performed over the number of slots expressed by the ModAcc Measurement Length property starting at ModAcc Measurement Offset slots from the trigger. This is the fastest way to do a ModAcc measurement. This mode requires the Trigger Type property to be set to Digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511004.html language=enus -->
## TOPIC 00074: ModAcc:Measurement Length (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511004.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the ModAcc measurement. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default

### ModAcc:Measurement Length (slots)

Specifies the duration of the ModAcc measurement.

This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1. Valid values are [1, (15 - [ModAcc Measurement Offset](attr511003.html))]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Meas Length (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA ModAcc Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511005.html language=enus -->
## TOPIC 00075: ModAcc:Spectrum Inverted

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511005.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks Th

### ModAcc:Spectrum Inverted

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Spectrum Inverted |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The spectrum is not inverted. |
| --- | --- | --- |
| True | 1 | The spectrum is inverted. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511006.html language=enus -->
## TOPIC 00076: ModAcc:IQ Offset Removal Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511006.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the ModAcc measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is F

### ModAcc:IQ Offset Removal Enabled

Specifies whether to remove the I/Q offset before the ModAcc measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc IQ Offset Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The I/Q offset is not removed before the ModAcc measurement. |
| --- | --- | --- |
| True | 1 | The I/Q offset is removed before the ModAcc measurement. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511007.html language=enus -->
## TOPIC 00077: ModAcc:Transient Removal Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511007.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results. Transients are expected to be present at the slot boundaries, where the mean power of the received signal can change.

### ModAcc:Transient Removal Enabled

Specifies whether the measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error and RMS phase error results.

Transients are expected to be present at the slot boundaries, where the mean power of the received signal can change.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Transient Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The entire measurement interval is used to compute the RMS EVM, peak EVM, RMS magnitude error, and RMS phase error results. |
| --- | --- | --- |
| True | 1 | The measurement excludes 25 microseconds from the start and end of each slot while computing the RMS EVM, peak EVM, RMS magnitude error, and RMS phase error results. The ModAcc Sync Mode property must be set to Frame, Slot, or Marker. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511015.html language=enus -->
## TOPIC 00078: ModAcc:Results:Rho

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511015.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the figure of merit used to characterize the modulation accuracy of the composite code domain signal. It refers to the fraction of the total power that can be correlated to the correct active channels in the detected reference signal. Use "carrier<n>" as the selector string to read this prop

### ModAcc:Results:Rho

Returns the figure of merit used to characterize the modulation accuracy of the composite code domain signal. It refers to the fraction of the total power that can be correlated to the correct active channels in the detected reference signal.

Use "carrier<*n*>" as the selector string to read this property.

You can calculate the value of Rho using the following equation:

*Rho* = *Power correctly correlated to active channels* / *Total power*

A Rho value of 1 indicates that all the transmitted power is correlated to the correct active channels and there is no power in the inactive (undesired) channels. Any energy correlated to the inactive channels degrades modulation quality and results in a value of Rho less than 1. Valid values are 0.0 to 1.0, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Rho |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511016.html language=enus -->
## TOPIC 00079: ModAcc:Results:I/Q Origin Offset (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511016.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the cha

### ModAcc:Results:I/Q Origin Offset (dB)

Returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB.

The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511017.html language=enus -->
## TOPIC 00080: ModAcc:Results:Frequency Error (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511017.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency offset of the composite signal. This value is expressed in Hz. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Freq Error (Hz) Data type cdbl.png Permissions Read On

### ModAcc:Results:Frequency Error (Hz)

Returns the frequency offset of the composite signal.

This value is expressed in Hz.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511018.html language=enus -->
## TOPIC 00081: ModAcc:Results:Chip Rate Error (ppm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511018.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error of the composite signal. This value is expressed in ppm. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Chip Rate Error (ppm) Data type cdbl.png Permissions R

### ModAcc:Results:Chip Rate Error (ppm)

Returns the chip rate error of the composite signal.

This value is expressed in ppm.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Chip Rate Error (ppm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511019.html language=enus -->
## TOPIC 00082: ModAcc:Results:Peak CDE (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511019.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum code domain error value (CDE). This value is expressed in dB. The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used. The CDE for every code with the specific spreading factor is defined as the ra

### ModAcc:Results:Peak CDE (dB)

Returns the maximum code domain error value (CDE).

This value is expressed in dB.

The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used.

The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk CDE (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101b.html language=enus -->
## TOPIC 00083: ModAcc:Results:Peak CDE Code

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101b.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading code corresponding to the value of the ModAcc Results Pk CDE property. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Pk CDE Code Data type ci32.png Permissions Rea

### ModAcc:Results:Peak CDE Code

Returns the spreading code corresponding to the value of the [ModAcc Results Pk CDE](/csh?topicname=attr511019.html) property.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk CDE Code |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101c.html language=enus -->
## TOPIC 00084: ModAcc:Results:Peak Active CDE (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101c.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB. The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as th

### ModAcc:Results:Peak Active CDE (dB)

Returns the maximum value among the active code domain errors (CDEs) for a carrier. This value is expressed in dB.

The active CDEs are computed by despreading the descrambled error vectors corresponding to each active channel with the appropriate active channel codes. The active CDE is defined as the ratio of the mean power of this despread error vector to the mean power of the composite reference waveform.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk Active CDE (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101e.html language=enus -->
## TOPIC 00085: ModAcc:Results:Peak Active CDE Code

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101e.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading code of the channel corresponding to the value of the ModAcc Results Pk Active CDE property for a carrier. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Pk Active

### ModAcc:Results:Peak Active CDE Code

Returns the spreading code of the channel corresponding to the value of the [ModAcc Results Pk Active CDE](/csh?topicname=attr51101c.html) property for a carrier.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk Active CDE Code |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101f.html language=enus -->
## TOPIC 00086: ModAcc:Results:P-SCH Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51101f.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The primary SCH power for a BS UUT. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results P-SCH Power (dBm) Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### ModAcc:Results:P-SCH Power (dBm)

The primary SCH power for a BS UUT.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results P-SCH Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511020.html language=enus -->
## TOPIC 00087: ModAcc:Results:S-SCH Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511020.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The secondary SCH power for a BS UUT. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results S-SCH Power (dBm) Data type cdbl.png Permissions Read Only High-level VIs N/A Resettable No

### ModAcc:Results:S-SCH Power (dBm)

The secondary SCH power for a BS UUT.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results S-SCH Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511021.html language=enus -->
## TOPIC 00088: ModAcc:Results:DPCH Timing Offset (chips)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511021.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: The timing offset of the selected channel. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results DPCH Timing Offset (chips) Data type cdbl.png Permissions Read Only High-level VIs N/A Resettabl

### ModAcc:Results:DPCH Timing Offset (chips)

The timing offset of the selected channel.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results DPCH Timing Offset (chips) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511022.html language=enus -->
## TOPIC 00089: ModAcc:Results:Peak RCDE (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511022.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511022.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB. The relative CDEs are computed by despreading the descrambled error vector corresponding to each active channel with the appropriate active channel codes. The

### ModAcc:Results:Peak RCDE (dB)

Returns the maximum value among the relative code domain errors (RCDEs) for all active channels for a carrier. This value is expressed in dB.

The relative CDEs are computed by despreading the descrambled error vector corresponding to each active channel with the appropriate active channel codes. The RCDE is defined as the ratio of the mean power of this despread error vector to the mean power of the corresponding reference waveform.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk RCDE (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511023.html language=enus -->
## TOPIC 00090: ModAcc:Results:Peak RCDE Spreading Factor

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511023.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading factor of the channel corresponding to the value of the ModAcc Results Pk RCDE property for a carrier. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Pk RCDE Spread

### ModAcc:Results:Peak RCDE Spreading Factor

Returns the spreading factor of the channel corresponding to the value of the [ModAcc Results Pk RCDE](/csh?topicname=attr511022.html) property for a carrier.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk RCDE Spreading Factor |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511024.html language=enus -->
## TOPIC 00091: ModAcc:Results:Peak RCDE Code

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511024.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spreading code of the channel corresponding to the value of the ModAcc Results Pk RCDE property for a carrier. Use "carrier<n>" as the selector string to read this property. Remarks The following table lists the characteristics of this property. Short Name ModAcc Results Pk RCDE Code Dat

### ModAcc:Results:Peak RCDE Code

Returns the spreading code of the channel corresponding to the value of the [ModAcc Results Pk RCDE](/csh?topicname=attr511022.html) property for a carrier.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Pk RCDE Code |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511025.html language=enus -->
## TOPIC 00092: ModAcc:Results:Detected Channel:Number of Detected Channels

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr511025.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, this property returns the number of configured channels. Use "carrier<n>" as the selector string to read this

### ModAcc:Results:Detected Channel:Number of Detected Channels

Returns the number of detected channels when you set the [Channel Configuration Mode](/csh?topicname=attr500010.html) property to **Auto Detect**. If you set the Channel Configuration Mode property to **User Defined** or **Test Model**, this property returns the number of configured channels.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Num Detected Channels |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102d.html language=enus -->
## TOPIC 00093: ModAcc:Results:I/Q Gain Imbalance (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102d.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal of a carrier. This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. Use "carrier<n>" as the selector string to read this property. Remarks The

### ModAcc:Results:I/Q Gain Imbalance (dB)

Returns the I/Q gain imbalance of the composite signal of a carrier.
 This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102e.html language=enus -->
## TOPIC 00094: ModAcc:Results:I/Q Quadrature Error (deg)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102e.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error of the composite signal of a carrier. This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. Use "carrier<n>" as the selector string to read this property. Remarks The follo

### ModAcc:Results:I/Q Quadrature Error (deg)

Returns the I/Q quadrature error of the composite signal of a carrier.
 This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured.

Use "carrier<*n*>" as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Quadrature Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102f.html language=enus -->
## TOPIC 00095: ModAcc:Results:Multicarrier IQ Origin Offset (dB)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51102f.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the estimated I/Q origin offset of the multicarrier signal when the Transmitter Architecture property is set to LO per Band. This value is expressed in dB. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the Se

### ModAcc:Results:Multicarrier IQ Origin Offset (dB)

Returns the estimated I/Q origin offset of the multicarrier signal when the [Transmitter Architecture](/csh?topicname=attr50d001.html) property is set to **LO per Band**. This value is expressed in dB.

You do not need to use a selector string to configure or read this property for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

This result is useful when the LO is at the center of the multicarrier signal.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Multicarrier IQ Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200d.html language=enus -->
## TOPIC 00096: QEVM:Number of Analysis Threads

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200d.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the QEVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The numbe

### QEVM:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations. The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200e.html language=enus -->
## TOPIC 00097: QEVM:Results:Mean RMS EVM (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200e.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The EVM of a chip is the magni

### QEVM:Results:Mean RMS EVM (%)

Returns the mean of the RMS EVM values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr512006) property.

The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean RMS EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200f.html language=enus -->
## TOPIC 00098: QEVM:Results:Maximum RMS EVM (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51200f.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the RMS EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The EVM of a chip is the magnitude of the vector diff

### QEVM:Results:Maximum RMS EVM (%)

Returns the maximum value of the RMS EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations.

 The number of acquisitions is specified by the value of the [QEVM Averaging Count](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr512006) property.

The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max RMS EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512012.html language=enus -->
## TOPIC 00099: QEVM:Results:Mean Magnitude Error (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512012.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The magnitude

### QEVM:Results:Mean Magnitude Error (%)

Returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage.
 This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr512006) property.

The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512013.html language=enus -->
## TOPIC 00100: QEVM:Results:Maximum Magnitude Error (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512013.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The magnitude error of a chip is the diff

### QEVM:Results:Maximum Magnitude Error (%)

Returns the maximum value of the RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr512006) property.

The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512015.html language=enus -->
## TOPIC 00101: QEVM:Results:Maximum Phase Error (deg)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512015.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The phase error of a chip is the difference in the

### QEVM:Results:Maximum Phase Error (deg)

Returns the maximum value of the RMS phase errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the [QEVM Averaging Count](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr512006) property.

The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max Phase Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512016.html language=enus -->
## TOPIC 00102: QEVM:Results:Mean Frequency Error (Hz)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr512016.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The frequency error i

### QEVM:Results:Mean Frequency Error (Hz)

Returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz.
 This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the [QEVM Averaging Count](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr512006) property.

The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514002.html language=enus -->
## TOPIC 00103: SlotPhase:Synchronization Mode

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514002.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or the slot boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default

### SlotPhase:Synchronization Mode

Specifies whether the measurement is performed from the frame or the slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots expressed by the SlotPhase Meas Length property starting at SlotPhase Meas Offset slots from the slot boundary. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514003.html language=enus -->
## TOPIC 00104: SlotPhase:Measurement Offset (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514003.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPhase Sync Mode property. You do not need to use a selector string to configure or read this property for the default signal instance. Re

### SlotPhase:Measurement Offset (slots)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPhase Sync Mode](/csh?topicname=attr514002.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0. The valid values are any value greater than or equal to 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Meas Offset (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514004.html language=enus -->
## TOPIC 00105: SlotPhase:Measurement Length (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514004.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the SlotPhase measurement. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defau

### SlotPhase:Measurement Length (slots)

Specifies the duration of the SlotPhase measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 15. The valid values are any value greater than or equal to 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Meas Length (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514010.html language=enus -->
## TOPIC 00106: SlotPhase:Results:Discontinuity Count > Limit 2

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514010.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings topic for information about

### SlotPhase:Results:Discontinuity Count > Limit 2

Returns the number of times the phase discontinuity values exceed the *Limit 2* value for the acquired signal. *Limit 2* is fixed at 66 degrees.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Results Disc Count > Limit 2 |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514011.html language=enus -->
## TOPIC 00107: SlotPhase:Results:Discontinuity Minimum Distance (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr514011.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. You do not need to use a selector string to read this result for default signal and result instance. Refer to the Selector Strings

### SlotPhase:Results:Discontinuity Minimum Distance (slots)

Returns the minimum distance between two phase discontinuity measurements exceeding the *Limit 1* value. *Limit 1* is fixed at 36 degrees. This value is expressed in slots.

You do not need to use a selector string to read this result for default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and results.

If there are no phase discontinuity values greater than *Limit 1*, or if there is only one phase discontinuity value greater than *Limit 1*, this result is not valid. In such a case, -1 is reported as the result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Results Disc Min Dist (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515000.html language=enus -->
## TOPIC 00108: CDA:Measurement Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515000.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the CDA measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The followi

### CDA:Measurement Enabled

Specifies whether to enable the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515002.html language=enus -->
## TOPIC 00109: CDA:Synchronization Mode

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515002.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame, slot, or symbol boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The def

### CDA:Synchronization Mode

Specifies whether the measurement is performed from the frame, slot, or symbol boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected and the measurement is performed over the number of slots expressed by the CDA Meas Length property, starting at CDA Meas Offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected and the measurement is performed over the number of slots expressed by CDA Meas Length property, starting at CDA Meas Offset slots from the slot boundary. |
| Arbitrary | 2 | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the CDA Meas Length property, starting at CDA Meas Offset slots from the symbol boundary. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515004.html language=enus -->
## TOPIC 00110: CDA:Measurement Length (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515004.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the code domain measurement. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The def

### CDA:Measurement Length (slots)

Specifies the duration of the code domain measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1. Valid values are [1, (15 - [CDA Measurement Offset](attr515003.html))]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Meas Length (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515005.html language=enus -->
## TOPIC 00111: CDA:Spectrum Inverted

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515005.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks Th

### CDA:Spectrum Inverted

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Spectrum Inverted |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The spectrum is not inverted. |
| --- | --- | --- |
| True | 1 | The spectrum is inverted. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515006.html language=enus -->
## TOPIC 00112: CDA:IQ Offset Removal Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515006.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q offset before the CDA measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is Fals

### CDA:IQ Offset Removal Enabled

Specifies whether to remove the I/Q offset before the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA IQ Offset Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The I/Q offset is not removed before the CDA measurement. |
| --- | --- | --- |
| True | 1 | the I/Q offset is removed before the CDA measurement. |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515015.html language=enus -->
## TOPIC 00113: CDA:All Traces Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515015.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces after performing the CDA measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value i

### CDA:All Traces Enabled

Specifies whether to enable the traces after performing the CDA measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515017.html language=enus -->
## TOPIC 00114: CDA:Results:RMS Symbol EVM (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515017.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS EVM for the measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named

### CDA:Results:RMS Symbol EVM (%)

Returns the RMS EVM for the measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results RMS Symbol EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515018.html language=enus -->
## TOPIC 00115: CDA:Results:Peak Symbol EVM (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515018.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the peak EVM for the measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signals and named

### CDA:Results:Peak Symbol EVM (%)

Returns the peak EVM for the measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Pk Symbol EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515019.html language=enus -->
## TOPIC 00116: CDA:Results:RMS Symbol Magnitude Error (%)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515019.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about the string syntax for named signal

### CDA:Results:RMS Symbol Magnitude Error (%)

Returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results RMS Symbol Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501b.html language=enus -->
## TOPIC 00117: CDA:Results:Total Power (dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501b.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selector Strings topic for information about t

### CDA:Results:Total Power (dBm)

Returns the mean power of the received signal, sampled at ideal inter-symbol-interference free points. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Total Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501c.html language=enus -->
## TOPIC 00118: CDA:Results:Mean Symbol Power (dB or dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501c.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. You do not need

### CDA:Results:Mean Symbol Power (dB or dBm)

Returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. If you set the [CDA Pwr Unit](/csh?topicname=attr51500d.html) property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [CDA Results Total Pwr](/csh?topicname=attr51501b.html) property.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Mean Symbol Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501f.html language=enus -->
## TOPIC 00119: CDA:Results:Total Active Power (dB or dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr51501f.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the sum of all the active channel powers. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. You do not need to use a selector

### CDA:Results:Total Active Power (dB or dBm)

Returns the sum of all the active channel powers. If you set the [CDA Pwr Unit](/csh?topicname=attr51500d.html) property to **dBm**, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [CDA Results Total Pwr](/csh?topicname=attr51501b.html) property. This value is expressed in dB or dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Total Active Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515021.html language=enus -->
## TOPIC 00120: CDA:Results:Peak Active Power (dB or dBm)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr515021.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the largest code power among the set of active channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm.

### CDA:Results:Peak Active Power (dB or dBm)

Returns the largest code power among the set of active channels in the code domain. If you set the [CDA Pwr Unit](/csh?topicname=attr51500d.html) property to **dBm**, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the [CDA Results Total Pwr](/csh?topicname=attr51501b.html) property. This value is expressed in dB or dBm.

You do not need to use a selector string to read this result for the default signal and result instances. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Pk Active Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxWCDMA CDA Fetch |
| Resettable | No |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516000.html language=enus -->
## TOPIC 00121: SlotPower:Measurement Enabled

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516000.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPower measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The f

### SlotPower:Measurement Enabled

Specifies whether to enable the SlotPower measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516002.html language=enus -->
## TOPIC 00122: SlotPower:Measurement Offset (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516002.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the SlotPower Sync Mode property. You do not need to use a selector string to configure or read this property for the default signal instance. Re

### SlotPower:Measurement Offset (slots)

Specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the [SlotPower Sync Mode](/csh?topicname=attr516007.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0. The valid values are any value greater than or equal to 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Meas Offset (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516003.html language=enus -->
## TOPIC 00123: SlotPower:Measurement Length (slots)

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxwcdma-rc/rfmxwcdma/attr516003.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of the SlotPower measurement. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defau

### SlotPower:Measurement Length (slots)

Specifies the duration of the SlotPower measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 15. The valid values are any value greater than or equal to 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Meas Length (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxWCDMA SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxWCDMA Properties

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-measurement-method-vi.html language=enus -->
## TOPIC 00124: RFmxWCDMA ACP Configure Measurement Method VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-measurement-method-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-configure-measurement-method-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxWCDMA ACP Configure Measurement Method VI

Configures the method for performing the ACP measurement.

[IMAGE alt='icon' src='rfmxwcdma-acp-configure-measurement-method-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Method — Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum with the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported devices: PXIe-5665/5668R Sequential FFT (2) The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads >=1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Normal (0) | The ACP measurement acquires the spectrum with the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported devices: PXIe-5665/5668R |
| Sequential FFT (2) | The ACP measurement acquires I/Q samples for a duration specified by the ACP Sweep Time property. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed on each of these chunks. The resultant FFTs are averaged to get the spectrum and is used to compute ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of acquisition are not used for the measurement. Use this method to optimize ACP measurement speed. Accuracy of the results may be reduced when using this measurement method. For accurate power measurements, when the power characteristics of the signal vary over time, Averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Property Supported Value ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Sweep Time Auto False ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads >=1 ACP Amplitude Correction Type RF Center Frequency Note For multi-span FFT, the averaging count should be 1. |
| Property | Supported Value |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Sweep Time Auto | False |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | >=1 |
| ACP Amplitude Correction Type | RF Center Frequency |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-carrier-measurement-array-vi.html language=enus -->
## TOPIC 00125: RFmxWCDMA ACP Fetch Carrier Measurement (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-carrier-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-carrier-measurement-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the ACP Results Total Carrier Pwr property. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and re

### RFmxWCDMA ACP Fetch Carrier Measurement (Array) VI

Returns the array of absolute powers and the array of relative powers for the ACP measurement. The relative powers are relative to the [ACP Results Total Carrier Pwr](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr501022) property.

[IMAGE alt='icon' src='rfmxwcdma-acp-fetch-carrier-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Power (dBm) — Absolute Power returns an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. Relative Power (dB) — Relative Power returns an array of carrier power values relative to the total active carrier power. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-carrier-measurement-vi.html language=enus -->
## TOPIC 00126: RFmxWCDMA ACP Fetch Carrier Measurement VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-carrier-measurement-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power. Use "carrier<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, re

### RFmxWCDMA ACP Fetch Carrier Measurement VI

Fetches the absolute and relative powers of the carrier. The relative power is relative to the total carrier power.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxwcdma-acp-fetch-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Power (dBm) — Absolute Power returns the carrier power. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. Relative Power (dB) — Relative Power returns the carrier power relative to the total carrier power. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-offset-measurement-array-vi.html language=enus -->
## TOPIC 00127: RFmxWCDMA ACP Fetch Offset Measurement (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-offset-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-offset-measurement-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the ACP Offset Pwr Ref Carrier property. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector s

### RFmxWCDMA ACP Fetch Offset Measurement (Array) VI

Fetches an array of absolute powers and an array of relative powers measured in the offset channels for the ACP measurement. The relative powers are measured with reference to the [ACP Offset Pwr Ref Carrier](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr50100c) property.

[IMAGE alt='icon' src='rfmxwcdma-acp-fetch-offset-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Lower Absolute Power (dBm) — Lower Absolute Power returns an array of lower offset channel power values. The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. Upper Absolute Power (dBm) — Upper Absolute Power returns an array of upper offset channel power values. The upper offset channel power is the integrated power of the RRC-filtered signal at the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Lower Relative Power (dB) — Lower Relative Power returns an array of lower offset channel power values measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. Upper Relative Power (dB) — Upper Relative Power returns an array of upper offset channel power values measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-offset-measurement-vi.html language=enus -->
## TOPIC 00128: RFmxWCDMA ACP Fetch Offset Measurement VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-offset-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-offset-measurement-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier. Use "offset<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifi

### RFmxWCDMA ACP Fetch Offset Measurement VI

Fetches the absolute and relative powers measured in the offset channel for the ACP measurement. The relative powers are measured relative to the power reference carrier.

Use "offset<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxwcdma-acp-fetch-offset-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Lower Absolute Power (dBm) — Lower Absolute Power returns the lower offset channel power. The lower offset channel power is the integrated power of the RRC-filtered signal at the lower offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. Upper Absolute Power (dBm) — Upper Absolute Power returns the upper offset channel power. The upper offset channel power is the integrated power of the RRC-filtered signal at the upper offset frequency. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Lower Relative Power (dB) — Lower Relative Power returns the offset channel power measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. Upper Relative Power (dB) — Upper Relative Power returns the upper offset channel power measured relative to the power of the carrier(s) that you specify in the ACP Offset Pwr Ref Carrier property. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-relative-powers-trace-vi.html language=enus -->
## TOPIC 00129: RFmxWCDMA ACP Fetch Relative Powers Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-relative-powers-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-relative-powers-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the res

### RFmxWCDMA ACP Fetch Relative Powers Trace VI

Fetches the relative powers trace for the ACP measurement.

[IMAGE alt='icon' src='rfmxwcdma-acp-fetch-relative-powers-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Relative Powers (dB) — Relative Powers returns the trace of relative power values measured in each channel relative to the power reference carrier. This value is expressed in dB. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the relative power with reference to the power reference carrier property. The value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the relative power with reference to the power reference carrier property. The value is expressed in dB. |

Parent topic:

RFmxWCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00130: RFmxWCDMA ACP Fetch Spectrum VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-acp-fetch-spectrum-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxWCDMA ACP Fetch Spectrum VI

Fetches the spectrum used for the ACP measurement.

[IMAGE alt='icon' src='rfmxwcdma-acp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power at each frequency bin. The value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power at each frequency bin. The value is expressed in dBm. |

Parent topic:

RFmxWCDMA ACP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00131: RFmxWCDMA Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze-iq-1-wfm-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxWCDMA Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx WCDMA Commit

[IMAGE alt='icon' src='rfmxwcdma-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxWCDMA Analyze2 VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze-spectrum-1-wfm-vi.html language=enus -->
## TOPIC 00132: RFmxWCDMA Analyze (Spectrum, 1 Wfm) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze-spectrum-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-analyze-spectrum-1-wfm-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum waveform that you specify in the Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Reco

### RFmxWCDMA Analyze (Spectrum, 1 Wfm) VI

Performs the enabled measurements on the spectrum waveform that you specify in the **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **Spectral** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx WCDMA Commit

[IMAGE alt='icon' src='rfmxwcdma-analyze-spectrum-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". Spectrum — Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y contains the real-value power spectrum. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y contains the real-value power spectrum. |

Parent topic:

RFmxWCDMA Analyze2 VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-auto-level-vi.html language=enus -->
## TOPIC 00133: RFmxWCDMA Auto Level VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-auto-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-auto-level-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level. The RFmxWCDMA Auto Level VI completes the following tasks: Resets the mixer level, mixer level offset, a

### RFmxWCDMA Auto Level VI

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr500002) property. Use this VI to help calculate an approximate setting for the reference level.

The RFmxWCDMA Auto Level VI completes the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device, based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [Auto Level Initial Ref Level](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr50d000) property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxWCDMA Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='icon' src='rfmxwcdma-auto-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Interval (s) — Measurement Interval specifies the acquisition length. Use this value to compute the number of samples to acquire from the signal analyzer. This value is expressed in seconds. The default value is 10 ms. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Reference Level — Reference Level returns the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-build-carrier-string-vi.html language=enus -->
## TOPIC 00134: RFmxWCDMA Build Carrier String VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-build-carrier-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-build-carrier-string-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch VIs, properties, and results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the

### RFmxWCDMA Build Carrier String VI

Creates the carrier string to use as the selector string with the SEM and ACP carrier configuration or fetch VIs, properties, and results.

[IMAGE alt='icon' src='rfmxwcdma-build-carrier-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Carrier Number — Carrier Number specifies the carrier number for building the selector string. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-build-channel-string-vi.html language=enus -->
## TOPIC 00135: RFmxWCDMA Build Channel String VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-build-channel-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-build-channel-string-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the channel string to use as the selector string with the channel configuration and results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal insta

### RFmxWCDMA Build Channel String VI

Creates the channel string to use as the selector string with the channel configuration and results.

[IMAGE alt='icon' src='rfmxwcdma-build-channel-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Channel Number — Channel Number specifies the channel number for building the selector string. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-power-unit-vi.html language=enus -->
## TOPIC 00136: RFmxWCDMA CDA Configure Power Unit VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-power-unit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-power-unit-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power unit for all code domain power results, except Total Power (dBm). icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value

### RFmxWCDMA CDA Configure Power Unit VI

Configures the power unit for all code domain power results, except Total Power (dBm).

[IMAGE alt='icon' src='rfmxwcdma-cda-configure-power-unit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Power Unit — Power Unit specifies the measurement unit of all power results, except, CDA Results Total Pwr. The default value is dB. dB (0) Specifies the power relative to the total power. dBm (1) Specifies the absolute power measured. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| dB (0) | Specifies the power relative to the total power. |
| dBm (1) | Specifies the absolute power measured. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00137: RFmxWCDMA CDA Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxWCDMA CDA Configure Synchronization Mode and Interval VI

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='icon' src='rfmxwcdma-cda-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. The Valid values are [0, (15 - Measurement Length)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15. Measurement Length (slots) — Measurement Length specifies the duration of the code domain measurement. This value is expressed in slots. The default value is 1. Valid values are [1, (15 - Measurement Offset)]. The sum of the CDA measurement offset and CDA measurement length must be less than or equal to 15. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-code-domain-i-and-q-power-vi.html language=enus -->
## TOPIC 00138: RFmxWCDMA CDA Fetch Code Domain I and Q Power VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-code-domain-i-and-q-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-code-domain-i-and-q-power-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I and Q mean active powers and I and Q peak inactive powers. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not s

### RFmxWCDMA CDA Fetch Code Domain I and Q Power VI

Fetches the I and Q mean active powers and I and Q peak inactive powers.

[IMAGE alt='icon' src='rfmxwcdma-cda-fetch-code-domain-i-and-q-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Q Peak Inactive Power (dB or dBm) — Q Peak Inactive Power (dB or dBm) returns the largest code power among the set of inactive quadrature-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I Mean Active Power (dB or dBm) — I Mean Active Power returns the average code power among the set of active in-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. Q Mean Active Power (dB or dBm) — Q Mean Active Power returns the average code power among the set of active quadrature-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. I Peak Inactive Power (dB or dBm) — I Peak Inactive Power returns the largest code power among the set of inactive in-phase channels in the code domain. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. This value is expressed in dB or dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-code-domain-power-trace-vi.html language=enus -->
## TOPIC 00139: RFmxWCDMA CDA Fetch Code Domain Power Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-code-domain-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-code-domain-power-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the code domain power trace. The code domain power is obtained for all codes with spreading factor 256 for both I and Q branches in an interleaved manner. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. I

### RFmxWCDMA CDA Fetch Code Domain Power Trace VI

Fetches the code domain power trace. The code domain power is obtained for all codes with spreading factor 256 for both I and Q branches in an interleaved manner.

[IMAGE alt='icon' src='rfmxwcdma-cda-fetch-code-domain-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Code Domain Powers (dB or dBm) — Code Domain Powers returns an array of code domain powers for I and Q branches in an interleaved manner. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-symbol-evm-vi.html language=enus -->
## TOPIC 00140: RFmxWCDMA CDA Fetch Symbol EVM VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-symbol-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-cda-fetch-symbol-evm-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and r

### RFmxWCDMA CDA Fetch Symbol EVM VI

Returns the root mean square and peak of symbol EVM, RMS of symbol magnitude error, RMS of symbol phase error, and mean symbol power, corresponding to the measurement channel.

[IMAGE alt='icon' src='rfmxwcdma-cda-fetch-symbol-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Symbol Power (dB or dBm) — Mean Symbol Power returns the mean power of the symbols for the measurement channel. This value is expressed in dB or dBm. If you set the CDA Pwr Unit property to dBm, the measurement returns an absolute value; otherwise, the measurement returns a value relative to the CDA Results Total Pwr property. RMS Symbol Phase Error (deg) — RMS Symbol Phase Error returns the RMS phase error for the measurement channel. This value is expressed in degrees. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS Symbol EVM (%) — RMS Symbol EVM returns the RMS EVM for the measurement channel. This value is expressed as a percentage. Peak Symbol EVM (%) — Peak Symbol EVM returns the peak EVM for the measurement channel. This value is expressed as a percentage. RMS Symbol Magnitude Error (%) — RMS Symbol Magnitude Error returns the RMS magnitude error for the measurement channel. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. Chip Rate Error (ppm) — Chip Rate Error returns the chip rate error of the composite signal. This value is expressed in ppm. |
| --- |

Parent topic:

RFmxWCDMA CDA Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-check-measurement-status-vi.html language=enus -->
## TOPIC 00141: RFmxWCDMA Check Measurement Status VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-check-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-check-measurement-status-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal nam

### RFmxWCDMA Check Measurement Status VI

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='icon' src='rfmxwcdma-check-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. done? — done? indicates whether the measurement is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-averaging-vi.html language=enus -->
## TOPIC 00142: RFmxWCDMA CHP Configure Averaging VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-averaging-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::

### RFmxWCDMA CHP Configure Averaging VI

Configures averaging for the CHP measurement.

[IMAGE alt='icon' src='rfmxwcdma-chp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00143: RFmxWCDMA CHP Configure RBW Filter VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-rbw-filter-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use t

### RFmxWCDMA CHP Configure RBW Filter VI

Configures the RBW filter.

[IMAGE alt='icon' src='rfmxwcdma-chp-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. The default value is True. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 50 kHz. — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-sweep-time-vi.html language=enus -->
## TOPIC 00144: RFmxWCDMA CHP Configure Sweep Time VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-configure-sweep-time-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You

### RFmxWCDMA CHP Configure Sweep Time VI

Configures the sweep time interval.

[IMAGE alt='icon' src='rfmxwcdma-chp-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00145: RFmxWCDMA CHP Fetch Spectrum VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-spectrum-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxWCDMA CHP Fetch Spectrum VI

Fetches the spectrum used for the CHP measurement.

[IMAGE alt='icon' src='rfmxwcdma-chp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power at each frequency bin. The value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power at each frequency bin. The value is expressed in dBm. |

Parent topic:

RFmxWCDMA CHP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-total-carrier-power-vi.html language=enus -->
## TOPIC 00146: RFmxWCDMA CHP Fetch Total Carrier Power VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-total-carrier-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-total-carrier-power-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power for the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxWCDMA CHP Fetch Total Carrier Power VI

Fetches the total carrier power for the CHP measurement.

[IMAGE alt='icon' src='rfmxwcdma-chp-fetch-total-carrier-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Total Carrier Power (dBm) — Total Carrier Power returns the total integrated power of all the active carriers. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA CHP Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-vi.html language=enus -->
## TOPIC 00147: RFmxWCDMA CHP Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the CHP measurement results. icon

### RFmxWCDMA CHP Fetch VI

Fetches the CHP measurement results.

[IMAGE alt='icon' src='rfmxwcdma-chp-fetch-vi.png']

- [RFmxWCDMA CHP Fetch Total Carrier Power VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-total-carrier-power-vi.html) Fetches the total carrier power for the CHP measurement.
- [RFmxWCDMA CHP Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-carrier-measurement-vi.html) Fetches the absolute and relative powers of the carrier for the CHP measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA CHP Fetch Carrier Measurement (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-carrier-measurement-array-vi.html) Fetches an array of absolute powers and array of relative powers of the carriers for the CHP measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA CHP Fetch Spectrum VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-chp-fetch-spectrum-vi.html) Fetches the spectrum used for the CHP measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-all-named-results-vi.html language=enus -->
## TOPIC 00148: RFmxWCDMA Clear All Named Results VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-all-named-results-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value i

### RFmxWCDMA Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxwcdma-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-named-result-vi.html language=enus -->
## TOPIC 00149: RFmxWCDMA Clear Named Result VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-named-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-clear-named-result-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxWCDMA Clear Named Result VI

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxwcdma-clear-named-result-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-carrier-frequency-array-vi.html language=enus -->
## TOPIC 00150: RFmxWCDMA Configure Carrier Frequency (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-carrier-frequency-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-carrier-frequency-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of the center frequencies of the carriers, relative to the RF center frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The

### RFmxWCDMA Configure Carrier Frequency (Array) VI

Configures an array of the center frequencies of the carriers, relative to the RF center frequency.

[IMAGE alt='icon' src='rfmxwcdma-configure-carrier-frequency-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Carrier Frequency (Hz) — Carrier Frequency specifies an array of the center frequencies of the carriers, relative to the RF center frequency. This value is expressed in Hz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Array VIs

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-contiguous-carriers-vi.html language=enus -->
## TOPIC 00151: RFmxWCDMA Configure Contiguous Carriers VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-contiguous-carriers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-contiguous-carriers-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is us

### RFmxWCDMA Configure Contiguous Carriers VI

Configures the contiguous carriers based on the number of carriers and the carrier at the center frequency.

[IMAGE alt='icon' src='rfmxwcdma-configure-contiguous-carriers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Carriers — Number of Carriers specifies the number of carriers. The default value is 1. Carrier at Center Frequency — Carrier at Center Frequency specifies the index of the carrier that is at the center frequency. Set this parameter to -1 to specify a center frequency at the center of all carriers. For example, if you set the value of the Number of Carriers parameter to 2, and set the value of the Carrier at Center Frequency parameter to 1, the center frequency is at carrier1. If you set the value of the Number of Carriers parameter to 2, and set the value of the Carrier at Center Frequency parameter to -1, the center frequency is at the center of carrier0 and carrier1. If you set the value of the Number of Carriers parameter to 3, and set the value of the Carrier at Center Frequency parameter to either -1 or 1, the center frequency is at carrier1, which is the center of all carriers. The default value is -1. Recommended values are -1 to (Number of Carriers - 1). If you set this parameter to a value greater than (Number of Carriers - 1), the value of this parameter is coerced to (Number of Carriers - 1). error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00152: RFmxWCDMA Configure Digital Edge Trigger VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-digital-edge-trigger-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String specifies a selector

### RFmxWCDMA Configure Digital Edge Trigger VI

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='icon' src='rfmxwcdma-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital edge trigger. The default value of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. PXIe_DStarB (PXIe_DStarB) The trigger is received on the PXIe DStar B trigger line. TimerEvent (TimerEvent) The trigger is received from the timer event. Digital Edge — Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| PFI0 (PFI0) | The trigger is received on PFI 0. |
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

RFmxWCDMA Configure Trigger VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-external-attenuation-vi.html language=enus -->
## TOPIC 00153: RFmxWCDMA Configure External Attenuation VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-external-attenuation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-external-attenuation-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the external attenuation. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You

### RFmxWCDMA Configure External Attenuation VI

Configures the external attenuation.

[IMAGE alt='icon' src='rfmxwcdma-configure-external-attenuation-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. External Attenuation (dB) — External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-frequency-vi.html language=enus -->
## TOPIC 00154: RFmxWCDMA Configure Frequency VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-frequency-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF center frequency directly or by using the UTRA absolute radio frequency channel number (UARFCN) and band. icon

### RFmxWCDMA Configure Frequency VI

Configures the RF center frequency directly or by using the UTRA absolute radio frequency channel number (UARFCN) and band.

[IMAGE alt='icon' src='rfmxwcdma-configure-frequency-vi.png']

- [RFmxWCDMA Configure Frequency (Frequency) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-frequency-frequency-vi.html) Configures the RF center frequency.
- [RFmxWCDMA Configure Frequency (UARFCN) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-frequency-uarfcn-vi.html) Configures the center frequency in the universal mobile telecommunications system (UMTS) frequency band using the link direction, band, and UARFCN of the received signal.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-array-vi.html language=enus -->
## TOPIC 00155: RFmxWCDMA Configure Number of Channels (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of user-defined channels for all the carriers in the measurement. This VI is used when you set the Channel Configuration Mode property to User Defined. Call this VI before you call the RFmxWCDMA Configure User Defined Channel (Array) VI or the RFmxWCDMA Configure User Defined C

### RFmxWCDMA Configure Number of Channels (Array) VI

Configures the number of user-defined channels for all the carriers in the measurement. This VI is used when you set the [Channel Configuration Mode](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr500010) property to **User Defined**. Call this VI before you call the [RFmxWCDMA Configure User Defined Channel (Array)](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_configure_user_defined_channel) VI or the [RFmxWCDMA Configure User Defined Channel](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_configure_user_defined_channel) VI.

[IMAGE alt='icon' src='rfmxwcdma-configure-number-of-channels-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Channels — Number of Channels specifies the array of number of channels. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Array VIs

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-vi.html language=enus -->
## TOPIC 00156: RFmxWCDMA Configure Number of Channels VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-number-of-channels-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of user-defined channels for the measurement. This VI is used when you set the Channel Configuration Mode property to User Defined. Call this VI before you call the RFmxWCDMA Configure User Defined Channel (Array) VI or the RFmxWCDMA Configure User Defined Channel VI. Use "carr

### RFmxWCDMA Configure Number of Channels VI

Configures the number of user-defined channels for the measurement. This VI is used when you set the [Channel Configuration Mode](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr500010) property to **User Defined**. Call this VI before you call the [RFmxWCDMA Configure User Defined Channel (Array)](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_configure_user_defined_channel_(array)) VI or the [RFmxWCDMA Configure User Defined Channel](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_configure_user_defined_channel) VI.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxwcdma-configure-number-of-channels-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Channels — Number of Channels specifies the number of user-defined channels. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-reference-level-vi.html language=enus -->
## TOPIC 00157: RFmxWCDMA Configure Reference Level VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-reference-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-reference-level-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level, which represents the maximum expected power of an RF input signal. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The d

### RFmxWCDMA Configure Reference Level VI

Configures the reference level, which represents the maximum expected power of an RF input signal.

[IMAGE alt='icon' src='rfmxwcdma-configure-reference-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Level — Reference Level specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-rf-vi.html language=enus -->
## TOPIC 00158: RFmxWCDMA Configure RF VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-rf-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-rf-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RF properties of the signal specified by the selector string. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (em

### RFmxWCDMA Configure RF VI

Configures the RF properties of the signal specified by the selector string.

[IMAGE alt='icon' src='rfmxwcdma-configure-rf-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the center frequency of the acquired RF signal for a single carrier. For multicarrier measurements, the Center Frequency parameter specifies the reference frequency for the values in the Carrier Freq property. This value is expressed in Hz. The default value of this parameter is hardware dependent. Reference Level — Reference Level specifies the reference level that represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. External Attenuation (dB) — External Attenuation specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. This value is expressed in dB. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-software-edge-trigger-vi.html language=enus -->
## TOPIC 00159: RFmxWCDMA Configure Software Edge Trigger VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-software-edge-trigger-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a software trigger and then marks a reference point within the record. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String specifies a selector str

### RFmxWCDMA Configure Software Edge Trigger VI

Configures the device to wait for a software trigger and then marks a reference point within the record.

[IMAGE alt='icon' src='rfmxwcdma-configure-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA Configure Trigger VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-trigger-vi.html language=enus -->
## TOPIC 00160: RFmxWCDMA Configure Trigger VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-trigger-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Trigger you use to acquire the signal. icon

### RFmxWCDMA Configure Trigger VI

Configures the Reference Trigger you use to acquire the signal.

[IMAGE alt='icon' src='rfmxwcdma-configure-trigger-vi.png']

- [RFmxWCDMA Disable Trigger VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-disable-trigger-vi.html) Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.
- [RFmxWCDMA Configure Digital Edge Trigger VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-digital-edge-trigger-vi.html) Configures the device to wait for a digital edge trigger and then marks a reference point within the record.
- [RFmxWCDMA Configure IQ Power Edge Trigger VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-iq-power-edge-trigger-vi.html) Configures the device to wait for the complex power of the I/Q data to cross the specified threshold and then marks a reference point within the record.
- [RFmxWCDMA Configure Software Edge Trigger VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-software-edge-trigger-vi.html) Configures the device to wait for a software trigger and then marks a reference point within the record.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-array-vi.html language=enus -->
## TOPIC 00161: RFmxWCDMA Configure Uplink Test Model (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the uplink test model for all the carriers. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example:

### RFmxWCDMA Configure Uplink Test Model (Array) VI

Configures the uplink test model for all the carriers.

[IMAGE alt='icon' src='rfmxwcdma-configure-uplink-test-model-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. UL Test Model — UL Test Model specifies the array of uplink test models when you set the Channel Configuration Mode property to Test Model. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<n>, where n is the oldest release number with a given set of channel configurations. The default value is R6 C.2.1. R6 C.2.1 (0) The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.2 (1) The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.3 (2) The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.4 (3) The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.5 (4) The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.10.1.4 Subtest1 (5) The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest2 (6) The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest3 (7) The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest4 (8) The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest5 (9) The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest6 (10) The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. R7 C.10.1.4 Subtest1 (11) The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest2 (12) The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest3 (13) The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest4 (14) The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest1 (15) The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest2 (16) The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest3 (17) The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest4 (18) The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest5 (19) The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. R8 C.11.1.3 Subtest1 (20) The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest2 (21) The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest3 (22) The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest4 (23) The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest5 (24) The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.4 Subtest1 (25) The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| R6 C.2.1 (0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.2 (1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.3 (2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.4 (3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.5 (4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.10.1.4 Subtest1 (5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest2 (6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest3 (7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest4 (8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest5 (9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest6 (10) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7 C.10.1.4 Subtest1 (11) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest2 (12) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest3 (13) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest4 (14) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest1 (15) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest2 (16) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest3 (17) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest4 (18) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest5 (19) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8 C.11.1.3 Subtest1 (20) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest2 (21) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest3 (22) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest4 (23) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest5 (24) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.4 Subtest1 (25) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |

Parent topic:

Array VIs

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-vi.html language=enus -->
## TOPIC 00162: RFmxWCDMA Configure Uplink Test Model VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-uplink-test-model-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the uplink test model. Use "carrier<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instanc

### RFmxWCDMA Configure Uplink Test Model VI

Configures the uplink test model.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxwcdma-configure-uplink-test-model-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. UL Test Model — UL Test Model specifies the uplink test model when you set the Channel Configuration Mode property to Test Model. Each test model is a set of channel configurations defined by the standard. Each uplink test model is a set of channel configurations as defined by the reference measurement channels in tables C.2.1, C.2.2, C.2.3, C.2.4, C.2.5, C.10.1.4, C.11.1.3, or C.11.1.4 of the 3GPP TS 34.121-1 specification. Released specifications from version 6.3.0, release 6 to version 11.5.0, release 11 are supported. Reference measurement channels in multiple releases of the specification can be the same. Each uplink test model name starts with R<n>, where n is the oldest release number with a given set of channel configurations. The default value is R6 C.2.1. R6 C.2.1 (0) The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.2 (1) The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.3 (2) The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.4 (3) The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.2.5 (4) The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. R6 C.10.1.4 Subtest1 (5) The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest2 (6) The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest3 (7) The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest4 (8) The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest5 (9) The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. R6 C.10.1.4 Subtest6 (10) The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. R7 C.10.1.4 Subtest1 (11) The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest2 (12) The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest3 (13) The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.10.1.4 Subtest4 (14) The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest1 (15) The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest2 (16) The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest3 (17) The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest4 (18) The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. R7 C.11.1.3 Subtest5 (19) The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. R8 C.11.1.3 Subtest1 (20) The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest2 (21) The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest3 (22) The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest4 (23) The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.3 Subtest5 (24) The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. R8 C.11.1.4 Subtest1 (25) The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| R6 C.2.1 (0) | The UL R6 C.2.1 configuration (12.2 kbps) is as defined in Annex C, section C.2.1 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.2 (1) | The UL R6 C.2.2 configuration (64 kbps) is as defined in Annex C, section C.2.2 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.3 (2) | The UL R6 C.2.3 configuration (144 kbps) is as defined in Annex C, section C.2.3 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.4 (3) | The UL R6 C.2.4 configuration (384 kbps) is as defined in Annex C, section C.2.4 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.2.5 (4) | The UL R6 C.2.5 configuration (768 kbps) is as defined in Annex C, section C.2.5 of the 3GPP TS 34.121 specification, version 6.3.0, release 6. |
| R6 C.10.1.4 Subtest1 (5) | The UL R6 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest2 (6) | The UL R6 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest3 (7) | The UL R6 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest4 (8) | The UL R6 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest5 (9) | The UL R6 C.10.1.4 Subtest5 is as defined in Annex C, table C.10.1.4 Sub-Test 5 of the 3GPP TS 34.121 specification, release 6. |
| R6 C.10.1.4 Subtest6 (10) | The UL R6 C.10.1.4 Subtest6 is as defined in Annex C, table C.10.1.4 Sub-Test 6 of the 3GPP TS 34.121 specification, release 6. |
| R7 C.10.1.4 Subtest1 (11) | The UL R7 C.10.1.4 Subtest1 is as defined in Annex C, table C.10.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest2 (12) | The UL R7 C.10.1.4 Subtest2 is as defined in Annex C, table C.10.1.4 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest3 (13) | The UL R7 C.10.1.4 Subtest3 is as defined in Annex C, table C.10.1.4 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.10.1.4 Subtest4 (14) | The UL R7 C.10.1.4 Subtest4 is as defined in Annex C, table C.10.1.4 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest1 (15) | The UL R7 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest2 (16) | The UL R7 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest3 (17) | The UL R7 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest4 (18) | The UL R7 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 7. |
| R7 C.11.1.3 Subtest5 (19) | The UL R7 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 7. |
| R8 C.11.1.3 Subtest1 (20) | The UL R8 C.11.1.3 Subtest1 is as defined in Annex C, table C.11.1.3 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest2 (21) | The UL R8 C.11.1.3 Subtest2 is as defined in Annex C, table C.11.1.3 Sub-Test 2 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest3 (22) | The UL R8 C.11.1.3 Subtest3 is as defined in Annex C, table C.11.1.3 Sub-Test 3 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest4 (23) | The UL R8 C.11.1.3 Subtest4 is as defined in Annex C, table C.11.1.3 Sub-Test 4 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.3 Subtest5 (24) | The UL R8 C.11.1.3 Subtest5 is as defined in Annex C, table C.11.1.3 Sub-Test 5 of the 3GPP TS 34.121-1 specification, release 8. |
| R8 C.11.1.4 Subtest1 (25) | The UL R8 C.11.1.4 Subtest1 is as defined in Annex C, table C.11.1.4 Sub-Test 1 of the 3GPP TS 34.121-1 specification, release 8. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-array-vi.html language=enus -->
## TOPIC 00163: RFmxWCDMA Configure User Defined Channel (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this VI, you must configure the Num Channels property with the appropriate number of user-defined channels. Use "carrier<n>" as the selector string to configure this

### RFmxWCDMA Configure User Defined Channel (Array) VI

Configures an array of spreading factors, spreading codes, modulation types, and branches of the user-defined channels. Before calling this VI, you must configure the [Num Channels](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr500014) property with the appropriate number of user-defined channels.

Use "carrier<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxwcdma-configure-user-defined-channel-array-vi.png']

#### Inputs/Outputs

| Branch — Branch specifies an array of branches on which the data is modulated in the channel. The default value is I. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. Selector String — Selector String specifies a selector string comprising of the signal name and carrier number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Spreading Factor — Spreading Factor specifies an array of spreading factor of the channels. The default value is 256. Valid values are 2, 4, 8,16, 32, 64, 128, and 256. Spreading Code — Spreading Code specifies an array of spreading code of the channels. The default value is 0. Valid values are 0 to (Spreading factor - 1). Modulation Type — Modulation Type specifies an array of modulation types of the channels. The default value is BPSK/QPSK. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4 PAM. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4 PAM. |

Parent topic:

Array VIs

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-vi.html language=enus -->
## TOPIC 00164: RFmxWCDMA Configure User Defined Channel VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-configure-user-defined-channel-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this VI, you must configure the Num Channels property with the appropriate number of channels. Use "carrier<k>/channel<n>" as the selector string to configure this VI. icon Input

### RFmxWCDMA Configure User Defined Channel VI

Configures the spreading factor, spreading code, modulation type, and branch of each user-defined channel. Before calling this VI, you must configure the [Num Channels](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr500014) property with the appropriate number of channels.

Use "carrier<*k*>/channel<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxwcdma-configure-user-defined-channel-vi.png']

#### Inputs/Outputs

| Branch — Branch specifies the branch on which the data is modulated. The default value is I. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. Selector String — Selector String specifies a selector string comprising of the signal name, carrier number, and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "carrier0/channel0". Example: "carrier0/channel0" "signal::sig1/carrier0/channel0" You can use the RFmxWCDMA Build Channel String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Spreading Factor — Spreading Factor specifies the spreading factor of the channel. The default value is 256. Valid values are 2, 4, 8, 16, 32, 64, 128, and 256. Spreading Code — Spreading Code specifies the spreading code of the channel. The default value is 0. Valid values are 0 to (Spreading factor - 1). Modulation Type — Modulation Type specifies the modulation type of the channel. The default value is BPSK/QPSK. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4 PAM. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4 PAM. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-create-signal-configuration-vi.html language=enus -->
## TOPIC 00165: RFmxWCDMA Create Signal Configuration VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-create-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-create-signal-configuration-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" cgenclassrntag.png Instrument Handle In Instrument Handle In specifi

### RFmxWCDMA Create Signal Configuration VI

Creates a new instance of a signal.

[IMAGE alt='icon' src='rfmxwcdma-create-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-delete-signal-configuration-vi.html language=enus -->
## TOPIC 00166: RFmxWCDMA Delete Signal Configuration VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-delete-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-delete-signal-configuration-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" cgenclassrntag.png Instru

### RFmxWCDMA Delete Signal Configuration VI

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='icon' src='rfmxwcdma-delete-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-disable-trigger-vi.html language=enus -->
## TOPIC 00167: RFmxWCDMA Disable Trigger VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-disable-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-disable-trigger-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name

### RFmxWCDMA Disable Trigger VI

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='icon' src='rfmxwcdma-disable-trigger-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA Configure Trigger VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-get-all-named-result-names-vi.html language=enus -->
## TOPIC 00168: RFmxWCDMA Get All Named Result Names VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-get-all-named-result-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-get-all-named-result-names-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the named result names of the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The defa

### RFmxWCDMA Get All Named Result Names VI

Returns the named result names of the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxwcdma-get-all-named-result-names-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Result Names — Result Names returns an array of result names. Default Result Exists? — Default Result Exists? indicates whether the default result exists. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-initiate-vi.html language=enus -->
## TOPIC 00169: RFmxWCDMA Initiate VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-initiate-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the RFmxWCDMA Pro

### RFmxWCDMA Initiate VI

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the RFmxWCDMA Property Node.

To get the status of measurements, use the [RFmxWCDMA Wait for Measurement Complete](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_wait_for_measurement_complete) VI or the [RFmxWCDMA Check Measurement Status](/csh?context=rfmxwcdma_rfmxwcdmavi_rfmxwcdma_check_measurement_status) VI.

[IMAGE alt='icon' src='rfmxwcdma-initiate-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1", to enable fetching multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

WCDMA

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-configure-reference-waveform-vi.html language=enus -->
## TOPIC 00170: RFmxWCDMA ModAcc Configure Reference Waveform VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-configure-reference-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-configure-reference-waveform-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster ModAcc measurements. This VI is used only when you set the ModAcc Sync Mode property to Marker. icon Inputs/Outputs cstr.png Selector String S

### RFmxWCDMA ModAcc Configure Reference Waveform VI

Configures the reference waveform such that it corresponds to the transmitted signal for the ModAcc measurement. This reference waveform helps achieve faster
ModAcc measurements.

This VI is used only when you set the [ModAcc Sync Mode](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr511002) property to **Marker**.

[IMAGE alt='icon' src='rfmxwcdma-modacc-configure-reference-waveform-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Waveform — Reference Waveform specifies the ideal complex baseband reference waveform. x0 — x0 specifies the start time. This value is expressed in seconds. dx — dx specifies the sample duration. This value is expressed in seconds. y — y specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time. This value is expressed in seconds. dx — dx specifies the sample duration. This value is expressed in seconds. y — y specifies an array of the normalized ideal complex baseband samples, corresponding to the acquired signal. This value is expressed in volts. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00171: RFmxWCDMA ModAcc Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxWCDMA ModAcc Configure Synchronization Mode and Interval VI

Configures the synchronization mode, measurement offset, and measurement length of the ModAcc measurement.

[IMAGE alt='icon' src='rfmxwcdma-modacc-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. — Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the symbol boundary. Marker (3) The measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the Trigger. This is the fastest way to do a ModAcc measurement. This mode requires the Trigger Type property to be set to Digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. Valid values are [0, (15 - ModAcc Measurement Length)]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15. Measurement Length (slots) — Measurement Length specifies the duration for the modulation accuracy measurement. This value is expressed in slots. The default value is 1. Valid values are [1,(15 - ModAcc Measurement Offset)]. The sum of the ModAcc measurement offset and ModAcc measurement length must be less than or equal to 15. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the symbol boundary. |
| Marker (3) | The measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the Trigger. This is the fastest way to do a ModAcc measurement. This mode requires the Trigger Type property to be set to Digital and the trigger must occur at the start of the frame. For more information about Marker mode, refer to Marker Mode. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-constellation-trace-vi.html language=enus -->
## TOPIC 00172: RFmxWCDMA ModAcc Fetch Constellation Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-constellation-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result na

### RFmxWCDMA ModAcc Fetch Constellation Trace VI

Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Constellation — Constellation returns an array of complex chips of the corrected signal of a carrier on which the ModAcc measurements are done. You can use these chips to obtain the constellation diagram. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-detected-channel-array-vi.html language=enus -->
## TOPIC 00173: RFmxWCDMA ModAcc Fetch Detected Channel (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-detected-channel-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-detected-channel-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the Channel Configuration Mode property to Auto Detect for the ModAcc measurement. When you set the Channel Configuration

### RFmxWCDMA ModAcc Fetch Detected Channel (Array) VI

Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the [Channel Configuration Mode](/csh?context=rfmxwcdma_rfmxwcdmaprop_attr500010) property to **Auto Detect** for the ModAcc measurement. When you set the Channel Configuration Mode property to **User Defined** or **Test Model**, it returns the corresponding results for the configured channels of all the carriers.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-detected-channel-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Detected Branch — Detected Branch returns an array of branches of the detected channels when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of branches of the configured channels. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature-phase branch. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Detected Spreading Factor — Detected Spreading Factor returns an array of spreading factors of the detected channels, when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of spreading factors of the configured channels. Detected Spreading Code — Detected Spreading Code returns an array of spreading codes of the detected channels, when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of spreading codes of the configured channels. Detected Mod Type — Detected Mod Type returns an array of modulation types of the detected channels, when you set the Channel Configuration Mode property to Auto Detect. If you set the Channel Configuration Mode property to User Defined or Test Model, the measurement returns an array of modulation types of the configured channels. BPSK/QPSK (0) The modulation type is BPSK. 4PAM/16QAM (1) The modulation type is 4-PAM. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature-phase branch. |
| BPSK/QPSK (0) | The modulation type is BPSK. |
| 4PAM/16QAM (1) | The modulation type is 4-PAM. |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-array-vi.html language=enus -->
## TOPIC 00174: RFmxWCDMA ModAcc Fetch EVM (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measureme

### RFmxWCDMA ModAcc Fetch EVM (Array) VI

Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measurement. The array elements represent the result of each carrier in the measurement.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-evm-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Chip Rate Error (ppm) — Chip Rate Error returns the array of chip rate errors of the composite signal corresponding to the carriers. This value is expressed in ppm. Frequency Error (Hz) — Frequency Error returns the array of frequency offset values of the composite signal corresponding to the carriers. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS EVM (%) — RMS EVM returns the array of RMS EVM values of the composite signal corresponding to the carriers. This value is expressed as a percentage. Peak EVM (%) — Peak EVM returns the array of peak EVM values of the composite signal corresponding to the carriers. This value is expressed as a percentage. Rho — Rho returns the array of correlation values of the received signal with the reference signal normalized by the signal power corresponding to the carriers. Valid values range from 0 to 1.0, inclusive. The maximum value of Rho is 1.0, which indicates that the received signal and reference signal are perfectly correlated. error out — error out contains error information. This output provides standard error out functionality. RMS Magnitude Error (%) — RMS Magnitude Error returns the array of RMS magnitude errors of the composite signal corresponding to the carriers. This value is expressed in percentage. RMS Phase Error (deg) — RMS Phase Error returns the array of RMS phase error values of the composite signal corresponding to the carriers. This value is expressed in degrees. |
| --- |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-trace-vi.html language=enus -->
## TOPIC 00175: RFmxWCDMA ModAcc Fetch EVM Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace of a carrier for the ModAcc measurement. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not

### RFmxWCDMA ModAcc Fetch EVM Trace VI

Fetches the EVM trace of a carrier for the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. EVM (%) — EVM returns the trace of error vector magnitude of the composite corrected signal. This value is expressed as a percentage. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the EVM value. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the EVM value. This value is expressed as a percentage. |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-vi.html language=enus -->
## TOPIC 00176: RFmxWCDMA ModAcc Fetch EVM VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip rate error, frequency error, RMS EVM, peak EVM, Rho, RMS magnitude error, and RMS phase error of the complex chips of the corrected composite signal for a carrier in the ModAcc measurement. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/Outputs cst

### RFmxWCDMA ModAcc Fetch EVM VI

Fetches the chip rate error, frequency error, RMS EVM, peak EVM, Rho, RMS magnitude error, and RMS phase error of the complex chips of the corrected composite signal for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Chip Rate Error (ppm) — Chip Rate Error returns the chip rate error of the composite signal for a carrier. This value is expressed in ppm. Frequency Error (Hz) — Frequency Error returns the frequency offset of the composite signal for a carrier. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS EVM (%) — RMS EVM returns the RMS EVM of the composite signal for a carrier. This value is expressed as a percentage. Peak EVM (%) — Peak EVM returns the peak EVM of the composite signal for a carrier. This value is expressed as a percentage. Rho — Rho returns the correlation of the received signal with the reference signal normalized by the signal power for a carrier. Valid values range from 0 to 1.0, inclusive. The maximum value of Rho is 1.0, which indicates that the received signal and reference signal are perfectly correlated. error out — error out contains error information. This output provides standard error out functionality. RMS Magnitude Error (%) — RMS Magnitude Error returns the RMS magnitude error of the composite signal for a carrier. This value is expressed in percentage. RMS Phase Error (deg) — RMS Phase Error returns the RMS phase error of the composite signal for a carrier. This value is expressed in degrees. |
| --- |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-array-vi.html language=enus -->
## TOPIC 00177: RFmxWCDMA ModAcc Fetch IQ Impairments (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement. icon Inputs/Outputs cstr.png Selector String Selector S

### RFmxWCDMA ModAcc Fetch IQ Impairments (Array) VI

Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-iq-impairments-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I/Q Origin Offset (dB) — I/Q Origin Offset returns the array of I/Q origin offset values of the composite signal. This value is expressed in dB. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. I/Q Gain Imbalance (dB) — I/Q Gain Imbalance returns the array of I/Q gain imbalance values of the composite signal. This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. I/Q Quadrature Error (deg) — I/Q Quadrature Error returns the array of I/Q quadrature error values of the composite signal. This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00178: RFmxWCDMA ModAcc Fetch IQ Impairments VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal

### RFmxWCDMA ModAcc Fetch IQ Impairments VI

Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I/Q Origin Offset (dB) — I/Q Origin Offset returns the I/Q origin offset of the composite signal of a carrier. This value is expressed in dB. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. I/Q Gain Imbalance (dB) — I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal of a carrier. This value is expressed in dB. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. I/Q Quadrature Error (deg) — I/Q Quadrature Error returns the I/Q quadrature error of the composite signal of a carrier. This value is expressed in degrees. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-array-vi.html language=enus -->
## TOPIC 00179: RFmxWCDMA ModAcc Fetch Peak CDE (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier. icon Inputs/Outputs cstr.png Selector String

### RFmxWCDMA ModAcc Fetch Peak CDE (Array) VI

Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-peak-cde-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Peak CDE (dB) — Peak CDE returns the array of maximum CDE values. This value is expressed in dB. The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used. The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code. Peak CDE Code — Peak CDE Code returns the array of spreading codes corresponding to the value of the Peak CDE parameter. Peak CDE Branch — Peak CDE Branch returns the array of branches of the channel corresponding to the value of the Peak CDE parameter. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-vi.html language=enus -->
## TOPIC 00180: RFmxWCDMA ModAcc Fetch Peak CDE VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/

### RFmxWCDMA ModAcc Fetch Peak CDE VI

Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-peak-cde-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak CDE Branch — Peak CDE Branch returns the branch of the channel corresponding to the value of the Peak CDE parameter for a carrier in the received signal. I (0) The signal is modulated in the in-phase branch. Q (1) The signal is modulated in the quadrature branch. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Peak CDE (dB) — Peak CDE returns the maximum CDE value for a carrier in the received signal. The CDEs are computed by despreading the descrambled error vector using a specific spreading factor. A fixed spreading factor of 4 is used. The CDE for every code with the specific spreading factor is defined as the ratio of the mean power of the descrambled and despread error vector to the mean power of the composite reference waveform. The CDEs for both I and Q branches are computed for each code. This value is expressed in dB. Peak CDE Code — Peak CDE Code returns the spreading code corresponding to the value of the Peak CDE parameter for a carrier in the received signal. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | The signal is modulated in the in-phase branch. |
| Q (1) | The signal is modulated in the quadrature branch. |

Parent topic:

RFmxWCDMA ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-vi.html language=enus -->
## TOPIC 00181: RFmxWCDMA ModAcc Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches results of the ModAcc measurement. icon

### RFmxWCDMA ModAcc Fetch VI

Fetches results of the ModAcc measurement.

[IMAGE alt='icon' src='rfmxwcdma-modacc-fetch-vi.png']

- [RFmxWCDMA ModAcc Fetch EVM VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-vi.html) Fetches the chip rate error, frequency error, RMS EVM, peak EVM, Rho, RMS magnitude error, and RMS phase error of the complex chips of the corrected composite signal for a carrier in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-vi.html) Fetches the I/Q origin offset, I/Q gain imbalance and I/Q quadrature error for a carrier in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Peak CDE VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-vi.html) Fetches the peak value among the code domain errors (CDEs) obtained with a fixed spreading factor of 4, along with the code number and branch that correspond to this peak value for a carrier in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Peak Active CDE VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-active-cde-vi.html) Fetches the peak value among the code domain errors (CDEs) of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch RCDE VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-rcde-vi.html) Returns the peak relative code domain error (RCDE) value of the active channels, along with the code number, spreading factor, and branch that correspond to this peak value for a carrier in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Number of Detected Channels VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-number-of-detected-channels-vi.html) Fetches the number of detected channels in a carrier for the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Detected Channel VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-detected-channel-vi.html) Returns the spreading factor, spreading code, modulation type, and branch of the detected channel of a carrier in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch EVM (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-array-vi.html) Fetches an array of chip rate errors, an array of frequency errors, an array of RMS EVMs, an array of peak EVMs, an array of Rhos, an array of RMS magnitude errors, and an array of RMS phase errors of the complex chips of the corrected signal corresponding to all the carriers in the ModAcc measurement. The array elements represent the result of each carrier in the measurement.
- [RFmxWCDMA ModAcc Fetch IQ Impairments (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-iq-impairments-array-vi.html) Fetches the array of I/Q origin offsets, an array of I/Q gain imbalances, and an array of I/Q quadrature errors corresponding to all the carriers in the ModAcc measurement. The array elements represent result of each carrier in the measurement.
- [RFmxWCDMA ModAcc Fetch Peak CDE (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-cde-array-vi.html) Fetches an array of peak CDE values obtained with a fixed spreading factor of 4 for all the carriers and the corresponding code numbers and branches. Each element in these arrays corresponds to the peak value among the code domain errors in each carrier.
- [RFmxWCDMA ModAcc Fetch Peak Active CDE (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-peak-active-cde-array-vi.html) Fetches arrays of peak CDE values among all the active channels of a carrier, and the corresponding code numbers, spreading factors, and branches of the carriers. Each element in these arrays corresponds to the peak value among the code domain errors of all the active channels in each carrier.
- [RFmxWCDMA ModAcc Fetch RCDE (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-rcde-array-vi.html) Fetches arrays of peak relative CDE values of the active channels, of the carriers and the corresponding code numbers, spreading factors, and branches. Each element in these arrays corresponds to the peak value among the relative code domain errors of all the active channels in each carrier.
- [RFmxWCDMA ModAcc Fetch Number of Detected Channels (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-number-of-detected-channels-array-vi.html) Fetches an array of number of detected channels of all the carriers in the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Detected Channel (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-detected-channel-array-vi.html) Fetches an array of spreading factors, an array of spreading codes, an array of modulation types, and an array of branches of the detected channels of the carriers, when you set the Channel Configuration Mode property to Auto Detect for the ModAcc measurement. When you set the Channel Configuration Mode property to User Defined or Test Model , it returns the corresponding results for the configured channels of all the carriers.
- [RFmxWCDMA ModAcc Fetch Multicarrier IQ Impairments VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-multicarrier-iq-impairments-vi.html) Fetches the I/Q impairments for a multicarrier signal.
- [RFmxWCDMA ModAcc Fetch EVM Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-evm-trace-vi.html) Fetches the EVM trace of a carrier for the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Magnitude Error Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-magnitude-error-trace-vi.html) Fetches the magnitude error trace of a carrier for the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Phase Error Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-phase-error-trace-vi.html) Fetches the phase error trace of a carrier for the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch RCDE Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-rcde-trace-vi.html) Fetches the relative code domain errors (RCDE) trace of a carrier for the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-constellation-trace-vi.html) Fetches the complex chips of the composite corrected signal of a carrier for the ModAcc measurement.
- [RFmxWCDMA ModAcc Fetch Reference Waveform VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-modacc-fetch-reference-waveform-vi.html) Fetches the reference waveform for the ModAcc measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-averaging-vi.html language=enus -->
## TOPIC 00182: RFmxWCDMA OBW Configure Averaging VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-averaging-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::

### RFmxWCDMA OBW Configure Averaging VI

Configures averaging for the OBW measurement.

[IMAGE alt='icon' src='rfmxwcdma-obw-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00183: RFmxWCDMA OBW Configure RBW Filter VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-rbw-filter-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use t

### RFmxWCDMA OBW Configure RBW Filter VI

Configures the RBW filter.

[IMAGE alt='icon' src='rfmxwcdma-obw-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. The default value is True. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. If you set the RBW Filter Type parameter to FFT Based, the measurement calculates the RBW regardless of the value of this parameter. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the RBW Auto parameter to False. This parameter is valid only if you set the RBW Filter Type parameter to Gaussian or Flat. This value is expressed in Hz. The default value is 30 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-sweep-time-vi.html language=enus -->
## TOPIC 00184: RFmxWCDMA OBW Configure Sweep Time VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-configure-sweep-time-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You

### RFmxWCDMA OBW Configure Sweep Time VI

Configures the sweep time interval.

[IMAGE alt='icon' src='rfmxwcdma-obw-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-measurement-vi.html language=enus -->
## TOPIC 00185: RFmxWCDMA OBW Fetch Measurement VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-measurement-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify th

### RFmxWCDMA OBW Fetch Measurement VI

Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power.

[IMAGE alt='icon' src='rfmxwcdma-obw-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Stop Frequency (Hz) — Stop Frequency returns the stop frequency of the Occupied Bandwidth parameter. Start Frequency (Hz) — Start Frequency returns the start frequency of the Occupied Bandwidth parameter. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Occupied Bandwidth (Hz) — Occupied Bandwidth returns the bandwidth containing 99% of the total integrated power of the acquired signal, around the center of the carriers. Absolute Power (dBm) — Absolute Power returns the carrier power integrated over a bandwidth of 5 MHz. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA OBW Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-spectrum-vi.html language=enus -->
## TOPIC 00186: RFmxWCDMA OBW Fetch Spectrum VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-spectrum-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxWCDMA OBW Fetch Spectrum VI

Fetches the spectrum used for the OBW measurement.

[IMAGE alt='icon' src='rfmxwcdma-obw-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power at each frequency bin. The value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power at each frequency bin. The value is expressed in dBm. |

Parent topic:

RFmxWCDMA OBW Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-vi.html language=enus -->
## TOPIC 00187: RFmxWCDMA OBW Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the OBW measurement results. icon

### RFmxWCDMA OBW Fetch VI

Fetches the OBW measurement results.

[IMAGE alt='icon' src='rfmxwcdma-obw-fetch-vi.png']

- [RFmxWCDMA OBW Fetch Measurement VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-measurement-vi.html) Fetches the absolute and relative powers of the carrier for the OBW measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA OBW Fetch Spectrum VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-obw-fetch-spectrum-vi.html) Fetches the spectrum used for the OBW measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-property-node-vi.html language=enus -->
## TOPIC 00188: RFmxWCDMA Property Node VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-property-node-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets (writes) or gets (reads) RFmxWCDMA properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png error in (no error) error in describe

### RFmxWCDMA Property Node VI

Sets (writes) or gets (reads) RFmxWCDMA properties.

[IMAGE alt='icon' src='rfmxwcdma-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx WCDMA Property Node is used to get (read), set (write), or reset (set to default value) RFmx WCDMA properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

WCDMA

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-configure-averaging-vi.html language=enus -->
## TOPIC 00189: RFmxWCDMA QEVM Configure Averaging VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-configure-averaging-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal:

### RFmxWCDMA QEVM Configure Averaging VI

Configures averaging for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the QEVM measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the QEVM measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the value of the Averaging Count parameter as the number of acquisitions over which the QEVM measurement is averaged. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-configure-measurement-length-vi.html language=enus -->
## TOPIC 00190: RFmxWCDMA QEVM Configure Measurement Length VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-configure-measurement-length-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-configure-measurement-length-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the measurement length of the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examp

### RFmxWCDMA QEVM Configure Measurement Length VI

Configures the measurement length of the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-configure-measurement-length-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Length (chips) — Measurement Length specifies the duration of the QEVM measurement. The value is expressed in chips. The default value is 2560. NI recommends that you set this property to n * 512, where the value of n can range from 1 to 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-constellation-trace-vi.html language=enus -->
## TOPIC 00191: RFmxWCDMA QEVM Fetch Constellation Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-constellation-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the complex chips of the composite corrected signal for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. Th

### RFmxWCDMA QEVM Fetch Constellation Trace VI

Fetches the complex chips of the composite corrected signal for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Constellation — Constellation returns an array of complex chips of the QPSK corrected signal for the last acquisition. You can use these chips to obtain the constellation diagram. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-trace-vi.html language=enus -->
## TOPIC 00192: RFmxWCDMA QEVM Fetch EVM Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EVM trace for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string).

### RFmxWCDMA QEVM Fetch EVM Trace VI

Fetches the EVM trace for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. EVM (%) — EVM returns the trace of error vector magnitude of the QPSK corrected signal for the last acquisition. This value is expressed as a percentage. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the EVM value. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the EVM value. This value is expressed as a percentage. |

Parent topic:

RFmxWCDMA QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-vi.html language=enus -->
## TOPIC 00193: RFmxWCDMA QEVM Fetch EVM VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprisin

### RFmxWCDMA QEVM Fetch EVM VI

Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Phase Error (deg) — Mean Phase Error returns the mean of the RMS phase error values for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS phase errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The phase error of a chip is the difference in the phases of the received chip and the ideal chip. The RMS phase error is obtained from all the chips in the measurement interval. Mean Magnitude Error (%) — Mean Magnitude Error returns the mean of RMS magnitude errors for a QPSK signal. This value is expressed as a percentage. This value is obtained by averaging the RMS magnitude errors over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The magnitude error of a chip is the difference in the magnitudes of the received chip and the ideal chip. The RMS magnitude error is obtained from all the chips in the measurement interval. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean RMS EVM (%) — Mean RMS EVM returns the mean of the RMS EVM values for a QPSK signal. This value is obtained by averaging the RMS EVMs over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. This value is expressed as a percentage. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The RMS EVM is obtained from all the chips in the measurement interval. Maximum Peak EVM (%) — Maximum Peak EVM returns the maximum value of the peak EVMs for a QPSK signal. This value is expressed as a percentage. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The EVM of a chip is the magnitude of the vector difference between the received chip and the ideal chip. The peak EVM is obtained from all the chips in the measurement interval. Mean Frequency Error (Hz) — Mean Frequency Error returns the mean of the frequency errors for a QPSK signal. This value is expressed in Hz. This value is obtained by the mean of frequency errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The frequency error is the estimated difference between the carrier frequency of the received signal and the ideal signal. error out — error out contains error information. This output provides standard error out functionality. Mean Chip Rate Error (ppm) — Mean Chip Rate Error returns the mean of the chip rate errors for a QPSK signal. This value is expressed in ppm. This value is obtained by averaging the chip rate errors over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The chip rate error is the estimated error between the chip clock rate of the transmitted signal and the chip clock rate at the receiver. |
| --- |

Parent topic:

RFmxWCDMA QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00194: RFmxWCDMA QEVM Fetch IQ Impairments VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-iq-impairments-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the mean and maximum I/Q origin offsets, I/Q gain imbalances, and I/Q quadrature errors for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the

### RFmxWCDMA QEVM Fetch IQ Impairments VI

Fetches the mean and maximum I/Q origin offsets, I/Q gain imbalances, and I/Q quadrature errors for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Maximum I/Q Gain Imbalance (dB) — Maximum I/Q Gain Imbalance returns the maximum value of I/Q gain imbalances for a QPSK signal. This value is expressed in dB. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. This result is for future use. Maximum I/Q Origin Offset (dB) — Maximum I/Q Origin Offset returns the maximum I/Q origin offset for a QPSK signal. This value is expressed in dB. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean I/Q Origin Offset (dB) — Mean I/Q Origin Offset returns the mean of I/Q origin offsets for a QPSK signal. This value is expressed in dB. This value is obtained by averaging the I/Q origin offsets over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The I/Q origin offset is a measure of the DC component present in the I/Q signal being measured. Mean I/Q Gain Imbalance (dB) — Mean I/Q Gain Imbalance returns the mean of the I/Q gain imbalances for a QPSK signal. This value is expressed in dB. This value is obtained by the I/Q gain imbalances obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. The I/Q gain imbalance is the ratio of the magnitude of the I component to the Q component of the I/Q signal being measured. This result is for future use. Mean I/Q Quadrature Error (deg) — Mean I/Q Quadrature Error returns the mean of the I/Q quadrature errors for a QPSK signal. This value is expressed in degrees. This value is obtained by the mean of I/Q quadrature errors obtained over all averaging acquisitions. The number of acquisitions is specified by the value of the QEVM Averaging Count property. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. This result is for future use. error out — error out contains error information. This output provides standard error out functionality. Maximum I/Q Quadrature Error (deg) — Maximum I/Q Quadrature Error returns the maximum value of I/Q quadrature errors for a QPSK signal. This value is expressed in degrees. This value is obtained over all averaging iterations. The number of acquisitions is specified by the value of the QEVM Averaging Count property. Quadrature error is a measure of the error in the phase between I and Q components of the signal being measured. This result is for future use. |
| --- |

Parent topic:

RFmxWCDMA QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00195: RFmxWCDMA QEVM Fetch Magnitude Error Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-magnitude-error-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error trace for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (emp

### RFmxWCDMA QEVM Fetch Magnitude Error Trace VI

Fetches the magnitude error trace for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Magnitude Error (%) — Magnitude Error returns the trace of the magnitude errors of the QPSK corrected signal for the last acquisition. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the magnitude error values. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the magnitude error values. This value is expressed as a percentage. |

Parent topic:

RFmxWCDMA QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-phase-error-trace-vi.html language=enus -->
## TOPIC 00196: RFmxWCDMA QEVM Fetch Phase Error Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-phase-error-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty s

### RFmxWCDMA QEVM Fetch Phase Error Trace VI

Fetches the phase error trace for the QEVM measurement.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Phase Error (deg) — Phase Error returns the trace of phase errors of the QPSK corrected signal for the last acquisition. This value is expressed in degrees. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns an array of phase error values. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns an array of phase error values. This value is expressed in degrees. |

Parent topic:

RFmxWCDMA QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-vi.html language=enus -->
## TOPIC 00197: RFmxWCDMA QEVM Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the QEVM measurement results. icon

### RFmxWCDMA QEVM Fetch VI

Fetches the QEVM measurement results.

[IMAGE alt='icon' src='rfmxwcdma-qevm-fetch-vi.png']

- [RFmxWCDMA QEVM Fetch EVM VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-vi.html) Fetches the mean chip rate error, mean frequency error, mean RMS EVM, maximum peak EVM, mean magnitude error, and mean phase error of the complex chips of the corrected signal for the QEVM measurement.
- [RFmxWCDMA QEVM Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-iq-impairments-vi.html) Fetches the mean and maximum I/Q origin offsets, I/Q gain imbalances, and I/Q quadrature errors for the QEVM measurement.
- [RFmxWCDMA QEVM Fetch EVM Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-evm-trace-vi.html) Fetches the EVM trace for the QEVM measurement.
- [RFmxWCDMA QEVM Fetch Magnitude Error Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-magnitude-error-trace-vi.html) Fetches the magnitude error trace for the QEVM measurement.
- [RFmxWCDMA QEVM Fetch Phase Error Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-phase-error-trace-vi.html) Fetches the phase error trace for the QEVM measurement.
- [RFmxWCDMA QEVM Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-qevm-fetch-constellation-trace-vi.html) Fetches the complex chips of the composite corrected signal for the QEVM measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-reset-to-default-vi.html language=enus -->
## TOPIC 00198: RFmxWCDMA Reset to Default VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-reset-to-default-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" Y

### RFmxWCDMA Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxwcdma-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00199: RFmxWCDMA Select Measurement (Multiple) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-multiple-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxWCDMA Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxwcdma-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurements — Measurements specifies the measurements to perform. You can specify one or more of the following measurements. The default is an empty array. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. QEVM (5) Enables the QEVM measurement. SlotPhase (6) Enables the SlotPhase measurement. CDA (7) Enables the CDA measurement. SlotPower (8) Enables the SlotPower measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurements. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| QEVM (5) | Enables the QEVM measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| CDA (7) | Enables the CDA measurement. |
| SlotPower (8) | Enables the SlotPower measurement. |

Parent topic:

RFmxWCDMA Select Measurement VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-single-vi.html language=enus -->
## TOPIC 00200: RFmxWCDMA Select Measurement (Single) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-single-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the measurement that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxWCDMA Select Measurement (Single) VI

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxwcdma-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement — Measurement specifies the measurement to perform. The default value is ModAcc. ModAcc (0) Enables the ModAcc measurement. ACP (1) Enables the ACP measurement. CHP (2) Enables the CHP measurement. OBW (3) Enables the OBW measurement. SEM (4) Enables the SEM measurement. QEVM (5) Enables the QEVM measurement. SlotPhase (6) Enables the SlotPhase measurement. CDA (7) Enables the CDA measurement. SlotPower (8) Enables the SlotPower measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the ModAcc measurement. |
| ACP (1) | Enables the ACP measurement. |
| CHP (2) | Enables the CHP measurement. |
| OBW (3) | Enables the OBW measurement. |
| SEM (4) | Enables the SEM measurement. |
| QEVM (5) | Enables the QEVM measurement. |
| SlotPhase (6) | Enables the SlotPhase measurement. |
| CDA (7) | Enables the CDA measurement. |
| SlotPower (8) | Enables the SlotPower measurement. |

Parent topic:

RFmxWCDMA Select Measurement VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-vi.html language=enus -->
## TOPIC 00201: RFmxWCDMA Select Measurement VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. icon

### RFmxWCDMA Select Measurement VI

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

[IMAGE alt='icon' src='rfmxwcdma-select-measurement-vi.png']

- [RFmxWCDMA Select Measurement (Single) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxWCDMA Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

WCDMA

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-configure-averaging-vi.html language=enus -->
## TOPIC 00202: RFmxWCDMA SEM Configure Averaging VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-configure-averaging-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::

### RFmxWCDMA SEM Configure Averaging VI

Configures averaging for the SEM measurement.

[IMAGE alt='icon' src='rfmxwcdma-sem-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging of the spectrum for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one record to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one record to the next. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the spectrum is averaged. |
| RMS (0) | The power spectrum is linearly averaged. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one record to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one record to the next. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-configure-sweep-time-vi.html language=enus -->
## TOPIC 00203: RFmxWCDMA SEM Configure Sweep Time VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-configure-sweep-time-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time interval. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You

### RFmxWCDMA SEM Configure Sweep Time VI

Configures the sweep time interval.

[IMAGE alt='icon' src='rfmxwcdma-sem-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. True (1) The measurement uses a sweep time value of one slot duration. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 666.66666700000007 microseconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify in the Sweep Time Interval parameter. |
| True (1) | The measurement uses a sweep time value of one slot duration. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-array-vi.html language=enus -->
## TOPIC 00204: RFmxWCDMA SEM Fetch Carrier Measurement (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of t

### RFmxWCDMA SEM Fetch Carrier Measurement (Array) VI

Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-carrier-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns an array of carrier power values. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns an array of carrier power values relative to the total carrier power of all enabled carriers. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-vi.html language=enus -->
## TOPIC 00205: RFmxWCDMA SEM Fetch Carrier Measurement VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power. Use "carrier<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector Strin

### RFmxWCDMA SEM Fetch Carrier Measurement VI

Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power.

Use "carrier<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-carrier-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and carrier number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "carrier0". Example: "carrier0" "signal::sig1/carrier0" "result::r1/carrier0" "signal::sig1/result::r1/carrier0" You can use the RFmxWCDMA Build Carrier String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the carrier power. The carrier power is the integrated power of the RRC-filtered signal. The RRC filter uses a bandwidth of 3.84 MHz with a roll-off factor of 0.22. The carrier is centered at a frequency determined by the Center Frequency and Carrier Freq properties. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the carrier power relative to the total carrier power property. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-array-vi.html language=enus -->
## TOPIC 00206: RFmxWCDMA SEM Fetch Lower Offset Margin (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total ca

### RFmxWCDMA SEM Fetch Lower Offset Margin (Array) VI

Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-lower-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns an array of powers at which the margins occurred in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns an array of powers at which the margins occurred in the lower, or negative, offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status indicates an array of measurement status values based on the values of the SEM Results Lower Offset Margin property corresponding to each lower offset segment. Margin (dB) — Margin returns an array of margins of the lower offset segments. This value is expressed in dB. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit, in the lower offset segment is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is the margin. Margin Frequency (Hz) — Margin Frequency returns an array of frequencies at which the margins occurred in the lower, or negative, offset segments This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-vi.html language=enus -->
## TOPIC 00207: RFmxWCDMA SEM Fetch Lower Offset Margin VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. Use "offset<n>" as the selector string to read results from this

### RFmxWCDMA SEM Fetch Lower Offset Margin VI

Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-lower-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power at which the margin occurred in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power at which the margin occurred in the lower, or negative, offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status indicates the measurement status based on the SEM Results Lower Offset Margin property. Margin (dB) — Margin returns the margin of the lower offset segment. This value is expressed in dB. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit in the lower offset segment is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the lower offset segment is the margin. Margin Frequency (Hz) — Margin Frequency returns the frequency at which the margin occurred in the lower, or negative, offset segment. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-array-vi.html language=enus -->
## TOPIC 00208: RFmxWCDMA SEM Fetch Lower Offset Power (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power. icon Inputs/Out

### RFmxWCDMA SEM Fetch Lower Offset Power (Array) VI

Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-lower-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns an array of peak power values measured in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns an array of frequencies corresponding to the lower offset segment peak power values. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns an array of the powers measured in the lower, or negative, offset segments. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns an array of powers measured in the lower, or negative, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns an array of peak power values measured in the lower, or negative, offset segments. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-vi.html language=enus -->
## TOPIC 00209: RFmxWCDMA SEM Fetch Lower Offset Power VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power. Use "offset<n>" as the selector string to read result

### RFmxWCDMA SEM Fetch Lower Offset Power VI

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-lower-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the peak power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns the frequency corresponding to the lower offset segment peak power. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the power measured in the lower, or negative, offset segment. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the power measured in the lower, or negative, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns the peak power measured in the lower, or negative, offset segment. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00210: RFmxWCDMA SEM Fetch Measurement Status VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-measurement-status-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the 3GPP TS 34.121-1 specification, version 11.5.0, release 11. icon Inputs/Outputs cstr.png Selector String Selector St

### RFmxWCDMA SEM Fetch Measurement Status VI

Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the *3GPP TS 34.121-1* specification, version 11.5.0, release 11.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status indicates the overall SEM measurement status based on the SEM Results Lower Offset Meas Status and the SEM Results Upper Offset Meas Status properties. Fail (0) The measurement status of at least one offset segment has failed. Pass (1) The measurement status of all offset segments have passed. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The measurement status of at least one offset segment has failed. |
| Pass (1) | The measurement status of all offset segments have passed. |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-spectrum-vi.html language=enus -->
## TOPIC 00211: RFmxWCDMA SEM Fetch Spectrum VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-spectrum-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxWCDMA SEM Fetch Spectrum VI

Fetches the spectrum used for the SEM measurement.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. Relative Mask (dB) — Relative Mask returns the trace of power levels representing the relative mask in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of power levels for relative mask. The value is expressed in dBm. Absolute Mask (dBm) — Absolute Mask returns the trace of power levels representing the absolute mask in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of power levels for absolute mask. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of averaged powers measured at each frequency bin. The value is expressed in dBm. |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of power levels for relative mask. The value is expressed in dBm. |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns an array of power levels for absolute mask. This value is expressed in dBm. |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-total-carrier-power-vi.html language=enus -->
## TOPIC 00212: RFmxWCDMA SEM Fetch Total Carrier Power VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-total-carrier-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-total-carrier-power-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the total carrier power for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxWCDMA SEM Fetch Total Carrier Power VI

Fetches the total carrier power for the SEM measurement.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-total-carrier-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Total Carrier Power (dBm) — Total Carrier Power returns the sum of all active carrier powers, where each carrier power corresponds to the value of the SEM Results Carrier Abs Pwr property. This value is expressed in dBm. For a single-carrier measurement, total carrier power is the same as carrier absolute power. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-array-vi.html language=enus -->
## TOPIC 00213: RFmxWCDMA SEM Fetch Upper Offset Margin (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relati

### RFmxWCDMA SEM Fetch Upper Offset Margin (Array) VI

Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-upper-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin property, relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns an array of powers at the frequency corresponding to the SEM Results Upper Offset Margin property. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns an array of measurement status values based on the values of the SEM Results Upper Offset Margin property corresponding to each upper offset segment. Margin (dB) — Margin returns an array of margins of the upper offset segments. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit, in the upper offset segment, is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is the margin. This value is expressed in dB. Margin Frequency (Hz) — Margin Frequency returns an array of frequencies corresponding to the SEM Results Upper Offset Margin property. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-vi.html language=enus -->
## TOPIC 00214: RFmxWCDMA SEM Fetch Upper Offset Margin VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power. Use "offset<n>" as the selector string to read results from this

### RFmxWCDMA SEM Fetch Upper Offset Margin VI

Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-upper-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power at which the margin occurred in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power at which the margin occurred in the upper, or positive, offset segment This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status Indicates the measurement status based on the SEM Results Upper Offset Margin property. Margin (dB) — Margin returns the margin of the upper offset segment. In a single carrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is measured. The maximum of the relative spectrum trace with reference to the standard-defined relative mask limit in the upper offset segment is also measured. The higher value is the margin. In a multicarrier SEM, the maximum of the absolute spectrum trace with reference to the standard-defined absolute mask limit in the upper offset segment is the margin. This value is expressed in dB. Margin Frequency (Hz) — Margin Frequency returns the frequency at which the margin occurred in the upper, or positive, segment. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-array-vi.html language=enus -->
## TOPIC 00215: RFmxWCDMA SEM Fetch Upper Offset Power (Array) VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-array-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. A

### RFmxWCDMA SEM Fetch Upper Offset Power (Array) VI

Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-upper-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns an array of peak power values measured in the upper, or positive, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns an array of frequencies at which the peak power is observed in the upper, or positive, offset segments. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns an array of the powers measured in the upper, or positive, offset segments. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns an array of powers measured in the upper, or positive, offset segments relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns an array of peak power values measured in the upper, or positive, offset segments. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-vi.html language=enus -->
## TOPIC 00216: RFmxWCDMA SEM Fetch Upper Offset Power VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power. Use "offset<n>" as the selector string to read results

### RFmxWCDMA SEM Fetch Upper Offset Power VI

Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power.

Use "offset<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-upper-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxWCDMA Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the peak power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Peak Frequency (Hz) — Peak Frequency returns the frequency corresponding to the upper offset segment peak power. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the power measured in the upper, or positive, offset segment. This value is expressed in dBm. Relative Integrated Power (dB) — Relative Integrated Power returns the power measured in the upper, or positive, offset segment relative to the SEM Results Total Carrier Pwr property. This value is expressed in dB. Absolute Peak Power (dBm) — Absolute Peak Power returns an array of peak power values measured in the lower, or negative, offset segments This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SEM Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-vi.html language=enus -->
## TOPIC 00217: RFmxWCDMA SEM Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SEM measurement results. icon

### RFmxWCDMA SEM Fetch VI

Fetches the SEM measurement results.

[IMAGE alt='icon' src='rfmxwcdma-sem-fetch-vi.png']

- [RFmxWCDMA SEM Fetch Measurement Status VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-measurement-status-vi.html) Fetches the overall SEM measurement status based on the measurement limits and failure criteria for each offset segment, as defined in sections 5.9 , 5.9A, 5.9B, 5.9C, and 5.9D of the 3GPP TS 34.121-1 specification, version 11.5.0, release 11.
- [RFmxWCDMA SEM Fetch Total Carrier Power VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-total-carrier-power-vi.html) Fetches the total carrier power for the SEM measurement.
- [RFmxWCDMA SEM Fetch Carrier Measurement VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-vi.html) Fetches the absolute integrated power and the relative integrated power of the carrier for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Carrier Measurement (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-carrier-measurement-array-vi.html) Fetches an array of absolute integrated powers and an array of the relative integrated powers of the carriers for the SEM measurement. The relative powers are relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Lower Offset Power VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-vi.html) Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the lower offset segment for the SEM measurement. All relative powers are relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Lower Offset Power (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-power-array-vi.html) Fetches an array of the absolute integrated powers, the relative integrated powers, the absolute peak powers, the relative peak powers, and frequencies at absolute peak powers of lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Upper Offset Power VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-vi.html) Fetches the integrated absolute and relative powers, absolute and relative peak powers, and the frequency at the absolute peak power of the upper offset segment for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Upper Offset Power (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-power-array-vi.html) Returns an array of the absolute integrated powers and an array of the relative integrated powers, an array of the absolute peak powers and an array of the relative peak powers, and an array of the frequencies corresponding to peak absolute powers for upper offset segments for the SEM measurement. All relative powers are relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Lower Offset Margin VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-vi.html) Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Lower Offset Margin (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-lower-offset-margin-array-vi.html) Fetches an array of measurement status values, an array of margins, an array of frequencies at the margins, an array of the absolute powers, and an array of the relative powers at the margin frequencies for lower offset segments for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Upper Offset Margin VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-vi.html) Fetches the measurement status, margin, frequency at the margin, and the absolute and relative powers at the margin frequency for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Upper Offset Margin (Array) VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-upper-offset-margin-array-vi.html) Fetches an array of measurement status values, an array of margin values, an array of frequencies at the margins, an array of the absolute power values, and an array of the relative power values at the margin frequencies for upper offset segments for the SEM measurement. The relative power is relative to the total carrier power.
- [RFmxWCDMA SEM Fetch Spectrum VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-sem-fetch-spectrum-vi.html) Fetches the spectrum used for the SEM measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00218: RFmxWCDMA Send Software Edge Trigger VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-send-software-edge-trigger-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxWCDMA Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure a

### RFmxWCDMA Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxWCDMA Configure Trigger](/csh?topicname=rfmxwcdma-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxWCDMA Initiate VI.

[IMAGE alt='icon' src='rfmxwcdma-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00219: RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal inst

### RFmxWCDMA SlotPhase Configure Synchronization Mode and Interval VI

Configures the synchronization mode, the measurement offset, and the measurement length of the SlotPhase measurement.

[IMAGE alt='icon' src='rfmxwcdma-slotphase-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame or the slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. The valid values are any value greater than or equal to 0. Measurement Length (slots) — Measurement Length specifies the duration of the SlotPhase measurement. This value is expressed in slots. The default value is 15. The valid values are any value greater than or equal to 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter starting at Measurement Offset slots from the slot boundary. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html language=enus -->
## TOPIC 00220: RFmxWCDMA SlotPhase Fetch Chip Phase Error Linear Fit Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error linear fit trace for the SlotPhase measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do n

### RFmxWCDMA SlotPhase Fetch Chip Phase Error Linear Fit Trace VI

Fetches the chip phase error linear fit trace for the SlotPhase measurement.

[IMAGE alt='icon' src='rfmxwcdma-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Chip Phase Error Linear Fit (deg) — Chip Phase Error Linear Fit returns the linear-fit of the chip phase error after excluding 25 micro seconds at the start and end of each slot. The linear-fit is then extrapolated to the nearest slot boundaries on either side. The exclusion and extrapolation can be disabled if you set the SlotPhase Transient Removal Enabled property to False. Note This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling property and the RfmxInstr Frequency Settling Units property, to allow more time for the LO to settle. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the linear-fit chip phase error values. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the linear-fit chip phase error values. This value is expressed in degrees. |

Parent topic:

RFmxWCDMA SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-trace-vi.html language=enus -->
## TOPIC 00221: RFmxWCDMA SlotPhase Fetch Chip Phase Error Trace VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-trace-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace for the SlotPhase measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify

### RFmxWCDMA SlotPhase Fetch Chip Phase Error Trace VI

Fetches the chip phase error trace for the SlotPhase measurement.

[IMAGE alt='icon' src='rfmxwcdma-slotphase-fetch-chip-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Chip Phase Error (deg) — Chip Phase Error returns the chip phase error. The chip phase error is the difference in phase between the test waveform and the reference waveform for every chip. Note This trace can get affected by the LO settling time of the hardware. You can use the RfmxInstr Frequency Settling property and the RfmxInstr Frequency Settling Units property, to allow more time for the LO to settle. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns an array of phase error values. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns an array of phase error values. This value is expressed in degrees. |

Parent topic:

RFmxWCDMA SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-measurement-vi.html language=enus -->
## TOPIC 00222: RFmxWCDMA SlotPhase Fetch Measurement VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-measurement-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result n

### RFmxWCDMA SlotPhase Fetch Measurement VI

Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results.

[IMAGE alt='icon' src='rfmxwcdma-slotphase-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Discontinuity Minimum Distance (slots) — Discontinuity Minimum Distance returns the minimum distance between two phase discontinuity measurements exceeding the Limit 1 value. Limit 1 is fixed at 36 degrees. This value is expressed in slots. If there are no phase discontinuity values greater than Limit 1, or if there is only one phase discontinuity value greater than Limit 1, this result is not valid. In such a case, -1 is reported as the result. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Maximum Phase Discontinuity (deg) — Maximum Phase Discontinuity returns the maximum of all the measured phase discontinuity values at the slot boundaries. This value is expressed in degrees. Discontinuity Count > Limit 1 — Discontinuity Count > Limit 1 returns the number of times the phase discontinuity values exceed the Limit 1 value for the acquired signal. Limit 1 is fixed at 36 degrees. Discontinuity Count > Limit 2 — Discontinuity Count > Limit 2 returns the number of times the phase discontinuity values exceed the Limit 2 value for the acquired signal. Limit 2 is fixed at 66 degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-phase-discontinuities-vi.html language=enus -->
## TOPIC 00223: RFmxWCDMA SlotPhase Fetch Phase Discontinuities VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-phase-discontinuities-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-phase-discontinuities-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase discontinuity values for the slot phase measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value

### RFmxWCDMA SlotPhase Fetch Phase Discontinuities VI

Fetches the phase discontinuity values for the slot phase measurement.

[IMAGE alt='icon' src='rfmxwcdma-slotphase-fetch-phase-discontinuities-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Slot Phase Discontinuity (deg) — Slot Phase Discontinuity returns the difference between the first extrapolated linear chip phase of the current slot and the last extrapolated linear chip phase of the preceding slot. The extrapolation is for the exclusion period of 25us on either side of the slot boundary. If you set the SlotPhase Transient Removal Enabled property to False, this parameter returns the difference between the first and last linear chip phase, at each slot boundary. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-vi.html language=enus -->
## TOPIC 00224: RFmxWCDMA SlotPhase Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SlotPhase measurement results. icon

### RFmxWCDMA SlotPhase Fetch VI

Fetches the SlotPhase measurement results.

[IMAGE alt='icon' src='rfmxwcdma-slotphase-fetch-vi.png']

- [RFmxWCDMA SlotPhase Fetch Measurement VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-measurement-vi.html) Fetches the maximum phase discontinuity, discontinuity count greater than Limit 1, discontinuity count greater than Limit 2, and discontinuity minimum distance results.
- [RFmxWCDMA SlotPhase Fetch Phase Discontinuities VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-phase-discontinuities-vi.html) Fetches the phase discontinuity values for the slot phase measurement.
- [RFmxWCDMA SlotPhase Fetch Chip Phase Error Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-trace-vi.html) Fetches the chip phase error trace for the SlotPhase measurement.
- [RFmxWCDMA SlotPhase Fetch Chip Phase Error Linear Fit Trace VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html) Fetches the chip phase error linear fit trace for the SlotPhase measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00225: RFmxWCDMA SlotPower Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, measurement offset, and measurement length. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is ""

### RFmxWCDMA SlotPower Configure Synchronization Mode and Interval VI

Configures the synchronization mode, measurement offset, and measurement length.

[IMAGE alt='icon' src='rfmxwcdma-slotpower-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "signal::sig1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame or slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length property starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. The valid values are any value greater than or equal to 0. Measurement Length (slots) — Measurement Length specifies the duration of the SlotPower measurement. This value is expressed in slots. The default value is 15. The valid values are any value greater than or equal to 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length property starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |

Parent topic:

SlotPower

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-powers-vi.html language=enus -->
## TOPIC 00226: RFmxWCDMA SlotPower Fetch Powers VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-powers-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-powers-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Slot Power and Slot Power delta for all the slots in the measurement length. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxWCDMA SlotPower Fetch Powers VI

Fetches the Slot Power and Slot Power delta for all the slots in the measurement length.

[IMAGE alt='icon' src='rfmxwcdma-slotpower-fetch-powers-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Slot Power (dBm) — Slot Power returns an array of slot powers. This value is expressed in dBm. Slot Power Delta (dB) — Slot Power Delta returns an array of differences in powers between the adjacent slots. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxWCDMA SlotPower Fetch VI

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-vi.html language=enus -->
## TOPIC 00227: RFmxWCDMA SlotPower Fetch VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SlotPower measurement results. icon

### RFmxWCDMA SlotPower Fetch VI

Fetches the SlotPower measurement results.

[IMAGE alt='icon' src='rfmxwcdma-slotpower-fetch-vi.png']

- [RFmxWCDMA SlotPower Fetch Powers VI](../../../../../vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-slotpower-fetch-powers-vi.html) Fetches the Slot Power and Slot Power delta for all the slots in the measurement length.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00228: RFmxWCDMA Wait for Measurement Complete VI

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/rfmxwcdma-wait-for-measurement-complete-vi.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number of seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxWCDMA Wait for Measurement Complete VI

Waits for the specified number of seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxwcdma-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxWCDMA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00229: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxwcdma-labview-api-ref`
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

<!--NI_TOPIC bundle=rfmxwcdma-labview-api-ref path=vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00230: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxwcdma-labview-api-ref`
- source_path: `vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxwcdma-labview-api-ref/raw/resource/enus/vi-lib/rfmx/wcdma/mx/rfmxwcdma-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxwcdma-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node. Standard err

### Using the Standard Functionality for error out Parameters

Many LabVIEW nodes such as VIs contain an error out parameter you can use to manage errors. These parameters typically provide the same, standard functionality. When a node exhibits different parameter functionality, the exceptions are documented in the reference material for that node.

Standard error out functionality is as follows:

|  | error out contains error information. If error in indicates that an error occurred before this VI ran, error out contains the same error information. Otherwise, it describes the error status that this VI or function produces. Right-click the error out front panel indicator and select Explain Error from the shortcut menu for more information about the error. |
| --- | --- |

error out contains the following cluster elements:

|  | status is TRUE (X) if an error occurred before this node ran or during the running of this node or FALSE (checkmark) to indicate a warning or that no error occurred before this node ran or during the running of this node. |
| --- | --- |
|  | code is the error or warning code. If status is TRUE, code is an error code. If status is FALSE, code is 0 or a warning code. |
|  | source specifies the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. |
