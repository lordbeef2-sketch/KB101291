# NI DOCUMENT BUNDLE: rfmxvna-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxvna-labview-api-ref start=1 end=99 -->
<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/configuration/dir-mnu.html language=enus -->
## TOPIC 00001: Configuration

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/configuration/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/configuration/dir-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure measurements. You can use the RFmxVNA Property Node VI to configure additional properties. icon

### Configuration

Use the VIs on this palette to configure measurements. You can use the [RFmxVNA Property Node](/csh?context=rfmxvna_rfmxvnavi_rfmxvna_property_node) VI to configure additional properties.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxVNA Send Software Edge Trigger VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-send-software-edge-trigger-vi.html) Sends a trigger to the device when you set Trigger Type to Software and the device is waiting for the trigger to be sent.
- [RFmxVNA Auto Port Extension Measure VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-measure-vi.html) Automatically determine the fixture delay and loss (optional) values by measuring the standard at the configured port. The calculated delay and loss values are used to set the Port Extension Delay (s) , Port Extension DC Loss (dB) , Port Extension Loss1 (dB) and Port Extension Loss2 (dB) properties. Call this VI after calibrating the VNA port, where port extension is required, to obtain more accurate delay and loss estimates.
- [RFmxVNA Auto Port Extension Reset VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-reset-vi.html) Resets the measured standard data used for automatic port extension.
- [Correction](../../../../../../menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-correction-mnu.html) Use the VIs on this palette to configure correction. You can use the RFmxVNA Property Node to configure additional properties.
- [Calset](../../../../../../menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-calset-mnu.html) Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties.
- [SParams](../../../../../../menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-sparams-mnu.html) Use the VIs on this palette to configure S-Parameter measurements. You can use the RFmxVNA Property Node to configure additional properties.
- [Waves](../../../../../../menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-waves-mnu.html) Use the VIs on this palette to configure Wave measurements. You can use the RFmxVNA Property Node to configure additional properties.

Parent topic:

VNA

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-calset-mnu.html language=enus -->
## TOPIC 00002: Calset

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-calset-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-calset-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties. icon

### Calset

Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-vna-mx-configuration-calset-mnu.png']

- [RFmxVNA Calset Load from File VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-load-from-file-vi.html) Loads calset from a calset file (*.ncst), either to the default calset of the specified signal or to a named calset accessible across all signals.
- [RFmxVNA Calset Save to File VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-save-to-file-vi.html) Saves to a calset file (*.ncst), either the default calset of the specified signal or a named calset accessible across all signals and corresponding relevant stimulus settings that were used to perform calibration.
- [RFmxVNA Select Active Calset VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-select-active-calset-vi.html) Selects either the default calset of the specified signal or a named calset accessible across all signals as active calset for the specified signal.
- [RFmxVNA Deselect Active Calset VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-deselect-active-calset-vi.html) Deselects the active calset of the specified signal. You can select an active calset again using RFmxVNA Select Active Calset VI.
- [RFmxVNA Clear Calset VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clear-calset-vi.html) Clears either the default calset of the specified signal or a named calset accessible across all signals.
- [RFmxVNA Copy Calset VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-copy-calset-vi.html) Copies into a new calset either from the default calset of the specified signal or a named calset accessible across all signals.
- [RFmxVNA Get All Calset Names VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-get-all-calset-names-vi.html) Returns an array of calset names of all the available named calsets which are accessible across all signals.
- [RFmxVNA Calset Get Frequency Grid VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-frequency-grid-vi.html) Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals.
- [RFmxVNA Calset Get Error Term VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-error-term-vi.html) Returns values for a specific error term from either the default calset of the specified signal or a named calset accessible across all signals.
- [RFmxVNA Calset Embed Fixture (s2p) VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-embed-fixture-s2p-vi.html) Embeds the inverse of a given fixture network into a specified calset.
- [RFmxVNA Build CalStep String VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calstep-string-vi.html) Creates the calibration step string to use as the selector string with the RFmxVNA Calibration Acquire VI.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-correction-mnu.html language=enus -->
## TOPIC 00003: Correction

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-correction-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-correction-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure correction. You can use the RFmxVNA Property Node to configure additional properties. icon

### Correction

Use the VIs on this palette to configure correction. You can use the RFmxVNA Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-vna-mx-configuration-correction-mnu.png']

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-sparams-mnu.html language=enus -->
## TOPIC 00004: SParams

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-sparams-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-sparams-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure S-Parameter measurements. You can use the RFmxVNA Property Node to configure additional properties. icon

### SParams

Use the VIs on this palette to configure S-Parameter measurements. You can use the RFmxVNA Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-vna-mx-configuration-sparams-mnu.png']

- [RFmxVNA SParams Configure S-Parameter VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-configure-s-parameter-vi.html) Configures the S-Parameter to be measured in format S< receiver port number >< source port number >
- [RFmxVNA SParams Get S-Parameter VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-get-s-parameter-vi.html) Returns the S-Parameter being measured in format S< receiver port number >< source port number >
- [RFmxVNA SParams Export to SnP File VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-export-to-snp-file-vi.html) Exports the measured S-parameters to a SnP file.
- [RFmxVNA Build S-Parameter String VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-s-parameter-string-vi.html) Creates the selector string to use with S-Parameter configuration or fetch properties and VIs.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-waves-mnu.html language=enus -->
## TOPIC 00005: Waves

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-waves-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/configuration/rfmx-vna-mx-configuration-waves-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure Wave measurements. You can use the RFmxVNA Property Node to configure additional properties. icon

### Waves

Use the VIs on this palette to configure Wave measurements. You can use the RFmxVNA Property Node to configure additional properties.

[IMAGE alt='icon' src='rfmx-vna-mx-configuration-waves-mnu.png']

- [RFmxVNA Waves Configure Wave VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-configure-wave-vi.html) Configures the wave to be measured in format a< receiver port number >< source port number > or b< receiver port number >< source port number >, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver.
- [RFmxVNA Waves Get Wave VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-get-wave-vi.html) Returns the wave being measured in format a< receiver port number >< source port number > or b< receiver port number >< source port number >, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver.
- [RFmxVNA Build Wave String VI](../../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-wave-string-vi.html) Creates the selector string to use with Wave configuration or fetch properties and VIs.

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/dir-mnu.html language=enus -->
## TOPIC 00006: VNA

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/dir-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to perform VNA measurements. You can use the RFmxVNA Property Node to configure additional properties. © 2022–2026 National Instruments Corporation. All rights reserved. icon

### VNA

Use the VIs on this palette to perform VNA measurements. You can use the [RFmxVNA Property Node](/csh?context=rfmxvna_rfmxvnavi_rfmxvna_property_node) to configure additional properties.

© 2022–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [Configuration](../../../../../menus/categories/measurement/rfmx/vna/configuration/dir-mnu.html) Use the VIs on this palette to configure measurements. You can use the RFmxVNA Property Node VI to configure additional properties.
- [RFmxVNA Select Measurement VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-select-measurement-vi.html) Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.
- [RFmxVNA Initiate VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-initiate-vi.html) Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxVNA Wait for Measurement Complete VI or RFmxVNA Check Measurement Status VI.
- [Fetch](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-fetch-mnu.html) Use the VIs on this palette to fetch measurement results and traces.
- [Utility](../../../../../menus/categories/measurement/rfmx/vna/utility/dir-mnu.html) Use the VIs on this palette to configure utility measurements. You can use the RFmxVNA Property Node to configure additional properties.
- [RFmxVNA Property Node VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-property-node-vi.html) Gets (reads), sets (writes), or resets (sets to default value) RFmxVNA properties.
- [Build String](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-utility-build-string-mnu.html) Use the VIs on this palette to create strings for configurations that require a selector string.
- [Advanced](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-advanced-mnu.html) Use the VIs on this palette to use advanced features.
- [Calibration](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-mnu.html) Use the VIs on this palette to use calibration.
- [Marker](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-marker-mnu.html) Use the VIs on this palette to configure marker measurements.
- [Memory](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-memory-mnu.html) Use the VIs on this palette to Copy/Load data to measurement memory.

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-advanced-mnu.html language=enus -->
## TOPIC 00007: Advanced

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-advanced-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to use advanced features. icon

### Advanced

Use the VIs on this palette to use advanced features.

[IMAGE alt='icon' src='rfmx-vna-mx-advanced-mnu.png']

- [RFmxVNA Abort Measurements VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-abort-measurements-vi.html) Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxVNA Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.
- [RFmxVNA Create Signal Configuration VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-create-signal-configuration-vi.html) Creates a new instance of a signal. RFmxVNA Signal concept is same as Channel concept in third party software.
- [RFmxVNA Clone Signal Configuration VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clone-signal-configuration-vi.html) Creates a new instance of a signal by copying all the property values from an existing signal instance.
- [RFmxVNA Delete Signal Configuration VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-delete-signal-configuration-vi.html) Deletes an instance of a signal that you specify in the Signal Name parameter.
- [RFmxVNA Get All Named Result Names VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-get-all-named-result-names-vi.html) Returns all the named result names of the signal that you specify in the Selector String parameter.
- [RFmxVNA Clear Named Result VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clear-named-result-vi.html) Clears a result instance specified by the result name in the Selector String parameter.
- [RFmxVNA Clear All Named Results VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clear-all-named-results-vi.html) Clears all results for the signal that you specify in the Selector String parameter.

Parent topic:

VNA

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-delaymodel-mnu.html language=enus -->
## TOPIC 00008: Delay Model

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-delaymodel-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-delaymodel-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure delay model based calibration element. icon

### Delay Model

Use the VIs on this palette to configure delay model based calibration element.

[IMAGE alt='icon' src='rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-delaymodel-mnu.png']

- [RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Set Delay VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-delay-model-set-delay-vi.html) Defines the Delay of a Calibration Element defined by the Delay Model.
- [RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-delay-model-get-delay-vi.html) Returns the Delay of a Calibration Element defined by the Delay Model.

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-mnu.html language=enus -->
## TOPIC 00009: Calibration Element

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure calibration element. icon

### Calibration Element

Use the VIs on this palette to configure calibration element.

[IMAGE alt='icon' src='rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-mnu.png']

- [RFmxVNA Calkit Manager Calkit Calibration Element Set Description VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-description-vi.html) Sets the description for a Calibration Element of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Calibration Element Get Description VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-get-description-vi.html) Returns the description for a Calibration Element of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Calibration Element Set Types VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-types-vi.html) Sets the type(s) of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Get Types VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-get-types-vi.html) Returns the type(s) of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-port-connectors-vi.html) Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Get Port Connectors VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-get-port-connectors-vi.html) Returns the array of Connectors associated with the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-s-parameter-definition-vi.html) Defines the way how the S-Parameters of the Calibration Element are specified.
- [RFmxVNA Calkit Manager Calkit Calibration Element Get S-Parameter Definition VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-get-s-parameter-definition-vi.html) Returns the S-Parameter definition of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-minimum-frequency-vi.html) Sets the Minimum Frequency of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Get Minimum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-get-minimum-frequency-vi.html) Returns the Minimum Frequency of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-maximum-frequency-vi.html) Sets the Maximum Frequency of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element Get Maximum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-get-maximum-frequency-vi.html) Returns the Maximum Frequency of the Calibration Element.
- [Reflect Model](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-reflectmodel-mnu.html) Use the VIs on this palette to configure Reflect Model based calibration element.
- [Delay Model](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-delaymodel-mnu.html) Use the VIs on this palette to configure delay model based calibration element.
- [S-Parameter based](../../../../../menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-sparam-mnu.html) Use the VIs on this palette to configure s-parameter based calibration element.

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-reflectmodel-mnu.html language=enus -->
## TOPIC 00010: Reflect Model

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-reflectmodel-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-reflectmodel-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure Reflect Model based calibration element. icon

### Reflect Model

Use the VIs on this palette to configure Reflect Model based calibration element.

[IMAGE alt='icon' src='rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-reflectmodel-mnu.png']

- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Model Type VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-model-type-vi.html) Specifies the model type of the 1-port reflect standard.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Model Type VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-model-type-vi.html) Returns the model type of of the 1-port reflect standard.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-s-param-availability-vi.html) Specifies the S-Parameter availability.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get S-Param Availability VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-s-param-availability-vi.html) Returns the S-Parameter availability.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C0 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-c0-vi.html) Specifies the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C0 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c0-vi.html) Returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C1 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-c1-vi.html) Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C1 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c1-vi.html) Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C2 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-c2-vi.html) Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c2-vi.html) Returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C3 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-c3-vi.html) Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C3 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c3-vi.html) Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Delay VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-offset-delay-vi.html) Specifies the offset delay.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Delay VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-offset-delay-vi.html) Returns the offset delay.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Loss VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-offset-loss-vi.html) Specifies the offset loss.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Loss VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-offset-loss-vi.html) Returns the offset loss.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Z0 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-offset-z0-vi.html) Specifies the impedance of the offset.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Z0 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-offset-z0-vi.html) Returns the impedance of the offset.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Reference Impedance VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-reference-impedance-vi.html) Specifies the reference impedance.
- [RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Reference Impedance VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-reference-impedance-vi.html) Returns the reference impedance.

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-sparam-mnu.html language=enus -->
## TOPIC 00011: S-Parameter based

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-sparam-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-sparam-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure s-parameter based calibration element. icon

### S-Parameter based

Use the VIs on this palette to configure s-parameter based calibration element.

[IMAGE alt='icon' src='rfmx-vna-mx-calibration-calkitmanager-calkit-calibrationelement-sparam-mnu.png']

- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-frequency-vi.html) Defines the frequency array for the S-Parameter definition of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-frequency-vi.html) Returns the frequency array for the S-Parameter definition of the Calibration Element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S-Param Availability VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s-param-availability-vi.html) Defines the S-Parameter availability.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s-param-availability-vi.html) Returns the S-Parameter availability.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S11 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s11-vi.html) Sets the S11 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S11 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s11-vi.html) Returns the S11 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s12-vi.html) Sets the S12 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S12 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s12-vi.html) Returns the S12 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S21 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s21-vi.html) Sets the S21 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S21 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s21-vi.html) Returns the S21 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S22 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s22-vi.html) Sets the S22 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S22 VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s22-vi.html) returns the S22 S-Parameter for the calibration element.
- [RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-from-file-vi.html) Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element.

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-connector-mnu.html language=enus -->
## TOPIC 00012: Connector

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-connector-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-connector-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure additional options for an RFmxVNA Calkit. icon

### Connector

