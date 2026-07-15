# NI DOCUMENT BUNDLE: rfmxgsm-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxgsm-labview-api-ref start=1 end=108 -->
<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/configuration/dir-mnu.html language=enus -->
## TOPIC 00001: Configuration

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/configuration/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/configuration/dir-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure measurements. You can use the RFmxGSM Property Node to configure additional properties. icon

### Configuration

Use the VIs on this palette to configure measurements. You can use the RFmxGSM Property Node to configure additional properties.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxGSM Configure RF VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-rf-vi.html) Configures the RF properties of the signal specified by the selector string.
- [RFmxGSM Configure Frequency VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-vi.html) Configures the expected center frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.
- [RFmxGSM Configure Reference Level VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-reference-level-vi.html) Configures the reference level, which represents the maximum expected power of an RF input signal.
- [RFmxGSM Auto Level VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-auto-level-vi.html) Examines the input signal to calculate the peak power level and sets it as the value of the Reference Level property. Use this VI to help calculate an approximate setting for the reference level.
- [RFmxGSM Configure External Attenuation VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-external-attenuation-vi.html) Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer.
- [RFmxGSM Configure Trigger VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-trigger-vi.html) Configures the Reference Trigger used to acquire the signal.
- [RFmxGSM Send Software Edge Trigger VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-send-software-edge-trigger-vi.html) Sends a trigger to the device when you use the RFmxGSM Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.
- [RFmxGSM Configure Link Direction VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-link-direction-vi.html) Configures the source of the signal to be measured.
- [RFmxGSM Configure Signal Type VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-signal-type-vi.html) Configures the signal type.
- [RFmxGSM Configure Auto TSC Detection Enabled VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-auto-tsc-detection-enabled-vi.html) Configures whether to auto detect the training sequence code (TSC).
- [RFmxGSM Configure TSC VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-tsc-vi.html) Configures the training sequence code (TSC) in the burst.
- [RFmxGSM Configure Number of Timeslots VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-number-of-timeslots-vi.html) Configures the number of time slots to be measured.
- [RFmxGSM Configure Band VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-band-vi.html) Configures the band of operation.
- [RFmxGSM Configure Power Control Level VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-power-control-level-vi.html) Configures the power control level corresponding to the transmitted power.
- [RFmxGSM Configure Burst Synchronization Type VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-burst-synchronization-type-vi.html) Configures the burst synchronization type.
- [RFmxGSM Build Slot String VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-build-slot-string-vi.html) Creates a slot string to be used as the selector string with configuration or fetch properties and VIs.
- [ModAcc](../../../../../../menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-modacc-mnu.html) Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements.
- [ORFS](../../../../../../menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-orfs-mnu.html) Use the VIs on this palette to configure output radio frequency spectrum (ORFS) measurements.
- [PVT](../../../../../../menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-pvt-mnu.html) Use the VIs on this palette to configure power versus time (PVT) measurements.

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-modacc-mnu.html language=enus -->
## TOPIC 00002: ModAcc

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-modacc-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-modacc-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements. icon

### ModAcc

Use the VIs on this palette to configure modulation accuracy (ModAcc) measurements.

[IMAGE alt='icon' src='rfmx-gsm-mx-configuration-modacc-mnu.png']

- [RFmxGSM ModAcc Configure Droop Compensation Enabled VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-configure-droop-compensation-enabled-vi.html) Configures whether to enable droop compensation for the modulation accuracy (ModAcc) measurement.
- [RFmxGSM ModAcc Configure Averaging VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-configure-averaging-vi.html) Configures averaging for the modulation accuracy (ModAcc) measurement.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-orfs-mnu.html language=enus -->
## TOPIC 00003: ORFS

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-orfs-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-orfs-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure output radio frequency spectrum (ORFS) measurements. icon

### ORFS

Use the VIs on this palette to configure output radio frequency spectrum (ORFS) measurements.

[IMAGE alt='icon' src='rfmx-gsm-mx-configuration-orfs-mnu.png']

- [RFmxGSM ORFS Configure Measurement Type VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-measurement-type-vi.html) Configures the type of spectral distortion to be measured.
- [RFmxGSM ORFS Configure Averaging VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-averaging-vi.html) Configures averaging for the output radio frequency spectrum (ORFS) measurement.
- [RFmxGSM ORFS Configure Offset Frequency Mode VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-offset-frequency-mode-vi.html) Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.
- [RFmxGSM ORFS Configure Evaluation Symbols VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-evaluation-symbols-vi.html) Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average.
- [RFmxGSM ORFS Configure Noise Compensation Enabled VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-noise-compensation-enabled-vi.html) Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.
- [RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-modulation-custom-offset-frequency-array-vi.html) Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of modulation when you set the ORFS Offset Freq Mode property to Custom .
- [RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-switching-custom-offset-frequency-array-vi.html) Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the ORFS Offset Freq Mode property to Custom .

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-pvt-mnu.html language=enus -->
## TOPIC 00004: PVT

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-pvt-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/configuration/rfmx-gsm-mx-configuration-pvt-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure power versus time (PVT) measurements. icon

### PVT

Use the VIs on this palette to configure power versus time (PVT) measurements.

[IMAGE alt='icon' src='rfmx-gsm-mx-configuration-pvt-mnu.png']

- [RFmxGSM PVT Configure Averaging VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-configure-averaging-vi.html) Configures averaging for the power versus time (PVT) measurement.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/dir-mnu.html language=enus -->
## TOPIC 00005: GSM

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/dir-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to perform GSM measurements. You can use the RFmxGSM Property Node to configure additional properties. © 2015–2026 National Instruments Corporation. All rights reserved. icon

### GSM

Use the VIs on this palette to perform GSM measurements. You can use the RFmxGSM Property Node to configure additional properties.

© 2015–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [Configuration](../../../../../menus/categories/measurement/rfmx/gsm/configuration/dir-mnu.html) Use the VIs on this palette to configure measurements. You can use the RFmxGSM Property Node to configure additional properties.
- [RFmxGSM Select Measurement VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-vi.html) Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.
- [RFmxGSM Initiate VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-initiate-vi.html) Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxGSM Wait for Measurement Complete VI or RFmxGSM Check Measurement Status VI.
- [Fetch](../../../../../menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-fetch-mnu.html) Use the VIs on this palette to fetch measurement results and traces.
- [Utility](../../../../../menus/categories/measurement/rfmx/gsm/utility/dir-mnu.html) Use the VIs on this palette to configure utility measurements. You can use the RFmxGSM Property Node to configure additional properties.
- [RFmxGSM Property Node VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-property-node-vi.html) Gets (reads), sets (writes), or resets (sets to default value) RFmxGSM properties.
- [Advanced](../../../../../menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-advanced-mnu.html) Use the VIs on this palette to use advanced features.
- [Build String](../../../../../menus/categories/measurement/rfmx/gsm/utility/rfmx-gsm-mx-utility-build-string-mnu.html) Use the VIs on this palette to create strings for configurations that require a selector string.

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-advanced-mnu.html language=enus -->
## TOPIC 00006: Advanced

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-advanced-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. icon

### Advanced

Use the VIs on this palette to use advanced features.

[IMAGE alt='icon' src='rfmx-gsm-mx-advanced-mnu.png']

- [RFmxGSM Abort Measurements VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-abort-measurements-vi.html) Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. This acquisition and measurements were previously initiated by the RFmxGSM Initiate VI. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.
- [RFmxGSM Analyze (IQ, 1 Wfm) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-analyze-iq-1-wfm-vi.html) Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended Acquisition Type property value is IQ .
- [RFmxGSM Create Signal Configuration VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-create-signal-configuration-vi.html) Creates a new instance of a signal.
- [RFmxGSM Clone Signal Configuration VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clone-signal-configuration-vi.html) Creates a new instance of a signal by copying all the property values from an existing signal instance.
- [RFmxGSM Delete Signal Configuration VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-delete-signal-configuration-vi.html) Deletes an instance of a signal that you specify in the Signal Name parameter.
- [RFmxGSM Get All Named Result Names VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-get-all-named-result-names-vi.html) Returns all the named result names of the signal that you specify in the Selector String parameter.
- [RFmxGSM Clear Named Result VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-named-result-vi.html) Clears a result instance specified by the result name in the Selector String parameter.
- [RFmxGSM Clear All Named Results VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-all-named-results-vi.html) Clears all results for the signal that you specify in the Selector String parameter.

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-fetch-mnu.html language=enus -->
## TOPIC 00007: Fetch

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-fetch-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/rfmx-gsm-mx-fetch-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to fetch measurement results and traces. icon

### Fetch

Use the VIs on this palette to fetch measurement results and traces.

[IMAGE alt='icon' src='rfmx-gsm-mx-fetch-mnu.png']

- [RFmxGSM ModAcc Fetch VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-vi.html) Fetches the ModAcc measurement results.
- [RFmxGSM ORFS Fetch VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-vi.html) Fetches the output radio frequency spectrum (ORFS) measurement results.
- [RFmxGSM PVT Fetch VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-vi.html) Fetches the power versus time (PVT) measurement results.
- [Build String](../../../../../menus/categories/measurement/rfmx/gsm/utility/rfmx-gsm-mx-utility-build-string-mnu.html) Use the VIs on this palette to create strings for configurations that require a selector string.

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/utility/dir-mnu.html language=enus -->
## TOPIC 00008: Utility

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/utility/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/utility/dir-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure utility measurements. You can use the RFmxGSM Property Node to configure additional properties. icon

### Utility

Use the VIs on this palette to configure utility measurements. You can use the RFmxGSM Property Node to configure additional properties.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxGSM Commit VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-commit-vi.html) Commits settings to the hardware. Calling this VI is optional. RFmxGSM commits settings to the hardware when you call the RFmxGSM Initiate VI.
- [RFmxGSM Reset to Default VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-reset-to-default-vi.html) Resets a signal to the default values.
- [RFmxGSM Wait for Measurement Complete VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-wait-for-measurement-complete-vi.html) Waits for the specified number for seconds for all the measurements to complete.
- [RFmxGSM Check Measurement Status VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-check-measurement-status-vi.html) Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=menus/categories/measurement/rfmx/gsm/utility/rfmx-gsm-mx-utility-build-string-mnu.html language=enus -->
## TOPIC 00009: Build String

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/gsm/utility/rfmx-gsm-mx-utility-build-string-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/gsm/utility/rfmx-gsm-mx-utility-build-string-mnu.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to create strings for configurations that require a selector string. icon

