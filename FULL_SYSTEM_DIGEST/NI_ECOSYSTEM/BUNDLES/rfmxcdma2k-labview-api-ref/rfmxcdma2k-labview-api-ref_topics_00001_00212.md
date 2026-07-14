# NI DOCUMENT BUNDLE: rfmxcdma2k-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxcdma2k-labview-api-ref start=1 end=212 -->
<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/configuration/dir-mnu.html language=enus -->
## TOPIC 00001: Configuration

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/configuration/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/configuration/dir-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure RFmx CDMA2k measurements. You can use the RFmxCDMA2k Property Node to configure additional properties. icon

### Configuration

Use the VIs on this palette to configure RFmx CDMA2k measurements. You can use the [RFmxCDMA2k Property Node](/csh?topicname=rfmxcdma2k-property-node-vi.html) to configure additional properties.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxCDMA2k Configure RF VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-rf-vi.html) Configures the RF properties of the signal specified by the Selector String parameter.
- [RFmxCDMA2k Configure Frequency VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-vi.html) Configures the center frequency of the RF signal to acquire according to the Center Frequency value in Hz or according to the Channel Number and Band Class values. The signal analyzer tunes to this frequency.
- [RFmxCDMA2k Configure Reference Level VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-reference-level-vi.html) Configures the reference level. The reference level represents the maximum expected power of an input RF signal.
- [RFmxCDMA2k Auto Level VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-auto-level-vi.html) Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to calculate an approximate setting for the reference level.
- [RFmxCDMA2k Configure External Attenuation VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-external-attenuation-vi.html) Specifies any external attenuation to be considered by RFmx CDMA2k measurements, such as the attenuation of a switch or cable connected to the signal analyzer RF IN connector.
- [RFmxCDMA2k Configure Trigger VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-trigger-vi.html) Configures the Reference Trigger the signal analyzer uses to acquire the signal.
- [RFmxCDMA2k Send Software Edge Trigger VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-send-software-edge-trigger-vi.html) Sends a trigger to the device when you use the RFmxCDMA2k Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.
- [RFmxCDMA2k Configure Channel Configuration Mode VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-channel-configuration-mode-vi.html) Configures RFmx CDMA2k to detect the channels automatically or to use a specified channel configuration.
- [RFmxCDMA2k Configure Band Class VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-band-class-vi.html) Configures the band class used for the measurement.
- [RFmxCDMA2k Configure Number of Channels VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-number-of-channels-vi.html) Configures the number of channels for the user-defined channel configuration when you set the Channel Configuration Mode property to User Defined .
- [RFmxCDMA2k Configure User Defined Channel VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-vi.html) Configures an individual user-defined channel when the channel configuration mode is set to User Defined .
- [RFmxCDMA2k Configure User Defined Channel (Array) VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-array-vi.html) Configures all user-defined channels when you set the Channel Configuration Mode property to User Defined .
- [RFmxCDMA2k Configure Uplink Spreading VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-uplink-spreading-vi.html) Configures the scrambling code used for the uplink transmission.
- [RFmxCDMA2k Configure Radio Configuration VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-radio-configuration-vi.html) Configures the radio configuration of the CDMA2k signal.
- [RFmxCDMA2k Build Signal String VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-signal-string-vi.html) Creates a selector string to use with configuration or fetch properties and VIs.
- [RFmxCDMA2k Build Channel String VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-channel-string-vi.html) Creates a selector string to use with channel configuration.
- [ModAcc](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-modacc-mnu.html) Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [ACP](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-acp-mnu.html) Use the VIs on this palette to configure ACP measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [CHP](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-chp-mnu.html) Use the VIs on this palette to configure CHP measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [OBW](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-obw-mnu.html) Use the VIs on this palette to configure OBW measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [SEM](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-sem-mnu.html) Use the VIs on this palette to configure SEM measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [QEVM](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-qevm-mnu.html) Use the VIs on this palette to configure QEVM measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [CDA](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-cda-mnu.html) Use the VIs on this palette to configure CDA measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [SlotPhase](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotphase-mnu.html) Use the VIs on this palette to configure SlotPhase measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [SlotPower](../../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotpower-mnu.html) Use the VIs on this palette to configure SlotPower measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.

Parent topic:

CDMA2k

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-cda-mnu.html language=enus -->
## TOPIC 00002: CDA

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-cda-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-cda-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure CDA measurements. You can use the RFmxCDMA2k Property Node to configure additional properties. icon

### CDA

Use the VIs on this palette to configure CDA measurements. You can use the [RFmxCDMA2k Property Node](/csh?topicname=rfmxcdma2k-property-node-vi.html) to configure additional properties.

[IMAGE alt='icon' src='rfmx-cdma2k-mx-configuration-cda-mnu.png']

- [RFmxCDMA2k CDA Configure Power Unit VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-power-unit-vi.html) Configures the Power Unit parameter for the code domain power results, except for the Total Power parameter.
- [RFmxCDMA2k CDA Configure Synchronization Mode and Interval VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-synchronization-mode-and-interval-vi.html) Configures the Synchronization Mode , Measurement Offset , and Measurement Length parameters for the code domain analysis (CDA) measurement.
- [RFmxCDMA2k CDA Configure Measurement Channel VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-measurement-channel-vi.html) Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-modacc-mnu.html language=enus -->
## TOPIC 00003: ModAcc

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-modacc-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-modacc-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can use the RFmxCDMA2k Property Node to configure additional properties. icon

### ModAcc

Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. You can use the [RFmxCDMA2k Property Node](/csh?topicname=rfmxcdma2k-property-node-vi.html) to configure additional properties.

[IMAGE alt='icon' src='rfmx-cdma2k-mx-configuration-modacc-mnu.png']

- [RFmxCDMA2k ModAcc Configure Synchronization Mode and Interval VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-configure-synchronization-mode-and-interval-vi.html) Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotphase-mnu.html language=enus -->
## TOPIC 00004: SlotPhase

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotphase-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotphase-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure SlotPhase measurements. You can use the RFmxCDMA2k Property Node to configure additional properties. icon

### SlotPhase

Use the VIs on this palette to configure SlotPhase measurements. You can use the [RFmxCDMA2k Property Node](/csh?topicname=rfmxcdma2k-property-node-vi.html) to configure additional properties.

[IMAGE alt='icon' src='rfmx-cdma2k-mx-configuration-slotphase-mnu.png']

- [RFmxCDMA2k SlotPhase Configure Synchronization Mode and Interval VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-configure-synchronization-mode-and-interval-vi.html) Configures the Synchronization Mode , Measurement Offset , and Measurement Length parameters of the SlotPhase measurement.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotpower-mnu.html language=enus -->
## TOPIC 00005: SlotPower

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotpower-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/configuration/rfmx-cdma2k-mx-configuration-slotpower-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure SlotPower measurements. You can use the RFmxCDMA2k Property Node to configure additional properties. icon

### SlotPower

Use the VIs on this palette to configure SlotPower measurements. You can use the [RFmxCDMA2k Property Node](/csh?topicname=rfmxcdma2k-property-node-vi.html) to configure additional properties.

[IMAGE alt='icon' src='rfmx-cdma2k-mx-configuration-slotpower-mnu.png']

- [RFmxCDMA2k SlotPower Configure Synchronization Mode and Interval VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotpower-configure-synchronization-mode-and-interval-vi.html) Configures the Synchronization Mode , Measurement Offset , and Measurement Length parameters for the SlotPower measurement.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/dir-mnu.html language=enus -->
## TOPIC 00006: CDMA2k

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/dir-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to perform CDMA2k measurements. You can use the RFmxCDMA2k Property Node to configure additional properties. © 2015–2026 National Instruments Corporation. All rights reserved. icon

### CDMA2k

Use the VIs on this palette to perform CDMA2k measurements. You can use the [RFmxCDMA2k Property Node](/csh?topicname=rfmxcdma2k-property-node-vi.html) to configure additional properties.

© 2015–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [Configuration](../../../../../menus/categories/measurement/rfmx/cdma2k/configuration/dir-mnu.html) Use the VIs on this palette to configure RFmx CDMA2k measurements. You can use the RFmxCDMA2k Property Node to configure additional properties.
- [RFmxCDMA2k Select Measurement VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-select-measurement-vi.html) Specifies the measurements that you want to enable. To enable multiple measurements, use the Multiple Measurements instance. To enable a single measurement, use the Single Measurement instance.
- [RFmxCDMA2k Initiate VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-initiate-vi.html) Initiates all enabled measurements. Call this VI after configuring the signal and measurement.
- [Fetch](../../../../../menus/categories/measurement/rfmx/cdma2k/rfmx-cdma2k-mx-fetch-mnu.html) Use the VIs on this palette to fetch measurement results and traces.
- [Utility](../../../../../menus/categories/measurement/rfmx/cdma2k/utility/dir-mnu.html) Use the VIs on this palette to configure RFmx CDMA2k utilities.
- [RFmxCDMA2k Property Node VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-property-node-vi.html) Gets (reads), sets (writes), or resets (sets to default value) RFmxCDMA2k properties.
- [Advanced](../../../../../menus/categories/measurement/rfmx/cdma2k/rfmx-cdma2k-mx-advanced-mnu.html) Use the VIs on this palette to use advanced features.
- [Build String](../../../../../menus/categories/measurement/rfmx/cdma2k/utility/rfmx-cdma2k-mx-utility-build-string-mnu.html) Use the VIs on this palette to create selector strings for configurations and results that require a selector string.

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/rfmx-cdma2k-mx-advanced-mnu.html language=enus -->
## TOPIC 00007: Advanced

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/rfmx-cdma2k-mx-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/rfmx-cdma2k-mx-advanced-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. icon

### Advanced

Use the VIs on this palette to use advanced features.

[IMAGE alt='icon' src='rfmx-cdma2k-mx-advanced-mnu.png']

- [RFmxCDMA2k Abort Measurements VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-abort-measurements-vi.html) Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. The acquisition and measurements were previously initiated by the RFmxCDMA2k Initiate VI or measurement read VIs.
- [RFmxCDMA2k Analyze2 VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze2-vi.html) Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.
- [RFmxCDMA2k Create Signal Configuration VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-create-signal-configuration-vi.html) Creates a new instance of a signal.
- [RFmxCDMA2k Clone Signal Configuration VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clone-signal-configuration-vi.html) Creates a new instance of a signal by copying all the property values from an existing signal instance.
- [RFmxCDMA2k Delete Signal Configuration VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-delete-signal-configuration-vi.html) Deletes an instance of a signal that you specify in the Signal Name parameter.
- [RFmxCDMA2k Get All Named Result Names VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-get-all-named-result-names-vi.html) Returns the named result names of the signal that you specify in the Selector String parameter.
- [RFmxCDMA2k Clear Named Result VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-named-result-vi.html) Clears a result instance specified by the result name in the Selector String parameter.
- [RFmxCDMA2k Clear All Named Results VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-all-named-results-vi.html) Clears all results for the signal that you specify in the Selector String parameter.

Parent topic:

CDMA2k

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/utility/dir-mnu.html language=enus -->
## TOPIC 00008: Utility

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/utility/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/utility/dir-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure RFmx CDMA2k utilities. icon

### Utility

Use the VIs on this palette to configure RFmx CDMA2k utilities.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxCDMA2k Commit VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-commit-vi.html) Commits settings to the hardware. Calling this VI is optional. RFmxCDMA2k commits settings to the hardware when you call the RFmxCDMA2k Initiate VI.
- [RFmxCDMA2k Reset to Default VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-reset-to-default-vi.html) Resets a signal configuration to the default values.
- [RFmxCDMA2k Wait for Measurement Complete VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-wait-for-measurement-complete-vi.html) Waits for the specified number of seconds for all the measurements to complete.
- [RFmxCDMA2k Check Measurement Status VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-check-measurement-status-vi.html) Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

Parent topic:

CDMA2k

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=menus/categories/measurement/rfmx/cdma2k/utility/rfmx-cdma2k-mx-utility-build-string-mnu.html language=enus -->
## TOPIC 00009: Build String

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/cdma2k/utility/rfmx-cdma2k-mx-utility-build-string-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/cdma2k/utility/rfmx-cdma2k-mx-utility-build-string-mnu.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to create selector strings for configurations and results that require a selector string. icon

### Build String

Use the VIs on this palette to create selector strings for configurations and results that require a selector string.

[IMAGE alt='icon' src='rfmx-cdma2k-mx-utility-build-string-mnu.png']

- [RFmxCDMA2k Build Offset String VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-offset-string-vi.html) Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch properties and VIs.
- [RFmxCDMA2k Build Signal String VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-signal-string-vi.html) Creates a selector string to use with configuration or fetch properties and VIs.
- [RFmxCDMA2k Build Channel String VI](../../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-channel-string-vi.html) Creates a selector string to use with channel configuration.

Parent topic:

Fetch

Parent topic:

CDMA2k

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k-p.html language=enus -->
## TOPIC 00010: RFmxCDMA2k Properties

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k-p.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k-p.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RFmxCDMA2k properties to access options for configuring and fetching measurements. © 2015–2026 National Instruments Corporation. All rights reserved.

### RFmxCDMA2k Properties

Use the RFmxCDMA2k properties to access options for configuring and fetching measurements.

© 2015–2026 National Instruments Corporation. All rights reserved.