Use the VIs on this palette to configure additional options for an RFmxVNA Calkit.

[IMAGE alt='icon' src='rfmx-vna-mx-calibration-calkitmanager-calkit-connector-mnu.png']

- [RFmxVNA Calkit Manager Calkit Connector Set Description VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-description-vi.html) Sets the description for a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Get Description VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-get-description-vi.html) Returns the description of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Set Gender VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-gender-vi.html) Sets the Gender of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Get Gender VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-get-gender-vi.html) Returns the Gender of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Set Type VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-type-vi.html) Sets the Type of a Connector of a specific Calkit. Connector type is a user defined string (for example 'SMA', '1.8mm', etc.).
- [RFmxVNA Calkit Manager Calkit Connector Get Type VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-get-type-vi.html) Returns the Type of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Set Impedance VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-impedance-vi.html) Sets the Impedance of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Get Impedance VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-get-impedance-vi.html) Returns the Impedance of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Set Minimum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-minimum-frequency-vi.html) Sets the Minimum Frequency of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Get Minimum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-get-minimum-frequency-vi.html) Returns the Minimum Frequency of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Set Maximum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-maximum-frequency-vi.html) Sets the Maximum Frequency of a Connector of a specific Calkit.
- [RFmxVNA Calkit Manager Calkit Connector Get Maximum Frequency VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-get-maximum-frequency-vi.html) Returns the Maximum Frequency of a Connector of a specific Calkit.

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-options-mnu.html language=enus -->
## TOPIC 00013: Options

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-options-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/vna/rfmx-vna-mx-calibration-calkitmanager-calkit-options-mnu.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure additional options for an RFmxVNA Calkit.

### Options

Use the VIs on this palette to configure additional options for an RFmxVNA Calkit.

- [RFmxVNA Calkit Manager Calkit Set TRL Reference Plane VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-set-trl-reference-plane-vi.html) Sets the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration. Use Reflect, if the Thru standard is uncertainly known and the Reflect standard is well defined. Otherwise use the Thru standard to define the reference plane.
- [RFmxVNA Calkit Manager Calkit Get TRL Reference Plane VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-get-trl-reference-plane-vi.html) Returns the calibration standard (Thru or Reflect) that is used to define the measurement reference plane for TRL calibration.
- [RFmxVNA Calkit Manager Calkit Set LRL Line Auto Char VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-set-lrl-line-auto-char-vi.html) Configures whether line parameters are automatically characterized during LRL calibration. LRL line auto characterization is applicable only when the Line standards have the same characteristic impedance.
- [RFmxVNA Calkit Manager Calkit Get LRL Line Auto Char VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-get-lrl-line-auto-char-vi.html) Returns whether line parameters are automatically characterized during LRL calibration.

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna-p.html language=enus -->
## TOPIC 00014: RFmxVNA Properties

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna-p.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna-p.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the RFmxVNA properties to access options for configuring and fetching measurements. © 2022–2026 National Instruments Corporation. All rights reserved.

### RFmxVNA Properties

Use the RFmxVNA properties to access options for configuring and fetching measurements.

© 2022–2026 National Instruments Corporation. All rights reserved.