### Build String

Use the VIs on this palette to create strings for configurations that require a selector string.

[IMAGE alt='icon' src='rfmx-gsm-mx-utility-build-string-mnu.png']

- [RFmxGSM Build Signal String VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-build-signal-string-vi.html) Creates selector string for use with configuration or fetch properties and VIs.
- [RFmxGSM Build Offset String VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-build-offset-string-vi.html) Creates an offset string to be used as the selector string with configuration or fetch properties and VIs.
- [RFmxGSM Build Slot String VI](../../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-build-slot-string-vi.html) Creates a slot string to be used as the selector string with configuration or fetch properties and VIs.

Parent topic:

Fetch

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr0.html language=enus -->
## TOPIC 00010: Selector String

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr0.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr0.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node. When there are multiple instances of a property, specify the property instance to configure or fetch by using the Selector String property in a property node. Remarks T

### Selector String

Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node.

When there are multiple instances of a property, specify the property instance to configure or fetch by using the Selector String property in a property node.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Selector String |
| --- | --- |
| Data type |  |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400001.html language=enus -->
## TOPIC 00011: Center Frequency (Hz)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400001.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400001.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for informat

### Center Frequency (Hz)

Specifies the expected carrier frequency of the acquired RF signal. This value is expressed in Hz. The signal analyzer tunes to this frequency.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Center Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Frequency, RFmxGSM Configure RF |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400002.html language=enus -->
## TOPIC 00012: Reference Level

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400002.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Se

### Reference Level

Specifies the reference level that represents the maximum expected power of the RF input signal. This value is expressed in dBm for RF devices and Vpk-pk for baseband devices.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Reference Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Reference Level, RFmxGSM Configure RF |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400003.html language=enus -->
## TOPIC 00013: External Attenuation (dB)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400003.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the NI RF Vector Signal Analyzers Help. You do not nee

### External Attenuation (dB)