- [ACP:Advanced:Far IF Output Power Offset (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601036.html) Specifies the offset by which to adjust the IF output power level for offset channels that are far from the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False .
- [ACP:Advanced:IF Output Power Offset Auto](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601034.html) Specifies whether the measurement computes an IF output power level offset for the offset channels to improve the dynamic range of the ACP measurement. This property is used only if you set the ACP Meas Method property to Dynamic Range .
- [ACP:Advanced:Near IF Output Power Offset (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601035.html) Specifies the offset by which to adjust the IF output power level for offset channels that are near the carrier channel to improve the dynamic range. This value is expressed in dB. This property is used only if you set the ACP Meas Method property to Dynamic Range and set the ACP IF Output Power Offset Auto property to False .
- [ACP:Advanced:Sequential FFT Size](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601038.html) Specifies the FFT size, when you set the ACP Meas Method property to Sequential FFT .
- [ACP:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601021.html) Specifies whether to enable the traces to be stored and retrieved after performing the ACP measurement.
- [ACP:Averaging:Count](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601015.html) Specifies the number of acquisitions used for averaging when you set the ACP Averaging Enabled property to True .
- [ACP:Averaging:Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601016.html) Specifies whether to enable averaging for the ACP measurement.
- [ACP:Averaging:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601018.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.
- [ACP:Carrier:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601005.html) Returns the ACP carrier integration bandwidth. This value is expressed in Hz.
- [ACP:FFT:Overlap (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60103a.html) Returns the number of samples to overlap between consecutive chunks while performing FFT.
- [ACP:FFT:Overlap Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601039.html) Specifies how the FFT overlap is applied to the acquired samples.
- [ACP:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601000.html) Specifies whether to enable the ACP measurement.
- [ACP:Measurement Method](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601012.html) Specifies the method for performing the ACP measurement.
- [ACP:Noise Compensation Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601020.html) Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.
- [ACP:Number of Analysis Threads](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601014.html) Specifies the maximum number of threads used for parallelism for the ACP measurement.
- [ACP:Offset:Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100a.html) Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz.
- [ACP:Offset:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100e.html) Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.
- [ACP:Offset:Number of Offsets](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601008.html) Specifies the number of offset channels.
- [ACP:RBW Filter:Auto Bandwidth](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101b.html) Specifies whether the measurement computes the RBW.
- [ACP:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101c.html) Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the ACP RBW Auto property to False . This value is expressed in Hz.
- [ACP:RBW Filter:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101d.html) Specifies the shape of the digital RBW filter.
- [ACP:Results:Carrier:Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601026.html) Returns the absolute measured carrier power. This value is expressed in dBm.
- [ACP:Results:Lower Offset:Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60102c.html) Returns the absolute measured lower offset channel power. This value is expressed in dBm.
- [ACP:Results:Lower Offset:Relative Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60102d.html) Returns the lower offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB.
- [ACP:Results:Upper Offset:Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601032.html) Returns the absolute measured upper offset channel power. This value is expressed in dBm.
- [ACP:Results:Upper Offset:Relative Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601033.html) Returns the upper offset channel power measured relative to the carrier absolute integrated power. This value is expressed in dB.
- [ACP:Sweep Time:Auto](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101e.html) Specifies whether the measurement computes the sweep time.
- [ACP:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101f.html) Specifies the sweep time when you set the ACP Sweep Time Auto property to False . This value is expressed in seconds.
- [Advanced:Auto Level Initial Reference Level (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60d000.html) Specifies the initial reference level that the RFmxCDMA2k Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm.
- [Advanced:Limited Configuration Change](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60d003.html) Specifies the set of properties that are considered by RFmx in the locked signal configuration state.
- [Band Class](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600010.html) Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0.
- [CDA:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300f.html) Specifies whether to enable the traces to be stored and retrieved after performing the code domain analysis (CDA).
- [CDA:Base Spreading Factor](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613005.html) Specifies the base spreading factor used to calculate the code domain power traces.
- [CDA:IQ Gain Imbalance Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300c.html) Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.
- [CDA:IQ Offset Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300b.html) Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement.
- [CDA:IQ Quadrature Error Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300d.html) Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.
- [CDA:Measurement Channel:Branch](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613008.html) Specifies the branch of a channel subject to channel specific analysis.
- [CDA:Measurement Channel:Walsh Code Length](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613006.html) Specifies the Walsh code length of a channel subject to channel specific analysis.
- [CDA:Measurement Channel:Walsh Code Number](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613007.html) Specifies the Walsh code number of a channel subject to channel specific analysis.
- [CDA:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613000.html) Specifies whether to enable the code domain analysis (CDA) measurement.
- [CDA:Measurement Length (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613004.html) Specifies the duration of code domain measurement. This value is expressed in slots.
- [CDA:Measurement Offset (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613003.html) Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the CDA Sync Mode property. This value is expressed in slots.
- [CDA:Power Unit](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613009.html) Specifies the measurement unit of the measured code domain power results.
- [CDA:Receive Filter Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300e.html) Specifies whether to enable the received filter for the code domain analysis (CDA) measurement. Use this property to disable the filter, if the received signal is already filtered.
- [CDA:Results:Chip Rate Error (ppm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613026.html) Returns the chip rate error. This value is expressed in parts per million (ppm).
- [CDA:Results:Frequency Error (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613025.html) Returns the frequency error. This value is expressed in Hz.
- [CDA:Results:I Mean Active Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301d.html) Returns the average power of all active code channels measured on the I-branch. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:I Peak Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301e.html) Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:I/Q Gain Imbalance (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613023.html) Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.
- [CDA:Results:I/Q Origin Offset (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613022.html) Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB.
- [CDA:Results:I/Q Quadrature Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613024.html) Returns the I/Q quadrature error of the composite signal averaged over all measured slots. This value is expressed in degrees.
- [CDA:Results:Mean Active Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613019.html) Returns the average power of all active code channels. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:Mean Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301b.html) Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:Mean Pilot Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613021.html) Returns the mean power of the R-PICH.
- [CDA:Results:Mean Symbol Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613016.html) Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the CDA Pwr Unit property to dB , and in dBm, when you set the CDA Pwr Unit property to dBm .
- [CDA:Results:Peak Active Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301a.html) Returns the maximum power among all active code channels. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:Peak Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301c.html) Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:Peak Symbol EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613013.html) Returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage.
- [CDA:Results:Q Mean Active Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301f.html) Returns the average power of all active code channels measured on the Q-branch. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:Q Peak Inactive Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613020.html) Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:RMS Symbol EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613012.html) Returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage.
- [CDA:Results:RMS Symbol Magnitude Error (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613014.html) Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage.
- [CDA:Results:RMS Symbol Phase Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613015.html) Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees.
- [CDA:Results:Total Active Power (dB or dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613018.html) Returns the sum of the powers of all active code channels. If you set the CDA Pwr Unit property to dBm , this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property.
- [CDA:Results:Total Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613017.html) Returns the mean power of the received signal. This value is expressed in dBm.
- [CDA:Spectrum Inverted](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300a.html) Specifies whether the spectrum of the signal is inverted.
- [CDA:Synchronization Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613002.html) Specifies whether the measurement is performed from the frame, slot, or symbol boundary.
- [CHP:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603014.html) Specifies whether to enable the traces to be stored and retrieved after performing the CHP measurement.
- [CHP:Averaging:Count](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603006.html) Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True .
- [CHP:Averaging:Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603007.html) Specifies whether to enable averaging for the CHP measurement.
- [CHP:Averaging:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603009.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement.
- [CHP:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603002.html) Returns the CHP carrier integration bandwidth. This value is expressed in Hz.
- [CHP:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603000.html) Specifies whether to enable the CHP measurement.
- [CHP:Number of Analysis Threads](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603003.html) Specifies the maximum number of threads used for parallelism for the CHP measurement.
- [CHP:RBW Filter:Auto Bandwidth](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60300c.html) Specifies whether the measurement computes the RBW.
- [CHP:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60300d.html) Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the CHP RBW Auto property to False . This value is expressed in Hz.
- [CHP:RBW Filter:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60300e.html) Specifies the shape of the digital RBW filter.
- [CHP:Results:Carrier:Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603015.html) Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.
- [CHP:Sweep Time:Auto](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603011.html) Specifies whether the measurement computes the sweep time.
- [CHP:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603012.html) Specifies the sweep time when you set the CHP Sweep Time Auto property to False . This value is expressed in seconds.
- [Center Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600001.html) Specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz.
- [Channel:Configuration Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600012.html) Specifies whether to detect the channels automatically or to use a specified channel configuration.
- [Channel:User Defined:Branch](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600019.html) Specifies the branch on which a specific user-defined channel is mapped. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Channel:User Defined:Number of Channels](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600016.html) Specifies the number of user-defined channels. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Channel:User Defined:Walsh Code Length](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600017.html) Specifies the Walsh code length of a specific user-defined channel. This value is expressed in chips. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [Channel:User Defined:Walsh Code Number](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600018.html) Specifies the Walsh code number of a specific user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined .
- [External Attenuation (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600003.html) Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help .
- [Link Direction](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000d.html) Specifies the link direction of the received signal.
- [ModAcc:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611015.html) Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.
- [ModAcc:IQ Gain Imbalance Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr6110a1.html) Specifies whether to remove the I/Q gain imbalance before an EVM measurement.
- [ModAcc:IQ Offset Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611008.html) Specifies whether to remove the I/Q offset before an EVM measurement.
- [ModAcc:IQ Quadrature Error Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr6110a2.html) Specifies whether to remove the I/Q quadrature error before an EVM measurement.
- [ModAcc:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611000.html) Specifies whether to enable the modulation accuracy (ModAcc) measurement.
- [ModAcc:Measurement Length (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611007.html) Specifies the duration of the modulation accuracy (ModAcc) measurement. This value is expressed in slots.
- [ModAcc:Measurement Offset (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611006.html) Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the ModAcc Sync Mode property. This value is expressed in slots.
- [ModAcc:Multi Carrier Filter:Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611010.html) Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers.
- [ModAcc:Receive Filter Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr6110a3.html) Specifies whether to enable the received filter for the ModAcc measurement. For RC1/2, this property refers to the band-limiting filter specified in the Chapter 6.4.2.1 of 3GPP2 C.S0011-E . For RC3/4, this property refers to the complementary filter specified in the Chapter 6.4.2.2 of 3GPP2 C.S0011-E .
- [ModAcc:Results:Chip Rate Error (ppm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611033.html) Returns the chip rate error. This value is expressed in parts per million (ppm).
- [ModAcc:Results:Detected Channel:Branch](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611037.html) Returns the branch of the detected channel. If you set the Channel Configuration Mode property to User Defined , the property returns the branch of the configured channel.
- [ModAcc:Results:Detected Channel:Number of Detected Channels](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611034.html) Returns the total number of detected channels. If you set the Channel Configuration Mode property to User Defined , the property returns the number of configured channels.
- [ModAcc:Results:Detected Channel:Walsh Code Length](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611035.html) Returns the Walsh code length of the detected channel. If you set the Channel Configuration Mode property to User Defined , the property returns the Walsh code length of the configured channel.
- [ModAcc:Results:Detected Channel:Walsh Code Number](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611036.html) Returns the Walsh code number of the detected channel. If you set the Channel Configuration Mode property to User Defined , the property returns the Walsh code number of the configured channel.
- [ModAcc:Results:Frequency Error (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611027.html) Returns the frequency error averaged over all measured slots. This value is expressed in Hz.
- [ModAcc:Results:I/Q Gain Imbalance (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611025.html) Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.
- [ModAcc:Results:I/Q Origin Offset (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611024.html) Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB.
- [ModAcc:Results:I/Q Quadrature Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611026.html) Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.
- [ModAcc:Results:Peak Active CDE (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61102c.html) Returns the maximum value among the code domain errors (CDEs) for all active channels. This value is expressed in dB. The active CDEs are computed by projecting the descrambled error vector onto the codes of each active channel. The active CDE is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform.
- [ModAcc:Results:Peak Active CDE Branch](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611039.html) Returns the branch of the channel corresponding to the value that the ModAcc Results Pk Active CDE property returns.
- [ModAcc:Results:Peak Active CDE Walsh Code Length](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61102d.html) Returns the Walsh code length of the channel corresponding to the value that the ModAcc Results Pk Active CDE property returns.
- [ModAcc:Results:Peak Active CDE Walsh Code Number](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61102f.html) Returns the Walsh code number of the channel corresponding to the value that the ModAcc Results Pk Active CDE property returns.
- [ModAcc:Results:Peak CDE (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611029.html) Returns the maximum value among the code domain errors (CDEs). This value is expressed in dB. The CDEs are computed by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 16 is used. The CDEs are computed separately for I and Q branches.
- [ModAcc:Results:Peak CDE Branch](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611038.html) Returns the branch corresponding to the value that the ModAcc Results Pk CDE property returns.
- [ModAcc:Results:Peak CDE Walsh Code Number](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61102b.html) Returns the Walsh code number corresponding to the value that the ModAcc Results Pk CDE property returns.
- [ModAcc:Results:Peak EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611021.html) Returns the peak EVM of the composite signal. This value is expressed as a percentage.
- [ModAcc:Results:RMS EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611020.html) Returns the RMS EVM of the composite signal. This value is expressed as a percentage.
- [ModAcc:Results:RMS Magnitude Error (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611022.html) Returns the RMS magnitude error of the composite signal. This value is expressed as a percentage.
- [ModAcc:Results:RMS Phase Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611023.html) Returns the RMS phase error of the composite signal. This value is expressed in degrees.
- [ModAcc:Results:Rho](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611028.html) Returns the correlation of the received signal with the reference signal normalized by the signal power. The value of Rho is between 0 and 1.0, inclusive. A value of 1.0 indicates that the received signal and the reference signal are perfectly correlated.
- [ModAcc:Results:Slot Timing Error (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611030.html) Returns the measured timing error from the beginning of the acquisition to the location of the first slot acquired. This value is expressed in seconds.
- [ModAcc:Spectrum Inverted](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611009.html) Specifies whether the spectrum of the signal is inverted.
- [ModAcc:Synchronization Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611005.html) Specifies whether the measurement is performed from the frame, slot, or symbol boundary.
- [OBW:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606012.html) Specifies whether to enable the traces to be stored and retrieved after performing the OBW.
- [OBW:Averaging:Count](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606006.html) Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True .
- [OBW:Averaging:Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606007.html) Specifies whether to enable averaging for the OBW measurement.
- [OBW:Averaging:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606009.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the OBW measurement.
- [OBW:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606000.html) Specifies whether to enable the OBW measurement.
- [OBW:Number of Analysis Threads](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606003.html) Specifies the maximum number of threads used for parallelism for the OBW measurement.
- [OBW:RBW Filter:Auto Bandwidth](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600c.html) Specifies whether the measurement computes the RBW.
- [OBW:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600d.html) Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the OBW RBW Auto property to False . This value is expressed in Hz.
- [OBW:RBW Filter:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600e.html) Specifies the shape of the digital RBW filter.
- [OBW:Results:Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606014.html) Returns the absolute power measured in the OBW. This value is expressed in dBm.
- [OBW:Results:Occupied Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606013.html) Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz.
- [OBW:Results:Start Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606015.html) Returns the start frequency of the OBW. This value is expressed in Hz.
- [OBW:Results:Stop Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606016.html) Returns the stop frequency of the OBW. This value is expressed in Hz.
- [OBW:Span (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606004.html) Returns the frequency span of the OBW measurement. This value is expressed in Hz.
- [OBW:Sweep Time:Auto](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600f.html) Specifies whether the measurement computes the sweep time.
- [OBW:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606010.html) Specifies the sweep time when you set the OBW Sweep Time Auto property to False . This value is expressed in seconds.
- [QEVM:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200a.html) Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement.
- [QEVM:Averaging:Count](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612004.html) Specifies the number of measurements used for averaging when you set the QEVM Averaging Enabled property to True .
- [QEVM:Averaging:Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612003.html) Specifies whether to enable averaging for the QEVM measurement.
- [QEVM:IQ Gain Imbalance Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612007.html) Specifies whether to remove I/Q gain imbalance before QEVM measurement.
- [QEVM:IQ Offset Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612006.html) Specifies whether to remove I/Q offset before QEVM measurement.
- [QEVM:IQ Quadrature Error Removal Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612008.html) Specifies whether to remove I/Q quadrature error before QEVM measurement.
- [QEVM:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612000.html) Specifies whether to enable the QEVM measurement.
- [QEVM:Measurement Length (chips)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612002.html) Specifies the number of chips used for a single measurement.
- [QEVM:Number of Analysis Threads](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200b.html) Specifies the maximum number of threads used for parallelism for the QEVM measurement.
- [QEVM:Receive Filter Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612009.html) Specifies whether to enable the received filter for the QEVM measurement.
- [QEVM:Results:Maximum Chip Rate Error (ppm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201e.html) Returns the maximum chip rate error. This value is expressed in parts per million (ppm).
- [QEVM:Results:Maximum Frequency Error (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612016.html) Returns the maximum frequency error of the received signal. This value is expressed in Hz.
- [QEVM:Results:Maximum I/Q Gain Imbalance (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201a.html) Returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB.
- [QEVM:Results:Maximum I/Q Origin Offset (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612018.html) Returns the maximum origin offset of the received signal. This value is expressed in dB.
- [QEVM:Results:Maximum I/Q Quadrature Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201c.html) Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.
- [QEVM:Results:Maximum Magnitude Error (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612012.html) Returns the maximum magnitude error of the received signal. This value is expressed as a percentage.
- [QEVM:Results:Maximum Peak EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612010.html) Returns the maximum peak EVM of the received signal. This value is expressed as a percentage.
- [QEVM:Results:Maximum Phase Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612014.html) Returns the maximum phase error of the received signal. This value is expressed in degrees.
- [QEVM:Results:Maximum RMS EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200e.html) Returns the maximum RMS EVM of the received signal. This value is expressed as a percentage.
- [QEVM:Results:Mean Chip Rate Error (ppm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201d.html) Returns the mean chip rate error. This value is expressed in parts per million (ppm).
- [QEVM:Results:Mean Frequency Error (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612015.html) Returns the mean averaged frequency error of the received signal. This value is expressed in Hz.
- [QEVM:Results:Mean I/Q Gain Imbalance (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612019.html) Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB.
- [QEVM:Results:Mean I/Q Origin Offset (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612017.html) Returns the mean averaged origin offset of the received signal. This value is expressed in dB.
- [QEVM:Results:Mean I/Q Quadrature Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201b.html) Returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.
- [QEVM:Results:Mean Magnitude Error (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612011.html) Returns the mean averaged magnitude error of the received signal. This value is expressed as a percentage.
- [QEVM:Results:Mean Peak EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200f.html) Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage.
- [QEVM:Results:Mean Phase Error (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612013.html) Returns the mean averaged phase error of the received signal. This value is expressed in degrees.
- [QEVM:Results:Mean RMS EVM (%)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200d.html) Returns the mean averaged RMS EVM of the received signal. This value is expressed as a percentage.
- [QEVM:Spectrum Inverted](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612005.html) Specifies whether the spectrum of the signal is inverted.
- [Radio Configuration](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600011.html) Specifies the radio configuration for the channel.
- [Reference Level](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600002.html) Specifies the reference level, which represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.
- [Reference Level Headroom](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600ffc.html) Specifies the margin RFmx adds to the Reference Level property. The margin avoids clipping and overflow warnings if the input signal exceeds the configured reference level.
- [Result Fetch Timeout (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60c000.html) Specifies the time to wait before results are available in the RFmxCDMA2k Property Node . This value is expressed in seconds.
- [SEM:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608027.html) Specifies whether to enable the traces to be stored and retrieved after performing the SEM measurement.
- [SEM:Averaging:Count](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60801e.html) Specifies the number of acquisitions used for averaging when you set the SEM Averaging Enabled property to True .
- [SEM:Averaging:Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60801f.html) Specifies whether to enable averaging for the SEM measurement.
- [SEM:Averaging:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608021.html) Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the SEM measurement.
- [SEM:Carrier:Integration Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608005.html) Returns the SEM carrier integration bandwidth. This value is expressed in Hz.
- [SEM:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608000.html) Specifies whether to enable the SEM measurement.
- [SEM:Number of Analysis Threads](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60801d.html) Specifies the maximum number of threads used for parallelism for the SEM measurement.
- [SEM:Offset:Bandwidth Integral](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60800c.html) Returns the bandwidth integral for a specific offset segment.
- [SEM:Offset:Number of Offsets](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60800b.html) Returns the number of SEM offset segments.
- [SEM:Offset:RBW Filter:Bandwidth (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608017.html) Returns the bandwidth of the RBW filter used to sweep the offset segment. This value is expressed in Hz.
- [SEM:Offset:RBW Filter:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608018.html) Returns the type of RBW filter used to sweep the offset segment.
- [SEM:Offset:Start Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608014.html) Returns the start frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.
- [SEM:Offset:Stop Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608015.html) Returns the stop frequency of an SEM offset segment relative to the carrier frequency. This value is expressed in Hz.
- [SEM:Results:Carrier:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60802d.html) Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608034.html) Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608036.html) Returns the peak power measured in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Margin (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608039.html) Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask, which can be absolute or relative.
- [SEM:Results:Lower Offset:Margin Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803a.html) Returns the absolute power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm.
- [SEM:Results:Lower Offset:Margin Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803c.html) Returns the frequency at which the margin occurred in the lower (negative) offset segment. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Margin Relative Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803b.html) Returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.
- [SEM:Results:Lower Offset:Measurement Status](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803d.html) Indicates the lower offset segment measurement status based on measurement limits specified by the standard.
- [SEM:Results:Lower Offset:Peak Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608038.html) Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.
- [SEM:Results:Lower Offset:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608035.html) Returns the power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.
- [SEM:Results:Lower Offset:Relative Peak Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608037.html) Returns the peak power measured in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.
- [SEM:Results:Measurement Status](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608029.html) Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.
- [SEM:Results:Upper Offset:Absolute Integrated Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608041.html) Returns the power measured in the upper (positive) offset segment. This value is expressed in dB.
- [SEM:Results:Upper Offset:Absolute Peak Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608043.html) Returns the peak power measured in the upper (positive) offset segment. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Margin (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608046.html) Returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative).
- [SEM:Results:Upper Offset:Margin Absolute Power (dBm)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608047.html) Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Margin Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608049.html) Returns the frequency at which the margin occurred in the upper (positive) offset. This value is expressed in Hz.
- [SEM:Results:Upper Offset:Margin Relative Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608048.html) Returns the power at which the margin occurred in the upper (positive) offset segment. This value is expressed in dBm.
- [SEM:Results:Upper Offset:Measurement Status](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60804a.html) Indicates the upper offset measurement status based on measurement limits set by the standard.
- [SEM:Results:Upper Offset:Peak Frequency (Hz)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608045.html) Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.
- [SEM:Results:Upper Offset:Relative Integrated Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608042.html) Returns the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.
- [SEM:Results:Upper Offset:Relative Peak Power (dB)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608044.html) Returns the peak power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.
- [SEM:Sweep Time:Auto](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608025.html) Specifies whether the measurement computes the sweep time.
- [SEM:Sweep Time:Interval (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608026.html) Specifies the sweep time when you set the SEM Sweep Time Auto property to False . This value is expressed in seconds.
- [Selected Ports](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600ffd.html) Specifies the instrument port to be configured to acquire a signal. Use RFmxInstr Get Available Ports VI to get the valid port names.
- [Selector String](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600000.html) Specifies the selector strings used to access all subsequent properties in this instance of the property node.
- [SlotPhase:All Traces Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615008.html) Specifies whether to enable the traces to be stored and retrieved after performing the SlotPhase measurement.
- [SlotPhase:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615000.html) Specifies whether to enable the SlotPhase measurement.
- [SlotPhase:Measurement Length (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615004.html) Specifies the duration of the SlotPhase measurement. This value is expressed in slots.
- [SlotPhase:Measurement Offset (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615003.html) Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SlotPhase Sync Mode property. This value is expressed in slots.
- [SlotPhase:Receive Filter Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615006.html) Specifies whether to enable the received filter for the SlotPhase measurement. Use this property to disable the filter, if the received signal is already filtered.
- [SlotPhase:Results:Maximum Phase Discontinuity (deg)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61500b.html) Returns the maximum slot phase discontinuity value observed in the measurement interval. This value is expressed in degrees.
- [SlotPhase:Spectrum Inverted](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615005.html) Specifies whether the spectrum of the signal is inverted.
- [SlotPhase:Synchronization Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615002.html) Specifies whether the measurement is performed from the frame or slot boundary.
- [SlotPhase:Transient Duration (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615007.html) Specifies the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds.
- [SlotPower:Measurement Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614000.html) Specifies whether to enable the SlotPower measurement.
- [SlotPower:Measurement Length (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614004.html) Specifies the duration of the SlotPower measurement. This value is expressed in slots.
- [SlotPower:Measurement Offset (slots)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614003.html) Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SlotPower Sync Mode property. This value is expressed in slots.
- [SlotPower:Receive Filter Enabled](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614006.html) Specifies whether to enable the received filter for the SlotPower measurement. Use this property to disable the filter, if the received signal is already filtered.
- [SlotPower:Spectrum Inverted](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614005.html) Specifies whether the spectrum of the signal is inverted.
- [SlotPower:Synchronization Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614002.html) Specifies whether the measurement is performed from the frame or slot boundary.
- [Spreading:Downlink:PN Offset (64 chips)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600020.html) Specified the PN offset in increments of 64 chips for forward link.
- [Spreading:Uplink:Long Code Mask](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60001e.html) Specifies the long code mask for reverse link spreading.
- [Trigger:Delay (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000a.html) Specifies the trigger delay time. This value is expressed in seconds.
- [Trigger:Digital Edge:Edge](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600006.html) Specifies the active edge for the trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600005.html) Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:IQ Power Edge:Level](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600008.html) Specifies the power level at which the device triggers. This value is expressed in dB when the IQ Power Edge Level Type property is set to Relative and in dBm when the IQ Power Edge Level Type property is set to Absolute . The device asserts the trigger when the signal exceeds the level specified by the value of this property, taking into consideration the specified slope. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Level Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600fff.html) Specifies the reference for the IQ Power Edge Level Type property. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Slope](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600009.html) Specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:IQ Power Edge:Source](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600007.html) Specifies the channel from which the device monitors the trigger. This property is used only when you set the Trigger Type property to IQ Power Edge .
- [Trigger:Minimum Quiet Time:Duration (s)](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000c.html) Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.
- [Trigger:Minimum Quiet Time:Mode](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000b.html) Specifies whether the measurement computes the minimum quiet time used for triggering.
- [Trigger:Type](../../../resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600004.html) Specifies the trigger type.

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600004.html language=enus -->
## TOPIC 00011: Trigger:Type

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600004.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k Configure Trigger |
| Resettable | Yes |

| None | 0 | No Reference Trigger is configured. |
| --- | --- | --- |
| Digital Edge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Source property. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600005.html language=enus -->
## TOPIC 00012: Trigger:Digital Edge:Source

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600005.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informat

### Trigger:Digital Edge:Source

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](/csh?topicname=attr600004.html) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Trigger |
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

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000b.html language=enus -->
## TOPIC 00013: Trigger:Minimum Quiet Time:Mode

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000b.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k Configure Trigger |
| Resettable | Yes |

| Manual | 0 | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- | --- |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000c.html language=enus -->
## TOPIC 00014: Trigger:Minimum Quiet Time:Duration (s)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope

### Trigger:Minimum Quiet Time:Duration (s)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

If you set the [IQ Power Edge Slope](attr600009.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Min Quiet Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Trigger |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000d.html language=enus -->
## TOPIC 00015: Link Direction

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60000d.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | N/A |
| Resettable | Yes |

| Downlink | 0 | CDMA2k measurement uses 3GPP CDMA2k forward link direction also known as downlink direction to measure the received signal. |
| --- | --- | --- |
| Uplink | 1 | CDMA2k measurement uses 3GPP CDMA2k reverse link direction also known as uplink direction to measure the received signal. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600010.html language=enus -->
## TOPIC 00016: Band Class

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600010.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for i

### Band Class

Specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5- Band Class List, of the 3GPP2 C.S0057-F specification v1.0.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **0**. Valid values are 0 to 12, 14 and 15.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Band Class |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Band Class |
| Resettable | Yes |

| 0 | 0 | Specifies the 800 MHz cellular band. |
| --- | --- | --- |
| 1 | 1 | Specifies the 1.8 GHz to 2.0 GHz PCS band. |
| 2 | 2 | Specifies the 872 MHz to 960 MHz TACS band. |
| 3 | 3 | Specifies the 832 MHz to 925 MHZ JTACS band. |
| 4 | 4 | Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. |
| 5 | 5 | Specifies the 450 MHz NMT band. |
| 6 | 6 | Specifies the 2 GHz IMT-2000 band. |
| 7 | 7 | Specifies the upper 700 MHz PARMR band. |
| 8 | 8 | Specifies the 1,800 MHz to 2 GHz band. |
| 9 | 9 | Specifies the 900 MHz band. |
| 10 | 10 | Specifies the secondary 1,800 MHz band. |
| 11 | 11 | Specifies the 400 MHz European PAMR band. |
| 12 | 12 | Specifies the 800 MHz PAMR band. |
| 14 | 14 | Specifies the US PCS 1.9 GHz band. |
| 15 | 15 | Specifies the AWS band. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600011.html language=enus -->
## TOPIC 00017: Radio Configuration

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600011.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600011.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the radio configuration for the channel. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is RC3. Remarks The followi

### Radio Configuration

Specifies the radio configuration for the channel.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RC3**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Radio Configuration |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Radio Configuration |
| Resettable | Yes |

| RC1 | 0 | If Link Direction property is set to Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH), and reverse supplemental code channels (R-SCCHs). If Link Direction property is set to Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |
| --- | --- | --- |
| RC2 | 1 | If Link Direction property is set to Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH, and R-SCCHs. If Link Direction property is set to Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |
| RC3 | 2 | If Link Direction property is set to Uplink, Radio configuration 3 includes BPSK, R-FCH, and reverse supplemental channels (R-SCHs). If Link Direction property is set to Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |
| RC4 | 3 | If Link Direction property is set to Uplink, Radio configuration 4 includes BPSK, R-FCH, and R-SCHs. If Link Direction property is set to Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |
| RC5 | 4 | If Link Direction property is set to Uplink, Radio configuration 5 is not supported and gives invalid results. If Link Direction property is set to Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600012.html language=enus -->
## TOPIC 00018: Channel:Configuration Mode

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600012.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to detect the channels automatically or to use a specified channel configuration. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signa

### Channel:Configuration Mode

Specifies whether to detect the channels automatically or to use a specified channel configuration.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Auto Detect**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Channel Configuration Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Channel Configuration Mode |
| Resettable | Yes |

| Auto Detect | 0 | Specifies that the system automatically detects the channels. |
| --- | --- | --- |
| User Defined | 1 | Specifies that the system uses a specific channel configuration. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600018.html language=enus -->
## TOPIC 00019: Channel:User Defined:Walsh Code Number

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600018.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Walsh code number of a specific user-defined channel. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel< n >" as the Selector Strings to configure or read this property. The default value is 0. Remarks The following table list

### Channel:User Defined:Walsh Code Number

Specifies the Walsh code number of a specific user-defined channel. This property is used only when you set the [Channel Configuration Mode](/csh?topicname=attr600012.html) property to **User Defined**.

Use "channel<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Walsh Code Number |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure User Defined Channel |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600019.html language=enus -->
## TOPIC 00020: Channel:User Defined:Branch

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600019.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the branch on which a specific user-defined channel is mapped. This property is used only when you set the Channel Configuration Mode property to User Defined. Use "channel< n >" as the Selector Strings to configure or read this property. The default value is I. Remarks The following table

### Channel:User Defined:Branch

Specifies the branch on which a specific user-defined channel is mapped. This property is used only when you set the [Channel Configuration Mode](/csh?topicname=attr600012.html) property to **User Defined**.

Use "channel<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property.

The default value is **I**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Branch |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure User Defined Channel |
| Resettable | Yes |

| I | 0 | Specifies the in-phase branch. |
| --- | --- | --- |
| Q | 1 | Specifies the quadrature branch. |
| I and Q | 2 | Specifies the in-phase and quadrature branch. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60001e.html language=enus -->
## TOPIC 00021: Spreading:Uplink:Long Code Mask

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60001e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60001e.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the long code mask for reverse link spreading. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Remarks The fol

### Spreading:Uplink:Long Code Mask

Specifies the long code mask for reverse link spreading.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | UL Spreading Long Code Mask |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Uplink Spreading |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600020.html language=enus -->
## TOPIC 00022: Spreading:Downlink:PN Offset (64 chips)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr600020.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specified the PN offset in increments of 64 chips for forward link. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 0. Rema

### Spreading:Downlink:PN Offset (64 chips)

Specified the PN offset in increments of 64 chips for forward link.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | DL Spreading PN Offset (64 chips) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601000.html language=enus -->
## TOPIC 00023: ACP:Measurement Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601000.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The followi

### ACP:Measurement Enabled

Specifies whether to enable the ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100a.html language=enus -->
## TOPIC 00024: ACP:Offset:Frequency (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100a.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name ACP Offset Freq (Hz) Data type cdbl.png P

### ACP:Offset:Frequency (Hz)

Returns the frequency of an ACP offset channel relative to the carrier frequency. This value is expressed in Hz.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Offset Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100e.html language=enus -->
## TOPIC 00025: ACP:Offset:Integration Bandwidth (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60100e.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name ACP Offset IBW (Hz) Data type cdbl.png Permissions Read Only Hi

### ACP:Offset:Integration Bandwidth (Hz)

Returns the integration bandwidth of an ACP offset channel. This value is expressed in Hz.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Offset IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601016.html language=enus -->
## TOPIC 00026: ACP:Averaging:Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601016.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k ACP Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The ACP measurement uses the value of the ACP Averaging Count property as the number of acquisitions over which the ACP measurement is averaged. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601018.html language=enus -->
## TOPIC 00027: ACP:Averaging:Type

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601018.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the str

### ACP:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for ACP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101c.html language=enus -->
## TOPIC 00028: ACP:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the ACP RBW Auto property to False. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic

### ACP:RBW Filter:Bandwidth (Hz)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [ACP RBW Auto](/csh?topicname=attr60101b.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure RBW Filter |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101f.html language=enus -->
## TOPIC 00029: ACP:Sweep Time:Interval (s)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60101f.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the ACP Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### ACP:Sweep Time:Interval (s)

Specifies the sweep time when you set the [ACP Sweep Time Auto](/csh?topicname=attr60101e.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.0016667 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k ACP Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601020.html language=enus -->
## TOPIC 00030: ACP:Noise Compensation Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr601020.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k ACP Configure Noise Compensation Enabled |
| Resettable | Yes |

| False | 0 | Disables compensation of the channel powers for the noise floor of the signal analyzer. |
| --- | --- | --- |
| True | 1 | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the ACP measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832/5842/5860 |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60102c.html language=enus -->
## TOPIC 00031: ACP:Results:Lower Offset:Absolute Power (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60102c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60102c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute measured lower offset channel power. This value is expressed in dBm. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name ACP Results Lower Offset Abs Pwr (dBm) Data type cdbl.png Permis

### ACP:Results:Lower Offset:Absolute Power (dBm)

Returns the absolute measured lower offset channel power. This value is expressed in dBm.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ACP Results Lower Offset Abs Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ACP Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603003.html language=enus -->
## TOPIC 00032: CHP:Number of Analysis Threads

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603003.html
- document_id: `rfmxcdma2k-labview-api-ref`
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

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603006.html language=enus -->
## TOPIC 00033: CHP:Averaging:Count

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603006.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the CHP Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### CHP:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [CHP Averaging Enabled](/csh?topicname=attr603007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k CHP Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603007.html language=enus -->
## TOPIC 00034: CHP:Averaging:Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603007.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k CHP Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The CHP measurement uses the CHP Averaging Count property as the number of acquisitions over which the CHP measurement is averaged. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603009.html language=enus -->
## TOPIC 00035: CHP:Averaging:Type

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603009.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the

### CHP:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the CHP measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **RMS**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k CHP Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged on a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60300c.html language=enus -->
## TOPIC 00036: CHP:RBW Filter:Auto Bandwidth

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60300c.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k CHP Configure RBW Filter |
| Resettable | Yes |

| False | 0 | The measurement uses the RBW that you specify in the CHP RBW property. |
| --- | --- | --- |
| True | 1 | The measurement computes the RBW. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603014.html language=enus -->
## TOPIC 00037: CHP:All Traces Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603014.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603015.html language=enus -->
## TOPIC 00038: CHP:Results:Carrier:Absolute Power (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr603015.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### CHP:Results:Carrier:Absolute Power (dBm)

Returns the averaged CHP measured in the specified integration bandwidth. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CHP Results Carrier Abs Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CHP Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606000.html language=enus -->
## TOPIC 00039: OBW:Measurement Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606000.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606004.html language=enus -->
## TOPIC 00040: OBW:Span (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606004.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency span of the OBW measurement. This value is expressed in Hz. You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The following table

### OBW:Span (Hz)

Returns the frequency span of the OBW measurement. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Span (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606006.html language=enus -->
## TOPIC 00041: OBW:Averaging:Count

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606006.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the OBW Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax fo

### OBW:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [OBW Averaging Enabled](/csh?topicname=attr606007.html) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606007.html language=enus -->
## TOPIC 00042: OBW:Averaging:Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606007.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k OBW Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The OBW measurement uses the value of the OBW Averaging Count property as the number of acquisitions over which the OBW measurement is averaged. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606009.html language=enus -->
## TOPIC 00043: OBW:Averaging:Type

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606009.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606009.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k OBW Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The power spectrum is averaged in a logarithmic scale. |
| Scalar | 2 | The square root of the power spectrum is averaged. |
| Max | 3 | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min | 4 | The lowest power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600c.html language=enus -->
## TOPIC 00044: OBW:RBW Filter:Auto Bandwidth

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the RBW. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is True. Remarks The follo

### OBW:RBW Filter:Auto Bandwidth

Specifies whether the measurement computes the RBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure RBW Filter |
| Resettable | Yes |

| False | 0 | The measurement uses the RBW that you specify in the OBW RBW property. |
| --- | --- | --- |
| True | 1 | The measurement computes the RBW. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600d.html language=enus -->
## TOPIC 00045: OBW:RBW Filter:Bandwidth (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600d.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the OBW RBW Auto property to False. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic

### OBW:RBW Filter:Bandwidth (Hz)

Specifies the bandwidth of the RBW filter used to sweep the acquired signal when you set the [OBW RBW Auto](/csh?topicname=attr60600c.html) property to **False**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 30 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure RBW Filter |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600f.html language=enus -->
## TOPIC 00046: OBW:Sweep Time:Auto

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60600f.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k OBW Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the OBW Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606010.html language=enus -->
## TOPIC 00047: OBW:Sweep Time:Interval (s)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606010.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sweep time when you set the OBW Sweep Time Auto property to False. This value is expressed in seconds. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string synta

### OBW:Sweep Time:Interval (s)

Specifies the sweep time when you set the [OBW Sweep Time Auto](/csh?topicname=attr60600f.html) property to **False**. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.001667 seconds.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Sweep Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k OBW Configure Sweep Time |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606012.html language=enus -->
## TOPIC 00048: OBW:All Traces Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606012.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the OBW. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The

### OBW:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the OBW.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606013.html language=enus -->
## TOPIC 00049: OBW:Results:Occupied Bandwidth (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606013.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and

### OBW:Results:Occupied Bandwidth (Hz)

Returns the bandwidth that occupies 99% of the total signal power. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Occupied BW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606014.html language=enus -->
## TOPIC 00050: OBW:Results:Absolute Power (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606014.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute power measured in the OBW. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. Re

### OBW:Results:Absolute Power (dBm)

Returns the absolute power measured in the OBW. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Abs Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606015.html language=enus -->
## TOPIC 00051: OBW:Results:Start Frequency (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606015.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the start frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topi

### OBW:Results:Start Frequency (Hz)

Returns the start frequency of the OBW. This value is expressed in Hz.

The OBW is calculated using the following formula: *OBW = Stop Frequency - Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Start Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606016.html language=enus -->
## TOPIC 00052: OBW:Results:Stop Frequency (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr606016.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the stop frequency of the OBW. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic

### OBW:Results:Stop Frequency (Hz)

Returns the stop frequency of the OBW. This value is expressed in Hz.

The OBW is calculated using the following formula: *OBW = Stop Frequency - Start Frequency*

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OBW Results Stop Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k OBW Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608000.html language=enus -->
## TOPIC 00053: SEM:Measurement Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608000.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608005.html language=enus -->
## TOPIC 00054: SEM:Carrier:Integration Bandwidth (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608005.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM carrier integration bandwidth. This value is expressed in Hz. You do not need to use a selector string to read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The following table lis

### SEM:Carrier:Integration Bandwidth (Hz)

Returns the SEM carrier integration bandwidth. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Carrier IBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60801f.html language=enus -->
## TOPIC 00055: SEM:Averaging:Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60801f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60801f.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k SEM Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The SEM measurement uses the value of the SEM Averaging Count property as the number of acquisitions over which the SEM measurement is averaged. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608025.html language=enus -->
## TOPIC 00056: SEM:Sweep Time:Auto

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608025.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k SEM Configure Sweep Time |
| Resettable | Yes |

| False | 0 | The measurement uses the sweep time that you specify in the SEM Sweep Time property. |
| --- | --- | --- |
| True | 1 | The measurement uses the default sweep time, 0.001667 seconds. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608027.html language=enus -->
## TOPIC 00057: SEM:All Traces Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608027.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608029.html language=enus -->
## TOPIC 00058: SEM:Results:Measurement Status

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608029.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608029.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about th

### SEM:Results:Measurement Status

Indicates the overall measurement status based on the measurement limits, which are specified by the standard for each offset segment.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

| Fail | 0 | The measurement fails according to the measurement limits specified by this standard. |
| --- | --- | --- |
| Pass | 1 | The measurement passes according to the measurement limits specified by this standard. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60802d.html language=enus -->
## TOPIC 00059: SEM:Results:Carrier:Absolute Integrated Power (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60802d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60802d.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Sele

### SEM:Results:Carrier:Absolute Integrated Power (dBm)

Returns the carrier power. The carrier power is the power centered at the center frequency and integrated over the carrier bandwidth of 1.23 MHz. This value is expressed in dBm.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Carrier Abs Integrated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608034.html language=enus -->
## TOPIC 00060: SEM:Results:Lower Offset:Absolute Integrated Power (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608034.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Abs Integrated Pwr (d

### SEM:Results:Lower Offset:Absolute Integrated Power (dBm)

Returns the absolute power measured in the lower (negative) offset segment. This value is expressed in dBm.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Abs Integrated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608038.html language=enus -->
## TOPIC 00061: SEM:Results:Lower Offset:Peak Frequency (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608038.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608038.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Pk Freq (Hz) D

### SEM:Results:Lower Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power occurred in the lower offset segment. This value is expressed in Hz.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803d.html language=enus -->
## TOPIC 00062: SEM:Results:Lower Offset:Measurement Status

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60803d.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the lower offset segment measurement status based on measurement limits specified by the standard. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Lower Offset Meas Status Data typ

### SEM:Results:Lower Offset:Measurement Status

Indicates the lower offset segment measurement status based on measurement limits specified by the standard.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Lower Offset Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

| Fail | 0 | The lower offset segment measurement fails according to the measurement limits specified by the standard. |
| --- | --- | --- |
| Pass | 1 | The lower offset segment measurement passes according to the measurement limits specified by the standard. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608041.html language=enus -->
## TOPIC 00063: SEM:Results:Upper Offset:Absolute Integrated Power (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608041.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608041.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper (positive) offset segment. This value is expressed in dB. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Abs Integrated Pwr (dBm) Data t

### SEM:Results:Upper Offset:Absolute Integrated Power (dBm)

Returns the power measured in the upper (positive) offset segment. This value is expressed in dB.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Abs Integrated Pwr (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608042.html language=enus -->
## TOPIC 00064: SEM:Results:Upper Offset:Relative Integrated Power (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608042.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608042.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Re

### SEM:Results:Upper Offset:Relative Integrated Power (dB)

Returns the power measured in the upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Rel Integrated Pwr (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608045.html language=enus -->
## TOPIC 00065: SEM:Results:Upper Offset:Peak Frequency (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608045.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr608045.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Pk Freq (Hz) D

### SEM:Results:Upper Offset:Peak Frequency (Hz)

Returns the frequency at which the peak power occurred in the upper offset segment. This value is expressed in Hz.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Pk Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60804a.html language=enus -->
## TOPIC 00066: SEM:Results:Upper Offset:Measurement Status

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60804a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60804a.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates the upper offset measurement status based on measurement limits set by the standard. Use "offset< n >" as the Selector Strings to read this result. Remarks The following table lists the characteristics of this property. Short Name SEM Results Upper Offset Meas Status Data type ci32.png Per

### SEM:Results:Upper Offset:Measurement Status

Indicates the upper offset measurement status based on measurement limits set by the standard.

Use "offset<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SEM Results Upper Offset Meas Status |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k SEM Fetch |
| Resettable | No |

| Fail | 0 | The lower offset segment measurement fails according to the measurement limits specified by this standard. |
| --- | --- | --- |
| Pass | 1 | The lower offset segment measurement passes according to the measurement limits specified by this standard. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60d000.html language=enus -->
## TOPIC 00067: Advanced:Auto Level Initial Reference Level (dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60d000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr60d000.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the initial reference level that the RFmxCDMA2k Auto Level VI uses to estimate the peak power of the input signal. This value is expressed in dBm. The default value is 30 dBm. Remarks The following table lists the characteristics of this property. Short Name Auto Level Initial Ref Level (d

### Advanced:Auto Level Initial Reference Level (dBm)

Specifies the initial reference level that the [RFmxCDMA2k Auto Level](/csh?context=rfmxcdma2k_rfmxcdma2kvi_rfmxcdma2k_auto_level) VI uses to estimate the peak power of the input signal. This value is expressed in dBm.

The default value is 30 dBm.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Level Initial Ref Level (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Auto Level |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611005.html language=enus -->
## TOPIC 00068: ModAcc:Synchronization Mode

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611005.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the ModAcc Meas Length property starting at the ModAcc Meas Offset property from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the ModAcc Meas Length property starting at the ModAcc Meas Offset property from the slot boundary. |
| Arbitrary | 2 | The symbol boundary is detected, and the measurement is performed over the ModAcc Meas Length property starting at the ModAcc Meas Offset property from the slot boundary. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611006.html language=enus -->
## TOPIC 00069: ModAcc:Measurement Offset (slots)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611006.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the ModAcc Sync Mode property. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer

### ModAcc:Measurement Offset (slots)

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [ModAcc Sync Mode](/csh?topicname=attr611005.html) property. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0. The valid values are 1 to 16, inclusive. The sum of the ModAcc measurement offset and the ModAcc measurement length must be less than or equal to 16.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Meas Offset (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611010.html language=enus -->
## TOPIC 00070: ModAcc:Multi Carrier Filter:Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611010.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611010.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for infor

### ModAcc:Multi Carrier Filter:Enabled

Specifies whether to enable the multi carrier filter which can be used to improve ModAcc measurement quality in presence of neighboring carriers.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc MC-Filter Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables multi carrier filter for ModAcc measurement. |
| --- | --- | --- |
| True | 1 | Enables multi carrier filter for ModAcc measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611015.html language=enus -->
## TOPIC 00071: ModAcc:All Traces Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611015.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the

### ModAcc:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611025.html language=enus -->
## TOPIC 00072: ModAcc:Results:I/Q Gain Imbalance (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611025.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax

### ModAcc:Results:I/Q Gain Imbalance (dB)

Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611026.html language=enus -->
## TOPIC 00073: ModAcc:Results:I/Q Quadrature Error (deg)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611026.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the strin

### ModAcc:Results:I/Q Quadrature Error (deg)

Returns the I/Q quadrature error of the composite signal, averaged over all measured slots. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results I/Q Quadrature Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611027.html language=enus -->
## TOPIC 00074: ModAcc:Results:Frequency Error (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611027.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611027.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the frequency error averaged over all measured slots. This value is expressed in Hz. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and name

### ModAcc:Results:Frequency Error (Hz)

Returns the frequency error averaged over all measured slots. This value is expressed in Hz.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611034.html language=enus -->
## TOPIC 00075: ModAcc:Results:Detected Channel:Number of Detected Channels

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611034.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the total number of detected channels. If you set the Channel Configuration Mode property to User Defined, the property returns the number of configured channels. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector St

### ModAcc:Results:Detected Channel:Number of Detected Channels

Returns the total number of detected channels. If you set the [Channel Configuration Mode](/csh?topicname=attr600012.html) property to **User Defined**, the property returns the number of configured channels.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Num Detected Channels |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611035.html language=enus -->
## TOPIC 00076: ModAcc:Results:Detected Channel:Walsh Code Length

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611035.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr611035.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Walsh code length of the detected channel. If you set the Channel Configuration Mode property to User Defined, the property returns the Walsh code length of the configured channel. Use "channel< n >" as the Selector Strings to read this property. Remarks The following table lists the cha

### ModAcc:Results:Detected Channel:Walsh Code Length

Returns the Walsh code length of the detected channel. If you set the [Channel Configuration Mode](/csh?topicname=attr600012.html) property to **User Defined**, the property returns the Walsh code length of the configured channel.

Use "channel<
 *n*
 >" as the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Detected Walsh Code Length |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr6110a2.html language=enus -->
## TOPIC 00077: ModAcc:IQ Quadrature Error Removal Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr6110a2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr6110a2.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before an EVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default valu

### ModAcc:IQ Quadrature Error Removal Enabled

Specifies whether to remove the I/Q quadrature error before an EVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc IQ Quadrature Error Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | I/Q quadrature error is not removed before the EVM measurement. |
| --- | --- | --- |
| True | 1 | I/Q quadrature error is removed before the EVM measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612002.html language=enus -->
## TOPIC 00078: QEVM:Measurement Length (chips)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612002.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of chips used for a single measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 1536. The vali

### QEVM:Measurement Length (chips)

Specifies the number of chips used for a single measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1536. The valid values are 700 to 2500, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Meas Length (chips) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k QEVM Configure Measurement Length |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612003.html language=enus -->
## TOPIC 00079: QEVM:Averaging:Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612003.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the QEVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Rema

### QEVM:Averaging:Enabled

Specifies whether to enable averaging for the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k QEVM Configure Averaging |
| Resettable | Yes |

| False | 0 | The averaging is disabled for the measurement. |
| --- | --- | --- |
| True | 1 | The averaging is enabled for the measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612004.html language=enus -->
## TOPIC 00080: QEVM:Averaging:Count

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612004.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of measurements used for averaging when you set the QEVM Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax f

### QEVM:Averaging:Count

Specifies the number of measurements used for averaging when you set the [QEVM Averaging Enabled](/csh?context=rfmxcdma2k_rfmxcdma2kprop_attr612003) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default values is 10. The valid values are 1 to 10000, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k QEVM Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612005.html language=enus -->
## TOPIC 00081: QEVM:Spectrum Inverted

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612005.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks Th

### QEVM:Spectrum Inverted

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Spectrum Inverted |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement spectrum is normal. |
| --- | --- | --- |
| True | 1 | The measurement spectrum is inverted. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612006.html language=enus -->
## TOPIC 00082: QEVM:IQ Offset Removal Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612006.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q offset before QEVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Rema

### QEVM:IQ Offset Removal Enabled

Specifies whether to remove I/Q offset before QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM IQ Offset Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | I/Q offset is not removed before the QEVM measurement. |
| --- | --- | --- |
| True | 1 | I/Q offset is removed before the QEVM measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200a.html language=enus -->
## TOPIC 00083: QEVM:All Traces Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200a.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named

### QEVM:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the QEVM measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200b.html language=enus -->
## TOPIC 00084: QEVM:Number of Analysis Threads

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200b.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the QEVM measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resource

### QEVM:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the QEVM measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

The default value is 1. Valid values range from 0 to 10, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200f.html language=enus -->
## TOPIC 00085: QEVM:Results:Mean Peak EVM (%)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61200f.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals

### QEVM:Results:Mean Peak EVM (%)

Returns the mean averaged peak EVM of the received signal. This value is expressed as a percentage.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean Pk EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612013.html language=enus -->
## TOPIC 00086: QEVM:Results:Mean Phase Error (deg)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612013.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged phase error of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Stringss topic for information about the string syntax for named signals.

### QEVM:Results:Mean Phase Error (deg)

Returns the mean averaged phase error of the received signal. This value is expressed in degrees.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string)s topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean Phase Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612014.html language=enus -->
## TOPIC 00087: QEVM:Results:Maximum Phase Error (deg)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612014.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum phase error of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remark

### QEVM:Results:Maximum Phase Error (deg)

Returns the maximum phase error of the received signal. This value is expressed in degrees.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max Phase Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612015.html language=enus -->
## TOPIC 00088: QEVM:Results:Mean Frequency Error (Hz)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612015.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged frequency error of the received signal. This value is expressed in Hz. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. R

### QEVM:Results:Mean Frequency Error (Hz)

Returns the mean averaged frequency error of the received signal. This value is expressed in Hz.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612017.html language=enus -->
## TOPIC 00089: QEVM:Results:Mean I/Q Origin Offset (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612017.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean averaged origin offset of the received signal. This value is expressed in dB. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Rem

### QEVM:Results:Mean I/Q Origin Offset (dB)

Returns the mean averaged origin offset of the received signal. This value is expressed in dB.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean I/Q Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612018.html language=enus -->
## TOPIC 00090: QEVM:Results:Maximum I/Q Origin Offset (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612018.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum origin offset of the received signal. This value is expressed in dB. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks T

### QEVM:Results:Maximum I/Q Origin Offset (dB)

Returns the maximum origin offset of the received signal. This value is expressed in dB.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max I/Q Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612019.html language=enus -->
## TOPIC 00091: QEVM:Results:Mean I/Q Gain Imbalance (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr612019.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks

### QEVM:Results:Mean I/Q Gain Imbalance (dB)

Returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Mean I/Q Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201c.html language=enus -->
## TOPIC 00092: QEVM:Results:Maximum I/Q Quadrature Error (deg)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string synta

### QEVM:Results:Maximum I/Q Quadrature Error (deg)

Returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees.

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max I/Q Quadrature Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k QEVM Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201e.html language=enus -->
## TOPIC 00093: QEVM:Results:Maximum Chip Rate Error (ppm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61201e.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum chip rate error. This value is expressed in parts per million (ppm). You do not need to use a selector string to read this property for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks T

### QEVM:Results:Maximum Chip Rate Error (ppm)

Returns the maximum chip rate error. This value is expressed in parts per million (ppm).

You do not need to use a selector string to read this property for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | QEVM Results Max Chip Rate Error (ppm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613002.html language=enus -->
## TOPIC 00094: CDA:Synchronization Mode

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613002.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
| High-level VIs | RFmxCDMA2k CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at the CDA measurement offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at the CDA measurement offset slots from the slot boundary. |
| Arbitrary | 2 | The symbol boundary is detected, and the measurement is performed over the number of slots specified by the CDA Meas Length property starting at the CDA measurement offset slots from the symbol boundary. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613004.html language=enus -->
## TOPIC 00095: CDA:Measurement Length (slots)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613004.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the duration of code domain measurement. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default

### CDA:Measurement Length (slots)

Specifies the duration of code domain measurement. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1. The valid values are 1 to 16, inclusive. The sum of the CDA measurement offset and the CDA measurement length must be less than or equal to 16.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Meas Length (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k CDA Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613005.html language=enus -->
## TOPIC 00096: CDA:Base Spreading Factor

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613005.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the base spreading factor used to calculate the code domain power traces. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default

### CDA:Base Spreading Factor

Specifies the base spreading factor used to calculate the code domain power traces.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Base Spreading Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613006.html language=enus -->
## TOPIC 00097: CDA:Measurement Channel:Walsh Code Length

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613006.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Walsh code length of a channel subject to channel specific analysis. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default v

### CDA:Measurement Channel:Walsh Code Length

Specifies the Walsh code length of a channel subject to channel specific analysis.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Meas Ch Walsh Code Length |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k CDA Configure Measurement Channel |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613007.html language=enus -->
## TOPIC 00098: CDA:Measurement Channel:Walsh Code Number

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613007.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the Walsh code number of a channel subject to channel specific analysis. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default v

### CDA:Measurement Channel:Walsh Code Number

Specifies the Walsh code number of a channel subject to channel specific analysis.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0. The valid values are 0 to 63, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Meas Ch Walsh Code Number |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k CDA Configure Measurement Channel |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300a.html language=enus -->
## TOPIC 00099: CDA:Spectrum Inverted

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300a.html
- document_id: `rfmxcdma2k-labview-api-ref`
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

| False | 0 | The measured spectrum is normal. |
| --- | --- | --- |
| True | 1 | The measured spectrum is inverted. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300b.html language=enus -->
## TOPIC 00100: CDA:IQ Offset Removal Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300b.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The de

### CDA:IQ Offset Removal Enabled

Specifies whether to remove I/Q offset before the code domain analysis (CDA) measurement.

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

| False | 0 | I/Q offset is not removed before the CDA measurement. |
| --- | --- | --- |
| True | 1 | I/Q offset is removed before the CDA measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300c.html language=enus -->
## TOPIC 00101: CDA:IQ Gain Imbalance Removal Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named sig

### CDA:IQ Gain Imbalance Removal Enabled

Specifies whether to remove the I/Q gain imbalance before the code domain analysis (CDA) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA IQ Gain Imbalance Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | I/Q gain imbalance is not removed before the CDA measurement. |
| --- | --- | --- |
| True | 1 | I/Q gain imbalance is removed before the CDA measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300d.html language=enus -->
## TOPIC 00102: CDA:IQ Quadrature Error Removal Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61300d.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named s

### CDA:IQ Quadrature Error Removal Enabled

Specifies whether to remove the I/Q quadrature error before the code domain analysis (CDA) measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA IQ Quadrature Error Removal Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | I/Q quadrature error is not removed before the CDA measurement. |
| --- | --- | --- |
| True | 1 | I/Q quadrature error is removed before the CDA measurement. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613014.html language=enus -->
## TOPIC 00103: CDA:Results:RMS Symbol Magnitude Error (%)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613014.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax

### CDA:Results:RMS Symbol Magnitude Error (%)

Returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results RMS Symbol Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613015.html language=enus -->
## TOPIC 00104: CDA:Results:RMS Symbol Phase Error (deg)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613015.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named

### CDA:Results:RMS Symbol Phase Error (deg)

Returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results RMS Symbol Phase Error (deg) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613016.html language=enus -->
## TOPIC 00105: CDA:Results:Mean Symbol Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613016.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the CDA Pwr Unit property to dB, and in dBm, when you set the CDA Pwr Unit property to dBm. You do not need to use a selector string to read this result for the default signal and result

### CDA:Results:Mean Symbol Power (dB or dBm)

Returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dB**, and in dBm, when you set the CDA Pwr Unit property to **dBm**.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Mean Symbol Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613019.html language=enus -->
## TOPIC 00106: CDA:Results:Mean Active Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613019.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of all active code channels. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. You do not need to use a selector string to read this

### CDA:Results:Mean Active Power (dB or dBm)

Returns the average power of all active code channels. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Mean Active Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301a.html language=enus -->
## TOPIC 00107: CDA:Results:Peak Active Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301a.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum power among all active code channels. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. You do not need to use a selector string to read t

### CDA:Results:Peak Active Power (dB or dBm)

Returns the maximum power among all active code channels. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Pk Active Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301b.html language=enus -->
## TOPIC 00108: CDA:Results:Mean Inactive Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301b.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Tota

### CDA:Results:Mean Inactive Power (dB or dBm)

Returns the average code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Mean Inactive Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301c.html language=enus -->
## TOPIC 00109: CDA:Results:Peak Inactive Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301c.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Re

### CDA:Results:Peak Inactive Power (dB or dBm)

Returns the maximum measured code power, measured among the set of inactive channels, in the code domain of the base spreading factor. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Pk Inactive Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301e.html language=enus -->
## TOPIC 00110: CDA:Results:I Peak Inactive Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301e.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to t

### CDA:Results:I Peak Inactive Power (dB or dBm)

Returns the maximum measured code power among the set of inactive channels on the I-branch and in the code domain of the base spreading factor. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results I Pk Inactive Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301f.html language=enus -->
## TOPIC 00111: CDA:Results:Q Mean Active Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr61301f.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the average power of all active code channels measured on the Q-branch. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. You do not need to use a sel

### CDA:Results:Q Mean Active Power (dB or dBm)

Returns the average power of all active code channels measured on the Q-branch. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Q Mean Active Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613020.html language=enus -->
## TOPIC 00112: CDA:Results:Q Peak Inactive Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613020.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to t

### CDA:Results:Q Peak Inactive Power (dB or dBm)

Returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the [CDA Pwr Unit](/csh?topicname=attr613009.html) property to **dBm**, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the [CDA Result Total Power](/csh?topicname=attr613017.html) property.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Q Pk Inactive Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613021.html language=enus -->
## TOPIC 00113: CDA:Results:Mean Pilot Power (dB or dBm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613021.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613021.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean power of the R-PICH. Returns the mean power value in dB, when you set the CDA Pwr Unit property to dB. Returns the mean power value in dBm, when you set the CDA Pwr Unit property to dBm. You do not need to use a selector string to read this result for the default signal and result i

### CDA:Results:Mean Pilot Power (dB or dBm)

Returns the mean power of the R-PICH.

Returns the mean power value in dB, when you set the [CDA Pwr Unit](attr613009.html) property to **dB**.

Returns the mean power value in dBm, when you set the CDA Pwr Unit property to **dBm**.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Mean Pilot Pwr |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613022.html language=enus -->
## TOPIC 00114: CDA:Results:I/Q Origin Offset (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613022.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613022.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax

### CDA:Results:I/Q Origin Offset (dB)

Returns the I/Q origin offset of the composite signal averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results I/Q Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613023.html language=enus -->
## TOPIC 00115: CDA:Results:I/Q Gain Imbalance (dB)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613023.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613023.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB. You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax

### CDA:Results:I/Q Gain Imbalance (dB)

Returns the I/Q gain imbalance of the composite signal averaged over all measured slots. This value is expressed in dB.

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results I/Q Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613026.html language=enus -->
## TOPIC 00116: CDA:Results:Chip Rate Error (ppm)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr613026.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the chip rate error. This value is expressed in parts per million (ppm). You do not need to use a selector string to read this result for the default signal and result instance. Refer to the Selector Strings topic for information about the string syntax for named signals and named results. R

### CDA:Results:Chip Rate Error (ppm)

Returns the chip rate error. This value is expressed in parts per million (ppm).

You do not need to use a selector string to read this result for the default signal and result instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | CDA Results Chip Rate Error (ppm) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxCDMA2k CDA Fetch |
| Resettable | No |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614002.html language=enus -->
## TOPIC 00117: SlotPower:Synchronization Mode

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614002.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default valu

### SlotPower:Synchronization Mode

Specifies whether the measurement is performed from the frame or slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at the SlotPower measurement offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the number of slots specified by the SlotPower Meas Length property starting at the SlotPower measurement offset slots from the slot boundary. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614003.html language=enus -->
## TOPIC 00118: SlotPower:Measurement Offset (slots)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614003.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SlotPower Sync Mode property. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Re

### SlotPower:Measurement Offset (slots)

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SlotPower Sync Mode](/csh?topicname=attr614002.html) property. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Meas Offset (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SlotPower Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614005.html language=enus -->
## TOPIC 00119: SlotPower:Spectrum Inverted

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr614005.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the spectrum of the signal is inverted. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks Th

### SlotPower:Spectrum Inverted

Specifies whether the spectrum of the signal is inverted.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPower Spectrum Inverted |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement spectrum is normal. |
| --- | --- | --- |
| True | 1 | The measurement spectrum is inverted. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615000.html language=enus -->
## TOPIC 00120: SlotPhase:Measurement Enabled

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615000.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the SlotPhase measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is FALSE. Remarks The f

### SlotPhase:Measurement Enabled

Specifies whether to enable the SlotPhase measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k Select Measurement |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615002.html language=enus -->
## TOPIC 00121: SlotPhase:Synchronization Mode

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615002.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed from the frame or slot boundary. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default valu

### SlotPhase:Synchronization Mode

Specifies whether the measurement is performed from the frame or slot boundary.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Slot**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Sync Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

| Frame | 0 | The frame boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property starting at the SlotPhase measurement offset slots from the frame boundary. |
| --- | --- | --- |
| Slot | 1 | The slot boundary is detected, and the measurement is performed over the number of slots specified by the SlotPhase Meas Length property starting at the SlotPhase measurement offset slots from the slot boundary. |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615003.html language=enus -->
## TOPIC 00122: SlotPhase:Measurement Offset (slots)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615003.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the SlotPhase Sync Mode property. This value is expressed in slots. You do not need to use a selector string to configure or read this property for the default signal instance. Re

### SlotPhase:Measurement Offset (slots)

Specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the [SlotPhase Sync Mode](/csh?topicname=attr615002.html) property. This value is expressed in slots.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Meas Offset (slots) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxCDMA2k SlotPhase Configure Synchronization Mode and Interval |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615007.html language=enus -->
## TOPIC 00123: SlotPhase:Transient Duration (s)

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxcdma2k-rc/rfmxcdma2k/attr615007.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds. The transient duration is applied equally on either side of a slot boundary, that is at the start and end of each slot. If you set the transient duration to zero, there i

### SlotPhase:Transient Duration (s)

Specifies the region to exclude for computing the individual slot phase discontinuity values. This value is expressed in seconds.

The transient duration is applied equally on either side of a slot boundary, that is at the start and end of each slot. If you set the transient duration to zero, there is no transient period and the entire slot data is used to determine the phase error best fit line which is used to compute the phase discontinuity at the slot boundaries.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 0. The valid values are 0 to 0.0002, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SlotPhase Transient Duration (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxCDMA2k Properties

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-abort-measurements-vi.html language=enus -->
## TOPIC 00124: RFmxCDMA2k Abort Measurements VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-abort-measurements-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. The acquisition and measurements were previously initiated by the RFmxCDMA2k Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measureme

### RFmxCDMA2k Abort Measurements VI

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. The acquisition and measurements were previously initiated by the [RFmxCDMA2k Initiate](/csh?topicname=rfmxcdma2k-initiate-vi.html) VI or measurement read VIs.

Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxcdma2k-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-averaging-vi.html language=enus -->
## TOPIC 00125: RFmxCDMA2k ACP Configure Averaging VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-averaging-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "sign

### RFmxCDMA2k ACP Configure Averaging VI

Configures averaging for the ACP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-acp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The ACP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the ACP measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The ACP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the ACP measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-measurement-method-vi.html language=enus -->
## TOPIC 00126: RFmxCDMA2k ACP Configure Measurement Method VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-measurement-method-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-measurement-method-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the method for performing the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxCDMA2k ACP Configure Measurement Method VI

Configures the method for performing the ACP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-acp-configure-measurement-method-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Method — Measurement Method specifies the method for performing the ACP measurement. The default value is Normal. Normal (0) The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. Dynamic Range (1) The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. Sequential FFT (2) The ACP measurement acquires I/Q the samples specified by the ACP Sweep Time. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed for each these chunks. The resultant FFTs are averaged to get the spectrum used to compute the the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Use this method to optimize the ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Properties Supported Values ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads >=1 Note For multi-span FFT, the averaging count should be 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Normal (0) | The ACP measurement acquires the spectrum using the same signal analyzer setting across frequency bands. Use this method when measurement speed is desirable over higher dynamic range. |
| Dynamic Range (1) | The ACP measurement acquires the spectrum using the hardware-specific optimizations for different frequency bands. Use this method to get the best dynamic range. Supported Devices: PXIe-5665/5668R. |
| Sequential FFT (2) | The ACP measurement acquires I/Q the samples specified by the ACP Sweep Time. These samples are divided into smaller chunks. The size of each chunk is defined by the ACP Sequential FFT Size property, and FFT is computed for each these chunks. The resultant FFTs are averaged to get the spectrum used to compute the the ACP. If the total acquired samples is not an integer multiple of the FFT size, the remaining samples at the end of the acquisition are not used. Use this method to optimize the ACP Measurement speed. The accuracy of results may be reduced when using this measurement method. For accurate power measurements when the power characteristics of the signal vary over time, averaging is allowed. The following properties have limited support when you set the ACP Measurement Method property to Sequential FFT. Properties Supported Values ACP RBW Auto True ACP RBW Filter Type FFT Based ACP Averaging Count >=1 ACP Noise Comp Enabled False ACP Num Analysis Threads >=1 Note For multi-span FFT, the averaging count should be 1. |
| Properties | Supported Values |
| ACP RBW Auto | True |
| ACP RBW Filter Type | FFT Based |
| ACP Averaging Count | >=1 |
| ACP Noise Comp Enabled | False |
| ACP Num Analysis Threads | >=1 |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-number-of-offsets-vi.html language=enus -->
## TOPIC 00127: RFmxCDMA2k ACP Configure Number of Offsets VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-number-of-offsets-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-number-of-offsets-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of offsets for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Exampl

### RFmxCDMA2k ACP Configure Number of Offsets VI

Configures the number of offsets for the ACP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-acp-configure-number-of-offsets-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Offsets — Number of Offsets specifies the number of offset channels. The default value is 2. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00128: RFmxCDMA2k ACP Configure RBW Filter VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-rbw-filter-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxCDMA2k ACP Configure RBW Filter VI

Configures the RBW filter.

[IMAGE alt='icon' src='rfmxcdma2k-acp-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. Refer to the RBW and Sweep Time section in the ACP topic for more information about RBW and sweep time. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. The default value is True. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the RBW Auto parameter to False. This value is expressed in Hz. The default value is 10 kHz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-sweep-time-vi.html language=enus -->
## TOPIC 00129: RFmxCDMA2k ACP Configure Sweep Time VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-configure-sweep-time-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxCDMA2k ACP Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxcdma2k-acp-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 0.001667 seconds. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time if you set the Sweep Time Auto parameter to False. This value is expressed in seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

ACP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-absolute-powers-trace-vi.html language=enus -->
## TOPIC 00130: RFmxCDMA2k ACP Fetch Absolute Powers Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-absolute-powers-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-absolute-powers-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the absolute powers trace for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the res

### RFmxCDMA2k ACP Fetch Absolute Powers Trace VI

Fetches the absolute powers trace for the ACP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-absolute-powers-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Powers (dBm) — Absolute Powers returns the array of traces of absolute integrated power measured in each offset channel. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged absolute power at each frequency bin. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged absolute power at each frequency bin. This value is expressed in dB. |

Parent topic:

RFmxCDMA2k ACP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-carrier-absolute-power-vi.html language=enus -->
## TOPIC 00131: RFmxCDMA2k ACP Fetch Carrier Absolute Power VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-carrier-absolute-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-carrier-absolute-power-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default r

### RFmxCDMA2k ACP Fetch Carrier Absolute Power VI

Returns the absolute carrier power.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-carrier-absolute-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Carrier Absolute Power (dBm) — Carrier Absolute Power returns the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k ACP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-array-vi.html language=enus -->
## TOPIC 00132: RFmxCDMA2k ACP Fetch Offset Measurement (Array) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-array-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not spec

### RFmxCDMA2k ACP Fetch Offset Measurement (Array) VI

Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-offset-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Lower Absolute Power (dBm) — Lower Absolute Power returns the array of lower offset channel absolute powers. Upper Absolute Power (dBm) — Upper Absolute Power returns the array of upper offset channel absolute powers. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Lower Relative Power (dB) — Lower Relative Power returns the array of lower offset channel powers measured relative to the carrier absolute power. This value is expressed in dB. Upper Relative Power (dB) — Upper Relative Power returns the array of upper offset channel powers measured relative to the carrier absolute power. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k ACP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-vi.html language=enus -->
## TOPIC 00133: RFmxCDMA2k ACP Fetch Offset Measurement VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute and relative powers measured in the specified offset channel. The relative powers are measured relative to the carrier absolute power. Use "offset<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a se

### RFmxCDMA2k ACP Fetch Offset Measurement VI

Returns the absolute and relative powers measured in the specified offset channel. The relative powers are measured relative to the carrier absolute power.

Use "offset<n>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-offset-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxCDMA2k Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Lower Absolute Power (dBm) — Lower Absolute Power returns the lower offset channel absolute power. Upper Absolute Power (dBm) — Upper Absolute Power returns the upper offset channel absolute power. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Lower Relative Power (dB) — Lower Relative Power returns the lower offset channel power measured relative to the carrier absolute power. This value is expressed in dB. Upper Relative Power (dB) — Upper Relative Power returns the upper offset channel power measured relative to the carrier absolute power. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k ACP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-relative-powers-trace-vi.html language=enus -->
## TOPIC 00134: RFmxCDMA2k ACP Fetch Relative Powers Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-relative-powers-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-relative-powers-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the relative powers trace for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the res

### RFmxCDMA2k ACP Fetch Relative Powers Trace VI

Fetches the relative powers trace for the ACP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-relative-powers-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Relative Powers (dB) — Relative Powers returns the array of relative power traces measured in each offset channel relative to the absolute carrier power. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged relative power at each frequency bin relative to absolute carrier power. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged relative power at each frequency bin relative to absolute carrier power. This value is expressed in dB. |

Parent topic:

RFmxCDMA2k ACP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00135: RFmxCDMA2k ACP Fetch Spectrum VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-spectrum-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the ACP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxCDMA2k ACP Fetch Spectrum VI

Fetches the spectrum used for the ACP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |

Parent topic:

RFmxCDMA2k ACP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-vi.html language=enus -->
## TOPIC 00136: RFmxCDMA2k ACP Fetch VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ACP measurement results. icon

### RFmxCDMA2k ACP Fetch VI

Fetches the ACP measurement results.

[IMAGE alt='icon' src='rfmxcdma2k-acp-fetch-vi.png']

- [RFmxCDMA2k ACP Fetch Carrier Absolute Power VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-carrier-absolute-power-vi.html) Returns the absolute carrier power.
- [RFmxCDMA2k ACP Fetch Offset Measurement VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-vi.html) Returns the absolute and relative powers measured in the specified offset channel. The relative powers are measured relative to the carrier absolute power.
- [RFmxCDMA2k ACP Fetch Offset Measurement (Array) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-offset-measurement-array-vi.html) Returns the absolute and relative powers measured in the offset channel. The relative powers are measured relative to the carrier absolute power.
- [RFmxCDMA2k ACP Fetch Spectrum VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-spectrum-vi.html) Fetches the spectrum used for the ACP measurement.
- [RFmxCDMA2k ACP Fetch Relative Powers Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-relative-powers-trace-vi.html) Fetches the relative powers trace for the ACP measurement.
- [RFmxCDMA2k ACP Fetch Absolute Powers Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-acp-fetch-absolute-powers-trace-vi.html) Fetches the absolute powers trace for the ACP measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00137: RFmxCDMA2k Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-iq-1-wfm-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxCDMA2k Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **IQ** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx CDMA2k Commit

[IMAGE alt='icon' src='rfmxcdma2k-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies the array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

RFmxCDMA2k Analyze2 VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-spectrum-1-wfm-vi.html language=enus -->
## TOPIC 00138: RFmxCDMA2k Analyze (Spectrum, 1 Wfm) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-spectrum-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-spectrum-1-wfm-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the spectrum waveform that you specify in Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommen

### RFmxCDMA2k Analyze (Spectrum, 1 Wfm) VI

Performs the enabled measurements on the spectrum waveform that you specify in **Spectrum** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is either **Spectral** or **IQ or Spectral**.

Note

RFmxInstr Property Node

RFmx CDMA2k Commit

[IMAGE alt='icon' src='rfmxcdma2k-analyze-spectrum-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string) which refers to default result instance. Example: "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by Result Name parameter or the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". Spectrum — Spectrum specifies the data for a spectrum waveform including the start, delta, and actual values. x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y contains the real-value power spectrum. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of Configure, Initiate, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start frequency of the spectrum. This value is expressed in Hz. dx — dx specifies the frequency interval between data points in the spectrum. y — y contains the real-value power spectrum. |

Parent topic:

RFmxCDMA2k Analyze2 VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze2-vi.html language=enus -->
## TOPIC 00139: RFmxCDMA2k Analyze2 VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze2-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze2-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance. icon

### RFmxCDMA2k Analyze2 VI

Performs the enabled measurements on the specified waveform. For I/Q measurements, select the IQ instance. For spectral measurements, select the Spectrum instance.

[IMAGE alt='icon' src='rfmxcdma2k-analyze2-vi.png']

- [RFmxCDMA2k Analyze (IQ, 1 Wfm) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-iq-1-wfm-vi.html) Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is either IQ or IQ or Spectral .
- [RFmxCDMA2k Analyze (Spectrum, 1 Wfm) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-analyze-spectrum-1-wfm-vi.html) Performs the enabled measurements on the spectrum waveform that you specify in Spectrum parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is either Spectral or IQ or Spectral .

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-auto-level-vi.html language=enus -->
## TOPIC 00140: RFmxCDMA2k Auto Level VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-auto-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-auto-level-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to calculate an approximate setting for the reference level. The RFmxCDMA2k Auto Level VI does the following tasks: Resets the mixer level, mixer level offset, and IF out

### RFmxCDMA2k Auto Level VI

Examines the input signal to calculate the peak power level and sets it as the value of the [Reference Level](/csh?context=rfmxcdma2k_rfmxcdma2kprop_attr600002) property. Use this VI to calculate an approximate setting for the reference level.

The RFmxCDMA2k Auto Level VI does the following tasks:

1. Resets the mixer level, mixer level offset, and IF output power offset.
2. Sets the starting reference level to the maximum reference level supported by the device based on the current RF attenuation, mechanical attenuation, and preamplifier enabled settings.
3. Iterates to adjust the reference level based on the input signal peak power.
4. Uses immediate triggering and restores the trigger settings back to user setting after the execution.

You can also specify the starting reference level using the [Auto Level Initial Ref Level](/csh?context=rfmxcdma2k_rfmxcdma2kprop_attr60d000) property.

When using NI 5663, 5665, or 5668R devices, NI recommends that you set an appropriate value for mechanical attenuation before calling the RFmxCDMA2k Auto Level VI. Setting an appropriate value for mechanical attenuation reduces the number of times the attenuator settings are changed by this function; thus reducing wear and tear, and maximizing the life time of the attenuator.

[IMAGE alt='icon' src='rfmxcdma2k-auto-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Interval (s) — Measurement Interval specifies the acquisition length. This value is expressed in seconds. Use this value to compute the number of samples to acquire from the signal analyzer. Auto Level VI does not use any trigger for acquisition. It ignores the user-configured trigger properties. NI recommends that you set a sufficiently high measurement interval to ensure that the acquired waveform is at least as long as one period of the signal. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Reference Level — Reference Level returns the estimated peak power level of the input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-channel-string-vi.html language=enus -->
## TOPIC 00141: RFmxCDMA2k Build Channel String VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-channel-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-channel-string-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with channel configuration. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do

### RFmxCDMA2k Build Channel String VI

Creates a selector string to use with channel configuration.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxcdma2k-build-channel-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Channel Number — Channel Number specifies the channel number used to build the selector string. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input on Configure VIs, Initiate VIs, and Fetch VIs. |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-offset-string-vi.html language=enus -->
## TOPIC 00142: RFmxCDMA2k Build Offset String VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-offset-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-offset-string-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selec

### RFmxCDMA2k Build Offset String VI

Creates the offset string to use as the selector string with the SEM and ACP offset configuration for fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxcdma2k-build-offset-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Offset Number — Offset Number specifies the offset number used to build the selector string. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input on Configure VIs, Initiate VIs, and Fetch VIs. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-signal-string-vi.html language=enus -->
## TOPIC 00143: RFmxCDMA2k Build Signal String VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-signal-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-build-signal-string-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string to use with configuration or fetch properties and VIs. Refer to the Selector String topic for information about the string syntax for named signals. icon Inputs/Outputs cstr.png Result Name Result Name specifies the name of the result when performing overlapped measurements

### RFmxCDMA2k Build Signal String VI

Creates a selector string to use with configuration or fetch properties and VIs.

Refer to the [Selector String](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

[IMAGE alt='icon' src='rfmxcdma2k-build-signal-string-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name of the result when performing overlapped measurements. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string). Examples: "" "result::r1" "r1" Signal Name — Signal Name specifies the name of the signal when using named signal configurations. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Examples: "" "signal::sig1" "sig1" Selector String — Selector String returns the selector string you can use in the input to Configuration VIs, Fetch VIs, or other VIs that build selector strings. This string contains the signal and/or result names with their appropriate prefixes. Examples: "signal::sig1" "result::r1" "signal::sig1/result::r1" |
| --- |

Parent topic:

Configuration

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-measurement-channel-vi.html language=enus -->
## TOPIC 00144: RFmxCDMA2k CDA Configure Measurement Channel VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-measurement-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-measurement-channel-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is us

### RFmxCDMA2k CDA Configure Measurement Channel VI

Configures the spreading factor, spreading code, modulation type, and branch of the channel to be measured.

[IMAGE alt='icon' src='rfmxcdma2k-cda-configure-measurement-channel-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Walsh Code Length — Walsh Code Length specifies the Walsh code length of a channel subject to channel specific analysis. The default value is 64. The valid values are 2, 4, 8, 16, 32, and 64. Walsh Code Number — Walsh Code Number specifies the Walsh code number of a channel subject to channel specific analysis. Branch — Branch specifies the Walsh branch of a channel subject to channel specific analysis. The default value is I. I (0) Specifies the in-phase branch. Q (1) Specifies the quadrature branch. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | Specifies the in-phase branch. |
| Q (1) | Specifies the quadrature branch. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-power-unit-vi.html language=enus -->
## TOPIC 00145: RFmxCDMA2k CDA Configure Power Unit VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-power-unit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-power-unit-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Power Unit parameter for the code domain power results, except for the Total Power parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is u

### RFmxCDMA2k CDA Configure Power Unit VI

Configures the **Power Unit** parameter for the code domain power results, except for the **Total Power** parameter.

[IMAGE alt='icon' src='rfmxcdma2k-cda-configure-power-unit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Power Unit — Power Unit specifies the measurement unit of the measured code domain power results. This value is expressed in dB/dBm. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00146: RFmxCDMA2k CDA Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters for the code domain analysis (CDA) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, th

### RFmxCDMA2k CDA Configure Synchronization Mode and Interval VI

Configures the **Synchronization Mode**, **Measurement Offset**, and **Measurement Length** parameters for the code domain analysis (CDA) measurement.

[IMAGE alt='icon' src='rfmxcdma2k-cda-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the symbol boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. The synchronization boundary is specified by the Synchronization Mode parameter. This value is expressed in slots. Measurement Length (slots) — Measurement Length specifies the duration of code domain measurement. This value is expressed in slots. The default value is 0. The valid values are 1 to 16, inclusive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the symbol boundary. |

Parent topic:

CDA

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-trace-vi.html language=enus -->
## TOPIC 00147: RFmxCDMA2k CDA Fetch Code Domain I and Q Power Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I and Q code power trace measured in the code domain of the base spreading factor. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is

### RFmxCDMA2k CDA Fetch Code Domain I and Q Power Trace VI

Returns the I and Q code power trace measured in the code domain of the base spreading factor.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I Code Domain Powers (dB or dBm) — I Code Domain Powers returns the array of I code power measured in the code domain of the base spreading factor. This value is expressed in dB or dBm. Q Code Domain Powers (dB or dBm) — Q Code Domain Powers returns the array of Q code power measured in the code domain of the base spreading factor. This value is expressed in dB or dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-vi.html language=enus -->
## TOPIC 00148: RFmxCDMA2k CDA Fetch Code Domain I and Q Power VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the I and Q mean active powers, and I and Q peak inactive powers. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not

### RFmxCDMA2k CDA Fetch Code Domain I and Q Power VI

Returns the I and Q mean active powers, and I and Q peak inactive powers.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Q Peak Inactive Power (dB or dBm) — Q Peak Inactive Power returns the maximum measured code power among the set of inactive channels on the Q-branch and in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I Mean Active Power (dB or dBm) — I Mean Active Power returns the average power of all active code channels measured on the I-branch. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. Q Mean Active Power (dB or dBm) — Q Mean Active Power returns the average power of all active code channels measured on the Q-branch. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. I Peak Inactive Power (dB or dBm) — I Peak Inactive Power returns the maximum measured code power among the set of inactive channels on the I-Branch. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-power-vi.html language=enus -->
## TOPIC 00149: RFmxCDMA2k CDA Fetch Code Domain Power VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-power-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the scalar code domain power results. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the

### RFmxCDMA2k CDA Fetch Code Domain Power VI

Returns the scalar code domain power results.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-code-domain-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Inactive Power (dB or dBm) — Mean Inactive Power returns the average code power measured among the set of inactive channels in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. Peak Active Power (dB or dBm) — Peak Active Power returns the maximum power among all active code channels. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Total Power (dBm) — Total Power returns the mean power of the received signal. This value is expressed in dBm. Total Active Power (dB or dBm) — Total Active Power returns the sum of the powers of all active code channels. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. Mean Active Power (dB or dBm) — Mean Active Power returns the average power of all active code channels. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. error out — error out contains error information. This output provides standard error out functionality. Peak Inactive Power (dB or dBm) — Peak Inactive Power returns the maximum measured code power among the set of inactive channels in the code domain of the base spreading factor. If you set the CDA Pwr Unit property to dBm, this measurement returns the absolute measured power; otherwise, this measurement returns a value relative to the CDA Result Total Power property. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00150: RFmxCDMA2k CDA Fetch IQ Impairments VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-iq-impairments-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured I/Q impairments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default

### RFmxCDMA2k CDA Fetch IQ Impairments VI

Returns the measured I/Q impairments.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I/Q Origin Offset (dB) — I/Q Origin Offset returns the I/Q origin offset of the composite signal. This value is expressed in dB. I/Q Gain Imbalance (dB) — I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal. This value is expressed in dB. I/Q Quadrature Error (deg) — I/Q Quadrature Error returns the I/Q quadrature error of the composite signal. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-constellation-trace-vi.html language=enus -->
## TOPIC 00151: RFmxCDMA2k CDA Fetch Symbol Constellation Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-constellation-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol constellation trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do

### RFmxCDMA2k CDA Fetch Symbol Constellation Trace VI

Returns the symbol constellation trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-symbol-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Constellation — Symbol Constellation returns the array of symbol constellation points of the configured measurement channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-trace-vi.html language=enus -->
## TOPIC 00152: RFmxCDMA2k CDA Fetch Symbol EVM Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol EVM trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specif

### RFmxCDMA2k CDA Fetch Symbol EVM Trace VI

Returns the symbol EVM trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-symbol-evm-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol EVM (%) — Symbol EVM returns the array of symbol EVM values of the configured measurement channel. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-vi.html language=enus -->
## TOPIC 00153: RFmxCDMA2k CDA Fetch Symbol EVM VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation accuracy related measures for the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxCDMA2k CDA Fetch Symbol EVM VI

Returns the modulation accuracy related measures for the configured measurement channel.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-symbol-evm-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Mean Symbol Power (dB or dBm) — Mean Symbol Power returns the mean symbol power of the configured measurement channel. This value is expressed in dB, when you set the CDA Pwr Unit property to dB, and in dBm, when you set the CDA Pwr Unit property to dBm. RMS Symbol Phase Error (deg) — RMS Symbol Phase Error returns the RMS symbol phase error of the configured measurement channel. This value is expressed in degrees. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. RMS Symbol EVM (%) — RMS Symbol EVM returns the RMS symbol EVM of the configured measurement channel. This value is expressed as a percentage. Peak Symbol EVM (%) — Peak Symbol EVM returns the peak symbol EVM of the configured measurement channel. This value is expressed as a percentage. RMS Symbol Magnitude Error (%) — RMS Symbol Magnitude Error returns the RMS symbol magnitude error of the configured measurement channel. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. Frequency Error (Hz) — Frequency Error returns the frequency error. This value is expressed in Hz. Chip Rate Error (ppm) — Chip Rate Error returns the chip rate error. This value is expressed in parts per million (ppm). |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00154: RFmxCDMA2k CDA Fetch Symbol Magnitude Error Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-magnitude-error-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol magnitude error trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxCDMA2k CDA Fetch Symbol Magnitude Error Trace VI

Returns the symbol magnitude error trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-symbol-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Magnitude Error (%) — Symbol Magnitude Error returns the trace of the symbol magnitude errors of the corrected composite signal. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-phase-error-trace-vi.html language=enus -->
## TOPIC 00155: RFmxCDMA2k CDA Fetch Symbol Phase Error Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-phase-error-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol phase error trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do no

### RFmxCDMA2k CDA Fetch Symbol Phase Error Trace VI

Returns the symbol phase error trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-symbol-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Phase Error (deg) — Symbol Phase Error returns the array of symbol phase error values of the configured measurement channel. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-power-trace-vi.html language=enus -->
## TOPIC 00156: RFmxCDMA2k CDA Fetch Symbol Power Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-power-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol power trace of the configured measurement channel. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not spec

### RFmxCDMA2k CDA Fetch Symbol Power Trace VI

Returns the symbol power trace of the configured measurement channel.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-symbol-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Symbol Powers (dBm) — Symbol Powers returns the array of symbol power of the configured measurement channel. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CDA Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-vi.html language=enus -->
## TOPIC 00157: RFmxCDMA2k CDA Fetch VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the CDA measurement results. icon

### RFmxCDMA2k CDA Fetch VI

Fetches the CDA measurement results.

[IMAGE alt='icon' src='rfmxcdma2k-cda-fetch-vi.png']

- [RFmxCDMA2k CDA Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-iq-impairments-vi.html) Returns the measured I/Q impairments.
- [RFmxCDMA2k CDA Fetch Symbol EVM VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-vi.html) Returns the modulation accuracy related measures for the configured measurement channel.
- [RFmxCDMA2k CDA Fetch Code Domain Power VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-power-vi.html) Returns the scalar code domain power results.
- [RFmxCDMA2k CDA Fetch Code Domain I and Q Power VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-vi.html) Returns the I and Q mean active powers, and I and Q peak inactive powers.
- [RFmxCDMA2k CDA Fetch Symbol EVM Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-evm-trace-vi.html) Returns the symbol EVM trace of the configured measurement channel.
- [RFmxCDMA2k CDA Fetch Symbol Magnitude Error Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-magnitude-error-trace-vi.html) Returns the symbol magnitude error trace of the configured measurement channel.
- [RFmxCDMA2k CDA Fetch Symbol Phase Error Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-phase-error-trace-vi.html) Returns the symbol phase error trace of the configured measurement channel.
- [RFmxCDMA2k CDA Fetch Code Domain I and Q Power Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-code-domain-i-and-q-power-trace-vi.html) Returns the I and Q code power trace measured in the code domain of the base spreading factor.
- [RFmxCDMA2k CDA Fetch Symbol Power Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-power-trace-vi.html) Returns the symbol power trace of the configured measurement channel.
- [RFmxCDMA2k CDA Fetch Symbol Constellation Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-cda-fetch-symbol-constellation-trace-vi.html) Returns the symbol constellation trace of the configured measurement channel.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-check-measurement-status-vi.html language=enus -->
## TOPIC 00158: RFmxCDMA2k Check Measurement Status VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-check-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-check-measurement-status-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal nam

### RFmxCDMA2k Check Measurement Status VI

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='icon' src='rfmxcdma2k-check-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. done? — done? indicates whether the measurement is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-averaging-vi.html language=enus -->
## TOPIC 00159: RFmxCDMA2k CHP Configure Averaging VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-averaging-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "sign

### RFmxCDMA2k CHP Configure Averaging VI

Configures averaging for the CHP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-chp-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The CHP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the CHP measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The CHP measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the CHP measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-rbw-filter-vi.html language=enus -->
## TOPIC 00160: RFmxCDMA2k CHP Configure RBW Filter VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-rbw-filter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-rbw-filter-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the RBW filter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxCDMA2k CHP Configure RBW Filter VI

Configures the RBW filter.

[IMAGE alt='icon' src='rfmxcdma2k-chp-configure-rbw-filter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. RBW Auto — RBW Auto specifies whether the measurement computes the RBW. The default value is True. Refer to the RBW and Sweep Time section in the CHP topic for more information about RBW and sweep time. False (0) The measurement uses the RBW that you specify in the RBW parameter. True (1) The measurement computes the RBW. RBW (Hz) — RBW specifies the bandwidth of the RBW filter used to sweep the acquired signal if you set the RBW Auto parameter to False. This value is expressed in Hz. RBW Filter Type — RBW Filter Type specifies the shape of the digital RBW filter. The default value is Gaussian. FFT Based (0) No RBW filtering is performed. Gaussian (1) An RBW filter with a Gaussian response is applied. Flat (2) An RBW filter with a flat response is applied. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the RBW that you specify in the RBW parameter. |
| True (1) | The measurement computes the RBW. |
| FFT Based (0) | No RBW filtering is performed. |
| Gaussian (1) | An RBW filter with a Gaussian response is applied. |
| Flat (2) | An RBW filter with a flat response is applied. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-sweep-time-vi.html language=enus -->
## TOPIC 00161: RFmxCDMA2k CHP Configure Sweep Time VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-configure-sweep-time-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxCDMA2k CHP Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxcdma2k-chp-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True . False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 0.001667 seconds. Refer to the RBW and Sweep Time section in the CHP topic for more information about RBW and sweep time. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time if you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 0.00167 seconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

CHP

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-carrier-absolute-power-vi.html language=enus -->
## TOPIC 00162: RFmxCDMA2k CHP Fetch Carrier Absolute Power VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-carrier-absolute-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-carrier-absolute-power-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier power of the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the res

### RFmxCDMA2k CHP Fetch Carrier Absolute Power VI

Returns the absolute carrier power of the CHP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-chp-fetch-carrier-absolute-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Carrier Absolute Power (dBm) — Carrier Absolute Power returns the averaged channel power measured in the specified integration bandwidth. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k CHP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-spectrum-vi.html language=enus -->
## TOPIC 00163: RFmxCDMA2k CHP Fetch Spectrum VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-spectrum-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the spectrum used for the CHP measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxCDMA2k CHP Fetch Spectrum VI

Fetches the spectrum used for the CHP measurement.

[IMAGE alt='icon' src='rfmxcdma2k-chp-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the averaged power measured at each frequency bin. This value is expressed in dBm or dBm/Hz. |

Parent topic:

RFmxCDMA2k CHP Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-vi.html language=enus -->
## TOPIC 00164: RFmxCDMA2k CHP Fetch VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the CHP measurement results. icon

### RFmxCDMA2k CHP Fetch VI

Fetches the CHP measurement results.

[IMAGE alt='icon' src='rfmxcdma2k-chp-fetch-vi.png']

- [RFmxCDMA2k CHP Fetch Carrier Absolute Power VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-carrier-absolute-power-vi.html) Returns the absolute carrier power of the CHP measurement.
- [RFmxCDMA2k CHP Fetch Spectrum VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-chp-fetch-spectrum-vi.html) Fetches the spectrum used for the CHP measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-all-named-results-vi.html language=enus -->
## TOPIC 00165: RFmxCDMA2k Clear All Named Results VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-all-named-results-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value i

### RFmxCDMA2k Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxcdma2k-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-named-result-vi.html language=enus -->
## TOPIC 00166: RFmxCDMA2k Clear Named Result VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-named-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clear-named-result-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxCDMA2k Clear Named Result VI

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxcdma2k-clear-named-result-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clone-signal-configuration-vi.html language=enus -->
## TOPIC 00167: RFmxCDMA2k Clone Signal Configuration VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clone-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-clone-signal-configuration-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal by copying all the property values from an existing signal instance. icon Inputs/Outputs cstr.png Old Signal Name Old Signal Name specifies the name of an existing signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::

### RFmxCDMA2k Clone Signal Configuration VI

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='icon' src='rfmxcdma2k-clone-signal-configuration-vi.png']

#### Inputs/Outputs

| Old Signal Name — Old Signal Name specifies the name of an existing signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::OldSigName" "OldSigName" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. New Signal Name — New Signal Name specifies the name of the new signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::NewSigName" "NewSigName" error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input on Configure VIs, Initiate VIs, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-commit-vi.html language=enus -->
## TOPIC 00168: RFmxCDMA2k Commit VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-commit-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-commit-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits settings to the hardware. Calling this VI is optional. RFmxCDMA2k commits settings to the hardware when you call the RFmxCDMA2k Initiate VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signa

### RFmxCDMA2k Commit VI

Commits settings to the hardware. Calling this VI is optional. RFmxCDMA2k commits settings to the hardware when you call the [RFmxCDMA2k Initiate](/csh?topicname=rfmxcdma2k-initiate-vi.html) VI.

[IMAGE alt='icon' src='rfmxcdma2k-commit-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-band-class-vi.html language=enus -->
## TOPIC 00169: RFmxCDMA2k Configure Band Class VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-band-class-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-band-class-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the band class used for the measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: ""

### RFmxCDMA2k Configure Band Class VI

Configures the band class used for the measurement.

[IMAGE alt='icon' src='rfmxcdma2k-configure-band-class-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Band Class — Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. The default value is 0. 0 (0) Specifies the 800 MHz cellular band. 1 (1) Specifies the 1.8 GHz to 2.0 GHz PCS band. 2 (2) Specifies the 872 MHz to 960 MHz TACS band. 3 (3) Specifies the 832 MHz to 925 MHZ JTACS band. 4 (4) Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. 5 (5) Specifies the 450 MHz NMT band. 6 (6) Specifies the 2 GHz IMT-2000 band. 7 (7) Specifies the upper 700 MHz PARMR band. 8 (8) Specifies the 1,800 MHz to 2 GHz band. 9 (9) Specifies the 900 MHz band. 10 (10) Specifies the secondary 1,800 MHz band. 11 (11) Specifies the 400 MHz European PAMR band. 12 (12) Specifies the 800 MHz PAMR band. 14 (14) Specifies the US PCS 1.9 GHz band. 15 (15) Specifies the AWS band. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 (0) | Specifies the 800 MHz cellular band. |
| 1 (1) | Specifies the 1.8 GHz to 2.0 GHz PCS band. |
| 2 (2) | Specifies the 872 MHz to 960 MHz TACS band. |
| 3 (3) | Specifies the 832 MHz to 925 MHZ JTACS band. |
| 4 (4) | Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. |
| 5 (5) | Specifies the 450 MHz NMT band. |
| 6 (6) | Specifies the 2 GHz IMT-2000 band. |
| 7 (7) | Specifies the upper 700 MHz PARMR band. |
| 8 (8) | Specifies the 1,800 MHz to 2 GHz band. |
| 9 (9) | Specifies the 900 MHz band. |
| 10 (10) | Specifies the secondary 1,800 MHz band. |
| 11 (11) | Specifies the 400 MHz European PAMR band. |
| 12 (12) | Specifies the 800 MHz PAMR band. |
| 14 (14) | Specifies the US PCS 1.9 GHz band. |
| 15 (15) | Specifies the AWS band. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-channel-configuration-mode-vi.html language=enus -->
## TOPIC 00170: RFmxCDMA2k Configure Channel Configuration Mode VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-channel-configuration-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-channel-configuration-mode-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures RFmx CDMA2k to detect the channels automatically or to use a specified channel configuration. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used.

### RFmxCDMA2k Configure Channel Configuration Mode VI

Configures RFmx CDMA2k to detect the channels automatically or to use a specified channel configuration.

[IMAGE alt='icon' src='rfmxcdma2k-configure-channel-configuration-mode-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Channel Configuration Mode — Channel Configuration Mode specifies whether to detect the channels automatically or to use a specified channel configuration. This parameter has no effect if radio configuration 1 or 2 (RC1 or RC2) is configured, as RC1 and RC2 always use a single 64-ary Walsh-modulated channel. Auto Detect (0) Specifies that the system automatically detects the channels. User Defined (1) Specifies that the system uses a specific channel configuration. This mode increases measurement speed because no time is spent on channel detection. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Auto Detect (0) | Specifies that the system automatically detects the channels. |
| User Defined (1) | Specifies that the system uses a specific channel configuration. This mode increases measurement speed because no time is spent on channel detection. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00171: RFmxCDMA2k Configure Digital Edge Trigger VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-digital-edge-trigger-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String specifies a selector

### RFmxCDMA2k Configure Digital Edge Trigger VI

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='icon' src='rfmxcdma2k-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital edge trigger. The default value of this parameter is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. Digital Edge — Digital Edge specifies the trigger edge to detect. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
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
| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

Parent topic:

RFmxCDMA2k Configure Trigger VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-channel-number-vi.html language=enus -->
## TOPIC 00172: RFmxCDMA2k Configure Frequency (Channel Number) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-channel-number-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-channel-number-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the

### RFmxCDMA2k Configure Frequency (Channel Number) VI

Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxcdma2k-configure-frequency-channel-number-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Link Direction — Link Direction specifies the direction for which the frequency is calculated. Currently only Uplink is supported. Uplink (1) The frequency is calculated in the reverse link direction, also known as the uplink direction. Band Class — Band Class specifies the band in which the channel is located as defined in Section: 1.5, Table 1.5-1: Band Class List, of the 3GPP2 C.S0057-F specification v1.0. The default value is 0. 0 (0) Specifies the 800 MHz cellular band. 1 (1) Specifies the 1.8 GHz to 2.0 GHz PCS band. 2 (2) Specifies the 872 MHz to 960 MHz TACS band. 3 (3) Specifies the 832 MHz to 925 MHZ JTACS band. 4 (4) Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. 5 (5) Specifies the 450 MHz NMT band. 6 (6) Specifies the 2 GHz IMT-2000 band. 7 (7) Specifies the upper 700 MHz PARMR band. 8 (8) Specifies the 1,800 MHz to 2 GHz band. 9 (9) Specifies the 900 MHz band. 10 (10) Specifies the secondary 1,800 MHz band. 11 (11) Specifies the 400 MHz European PAMR band. 12 (12) Specifies the 800 MHz PAMR band. 14 (14) Specifies the US PCS 1.9 GHz band. 15 (15) Specifies the AWS band. Channel Number — Channel Number specifies the channel number used to build the selector string. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Uplink (1) | The frequency is calculated in the reverse link direction, also known as the uplink direction. |
| 0 (0) | Specifies the 800 MHz cellular band. |
| 1 (1) | Specifies the 1.8 GHz to 2.0 GHz PCS band. |
| 2 (2) | Specifies the 872 MHz to 960 MHz TACS band. |
| 3 (3) | Specifies the 832 MHz to 925 MHZ JTACS band. |
| 4 (4) | Specifies the 1.75 GHz to 1.87 GHz Korean PCS band. |
| 5 (5) | Specifies the 450 MHz NMT band. |
| 6 (6) | Specifies the 2 GHz IMT-2000 band. |
| 7 (7) | Specifies the upper 700 MHz PARMR band. |
| 8 (8) | Specifies the 1,800 MHz to 2 GHz band. |
| 9 (9) | Specifies the 900 MHz band. |
| 10 (10) | Specifies the secondary 1,800 MHz band. |
| 11 (11) | Specifies the 400 MHz European PAMR band. |
| 12 (12) | Specifies the 800 MHz PAMR band. |
| 14 (14) | Specifies the US PCS 1.9 GHz band. |
| 15 (15) | Specifies the AWS band. |

Parent topic:

RFmxCDMA2k Configure Frequency VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-frequency-vi.html language=enus -->
## TOPIC 00173: RFmxCDMA2k Configure Frequency (Frequency) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-frequency-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instan

### RFmxCDMA2k Configure Frequency (Frequency) VI

Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxcdma2k-configure-frequency-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. This value is expressed in Hz. The default value of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k Configure Frequency VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-vi.html language=enus -->
## TOPIC 00174: RFmxCDMA2k Configure Frequency VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency of the RF signal to acquire according to the Center Frequency value in Hz or according to the Channel Number and Band Class values. The signal analyzer tunes to this frequency. icon

### RFmxCDMA2k Configure Frequency VI

Configures the center frequency of the RF signal to acquire according to the **Center Frequency** value in Hz or according to the **Channel Number** and **Band Class** values. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxcdma2k-configure-frequency-vi.png']

- [RFmxCDMA2k Configure Frequency (Frequency) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-frequency-vi.html) Configures the expected carrier frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.
- [RFmxCDMA2k Configure Frequency (Channel Number) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-frequency-channel-number-vi.html) Configures the expected carrier frequency of the RF signal to acquire according to the given channel number. The signal analyzer tunes to this frequency.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-iq-power-edge-trigger-vi.html language=enus -->
## TOPIC 00175: RFmxCDMA2k Configure IQ Power Edge Trigger VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-iq-power-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-iq-power-edge-trigger-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record. To trigger on burst signals, specify a minimum quiet time. The minimum quiet time ensures that the trigger does not occur in the middle of the burst signa

### RFmxCDMA2k Configure IQ Power Edge Trigger VI

Configures the device to wait for the complex power of the I/Q data to cross the specified threshold to mark a reference point within the record.

To trigger on burst signals, specify a minimum quiet time. The minimum quiet time ensures that the trigger does not occur in the middle of the burst signal. The quiet time must be set to a value smaller than the time between bursts but large enough to ignore power changes within a burst.

[IMAGE alt='icon' src='rfmxcdma2k-configure-iq-power-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether the trigger is used. The default value is TRUE. Trigger Delay (s) — Trigger Delay specifies the trigger delay time. This value is expressed in seconds. The default value is 0. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. IQ Power Edge Source — IQ Power Edge Source specifies the channel from which the device monitors the trigger. The default value of this parameter is hardware dependent. IQ Power Edge Slope — IQ Power Edge Slope specifies whether the device asserts the trigger when the signal power is rising or when it is falling. The device asserts the trigger when the signal power exceeds the specified level with the slope you specify. The default value is Rising Slope. Rising Slope (0) The trigger asserts when the signal power is rising. Falling Slope (1) The trigger asserts when the signal power is falling. IQ Power Edge Level (dB or dBm) — IQ Power Edge Level specifies the power level at which the device triggers. This value is expressed in dB when you set the IQ Power Edge Level Type parameter to Relative; and is expressed in dBm when you set the IQ Power Edge Level Type parameter to Absolute. The device asserts the trigger when the signal exceeds the level specified by the value of this parameter, taking into consideration the specified slope. The default of this property is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Minimum Quiet Time Mode — Minimum Quiet Time Mode specifies whether the measurement computes the minimum quiet time used for triggering. The default value is Auto. Manual (0) The minimum quiet time for triggering is the value you specify using the Minimum Quiet Time input. Auto (1) The measurement computes the minimum quiet time used for triggering. Minimum Quiet Time (s) — Minimum Quiet Time specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope parameter to Rising Slope, the signal is quiet while it is below the trigger level. If you set the IQ Power Edge Slope parameter to Falling Slope, the signal is quiet when it is above the trigger level. The default value of this parameter is hardware dependent. IQ Power Edge Level Type — IQ Power Edge Level Type specifies the reference for the IQ Power Edge Level parameter. The IQ Power Edge Level Type parameter is used only when you set the Trigger Type property to IQ Power Edge. Relative (0) The IQ Power Edge Level property is relative to the value of the reference level property. Absolute (1) The IQ Power Edge Level property specifies the absolute power. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Rising Slope (0) | The trigger asserts when the signal power is rising. |
| Falling Slope (1) | The trigger asserts when the signal power is falling. |
| Manual (0) | The minimum quiet time for triggering is the value you specify using the Minimum Quiet Time input. |
| Auto (1) | The measurement computes the minimum quiet time used for triggering. |
| Relative (0) | The IQ Power Edge Level property is relative to the value of the reference level property. |
| Absolute (1) | The IQ Power Edge Level property specifies the absolute power. |

Parent topic:

RFmxCDMA2k Configure Trigger VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-radio-configuration-vi.html language=enus -->
## TOPIC 00176: RFmxCDMA2k Configure Radio Configuration VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-radio-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-radio-configuration-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the radio configuration of the CDMA2k signal. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example

### RFmxCDMA2k Configure Radio Configuration VI

Configures the radio configuration of the CDMA2k signal.

[IMAGE alt='icon' src='rfmxcdma2k-configure-radio-configuration-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Radio Configuration — Radio Configuration specifies the radio configuration of the CDMA2k signal to be analyzed. The default value is RC3. RC1 (0) For Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH) and reverse supplemental code channels (R-SCCHs). For Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). RC2 (1) For Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH and R-SCCHs. For Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. RC3 (2) For Uplink, Radio configuration 3 includes binary phase shift keying (BPSK), R-FCH and reverse supplemental channels (R-SCHs). For Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. RC4 (3) For Uplink, Radio configuration 4 includes BPSK, R-FCH and R-SCHs. For Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. RC5 (4) For Uplink, Radio configuration 5 is not supported. For Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| RC1 (0) | For Uplink, Radio configuration 1 includes 64-ary orthogonal modulation, reverse fundamental channel (R-FCH) and reverse supplemental code channels (R-SCCHs). For Downlink, Radio Configuration 1 includes binary phase-shift keying (BPSK), forward fundamental channels (F-FCHs) and forward supplemental channels (F-SCHs). |
| RC2 (1) | For Uplink, Radio configuration 2 includes 64-ary orthogonal modulation, R-FCH and R-SCCHs. For Downlink, Radio Configuration 2 includes BPSKs, F-FCHs and F-SCHs. |
| RC3 (2) | For Uplink, Radio configuration 3 includes binary phase shift keying (BPSK), R-FCH and reverse supplemental channels (R-SCHs). For Downlink, Radio Configuration 3 includes quadrature phase-shift keying (QPSK), F-FCHs and F-SCHs. |
| RC4 (3) | For Uplink, Radio configuration 4 includes BPSK, R-FCH and R-SCHs. For Downlink, Radio Configuration 4 includes QPSK, F-FCHs and F-SCHs. |
| RC5 (4) | For Uplink, Radio configuration 5 is not supported. For Downlink, Radio Configuration 5 includes QPSK, F-FCHs and F-SCHs. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-reference-level-vi.html language=enus -->
## TOPIC 00177: RFmxCDMA2k Configure Reference Level VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-reference-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-reference-level-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the reference level. The reference level represents the maximum expected power of an input RF signal. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxCDMA2k Configure Reference Level VI

Configures the reference level. The reference level represents the maximum expected power of an input RF signal.

[IMAGE alt='icon' src='rfmxcdma2k-configure-reference-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Level — Reference Level specifies the reference level, which represents the maximum expected power of an RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. The default value of this parameter is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-array-vi.html language=enus -->
## TOPIC 00178: RFmxCDMA2k Configure User Defined Channel (Array) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-array-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures all user-defined channels when you set the Channel Configuration Mode property to User Defined. Use equal-sized arrays for Walsh Code Length, Walsh Code Number, and Branch. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal na

### RFmxCDMA2k Configure User Defined Channel (Array) VI

Configures all user-defined channels when you set the [Channel Configuration Mode](/csh?context=rfmxcdma2k_rfmxcdma2kprop_attr600012) property to **User Defined**.

Use equal-sized arrays for **Walsh Code Length**, **Walsh Code Number**, and **Branch**.

[IMAGE alt='icon' src='rfmxcdma2k-configure-user-defined-channel-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Walsh Code Length — Walsh Code Length specifies an array of the Walsh code length of the CDMA2k signal. The default value is 64. Walsh Code Number — Walsh Code Number specifies an array of the Walsh code number of the CDMA2k signal. The default value is 0. Branch — Branch specifies an array of the branch on which a specific user-defined channel is mapped. The default value is I. I (0) Specifies the in-phase branch. Q (1) Specifies the quadrature branch. I and Q (2) Specifies the in-phase and quadrature branch. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | Specifies the in-phase branch. |
| Q (1) | Specifies the quadrature branch. |
| I and Q (2) | Specifies the in-phase and quadrature branch. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-vi.html language=enus -->
## TOPIC 00179: RFmxCDMA2k Configure User Defined Channel VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-configure-user-defined-channel-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an individual user-defined channel when the channel configuration mode is set to User Defined. Use "channel<n>" as the selector string to configure this VI. A channel is defined by the Walsh code length and number and the quadrature branch on which it is mapped. icon Inputs/Outputs cstr.p

### RFmxCDMA2k Configure User Defined Channel VI

Configures an individual user-defined channel when the channel configuration mode is set to **User Defined**.

Use "channel<n>" as the selector string to configure this VI.

A channel is defined by the Walsh code length and number and the quadrature branch on which it is mapped.

[IMAGE alt='icon' src='rfmxcdma2k-configure-user-defined-channel-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and channel number. If you do not specify the signal name, the default signal instance is used. The default value is "channel0". Examples: "channel0" "signal::sig1/channel0" You can use the RFmxCDMA2k Build Channel String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Walsh Code Length — Walsh Code Length specifies the Walsh code length of a specific user-defined channel. The default value is 64. Walsh Code Number — Walsh Code Number specifies the Walsh code number of a specific user-defined channel. The default value is 0. Branch — Branch specifies the branch on which a specific user-defined channel is mapped. The default value is I. I (0) Specifies the in-phase branch. Q (1) Specifies the quadrature branch. I and Q (2) Specifies the in-phase and quadrature branch. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | Specifies the in-phase branch. |
| Q (1) | Specifies the quadrature branch. |
| I and Q (2) | Specifies the in-phase and quadrature branch. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-create-signal-configuration-vi.html language=enus -->
## TOPIC 00180: RFmxCDMA2k Create Signal Configuration VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-create-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-create-signal-configuration-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::sig1" "sig1" cgenclassrntag.png Instrument Handle In Instrument Handle In specifies

### RFmxCDMA2k Create Signal Configuration VI

Creates a new instance of a signal.

[IMAGE alt='icon' src='rfmxcdma2k-create-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input on Configure VIs, Initiate VIs, and Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-delete-signal-configuration-vi.html language=enus -->
## TOPIC 00181: RFmxCDMA2k Delete Signal Configuration VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-delete-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-delete-signal-configuration-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::sig1" "sig1" cgenclassrntag.png Instrumen

### RFmxCDMA2k Delete Signal Configuration VI

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='icon' src='rfmxcdma2k-delete-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This input accepts the signal name with or without the "signal::" prefix. Examples: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-disable-trigger-vi.html language=enus -->
## TOPIC 00182: RFmxCDMA2k Disable Trigger VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-disable-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-disable-trigger-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name

### RFmxCDMA2k Disable Trigger VI

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='icon' src='rfmxcdma2k-disable-trigger-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k Configure Trigger VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-initiate-vi.html language=enus -->
## TOPIC 00183: RFmxCDMA2k Initiate VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-initiate-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node

### RFmxCDMA2k Initiate VI

Initiates all enabled measurements. Call this VI after configuring the signal and measurement.

This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxCDMA2k Wait for Measurement Complete](rfmxcdma2k-wait-for-measurement-complete-vi.html) VI or [RFmxCDMA2k Check Measurement Status](rfmxcdma2k-check-measurement-status-vi.html) VI.

[IMAGE alt='icon' src='rfmxcdma2k-initiate-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result:" prefix. The default value is "" (empty string), which refers to the default result instance. Examples: "" "result::r1" "r1" Selector String — Selector String specifies a selector string comprising the signal name and the result name. The result name can either by specified through this input or the Result Name input. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this input, either the result name specified by the Result Name input or the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String input on Fetch VIs when using named signal configurations or named results. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

CDMA2k

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00184: RFmxCDMA2k ModAcc Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The d

### RFmxCDMA2k ModAcc Configure Synchronization Mode and Interval VI

Configures the synchronization mode, offset, and length for modulation accuracy (ModAcc) analysis.

[IMAGE alt='icon' src='rfmxcdma2k-modacc-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame, slot, or symbol boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. Arbitrary (2) The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. Measurement Length (slots) — Measurement Length specifies the duration of the modulation accuracy measurement. This value is expressed in slots. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the slot boundary. |
| Arbitrary (2) | The symbol boundary is detected and the measurement is performed over the number of slots expressed by the Measurement Length parameter, starting at Measurement Offset slots from the symbol boundary. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00185: RFmxCDMA2k ModAcc Fetch IQ Impairments VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-iq-impairments-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the origin offset, gain imbalance, and quadrature error. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify t

### RFmxCDMA2k ModAcc Fetch IQ Impairments VI

Returns the origin offset, gain imbalance, and quadrature error.

[IMAGE alt='icon' src='rfmxcdma2k-modacc-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. I/Q Origin Offset (dB) — I/Q Origin Offset returns the I/Q origin offset of the composite signal. This value is expressed in dB. I/Q Gain Imbalance (dB) — I/Q Gain Imbalance returns the I/Q gain imbalance of the composite signal. This value is expressed in dB. I/Q Quadrature Error (deg) — I/Q Quadrature Error returns the I/Q quadrature error of the composite signal. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00186: RFmxCDMA2k ModAcc Fetch Magnitude Error Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-magnitude-error-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If y

### RFmxCDMA2k ModAcc Fetch Magnitude Error Trace VI

Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement.

[IMAGE alt='icon' src='rfmxcdma2k-modacc-fetch-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Magnitude Error (%) — Magnitude Error returns the trace of the magnitude errors of the corrected composite signal. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the array of the magnitude error values. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the chip duration. This value is expressed in seconds. y — y returns the array of the magnitude error values. This value is expressed as a percentage. |

Parent topic:

RFmxCDMA2k ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-peak-cde-vi.html language=enus -->
## TOPIC 00187: RFmxCDMA2k ModAcc Fetch Peak CDE VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-peak-cde-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-peak-cde-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum value among the code domain errors (CDEs), in dB. This VI calculates the CDEs by projecting the descrambled error vector onto the code domain at a specific spreading factor. The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the p

### RFmxCDMA2k ModAcc Fetch Peak CDE VI

Returns the maximum value among the code domain errors (CDEs), in dB.

This VI calculates the CDEs by projecting the descrambled error vector onto the code domain at a specific spreading factor.

The CDE for every code with a specific spreading factor is defined as the ratio of the mean power of the projection onto that code to the mean power of the composite reference waveform. A fixed spreading factor of 32 is used.

This VI computes the CDEs separately for I and Q branches.

[IMAGE alt='icon' src='rfmxcdma2k-modacc-fetch-peak-cde-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Peak CDE Branch — Peak CDE Branch returns the branch of the channel corresponding to the Peak CDE value. I (0) The signal is modulated on the in-phase branch. Q (1) The signal is modulated on the quadrature branch. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Peak CDE (dB) — Peak CDE returns the maximum value among the code domain errors. This value is expressed in dB. Peak CDE Walsh Code Number — Peak CDE Walsh Code Number returns the code number of the channel corresponding to the Peak CDE value. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| I (0) | The signal is modulated on the in-phase branch. |
| Q (1) | The signal is modulated on the quadrature branch. |

Parent topic:

RFmxCDMA2k ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-vi.html language=enus -->
## TOPIC 00188: RFmxCDMA2k ModAcc Fetch VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc measurement results. icon

### RFmxCDMA2k ModAcc Fetch VI

Fetches the ModAcc measurement results.

[IMAGE alt='icon' src='rfmxcdma2k-modacc-fetch-vi.png']

- [RFmxCDMA2k ModAcc Fetch EVM VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-evm-vi.html) Returns the EVM value and related measurement values of the modulation accuracy (ModAcc) of the CDMA2k signal.
- [RFmxCDMA2k ModAcc Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-iq-impairments-vi.html) Returns the origin offset, gain imbalance, and quadrature error.
- [RFmxCDMA2k ModAcc Fetch Peak CDE VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-peak-cde-vi.html) Returns the maximum value among the code domain errors (CDEs), in dB.
- [RFmxCDMA2k ModAcc Fetch Peak Active CDE VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-peak-active-cde-vi.html) Returns the peak value among the code domain errors of the active channels, along with the code number and the code length.
- [RFmxCDMA2k ModAcc Fetch Number of Detected Channels VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-number-of-detected-channels-vi.html) Returns the total number of detected channels. If the you set the Channel Configuration Mode property to User Defined , the measurement returns the number of configured channels.
- [RFmxCDMA2k ModAcc Fetch Detected Channel VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-detected-channel-vi.html) Returns a detected channel by its channel name.
- [RFmxCDMA2k ModAcc Fetch Detected Channel (Array) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-detected-channel-array-vi.html) Returns the detected channels. If you set the Channel Configuration Mode property to User Defined , the measurement returns the configured channels.
- [RFmxCDMA2k ModAcc Fetch EVM Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-evm-trace-vi.html) Returns the EVM trace of the ModAcc measurement.
- [RFmxCDMA2k ModAcc Fetch Magnitude Error Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-magnitude-error-trace-vi.html) Returns the magnitude error trace for the modulation accuracy (ModAcc) measurement.
- [RFmxCDMA2k ModAcc Fetch Phase Error Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-phase-error-trace-vi.html) Returns the phase error trace of the ModAcc measurement.
- [RFmxCDMA2k ModAcc Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-modacc-fetch-constellation-trace-vi.html) Returns the complex chips of the corrected composite signal for the modulation accuracy (ModAcc) measurement.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-obw-configure-averaging-vi.html language=enus -->
## TOPIC 00189: RFmxCDMA2k OBW Configure Averaging VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-obw-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-obw-configure-averaging-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "sign

### RFmxCDMA2k OBW Configure Averaging VI

Configures averaging for the OBW measurement.

[IMAGE alt='icon' src='rfmxcdma2k-obw-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The OBW measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the OBW measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The OBW measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the OBW measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

OBW

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-obw-fetch-measurement-vi.html language=enus -->
## TOPIC 00190: RFmxCDMA2k OBW Fetch Measurement VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-obw-fetch-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-obw-fetch-measurement-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the OBW measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result i

### RFmxCDMA2k OBW Fetch Measurement VI

Returns the OBW measurement.

[IMAGE alt='icon' src='rfmxcdma2k-obw-fetch-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Stop Frequency (Hz) — Stop Frequency returns the stop frequency of the OBW. This value is expressed in Hz. Start Frequency (Hz) — Start Frequency returns the start frequency of the OBW. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Occupied Bandwidth (Hz) — Occupied Bandwidth returns the occupied bandwidth. This value is expressed in Hz. The OBW is calculated using the following formula: OBW = Stop Frequency - Start Frequency Absolute Power (dBm) — Absolute Power returns the total integrated power of the spectrum acquired by the OBW measurement. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k OBW Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-configure-averaging-vi.html language=enus -->
## TOPIC 00191: RFmxCDMA2k QEVM Configure Averaging VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-configure-averaging-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal:

### RFmxCDMA2k QEVM Configure Averaging VI

Configures averaging for QEVM measurement.

[IMAGE alt='icon' src='rfmxcdma2k-qevm-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The QEVM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the QEVM measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The QEVM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the QEVM measurement is averaged. |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-configure-measurement-length-vi.html language=enus -->
## TOPIC 00192: RFmxCDMA2k QEVM Configure Measurement Length VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-configure-measurement-length-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-configure-measurement-length-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of chips used for a single QEVM measurement iteration. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (em

### RFmxCDMA2k QEVM Configure Measurement Length VI

Configures the number of chips used for a single QEVM measurement iteration.

[IMAGE alt='icon' src='rfmxcdma2k-qevm-configure-measurement-length-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement Length (chips) — Measurement Length specifies the number of chips used for a single measurement. The default value is 1536. The valid values range from 700 to 2500, inclusive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

QEVM

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-fetch-constellation-trace-vi.html language=enus -->
## TOPIC 00193: RFmxCDMA2k QEVM Fetch Constellation Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-fetch-constellation-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-fetch-constellation-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the complex chips of the corrected received signal for the QEVM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If

### RFmxCDMA2k QEVM Fetch Constellation Trace VI

Returns the complex chips of the corrected received signal for the QEVM measurement.

[IMAGE alt='icon' src='rfmxcdma2k-qevm-fetch-constellation-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Constellation — Constellation returns the array of complex chips of the corrected signal on which the QEVM measurements are performed. You can use these chips to obtain the constellation diagram. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-fetch-iq-impairments-vi.html language=enus -->
## TOPIC 00194: RFmxCDMA2k QEVM Fetch IQ Impairments VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-fetch-iq-impairments-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-qevm-fetch-iq-impairments-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measured I/Q impairments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default

### RFmxCDMA2k QEVM Fetch IQ Impairments VI

Returns the measured I/Q impairments.

[IMAGE alt='icon' src='rfmxcdma2k-qevm-fetch-iq-impairments-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Maximum I/Q Gain Imbalance (dB) — Maximum I/Q Gain Imbalance returns the maximum I/Q gain imbalance of the received signal. This value is expressed in dB. Maximum I/Q Origin Offset (dB) — Maximum I/Q Origin Offset returns the maximum origin offset of the received signal. This value is expressed in dB. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean I/Q Origin Offset (dB) — Mean I/Q Origin Offset returns the mean averaged origin offset of the received signal. This value is expressed in dB. Mean I/Q Gain Imbalance (dB) — Mean I/Q Gain Imbalance returns the mean I/Q gain imbalance of the received signal. This value is expressed in dB. Mean I/Q Quadrature Error (deg) — Mean I/Q Quadrature Error returns the mean I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. error out — error out contains error information. This output provides standard error out functionality. Maximum I/Q Quadrature Error (deg) — Maximum I/Q Quadrature Error returns the maximum I/Q quadrature error (phase imbalance) of the received signal. This value is expressed in degrees. |
| --- |

Parent topic:

RFmxCDMA2k QEVM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-reset-to-default-vi.html language=enus -->
## TOPIC 00195: RFmxCDMA2k Reset to Default VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-reset-to-default-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal configuration to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "

### RFmxCDMA2k Reset to Default VI

Resets a signal configuration to the default values.

[IMAGE alt='icon' src='rfmxcdma2k-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-select-measurement-vi.html language=enus -->
## TOPIC 00196: RFmxCDMA2k Select Measurement VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-select-measurement-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To enable multiple measurements, use the Multiple Measurements instance. To enable a single measurement, use the Single Measurement instance. icon

### RFmxCDMA2k Select Measurement VI

Specifies the measurements that you want to enable. To enable multiple measurements, use the **Multiple Measurements** instance. To enable a single measurement, use the **Single Measurement** instance.

[IMAGE alt='icon' src='rfmxcdma2k-select-measurement-vi.png']

- [RFmxCDMA2k Select Measurement (Single) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxCDMA2k Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

CDMA2k

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-configure-averaging-vi.html language=enus -->
## TOPIC 00197: RFmxCDMA2k SEM Configure Averaging VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-configure-averaging-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "sign

### RFmxCDMA2k SEM Configure Averaging VI

Configures averaging for the SEM measurement.

[IMAGE alt='icon' src='rfmxcdma2k-sem-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The SEM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the SEM measurement is averaged. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. RFmx uses the averaged spectrum for the measurement. The default value is RMS. RMS (0) The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The power spectrum is averaged in a logarithmic scale. Scalar (2) The square root of the power spectrum is averaged. Max (3) The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. Min (4) The least power in the spectrum at each frequency bin is retained from one acquisition to the next. Refer to the Averaging section of the Spectrum topic for more information about averaging types. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The SEM measurement uses the Averaging Count parameter to calculate the number of acquisitions over which the SEM measurement is averaged. |
| RMS (0) | The power spectrum is linearly averaged. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The power spectrum is averaged in a logarithmic scale. |
| Scalar (2) | The square root of the power spectrum is averaged. |
| Max (3) | The peak power in the spectrum at each frequency bin is retained from one acquisition to the next. |
| Min (4) | The least power in the spectrum at each frequency bin is retained from one acquisition to the next. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-configure-sweep-time-vi.html language=enus -->
## TOPIC 00198: RFmxCDMA2k SEM Configure Sweep Time VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-configure-sweep-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-configure-sweep-time-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the sweep time. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can u

### RFmxCDMA2k SEM Configure Sweep Time VI

Configures the sweep time.

[IMAGE alt='icon' src='rfmxcdma2k-sem-configure-sweep-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Sweep Time Auto — Sweep Time Auto specifies whether the measurement computes the sweep time. The default value is True. False (0) The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. True (1) The measurement uses the default sweep time of 0.001667 seconds. Sweep Time Interval (s) — Sweep Time Interval specifies the sweep time when you set the Sweep Time Auto parameter to False. This value is expressed in seconds. The default value is 1.67 ms. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement uses the sweep time that you specify using the Sweep Time Interval parameter. |
| True (1) | The measurement uses the default sweep time of 0.001667 seconds. |

Parent topic:

SEM

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-carrier-absolute-integrated-power-vi.html language=enus -->
## TOPIC 00199: RFmxCDMA2k SEM Fetch Carrier Absolute Integrated Power VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-carrier-absolute-integrated-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-carrier-absolute-integrated-power-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the absolute carrier integrated power of the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not spec

### RFmxCDMA2k SEM Fetch Carrier Absolute Integrated Power VI

Returns the absolute carrier integrated power of the SEM measurement.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-carrier-absolute-integrated-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Carrier Absolute Integrated Power (dBm) — Carrier Absolute Integrated Power returns the averaged integrated channel power measured in the specified integration bandwidth. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-margin-array-vi.html language=enus -->
## TOPIC 00200: RFmxCDMA2k SEM Fetch Lower Offset Margin (Array) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-margin-array-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the array of measurement status and margins from the limit line measured in the lower offset segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default si

### RFmxCDMA2k SEM Fetch Lower Offset Margin (Array) VI

Returns the array of measurement status and margins from the limit line measured in the lower offset segments.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-lower-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the array of powers at which the margin occurred in each lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the array of powers at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the array of lower offset measurement status based on measurement limits and the failure criteria specified by the standard. Fail (0) The measurement fails according to the measurement limits specified by this standard. Pass (1) The measurement passes according to the measurement limits specified by this standard. Margin (dB) — Margin returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the maximum difference between the spectrum and the limit mask. Margin Frequency (Hz) — Margin Frequency returns the array of frequencies at which the margin occurred in each lower (negative) offset segment. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-margin-vi.html language=enus -->
## TOPIC 00201: RFmxCDMA2k SEM Fetch Lower Offset Margin VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-margin-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-margin-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the lower offset segment. Use "offset<n>" as the selector string to read parameters from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result n

### RFmxCDMA2k SEM Fetch Lower Offset Margin VI

Returns the measurement status and margin from the limit line measured in the lower offset segment.

Use "offset<n>" as the selector string to read parameters from this VI.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-lower-offset-margin-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxCDMA2k Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the power at which the margin occurred in the lower (negative) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the power at which the margin occurred in the lower (negative) offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the lower offset measurement status based on measurement limits and the failure criteria specified by the standard. Fail (0) The measurement fails according to the measurement limits specified by this standard. Pass (1) The measurement passes according to the measurement limits specified by this standard. Margin (dB) — Margin returns the margin from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). Margin Frequency (Hz) — Margin Frequency returns the frequency at which the margin occurred in the lower (negative) offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-power-array-vi.html language=enus -->
## TOPIC 00202: RFmxCDMA2k SEM Fetch Lower Offset Power (Array) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-power-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-power-array-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the arrays of lower offset segment power measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the

### RFmxCDMA2k SEM Fetch Lower Offset Power (Array) VI

Returns the arrays of lower offset segment power measurements.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-lower-offset-power-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the array of peak powers in the lower (negative) offset segment relative to the carrier absolute integrated power. Peak Frequency (Hz) — Peak Frequency returns the array of frequencies at which the peak power occurred in each offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the array of lower (negative) offset segment powers measured. Relative Integrated Power (dB) — Relative Integrated Power returns the array of powers in each lower (negative) offset segment relative to the carrier absolute integrated power. Absolute Peak Power (dBm) — Absolute Peak Power returns the array of peak powers measured in each lower (negative) offset segment. The power is measured in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-power-vi.html language=enus -->
## TOPIC 00203: RFmxCDMA2k SEM Fetch Lower Offset Power VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-power-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-lower-offset-power-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the lower offset segment power measurements. Use "offset<n>" as the selector string to read parameters from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify t

### RFmxCDMA2k SEM Fetch Lower Offset Power VI

Returns the lower offset segment power measurements.

Use "offset<n>" as the selector string to read parameters from this VI.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-lower-offset-power-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and offset number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Examples: "offset0" "signal::sig1/offset0" "result::r1/offset0" "signal::sig1/result::r1/offset0" You can use the RFmxCDMA2k Build Offset String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Relative Peak Power (dB) — Relative Peak Power returns the peak power in the lower (negative) offset segment relative to the carrier absolute integrated power. Peak Frequency (Hz) — Peak Frequency returns the frequency at which the peak power occurred in the offset segment. This value is expressed in Hz. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Absolute Integrated Power (dBm) — Absolute Integrated Power returns the lower (negative) offset segment power measured. Relative Integrated Power (dB) — Relative Integrated Power returns the power in the lower (negative) offset segment relative to the carrier absolute integrated power. Absolute Peak Power (dBm) — Absolute Peak Power returns the peak power measured in the lower (negative) offset segment. The power is measured in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00204: RFmxCDMA2k SEM Fetch Measurement Status VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-measurement-status-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SEM measurement status. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default r

### RFmxCDMA2k SEM Fetch Measurement Status VI

Returns the SEM measurement status.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the overall measurement status based on the measurement limits which are specified by the standard for each offset segment. Fail (0) The measurement fails according to the measurement limits specified by this standard. Pass (1) The measurement passes according to the measurement limits specified by this standard. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-spectrum-vi.html language=enus -->
## TOPIC 00205: RFmxCDMA2k SEM Fetch Spectrum VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-spectrum-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-spectrum-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the spectrum used for the SEM measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxCDMA2k SEM Fetch Spectrum VI

Returns the spectrum used for the SEM measurement.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-spectrum-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Spectrum (dBm) — Spectrum returns the trace of power levels in the spectral domain. This value is expressed in dBm. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. Relative Mask (dB) — Relative Mask returns the trace of power levels representing the relative mask in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of power levels for relative mask. This value is expressed in dB. Absolute Mask (dBm) — Absolute Mask returns the trace of power levels representing the absolute mask in the spectral domain. x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of power levels for absolute mask. This value is expressed in dBm. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of averaged powers measured at each frequency bin. This value is expressed in dBm. |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of power levels for relative mask. This value is expressed in dB. |
| x0 — x0 returns the start frequency. This value is expressed in Hz. dx — dx returns the frequency bin spacing. This value is expressed in Hz. y — y returns the array of power levels for absolute mask. This value is expressed in dBm. |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-upper-offset-margin-array-vi.html language=enus -->
## TOPIC 00206: RFmxCDMA2k SEM Fetch Upper Offset Margin (Array) VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-upper-offset-margin-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-sem-fetch-upper-offset-margin-array-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the measurement status and margin from the limit line measured in the upper offset segments. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal insta

### RFmxCDMA2k SEM Fetch Upper Offset Margin (Array) VI

Returns the measurement status and margin from the limit line measured in the upper offset segments.

[IMAGE alt='icon' src='rfmxcdma2k-sem-fetch-upper-offset-margin-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Margin Relative Power (dB) — Margin Relative Power returns the array of powers at which the margin occurred in each upper (positive) offset segment relative to the carrier absolute integrated power. This value is expressed in dB. Margin Absolute Power (dBm) — Margin Absolute Power returns the array of powers at which the margin occurred in each upper (positive) offset segment. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status returns the array of upper offset measurement statuses based on measurement limits and the failure criteria specified by the standard. Fail (0) The measurement fails according to the measurement limits specified by this standard. Pass (1) The measurement passes according to the measurement limits specified by this standard. Margin (dB) — Margin returns the array of margins from the limit mask value specified by the standard. This value is expressed in dB. Margin is defined as the minimum difference between the spectrum and the closest limit mask (absolute or relative). Margin Frequency (Hz) — Margin Frequency returns the array of frequencies at which the margin occurred in each upper (positive) offset. This value is expressed in Hz. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The measurement fails according to the measurement limits specified by this standard. |
| Pass (1) | The measurement passes according to the measurement limits specified by this standard. |

Parent topic:

RFmxCDMA2k SEM Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-configure-synchronization-mode-and-interval-vi.html language=enus -->
## TOPIC 00207: RFmxCDMA2k SlotPhase Configure Synchronization Mode and Interval VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-configure-synchronization-mode-and-interval-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-configure-synchronization-mode-and-interval-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Synchronization Mode, Measurement Offset, and Measurement Length parameters of the SlotPhase measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal i

### RFmxCDMA2k SlotPhase Configure Synchronization Mode and Interval VI

Configures the **Synchronization Mode**, **Measurement Offset**, and **Measurement Length** parameters of the SlotPhase measurement.

[IMAGE alt='icon' src='rfmxcdma2k-slotphase-configure-synchronization-mode-and-interval-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Synchronization Mode — Synchronization Mode specifies whether the measurement is performed from the frame or slot boundary. The default value is Slot. Frame (0) The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. Slot (1) The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. Measurement Offset (slots) — Measurement Offset specifies the measurement offset to skip from the synchronization boundary. This value is expressed in slots. The synchronization boundary is specified by the Synchronization Mode parameter. The default value is 0. Measurement Length (slots) — Measurement Length specifies the duration of the SlotPhase measurement. This value is expressed in slots. The default value is 16. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Frame (0) | The frame boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the frame boundary. |
| Slot (1) | The slot boundary is detected, and the measurement is performed over the number of slots specified by the Measurement Length parameter starting at the Measurement Offset slots from the slot boundary. |

Parent topic:

SlotPhase

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html language=enus -->
## TOPIC 00208: RFmxCDMA2k SlotPhase Fetch Chip Phase Error Linear Fit Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of th

### RFmxCDMA2k SlotPhase Fetch Chip Phase Error Linear Fit Trace VI

Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the slot boundary and extrapolates the phase error to the slot boundaries.

[IMAGE alt='icon' src='rfmxcdma2k-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Chip Phase Error Linear Fit (deg) — Chip Phase Error Linear Fit returns the chip phase error linear fit trace for the SlotPhase measurement. This value is expressed in degrees. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the delta parameter. y — y returns the array of chip phase error for the SlotPhase measurement. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the delta parameter. y — y returns the array of chip phase error for the SlotPhase measurement. |

Parent topic:

RFmxCDMA2k SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-trace-vi.html language=enus -->
## TOPIC 00209: RFmxCDMA2k SlotPhase Fetch Chip Phase Error Trace VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-trace-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name.

### RFmxCDMA2k SlotPhase Fetch Chip Phase Error Trace VI

Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform.

[IMAGE alt='icon' src='rfmxcdma2k-slotphase-fetch-chip-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Chip Phase Error (deg) — Chip Phase Error returns the chip phase error for the SlotPhase measurement. This value is expressed in degrees. x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the delta parameter. y — y returns the array of chip phase error for the SlotPhase measurement. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time. This value is expressed in seconds. dx — dx returns the delta parameter. y — y returns the array of chip phase error for the SlotPhase measurement. |

Parent topic:

RFmxCDMA2k SlotPhase Fetch VI

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-vi.html language=enus -->
## TOPIC 00210: RFmxCDMA2k SlotPhase Fetch VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the SlotPhase measurement results. icon

### RFmxCDMA2k SlotPhase Fetch VI

Fetches the SlotPhase measurement results.

[IMAGE alt='icon' src='rfmxcdma2k-slotphase-fetch-vi.png']

- [RFmxCDMA2k SlotPhase Fetch Phase Discontinuities VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-phase-discontinuities-vi.html) Fetches the phase discontinuity values for the slot boundaries in the measurement interval.
- [RFmxCDMA2k SlotPhase Fetch Maximum Phase Discontinuity VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-maximum-phase-discontinuity-vi.html) Fetches the maximum phase discontinuity value observed in the measurement interval.
- [RFmxCDMA2k SlotPhase Fetch Chip Phase Error Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-trace-vi.html) Fetches the chip phase error trace for the SlotPhase measurement. The chip phase error is the phase error between the received waveform and the reference waveform.
- [RFmxCDMA2k SlotPhase Fetch Chip Phase Error Linear Fit Trace VI](../../../../../vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-slotphase-fetch-chip-phase-error-linear-fit-trace-vi.html) Fetches the chip phase error trace linear fit trace for the SlotPhase measurement. The linear fit is obtained from the chip phase error on a slot basis. If a transient duration greater than zero is configured, the linear fit computation ignores the data of the transient duration on either side of the slot boundary and extrapolates the phase error to the slot boundaries.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00211: RFmxCDMA2k Wait for Measurement Complete VI

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/rfmxcdma2k-wait-for-measurement-complete-vi.html
- document_id: `rfmxcdma2k-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number of seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you d

### RFmxCDMA2k Wait for Measurement Complete VI

Waits for the specified number of seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxcdma2k-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Examples: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxCDMA2k Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxcdma2k-labview-api-ref path=vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00212: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxcdma2k-labview-api-ref`
- source_path: `vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxcdma2k-labview-api-ref/raw/resource/enus/vi-lib/rfmx/cdma2k/mx/rfmxcdma2k-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxcdma2k-labview-api-ref`
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