- [Advanced:Ground Terminated Ports](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0200d.html) Specifies the selection of ports to be ground terminated in case of SM2 devices. The ports passed to this attribute will be mutually exclusive to the ports passed to the Selected Ports attribute.
- [Advanced:Limited Configuration Change](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0200b.html) Specifies the set of properties that are considered by NI-RFmx in the locked signal configuration state.
- [Advanced:Source Power Mode](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0200c.html) Specifies whether to make VNA measurements with source turned off.
- [Averaging:Count](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00008.html) Specifies the number of times each measurement is repeated and averaged-over. This property is used only when you set the Averaging Enabled property to True .
- [Averaging:Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00007.html) Specifies whether to enable measurement averaging.
- [Correction:Calibration:Calkit:Electronic:Orientation](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0001e.html) Specifies the orientation of the vCal fixture ports with respect to vCal ports.
- [Correction:Calibration:Calkit:Electronic:Resource Name](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00013.html) Specifies the resource name of the electronic calibration module (vCal) used for calibration. This property is used only when you set the Calkit Type property to Electronic .
- [Correction:Calibration:Calkit:Mechanical:Name](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00014.html) Specifies the name of the mechanical calkit used for calibration. This property is used only when you set the Calkit Type property to Mechanical .
- [Correction:Calibration:Calkit:Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00012.html) Specifies the type of calkit used for calibration.
- [Correction:Calibration:Connector Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00011.html) Specifies the connector type of the DUT. The specified connector type must be supported by the calkit that you selected for calibration.
- [Correction:Calibration:Estimated Thru Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00800.html) Returns the estimated Thru Delay when Thru Method is set to Undefined Thru .
- [Correction:Calibration:Method](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00015.html) Specifies the calibration method.
- [Correction:Calibration:Ports](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00010.html) Specifies the ports that are selected for calibration. Use comma-separated list of ports to specify multiple ports.
- [Correction:Calibration:Step:Count](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00019.html) Returns the total number of manual connection steps required to perform the selected calibration routine.
- [Correction:Calibration:Step:Description](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0001a.html) Returns the description for the specified calibration step. You can use the description for each calibration step to determine which mechanical cal standard or electronic calkit module should you connect to which VNA port(s).
- [Correction:Calibration:Thru:Coax:Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00018.html) Specifies the delay of the Thru mechanical standard when Calkit Type property is set to Mechanical and Thru Method property is set to Auto or Undefined Thru . This value is expressed in seconds.
- [Correction:Calibration:Thru:Method](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00017.html) Specifies the Thru calibration method when Calibration Method property is set to SOLT .
- [Correction:Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0000b.html) Specifies whether to enable error correction for VNA measurement.
- [Correction:Interpolation Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00058.html) Specifies whether to enable interpolation of error terms for corrected VNA measurement. This property is used only when you set the Correction Enabled property to True .
- [Correction:Port Extension:Auto:Frequency Mode](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007c.html) Specifies the frequency mode over which the delay and loss (optional) values are determined.
- [Correction:Port Extension:Auto:Loss Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007a.html) Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values.
- [Correction:Port Extension:Auto:Regularization Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007b.html) Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This property is used only when you set the Auto Port Extension Loss Enabled property to True .
- [Correction:Port Extension:Auto:Start Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007d.html) Specifies the start frequency of the user span. This property is used only when you set the Auto Port Extension Frequency Mode property to User Span . This value is expressed in Hz.
- [Correction:Port Extension:Auto:Stop Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007e.html) Specifies the stop frequency of the user span. This property is used only when you set the Auto Port Extension Frequency Mode property to User Span . This value is expressed in Hz.
- [Correction:Port Extension:Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00027.html) Specifies the port extension electrical delay. This value is expressed in seconds. This property is used only when you set the Port Extension Enabled property to True .
- [Correction:Port Extension:Delay Domain](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0005f.html) Specifies whether port extension utilizes delay-based or distance-velocity factor-based definition. This property is used only when you set the Port Extension Enabled property to True .
- [Correction:Port Extension:Distance](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00060.html) Specifies the port extension delay in physical length. This value is expressed in meters by default. The unit can be chosen by setting the Port Extension Distance Unit property. This property is used only when you set the Port Extension Enabled property to True and Port Extension Delay Domain property to Distance .
- [Correction:Port Extension:Distance Unit](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00061.html) Specifies the unit of the port extension delay in physical length. This property is used only when you set the Port Extension Enabled property to True and Port Extension Delay Domain property to Distance .
- [Correction:Port Extension:Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00026.html) Specifies whether to enable port extension.
- [Correction:Port Extension:Loss:DC Loss (dB)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00029.html) Specifies the frequency-independent loss to compensate as part of the port extension. This property is used only when you set the Port Extension Enabled property to True . This value is expressed in dB.
- [Correction:Port Extension:Loss:DC Loss Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00028.html) Specifies whether to compensate for the frequency-independent loss as part of the port extension. This property is used only when you set the Port Extension Enabled property to True .
- [Correction:Port Extension:Loss:Loss1 (dB)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0005b.html) Specifies the frequency-dependent loss, Loss1 in dB, to compensate as part of port extension.
- [Correction:Port Extension:Loss:Loss1 Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00059.html) Specifies whether to compensate for the frequency-dependent loss, Loss1, as part of the port extension. This property is used only when you set the Port Extension Enabled property to True .
- [Correction:Port Extension:Loss:Loss1 Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0005a.html) Specifies the frequency at which Loss1 is applied and compensated. This property is used only when the Port Extension Enabled property is set to True and the Port Extension Loss1 Enabled property is set to True . This value is expressed in Hz.
- [Correction:Port Extension:Loss:Loss2 (dB)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0005e.html) Specifies the frequency-dependent loss, Loss2 in dB, to compensate as part of the port extension.
- [Correction:Port Extension:Loss:Loss2 Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0005c.html) Specifies whether to compensate for the frequency-dependent loss, Loss2, as part of the port extension. This property is used only when you set the Port Extension Enabled property to True and the Port Extension Loss1 Enabled property is set to True .
- [Correction:Port Extension:Loss:Loss2 Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0005d.html) Specifies the frequency at which Loss2 is applied and compensated. This property is used only when the Port Extension Enabled property is set to True , the Port Extension Loss1 Enabled property is set to True and the Port Extension Loss2 Enabled property is set to True . This value is expressed in Hz.
- [Correction:Port Extension:Velocity Factor](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00062.html) Specifies the speed of light in the port extension medium relative to speed of light in vacuum. Velocity Factor of 1 represents speed of light in vacuum. This property is used in conjuction with Port Extension Distance property to compute electrical delay. This value is unitless. This property is used only when you set the Port Extension Enabled property to True and Port Extension Delay Domain property to Distance .
- [Correction:Port Subset:Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0000e.html) Specifies whether to enable correction for a subset of ports for which calibration data is avaialble in the calset. This property is used only when you set the Correction Enabled property to True .
- [Correction:Port Subset:Full Ports](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0000f.html) Specifies the subset of ports, that are selected for full N-Port correction, where N is the number of ports specified in this property. Use comma-separated list of ports to specify multiple ports. The configured measurement is full N-Port corrected if both the measurement receiver and source port are specified using this property. The configured measurement is one-path two-port corrected if one of the measurement ports is specified using this property and another is specified using Correction Port Subset Response Ports . Measurements involving the ports outside Correction Port Subset Full Ports and Correction Port Subset Response Ports return error.
- [Correction:Port Subset:Response Ports](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00079.html) Specifies the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using Correction Port Subset Full Ports . Measurements involving the ports outside the Correction Port Subset Response Ports and Correction Port Subset Full Ports return error.
- [Event:Index:Level](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00068.html) Specifies the trigger level for the Index event. This event indicates that the analyzer has completed all acquisitions for the signal.
- [Event:Index:Output Terminal](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00066.html) Specifies the destination terminal name for the Index event. This event indicates that the analyzer has completed all acquisitions for the signal. Use Index Event Level to define the polarity.
- [Event:Index:Terminal Name](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00067.html) Returns the fully qualified signal name as string.
- [Event:Ready For Trigger:Level](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00065.html) Specifies the trigger level for the Ready For Trigger event. This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger.
- [Event:Ready For Trigger:Output Terminal](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00063.html) Specifies the destination terminal name for the Ready For Trigger event. This event indicates to an external device responsible for sending triggers that the VNA is ready to receive the trigger. Use Ready For Trigger Event Level to define the polarity.
- [Event:Ready For Trigger:Terminal Name](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00064.html) Returns the fully qualified signal name as string.
- [IQ:Acquisition Time (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0100d.html)
- [IQ:Measurement Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0100a.html)
- [IQ:Receiver Port](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0100f.html)
- [IQ:Results:Correction:State](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01019.html) Returns the error correction state of the VNA IQ measurement.
- [IQ:Source Port](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01010.html)
- [Result Fetch Timeout (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0c000.html) Specifies the time, in seconds, to wait before results are available. Set this value to a time longer than expected for fetching the measurement. A value of -1 specifies that the RFmxVNA waits until the measurement is complete.
- [SParams:Format](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01005.html) Specifies the format of S-Parameter measurement.
- [SParams:Group Delay Aperture:Frequency Span (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0101f.html) Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all S-Parameters for which Sparams Format property is set to Group Delay and SParams Group Delay Aperture Mode property is set to Frequency Span .
- [SParams:Group Delay Aperture:Mode](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0101c.html) Specifies the aperture mode to be used for the computation of group delay for all S-Parameters for which Sparams Format property is set to Group Delay .
- [SParams:Group Delay Aperture:Percentage (%)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0101e.html) Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all S-Parameters for which Sparams Format property is set to Group Delay and SParams Group Delay Aperture Mode property is set to Percentage .
- [SParams:Group Delay Aperture:Points](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0101d.html) Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all S-Parameters for which Sparams Format property is set to Group Delay and SParams Group Delay Aperture Mode property is set to Points . You must set the value of this property between 2 and the total number of frequency points in the measurement frequency range.
- [SParams:Magnitude Units](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01006.html) Specifies the magnitude units for all S-Parameters for which you set Sparams Format property to Magnitude .
- [SParams:Math:Active Measurement Memory](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0101b.html) Specifies the active measurement memory for performing mathematical operations when several measurement memories are associated with the configured S-Parameter. If only one measurement memory is associated with the configured S-Parameter, that measurement memory will be used for mathematical operations.
- [SParams:Math:Function](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0101a.html) Specifies the mathematical operation between the configured S-Parameter and its active measurement memory. All mathematical operations are applied on complex data before being formatted.
- [SParams:Measurement Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01000.html) Specifies whether to enable the Sparams measurement.
- [SParams:Number of S-Parameters](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01002.html) Specifies the number of S-Parameters to measure.
- [SParams:Phase Trace Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01007.html) Specifies the phase type for all S-Parameters for which Sparams Format property is set to Phase . Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.
- [SParams:Receiver Port](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01003.html) Specifies the receiver port name of the S-Parameter. S-Parameter is denoted by "S_< receiver port name >_< source port name >".
- [SParams:Results:Correction:Level](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01020.html) Returns the level of error correction applied to the specified S-Parameter measurement.
- [SParams:Results:Correction:State](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01018.html) Returns the error correction state of the VNA S-Parameter measurement.
- [SParams:SnP Export:Data Format](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01013.html) Specifies the format in which the measured S-parameters are saved in a SnP file.
- [SParams:SnP Export:Ports](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01015.html) Specifies the ports for which the measured S-parameters are saved to file.
- [SParams:SnP Export:User Comment](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01014.html) Specifies a string that is incorporated into saved SnP file. You can specify any arbitrary string to add any meta information that you may want to store along with the measured S-Parameters data in SnP file. RFmx automatically adds a special token(!) at the start of this string such that any standard SnP file parsers would ignore this line. Additionally, multiline comments are allowed and each line is appended with the next line escape character.
- [SParams:Source Port](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd01004.html) Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_< receiver port name >_< source port name >".
- [Selector String](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00000.html) Specifies the selector string used to access all subsequent channel-based properties in this instance of the property node.
- [Sweep:Auto IF Bandwidth Scaling Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00046.html) Specifies whether IF Bandwidth is automatically scaled down to account for the increased VNA receiver noise at low frequencies. This property will automatically set to False when Pulse Mode Enabled property is set to True .
- [Sweep:Frequency:CW Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0006a.html) Specifies the frequency at which measurements are performed. This property is used only when you set the Sweep Type property to CW Time . This value is expressed in Hz.
- [Sweep:Frequency:Frequency List (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00002.html) Specifies the frequency values for the configured measurements. The frequencies must be in ascending order and must not contain duplicates. This property is used only when you set the Sweep Type property to List . This value is expressed in Hz.
- [Sweep:Frequency:Start Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00051.html) Specifies the lowest frequency at which measurements are performed. This property is used only when you set the Sweep Type property to Linear . This value is expressed in Hz.
- [Sweep:Frequency:Stop Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00052.html) Specifies the highest frequency at which measurements are performed. This property is used only when you set the Sweep Type property to Linear . This value is expressed in Hz.
- [Sweep:IF Bandwidth (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00004.html) Specifies the digital IF filter bandwidth. This value is expressed in Hz.
- [Sweep:Number of Points](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00053.html) Specifies the number of points at which measurements are performed. This property is used only when you set the Sweep Type property to Linear or CW Time .
- [Sweep:Power Level (dBm)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00003.html) Specifies the power level for the VNA source port. This value is expressed in dBm.
- [Sweep:Pulse:Acquisition:Auto](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00039.html) Specifies whether, based on Pulse Modulator Width , the measurement automatically sets appropriate Pulse Acquisition Delay and Pulse Acquisition Width . This property is used only when you set Pulse Mode Enabled property to True .
- [Sweep:Pulse:Acquisition:Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0003a.html) Specifies the delay in the start of the pulse acquisition relative to the pulse trigger. Pulse trigger can be internal or external. When you set Pulse Trigger Type to None then the VNA creates appropriate periodic pulse triggers internally. This property is used only when you set Pulse Mode Enabled property to True and Pulse Acquisition Auto property to False . This value is expressed in seconds.
- [Sweep:Pulse:Acquisition:Width (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0003b.html) Specifies the acquisition-time per point for pulse measurements. This property is used only when you set Pulse Mode Enabled property to True and Pulse Acquisition Auto property to False . This value is expressed in seconds.
- [Sweep:Pulse:Generator:Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00040.html) Specifies the delay between the pulse trigger and digital pulse generated by the selected Pulse Generator. You must set the value of the this property such that Delay + Pulse Generator Width property does not exceed Pulse Period property. This value is expressed in seconds.
- [Sweep:Pulse:Generator:Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0003e.html) Specifies whether to enable a pulse generator. This property is used only when you set Pulse Mode Enabled property to True .
- [Sweep:Pulse:Generator:Export Output Terminal](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0003f.html) Specifies the destination terminal for an exported Pulse Generator. This property is used only when you set Pulse Mode Enabled property to True and Pulse Generator Enabled property to True .
- [Sweep:Pulse:Generator:Terminal Name](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00050.html) Returns the fully qualified signal name as a string.
- [Sweep:Pulse:Generator:Width (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00041.html) Specifies the pulse width of the selected pulse generator.
- [Sweep:Pulse:Mode Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00031.html) Specifies whether to use pulsed RF signal as stimulus and/or export pulse generator digital signals.
- [Sweep:Pulse:Modulator:Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00037.html) Specifies the delay between the pulse trigger digital edge and the rising edge of the RF pulse. This property is used only when you set Pulse Mode Enabled property to True . This value is expressed in seconds.
- [Sweep:Pulse:Modulator:Width (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00038.html) Specifies the Pulse Width of the pulsed RF signal. Pulse is in HIGH state for a duration equal to the Pulse Width, and remains in the LOW state for the rest of the Pulse Period. This property is used only when you set Pulse Mode Enabled property to True . This value is expressed in seconds.
- [Sweep:Pulse:Period (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00035.html) Specifies the time interval after which the pulse repeats. This property is used only when you set the Pulse Mode Enabled property to True . If you set Pulse Trigger Type property to Digital Edge , pulses are generated only when an external pulse digital edge trigger is received by the VNA. This value is expressed in seconds.
- [Sweep:Pulse:Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00034.html) Specifies the source of the digital edge pulse trigger. This property is used only when you set the Pulse Mode Enabled property to True and set the Pulse Trigger Type property to Digital Edge .
- [Sweep:Pulse:Trigger:Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00033.html) Specifies the pulse trigger type. This property is used only when you set the Pulse Mode Enabled property to True .
- [Sweep:Segment:Dwell Time (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004f.html) Specifies the dwell time for the selected segment. This property is used only when you set the Sweep Type property to Segment and Segment Dwell Time Enabled property to True . This value is expressed in seconds.
- [Sweep:Segment:Dwell Time Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004e.html) Specifies whether VNA performs measurements using the same dwell time value for all segments or uses different dwell time for each segment. This property is used only when you set the Sweep Type property to Segment .
- [Sweep:Segment:Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0002f.html) Specifies whether to enable the selected segment for the sweep. This property is used only when you set Sweep Type property to Segment
- [Sweep:Segment:Frequency:Number of Frequency Points](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00056.html) Specifies the number of frequency points measured in the selected segment. This property is used only when you set the Sweep Type property to Segment .
- [Sweep:Segment:Frequency:Start Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00054.html) Specifies the lowest frequency of the selected segment at which measurements are performed. This property is used only when you set the Sweep Type property to Segment . This value is expressed in Hz.
- [Sweep:Segment:Frequency:Stop Frequency (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00055.html) Specifies the highest frequency of the selected segment at which measurements are performed. This property is used only when you set the Sweep Type property to Segment . This value is expressed in Hz.
- [Sweep:Segment:IF Bandwidth (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004b.html) Specifies the digital IF filter bandwidth for the selected segment. This property is used only when you set the Sweep Type property to Segment and Segment IF Bandwidth Enabled property to True . This value is expressed in Hz.
- [Sweep:Segment:IF Bandwidth Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004a.html) Specifies whether VNA performs measurements using the same digital IF filter bandwidth for all segments or uses different digital IF filter bandwidth for each segment. This property is used only when you set the Sweep Type property to Segment .
- [Sweep:Segment:Number of Segments](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00001.html) Specifies the number of sweep segments. This property is used only when you set Sweep Type property to Segment
- [Sweep:Segment:Power Level (dBm)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00049.html) Specifies the source power level for the selected segment. This property is used only when you set the Sweep Type property to Segment and Segment Power Level Enabled property to True . This value is expressed in dBm.
- [Sweep:Segment:Power Level Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00048.html) Specifies whether VNA performs measurements using the same source power level for all segments or uses different source power level for each segment. This property is used only when you set the Sweep Type property to Segment .
- [Sweep:Segment:Test Receiver Attenuation (dB)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004d.html) Specifies the test receiver attenuation for the selected segment. This property is used only when you set the Sweep Type property to Segment and Segment Test Receiver Attenuation Enabled property to True . This value is expressed in dB.
- [Sweep:Segment:Test Receiver Attenuation Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004c.html) Specifies whether VNA performs measurements using the same test receiver attenuation for all segments or uses different test receiver attenuation for each segment. This property is used only when you set the Sweep Type property to Segment .
- [Sweep:Sequence](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0002d.html) Specifies the sequence of acquisitions for various frequency points and source ports.
- [Sweep:Test Receiver Attenuation (dB)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0000a.html) Specifies the attenuation that the VNA uses to attenuate the RF signal before it reaches the downconverting mixer on the path towards the Test Receiver. The receiver that measures the scattered waves traveling away from the DUT port and towards the VNA port is referred to as the Test Receiver. This value is expressed in dB.
- [Sweep:Timing:Dwell Time (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00006.html) Specifies the time for which the analyzer waits before acquiring the signal for each measurement point. Use dwell time when measuring devices with substantial electrical lengths, requiring compensation for the delay between frequency changes at the generator and their observation at the analyzer. This value is expressed in seconds.
- [Sweep:Timing:Sweep Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00005.html) Specifies the time for which VNA waits before it starts acquiring data for each sweep. Total delay for acquiring the first point in each sweep is sum of this delay and Dwell Time . This value is expressed in seconds.
- [Sweep:Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd0002e.html) Specifies the sweep type for the measurement.
- [Sweep:X-Axis Values](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00057.html) Returns an array of frequency values when you perform measurements with Sweep Type property set to List or Linear or Segment or an array of time values when you perform measurements with Sweep Type property set to CW Time .
- [Trigger:Delay (s)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00070.html) Specifies the delay between the instance when the analyzer receives a trigger and the instance when it starts acquiring.
- [Trigger:Digital Edge:Edge](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00044.html) Specifies the edge of the digital-signal used to assert a digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Digital Edge:Source](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00043.html) Specifies the terminal name used as the source for asserting a digital edge trigger. This property is used only when you set the Trigger Type property to Digital Edge .
- [Trigger:Mode](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00045.html) Specifies the trigger mode. Trigger Mode decides how many data points are acquired for each asserted trigger.
- [Trigger:Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd00042.html) Specifies the trigger type.
- [Waves:Format](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02006.html) Specifies the format for wave measurement.
- [Waves:Group Delay Aperture:Frequency Span (Hz)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02018.html) Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which Waves Format property is set to Group Delay and Waves Group Delay Aperture Mode property is set to Frequency Span .
- [Waves:Group Delay Aperture:Mode](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02015.html) Specifies the aperture mode to be used for the computation of group delay for all waves for which Waves Format property is set to Group Delay .
- [Waves:Group Delay Aperture:Percentage (%)](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02017.html) Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation, where separation is expressed as a percentage of the total measurement frequency range for all waves for which Waves Format property is set to Group Delay and Waves Group Delay Aperture Mode property is set to Percentage .
- [Waves:Group Delay Aperture:Points](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02016.html) Specifies the group delay aperture in terms of the number of frequency points that separates the two frequency points for all waves for which Waves Format property is set to Group Delay and Waves Group Delay Aperture Mode property is set to Points . You must set the value of this property between 2 and the total number of frequency points in the measurement frequency range.
- [Waves:Magnitude Units](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02007.html) Specifies the magnitude units for all waves for which Waves Format property is set to Magnitude .
- [Waves:Measurement Enabled](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02000.html) Specifies whether to enable the Waves measurement.
- [Waves:Number of Waves](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02002.html) Specifies the number of waves to be measured.
- [Waves:Phase Trace Type](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02008.html) Specifies the phase type for all waves for which Waves Format property is set to Phase . Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.
- [Waves:Receiver](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02003.html) Specifies whether to measure the wave on the reference receiver or the test receiver of the Wave Receiver Port.
- [Waves:Receiver Port](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02004.html) Specifies the receiver port name for wave measurement.
- [Waves:Results:Correction:Level](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02019.html) Returns the level of error correction applied to the specified wave measurement.
- [Waves:Results:Correction:State](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02013.html) Returns the error correction state of the VNA Waves measurement.
- [Waves:Source Port](../../../resource/objmgr/rfmxvna-rc/rfmxvna/attrd02005.html) Specifies the source port name for wave measurement.

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00002.html language=enus -->
## TOPIC 00015: Sweep:Frequency:Frequency List (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00002.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency values for the configured measurements. The frequencies must be in ascending order and must not contain duplicates. This property is used only when you set the Sweep Type property to List. This value is expressed in Hz. You do not need to use a selector string to configure or

### Sweep:Frequency:Frequency List (Hz)

Specifies the frequency values for the configured measurements. The frequencies must be in ascending order and must not contain duplicates. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **List**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is an empty array.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Freq List (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00003.html language=enus -->
## TOPIC 00016: Sweep:Power Level (dBm)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00003.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00003.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level for the VNA source port. This value is expressed in dBm. Use "port::<portname>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure same power level for all VNA ports. The default value is -10 dBm. Remarks The foll

### Sweep:Power Level (dBm)

Specifies the power level for the VNA source port. This value is expressed in dBm.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure same power level for all VNA ports.

The default value is -10 dBm.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Power Level (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00004.html language=enus -->
## TOPIC 00017: Sweep:IF Bandwidth (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00004.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the digital IF filter bandwidth. This value is expressed in Hz. NI PXIe-5633 supports the following IF Bandwidths: 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M. If you set

### Sweep:IF Bandwidth (Hz)

Specifies the digital IF filter bandwidth. This value is expressed in Hz.

NI PXIe-5633 supports the following IF Bandwidths: 1, 2, 3, 5, 7, 10, 20, 30, 50, 70, 100, 200, 300, 500, 700, 1k, 2k, 3k, 5k, 7k, 10k, 20k, 30k, 50k, 70k, 100k, 200k, 300k, 500k, 700k, 1M, 2M, 3M, 5M, 7M, 10M, 15M. If you set IF Bandwidth to an unsupported value, RFmx automatically coerces to the smallest supported IF Bandwidth greater than or equal to the value you set. If you set IF Bandwidth to a value higher than the maximum supported value, RFmx automatically coerces it to maximum supported IF Bandwidth.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 100 kHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Bandwidth (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00014.html language=enus -->
## TOPIC 00018: Correction:Calibration:Calkit:Mechanical:Name

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00014.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the name of the mechanical calkit used for calibration. This property is used only when you set the Calkit Type property to Mechanical. You must set a valid calkit name. Use RFmxVNA Calkit Manager Get Calkit IDs VI to get list of available mechanical calkits. Currently, RFmxVNA only suppor

### Correction:Calibration:Calkit:Mechanical:Name

Specifies the name of the mechanical calkit used for calibration. This property is used only when you set the [Calkit Type](/csh?context=rfmxvna_rfmxvnaprop_attrd00012) property to **Mechanical**.

You must set a valid calkit name. Use [RFmxVNA Calkit Manager Get Calkit IDs](/csh?context=rfmxvna_rfmxvnavi_rfmxvna_calkit_manager_get_calkit_ids) VI to get list of available mechanical calkits.

Note

Use "port::all" as the selector string to specify the same calkit name for all VNA ports. Use "port::<*portname*>" as the selector string to read this property for a specific VNA port.

The default value is an empty string.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Calkit Name |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00028.html language=enus -->
## TOPIC 00019: Correction:Port Extension:Loss:DC Loss Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00028.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00028.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to compensate for the frequency-independent loss as part of the port extension. This property is used only when you set the Port Extension Enabled property to True. Use "port::<portname>" as the selector string to configure or read this property for a specific VNA port. Use "port::

### Correction:Port Extension:Loss:DC Loss Enabled

Specifies whether to compensate for the frequency-independent loss as part of the port extension. This property is used only when you set the [Port Extension Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00026) property to **True**.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure for all VNA ports.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Port Extension DC Loss Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | The measurement disables the compensation of DC Loss of the port extension. |
| --- | --- | --- |
| True | 1 | The measurement compensates for the DC loss based on the value of Port Extension DC Loss (dB) specified by you. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0002d.html language=enus -->
## TOPIC 00020: Sweep:Sequence

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0002d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0002d.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the sequence of acquisitions for various frequency points and source ports. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The defaul

### Sweep:Sequence

Specifies the sequence of acquisitions for various frequency points and source ports.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Standard**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Sweep Sequence |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Standard | 0 | Acquisitions for all frequency points are completed with the first source port before moving to the next source port. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f2, port1), (f3, port1), (f1, port2), (f2, port2), (f3, port2). |
| --- | --- | --- |
| Point | 1 | All acquisitions for a frequency point are completed with all required source ports, before moving to the next frequency point. For example, if there are three frequency points f1, f2 and f3 and two source ports, port1 and port2, then the sweep sequence will be (f1, port1), (f1, port2), (f2, port1), (f2, port2), (f3, port1), (f3, port2). |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00034.html language=enus -->
## TOPIC 00021: Sweep:Pulse:Trigger:Digital Edge:Source

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00034.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00034.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source of the digital edge pulse trigger. This property is used only when you set the Pulse Mode Enabled property to True and set the Pulse Trigger Type property to Digital Edge. You do not need to use a selector string to configure or read this property for the default signal instance

### Sweep:Pulse:Trigger:Digital Edge:Source

Specifies the source of the digital edge pulse trigger. This property is used only when you set the [Pulse Mode Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00031) property to **True** and set the [Pulse Trigger Type](/csh?context=rfmxvna_rfmxvnaprop_attrd00033) property to **Digital Edge**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default of this property is "" (empty string).

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Digital Edge Trigger Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| PFI0 | PFI0 | The trigger is received on PFI 0. |
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
| PXI_STAR | PXI_STAR | The trigger is received on the PXI star trigger line. Note that, RFmxVNA does not yet support this trigger line. |
| PXIe_DStarB | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00035.html language=enus -->
## TOPIC 00022: Sweep:Pulse:Period (s)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00035.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00035.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the time interval after which the pulse repeats. This property is used only when you set the Pulse Mode Enabled property to True. If you set Pulse Trigger Type property to Digital Edge, pulses are generated only when an external pulse digital edge trigger is received by the VNA. This value

### Sweep:Pulse:Period (s)

Specifies the time interval after which the pulse repeats. This property is used only when you set the [Pulse Mode Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00031) property to **True**. If you set [Pulse Trigger Type](/csh?context=rfmxvna_rfmxvnaprop_attrd00033) property to **Digital Edge**, pulses are generated only when an external pulse digital edge trigger is received by the VNA. This value is expressed in seconds.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 ms.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Pulse Period (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00046.html language=enus -->
## TOPIC 00023: Sweep:Auto IF Bandwidth Scaling Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00046.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00046.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether IF Bandwidth is automatically scaled down to account for the increased VNA receiver noise at low frequencies. This property will automatically set to False when Pulse Mode Enabled property is set to True. Consider disabling automatic IF Bandwidth scaling by setting this property to

### Sweep:Auto IF Bandwidth Scaling Enabled

Specifies whether IF Bandwidth is automatically scaled down to account for the increased VNA receiver noise at low frequencies. This property will automatically set to **False** when [Pulse Mode Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00031) property is set to **True**.

Consider disabling automatic IF Bandwidth scaling by setting this property to False if you want faster measurement speed but with higher measurment noise at low frequencies.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto IF Bandwidth Scaling Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |
| --- | --- | --- |
| True | 1 | Enables automatic IF Bandwidth scaling that compensates for the increased VNA receiver noise at low frequencies. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00048.html language=enus -->
## TOPIC 00024: Sweep:Segment:Power Level Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00048.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00048.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether VNA performs measurements using the same source power level for all segments or uses different source power level for each segment. This property is used only when you set the Sweep Type property to Segment. You do not need to use a selector string to configure or read this propert

### Sweep:Segment:Power Level Enabled

Specifies whether VNA performs measurements using the same source power level for all segments or uses different source power level for each segment. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Segment**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segment Power Level Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | All segments are measured with the source power level that you specify using Power Level property. |
| --- | --- | --- |
| True | 1 | The selected segment is measured with the source power level that you specify using Segment Power Level property. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00049.html language=enus -->
## TOPIC 00025: Sweep:Segment:Power Level (dBm)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00049.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00049.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source power level for the selected segment. This property is used only when you set the Sweep Type property to Segment and Segment Power Level Enabled property to True. This value is expressed in dBm. Use "port::<portname>" as the selector string to configure or read this property for

### Sweep:Segment:Power Level (dBm)

Specifies the source power level for the selected segment. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Segment** and [Segment Power Level Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00048) property to **True**. This value is expressed in dBm.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port for segment0. Use "port::*all*" to configure this property for all VNA ports for segment0.

Use "segment::<*segmentnumber*>/port::<*portname*>" as the selector string to configure or read this property for a specific segment and for a specific VNA port. Use "segment::*all*/port::*all*" as the selector string to configure this property for all segments and for all VNA ports.

The default value is -10 dBm.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segment Power Level (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004c.html language=enus -->
## TOPIC 00026: Sweep:Segment:Test Receiver Attenuation Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0004c.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether VNA performs measurements using the same test receiver attenuation for all segments or uses different test receiver attenuation for each segment. This property is used only when you set the Sweep Type property to Segment. You do not need to use a selector string to configure or rea

### Sweep:Segment:Test Receiver Attenuation Enabled

Specifies whether VNA performs measurements using the same test receiver attenuation for all segments or uses different test receiver attenuation for each segment. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Segment**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segment Test Receiver Attn Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | All segments are measured with the test receiver attenuation that you specify using Test Receiver Attenuation property. |
| --- | --- | --- |
| True | 1 | The selected segment is measured with the test receiver attenuation that you specify using Segment Test Receiver Attenuation property. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00052.html language=enus -->
## TOPIC 00027: Sweep:Frequency:Stop Frequency (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00052.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00052.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the highest frequency at which measurements are performed. This property is used only when you set the Sweep Type property to Linear. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Sel

### Sweep:Frequency:Stop Frequency (Hz)

Specifies the highest frequency at which measurements are performed. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Linear**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 2 GHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Stop Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00053.html language=enus -->
## TOPIC 00028: Sweep:Number of Points

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00053.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00053.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of points at which measurements are performed. This property is used only when you set the Sweep Type property to Linear or CW Time. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic f

### Sweep:Number of Points

Specifies the number of points at which measurements are performed. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Linear** or **CW Time**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 201.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Number of Points |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00054.html language=enus -->
## TOPIC 00029: Sweep:Segment:Frequency:Start Frequency (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00054.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00054.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the lowest frequency of the selected segment at which measurements are performed. This property is used only when you set the Sweep Type property to Segment. This value is expressed in Hz. Use "segment::<segmentnumber>" as the selector string to configure or read this property for a specif

### Sweep:Segment:Frequency:Start Frequency (Hz)

Specifies the lowest frequency of the selected segment at which measurements are performed. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Segment**. This value is expressed in Hz.

Use "segment::<*segmentnumber*>" as the selector string to configure or read this property for a specific segment.

The default value is 1 GHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segment Start Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00055.html language=enus -->
## TOPIC 00030: Sweep:Segment:Frequency:Stop Frequency (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00055.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00055.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the highest frequency of the selected segment at which measurements are performed. This property is used only when you set the Sweep Type property to Segment. This value is expressed in Hz. Use "segment::<segmentnumber>" as the selector string to configure or read this property for a speci

### Sweep:Segment:Frequency:Stop Frequency (Hz)

Specifies the highest frequency of the selected segment at which measurements are performed. This property is used only when you set the [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property to **Segment**. This value is expressed in Hz.

Use "segment::<*segmentnumber*>" as the selector string to configure or read this property for a specific segment.

The default value is 2 GHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Segment Stop Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00057.html language=enus -->
## TOPIC 00031: Sweep:X-Axis Values

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00057.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00057.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of frequency values when you perform measurements with Sweep Type property set to List or Linear or Segment or an array of time values when you perform measurements with Sweep Type property set to CW Time. You do not need to use a selector string to configure or read this property f

### Sweep:X-Axis Values

Returns an array of frequency values when you perform measurements with [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property set to **List** or **Linear** or **Segment** or an array of time values when you perform measurements with [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property set to **CW Time**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | X-Axis Values |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00060.html language=enus -->
## TOPIC 00032: Correction:Port Extension:Distance

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00060.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00060.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the port extension delay in physical length. This value is expressed in meters by default. The unit can be chosen by setting the Port Extension Distance Unit property. This property is used only when you set the Port Extension Enabled property to True and Port Extension Delay Domain proper

### Correction:Port Extension:Distance

Specifies the port extension delay in physical length. This value is expressed in meters by default. The unit can be chosen by setting the [Port Extension Distance Unit](/csh?context=rfmxvna_rfmxvnaprop_attrd00061) property. This property is used only when you set the [Port Extension Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00026) property to **True** and [Port Extension Delay Domain](/csh?context=rfmxvna_rfmxvnaprop_attrd0005f) property to **Distance**.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure the same distance value for all VNA ports.

The default value is 0 m.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Port Extension Distance |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00061.html language=enus -->
## TOPIC 00033: Correction:Port Extension:Distance Unit

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00061.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00061.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the unit of the port extension delay in physical length. This property is used only when you set the Port Extension Enabled property to True and Port Extension Delay Domain property to Distance. Use "port::<portname>" as the selector string to configure or read this property for a specific

### Correction:Port Extension:Distance Unit

Specifies the unit of the port extension delay in physical length. This property is used only when you set the [Port Extension Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00026) property to **True** and [Port Extension Delay Domain](/csh?context=rfmxvna_rfmxvnaprop_attrd0005f) property to **Distance**.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure the same distance unit for all VNA ports.

The default value is **Meters**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Port Extension Distance Unit |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Meters | 0 | The port extension physical length is expressed in meters. |
| --- | --- | --- |
| Feet | 1 | The port extension physical length is expressed in feet. |
| Inches | 2 | The port extension physical length is expressed in inches. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00062.html language=enus -->
## TOPIC 00034: Correction:Port Extension:Velocity Factor

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00062.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00062.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the speed of light in the port extension medium relative to speed of light in vacuum. Velocity Factor of 1 represents speed of light in vacuum. This property is used in conjuction with Port Extension Distance property to compute electrical delay. This value is unitless. This property is us

### Correction:Port Extension:Velocity Factor

Specifies the speed of light in the port extension medium relative to speed of light in vacuum. Velocity Factor of 1 represents speed of light in vacuum. This property is used in conjuction with [Port Extension Distance](/csh?context=rfmxvna_rfmxvnaprop_attrd00060) property to compute electrical delay. This value is unitless. This property is used only when you set the [Port Extension Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd00026) property to **True** and [Port Extension Delay Domain](/csh?context=rfmxvna_rfmxvnaprop_attrd0005f) property to **Distance**.

Use "port::<*portname*>" as the selector string to configure or read this property for a specific VNA port. Use "port::all" to configure the same velocity factor for all VNA ports.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Port Extension Velocity Factor |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd00079.html language=enus -->
## TOPIC 00035: Correction:Port Subset:Response Ports

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd00079.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd00079.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is a

### Correction:Port Subset:Response Ports

Specifies the subset of ports, that are selected for one-path two-port error correction. Use comma-separated list of ports to specify multiple ports. The configured measurement is one-path two-port corrected if both measurement ports are specified using this property. Alternatively, measurement is also one-path two-port corrected if one of the measurement port is specified using this property and another is specified using [Correction Port Subset Full Ports](/csh?context=rfmxvna_rfmxvnaprop_attrd0000f). Measurements involving the ports outside the [Correction Port Subset Response Ports](/csh?context=rfmxvna_rfmxvnaprop_attrd00079) and [Correction Port Subset Full Ports](/csh?context=rfmxvna_rfmxvnaprop_attrd0000f) return error.

This property is used only when you set the [Correction Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd0000b) property to **True** and [Correction Port Subset Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd0000e) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is an empty string.

For example, when performing S21 error-corrected measurement for a 2-port DUT using a 2-port VNA and a 2-port calset, VNA generally acquires data by setting the source to port1 first and then to port2. To perform S21 one-path two-port error corrected measurement and to achieve faster measurement speed, set this property to **port1, port2**. VNA then acquires data using source port1 and skips acquiring data with source port2.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Correction Port Subset Response Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007a.html language=enus -->
## TOPIC 00036: Correction:Port Extension:Auto:Loss Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007a.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension. Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values. You

### Correction:Port Extension:Auto:Loss Enabled

Specifies whether to determine both the frequency-dependent losses (Loss1 and Loss2) and the frequency-independent loss (DC Loss) during automatic port extension.
 Typically, the frequencies located at one-quarter and three-quarters of the configured sweep range are used as the f1 and f2 values.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Port Extension Loss Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disable the loss estimation in automatic port extension. |
| --- | --- | --- |
| True | 1 | Enable the loss estimation in automatic port extension. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007b.html language=enus -->
## TOPIC 00037: Correction:Port Extension:Auto:Regularization Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007b.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters. This property is used only when you set t

### Correction:Port Extension:Auto:Regularization Enabled

Specifies whether the compensated trace should be regularized to ensure it remains at or below 0 dB. Fixture mismatch can sometimes cause S11 or S22 measurements to exceed 0 dB, which may introduce numerical instability when using the resulting S-parameters.
 This property is used only when you set the [Auto Port Extension Loss Enabled](/csh?context=rfmxvna_rfmxvnaprop_attrd0007a) property to **True**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **True**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Port Extension Regularization Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| False | 0 | Disable the regularization of the compensated trace in automatic port extension. |
| --- | --- | --- |
| True | 1 | Enable the regularization of the compensated trace in automatic port extension. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007c.html language=enus -->
## TOPIC 00038: Correction:Port Extension:Auto:Frequency Mode

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007c.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency mode over which the delay and loss (optional) values are determined. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The

### Correction:Port Extension:Auto:Frequency Mode

Specifies the frequency mode over which the delay and loss (optional) values are determined.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Sweep**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Port Extension Frequency Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Sweep | 0 | Sets the frequency mode to Sweep. Configured sweep range is used to determine the phase and loss values. |
| --- | --- | --- |
| User | 1 | Sets the frequency mode to User Span. User-defined span is used to determine the phase and loss values. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007d.html language=enus -->
## TOPIC 00039: Correction:Port Extension:Auto:Start Frequency (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007d.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the start frequency of the user span. This property is used only when you set the Auto Port Extension Frequency Mode property to User Span. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to t

### Correction:Port Extension:Auto:Start Frequency (Hz)

Specifies the start frequency of the user span. This property is used only when you set the [Auto Port Extension Frequency Mode](/csh?context=rfmxvna_rfmxvnaprop_attrd0007c) property to **User Span**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1 GHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Port Extension Start Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007e.html language=enus -->
## TOPIC 00040: Correction:Port Extension:Auto:Stop Frequency (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0007e.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the stop frequency of the user span. This property is used only when you set the Auto Port Extension Frequency Mode property to User Span. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to th

### Correction:Port Extension:Auto:Stop Frequency (Hz)

Specifies the stop frequency of the user span. This property is used only when you set the [Auto Port Extension Frequency Mode](/csh?context=rfmxvna_rfmxvnaprop_attrd0007c) property to **User Span**. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 2 GHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Auto Port Extension Stop Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd01004.html language=enus -->
## TOPIC 00041: SParams:Source Port

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd01004.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd01004.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_<receiver port name>_<source port name>". For example, to measure S21, set this property to "port1". Use "sparam<n>" as the selector string to configure or read this property. The default value is "port1". Remarks The fo

### SParams:Source Port

Specifies the source port name of the S-Parameter. S-Parameter is denoted by "S_<*receiver port name*>_<*source port name*>".

For example, to measure S21, set this property to "port1".

Use "sparam<*n*>" as the selector string to configure or read this property.

The default value is "port1".

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SParams Source Port |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd0100d.html language=enus -->
## TOPIC 00042: IQ:Acquisition Time (s)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd0100d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd0100d.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The following table lists the characteristics of this property. Short Name IQ Acquisitio

### IQ:Acquisition Time (s)

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IQ Acquisition Time (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd01014.html language=enus -->
## TOPIC 00043: SParams:SnP Export:User Comment

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd01014.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd01014.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies a string that is incorporated into saved SnP file. You can specify any arbitrary string to add any meta information that you may want to store along with the measured S-Parameters data in SnP file. RFmx automatically adds a special token(!) at the start of this string such that any standar

### SParams:SnP Export:User Comment

Specifies a string that is incorporated into saved SnP file. You can specify any arbitrary string to add any meta information that you may want to store along with the measured S-Parameters data in SnP file. RFmx automatically adds a special token(!) at the start of this string such that any standard SnP file parsers would ignore this line. Additionally, multiline comments are allowed and each line is appended with the next line escape character.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SParams SnP User Comment |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd01015.html language=enus -->
## TOPIC 00044: SParams:SnP Export:Ports

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd01015.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd01015.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the ports for which the measured S-parameters are saved to file. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. Remarks The following

### SParams:SnP Export:Ports

Specifies the ports for which the measured S-parameters are saved to file.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SParams SnP Ports |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd01020.html language=enus -->
## TOPIC 00045: SParams:Results:Correction:Level

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd01020.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd01020.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the level of error correction applied to the specified S-Parameter measurement. Use "sparam<n>" as the selector string to read this property. Uncorrected Correction is not applied to the configured S-Parameter. N-Port Full N-Port correction is applied to the configured S-Parameter, where N r

### SParams:Results:Correction:Level

Returns the level of error correction applied to the specified S-Parameter measurement.

Use "sparam<*n*>" as the selector string to read this property.

| Uncorrected | Correction is not applied to the configured S-Parameter. |
| --- | --- |
| N-Port | Full N-Port correction is applied to the configured S-Parameter, where N refers to the number of VNA ports involved in the correction. |
| 1-Path | One Path Two Port correction is applied to the configured transmission measurement. Refer to Correction Port Subset Response Ports property for more information about one-path two-port correction. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SParams Results Correction Level |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02000.html language=enus -->
## TOPIC 00046: Waves:Measurement Enabled

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02000.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02000.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the Waves measurement. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals. The default value is False. Remarks The follo

### Waves:Measurement Enabled

Specifies whether to enable the Waves measurement.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **False**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02002.html language=enus -->
## TOPIC 00047: Waves:Number of Waves

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02002.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02002.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the number of waves to be measured. If you increase this property value from N to N+K, then existing N Waves are not affected but K new Waves are added. If you reduce number of Waves from N to N-K, then last K Waves are deleted without affecting the remaining N-K Waves. You do not need to

### Waves:Number of Waves

Specifies the number of waves to be measured.

If you increase this property value from N to N+K, then existing N Waves are not affected but K new Waves are added. If you reduce number of Waves from N to N-K, then last K Waves are deleted without affecting the remaining N-K Waves.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 1.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Num Waves |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02005.html language=enus -->
## TOPIC 00048: Waves:Source Port

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02005.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02005.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source port name for wave measurement. Incident and scattered waves are denoted by "a_<receiver port name>_<source port name>" and "b_<receiver port name>_<source port name>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver res

### Waves:Source Port

Specifies the source port name for wave measurement.

Incident and scattered waves are denoted by "a_<*receiver port name*>_<*source port name*>" and "b_<*receiver port name*>_<*source port name*>" respectively. On a receiver port, the a and b waves are measured using Reference receiver and Test receiver respectively.

For example, to measure "b21", set [Waves Receiver](/csh?context=rfmxvna_rfmxvnaprop_attrd02003) to **Test (0)**, [Waves Receiver Port](/csh?context=rfmxvna_rfmxvnaprop_attrd02004) to "port2" and set this property to "port1".

Use "wave<*n*>" as the selector string to configure or read this property.

The default value is "port1".

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Source Port |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02006.html language=enus -->
## TOPIC 00049: Waves:Format

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02006.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02006.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the format for wave measurement. Use "wave<n>" as the selector string to configure or read this property. Use RFmxVNA Waves Fetch Y Data to fetch the waves. The default value is Magnitude. Remarks The following table lists the characteristics of this property. Short Name Waves Format Data

### Waves:Format

Specifies the format for wave measurement.

Use "wave<*n*>" as the selector string to configure or read this property.

Use RFmxVNA Waves Fetch Y Data to fetch the waves.

The default value is **Magnitude**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Format |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Magnitude | 0 | Sets the format for the selected wave to Magnitude. You can specify Wave Magnitude Units. |
| --- | --- | --- |
| Phase | 1 | Sets the format of the selected wave to Phase. Phase values are expressed in degrees. Phase can be represented in various, mathematically equivalent ways such as phase wrapped between the range [-180, 180) degrees, or phase can be represented in an unwrapped manner. You can specify the phase representation by configuring Wave Phase Trace Type. |
| Complex | 2 | Sets the format for the selected wave as complex numbers in cartesian co-ordinates. |
| SWR | 3 | Sets the format for the selected wave to Standing Wave Ratio (SWR). SWR is a unitless quantity. |
| Smith Impedance | 4 | Sets the format for the selected wave to Smith Impedance. The measured values of the wave are transformed into impedence values. Impedence values are expressed in ohms. You can use these values to plot on a Smith Chart. |
| Smith Admittance | 5 | Sets the format for the selected wave to Smith Admittance. The measured values of the wave are transformed into admittance values. Admittance values are expressed in siemens. You can use these values to plot on an Inverted Smith Chart. |
| Polar | 6 | Sets the format for the selected wave as complex numbers in polar co-ordinates, where the radial axis (i.e., magnitude of the complex numbers) is always in linear scale and angular axis (phase) is represented in degrees and always wrapped between ±180 deg. |
| Group Delay | 7 | Sets the format of the selected wave to Group Delay. Group delay represents the time it takes for the signal to pass through a device under test. The delay is expressed in seconds. Group delay vs. frequency is derived from phase vs. frequency response. At a given frequency point, group delay is computed by selecting two nearby frequency points and taking the ratio of the phase difference to the frequency separation between them. The frequency separation between the two selected points is called the group delay aperture. You can control the aperture by first configuring Waves Group Delay Aperture Mode and once the mode is selected, you can set the aperture by configuring Waves Group Delay Aperture Points, Waves Group Delay Aperture Percentage or Waves Group Delay Aperture Frequency Span. For example, if the number of aperture points is equal to 3, then group delay at a nth frequency point is computed by selecting the (n-1)th frequency point and (n+1)th frequency point. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02007.html language=enus -->
## TOPIC 00050: Waves:Magnitude Units

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02007.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02007.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the magnitude units for all waves for which Waves Format property is set to Magnitude. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector Strings topic for information about the string syntax for named signals.

### Waves:Magnitude Units

Specifies the magnitude units for all waves for which [Waves Format](/csh?context=rfmxvna_rfmxvnaprop_attrd02006) property is set to **Magnitude**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **dBm**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Magnitude Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| dBm | 0 | Sets wave magnitude units to dBm. |
| --- | --- | --- |
| dBmV | 1 | Sets wave magnitude units to dBmV. |
| dBuV | 2 | Sets wave magnitude units to dBuV. |
| dBmA | 3 | Sets wave magnitude units to dBmA. |
| W | 4 | Sets wave magnitude units to watts. |
| V | 5 | Sets wave magnitude units to volts. |
| A | 6 | Sets wave magnitude units to ampere. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02008.html language=enus -->
## TOPIC 00051: Waves:Phase Trace Type

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02008.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02008.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the phase type for all waves for which Waves Format property is set to Phase. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner. You do not need to use a selector stri

### Waves:Phase Trace Type

Specifies the phase type for all waves for which [Waves Format](/csh?context=rfmxvna_rfmxvnaprop_attrd02006) property is set to **Phase**. Phase can be represented in two mathematically equivalent ways viz. phase wrapped between the range [-180, 180) degrees, and phase can be represented in an unwrapped manner.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is **Wrapped**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Phase Trace Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Wrapped | 0 | The reported wave phase is wrapped between -180 degress to +180 degrees. |
| --- | --- | --- |
| Unwrapped | 1 | The reported wave phase is unwrapped. |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02018.html language=enus -->
## TOPIC 00052: Waves:Group Delay Aperture:Frequency Span (Hz)

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02018.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02018.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which Waves Format property is set to Group Delay and Waves Group Delay Aperture Mode property is set to Frequency Span. You do not need to

### Waves:Group Delay Aperture:Frequency Span (Hz)

Specifies the group delay aperture in terms of the frequency separation between the two frequency points selected for group delay computation for all waves for which [Waves Format](/csh?context=rfmxvna_rfmxvnaprop_attrd02006) property is set to **Group Delay** and [Waves Group Delay Aperture Mode](/csh?context=rfmxvna_rfmxvnaprop_attrd02015) property is set to **Frequency Span**.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is 50 MHz.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Group Delay Freq Span (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=resource/objmgr/rfmxvna-rc/rfmxvna/attrd02019.html language=enus -->
## TOPIC 00053: Waves:Results:Correction:Level

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `resource/objmgr/rfmxvna-rc/rfmxvna/attrd02019.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxvna-rc/rfmxvna/attrd02019.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the level of error correction applied to the specified wave measurement. Use "wave<n>" as the selector string to read this property. Uncorrected Correction is not applied to the configured wave. Wave 1-Port correction is applied to the configured Wave. Remarks The following table lists the c

### Waves:Results:Correction:Level

Returns the level of error correction applied to the specified wave measurement.

Use "wave<*n*>" as the selector string to read this property.

| Uncorrected | Correction is not applied to the configured wave. |
| --- | --- |
| Wave | 1-Port correction is applied to the configured Wave. |

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Waves Results Correction Level |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxVNA Properties

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-abort-measurements-vi.html language=enus -->
## TOPIC 00054: RFmxVNA Abort Measurements VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-abort-measurements-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-abort-measurements-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxVNA Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI

### RFmxVNA Abort Measurements VI

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxVNA Initiate VI](/csh?topicname=rfmxvna-initiate-vi.html) or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxvna-abort-measurements-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Advanced

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-measure-vi.html language=enus -->
## TOPIC 00055: RFmxVNA Auto Port Extension Measure VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-measure-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-measure-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Automatically determine the fixture delay and loss (optional) values by measuring the standard at the configured port. The calculated delay and loss values are used to set the Port Extension Delay (s), Port Extension DC Loss (dB), Port Extension Loss1 (dB) and Port Extension Loss2 (dB) properties. C

### RFmxVNA Auto Port Extension Measure VI

Automatically determine the fixture delay and loss (optional) values by measuring the standard at the configured port. The calculated delay and loss values are used to set the [Port Extension Delay (s)](/csh?context=rfmxvna_rfmxvnaprop_attrd00027), [Port Extension DC Loss (dB)](/csh?context=rfmxvna_rfmxvnaprop_attrd00029), [Port Extension Loss1 (dB)](/csh?context=rfmxvna_rfmxvnaprop_attrd0005b) and [Port Extension Loss2 (dB)](/csh?context=rfmxvna_rfmxvnaprop_attrd0005e) properties. Call this VI after calibrating the VNA port, where port extension is required, to obtain more accurate delay and loss estimates.

An ideal OPEN and SHORT standard, with zero loss and delay, is assumed. Therefore, the accuracy depends on the quality of the standard.

To measure either OPEN or SHORT, call [RFmxVNA Auto Port Extension Reset VI](rfmxvna-auto-port-extension-reset-vi.html) before measuring the standard.

When both OPEN and SHORT standards are measured, the average of the calculated delay and loss values are entered.

Note

RFmxVNA Initiate VI

[IMAGE alt='icon' src='rfmxvna-auto-port-extension-measure-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Standard — Standard specifies the standard to be measured. Open (0) Open standard is measured. Short (1) Short standard is measured. Port — Port specifies the calibrated port at which the Open or Short standard is connected. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| Open (0) | Open standard is measured. |
| Short (1) | Short standard is measured. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-reset-vi.html language=enus -->
## TOPIC 00056: RFmxVNA Auto Port Extension Reset VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-reset-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-auto-port-extension-reset-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the measured standard data used for automatic port extension. Before measuring an OPEN or SHORT standard, you must reset any previously measured standard data. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not

### RFmxVNA Auto Port Extension Reset VI

Resets the measured standard data used for automatic port extension.

Note

[IMAGE alt='icon' src='rfmxvna-auto-port-extension-reset-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calkit-string-vi.html language=enus -->
## TOPIC 00057: RFmxVNA Build Calkit String VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calkit-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calkit-string-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string specifying the Calkit. icon Inputs/Outputs cstr.png Calkit ID Calkit ID specifies the ID for the Calkit in Calkit Manager. istr.png Calkit Selector String Out Calkit Selector String Out returns the selector string created by this VI. The selector string comprises of the Cal

### RFmxVNA Build Calkit String VI

Creates a selector string specifying the Calkit.

[IMAGE alt='icon' src='rfmxvna-build-calkit-string-vi.png']

#### Inputs/Outputs

| Calkit ID — Calkit ID specifies the ID for the Calkit in Calkit Manager. Calkit Selector String Out — Calkit Selector String Out returns the selector string created by this VI. The selector string comprises of the Calkit ID. Example: "ckit::MyCkitID" |
| --- |

Parent topic:

Calkit Manager

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calstep-string-vi.html language=enus -->
## TOPIC 00058: RFmxVNA Build CalStep String VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calstep-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-calstep-string-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the calibration step string to use as the selector string with the RFmxVNA Calibration Acquire VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal

### RFmxVNA Build CalStep String VI

Creates the calibration step string to use as the selector string with the [RFmxVNA Calibration Acquire](/csh?topicname=rfmxvna-calibration-acquire-vi.html) VI.

[IMAGE alt='icon' src='rfmxvna-build-calstep-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. CalStep Number — CalStep Number specifies the calibration step number for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Calset

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-segment-string-vi.html language=enus -->
## TOPIC 00059: RFmxVNA Build Segment String VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-segment-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-segment-string-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a selector string specifying the segment number for use with configuration or fetch properties and VIs. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance i

### RFmxVNA Build Segment String VI

Creates a selector string specifying the segment number for use with configuration or fetch properties and VIs.

[IMAGE alt='icon' src='rfmxvna-build-segment-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Segment Number — Segment Number specifies the segment for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-wave-string-vi.html language=enus -->
## TOPIC 00060: RFmxVNA Build Wave String VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-wave-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-build-wave-string-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates the selector string to use with Wave configuration or fetch properties and VIs. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default valu

### RFmxVNA Build Wave String VI

Creates the selector string to use with Wave configuration or fetch properties and VIs.

[IMAGE alt='icon' src='rfmxvna-build-wave-string-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Wave Number — Wave Number specifies the wave index for building the selector string. Selector String Out — Selector String Out returns the selector string created by this VI. |
| --- |

Parent topic:

Waves

Parent topic:

Build String

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-abort-vi.html language=enus -->
## TOPIC 00061: RFmxVNA Calibration Abort VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-abort-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-abort-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stops the calibration, which was previously initiated by RFmxVNA Calibration Initiate VI, for the signal instance that you specify in the Selector String parameter. Calling this VI is optional, unless you want to stop a calibration before it is complete. This VI executes even if there is an incoming

### RFmxVNA Calibration Abort VI

Stops the calibration, which was previously initiated by [RFmxVNA Calibration Initiate VI](/csh?topicname=rfmxvna-calibration-initiate-vi.html), for the signal instance that you specify in the **Selector String** parameter. Calling this VI is optional, unless you want to stop a calibration before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='icon' src='rfmxvna-calibration-abort-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-acquire-vi.html language=enus -->
## TOPIC 00062: RFmxVNA Calibration Acquire VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-acquire-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-acquire-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Measures one or more calibration standards for the specified calibration step. You can call this VI only after required calibration steps are determined by RFmx when you call RFmxVNA Calibration Initiate VI. One successful call to RFmxVNA Calibration Initiate VI is sufficient for all subsequent call

### RFmxVNA Calibration Acquire VI

Measures one or more calibration standards for the specified calibration step.

You can call this VI only after required calibration steps are determined by RFmx when you call [RFmxVNA Calibration Initiate VI](rfmxvna-calibration-initiate-vi.html). One successful call to [RFmxVNA Calibration Initiate VI](rfmxvna-calibration-initiate-vi.html) is sufficient for all subsequent calls to this VI.

When [Calkit Type](/csh?context=rfmxvna_rfmxvnaprop_attrd00012) is **Electronic**, RFmx uses all relevant 1-port and 2-port calibration standards in the selected electronic calibration module. A single call to this VI measures all such cal standards in the electronic calibration module. For example, if you use NI CAL-5501 electronic calkit to calibrate NI PXIe-5633 by using SOLT calibration method, you only need to perform 1 manual connection to connect the 2 cal module ports to 2 VNA ports. After setting up the required connection, a single call to this VI measures all relevant cal standards automatically.

When [Calkit Type](/csh?context=rfmxvna_rfmxvnaprop_attrd00012) is **Mechanical**, RFmx can measure for only one cal standard for each cal step. Specify the active cal step in the Selector String. Use [RFmxVNA Build CalStep String](rfmxvna-build-calstep-string-vi.html) VI to build cal step string. For example, if you calibrate the NI PXIe-5633 using a mechanical calkit containing a Short, Open, Load and Thru discrete cal standards, then you must perform 7 distinct manual connections, call this VI once per cal step, which in-turn instructs you to connect an appropriate 1 or 2-port cal standard to the VNA port(s).

Note

RFmxVNA Calibration Save

[IMAGE alt='icon' src='rfmxvna-calibration-acquire-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Valid selector string format is [signal::<signal name>[/calstep<n>]]. Example: "signal::mysignal" "signal::mysig/calstep0" "signal::mysig/calstep3" When you set the Selector String to "" (empty string), calling this VI will acquire calibration standard measurements for calstep0 for the default signal. When you set the Selector String to "signal::mysignal", calling this VI will acquire calibration standard measurements for calstep0 for the signal "signal::mysignal". When you set the Selector String to "signal::mysig/calstep<n>", calling this VI will acquire calibration standard measurements for calstep<n> for the signal "signal::mysig". You can use the RFmxVNA Build S-Parameter String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Timeout (s) — Timeout (s) specifies the timeout, in seconds, for acquiring the calibration data. Set this value to an appropriate time, longer than expected for completing acqusition(s) for the speficied calibration step. A value of -1 specifies that the VI waits until the acquisition is complete. The default value is 10 seconds. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-initiate-vi.html language=enus -->
## TOPIC 00063: RFmxVNA Calibration Initiate VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-initiate-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-initiate-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Determines the set of calibration standard measurements required for performing calibration with the sweep and calibration settings that you configure. Call this VI after configuring all the appropriate sweep and calibration settings such as Frequency Settings, Power Level and Test Receiver attenuat

### RFmxVNA Calibration Initiate VI

Determines the set of calibration standard measurements required for performing calibration with the sweep and calibration settings that you configure. Call this VI after configuring all the appropriate sweep and calibration settings such as Frequency Settings, Power Level and Test Receiver attenuation settings, IF Bandwidth, Calkit and Cal Method related settings etc.

After you call this VI, you can query number of distinct physical connection steps using [Cal Step Count](/csh?context=rfmxvna_rfmxvnaprop_attrd00019). To understand the physical connection required in a given cal step, query [Cal Step Description](/csh?context=rfmxvna_rfmxvnaprop_attrd0001a) property. You can refer to following sequence of operations to better understand the usage of this VI in a typical calibration routine.

[START] -> ... -> [Select Measurement] -> [Configure Sweep Settings] -> [Configure Calibration Settings] -> [Call RFmxVNA Auto Detect vCal Orientation VI] -> [Call RFmxVNA Calibration Initiate VI] -> [Query [Cal Step Count](/csh?context=rfmxvna_rfmxvnaprop_attrd00019)] -> [Query and make connection as per [Cal Step Description](/csh?context=rfmxvna_rfmxvnaprop_attrd0001a) for Step<*m*>] -> [Call [RFmxVNA Calibration Acquire](rfmxvna-calibration-acquire-vi.html) VI for Step<*m*>] -> [Query and make connection as per [Cal Step Description](/csh?context=rfmxvna_rfmxvnaprop_attrd0001a) for Step<*n*>] -> [Call [RFmxVNA Calibration Acquire](rfmxvna-calibration-acquire-vi.html) VI for Step<*n*>] -> [Call [RFmxVNA Calibration Save](rfmxvna-calibration-save-vi.html) VI] -> [Call [RFmxVNA Calset Save to File](rfmxvna-calset-save-to-file-vi.html) VI] -> ...-> [END].

Note

- You must select SParams or Wave measurement before calling this VI.
- After calling this VI, if you change any sweep and calibration setting, you must call this VI again to commit the change(s) to said sweep and calibration setting(s).

[IMAGE alt='icon' src='rfmxvna-calibration-initiate-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-save-vi.html language=enus -->
## TOPIC 00064: RFmxVNA Calibration Save VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-save-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calibration-save-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Computes error-correction terms and saves the calset in memory. Call this VI after all calibration standards have been measured using RFmxVNA Calibration Acquire VI. If you do not specify Calset Name input parameter, the calset is saved as default calset for the specified signal and is not available

### RFmxVNA Calibration Save VI

Computes error-correction terms and saves the calset in memory. Call this VI after all calibration standards have been measured using [RFmxVNA Calibration Acquire](/csh?topicname=rfmxvna-calibration-acquire-vi.html) VI.

If you do not specify Calset Name input parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal.

Note

RFmxVNA Calibration Initiate

[IMAGE alt='icon' src='rfmxvna-calibration-save-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Calset Name — Calset Name specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-add-calibration-element-vi.html language=enus -->
## TOPIC 00065: RFmxVNA Calkit Manager Calkit Add Calibration Element VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-add-calibration-element-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-add-calibration-element-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the C

### RFmxVNA Calkit Manager Calkit Add Calibration Element VI

Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-add-calibration-element-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Calibration Element ID — Calibration Element ID specifies the ID of the Calibration Element within the Calkit. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calkit

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-delay-model-get-delay-vi.html language=enus -->
## TOPIC 00066: RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-delay-model-get-delay-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-delay-model-get-delay-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Delay of a Calibration Element defined by the Delay Model. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalel

### RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay VI

Returns the Delay of a Calibration Element defined by the Delay Model.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-delay-model-get-delay-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Delay (s) — Delay (s) returns the Delay of a Calibration Element defined by the Delay Model. error out — error out returns error information. |
| --- |

Parent topic:

Delay Model

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c2-vi.html language=enus -->
## TOPIC 00067: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2 VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c2-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c2-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and

### RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2 VI

Returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-get-c2-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. C2 (F or H) — C2 (F or H) returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. error out — error out returns error information. |
| --- |

Parent topic:

Reflect Model

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-s-param-availability-vi.html language=enus -->
## TOPIC 00068: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-s-param-availability-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-s-param-availability-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the S-Parameter availability. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Bui

### RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability VI

Specifies the S-Parameter availability.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-reflect-model-set-s-param-availability-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. S-Parameter Availability — S-Parameter Availability specifies the S-Parameter availability. Estimate (0) S-Parameters treated as roughly known. Known (1) S-Parameters treated as exactly known. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| Estimate (0) | S-Parameters treated as roughly known. |
| Known (1) | S-Parameters treated as exactly known. |

Parent topic:

Reflect Model

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s-param-availability-vi.html language=enus -->
## TOPIC 00069: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s-param-availability-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s-param-availability-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-Parameter availability. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build

### RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability VI

Returns the S-Parameter availability.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-get-s-param-availability-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. S-Parameter Availability — S-Parameter Availability returns the S-Parameter availability. Estimate (0) S-Parameters treated as roughly known. Known (1) S-Parameters treated as exactly known. error out — error out returns error information. |  |
| --- | --- |
| Estimate (0) | S-Parameters treated as roughly known. |
| Known (1) | S-Parameters treated as exactly known. |

Parent topic:

S-Parameter based

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-frequency-vi.html language=enus -->
## TOPIC 00070: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-frequency-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the frequency array for the S-Parameter definition of the Calibration Element. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitI

### RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency VI

Defines the frequency array for the S-Parameter definition of the Calibration Element.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Frequency (Hz) — Frequency (Hz) specifies the frequency array for the S-Parameter definition of the Calibration Element. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

S-Parameter based

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-from-file-vi.html language=enus -->
## TOPIC 00071: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-from-file-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element

### RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File VI

Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-from-file-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. File Name — File Name specifies the touchstone file name. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

S-Parameter based

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s12-vi.html language=enus -->
## TOPIC 00072: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12 VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s12-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s12-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the S12 S-Parameter for the calibration element. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use t

### RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12 VI

Sets the S12 S-Parameter for the calibration element.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-s-parameter-set-s12-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. S12 — S12 specifies the S12 S-Parameter for the calibration element. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

S-Parameter based

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-maximum-frequency-vi.html language=enus -->
## TOPIC 00073: RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-maximum-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-maximum-frequency-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Maximum Frequency of the Calibration Element. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use

### RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency VI

Sets the Maximum Frequency of the Calibration Element.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-set-maximum-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Maximum Frequency (Hz) — Maximum Frequency (Hz) specifies the Maximum Frequency of the Calibration Element. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-minimum-frequency-vi.html language=enus -->
## TOPIC 00074: RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-minimum-frequency-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-minimum-frequency-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Minimum Frequency of the Calibration Element. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use

### RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency VI

Sets the Minimum Frequency of the Calibration Element.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-set-minimum-frequency-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Minimum Frequency (Hz) — Minimum Frequency (Hz) specifies the Minimum Frequency of the Calibration Element. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-port-connectors-vi.html language=enus -->
## TOPIC 00075: RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-port-connectors-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-port-connectors-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element. icon Inputs/Outputs cstr.png Sele

### RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors VI

Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-set-port-connectors-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Connector IDs — Connector IDs specifies the array of Connectors associated with the Calibration Element. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-s-parameter-definition-vi.html language=enus -->
## TOPIC 00076: RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-s-parameter-definition-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-calibration-element-set-s-parameter-definition-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Defines the way how the S-Parameters of the Calibration Element are specified. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel:

### RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition VI

Defines the way how the S-Parameters of the Calibration Element are specified.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-calibration-element-set-s-parameter-definition-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. S-Parameter Definition — S-Parameter Definition specifies the S-Parameter definition of the Calibration Element. Reflect Model (0) S-Parameters defined by the Reflect model (1-port). Sparameter (1) S-Parameters defined by a S-Parameter list (1-port and 2-port). Delay Model (2) S-Parameters defined by a delay model (2-port). Unknown (3) S-Parameters not further specified. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| Reflect Model (0) | S-Parameters defined by the Reflect model (1-port). |
| Sparameter (1) | S-Parameters defined by a S-Parameter list (1-port and 2-port). |
| Delay Model (2) | S-Parameters defined by a delay model (2-port). |
| Unknown (3) | S-Parameters not further specified. |

Parent topic:

Calibration Element

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-impedance-vi.html language=enus -->
## TOPIC 00077: RFmxVNA Calkit Manager Calkit Connector Set Impedance VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-impedance-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-connector-set-impedance-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Impedance of a Connector of a specific Calkit. icon Inputs/Outputs cstr.png Selector String Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyCo

### RFmxVNA Calkit Manager Calkit Connector Set Impedance VI

Sets the Impedance of a Connector of a specific Calkit.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-connector-set-impedance-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Impedance (Ohm) — Impedance (Ohm) specifies the Impedance of a Connector of a specific Calkit. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Connector

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-set-lrl-line-auto-char-vi.html language=enus -->
## TOPIC 00078: RFmxVNA Calkit Manager Calkit Set LRL Line Auto Char VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-set-lrl-line-auto-char-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calkit-manager-calkit-set-lrl-line-auto-char-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures whether line parameters are automatically characterized during LRL calibration. LRL line auto characterization is applicable only when the Line standards have the same characteristic impedance. icon

### RFmxVNA Calkit Manager Calkit Set LRL Line Auto Char VI

Configures whether line parameters are automatically characterized during LRL calibration. LRL line auto characterization is applicable only when the Line standards have the same characteristic impedance.

[IMAGE alt='icon' src='rfmxvna-calkit-manager-calkit-set-lrl-line-auto-char-vi.png']

Parent topic:

Options

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-error-term-vi.html language=enus -->
## TOPIC 00079: RFmxVNA Calset Get Error Term VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-error-term-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-error-term-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns values for a specific error term from either the default calset of the specified signal or a named calset accessible across all signals. Behaviors for different combinations of Calset Name and Signal Name strings are as follows: Calset Name is "" (empty string): RFmx returns the error term v

### RFmxVNA Calset Get Error Term VI

Returns values for a specific error term from either the default calset of the specified signal or a named calset accessible across all signals.

Behaviors for different combinations of Calset Name and Signal Name strings are as follows:

- Calset Name is "" (empty string): RFmx returns the error term values from the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx returns the error term values from the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

[IMAGE alt='icon' src='rfmxvna-calset-get-error-term-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Calset Name — Calset Name specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. Error Term Identifier — Error Term Identifier specifies the type of error term in the calset. The error term can take the following values: Directivity (0) Directivity measured at Measurement Port (Source Port ignored). Source Match (1) Source Match measured at Measurement Port (Source Port ignored). Reflection Tracking (2) Reflection Tracking measured at Measurement Port (Source Port ignored). Transmission Tracking (3) Transmission Tracking measured at Measurement Port with Source Port being the source port. Load Match (4) Load Match measured at Measurement Port with Source Port being the source port. K (5) K measured at Measurement Port (Source Port ignored). alpha (6) alpha measured at Measurement Port (Source Port ignored). beta (7) beta measured at Measurement Port (Source Port ignored). gamma (8) gamma measured at Measurement Port (Source Port ignored). delta (9) delta measured at Measurement Port (Source Port ignored). Switch Term (10) Switch term measured at Measurement Port (Source Port ignored). The error term K, alpha, beta, gamma, and delta describe the relation of the scattered and incident waves at the calibration plane (denoted as waves a and b respectively) and the waves measured at VNA reference and test receivers (denoted as waves r and s respectively) by the following equations: a = K[alpha r + beta s] b = K[gamma r + delta s] , where alpha, beta, gamma, and delta represent the complex elements of a transmission matrix and K represents a complex scaling factor. Measurement Port — Measurement Port specifies the VNA port name corresponding to the Error Term you queried. error in (no error) — error in describes error conditions that occur before this node runs. Source Port — Source Port specifies the VNA port name for which the Error Term is queried. This parameter is only required to query Error Term defined by port pairs. The valid values of the parameter Error Term Identifier defined for port pairs are Transmission Tracking and Load Match. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Error Term — Error Term returns the computed error term from the calset. error out — error out returns error information. |  |
| --- | --- |
| Directivity (0) | Directivity measured at Measurement Port (Source Port ignored). |
| Source Match (1) | Source Match measured at Measurement Port (Source Port ignored). |
| Reflection Tracking (2) | Reflection Tracking measured at Measurement Port (Source Port ignored). |
| Transmission Tracking (3) | Transmission Tracking measured at Measurement Port with Source Port being the source port. |
| Load Match (4) | Load Match measured at Measurement Port with Source Port being the source port. |
| K (5) | K measured at Measurement Port (Source Port ignored). |
| alpha (6) | alpha measured at Measurement Port (Source Port ignored). |
| beta (7) | beta measured at Measurement Port (Source Port ignored). |
| gamma (8) | gamma measured at Measurement Port (Source Port ignored). |
| delta (9) | delta measured at Measurement Port (Source Port ignored). |
| Switch Term (10) | Switch term measured at Measurement Port (Source Port ignored). |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-frequency-grid-vi.html language=enus -->
## TOPIC 00080: RFmxVNA Calset Get Frequency Grid VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-frequency-grid-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-calset-get-frequency-grid-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals. Behaviors for different combinations of Calset Name and Signal Name strings are as follows: Calset Name is "" (empty string): RFmx returns the calibration fr

### RFmxVNA Calset Get Frequency Grid VI

Returns the calibration frequency grid from either the default calset of the specified signal or a named calset accessible across all signals.

Behaviors for different combinations of Calset Name and Signal Name strings are as follows:

- Calset Name is "" (empty string): RFmx returns the calibration frequency grid from the default calset of the signal instance specified in the Selector String. If you do not specify a Signal Name, then default RFmxVNA signal instance is used.
- Calset Name is non-empty string: If you do not specify a Signal Name, then RFmx returns the calibration frequency grid from the named calset. RFmx returns an error if you specify both Calset Name and Signal Name as non-empty strings.

[IMAGE alt='icon' src='rfmxvna-calset-get-frequency-grid-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Calset Name — Calset Name specifies the name of the calset. If you do not specify this parameter, the calset is saved as default calset for the specified signal and is not available for use in other signals. If you specify non-empty Calset Name string, calset is saved as a named calset available for use across all signals and is also selected as the active calset for the current signal. Error Term Identifier — Error Term Identifier specifies the type of error term in the calset. The error term can take the following values: Directivity (0) Directivity measured at Measurement Port (Source Port ignored). Source Match (1) Source Match measured at Measurement Port (Source Port ignored). Reflection Tracking (2) Reflection Tracking measured at Measurement Port (Source Port ignored). Transmission Tracking (3) Transmission Tracking measured at Measurement Port with Source Port being the source port. Load Match (4) Load Match measured at Measurement Port with Source Port being the source port. K (5) K measured at Measurement Port (Source Port ignored). alpha (6) alpha measured at Measurement Port (Source Port ignored). beta (7) beta measured at Measurement Port (Source Port ignored). gamma (8) gamma measured at Measurement Port (Source Port ignored). delta (9) delta measured at Measurement Port (Source Port ignored). Switch Term (10) Switch term measured at Measurement Port (Source Port ignored). The error term K, alpha, beta, gamma, and delta describe the relation of the scattered and incident waves at the calibration plane (denoted as waves a and b respectively) and the waves measured at VNA reference and test receivers (denoted as waves r and s respectively) by the following equations: a = K[alpha r + beta s] b = K[gamma r + delta s] , where alpha, beta, gamma, and delta represent the complex elements of a transmission matrix and K represents a complex scaling factor. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Frequency Grid (Hz) — Frequency Grid (Hz) returns the calibration frequency grid from the calset. This value is expressed in Hz. error out — error out returns error information. |  |
| --- | --- |
| Directivity (0) | Directivity measured at Measurement Port (Source Port ignored). |
| Source Match (1) | Source Match measured at Measurement Port (Source Port ignored). |
| Reflection Tracking (2) | Reflection Tracking measured at Measurement Port (Source Port ignored). |
| Transmission Tracking (3) | Transmission Tracking measured at Measurement Port with Source Port being the source port. |
| Load Match (4) | Load Match measured at Measurement Port with Source Port being the source port. |
| K (5) | K measured at Measurement Port (Source Port ignored). |
| alpha (6) | alpha measured at Measurement Port (Source Port ignored). |
| beta (7) | beta measured at Measurement Port (Source Port ignored). |
| gamma (8) | gamma measured at Measurement Port (Source Port ignored). |
| delta (9) | delta measured at Measurement Port (Source Port ignored). |
| Switch Term (10) | Switch term measured at Measurement Port (Source Port ignored). |

Parent topic:

Calset

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clear-measurement-memory-names-vi.html language=enus -->
## TOPIC 00081: RFmxVNA Clear Measurement Memory Names VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clear-measurement-memory-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-clear-measurement-memory-names-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the measurement memory for the measurement number specified by the Selector String. If Measurement memory name is "" (empty string): RFmx clears all the measurement memories associated with the measurement number. If measurement memory name is non-empty string: RFmx clears the specified measu

### RFmxVNA Clear Measurement Memory Names VI

Clears the measurement memory for the measurement number specified by the Selector String.

Note

- If Measurement memory name is "" (empty string): RFmx clears all the measurement memories associated with the measurement number.
- If measurement memory name is non-empty string: RFmx clears the specified measurement memory.

[IMAGE alt='icon' src='rfmxvna-clear-measurement-memory-names-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, measurement number and the measurement memory name. If you do not specify the signal name, the default signal instance is used. You must specify the measurement number. Example: "signal::sig1/sparam0/measmem::<measMemoryName>" "signal::sig1/sparam0" "sparam0" You can use the RFmxVNA Build Measurement Memory String along withRFmxVNA Build S-Parameter String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Memory

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-load-data-to-measurement-memory-from-file-vi.html language=enus -->
## TOPIC 00082: RFmxVNA Load Data to Measurement Memory from File VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-load-data-to-measurement-memory-from-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-load-data-to-measurement-memory-from-file-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the data from the input file to the measurement memory specified by the Selector String. This VI will overwrite the contents of the measurement memory if it already exists. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name an

### RFmxVNA Load Data to Measurement Memory from File VI

Loads the data from the input file to the measurement memory specified by the Selector String.

Note

[IMAGE alt='icon' src='rfmxvna-load-data-to-measurement-memory-from-file-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and the measurement number. If you do not specify the signal name, the default signal instance is used. You must specify the measurement number. Example: "signal::sig1/sparam0" "sparam0" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. File Path — File Path specifies the path to the file that contains the measurement data. Example: For S-Parameter measurement use a *.SnP file. Parameter — Parameter specifies the measurement parameter to load from the file. Example: Specify S11 for an *.S1P file. Specify 'S11 or S12 or S21 or S22 for an *.S2P file. Measurement Memory Name — Measurement Memory Name Measurement Memory Name specifies the name to associate with the data you load to the measurement memory. Provide a unique name. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Memory

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-mode-vi.html language=enus -->
## TOPIC 00083: RFmxVNA Marker Configure Mode VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-mode-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the marker mode. Use "marker<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is use

### RFmxVNA Marker Configure Mode VI

Configures the marker mode.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxvna-marker-configure-mode-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Marker Mode — Marker Mode specifies the mode for placing the marker. Continuous (0) Marker can be placed at any point and its response value is obtained by interpolation of actual measured data points. Discrete (1) Marker can be placed only at actual measured data points. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| Continuous (0) | Marker can be placed at any point and its response value is obtained by interpolation of actual measured data points. |
| Discrete (1) | Marker can be placed only at actual measured data points. |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-peak-search-excursion-vi.html language=enus -->
## TOPIC 00084: RFmxVNA Marker Configure Peak-Search Excursion VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-peak-search-excursion-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-peak-search-excursion-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search VI finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value. Use "marker<n>" as the selector string to configure this VI. icon Inputs/Outp

### RFmxVNA Marker Configure Peak-Search Excursion VI

Configures the peak-search excursion. When peak-excursion is enabled, peak search using Marker Search VI finds a peak such that the data value rises and falls around the peak by at least the specified peak excursion value.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxvna-marker-configure-peak-search-excursion-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Peak Excursion Enabled — Peak Excursion Enabled specifies whether Marker Search VI finds a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value or finds a peak without considering any peak excursion constraint. False (0) Disables the peak excursion. True (1) Enables the peak excursion. Peak Excursion — Peak Excursion specifies the peak excursion value that Marker Search VI uses to find a peak such that the data value rises and falls around the peak by atleast the specified peak excursion value. The threshold is expressed in the same units as the source data. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| False (0) | Disables the peak excursion. |
| True (1) | Enables the peak excursion. |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-peak-search-threshold-vi.html language=enus -->
## TOPIC 00085: RFmxVNA Marker Configure Peak-Search Threshold VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-peak-search-threshold-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-peak-search-threshold-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search VI in peak search mode finds the peaks that exceed this value and discards all other peaks. Use "marker<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String

### RFmxVNA Marker Configure Peak-Search Threshold VI

Configures the peak-search threshold. When peak-thresholding is enabled, Marker Search VI in peak search mode finds the peaks that exceed this value and discards all other peaks.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxvna-marker-configure-peak-search-threshold-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Threshold Enabled — Threshold Enabled specifies whether Marker Search VI finds a peak above specified Threshold or finds a peak without considering any Threshold constraint. False (0) Disables peak-thresholding. True (1) Enables peak-thresholding. Threshold — Threshold specifies the threshold value that a valid peak must exceed when you use Marker Search VI to find peaks. The threshold is expressed in the same units as the source data. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| False (0) | Disables peak-thresholding. |
| True (1) | Enables peak-thresholding. |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-reference-marker-vi.html language=enus -->
## TOPIC 00086: RFmxVNA Marker Configure Reference Marker VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-reference-marker-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-reference-marker-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an associated reference marker for a delta marker. Markers with Marker Type property set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta. Use "marker<n>" as the selector string to configure this

### RFmxVNA Marker Configure Reference Marker VI

Configures an associated reference marker for a delta marker. Markers with Marker Type property set to Delta must be associated with a reference marker. You cannot associate a reference marker for other markers whose Marker Type is not Delta.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxvna-marker-configure-reference-marker-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Reference Marker — Reference Marker specifies the marker index to be used as reference for the specified delta marker. All types of markers including Normal, Delta and Fixed can be used as a reference marker. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-target-value-vi.html language=enus -->
## TOPIC 00087: RFmxVNA Marker Configure Target Value VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-target-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-target-value-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the target value for the specified marker when performing Target search using Marker Search VI. Use "marker<n>" as the selector string to configure this VI. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and marker nu

### RFmxVNA Marker Configure Target Value VI

Configures the target value for the specified marker when performing Target search using Marker Search VI.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxvna-marker-configure-target-value-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Target Value — Marker X specifies the target value for target search. The target value is expressed in the same units as the source data. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-y-vi.html language=enus -->
## TOPIC 00088: RFmxVNA Marker Configure Y VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-y-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-configure-y-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Y value of the marker. You can configure the Y location of Fixed markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y

### RFmxVNA Marker Configure Y VI

Configures the Y value of the marker. You can configure the Y location of **Fixed** markers only. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number.

If Y value is a complex number, use Marker Y1 and Marker Y2 to set its real and imaginary components respectively. If Y value is a real number, use Marker Y1 to set the Y location and set Marker Y2 to 0.

When you want to use a **Fixed** marker as a reference marker for a Delta marker, then you must configure the Y value of the **Fixed** reference marker by calling this VI or by performing any marker search operation on the reference marker before configuring the X value of the **Delta** marker.

Use "marker<*n*>" as the selector string to configure this VI.

[IMAGE alt='icon' src='rfmxvna-marker-configure-y-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Marker Y1 — Marker Y1 specifies the Y1 component of the (Fixed) marker's Y value. Marker Y2 — Marker Y2 specifies the Y2 component of the (Fixed) marker's Y value.. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-fetch-y-vi.html language=enus -->
## TOPIC 00089: RFmxVNA Marker Fetch Y VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-fetch-y-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-fetch-y-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Y value of the marker. Y value of a Delta marker is relative to its reference marker. Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other format

### RFmxVNA Marker Fetch Y VI

Returns the Y value of the marker. Y value of a **Delta** marker is relative to its reference marker.

Y value can be a real or a complex number depending on format of the selected measurement for the configured data source. Y is a complex number for Complex, Smith and Polar formats. For all other formats, Y is a real number. If Y value is a complex number, Marker Y1 and Marker Y2 return its real and imaginary components respectively. If Y value is a real number, Marker Y1 returns the Y location and Marker Y2 returns 0.

[IMAGE alt='icon' src='rfmxvna-marker-fetch-y-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" "result::r1/marker0" "signal::sig1/result::r1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Marker Y1 — Marker Y1 returns the Y1 component of marker's Y value. Marker Y2 — Marker Y2 returns the Y2 component of marker's Y value. Y value is always returned as two components (Y1,Y2). The format of the Y value depends on the format of the selected measurement. If the format is Complex, Smith or Polar (Y1,Y2) are (Real, Imaginary). For all other formats (Y1,Y2) are (Value,0). error out — error out returns error information. |
| --- |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-search-vi.html language=enus -->
## TOPIC 00090: RFmxVNA Marker Search VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-search-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-marker-search-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Performs the marker search operation that you specify using Search Mode. Marker search operation is performed on real-valued data only. No search operation is performed on complex-valued data. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the

### RFmxVNA Marker Search VI

Performs the marker search operation that you specify using Search Mode.

Note

[IMAGE alt='icon' src='rfmxvna-marker-search-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name and marker number. If you do not specify the signal name, the default signal instance is used. Example: "marker0" "signal::sig1/marker0" "result::r1/marker0" "signal::sig1/result::r1/marker0" You can use the RFmxVNA_Build_Marker_String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI. Search Mode — Search Mode specifies the search-target. If search is successful, RFmx updates the marker X and Y values to the location at which search-target is found. None (0) No search operation is performed. Max (1) Moves the marker to the highest measured value on the configured data source. Min (2) Moves the marker to the lowest measured value on the configured data source. Peak (3) Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria. Next Peak (4) Moves the marker to the next peak that satisfies peak threshold and peak excursion criteria. Next Left Peak (5) Moves the marker to the next left peak that satisfies peak threshold and peak excursion criteria. Next Right Peak (6) Moves the marker to the next right peak that satisfies peak threshold and peak excursion criteria. Target (7) Moves the marker to the first right target encountered from the current marker position, wraps around if no target found. If marker mode is Discrete,marker moves to the data point closest to the first right target. Next Left Target (8) Moves the marker to the next left target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next left target. Next Right Target (9) Moves the marker to the next right target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next right target. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |  |
| --- | --- |
| None (0) | No search operation is performed. |
| Max (1) | Moves the marker to the highest measured value on the configured data source. |
| Min (2) | Moves the marker to the lowest measured value on the configured data source. |
| Peak (3) | Moves the marker to the highest peak that satisfies peak threshold and peak excursion criteria. |
| Next Peak (4) | Moves the marker to the next peak that satisfies peak threshold and peak excursion criteria. |
| Next Left Peak (5) | Moves the marker to the next left peak that satisfies peak threshold and peak excursion criteria. |
| Next Right Peak (6) | Moves the marker to the next right peak that satisfies peak threshold and peak excursion criteria. |
| Target (7) | Moves the marker to the first right target encountered from the current marker position, wraps around if no target found. If marker mode is Discrete,marker moves to the data point closest to the first right target. |
| Next Left Target (8) | Moves the marker to the next left target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next left target. |
| Next Right Target (9) | Moves the marker to the next right target encountered from the current marker position. If marker mode is Discrete,marker moves to the data point closest to the next right target. |

Parent topic:

Marker

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-send-software-edge-trigger-vi.html language=enus -->
## TOPIC 00091: RFmxVNA Send Software Edge Trigger VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-send-software-edge-trigger-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-send-software-edge-trigger-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a trigger to the device when you set Trigger Type to Software and the device is waiting for the trigger to be sent. RFmxVNA ignores Software Edge Trigger when performing calibration. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In specifies the RFmx session ref

### RFmxVNA Send Software Edge Trigger VI

Sends a trigger to the device when you set [Trigger Type](/csh?context=rfmxvna_rfmxvnaprop_attrd00042) to Software and the device is waiting for the trigger to be sent.

Note

[IMAGE alt='icon' src='rfmxvna-send-software-edge-trigger-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-data-vi.html language=enus -->
## TOPIC 00092: RFmxVNA SParams Fetch Data VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-data-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the S-Parameters (SParams) measurement results. Use the pull-down menu to select an instance of this VI. icon

### RFmxVNA SParams Fetch Data VI

Fetches the S-Parameters (SParams) measurement results.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='rfmxvna-sparams-fetch-data-vi.png']

- [RFmxVNA SParams Fetch X Data VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-x-data-vi.html) Fetches an array of frequency values when you perform S-Parameter measurement with Sweep Type property set to List or Linear or Segment . It fetches an array of time values when you perform S-Parameter measurement with Sweep Type property set to CW Time .
- [RFmxVNA SParams Fetch Y Data VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-y-data-vi.html) Fetches the S-Parameter data for all SParams Format types.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-x-data-vi.html language=enus -->
## TOPIC 00093: RFmxVNA SParams Fetch X Data VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-x-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-x-data-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of frequency values when you perform S-Parameter measurement with Sweep Type property set to List or Linear or Segment. It fetches an array of time values when you perform S-Parameter measurement with Sweep Type property set to CW Time. icon Inputs/Outputs cstr.png Selector String S

### RFmxVNA SParams Fetch X Data VI

Fetches an array of frequency values when you perform S-Parameter measurement with [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property set to **List** or **Linear** or **Segment**. It fetches an array of time values when you perform S-Parameter measurement with [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property set to **CW Time**.

[IMAGE alt='icon' src='rfmxvna-sparams-fetch-x-data-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Timeout (s) — Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. X — X returns X-Axis Data. error out — error out returns error information. |
| --- |

Parent topic:

RFmxVNA SParams Fetch Data VI

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-y-data-vi.html language=enus -->
## TOPIC 00094: RFmxVNA SParams Fetch Y Data VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-y-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-fetch-y-data-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the S-Parameter data for all SParams Format types. Use "sparam<n>" as the selector string to read results from this VI. For different SParams Format, the data is returned as follows: SParam Format Y1 Y2 Magnitude (0) Magnitude of the S-Parameter data Empty array Phase (1) Phase of the S-Para

### RFmxVNA SParams Fetch Y Data VI

Fetches the S-Parameter data for all [SParams Format](/csh?context=rfmxvna_rfmxvnaprop_attrd01005) types.

Use "sparam<*n*>" as the selector string to read results from this VI.

For different [SParams Format](/csh?context=rfmxvna_rfmxvnaprop_attrd01005), the data is returned as follows:

| SParam Format | Y1 | Y2 |
| --- | --- | --- |
| Magnitude (0) | Magnitude of the S-Parameter data | Empty array |
| Phase (1) | Phase of the S-Parameter data | Empty array |
| Complex (2) | Real part of the complex S-Parameter data | Imaginary part of the complex S-Parameter data |
| SWR (3) | Standing wave ratio computed from the S-Parameter data | Empty array |
| Smith Impedance (4) | Real part of the complex impedance computed from the S-Parameter data | Imaginary part of the complex impedance computed from the S-Parameter data |
| Smith Admittance (5) | Real part of the complex admittance computed from the S-Parameter data | Imaginary part of the complex admittance computed from the S-Parameter data |
| Polar (6) | Magnitude of the S-Parameter data | Phase of the S-Parameter data |
| Group Delay (7) | Group delay computed from the S-Parameter data | Empty array |

[IMAGE alt='icon' src='rfmxvna-sparams-fetch-y-data-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "sparam0" "signal::sig1/sparam0" "result::r1/sparam0" "signal::sig1/result::r1/sparam0" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Timeout (s) — Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. Y1 — Y1 returns Y1 data array. You can refer to the VI description for interpreting Y data based on SParams Format type. Y2 — Y2 returns Y2 data array. You can refer to the VI description for interpreting Y data based on SParams Format type. error out — error out returns error information. |
| --- |

Parent topic:

RFmxVNA SParams Fetch Data VI

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-get-s-parameter-vi.html language=enus -->
## TOPIC 00095: RFmxVNA SParams Get S-Parameter VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-get-s-parameter-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-sparams-get-s-parameter-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the S-Parameter being measured in format S<receiver port number><source port number> Use "sparam<n>" as the selector string for this VI. Supported devices: NI PXIe-5633 icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name, res

### RFmxVNA SParams Get S-Parameter VI

Returns the S-Parameter being measured in format S<*receiver port number*><*source port number*>

Use "sparam<*n*>" as the selector string for this VI.

**Supported devices**: NI PXIe-5633

[IMAGE alt='icon' src='rfmxvna-sparams-get-s-parameter-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "sparam0" "signal::sig1/sparam0" "result::r1/sparam0" "signal::sig1/result::r1/sparam0" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. S-Parameter — S-Parameter returns the S-Parameter being measured in format S<receiver port number><source port number>. error out — error out returns error information. |
| --- |

Parent topic:

SParams

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-wait-for-measurement-complete-vi.html language=enus -->
## TOPIC 00096: RFmxVNA Wait for Measurement Complete VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-wait-for-measurement-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-wait-for-measurement-complete-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits for the specified number for seconds for all the measurements to complete. icon Inputs/Outputs cstr.png Selector String Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you

### RFmxVNA Wait for Measurement Complete VI

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='icon' src='rfmxvna-wait-for-measurement-complete-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Timeout (s) — Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. error out — error out returns error information. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-data-vi.html language=enus -->
## TOPIC 00097: RFmxVNA Waves Fetch Data VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-data-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches the Waves measurement results. Use the pull-down menu to select an instance of this VI. icon

### RFmxVNA Waves Fetch Data VI

Fetches the Waves measurement results.

Use the pull-down menu to select an instance of this VI.

[IMAGE alt='icon' src='rfmxvna-waves-fetch-data-vi.png']

- [RFmxVNA Waves Fetch X Data VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-x-data-vi.html) Fetches an array of frequency values when you perform wave measurement with Sweep Type property set to List or Linear or Segment . It fetches an array of time values when you perform wave measurement with Sweep Type property set to CW Time .
- [RFmxVNA Waves Fetch Y Data VI](../../../../../vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-y-data-vi.html) Fetches the wave data for all Waves Format types.

Parent topic:

Fetch

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-x-data-vi.html language=enus -->
## TOPIC 00098: RFmxVNA Waves Fetch X Data VI

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-x-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/rfmxvna-waves-fetch-x-data-vi.html
- document_id: `rfmxvna-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches an array of frequency values when you perform wave measurement with Sweep Type property set to List or Linear or Segment. It fetches an array of time values when you perform wave measurement with Sweep Type property set to CW Time. icon Inputs/Outputs cstr.png Selector String Selector String

### RFmxVNA Waves Fetch X Data VI

Fetches an array of frequency values when you perform wave measurement with [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property set to **List** or **Linear** or **Segment**. It fetches an array of time values when you perform wave measurement with [Sweep Type](/csh?context=rfmxvna_rfmxvnaprop_attrd0002e) property set to **CW Time**.

[IMAGE alt='icon' src='rfmxvna-waves-fetch-x-data-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" Instrument Handle In — Instrument Handle In specifies the RFmx session refnum. Timeout (s) — Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. Instrument Handle Out — Instrument Handle Out passes a reference of your RFmx session to the next VI. X — X returns X-Axis Data. error out — error out returns error information. |
| --- |

Parent topic:

RFmxVNA Waves Fetch Data VI

<!--NI_TOPIC bundle=rfmxvna-labview-api-ref path=vi-lib/rfmx/vna/mx/rfmxvna-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00099: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxvna-labview-api-ref`
- source_path: `vi-lib/rfmx/vna/mx/rfmxvna-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxvna-labview-api-ref/raw/resource/enus/vi-lib/rfmx/vna/mx/rfmxvna-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxvna-labview-api-ref`
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