Specifies the attenuation of a switch or cable connected to the RF IN connector of the signal analyzer. This value is expressed in dB. For more information about attenuation, refer to the RF Attenuation and Signal Levels topic for your device in the *NI RF Vector Signal Analyzers Help*.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | External Attenuation (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure External Attenuation, RFmxGSM Configure RF |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400004.html language=enus -->
## TOPIC 00014: Trigger:Type

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400004.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger type. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is IQ Power Edge. Remarks The following table lists

### Trigger:Type

Specifies the trigger type.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **IQ Power Edge**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

| None | 0 | No Reference Trigger is configured. |
| --- | --- | --- |
| Digital Edge | 1 | The Reference Trigger is not asserted until a digital edge is detected. The source of the digital edge is specified using the Digital Edge Source property. |
| IQ Power Edge | 2 | The Reference Trigger is asserted when the signal changes past the level specified by the slope (rising or falling), which is configured using the IQ Power Edge Slope property. |
| Software | 3 | The Reference Trigger is not asserted until a software trigger occurs. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400005.html language=enus -->
## TOPIC 00015: Trigger:Digital Edge:Source

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400005.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for informati

### Trigger:Digital Edge:Source

Specifies the source terminal for the digital edge trigger. This property is used only when you set the [Trigger Type](/csh?topicname=attr400004.html) property to **Digital Edge**.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
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

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000a.html language=enus -->
## TOPIC 00016: Trigger:Delay (s)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000a.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the trigger delay time. This value is expressed in seconds. If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples. You do not need to use a selector string to configure or read this property for the de

### Trigger:Delay (s)

Specifies the trigger delay time. This value is expressed in seconds.

If the delay is negative, the measurement acquires pretrigger samples. If the delay is positive, the measurement acquires post-trigger samples.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Delay (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000b.html language=enus -->
## TOPIC 00017: Trigger:Minimum Quiet Time:Mode

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000b.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement computes the minimum quiet time used for triggering. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The defaul

### Trigger:Minimum Quiet Time:Mode

Specifies whether the measurement computes the minimum quiet time used for triggering.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Auto**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Min Quiet Time Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

| Manual | 0 | The minimum quiet time for triggering is the value of the Trigger Min Quiet Time property. |
| --- | --- | --- |
| Auto | 1 | The measurement computes the minimum quiet time used for triggering. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000c.html language=enus -->
## TOPIC 00018: Trigger:Minimum Quiet Time:Duration (s)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000c.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds. If you set the IQ Power Edge Slope property to Rising Slope, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope

### Trigger:Minimum Quiet Time:Duration (s)

Specifies the time duration for which the signal must be quiet before the signal analyzer arms the I/Q power edge trigger. This value is expressed in seconds.

If you set the [IQ Power Edge Slope](attr400009.html) property to **Rising Slope**, the signal is quiet below the trigger level. If you set the IQ Power Edge Slope property to **Falling Slope**, the signal is quiet above the trigger level.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default of this property is hardware dependent.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Min Quiet Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000d.html language=enus -->
## TOPIC 00019: Link Direction

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000d.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the signal to be measured. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is Uplink. Remarks The follo

### Link Direction

Specifies the source of the signal to be measured.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Uplink**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Link Direction |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Link Direction |
| Resettable | Yes |

| Downlink | 0 | The source is a base transceiver station. |
| --- | --- | --- |
| Uplink | 1 | The source is a mobile station. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000e.html language=enus -->
## TOPIC 00020: Band

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40000e.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the operation band. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is PGSM. Remarks The following table lists the ch

### Band

Specifies the operation band.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **PGSM**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Band |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Band |
| Resettable | Yes |

| PGSM | 0 | The operation band is Primary GSM in the 900 MHz band. |
| --- | --- | --- |
| EGSM | 1 | The operation band is Extended GSM in the 900 MHz band. |
| RGSM | 2 | The operation band is Railway GSM in the 900 MHz band. |
| DCS1800 | 3 | The operation band is GSM in the 1800 MHz band. |
| PCS1900 | 4 | The operation band is GSM in the 1900 MHz band. |
| GSM450 | 5 | The operation band is GSM in the 450 MHz band. |
| GSM480 | 6 | The operation band is GSM in the 480 MHz band. |
| GSM850 | 7 | The operation band is GSM in the 850 MHz band. |
| GSM750 | 8 | The operation band is GSM in the 750 MHz band. |
| TGSM810 | 9 | The operation band is terrestrial GSM in the 810 MHz band. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400013.html language=enus -->
## TOPIC 00021: Auto TSC Detection Enabled

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400013.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement automatically detects the training sequence code (TSC). You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The def

### Auto TSC Detection Enabled

Specifies whether the measurement automatically detects the training sequence code (TSC).

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto TSC Detect Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Auto TSC Detection Enabled |
| Resettable | Yes |

| False | 0 | The measurement uses the value that you configure using the TSC property. |
| --- | --- | --- |
| True | 1 | The measurement detects the TSC in the burst. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400014.html language=enus -->
## TOPIC 00022: TSC

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400014.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the training sequence code (TSC) to use. This property is applicable only when you set the Burst Sync Type property to TSC and the Auto TSC Detect Enabled property to False. For access burst TSC0, TSC1, and TSC2 are applicable. Use "slot<n>" as the selector string to configure or read this

### TSC

Specifies the training sequence code (TSC) to use. This property is applicable only when you set the [Burst Sync Type](/csh?topicname=attr400016.html) property to **TSC** and the [Auto TSC Detect Enabled](/csh?topicname=attr400013.html) property to **False**. For access burst **TSC0**, **TSC1**, and **TSC2** are applicable.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is **TSC0**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | TSC |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure TSC |
| Resettable | Yes |

| TSC0 | 0 | The measurement uses training sequence code 0. |
| --- | --- | --- |
| TSC1 | 1 | The measurement uses training sequence code 1. |
| TSC2 | 2 | The measurement uses training sequence code 2. |
| TSC3 | 3 | The measurement uses training sequence code 3. |
| TSC4 | 4 | The measurement uses training sequence code 4. |
| TSC5 | 5 | The measurement uses training sequence code 5. |
| TSC6 | 6 | The measurement uses training sequence code 6. |
| TSC7 | 7 | The measurement uses training sequence code 7. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400015.html language=enus -->
## TOPIC 00023: Power Control Level

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400015.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. Use "slot<n>" as the selector string to configure or read this property. The default value is 0. Valid values are 0 to 31, inclusive. Remarks The following

### Power Control Level

Specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the *3GPP TS 45.005 v8.0.0 specifications*.

Use "slot<*n*>" as the selector string to configure or read this property.

The default value is 0. Valid values are 0 to 31, inclusive.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pwr Control Level |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Power Control Level |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400016.html language=enus -->
## TOPIC 00024: Burst Synchronization Type

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400016.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400016.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the method used to synchronize the burst. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is TSC. Remarks The followi

### Burst Synchronization Type

Specifies the method used to synchronize the burst.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **TSC**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Burst Sync Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Burst Synchronization Type |
| Resettable | Yes |

| TSC | 0 | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| --- | --- | --- |
| Amplitude | 1 | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF envelope. |
| None | 2 | Sets the T0 point to 273.23 microseconds after the trigger. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400017.html language=enus -->
## TOPIC 00025: Signal Structure

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400017.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400017.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the Trigger Type to IQ Power Edge and None, respectively. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String to

### Signal Structure

Specifies whether the signal is bursted or continuous. For bursted signal and continuous signals, set the [Trigger Type](/csh?topicname=attr400004.html) to **IQ Power Edge** and **None**, respectively.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Bursted**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Signal Structure |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Bursted | 0 | The signal is bursted. |
| --- | --- | --- |
| Continuous | 1 | The signal is continuous. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400fff.html language=enus -->
## TOPIC 00026: Trigger:IQ Power Edge:Level Type

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400fff.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr400fff.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the reference for the IQ Power Edge Level property. The IQ Power Edge Level Type property is used only when you set the Trigger Type property to IQ Power Edge. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector

### Trigger:IQ Power Edge:Level Type

Specifies the reference for the [IQ Power Edge Level](/csh?topicname=attr400008.html) property. The IQ Power Edge Level Type property is used only when you set the [Trigger Type](/csh?topicname=attr400004.html) property to **IQ Power Edge**.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Relative**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Power Edge Level Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM Configure Trigger |
| Resettable | Yes |

| Relative | 0 | The value of the IQ Power Edge Level property is relative to the value of the Reference Level property. |
| --- | --- | --- |
| Absolute | 1 | The IQ Power Edge Level property specifies the absolute power. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401006.html language=enus -->
## TOPIC 00027: ModAcc:All Traces Enabled

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401006.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the s

### ModAcc:All Traces Enabled

Specifies whether to enable the traces to be stored and retrieved after performing the modulation accuracy (ModAcc) measurement.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is FALSE.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc All Traces Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401007.html language=enus -->
## TOPIC 00028: ModAcc:Number of Analysis Threads

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401007.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum number of threads used for parallelism for the ModAcc measurement. The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resour

### ModAcc:Number of Analysis Threads

Specifies the maximum number of threads used for parallelism for the ModAcc measurement.

The number of threads can range from 1 to the number of physical cores. The number of threads you set may not be used in calculations. The actual number of threads used depends on the problem size, system resources, data availability, and other considerations.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Num Analysis Threads |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401008.html language=enus -->
## TOPIC 00029: ModAcc:Results:EVM:Mean RMS (%)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401008.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401008.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to configure or read this property for the default signal and result instances. Refe

### ModAcc:Results:EVM:Mean RMS (%)

Returns the mean of RMS values of EVM over all the measured time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Mean RMS EVM (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100d.html language=enus -->
## TOPIC 00030: ModAcc:Results:EVM:Peak EVM Symbol

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100d.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the symbol number in the useful portion of the burst corresponding to ModAcc Results EVM Max Pk EVM result. The property returns this result for ModAcc EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to

### ModAcc:Results:EVM:Peak EVM Symbol

Returns the symbol number in the useful portion of the burst corresponding to [ModAcc Results EVM Max Pk EVM](/csh?topicname=attr40100b.html) result. The property returns this result for ModAcc EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Pk EVM Symbol |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100e.html language=enus -->
## TOPIC 00031: ModAcc:Results:EVM:Magnitude Error:Mean (%)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100e.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer t

### ModAcc:Results:EVM:Magnitude Error:Mean (%)

Returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Mean Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100f.html language=enus -->
## TOPIC 00032: ModAcc:Results:EVM:Magnitude Error:Maximum (%)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40100f.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refe

### ModAcc:Results:EVM:Magnitude Error:Maximum (%)

Returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Max Magnitude Error (%) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401012.html language=enus -->
## TOPIC 00033: ModAcc:Results:EVM:Frequency Error:Mean (Hz)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401012.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Selecto

### ModAcc:Results:EVM:Frequency Error:Mean (Hz)

Returns the mean of the frequency error values over all the measured time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Mean Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401013.html language=enus -->
## TOPIC 00034: ModAcc:Results:EVM:Frequency Error:Maximum (Hz)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401013.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the Sele

### ModAcc:Results:EVM:Frequency Error:Maximum (Hz)

Returns the maximum of the frequency error values over all the measured time slots. This value is expressed in Hz. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Max Freq Error (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401014.html language=enus -->
## TOPIC 00035: ModAcc:Results:EVM:Amplitude Droop:Mean (dB/symbol)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401014.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to the

### ModAcc:Results:EVM:Amplitude Droop:Mean (dB/symbol)

Returns the mean of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Mean Ampl Droop |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401015.html language=enus -->
## TOPIC 00036: ModAcc:Results:EVM:Amplitude Droop:Maximum (dB/symbol)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401015.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements. You do not need to use a selector string to read this result for the default signal and result instances. Refer to t

### ModAcc:Results:EVM:Amplitude Droop:Maximum (dB/symbol)

Returns the maximum of the amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. The property returns this result for EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results EVM Max Ampl Droop |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40101e.html language=enus -->
## TOPIC 00037: ModAcc:Results:IQ Gain Imbalance:Maximum (dB)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40101e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40101e.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance. You do not need to use a selector string to read this result for the default signal and resul

### ModAcc:Results:IQ Gain Imbalance:Maximum (dB)

Returns the maximum of I/Q gain imbalance values over all the measured time slots. This value is expressed in dB. The presence of quadrature skew in the signal affects the measurement of I/Q gain imbalance.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Max IQ Gain Imbalance (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40101f.html language=enus -->
## TOPIC 00038: ModAcc:Results:IQ Origin Offset:Mean (dB)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40101f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40101f.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements. You do not n

### ModAcc:Results:IQ Origin Offset:Mean (dB)

Returns the mean of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Mean IQ Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401020.html language=enus -->
## TOPIC 00039: ModAcc:Results:IQ Origin Offset:Maximum (dB)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr401020.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements. You do no

### ModAcc:Results:IQ Origin Offset:Maximum (dB)

Returns the maximum of the I/Q origin offset values over all the measured time slots. This value is expressed in dB. Presence of I/Q gain imbalance and quadrature skew in the signal affects the I/Q origin offset measurement. The property returns this result for GSM/EDGE/EGPRS measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this result for the default signal and result instances. Refer to the Selector String topic for information about the string syntax for named signals and named results.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Results Max IQ Origin Offset (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | RFmxGSM ModAcc Fetch |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40102a.html language=enus -->
## TOPIC 00040: ModAcc:Measurement Interval

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40102a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40102a.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for name

### ModAcc:Measurement Interval

Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default Value is **'Number of Timeslots'**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Meas Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Number of Timeslots | 0 | The measurement includes all timeslots defined by the Num Timeslots property. |
| --- | --- | --- |
| Timeslot at Offset | 1 | The measurement is performed only on the timeslot specified by the ModAcc Meas Offset property. This property is applicable only when you set the Trigger Type property to IQ Power Edge or Digital Edge . |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40102b.html language=enus -->
## TOPIC 00041: ModAcc:Measurement Offset

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40102b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40102b.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset, relative to the trigger of the timeslot to be measured. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value i

### ModAcc:Measurement Offset

Specifies the offset, relative to the trigger of the timeslot to be measured.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, ([Num Timeslots](attr40000f.html) -1)].

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ModAcc Meas Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402002.html language=enus -->
## TOPIC 00042: ORFS:Averaging:Enabled

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402002.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

### ORFS:Averaging:Enabled

Specifies whether to enable averaging for the output radio frequency spectrum (ORFS) measurement.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Averaging Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Averaging |
| Resettable | Yes |

| False | 0 | The measurement is performed on a single acquisition. |
| --- | --- | --- |
| True | 1 | The measurement is averaged over multiple acquisitions. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402003.html language=enus -->
## TOPIC 00043: ORFS:Averaging:Type

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402003.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Stri

### ORFS:Averaging:Type

Specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the output radio frequency spectrum (ORFS) measurement.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Log**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Averaging Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Averaging |
| Resettable | Yes |

| RMS | 0 | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| --- | --- | --- |
| Log | 1 | The measurement averages the power spectrum in a logarithmic scale. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402004.html language=enus -->
## TOPIC 00044: ORFS:Averaging:Count

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402004.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of acquisitions used for averaging when you set the ORFS Averaging Enabled property to True. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax fo

### ORFS:Averaging:Count

Specifies the number of acquisitions used for averaging when you set the [ORFS Averaging Enabled](/csh?topicname=attr402002.html) property to **True**.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 10.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Averaging Count |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Averaging |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402005.html language=enus -->
## TOPIC 00045: ORFS:Measurement Type

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402005.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the type of spectral distortion to be measured. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is Modulation and Swi

### ORFS:Measurement Type

Specifies the type of spectral distortion to be measured.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Modulation and Switching**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Meas Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Measurement Type |
| Resettable | Yes |

| Modulation and Switching | 0 | Measures the spectrum on the modulated part and the switching part of the waveform. |
| --- | --- | --- |
| Modulation | 1 | Measures the spectrum on the modulated part of the waveform. |
| Switching | 2 | Measures the spectrum on the switching part of the waveform. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402006.html language=enus -->
## TOPIC 00046: ORFS:Noise Compensation Enabled

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402006.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets. You do not need to use a selector string to configure or read this property for the default si

### ORFS:Noise Compensation Enabled

Specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. Noise compensation is applicable only on modulation offsets and not on switching offsets.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

**Supported Devices**: PXIe-5663/5665/5668R, PXIe-5830/5831/5832

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Noise Comp Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Noise Compensation Enabled |
| Resettable | Yes |

| False | 0 | Disables compensation of the channel powers for the signal analyzer noise floor. |
| --- | --- | --- |
| True | 1 | Enables compensation of the channel powers for the noise floor of the signal analyzer. The noise floor of the signal analyzer is measured for the RF path used by the output radio frequency spectrum (ORFS) measurement and cached for future use. If signal analyzer or measurement parameters change, noise floors are measured again. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402007.html language=enus -->
## TOPIC 00047: ORFS:Offset Frequency Mode

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402007.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string

### ORFS:Offset Frequency Mode

Specifies the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **Standard**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Offset Freq Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Offset Frequency Mode |
| Resettable | Yes |

| Standard | 0 | Uses the list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| --- | --- | --- |
| Short | 1 | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Custom | 2 | Uses the list of frequencies that is configured using the RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) and RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VIs for measurement of spectrum produced by modulation and switching measurements. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40200b.html language=enus -->
## TOPIC 00048: ORFS:Modulation:Carrier RBW (Hz)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40200b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr40200b.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RBW used for measuring modulation carrier power in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is 30kHz.

### ORFS:Modulation:Carrier RBW (Hz)

Specifies the RBW used for measuring modulation carrier power in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 30kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Mod Carrier RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402012.html language=enus -->
## TOPIC 00049: ORFS:Evaluation Symbols:Include TSC

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402012.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402012.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax

### ORFS:Evaluation Symbols:Include TSC

Specifies whether to include the training sequence code (TSC) portion of burst for measuring ORFS due to modulation.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Evaluation Symbols Include TSC |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Evaluation Symbols |
| Resettable | Yes |

| False | 0 | The TSC portion of the burst will be excluded while performing the ORFS measurement. |
| --- | --- | --- |
| True | 1 | The TSC portion of the burst will be included while performing the ORFS measurement. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402013.html language=enus -->
## TOPIC 00050: ORFS:Evaluation Symbols:Stop (%)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402013.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402013.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string synta

### ORFS:Evaluation Symbols:Stop (%)

Specifies the stop position within the useful part of the burst, in percentage, for measuring ORFS due to modulation.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 90.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Evaluation Symbols Stop (%) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxGSM ORFS Configure Evaluation Symbols |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402022.html language=enus -->
## TOPIC 00051: ORFS:Switching:Offset RBW (Hz)

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402022.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402022.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz. Use "offset<n>" as the selector string to configure or read this property. The default value is 30kHz. Remarks The following table lists the characteristics of this property. Short Name ORFS

### ORFS:Switching:Offset RBW (Hz)

Specifies the resolution bandwidth used for ORFS due to switching measurement. This value is expressed in Hz.

Use "offset<*n*>" as the selector string to configure or read this property.

The default value is 30kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Switching Offset RBW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402024.html language=enus -->
## TOPIC 00052: ORFS:Evaluation Symbols:Scope

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402024.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402024.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the modulation power measurements that will use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for informat

### ORFS:Evaluation Symbols:Scope

Specifies the modulation power measurements that will use the part of burst configured using the [RFmxGSM ORFS Configure Evaluation Symbols VI](/csh?context=rfmxgsm_rfmxgsmvi_rfmxgsm_orfs_configure_evaluation_symbols).

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Offset**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Evaluation Symbols Scope |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Offset | 0 | Modulation Offset Power measurements will only use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI. Modulation Carrier Power measurement will use all of the useful part of the burst. |
| --- | --- | --- |
| Offset and Carrier | 1 | Modulation Offset and Carrier Power measurements will both use the part of burst configured using the RFmxGSM ORFS Configure Evaluation Symbols VI. |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402025.html language=enus -->
## TOPIC 00053: ORFS:Measurement Interval

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402025.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402025.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for name

### ORFS:Measurement Interval

Specifies whether the measurement is performed on a single specified timeslot or across multiple timeslots.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default Value is **'Number of Timeslots'**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Meas Interval |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Number of Timeslots | 0 | The measurement includes all timeslots defined by the Num Timeslots property. |
| --- | --- | --- |
| Timeslot at Offset | 1 | The measurement is performed only on the timeslot specified by the ORFS Meas Offset property. This property is applicable only when you set the Trigger Type property to IQ Power Edge or Digital Edge . |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402026.html language=enus -->
## TOPIC 00054: ORFS:Measurement Offset

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402026.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr402026.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset, relative to the trigger, of the timeslot to be measured. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value

### ORFS:Measurement Offset

Specifies the offset, relative to the trigger, of the timeslot to be measured.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

The default value is 0. Valid values are [0, ([Num Timeslots](attr40000f.html) -1)].

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | ORFS Meas Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=resource/objmgr/rfmxgsm-rc/rfmxgsm/attr403000.html language=enus -->
## TOPIC 00055: PVT:Measurement Enabled

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `resource/objmgr/rfmxgsm-rc/rfmxgsm/attr403000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxgsm-rc/rfmxgsm/attr403000.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the power versus time (PVT) measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals. The default value is FALSE.

### PVT:Measurement Enabled

Specifies whether to enable the power versus time (PVT) measurement.

You do not need to use a [selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to configure or read this property for the default signal instance. Refer to the Selector String topic for information about the string syntax for named signals.

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

RFmxGSM Properties

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-abort-measurements-vi.html language=enus -->
## TOPIC 00056: RFmxGSM Abort Measurements VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-abort-measurements-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with the signal instance that you specify in the Selector String parameter. This acquisition and measurements were previously initiated by the RFmxGSM Initiate VI. Calling this VI is optional, unless you want to stop a measurement before it is complete.

### RFmxGSM Abort Measurements VI

Stops acquisition and measurements associated with the signal instance that you specify in the **Selector String** parameter. This acquisition and measurements were previously initiated by the [RFmxGSM Initiate](/csh?topicname=rfmxgsm-initiate-vi.html) VI. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxgsm-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-analyze-iq-1-wfm-vi.html language=enus -->
## TOPIC 00057: RFmxGSM Analyze (IQ, 1 Wfm) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-analyze-iq-1-wfm-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-analyze-iq-1-wfm-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the enabled measurements on the I/Q complex waveform that you specify in IQ parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node. Use this VI only if the Recommended

### RFmxGSM Analyze (IQ, 1 Wfm) VI

Performs the enabled measurements on the I/Q complex waveform that you specify in **IQ** parameter. Call this VI after you configure the signal and measurement properties. You can fetch measurement results using the Fetch VIs or result properties in the property node.
Use this VI only if the [Recommended Acquisition Type](/csh?context=rfmxinstr_rfmxinstrprop_attr27) property value is **IQ**.

Note

RFmxInstr Property Node

RFmx GSM Commit

[IMAGE alt='icon' src='rfmxgsm-analyze-iq-1-wfm-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI with option string as "AnalysisOnly=1". IQ — IQ specifies the data for a complex waveform including the start, delta, and actual values. x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. Reset? — Reset? resets measurement averaging. If you enable averaging, set this parameter to TRUE for first record and FALSE for subsequent records. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to Selector String parameter on Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 specifies the start time of the input Y array. This value is expressed in seconds. dx — dx specifies the time interval between the samples in the input Y array. This value is expressed in seconds. The reciprocal of dx indicates the I/Q rate of the input signal. y — y specifies an array of complex-valued time domain data. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-check-measurement-status-vi.html language=enus -->
## TOPIC 00058: RFmxGSM Check Measurement Status VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-check-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-check-measurement-status-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal nam

### RFmxGSM Check Measurement Status VI

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='icon' src='rfmxgsm-check-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. done? — done? indicates whether the measurement is complete. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-all-named-results-vi.html language=enus -->
## TOPIC 00059: RFmxGSM Clear All Named Results VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-all-named-results-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-all-named-results-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears all results for the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (

### RFmxGSM Clear All Named Results VI

Clears all results for the signal that you specify in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxgsm-clear-all-named-results-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-named-result-vi.html language=enus -->
## TOPIC 00060: RFmxGSM Clear Named Result VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-named-result-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-clear-named-result-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears a result instance specified by the result name in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used.

### RFmxGSM Clear Named Result VI

Clears a result instance specified by the result name in the **Selector String** parameter.

[IMAGE alt='icon' src='rfmxgsm-clear-named-result-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-burst-synchronization-type-vi.html language=enus -->
## TOPIC 00061: RFmxGSM Configure Burst Synchronization Type VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-burst-synchronization-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-burst-synchronization-type-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the burst synchronization type. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You

### RFmxGSM Configure Burst Synchronization Type VI

Configures the burst synchronization type.

[IMAGE alt='icon' src='rfmxgsm-configure-burst-synchronization-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Burst Sync Type — Burst Sync Type specifies the method used to synchronize the burst. The default value is TSC. TSC (0) Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. Amplitude (1) Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF Envelope. None (2) Sets the T0 point to 273.23 µsec after the trigger. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| TSC (0) | Synchronizes the measurement to the timing of the demodulated training sequence in the burst. The measurement requires a burst with a valid training sequence code (TSC). The measurement determines the T0 point by demodulating the burst and identifying the TSC. |
| Amplitude (1) | Synchronizes the measurement based on the RF envelope of the received signal. The measurement sets the T0 point as the center of the RF Envelope. |
| None (2) | Sets the T0 point to 273.23 µsec after the trigger. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-digital-edge-trigger-vi.html language=enus -->
## TOPIC 00062: RFmxGSM Configure Digital Edge Trigger VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-digital-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-digital-edge-trigger-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to wait for a digital edge trigger and then marks a reference point within the record. icon Inputs/Outputs cbool.png Enable Trigger? Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. cstr.png Selector String Selector String specifies a selector

### RFmxGSM Configure Digital Edge Trigger VI

Configures the device to wait for a digital edge trigger and then marks a reference point within the record.

[IMAGE alt='icon' src='rfmxgsm-configure-digital-edge-trigger-vi.png']

#### Inputs/Outputs

| Enable Trigger? — Enable Trigger? specifies whether to enable the trigger. The default value is TRUE. Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Digital Edge Source — Digital Edge Source specifies the source terminal for the digital-edge trigger. The default of this property is hardware dependent. PFI0 (PFI0) The trigger is received on PFI 0. PFI1 (PFI1) The trigger is received on PFI 1. PXI_Trig0 (PXI_Trig0) The trigger is received on PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The trigger is received on PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The trigger is received on PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The trigger is received on PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The trigger is received on PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The trigger is received on PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The trigger is received on PXI trigger line 6. PXI_Trig7 (PXI_Trig7) The trigger is received on PXI trigger line 7. PXI_STAR (PXI_STAR) The trigger is received on the PXI star trigger line. Digital Edge — Digital Edge specifies the active edge for the trigger. This parameter is used only when you set the Trigger Type property to Digital Edge. The default value is Rising Edge. Rising Edge (0) The trigger asserts on the rising edge of the signal. Falling Edge (1) The trigger asserts on the falling edge of the signal. Trigger Delay (s) — Trigger Delay specifies the trigger delay time, in seconds. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
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

RFmxGSM Configure Trigger VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-arfcn-vi.html language=enus -->
## TOPIC 00063: RFmxGSM Configure Frequency (ARFCN) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-arfcn-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-arfcn-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxGSM Configure Frequency (ARFCN) VI

Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction.

[IMAGE alt='icon' src='rfmxgsm-configure-frequency-arfcn-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Link Direction — Link Direction specifies the source of the signal to be measured. The default value is Uplink. Downlink (0) The source is a base transceiver station. Uplink (1) The source is a mobile station. Band — Band specifies the band of operation. The default value is PGSM. PGSM (0) The operation band is Primary GSM in the 900 MHz band. EGSM (1) The operation band is Extended GSM in the 900 MHz band. RGSM (2) The operation band is Railway GSM in the 900 MHz band. DCS1800 (3) The operation band is GSM in the 1800 MHz band. PCS1900 (4) The operation band is GSM in the 1900 MHz band. GSM450 (5) The operation band is GSM in the 450 MHz band. GSM480 (6) The operation band is GSM in the 480 MHz band. GSM850 (7) The operation band is GSM in the 850 MHz band. GSM750 (8) The operation band is GSM in the 750 MHz band. T-GSM810 (9) The operation band is terrestrial GSM in the 810 MHz band. ARFCN — ARFCN specifies the ARFCN. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Downlink (0) | The source is a base transceiver station. |
| Uplink (1) | The source is a mobile station. |
| PGSM (0) | The operation band is Primary GSM in the 900 MHz band. |
| EGSM (1) | The operation band is Extended GSM in the 900 MHz band. |
| RGSM (2) | The operation band is Railway GSM in the 900 MHz band. |
| DCS1800 (3) | The operation band is GSM in the 1800 MHz band. |
| PCS1900 (4) | The operation band is GSM in the 1900 MHz band. |
| GSM450 (5) | The operation band is GSM in the 450 MHz band. |
| GSM480 (6) | The operation band is GSM in the 480 MHz band. |
| GSM850 (7) | The operation band is GSM in the 850 MHz band. |
| GSM750 (8) | The operation band is GSM in the 750 MHz band. |
| T-GSM810 (9) | The operation band is terrestrial GSM in the 810 MHz band. |

Parent topic:

RFmxGSM Configure Frequency VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-frequency-vi.html language=enus -->
## TOPIC 00064: RFmxGSM Configure Frequency (Frequency) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-frequency-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the center frequency of the RF signal to acquire. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example:

### RFmxGSM Configure Frequency (Frequency) VI

Configures the center frequency of the RF signal to acquire.

[IMAGE alt='icon' src='rfmxgsm-configure-frequency-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Center Frequency (Hz) — Center Frequency specifies the expected center frequency of the RF signal to acquire. This value is expressed in Hz. The signal analyzer tunes to this frequency. The default of this property is hardware dependent. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM Configure Frequency VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-vi.html language=enus -->
## TOPIC 00065: RFmxGSM Configure Frequency VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the expected center frequency of the RF signal to acquire. The signal analyzer tunes to this frequency. icon

### RFmxGSM Configure Frequency VI

Configures the expected center frequency of the RF signal to acquire. The signal analyzer tunes to this frequency.

[IMAGE alt='icon' src='rfmxgsm-configure-frequency-vi.png']

- [RFmxGSM Configure Frequency (Frequency) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-frequency-vi.html) Configures the center frequency of the RF signal to acquire.
- [RFmxGSM Configure Frequency (ARFCN) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-frequency-arfcn-vi.html) Configures the center frequency from the absolute RF channel number (ARFCN), band, and the link direction.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-link-direction-vi.html language=enus -->
## TOPIC 00066: RFmxGSM Configure Link Direction VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-link-direction-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-link-direction-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the source of the signal to be measured. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::

### RFmxGSM Configure Link Direction VI

Configures the source of the signal to be measured.

[IMAGE alt='icon' src='rfmxgsm-configure-link-direction-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Link Direction — Link Direction specifies the source of the signal to be measured. The default value is Uplink. Downlink (0) The source is a base transceiver station. Uplink (1) The source is a mobile station. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Downlink (0) | The source is a base transceiver station. |
| Uplink (1) | The source is a mobile station. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-number-of-timeslots-vi.html language=enus -->
## TOPIC 00067: RFmxGSM Configure Number of Timeslots VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-number-of-timeslots-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-number-of-timeslots-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the number of time slots to be measured. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::

### RFmxGSM Configure Number of Timeslots VI

Configures the number of time slots to be measured.

[IMAGE alt='icon' src='rfmxgsm-configure-number-of-timeslots-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Number of Timeslots — Number of Timeslots specifies the number of time slots to be measured. The default value is 1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-power-control-level-vi.html language=enus -->
## TOPIC 00068: RFmxGSM Configure Power Control Level VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-power-control-level-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-power-control-level-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the power control level corresponding to the transmitted power. Use "slot<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the sign

### RFmxGSM Configure Power Control Level VI

Configures the power control level corresponding to the transmitted power.

Use "slot<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxgsm-configure-power-control-level-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all". Example: "slot0" "slot::all" "signal::sig1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Power Control Level — Power Control Level specifies the power control level corresponding to the transmitted power, as defined in section 4.1 of the 3GPP TS 45.005 v8.0.0 specifications. The default value is 0. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-signal-type-vi.html language=enus -->
## TOPIC 00069: RFmxGSM Configure Signal Type VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-signal-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-configure-signal-type-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the signal type. Use "slot<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. T

### RFmxGSM Configure Signal Type VI

Configures the signal type.

Use "slot<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxgsm-configure-signal-type-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and slot number. If you do not specify the signal name, the default signal instance is used. The default value is "slot::all". Example: "slot0" "slot::all" "signal::sig1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Modulation Type — Modulation Type specifies the modulation type of the signal. The default value is 8PSK. GMSK (0) The modulation type is Gaussian MSK. This value is valid only when you set the Burst Type parameter to NB or AB. 8PSK (1) The modulation type is 8-PSK. This value is valid only when you set theBurst Type parameter to NB. QPSK (2) The modulation type is QPSK. This value is valid only when you set the Burst Type parameter to HB. 16QAM (3) The modulation type is 16-QAM. 32QAM (4) The modulation type is 32-QAM. Burst Type — Burst Type specifies the burst type. The default value is NB. NB (0) The burst type is Normal Burst. HB (1) The burst type is Higher Symbol Rate Burst. AB (2) The burst type is Access Burst. HB Filter Width — HB Filter Width specifies the filter width when you set the Burst Type parameter to HB. The default value is Narrow. Narrow (0) The measurement uses a narrow filter. Wide (1) The measurement uses a wide filter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| GMSK (0) | The modulation type is Gaussian MSK. This value is valid only when you set the Burst Type parameter to NB or AB. |
| 8PSK (1) | The modulation type is 8-PSK. This value is valid only when you set theBurst Type parameter to NB. |
| QPSK (2) | The modulation type is QPSK. This value is valid only when you set the Burst Type parameter to HB. |
| 16QAM (3) | The modulation type is 16-QAM. |
| 32QAM (4) | The modulation type is 32-QAM. |
| NB (0) | The burst type is Normal Burst. |
| HB (1) | The burst type is Higher Symbol Rate Burst. |
| AB (2) | The burst type is Access Burst. |
| Narrow (0) | The measurement uses a narrow filter. |
| Wide (1) | The measurement uses a wide filter. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-create-signal-configuration-vi.html language=enus -->
## TOPIC 00070: RFmxGSM Create Signal Configuration VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-create-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-create-signal-configuration-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a new instance of a signal. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" cgenclassrntag.png Instrument Handle In Instrument Handle In specifi

### RFmxGSM Create Signal Configuration VI

Creates a new instance of a signal.

[IMAGE alt='icon' src='rfmxgsm-create-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to the Selector String parameter of configure, initiate, and fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-delete-signal-configuration-vi.html language=enus -->
## TOPIC 00071: RFmxGSM Delete Signal Configuration VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-delete-signal-configuration-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-delete-signal-configuration-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes an instance of a signal that you specify in the Signal Name parameter. icon Inputs/Outputs cstr.png Signal Name Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" cgenclassrntag.png Instru

### RFmxGSM Delete Signal Configuration VI

Deletes an instance of a signal that you specify in the **Signal Name** parameter.

[IMAGE alt='icon' src='rfmxgsm-delete-signal-configuration-vi.png']

#### Inputs/Outputs

| Signal Name — Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-disable-trigger-vi.html language=enus -->
## TOPIC 00072: RFmxGSM Disable Trigger VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-disable-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-disable-trigger-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name

### RFmxGSM Disable Trigger VI

Configures the device to not wait for a trigger to mark a reference point within a record. This VI defines the signal triggering as immediate.

[IMAGE alt='icon' src='rfmxgsm-disable-trigger-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM Configure Trigger VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-get-all-named-result-names-vi.html language=enus -->
## TOPIC 00073: RFmxGSM Get All Named Result Names VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-get-all-named-result-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-get-all-named-result-names-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all the named result names of the signal that you specify in the Selector String parameter. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The

### RFmxGSM Get All Named Result Names VI

Returns all the named result names of the signal that you specify in the Selector String parameter.

[IMAGE alt='icon' src='rfmxgsm-get-all-named-result-names-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Result Names — Result Names returns an array of result names. Default Result Exists? — Default Result Exists? indicates whether the default result exists. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-initiate-vi.html language=enus -->
## TOPIC 00074: RFmxGSM Initiate VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-initiate-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node

### RFmxGSM Initiate VI

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxGSM Wait for Measurement Complete](/csh?topicname=rfmxgsm-wait-for-measurement-complete-vi.html) VI or [RFmxGSM Check Measurement Status](/csh?topicname=rfmxgsm-check-measurement-status-vi.html) VI.

[IMAGE alt='icon' src='rfmxgsm-initiate-vi.png']

#### Inputs/Outputs

| Result Name — Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" Selector String — Selector String specifies a selector string comprising of the signal name and result name. The result name can either be specified through this input or the Result Name parameter. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name in this parameter, either the result name specified by the Result Name parameter or the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Selector String Out — Selector String Out returns the selector string that can be passed to Selector String parameter on Fetch VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-configure-averaging-vi.html language=enus -->
## TOPIC 00075: RFmxGSM ModAcc Configure Averaging VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-configure-averaging-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the modulation accuracy (ModAcc) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string).

### RFmxGSM ModAcc Configure Averaging VI

Configures averaging for the modulation accuracy (ModAcc) measurement.

[IMAGE alt='icon' src='rfmxgsm-modacc-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. |

Parent topic:

ModAcc

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-demodulated-bits-vi.html language=enus -->
## TOPIC 00076: RFmxGSM ModAcc Fetch Demodulated Bits VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-demodulated-bits-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-demodulated-bits-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default sig

### RFmxGSM ModAcc Fetch Demodulated Bits VI

Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-demodulated-bits-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Bits — Bits returns an array of demodulated bits concatenated over all the measured time slots for the last acquisition. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-array-vi.html language=enus -->
## TOPIC 00077: RFmxGSM ModAcc Fetch Detected TSC (Array) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-array-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS. When the ModAcc Meas Interval property is set to Timeslot at Offset, Detected TSC array has one element and the Detected TSC is returned at index 0. icon Inputs/Outputs cstr.png Selector String Selector Str

### RFmxGSM ModAcc Fetch Detected TSC (Array) VI

Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS.

When the [ModAcc Meas Interval](/csh?context=rfmxgsm_rfmxgsmprop_attr40102a) property is set to **Timeslot at Offset**, Detected TSC array has one element and the Detected TSC is returned at index 0.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-detected-tsc-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Detected TSC — Detected TSC returns an array of the detected TSCs when you set the Burst Sync Type property to TSC. Unknown (-1) The synchronization is not found and measurements correspond to best estimate of synchronization. TSC0 (0) The detected TSC is TSC0. TSC1 (1) The detected TSC is TSC1. TSC2 (2) The detected TSC is TSC2. TSC3 (3) The detected TSC is TSC3. TSC4 (4) The detected TSC is TSC4. TSC5 (5) The detected TSC is TSC5. TSC6 (6) The detected TSC is TSC6. TSC7 (7) The detected TSC is TSC7. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Unknown (-1) | The synchronization is not found and measurements correspond to best estimate of synchronization. |
| TSC0 (0) | The detected TSC is TSC0. |
| TSC1 (1) | The detected TSC is TSC1. |
| TSC2 (2) | The detected TSC is TSC2. |
| TSC3 (3) | The detected TSC is TSC3. |
| TSC4 (4) | The detected TSC is TSC4. |
| TSC5 (5) | The detected TSC is TSC5. |
| TSC6 (6) | The detected TSC is TSC6. |
| TSC7 (7) | The detected TSC is TSC7. |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-vi.html language=enus -->
## TOPIC 00078: RFmxGSM ModAcc Fetch Detected TSC VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS. Use "slot<n>" as the selector string to read results from this VI. When the ModAcc Meas Interval property is set to Timeslot at Offset, Detected TSC array has one element and the Detected TSC is returned at index

### RFmxGSM ModAcc Fetch Detected TSC VI

Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS.

Use "slot<*n*>" as the selector string to read results from this VI.

When the [ModAcc Meas Interval](/csh?context=rfmxgsm_rfmxgsmprop_attr40102a) property is set to **Timeslot at Offset**, Detected TSC array has one element and the Detected TSC is returned at index 0.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-detected-tsc-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "slot0" "signal::sig1/slot0" "result::r1/slot0" "signal::sig1/result::r1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Detected TSC — Detected TSC returns the detected TSC when you set the Burst Sync Type property to TSC. Unknown (-1) Burst synchronization is not found and measurements correspond to best estimate of synchronization. TSC0 (0) The detected TSC is TSC0. TSC1 (1) The detected TSC is TSC1. TSC2 (2) The detected TSC is TSC2. TSC3 (3) The detected TSC is TSC3. TSC4 (4) The detected TSC is TSC4. TSC5 (5) The detected TSC is TSC5. TSC6 (6) The detected TSC is TSC6. TSC7 (7) The detected TSC is TSC7. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Unknown (-1) | Burst synchronization is not found and measurements correspond to best estimate of synchronization. |
| TSC0 (0) | The detected TSC is TSC0. |
| TSC1 (1) | The detected TSC is TSC1. |
| TSC2 (2) | The detected TSC is TSC2. |
| TSC3 (3) | The detected TSC is TSC3. |
| TSC4 (4) | The detected TSC is TSC4. |
| TSC5 (5) | The detected TSC is TSC5. |
| TSC6 (6) | The detected TSC is TSC6. |
| TSC7 (7) | The detected TSC is TSC7. |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-amplitude-droop-vi.html language=enus -->
## TOPIC 00079: RFmxGSM ModAcc Fetch EVM Amplitude Droop VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-amplitude-droop-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-amplitude-droop-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the amplitude droop measurement results for EDGE/EGPRS. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify th

### RFmxGSM ModAcc Fetch EVM Amplitude Droop VI

Fetches the amplitude droop measurement results for EDGE/EGPRS.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-evm-amplitude-droop-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Amplitude Droop (dB/symbol) — Mean Amplitude Droop returns the mean of amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. Maximum Amplitude Droop (dB/symbol) — Maximum Amplitude Droop returns the maximum of amplitude droop values over all the measured time slots. This value is expressed in dB/symbol. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-magnitude-error-vi.html language=enus -->
## TOPIC 00080: RFmxGSM ModAcc Fetch EVM Magnitude Error VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-magnitude-error-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-magnitude-error-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the magnitude error measurement results for EDGE/EGPRS. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify th

### RFmxGSM ModAcc Fetch EVM Magnitude Error VI

Fetches the magnitude error measurement results for EDGE/EGPRS.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-evm-magnitude-error-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Mean Magnitude Error (%) — Mean Magnitude Error returns the mean of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. Maximum Magnitude Error (%) — Maximum Magnitude Error returns the maximum of RMS values of magnitude error over all the measured time slots. This value is expressed as a percentage. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-magnitude-error-trace-vi.html language=enus -->
## TOPIC 00081: RFmxGSM ModAcc Fetch Magnitude Error Trace VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-magnitude-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-magnitude-error-trace-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the defa

### RFmxGSM ModAcc Fetch Magnitude Error Trace VI

Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-magnitude-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Magnitude Error (%) — Magnitude Error returns the magnitude error trace. This value is expressed as a percentage. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of magnitude error values measured at each time instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of magnitude error values measured at each time instance. |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-phase-error-trace-vi.html language=enus -->
## TOPIC 00082: RFmxGSM ModAcc Fetch Phase Error Trace VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-phase-error-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-phase-error-trace-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the phase error trace concatenated over all the measured time slots for the last acquisition. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal inst

### RFmxGSM ModAcc Fetch Phase Error Trace VI

Fetches the phase error trace concatenated over all the measured time slots for the last acquisition.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-phase-error-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Phase Error (deg) — Phase Error returns the phase error trace. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in symbols. y — y returns an array of phase error values measured at each time instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in symbols. y — y returns an array of phase error values measured at each time instance. |

Parent topic:

RFmxGSM ModAcc Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-vi.html language=enus -->
## TOPIC 00083: RFmxGSM ModAcc Fetch VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the ModAcc measurement results. icon

### RFmxGSM ModAcc Fetch VI

Fetches the ModAcc measurement results.

[IMAGE alt='icon' src='rfmxgsm-modacc-fetch-vi.png']

- [RFmxGSM ModAcc Fetch EVM VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-vi.html) Fetches the EVM measurement results for EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch EVM Magnitude Error VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-magnitude-error-vi.html) Fetches the magnitude error measurement results for EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch EVM Phase Error VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-phase-error-vi.html) Fetches the phase error measurement results for EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch EVM Amplitude Droop VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-amplitude-droop-vi.html) Fetches the amplitude droop measurement results for EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch PFER VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-pfer-vi.html) Fetches the phase and frequency error measurement results for GSM.
- [RFmxGSM ModAcc Fetch IQ Impairments VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-iq-impairments-vi.html) Fetches the origin offset and gain imbalance measurement results for GSM/EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch Detected TSC VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-vi.html) Fetches the detected training sequence code (TSC) of the last burst for GSM/EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch Detected TSC (Array) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-detected-tsc-array-vi.html) Fetches the detected training sequence code (TSC) of the last acquisition for GSM/EDGE/EGPRS.
- [RFmxGSM ModAcc Fetch Constellation Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-constellation-trace-vi.html) Fetches the constellation trace concatenated over all the measured time slots for the last acquisition.
- [RFmxGSM ModAcc Fetch Phase Error Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-phase-error-trace-vi.html) Fetches the phase error trace concatenated over all the measured time slots for the last acquisition.
- [RFmxGSM ModAcc Fetch Demodulated Bits VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-demodulated-bits-vi.html) Fetches the array of demodulated bits concatenated over all the measured time slots for the last acquisition.
- [RFmxGSM ModAcc Fetch Magnitude Error Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-magnitude-error-trace-vi.html) Fetches the EDGE/EGPRS magnitude error trace concatenated over all the measured time slots for the last acquisition.
- [RFmxGSM ModAcc Fetch EVM Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-modacc-fetch-evm-trace-vi.html) Fetches the EDGE/EGPRS RMS EVM trace concatenated over all the measured time slots for the last acquisition.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-averaging-vi.html language=enus -->
## TOPIC 00084: RFmxGSM ORFS Configure Averaging VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-averaging-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the output radio frequency spectrum (ORFS) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empt

### RFmxGSM ORFS Configure Averaging VI

Configures averaging for the output radio frequency spectrum (ORFS) measurement.

[IMAGE alt='icon' src='rfmxgsm-orfs-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is Log. RMS (0) The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. Log (1) The measurement averages the power spectrum in a logarithmic scale. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. |
| RMS (0) | The measurement averages the power spectrum linearly. RMS averaging reduces signal fluctuations but not the noise floor. |
| Log (1) | The measurement averages the power spectrum in a logarithmic scale. |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-evaluation-symbols-vi.html language=enus -->
## TOPIC 00085: RFmxGSM ORFS Configure Evaluation Symbols VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-evaluation-symbols-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-evaluation-symbols-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a

### RFmxGSM ORFS Configure Evaluation Symbols VI

Configures the evaluation symbols. The GSM standard specifies that 50% to 90% portion of the burst, excluding the midamble, be measured. However, RFmxGSM allows you to specify the portion of the burst to measure for ORFS due to modulation. RFmx considers the measurement over evaluation symbols for a single burst as one average.

[IMAGE alt='icon' src='rfmxgsm-orfs-configure-evaluation-symbols-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Evaluation Symbols Start (%) — Evaluation Symbols Start specifies the start position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. The default value is 50. Evaluation Symbols Include TSC — Evaluation Symbols Include TSC specifies whether to include the TSC portion of burst in the ORFS measurement. The default value is False. False (0) The TSC portion of the burst is excluded in the ORFS measurement. True (1) The TSC portion of the burst is included in the ORFS measurement. Evaluation Symbols Stop (%) — Evaluation Symbols Stop specifies the stop position of the burst over which you perform the ORFS measurement. This value is expressed as a percentage. The default value is 90. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The TSC portion of the burst is excluded in the ORFS measurement. |
| True (1) | The TSC portion of the burst is included in the ORFS measurement. |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-noise-compensation-enabled-vi.html language=enus -->
## TOPIC 00086: RFmxGSM ORFS Configure Noise Compensation Enabled VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-noise-compensation-enabled-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-noise-compensation-enabled-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal insta

### RFmxGSM ORFS Configure Noise Compensation Enabled VI

Configures whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer.

[IMAGE alt='icon' src='rfmxgsm-orfs-configure-noise-compensation-enabled-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Noise Compensation Enabled — Noise Compensation Enabled specifies whether to enable compensation of the channel powers for the inherent noise floor of the signal analyzer. The default value is False. False (0) Disables compensation of the channel powers for the signal analyzer noise floor. True (1) Enables compensation of the channel powers for the signal analyzer noise floor. The measurement calculates the signal analyzer noise floor for the RF path used by the output radio frequency spectrum (ORFS) measurement and caches the noise floor for future use. If signal analyzer parameters or measurement parameters change, the measurement calculates noise floors again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | Disables compensation of the channel powers for the signal analyzer noise floor. |
| True (1) | Enables compensation of the channel powers for the signal analyzer noise floor. The measurement calculates the signal analyzer noise floor for the RF path used by the output radio frequency spectrum (ORFS) measurement and caches the noise floor for future use. If signal analyzer parameters or measurement parameters change, the measurement calculates noise floors again. Supported Devices: PXIe-5663/5665/5668R, PXIe-5830/5831/5832 |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-offset-frequency-mode-vi.html language=enus -->
## TOPIC 00087: RFmxGSM ORFS Configure Offset Frequency Mode VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-offset-frequency-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-offset-frequency-mode-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signa

### RFmxGSM ORFS Configure Offset Frequency Mode VI

Configures the list of frequency offsets for which you can perform the output radio frequency spectrum (ORFS) measurements.

[IMAGE alt='icon' src='rfmxgsm-orfs-configure-offset-frequency-mode-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Offset Frequency Mode — Offset Frequency Mode specifies the list of frequency offsets for which you can perform the ORFS measurements. The default value is Standard. Standard (0) Uses a list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. Short (1) Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. Custom (2) Uses the list of frequencies that is configured using the RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) and RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VIs for measurement of spectrum produced by modulation and switching measurements. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Standard (0) | Uses a list of lower and upper offset frequencies of 100 kHz, 200 kHz, 250 kHz, 400 kHz, 600 kHz, 800 kHz, 1000 kHz, 1200 kHz, 1400 kHz, 1600 kHz, and 1800 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Short (1) | Uses the list of lower and upper offset frequencies of 200 kHz, 250 kHz, 400 kHz, 600 kHz, and 1200 kHz for the spectrum due to the modulation measurement, and the lower and upper offset frequencies of 400 kHz, 600 kHz, 1200 kHz, and 1800 kHz for the spectrum produced by the switching measurement. |
| Custom (2) | Uses the list of frequencies that is configured using the RFmxGSM ORFS Configure Modulation Custom Offset Frequency (Array) and RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VIs for measurement of spectrum produced by modulation and switching measurements. |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-switching-custom-offset-frequency-array-vi.html language=enus -->
## TOPIC 00088: RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-switching-custom-offset-frequency-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-configure-switching-custom-offset-frequency-array-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the ORFS Offset Freq Mode property to Custom. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the

### RFmxGSM ORFS Configure Switching Custom Offset Frequency (Array) VI

Configures an array of positive offset frequencies relative to the carrier frequency for the spectrum measurement because of switching when you set the [ORFS Offset Freq Mode](/csh?context=rfmxgsm_rfmxgsmprop_attr402007) property to **Custom**.

[IMAGE alt='icon' src='rfmxgsm-orfs-configure-switching-custom-offset-frequency-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Switching Custom Offset Frequency (Hz) — Switching Custom Offset Frequency specifies an array of positive offset frequencies relative to the frequency of the carrier for the spectrum measurement because of switching when you set the ORFS Offset Freq Mode property to Custom. This value is expressed in Hz. The lower offset frequency or the negative offset value corresponding to each entry is automatically considered for the measurement. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

ORFS

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-power-trace-vi.html language=enus -->
## TOPIC 00089: RFmxGSM ORFS Fetch Modulation Power Trace VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-power-trace-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the modulation power trace and frequency offset. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxGSM ORFS Fetch Modulation Power Trace VI

Fetches the modulation power trace and frequency offset.

[IMAGE alt='icon' src='rfmxgsm-orfs-fetch-modulation-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Offset Frequency (Hz) — Offset Frequency returns an array of modulation offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. Absolute Power (dBm) — Absolute Power returns an array of absolute powers corresponding to the modulation offset frequency list. This value is expressed in dBm. Relative Power (dB) — Relative Power returns an array of relative powers corresponding to modulation offset frequency list. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ORFS Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-results-array-vi.html language=enus -->
## TOPIC 00090: RFmxGSM ORFS Fetch Modulation Results (Array) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-results-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-results-array-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector str

### RFmxGSM ORFS Fetch Modulation Results (Array) VI

Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.

[IMAGE alt='icon' src='rfmxgsm-orfs-fetch-modulation-results-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Lower Absolute Power (dBm) — Lower Absolute Power returns an array of absolute powers measured at the negative modulation offset frequencies. This value is expressed in dBm. Upper Absolute Power (dBm) — Upper Absolute Power returns an array of absolute powers measured at the positive modulation offset frequencies. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Modulation Carrier Power (dBm) — Modulation Carrier Power returns the modulation carrier power. This value is expressed in dBm. Lower Relative Power (dB) — Lower Relative Power returns an array of relative powers measured at the negative modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. Upper Relative Power (dB) — Upper Relative Power returns an array of relative powers measured at the positive modulation offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated modulation power of the carrier. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ORFS Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-power-trace-vi.html language=enus -->
## TOPIC 00091: RFmxGSM ORFS Fetch Switching Power Trace VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-power-trace-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the switching power trace and frequency offsets. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the resul

### RFmxGSM ORFS Fetch Switching Power Trace VI

Fetches the switching power trace and frequency offsets.

[IMAGE alt='icon' src='rfmxgsm-orfs-fetch-switching-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Offset Frequency (Hz) — Offset Frequency returns an array of switching offset frequencies at which the measurement is performed in an ascending order. This value is expressed in Hz. Absolute Power (dBm) — Absolute Power returns an array of absolute powers corresponding to the switching offset frequency list. This value is expressed in dBm. Relative Power (dB) — Relative Power returns an array of relative powers corresponding to the switching offset frequencies. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ORFS Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-results-array-vi.html language=enus -->
## TOPIC 00092: RFmxGSM ORFS Fetch Switching Results (Array) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-results-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-results-array-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string

### RFmxGSM ORFS Fetch Switching Results (Array) VI

Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.

[IMAGE alt='icon' src='rfmxgsm-orfs-fetch-switching-results-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Lower Absolute Power (dBm) — Lower Absolute Power returns an array of absolute powers measured at the negative switching offset frequencies. This value is expressed in dBm. Upper Absolute Power (dBm) — Upper Absolute Power returns an array of absolute powers measured at the positive switching offset frequencies. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Switching Carrier Power (dBm) — Switching Carrier Power returns the switching carrier power. This value is expressed in dBm. Lower Relative Power (dB) — Lower Relative Power returns an array of relative powers measured at the negative switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. Upper Relative Power (dB) — Upper Relative Power returns an array of relative powers measured at the positive switching offset frequencies. This value is expressed in dB. The relative powers are measured relative to the integrated switching power of the carrier. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxGSM ORFS Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-vi.html language=enus -->
## TOPIC 00093: RFmxGSM ORFS Fetch VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the output radio frequency spectrum (ORFS) measurement results. icon

### RFmxGSM ORFS Fetch VI

Fetches the output radio frequency spectrum (ORFS) measurement results.

[IMAGE alt='icon' src='rfmxgsm-orfs-fetch-vi.png']

- [RFmxGSM ORFS Fetch Modulation Results (Array) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-results-array-vi.html) Returns the modulation carrier power, absolute powers, and relative powers measured at the modulation offset frequencies. The relative powers are measured relative to the integrated modulation power of the carrier.
- [RFmxGSM ORFS Fetch Switching Results (Array) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-results-array-vi.html) Fetches the switching carrier power, absolute powers, and relative powers measured at the switching offset frequencies. The relative powers are measured relative to the integrated switching power of the carrier.
- [RFmxGSM ORFS Fetch Modulation Power Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-modulation-power-trace-vi.html) Fetches the modulation power trace and frequency offset.
- [RFmxGSM ORFS Fetch Switching Power Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-orfs-fetch-switching-power-trace-vi.html) Fetches the switching power trace and frequency offsets.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-property-node-vi.html language=enus -->
## TOPIC 00094: RFmxGSM Property Node VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-property-node-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) RFmxGSM properties. icon Inputs/Outputs cgenclassrntag.png niRFmx Instrument Handle Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. cerrcodeclst.png error

### RFmxGSM Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) RFmxGSM properties.

[IMAGE alt='icon' src='rfmxgsm-property-node-vi.png']

#### Inputs/Outputs

| niRFmx Instrument Handle — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx GSM Property Node is used to get (read), set (write), or reset (set to default value) RFmx GSM properties. niRFmx Instrument Handle — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-configure-averaging-vi.html language=enus -->
## TOPIC 00095: RFmxGSM PVT Configure Averaging VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-configure-averaging-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-configure-averaging-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures averaging for the power versus time (PVT) measurement. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Exam

### RFmxGSM PVT Configure Averaging VI

Configures averaging for the power versus time (PVT) measurement.

[IMAGE alt='icon' src='rfmxgsm-pvt-configure-averaging-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Averaging Enabled — Averaging Enabled specifies whether to enable averaging for the measurement. The default value is False. False (0) The measurement is performed on a single acquisition. True (1) The measurement is averaged over multiple acquisitions. Averaging Count — Averaging Count specifies the number of acquisitions used for averaging when you set the Averaging Enabled parameter to True. The default value is 10. Averaging Type — Averaging Type specifies the averaging type for averaging multiple spectrum acquisitions. The averaged spectrum is used for the measurement. The default value is RMS. RMS (0) The power at each sample interval is linearly averaged from an acquisition to the next acquisition. Log (1) The power at each sample interval is averaged on logarithmic scale from an acquisition to the next acquisition. Max (3) The peak power at each sample interval is retained from an acquisition to the next acquisition. Min (4) The lowest power at each sample interval is retained from an acquisition to the next acquisition. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| False (0) | The measurement is performed on a single acquisition. |
| True (1) | The measurement is averaged over multiple acquisitions. |
| RMS (0) | The power at each sample interval is linearly averaged from an acquisition to the next acquisition. |
| Log (1) | The power at each sample interval is averaged on logarithmic scale from an acquisition to the next acquisition. |
| Max (3) | The peak power at each sample interval is retained from an acquisition to the next acquisition. |
| Min (4) | The lowest power at each sample interval is retained from an acquisition to the next acquisition. |

Parent topic:

PVT

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-measurement-status-vi.html language=enus -->
## TOPIC 00096: RFmxGSM PVT Fetch Measurement Status VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-measurement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-measurement-status-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the overall PVT measurement status based on the standard defined measurement limits. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is u

### RFmxGSM PVT Fetch Measurement Status VI

Fetches the overall PVT measurement status based on the standard defined measurement limits.

[IMAGE alt='icon' src='rfmxgsm-pvt-fetch-measurement-status-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1/result::r1" "signal::sig1" "result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Measurement Status — Measurement Status indicates the overall measurement status based on standard-defined limits. Fail (0) The measurement failed because the average power of at least one slot is outside the standard-defined limits. Pass (1) The measurement passed because the average power of all slots is within the standard-defined limits. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Fail (0) | The measurement failed because the average power of at least one slot is outside the standard-defined limits. |
| Pass (1) | The measurement passed because the average power of all slots is within the standard-defined limits. |

Parent topic:

RFmxGSM PVT Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-power-trace-vi.html language=enus -->
## TOPIC 00097: RFmxGSM PVT Fetch Power Trace VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-power-trace-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-power-trace-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the upper mask, signal power, and lower mask trace. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the re

### RFmxGSM PVT Fetch Power Trace VI

Fetches the upper mask, signal power, and lower mask trace.

[IMAGE alt='icon' src='rfmxgsm-pvt-fetch-power-trace-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1/result::r1" "signal::sig1" "result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Upper Mask (dB) — Upper Mask returns the upper mask trace, in dB. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of upper mask values measured at each time instance. Signal Power (dBm) — Signal Power returns the signal power trace. This value is expressed in dBm. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of signal power values measured at each time instance. Lower Mask (dB) — Lower Mask returns the lower mask trace. This value is expressed in dB. x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of lower mask values measured at each time instance. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of upper mask values measured at each time instance. |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of signal power values measured at each time instance. |
| x0 — x0 returns the start time, in seconds. dx — dx returns the sample duration, in seconds. y — y returns an array of lower mask values measured at each time instance. |

Parent topic:

RFmxGSM PVT Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-array-vi.html language=enus -->
## TOPIC 00098: RFmxGSM PVT Fetch Slot Measurement (Array) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-array-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the PVT measurement results for each slot. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name

### RFmxGSM PVT Fetch Slot Measurement (Array) VI

Fetches the PVT measurement results for each slot.

[IMAGE alt='icon' src='rfmxgsm-pvt-fetch-slot-measurement-array-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Slot Minimum Power (dBm) — Slot Minimum Power returns an array of minimum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. Slot Maximum Power (dBm) — Slot Maximum Power returns an array of maximum powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Slot Average Power (dBm) — Slot Average Power returns an array of mean powers of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. Slot Burst Width (s) — Slot Burst Width returns an array of burst widths for the slots where the -3 dB transition points occur. This value is expressed in seconds. Slot Measurement Status — Slot Measurement Status indicates an array of PVT measurement statuses for multiple slots. Fail (0) The signal power is outside the standard-defined upper or lower mask Pass (1) The signal power is within the standard-defined upper and lower mask. error out — error out contains error information. This output provides standard error out functionality. Slot Burst Threshold (dBm) — Slot Burst Threshold returns an array of thresholds that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |  |
| --- | --- |
| Fail (0) | The signal power is outside the standard-defined upper or lower mask |
| Pass (1) | The signal power is within the standard-defined upper and lower mask. |

Parent topic:

RFmxGSM PVT Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-vi.html language=enus -->
## TOPIC 00099: RFmxGSM PVT Fetch Slot Measurement VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the measurement results for a single-slot PVT measurement. Use "slot<n>" as the selector string to read results from this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not sp

### RFmxGSM PVT Fetch Slot Measurement VI

Fetches the measurement results for a single-slot PVT measurement.

Use "slot<*n*>" as the selector string to read results from this VI.

[IMAGE alt='icon' src='rfmxgsm-pvt-fetch-slot-measurement-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and slot number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "slot0" "signal::sig1/slot0" "result::r1/slot0" "signal::sig1/result::r1/slot0" You can use the RFmxGSM Build Slot String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the timeout for fetching the specified measurement. This value is expressed in seconds. Set this value to an appropriate time, longer than expected for fetching the measurement. A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Slot Minimum Power (dBm) — Slot Minimum Power returns the minimum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. Slot Maximum Power (dBm) — Slot Maximum Power returns the maximum power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. Slot Average Power (dBm) — Slot Average Power returns the mean power of the signal, averaged over corresponding slots of each acquisition. This value is expressed in dBm. Slot Burst Width (s) — Slot Burst Width returns the burst width of the slot where the -3 dB transition points occur. This value is expressed in seconds. Slot Measurement Status — Slot Measurement Status indicates the PVT measurement status for a particular slot. Fail (0) The signal power is outside the standard-defined upper or lower mask Pass (1) The signal power is within the standard-defined upper and lower mask. error out — error out contains error information. This output provides standard error out functionality. Slot Burst Threshold (dBm) — Slot Burst Threshold returns the threshold that the PVT measurement uses to determine the burst validity. This value is expressed in dBm. |  |
| --- | --- |
| Fail (0) | The signal power is outside the standard-defined upper or lower mask |
| Pass (1) | The signal power is within the standard-defined upper and lower mask. |

Parent topic:

RFmxGSM PVT Fetch VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-vi.html language=enus -->
## TOPIC 00100: RFmxGSM PVT Fetch VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the power versus time (PVT) measurement results. icon

### RFmxGSM PVT Fetch VI

Fetches the power versus time (PVT) measurement results.

[IMAGE alt='icon' src='rfmxgsm-pvt-fetch-vi.png']

- [RFmxGSM PVT Fetch Measurement Status VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-measurement-status-vi.html) Fetches the overall PVT measurement status based on the standard defined measurement limits.
- [RFmxGSM PVT Fetch Slot Measurement VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-vi.html) Fetches the measurement results for a single-slot PVT measurement.
- [RFmxGSM PVT Fetch Slot Measurement (Array) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-slot-measurement-array-vi.html) Fetches the PVT measurement results for each slot.
- [RFmxGSM PVT Fetch Power Trace VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-pvt-fetch-power-trace-vi.html) Fetches the upper mask, signal power, and lower mask trace.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-reset-to-default-vi.html language=enus -->
## TOPIC 00101: RFmxGSM Reset to Default VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-reset-to-default-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets a signal to the default values. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can

### RFmxGSM Reset to Default VI

Resets a signal to the default values.

[IMAGE alt='icon' src='rfmxgsm-reset-to-default-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-multiple-vi.html language=enus -->
## TOPIC 00102: RFmxGSM Select Measurement (Multiple) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-multiple-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-multiple-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables all the measurements that you specify in the Measurements parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance

### RFmxGSM Select Measurement (Multiple) VI

Enables all the measurements that you specify in the **Measurements** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxgsm-select-measurement-multiple-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurements — Measurements specifies the measurement to perform. You can specify one or more of the following measurements. The default is an empty array. ModAcc (0) Enables the modulation accuracy (ModAcc) measurement. ORFS (1) Enables the output radio frequency spectrum (ORFS) measurement. PVT (2) Enables the power versus time (PVT) measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the modulation accuracy (ModAcc) measurement. |
| ORFS (1) | Enables the output radio frequency spectrum (ORFS) measurement. |
| PVT (2) | Enables the power versus time (PVT) measurement. |

Parent topic:

RFmxGSM Select Measurement VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-single-vi.html language=enus -->
## TOPIC 00103: RFmxGSM Select Measurement (Single) VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-single-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-single-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the measurement that you specify in the Measurement parameter and disables all other measurements. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is use

### RFmxGSM Select Measurement (Single) VI

Enables the measurement that you specify in the **Measurement** parameter and disables all other measurements.

[IMAGE alt='icon' src='rfmxgsm-select-measurement-single-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default is "" (empty string). Example: "signal::sig1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Measurement — Measurement specifies the measurement to perform. You can specify one of the following measurements. The default value is ModAcc. ModAcc (0) Enables the modulation accuracy (ModAcc) measurement. ORFS (1) Enables the output radio frequency spectrum (ORFS) measurement. PVT (2) Enables the power versus time (PVT) measurement. Enable All Traces — Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| ModAcc (0) | Enables the modulation accuracy (ModAcc) measurement. |
| ORFS (1) | Enables the output radio frequency spectrum (ORFS) measurement. |
| PVT (2) | Enables the power versus time (PVT) measurement. |

Parent topic:

RFmxGSM Select Measurement VI

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-vi.html language=enus -->
## TOPIC 00104: RFmxGSM Select Measurement VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. icon

### RFmxGSM Select Measurement VI

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

[IMAGE alt='icon' src='rfmxgsm-select-measurement-vi.png']

- [RFmxGSM Select Measurement (Single) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-single-vi.html) Enables the measurement that you specify in the Measurement parameter and disables all other measurements.
- [RFmxGSM Select Measurement (Multiple) VI](../../../../../vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-select-measurement-multiple-vi.html) Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

Parent topic:

GSM

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00105: RFmxGSM Send Software Edge Trigger VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-send-software-edge-trigger-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you use the RFmxGSM Configure Trigger VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger. This VI returns an error in the following situations: You configure an

### RFmxGSM Send Software Edge Trigger VI

Sends a trigger to the device when you use the [RFmxGSM Configure Trigger](/csh?topicname=rfmxgsm-configure-trigger-vi.html) VI to choose a software version of a trigger and the device is waiting for the trigger to be sent. You can also use this VI to override a hardware trigger.

This VI returns an error in the following situations:

- You configure an invalid trigger.
- You have not previously called the RFmxGSM Initiate VI.

[IMAGE alt='icon' src='rfmxgsm-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00106: RFmxGSM Wait for Measurement Complete VI

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/rfmxgsm-wait-for-measurement-complete-vi.html
- document_id: `rfmxgsm-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxGSM Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxgsm-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default is "" (empty string). Example: "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxGSM Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Timeout (s) — Timeout specifies the time for which the VI waits for the measurement to complete. This value is expressed in seconds. A value of -1 specifies that the VI waits until the measurement is complete. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference to your RFmx session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00107: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxgsm-labview-api-ref`
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

<!--NI_TOPIC bundle=rfmxgsm-labview-api-ref path=vi-lib/rfmx/gsm/mx/rfmxgsm-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00108: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxgsm-labview-api-ref`
- source_path: `vi-lib/rfmx/gsm/mx/rfmxgsm-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxgsm-labview-api-ref/raw/resource/enus/vi-lib/rfmx/gsm/mx/rfmxgsm-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxgsm-labview-api-ref`
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
