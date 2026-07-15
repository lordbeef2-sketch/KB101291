# NI DOCUMENT BUNDLE: rfmx-vna-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-vna-vi start=1 end=137 -->
<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/advanced_pal.html language=enus -->
## TOPIC 00001: Advanced

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/advanced_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/advanced_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Advanced

Owning Palette:

RFmx VNA VIs

Use the VIs on this palette to use advanced features.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Abort Measurements | Stops acquisition and measurements associated with signal instance that you specify in the Selector String parameter, which were previously initiated by the RFmxVNA Initiate VI or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error. |
| RFmxVNA Create Signal Configuration | Creates a new instance of a signal. RFmxVNA Signal concept is same as Channel concept in third party software. |
| RFmxVNA Clear Named Result | Clears a result instance specified by the result name in the Selector String parameter. |
| RFmxVNA Clone Signal Configuration | Creates a new instance of a signal by copying all the property values from an existing signal instance. |
| RFmxVNA Delete Signal Configuration | Deletes an instance of a signal that you specify in the Signal Name parameter. |
| RFmxVNA Get All Named Result Names | Returns all the named result names of the signal that you specify in the Selector String parameter. |
| RFmxVNA Clear All Named Results | Clears all results for the signal that you specify in the Selector String parameter. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/build_string_pal.html language=enus -->
## TOPIC 00002: Build String

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/build_string_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/build_string_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Build String

Owning Palette:

RFmx VNA VIs

Use the VIs on this palette to create strings for configurations that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Build CalStep String | Creates the calibration step string to use as the selector string with the RFmxVNA Calibration Acquire VI. |
| RFmxVNA Build Port String | Creates selector string specifying the port(s) for use with configuration or fetch properties and VIs. |
| RFmxVNA Build Segment String | Creates a selector string specifying the segment number for use with configuration or fetch properties and VIs. |
| RFmxVNA Build Signal String | Creates selector string for use with configuration or fetch properties and VIs. |
| RFmxVNA Build S-Parameter String | Creates the selector string to use with S-Parameter configuration or fetch properties and VIs. |
| RFmxVNA Build Wave String | Creates the selector string to use with Wave configuration or fetch properties and VIs. |
| RFmxVNA Build Calkit String | Creates a selector string specifying the Calkit. |
| RFmxVNA Build Connector String | Creates a selector string specifying the Connector within the Calkit. |
| RFmxVNA Build Calibration Element String | Creates a selector string specifying the Calibration Element within the Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/cal_config_pal.html language=enus -->
## TOPIC 00003: Calset

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/cal_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/cal_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Calset

Owning Palette:

Configuration

Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calset Load from File | Loads error-correction terms you saved in a calset file (.ncst) using RFmxVNA Calset Save to File VI. If error-correction terms already exist for the RFmx Signal instance you specified using the Selector String input, RFmx will replace those correction terms. You cannot specify both signal name in Selector String and Calset Name together. If you do not specify both signal name in Selector String and Calset Name, the error term will be loaded from specified file to in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the error term will be loaded from specified file to in memory calset of the specified signal instance. If you specify only Calset Name, the error term will be loaded from specified file to the global calset with the specified calset name. |
| RFmxVNA Calset Save to File | Saves the error-correction terms to a calset file (*.ncst). You can call this VI only after you call RFmxVNA Calibration Save VI. You cannot specify both signal name in Selector String and Calset Name together. If you do not specify both signal name in Selector String and Calset Name, the error term will be saved to specified file from in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the error term will be saved to specified file from in memory calset of the specified signal instance. If you specify only Calset Name, the error term will be saved to specified file from the global calset with the specified calset name. |
| RFmxVNA Copy Calset | Copies the source calset data into the new calset specified. This VI will not change the source calset data. You cannot specify both signal name in Selector String and Source Calset Name together. If you do not specify both signal name in Selector String and Source Calset Name, calset data from in memory calset of default signal instance will be copied to New Calset. If you do not specify Source Calset Name but specify signal name in Selector String, the calset data from in memory calset of the specified signal instance will be copied to New Calset. If you specify only Source Calset Name, the calset data from the global calset with the specified Source calset name will be copied to New Calset. |
| RFmxVNA Get All Calset Names | Returns all the global calset names. |
| RFmxVNA Select Active Calset | Activates the specified calset to the signal instance you specified using the Selector String input. If you do not specify both signal name in Selector String and Calset Name,the in memory calset will be activated for default signal instance. If you do not specify Calset Name but specify signal name in Selector String, in memory calset will be activated for the specified signal instance. If you specify only Calset Name, the global calset with the specified calset name will be activated for the default signal instance. If you specify both signal name in Selector string and Calset Name, the global calset with the specified calset name will be activated for the specified signal instance. You can use the RFmxVNA Get All Calset Names VI to get the list of available global calsets. |
| RFmxVNA Deselect Active Calset | Deselects the calset which is active for the signal instance you specified using the signal name in Selector String input. This VI will not delete in memory signal calset or global calset. |
| RFmxVNA Clear Calset | Deletes the specified calset. You cannot specify both signal name in Selector String and Calset Name together. If you do not specify both signal name in Selector String and Calset Name, in memory calset of default signal instance will be deleted if active on the signal. If you do not specify Calset Name but specify signal name in Selector String, the in memory calset of the specified signal instance will be deleted if active on the signal. If you specify only Calset Name, the global calset with the specified calset name will be deleted. |
| RFmxVNA Calset Get Frequency Grid | Returns the calibration frequency grid from the Calset. You cannot specify both signal name in Selector String and Calset Name together. If you do not specify both signal name in Selector String and Calset Name, the frequency grid will be returned from in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the frequency grid will be returned from in memory calset of the specified signal instance. If you specify only Calset Name, the frequency grid will returned from the global calset with the specified calset name. Note You can call this VI only after you call the RFmxVNA Calibration Save VI. |
|  | Note You can call this VI only after you call the RFmxVNA Calibration Save VI. |
| RFmxVNA Calset Get Error Term | Returns a specific error term from the Calset. You cannot specify both signal name in Selector String and Calset Name together. If you do not specify both signal name in Selector String and Calset Name, the error term will be returned from in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the error term will be returned from in memory calset of the specified signal instance. If you specify only Calset Name, the error term will returned from the global calset with the specified calset name. Note You can call this VI only after you call the RFmxVNA Calibration Save VI. |
|  | Note You can call this VI only after you call the RFmxVNA Calibration Save VI. |
| RFmxVNA Calset Embed Fixture (s2p) | Embeds the inverse of a given fixture network into a Calset in memory. The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed without considering the calibration adapter in the measurement deembedding. The fixture network must be known and the fixture S-parameters have to be provided as s2p-file. A potential flip of the fixture network with respect to its S-parameter definitions can be configured by the ‘S-Parameter Orientation’. The operation applies to one VNA port at a time, specified by ‘VNA Port’ parameter. Depending on the parameter ‘New Calset Name’, a new Calset will be created or the input Calset itself will be updated. You cannot specify both signal name in Selector String and Calset Name together. If you specify ‘New Calset Name’ input, a new global calset will be created from original calset specified by Calset Name input and modified with embedding data. If you do not specify ‘New Calset Name’ input, the original calset itself will be modified with embedding data. If you do not specify both signal name in Selector String and Calset Name, original calset refers to in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, original calset refers to in memory calset of the specified signal instance. If you specify only Calset Name, original calset refers to the global calset with the specified Calset Name. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/calelement_calkit_calkitmanager_config_pal.html language=enus -->
## TOPIC 00004: Calibration Element

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/calelement_calkit_calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/calelement_calkit_calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Calibration Element

Owning Palette:

Calkit

Use the VIs on this palette to configure calibration element.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Calkit Calibration Element Set Description | Sets the description for a Calibration Element of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Calibration Element Get Description | Returns the description for a Calibration Element of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Calibration Element Set Types | Sets the type(s) of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Get Types | Returns the type(s) of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors | Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Get Port Connectors | Returns the array of Connectors associated with the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition | Defines the way how the S-Parameters of the Calibration Element are specified. |
| RFmxVNA Calkit Manager Calkit Calibration Element Get S-Parameter Definition | Returns the S-Parameter definition of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency | Sets the Minimum Frequency of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Get Minimum Frequency | Returns the Minimum Frequency of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency | Sets the Maximum Frequency of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element Get Maximum Frequency | Returns the Maximum Frequency of the Calibration Element. |

| Subpalette | Description |
| --- | --- |
| Reflect Model | Use the VIs on this palette to configure Reflect Model based calibration element. |
| Delay Model | Use the VIs on this palette to configure delay model based calibration element. |
| S-Parameter | Use the VIs on this palette to configure s-parameter based calibration element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/calibration_pal.html language=enus -->
## TOPIC 00005: Calibration

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/calibration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/calibration_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Calibration

Owning Palette:

RFmx VNA VIs

Use the VIs on this palette to use calibration.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calibration Abort | Stops calibration associated with signal instance that you specify in the Selector String parameter, which was previously initiated by the RFmxVNA Calibration Initiate VI. Calling this VI is optional, unless you want to stop a calibration before it is complete. This VI executes even if there is an incoming error. |
| RFmxVNA Calibration Acquire | Measures one or more calibration standards for the specified calibration step. The recommended sequence of operations to call this VI is illustrated below: [START] -> ... -> [Configure Calibration Settings] -> [Call RFmxVNA Calibration Initiate VI] -> [Acquire Calibration Step<i>] -> [Acquire Calibration Step<j>] -> ...->[END]. Here, "Acquire Calibration Step<i>" denotes a call to RFmxVNA Calibration Acquire VI for the ith calibration step. When Calkit Type is Electronic, a single call to this VI acquires calibration data for all the calibration standards in the vCal module. When Calkit Type is Mechanical, calibration data for only the active cal step is acquired. Specify the active cal step in the Selector String. Use RFmxVNA Build CalStep String VI to build cal step string. |
| RFmxVNA Calibration Initiate | Commits the calibration settings. RFmx creates calibration-steps required to perform calibration. Call this VI after configuring the calibration settings. After calling this VI, if you change any calibration setting, you must call this VI again to commit the change(s) to said calibration setting(s). |
| RFmxVNA Calibration Save | Computes error-correction terms and saves the calset in memory. Call this VI after calibration data for all calibration steps have been acquired using RFmxVNA Calibration Acquire VI. To perform another calibration after you call this VI, you must call RFmxVNA Calibration Initiate VI again. Computed error-correction terms will be saved to calset in memory for the signal specified in Selector String input. If you specify Calset Name, error-correction terms will also be saved to the specified calset and made available globally for use by all signals. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/calkit_calkitmanager_config_pal.html language=enus -->
## TOPIC 00006: Calkit

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/calkit_calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/calkit_calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Calkit

Owning Palette:

Calkit Manager

Use the VIs on this palette to configure calkit.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Calkit Add Connector | Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit. |
| RFmxVNA Calkit Manager Calkit Remove Connector | Removes a Connector element from the Calkit. |
| RFmxVNA Calkit Manager Calkit Get Connector IDs | Returns the list of Connector IDs for all connectors in the Calkit. |
| RFmxVNA Calkit Manager Calkit Add Calibration Element | Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit. |
| RFmxVNA Calkit Manager Calkit Remove Calibration Element | Removes the Calibration Element identified by its Calibration Element ID from the Calkit. |
| RFmxVNA Calkit Manager Calkit Get Calibration Element IDs | Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit. |
| RFmxVNA Calkit Manager Calkit Set Description | Sets the description for the Calkit. |
| RFmxVNA Calkit Manager Calkit Get Description | Returns the description of the Calkit. |
| RFmxVNA Calkit Manager Calkit Set Version | Sets the version string for the Calkit. |
| RFmxVNA Calkit Manager Calkit Get Version | Returns the version string of the Calkit. |

| Subpalette | Description |
| --- | --- |
| Connector | Use the VIs on this palette to configure connector. |
| Calibration Element | Use the VIs on this palette to configure calibration element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/calkitmanager_config_pal.html language=enus -->
## TOPIC 00007: Calkit Manager

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Calkit Manager

Owning Palette:

Configuration

Use the VIs on this palette to configure calkit manager.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Import Calkit | Imports a Calkit file into the Calkit Manager. |
| RFmxVNA Calkit Manager Export Calkit | Exports a Calkit to file. |
| RFmxVNA Calkit Manager Create Calkit | Creates a new empty Calkit with the user defined Calkit ID in Calkit Manager. The user defined Calkit ID has to be unique among all Calkits in Calkit Manager. |
| RFmxVNA Calkit Manager Remove Calkit | Removes a Calkit from Calkit Manager. |
| RFmxVNA Calkit Manager Delete Calkit | Removes a Calkit from Calkit Manager and deletes the corresponding file, if it exists. |
| RFmxVNA Calkit Manager Validate Calkit | Validates the consistency of a Calkit definition and returns the status of the validation. |
| RFmxVNA Calkit Manager Get Calkit IDs | Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager. |

| Subpalette | Description |
| --- | --- |
| Calkit | Use the VIs on this palette to configure calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/configuration_pal.html language=enus -->
## TOPIC 00008: Configuration

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/configuration_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmx VNA VIs

Use the VIs on this palette to configure measurements. You can use the [RFmxVNA Property Node](rfmxvna_property_node.html) VI to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Configure Frequency List (Start Stop Points) | Configures the list of frequencies at which the measurement needs to be performed. The start frequency and stop frequency points are inclusive in the frequency list. |

| Subpalette | Description |
| --- | --- |
| SParams | Use the VIs on this palette to configure S-Parameter measurements. You can use the RFmxVNA Property Node to configure additional properties. |
| Waves | Use the VIs on this palette to configure Wave measurements. You can use the RFmxVNA Property Node to configure additional properties. |
| Calset | Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties. |
| Correction | Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties. |
| Calkit Manager | Use the VIs on this palette to configure calkit manager. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/connector_calkit_calkitmanager_config_pal.html language=enus -->
## TOPIC 00009: Connector

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/connector_calkit_calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/connector_calkit_calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Connector

Owning Palette:

Calkit

Use the VIs on this palette to configure connector.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Calkit Connector Set Description | Sets the description for a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Get Description | Returns the description of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Set Gender | Sets the Gender of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Get Gender | Returns the Gender of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Set Type | Sets the Type of a Connector of a specific Calkit. Connector type is a user defined string (for example 'SMA', '1.8mm', etc.). |
| RFmxVNA Calkit Manager Calkit Connector Get Type | Returns the Type of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Set Impedance | Sets the Impedance of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Get Impedance | Returns the Impedance of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Set Minimum Frequency | Sets the Minimum Frequency of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Get Minimum Frequency | Returns the Minimum Frequency of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Set Maximum Frequency | Sets the Maximum Frequency of a Connector of a specific Calkit. |
| RFmxVNA Calkit Manager Calkit Connector Get Maximum Frequency | Returns the Maximum Frequency of a Connector of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/correction_config_pal.html language=enus -->
## TOPIC 00010: Correction

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/correction_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/correction_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Correction

Owning Palette:

Configuration

Use the VIs on this palette to configure calset. You can use the RFmxVNA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Configure Correction Port Subset | Configures the subset of ports to be corrected when Correction Port Subset Enabled property is set to True. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/delaymodel_calelement_calkit_calkitmanager_config_pal.html language=enus -->
## TOPIC 00011: Delay Model

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/delaymodel_calelement_calkit_calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/delaymodel_calelement_calkit_calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Delay Model

Owning Palette:

Calibration Element

Use the VIs on this palette to configure delay model based calibration element.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Set Delay | Defines the Delay of a Calibration Element defined by the Delay Model. |
| RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay | Returns the Delay of a Calibration Element defined by the Delay Model. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/fetch_pal.html language=enus -->
## TOPIC 00012: Fetch

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/fetch_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/fetch_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Fetch

Owning Palette:

RFmx VNA VIs

Use the VIs on this palette to fetch measurement results and traces.

| Palette Object | Description |
| --- | --- |
| RFmxVNA SParams Fetch | Fetches the S-Parameters (SParams) measurement results. Use the pull-down menu to select an instance of this VI. |
| RFmxVNA Waves Fetch | Fetches the Waves measurement results. Use the pull-down menu to select an instance of this VI. |
| RFmxVNA Calkit Manager Get Calkit IDs | Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/refmodel_calelement_calkit_calkitmanager_config_pal.html language=enus -->
## TOPIC 00013: Reflect Model

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/refmodel_calelement_calkit_calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/refmodel_calelement_calkit_calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Reflect Model

Owning Palette:

Calibration Element

Use the VIs on this palette to configure Reflect Model based calibration element.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Model Type | Specifies the model type of the 1-port reflect standard. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Model Type | Returns the model type of of the 1-port reflect standard. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability | Specifies the S-Parameter availability. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get S-Param Availability | Returns the S-Parameter availability. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C0 | Specifies the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C0 | Returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C1 | Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C1 | Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C2 | Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2 | Returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C3 | Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C3 | Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Delay | Specifies the offset delay. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Delay | Returns the offset delay. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Loss | Specifies the offset loss. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Loss | Returns the offset loss. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Z0 | Specifies the impedance of the offset. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Z0 | Returns the impedance of the offset. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Reference Impedance | Specifies the reference impedance. |
| RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Reference Impedance | Returns the reference impedance. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_abort_measurements.html language=enus -->
## TOPIC 00014: RFmxVNA Abort Measurements (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_abort_measurements.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_abort_measurements.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Abort Measurements (VI)

Owning Palette:

Advanced

Stops acquisition and measurements associated with signal instance that you specify in the **Selector String** parameter, which were previously initiated by the [RFmxVNA Initiate VI](rfmxvna_initiate.html) or measurement read VIs. Calling this VI is optional, unless you want to stop a measurement before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxVNA Abort Measurements' src='rfmxvna_abort_measurements.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_calibration_element_string.html language=enus -->
## TOPIC 00015: RFmxVNA Build Calibration Element String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_calibration_element_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_calibration_element_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Calibration Element String (VI)

Owning Palette:

Build String

Creates a selector string specifying the Calibration Element within the Calkit.

[IMAGE alt='RFmxVNA Build Calibration Element String' src='rfmxvna_build_calibration_element_string.gif']

|  | Calkit Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
| --- | --- |
|  | Calibration Element ID specifies the ID of the Calibration Element within the Calkit. |
|  | Calkit Calibration Element Selector String Out returns the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_calkit_string.html language=enus -->
## TOPIC 00016: RFmxVNA Build Calkit String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_calkit_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_calkit_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Calkit String (VI)

Owning Palette:

Build String

Creates a selector string specifying the Calkit.

[IMAGE alt='RFmxVNA Build Calkit String' src='rfmxvna_build_calkit_string.gif']

|  | Calkit ID specifies the ID for the Calkit in Calkit Manager. |
| --- | --- |
|  | Calkit Selector String Out returns the selector string created by this VI. The selector string comprises of the Calkit ID. Example: "ckit::MyCkitID" |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_calstep_string.html language=enus -->
## TOPIC 00017: RFmxVNA Build CalStep String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_calstep_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_calstep_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build CalStep String (VI)

Owning Palette:

Build String

Creates the calibration step string to use as the selector string with the [RFmxVNA Calibration Acquire](rfmxvna_calibration_acquire.html) VI.

[IMAGE alt='RFmxVNA Build CalStep String' src='rfmxvna_build_calstep_string.gif']

|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | CalStep Number specifies the calibration step number for building the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_connector_string.html language=enus -->
## TOPIC 00018: RFmxVNA Build Connector String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_connector_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_connector_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Connector String (VI)

Owning Palette:

Build String

Creates a selector string specifying the Connector within the Calkit.

[IMAGE alt='RFmxVNA Build Connector String' src='rfmxvna_build_connector_string.gif']

|  | Calkit Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
| --- | --- |
|  | Connector ID specifies the ID of the Connector within the Calkit. |
|  | Calkit Connector Selector String Out returns the selector string created by this VI. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_port_string.html language=enus -->
## TOPIC 00019: RFmxVNA Build Port String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_port_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_port_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Port String (VI)

Owning Palette:

Build String

Creates selector string specifying the port(s) for use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxVNA Build Port String' src='rfmxvna_build_port_string.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Port Name specifies the signal name for building the selector string. This input accepts the port name with or without the "port::" prefix. The default value is "" (empty string). Example: "" "port::port1" "port1" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_s-parameter_string.html language=enus -->
## TOPIC 00020: RFmxVNA Build S-Parameter String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_s-parameter_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_s-parameter_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build S-Parameter String (VI)

Owning Palette:

Build String

Creates the selector string to use with S-Parameter configuration or fetch properties and VIs.

[IMAGE alt='RFmxVNA Build S-Parameter String' src='rfmxvna_build_s-parameter_string.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | S-Parameter Number specifies the s-parameter index for building the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_segment_string.html language=enus -->
## TOPIC 00021: RFmxVNA Build Segment String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_segment_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_segment_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Segment String (VI)

Owning Palette:

Build String

Creates a selector string specifying the segment number for use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxVNA Build Segment String' src='rfmxvna_build_segment_string.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Segment Number specifies the segment for building the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_signal_string.html language=enus -->
## TOPIC 00022: RFmxVNA Build Signal String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_signal_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_signal_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Signal String (VI)

Owning Palette:

Build String

Creates selector string for use with configuration or fetch properties and VIs.

[IMAGE alt='RFmxVNA Build Signal String' src='rfmxvna_build_signal_string.gif']

|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
| --- | --- |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_build_wave_string.html language=enus -->
## TOPIC 00023: RFmxVNA Build Wave String (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_build_wave_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_build_wave_string.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Build Wave String (VI)

Owning Palette:

Build String

Creates the selector string to use with Wave configuration or fetch properties and VIs.

[IMAGE alt='RFmxVNA Build Wave String' src='rfmxvna_build_wave_string.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Wave Number specifies the wave index for building the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calibration_abort.html language=enus -->
## TOPIC 00024: RFmxVNA Calibration Abort (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calibration_abort.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calibration_abort.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calibration Abort (VI)

Owning Palette:

Calibration

Stops calibration associated with signal instance that you specify in the **Selector String** parameter, which was previously initiated by the [RFmxVNA Calibration Initiate VI](rfmxvna_calibration_initiate.html). Calling this VI is optional, unless you want to stop a calibration before it is complete. This VI executes even if there is an incoming error.

[IMAGE alt='RFmxVNA Calibration Abort' src='rfmxvna_calibration_abort.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calibration_acquire.html language=enus -->
## TOPIC 00025: RFmxVNA Calibration Acquire (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calibration_acquire.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calibration_acquire.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calibration Acquire (VI)

Owning Palette:

Calibration

Measures one or more calibration standards for the specified calibration step. The recommended sequence of operations to call this VI is illustrated below:
[START] -> ... -> [Configure Calibration Settings] -> [Call RFmxVNA Calibration Initiate VI] -> [Acquire Calibration Step<*i*>] -> [Acquire Calibration Step<*j*>] -> ...->[END]. Here, "Acquire Calibration Step<*i*>" denotes a call to RFmxVNA Calibration Acquire VI for the i<sup>th</sup> calibration step.

When [Calkit Type](/csh?topicname=rfmxvnaprop/attrd00012.html) is **Electronic**, a single call to this VI acquires calibration data for all the calibration standards in the vCal module.

When [Calkit Type](/csh?topicname=rfmxvnaprop/attrd00012.html) is **Mechanical**, calibration data for only the active cal step is acquired. Specify the active cal step in the Selector String. Use [RFmxVNA Build CalStep String](rfmxvna_build_calstep_string.html) VI to build cal step string.

[IMAGE alt='RFmxVNA Calibration Acquire' src='rfmxvna_calibration_acquire.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Valid selector string format is [signal::<signal name>[/calstep<n>]]. Example: "signal::mysignal" "signal::mysig/calstep0" "signal::mysig/calstep3" When you set the Selector String to "" (empty string), calling this VI will acquire calibration standard measurements for calstep0 for the default signal. When you set the Selector String to "signal::mysignal", calling this VI will acquire calibration standard measurements for calstep0 for the signal "signal::mysignal". When you set the Selector String to "signal::mysig/calstep<n>", calling this VI will acquire calibration standard measurements for calstep<n> for the signal "signal::mysig". You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |
|  | Timeout (s) specifies the timeout, in seconds, for acquiring the calibration data. Set this value to an appropriate time, longer than expected for completing acqusition(s) for the speficied calibration step. A value of -1 specifies that the VI waits until the acquisition is complete. The default value is 10. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calibration_initiate.html language=enus -->
## TOPIC 00026: RFmxVNA Calibration Initiate (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calibration_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calibration_initiate.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calibration Initiate (VI)

Owning Palette:

Calibration

Commits the calibration settings. RFmx creates calibration-steps required to perform calibration. Call this VI after configuring the calibration settings. After calling this VI, if you change any calibration setting, you must call this VI again to commit the change(s) to said calibration setting(s).

[IMAGE alt='RFmxVNA Calibration Initiate' src='rfmxvna_calibration_initiate.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calibration_save.html language=enus -->
## TOPIC 00027: RFmxVNA Calibration Save (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calibration_save.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calibration_save.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calibration Save (VI)

Owning Palette:

Calibration

Computes error-correction terms and saves the calset in memory. Call this VI after calibration data for all calibration steps have been acquired using [RFmxVNA Calibration Acquire](rfmxvna_calibration_acquire.html) VI. To perform another calibration after you call this VI, you must call [RFmxVNA Calibration Initiate](rfmxvna_calibration_initiate.html) VI again.

Computed error-correction terms will be saved to calset in memory for the signal specified in Selector String input. If you specify Calset Name, error-correction terms will also be saved to the specified calset and made available globally for use by all signals.

[IMAGE alt='RFmxVNA Calibration Save' src='rfmxvna_calibration_save.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Calset Name specifies the name of the calset. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_add_calibration_element.html language=enus -->
## TOPIC 00028: RFmxVNA Calkit Manager Calkit Add Calibration Element (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_add_calibration_element.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_add_calibration_element.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Add Calibration Element (VI)

Owning Palette:

Calkit

Adds a new Calibration Element with a user defined Calibration Element ID to the Calkit. The user defined Calibration Element ID has to be unique among all Calibration Elements in the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Add Calibration Element' src='rfmxvna_calkit_manager_calkit_add_calibration_element.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | Calibration Element ID specifies the ID of the Calibration Element within the Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_add_connector.html language=enus -->
## TOPIC 00029: RFmxVNA Calkit Manager Calkit Add Connector (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_add_connector.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_add_connector.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Add Connector (VI)

Owning Palette:

Calkit

Adds a new Connector with a user defined Connector ID to the Calkit. The user defined Connector ID has to be unique among all Connectors in the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Add Connector' src='rfmxvna_calkit_manager_calkit_add_connector.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | Connector ID specifies the ID of the Connector within the Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_delay_model_get_delay.html language=enus -->
## TOPIC 00030: RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_delay_model_get_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_delay_model_get_delay.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay (VI)

Owning Palette:

Delay Model

Returns the Delay of a Calibration Element defined by the Delay Model.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Get Delay' src='rfmxvna_calkit_manager_calkit_calibration_element_delay_model_get_delay.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Delay (s) returns the Delay of a Calibration Element defined by the Delay Model. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_delay_model_set_delay.html language=enus -->
## TOPIC 00031: RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Set Delay (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_delay_model_set_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_delay_model_set_delay.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Set Delay (VI)

Owning Palette:

Delay Model

Defines the Delay of a Calibration Element defined by the Delay Model.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Delay Model Set Delay' src='rfmxvna_calkit_manager_calkit_calibration_element_delay_model_set_delay.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Delay (s) specifies the Delay of a Calibration Element defined by the Delay Model. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_description.html language=enus -->
## TOPIC 00032: RFmxVNA Calkit Manager Calkit Calibration Element Get Description (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_description.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Get Description (VI)

Owning Palette:

Calibration Element

Returns the description for a Calibration Element of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Get Description' src='rfmxvna_calkit_manager_calkit_calibration_element_get_description.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Description returns the description for a Calibration Element of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_maximum_frequency.html language=enus -->
## TOPIC 00033: RFmxVNA Calkit Manager Calkit Calibration Element Get Maximum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_maximum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_maximum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Get Maximum Frequency (VI)

Owning Palette:

Calibration Element

Returns the Maximum Frequency of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Get Maximum Frequency' src='rfmxvna_calkit_manager_calkit_calibration_element_get_maximum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Maximum Frequency (Hz) returns the Maximum Frequency of the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_minimum_frequency.html language=enus -->
## TOPIC 00034: RFmxVNA Calkit Manager Calkit Calibration Element Get Minimum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_minimum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_minimum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Get Minimum Frequency (VI)

Owning Palette:

Calibration Element

Returns the Minimum Frequency of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Get Minimum Frequency' src='rfmxvna_calkit_manager_calkit_calibration_element_get_minimum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Minimum Frequency (Hz) returns the Minimum Frequency of the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_port_connectors.html language=enus -->
## TOPIC 00035: RFmxVNA Calkit Manager Calkit Calibration Element Get Port Connectors (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_port_connectors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_port_connectors.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Get Port Connectors (VI)

Owning Palette:

Calibration Element

Returns the array of Connectors associated with the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Get Port Connectors' src='rfmxvna_calkit_manager_calkit_calibration_element_get_port_connectors.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Connector IDs returns the array of Connectors associated with the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_s-parameter_definition.html language=enus -->
## TOPIC 00036: RFmxVNA Calkit Manager Calkit Calibration Element Get S-Parameter Definition (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_s-parameter_definition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_s-parameter_definition.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Get S-Parameter Definition (VI)

Owning Palette:

Calibration Element

Returns the S-Parameter definition of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Get S-Parameter Definition' src='rfmxvna_calkit_manager_calkit_calibration_element_get_s-parameter_definition.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S-Parameter Definition returns the S-Parameter definition of the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_types.html language=enus -->
## TOPIC 00037: RFmxVNA Calkit Manager Calkit Calibration Element Get Types (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_get_types.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Get Types (VI)

Owning Palette:

Calibration Element

Returns the type(s) of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Get Types' src='rfmxvna_calkit_manager_calkit_calibration_element_get_types.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calibration Element Types returns the type(s) of the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c0.html language=enus -->
## TOPIC 00038: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C0 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c0.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C0 (VI)

Owning Palette:

Reflect Model

Returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C0' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c0.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | C0 (F or H) returns the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c1.html language=enus -->
## TOPIC 00039: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C1 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c1.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C1 (VI)

Owning Palette:

Reflect Model

Returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C1' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c1.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | C1 (F or H) returns the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c2.html language=enus -->
## TOPIC 00040: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c2.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2 (VI)

Owning Palette:

Reflect Model

Returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C2' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c2.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | C2 (F or H) returns the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c3.html language=enus -->
## TOPIC 00041: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C3 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c3.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C3 (VI)

Owning Palette:

Reflect Model

Returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get C3' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_c3.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | C3 (F or H) returns the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_model_type.html language=enus -->
## TOPIC 00042: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Model Type (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_model_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_model_type.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Model Type (VI)

Owning Palette:

Reflect Model

Returns the model type of of the 1-port reflect standard.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Model Type' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_model_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Model Type returns the model type of of the 1-port reflect standard. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_delay.html language=enus -->
## TOPIC 00043: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Delay (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_delay.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Delay (VI)

Owning Palette:

Reflect Model

Returns the offset delay.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Delay' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_delay.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Offset Delay (s) returns the offset delay. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_loss.html language=enus -->
## TOPIC 00044: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Loss (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_loss.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_loss.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Loss (VI)

Owning Palette:

Reflect Model

Returns the offset loss.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Loss' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_loss.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Offset Loss (dB) returns the offset loss. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_z0.html language=enus -->
## TOPIC 00045: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Z0 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_z0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_z0.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Z0 (VI)

Owning Palette:

Reflect Model

Returns the impedance of the offset.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Offset Z0' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_offset_z0.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_reference_impedance.html language=enus -->
## TOPIC 00046: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Reference Impedance (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_reference_impedance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_reference_impedance.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Reference Impedance (VI)

Owning Palette:

Reflect Model

Returns the reference impedance.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get Reference Impedance' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_reference_impedance.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Reference Impedance (Ohm) returns the reference impedance. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_s-param_availability.html language=enus -->
## TOPIC 00047: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get S-Param Availability (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_s-param_availability.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_s-param_availability.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get S-Param Availability (VI)

Owning Palette:

Reflect Model

Returns the S-Parameter availability.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Get S-Param Availability' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_get_s-param_availability.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S-Parameter Availability returns the S-Parameter availability. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c0.html language=enus -->
## TOPIC 00048: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C0 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c0.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C0 (VI)

Owning Palette:

Reflect Model

Specifies the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C0' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c0.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | C0 (F or H) specifies the 0th order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c1.html language=enus -->
## TOPIC 00049: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C1 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c1.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c1.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C1 (VI)

Owning Palette:

Reflect Model

Specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C1' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c1.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | C1 (F or H) specifies the 1st order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c2.html language=enus -->
## TOPIC 00050: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C2 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c2.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C2 (VI)

Owning Palette:

Reflect Model

Specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C2' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c2.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | C2 (F or H) specifies the 2nd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c3.html language=enus -->
## TOPIC 00051: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C3 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c3.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C3 (VI)

Owning Palette:

Reflect Model

Specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set C3' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_c3.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | C3 (F or H) specifies the 3rd order coefficient of the 3rd order polynomial capacitance/inductance model for the Reflect Open/Reflect Short model type. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_model_type.html language=enus -->
## TOPIC 00052: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Model Type (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_model_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_model_type.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Model Type (VI)

Owning Palette:

Reflect Model

Specifies the model type of the 1-port reflect standard.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Model Type' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_model_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Model Type specifies the model type of of the 1-port reflect standard. Reflect Open (0) Models an Offset Open by specifying the offset parameters and the parameters of the Open (3rd order polynomial model of the capacitance). Reflect Short (1) Models an Offset Short by specifying the offset parameters and the parameters of the short (3rd order polynomial model of the inductance). Load (2) Models an Offset Load by specifying the offset parameters. |
| Reflect Open (0) | Models an Offset Open by specifying the offset parameters and the parameters of the Open (3rd order polynomial model of the capacitance). |
| Reflect Short (1) | Models an Offset Short by specifying the offset parameters and the parameters of the short (3rd order polynomial model of the inductance). |
| Load (2) | Models an Offset Load by specifying the offset parameters. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_delay.html language=enus -->
## TOPIC 00053: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Delay (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_delay.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_delay.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Delay (VI)

Owning Palette:

Reflect Model

Specifies the offset delay.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Delay' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_delay.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Offset Delay (s) specifies the offset delay. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_loss.html language=enus -->
## TOPIC 00054: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Loss (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_loss.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_loss.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Loss (VI)

Owning Palette:

Reflect Model

Specifies the offset loss.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Loss' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_loss.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Offset Loss (dB) specifes the offset loss. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_z0.html language=enus -->
## TOPIC 00055: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Z0 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_z0.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_z0.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Z0 (VI)

Owning Palette:

Reflect Model

Specifies the impedance of the offset.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Offset Z0' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_offset_z0.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Offset Z0 (Ohm) specifies the impedance of the offset. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_reference_impedance.html language=enus -->
## TOPIC 00056: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Reference Impedance (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_reference_impedance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_reference_impedance.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Reference Impedance (VI)

Owning Palette:

Reflect Model

Specifies the reference impedance.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set Reference Impedance' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_reference_impedance.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Reference Impedance (Ohm) specifies the reference impedance. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_s-param_availability.html language=enus -->
## TOPIC 00057: RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_s-param_availability.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_s-param_availability.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability (VI)

Owning Palette:

Reflect Model

Specifies the S-Parameter availability.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Reflect Model Set S-Param Availability' src='rfmxvna_calkit_manager_calkit_calibration_element_reflect_model_set_s-param_availability.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S-Parameter Availability specifies the S-Parameter availability. Estimate (0) S-Parameters treated as roughly known. Known (1) S-Parameters treated as exactly known. |
| Estimate (0) | S-Parameters treated as roughly known. |
| Known (1) | S-Parameters treated as exactly known. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_frequency.html language=enus -->
## TOPIC 00058: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get Frequency (VI)

Owning Palette:

S-Parameter

Returns the frequency array for the S-Parameter definition of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get Frequency' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Frequency (Hz) returns the frequency array for the S-Parameter definition of the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s-param_availability.html language=enus -->
## TOPIC 00059: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s-param_availability.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s-param_availability.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability (VI)

Owning Palette:

S-Parameter

Returns the S-Parameter availability.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s-param_availability.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S-Parameter Availability returns the S-Parameter availability. Estimate (0) S-Parameters treated as roughly known. Known (1) S-Parameters treated as exactly known. |
| Estimate (0) | S-Parameters treated as roughly known. |
| Known (1) | S-Parameters treated as exactly known. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s11.html language=enus -->
## TOPIC 00060: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S11 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s11.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s11.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S11 (VI)

Owning Palette:

S-Parameter

Returns the S11 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S11' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s11.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S11 returns the S11 S-Parameter for the calibration element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s12.html language=enus -->
## TOPIC 00061: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S12 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s12.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s12.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S12 (VI)

Owning Palette:

S-Parameter

Returns the S12 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S12' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s12.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S12 returns the S12 S-Parameter for the calibration element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s21.html language=enus -->
## TOPIC 00062: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S21 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s21.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s21.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S21 (VI)

Owning Palette:

S-Parameter

Returns the S21 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S21' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s21.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S21 returns the S21 S-Parameter for the calibration element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s22.html language=enus -->
## TOPIC 00063: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S22 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s22.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s22.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S22 (VI)

Owning Palette:

S-Parameter

returns the S22 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S22' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_get_s22.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | S22 returns the S22 S-Parameter for the calibration element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_frequency.html language=enus -->
## TOPIC 00064: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency (VI)

Owning Palette:

S-Parameter

Defines the frequency array for the S-Parameter definition of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Frequency (Hz) specifies the frequency array for the S-Parameter definition of the Calibration Element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_from_file.html language=enus -->
## TOPIC 00065: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_from_file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_from_file.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File (VI)

Owning Palette:

S-Parameter

Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_from_file.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | File Name specifies the touchstone file name. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s-param_availability.html language=enus -->
## TOPIC 00066: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S-Param Availability (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s-param_availability.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s-param_availability.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S-Param Availability (VI)

Owning Palette:

S-Parameter

Defines the S-Parameter availability.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S-Param Availability' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s-param_availability.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S-Parameter Availability specifies the S-Parameter availability. Estimate (0) S-Parameters treated as roughly known. Known (1) S-Parameters treated as exactly known. |
| Estimate (0) | S-Parameters treated as roughly known. |
| Known (1) | S-Parameters treated as exactly known. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s11.html language=enus -->
## TOPIC 00067: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S11 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s11.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s11.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S11 (VI)

Owning Palette:

S-Parameter

Sets the S11 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S11' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s11.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S11 specifies the S11 S-Parameter for the calibration element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s12.html language=enus -->
## TOPIC 00068: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s12.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s12.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12 (VI)

Owning Palette:

S-Parameter

Sets the S12 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s12.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S12 specifies the S12 S-Parameter for the calibration element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s21.html language=enus -->
## TOPIC 00069: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S21 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s21.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s21.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S21 (VI)

Owning Palette:

S-Parameter

Sets the S21 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S21' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s21.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S21 specifies the S21 S-Parameter for the calibration element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s22.html language=enus -->
## TOPIC 00070: RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S22 (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s22.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s22.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S22 (VI)

Owning Palette:

S-Parameter

Sets the S22 S-Parameter for the calibration element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S22' src='rfmxvna_calkit_manager_calkit_calibration_element_s-parameter_set_s22.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S22 specifies the S22 S-Parameter for the calibration element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_description.html language=enus -->
## TOPIC 00071: RFmxVNA Calkit Manager Calkit Calibration Element Set Description (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_description.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Set Description (VI)

Owning Palette:

Calibration Element

Sets the description for a Calibration Element of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Set Description' src='rfmxvna_calkit_manager_calkit_calibration_element_set_description.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Description specifies the description for a Calibration Element of a specific Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_maximum_frequency.html language=enus -->
## TOPIC 00072: RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_maximum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_maximum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency (VI)

Owning Palette:

Calibration Element

Sets the Maximum Frequency of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Set Maximum Frequency' src='rfmxvna_calkit_manager_calkit_calibration_element_set_maximum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Maximum Frequency (Hz) specifies the Maximum Frequency of the Calibration Element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_minimum_frequency.html language=enus -->
## TOPIC 00073: RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_minimum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_minimum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency (VI)

Owning Palette:

Calibration Element

Sets the Minimum Frequency of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Set Minimum Frequency' src='rfmxvna_calkit_manager_calkit_calibration_element_set_minimum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Minimum Frequency (Hz) specifies the Minimum Frequency of the Calibration Element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_port_connectors.html language=enus -->
## TOPIC 00074: RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_port_connectors.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_port_connectors.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors (VI)

Owning Palette:

Calibration Element

Defines the connectors of the Calibration Element by providing an array of Connector IDs where the 1st array element refers to the connector of the 1st port of the Calibration element. The array size has to be equal to the number of ports of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Set Port Connectors' src='rfmxvna_calkit_manager_calkit_calibration_element_set_port_connectors.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Connector IDs specifies the array of Connectors associated with the Calibration Element. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_s-parameter_definition.html language=enus -->
## TOPIC 00075: RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_s-parameter_definition.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_s-parameter_definition.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition (VI)

Owning Palette:

Calibration Element

Defines the way how the S-Parameters of the Calibration Element are specified.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Set S-Parameter Definition' src='rfmxvna_calkit_manager_calkit_calibration_element_set_s-parameter_definition.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | S-Parameter Definition specifies the S-Parameter definition of the Calibration Element. Reflect Model (0) S-Parameters defined by the Reflect model (1-port). Sparameter (1) S-Parameters defined by a S-Parameter list (1-port and 2-port). Delay Model (2) S-Parameters defined by a delay model (2-port). Unknown (3) S-Parameters not further specified. |
| Reflect Model (0) | S-Parameters defined by the Reflect model (1-port). |
| Sparameter (1) | S-Parameters defined by a S-Parameter list (1-port and 2-port). |
| Delay Model (2) | S-Parameters defined by a delay model (2-port). |
| Unknown (3) | S-Parameters not further specified. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_types.html language=enus -->
## TOPIC 00076: RFmxVNA Calkit Manager Calkit Calibration Element Set Types (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_types.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_calibration_element_set_types.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Calibration Element Set Types (VI)

Owning Palette:

Calibration Element

Sets the type(s) of the Calibration Element.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Calibration Element Set Types' src='rfmxvna_calkit_manager_calkit_calibration_element_set_types.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string created by this VI. The selector string comprises of the Calkit ID and the Calibration Element ID. Example: "ckit::MyCkitID/calel::MyCalelID" You can use the RFmxVNA Build Calibration Element String VI to build the selector string. |
|  | Calibration Element Types specifies the type(s) of the Calibration Element. Unknown (0) Load (1) Open (2) Short (3) Line (4) Reflect (5) Termination (6) Thru (7) |
| Unknown (0) |  |
| Load (1) |  |
| Open (2) |  |
| Short (3) |  |
| Line (4) |  |
| Reflect (5) |  |
| Termination (6) |  |
| Thru (7) |  |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_description.html language=enus -->
## TOPIC 00077: RFmxVNA Calkit Manager Calkit Connector Get Description (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_description.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Get Description (VI)

Owning Palette:

Connector

Returns the description of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Get Description' src='rfmxvna_calkit_manager_calkit_connector_get_description.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Description |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_gender.html language=enus -->
## TOPIC 00078: RFmxVNA Calkit Manager Calkit Connector Get Gender (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_gender.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_gender.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Get Gender (VI)

Owning Palette:

Connector

Returns the Gender of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Get Gender' src='rfmxvna_calkit_manager_calkit_connector_get_gender.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Connector Gender returns the Gender of a Connector of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_impedance.html language=enus -->
## TOPIC 00079: RFmxVNA Calkit Manager Calkit Connector Get Impedance (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_impedance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_impedance.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Get Impedance (VI)

Owning Palette:

Connector

Returns the Impedance of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Get Impedance' src='rfmxvna_calkit_manager_calkit_connector_get_impedance.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Impedance (Ohm) returns the Impedance of a Connector of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_maximum_frequency.html language=enus -->
## TOPIC 00080: RFmxVNA Calkit Manager Calkit Connector Get Maximum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_maximum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_maximum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Get Maximum Frequency (VI)

Owning Palette:

Connector

Returns the Maximum Frequency of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Get Maximum Frequency' src='rfmxvna_calkit_manager_calkit_connector_get_maximum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Maximum Frequency (Hz) returns the Maximum Frequency of a Connector of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_minimum_frequency.html language=enus -->
## TOPIC 00081: RFmxVNA Calkit Manager Calkit Connector Get Minimum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_minimum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_minimum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Get Minimum Frequency (VI)

Owning Palette:

Connector

Returns the Minimum Frequency of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Get Minimum Frequency' src='rfmxvna_calkit_manager_calkit_connector_get_minimum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Minimum Frequency (Hz) returns the Minimum Frequency of a Connector of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_type.html language=enus -->
## TOPIC 00082: RFmxVNA Calkit Manager Calkit Connector Get Type (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_get_type.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Get Type (VI)

Owning Palette:

Connector

Returns the Type of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Get Type' src='rfmxvna_calkit_manager_calkit_connector_get_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Connector Type returns the Type of a Connector of a specific Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_description.html language=enus -->
## TOPIC 00083: RFmxVNA Calkit Manager Calkit Connector Set Description (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_description.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Set Description (VI)

Owning Palette:

Connector

Sets the description for a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Set Description' src='rfmxvna_calkit_manager_calkit_connector_set_description.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | Description specifies the description for a Connector of a specific Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_gender.html language=enus -->
## TOPIC 00084: RFmxVNA Calkit Manager Calkit Connector Set Gender (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_gender.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_gender.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Set Gender (VI)

Owning Palette:

Connector

Sets the Gender of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Set Gender' src='rfmxvna_calkit_manager_calkit_connector_set_gender.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | Connector Gender specifies the Gender of a Connector of a specific Calkit. Male (0) Female (1) NoGender (2) |
| Male (0) |  |
| Female (1) |  |
| NoGender (2) |  |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_impedance.html language=enus -->
## TOPIC 00085: RFmxVNA Calkit Manager Calkit Connector Set Impedance (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_impedance.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_impedance.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Set Impedance (VI)

Owning Palette:

Connector

Sets the Impedance of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Set Impedance' src='rfmxvna_calkit_manager_calkit_connector_set_impedance.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | Impedance (Ohm) specifies the Impedance of a Connector of a specific Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_maximum_frequency.html language=enus -->
## TOPIC 00086: RFmxVNA Calkit Manager Calkit Connector Set Maximum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_maximum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_maximum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Set Maximum Frequency (VI)

Owning Palette:

Connector

Sets the Maximum Frequency of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Set Maximum Frequency' src='rfmxvna_calkit_manager_calkit_connector_set_maximum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | Maximum Frequency (Hz) specifies the Maximum Frequency of a Connector of a specific Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_minimum_frequency.html language=enus -->
## TOPIC 00087: RFmxVNA Calkit Manager Calkit Connector Set Minimum Frequency (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_minimum_frequency.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_minimum_frequency.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Set Minimum Frequency (VI)

Owning Palette:

Connector

Sets the Minimum Frequency of a Connector of a specific Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Set Minimum Frequency' src='rfmxvna_calkit_manager_calkit_connector_set_minimum_frequency.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | Minimum Frequency (Hz) specifies the Minimum Frequency of a Connector of a specific Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_type.html language=enus -->
## TOPIC 00088: RFmxVNA Calkit Manager Calkit Connector Set Type (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_connector_set_type.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Connector Set Type (VI)

Owning Palette:

Connector

Sets the Type of a Connector of a specific Calkit. Connector type is a user defined string (for example 'SMA', '1.8mm', etc.).

[IMAGE alt='RFmxVNA Calkit Manager Calkit Connector Set Type' src='rfmxvna_calkit_manager_calkit_connector_set_type.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies the selector string to address a specific Connector within a Calkit. The selector string comprises of the Calkit ID and the Connector ID. Example: "ckit::MyCkitID/conn::MyConnID" You can use the RFmxVNA Build Connector String VI to build the selector string. |
|  | Connector Type specifies the Type of a Connector of a specific Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_get_calibration_element_ids.html language=enus -->
## TOPIC 00089: RFmxVNA Calkit Manager Calkit Get Calibration Element IDs (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_get_calibration_element_ids.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_get_calibration_element_ids.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Get Calibration Element IDs (VI)

Owning Palette:

Calkit

Returns a list of Calibration Element IDs of all Calibration Elements of the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Get Calibration Element IDs' src='rfmxvna_calkit_manager_calkit_get_calibration_element_ids.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calibration Element IDs returns the list of Calibration Element IDs of all Calibration Elements of the Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_get_connector_ids.html language=enus -->
## TOPIC 00090: RFmxVNA Calkit Manager Calkit Get Connector IDs (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_get_connector_ids.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_get_connector_ids.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Get Connector IDs (VI)

Owning Palette:

Calkit

Returns the list of Connector IDs for all connectors in the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Get Connector IDs' src='rfmxvna_calkit_manager_calkit_get_connector_ids.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Connector IDs returns the list of Connector IDs for all connectors in the Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_get_description.html language=enus -->
## TOPIC 00091: RFmxVNA Calkit Manager Calkit Get Description (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_get_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_get_description.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Get Description (VI)

Owning Palette:

Calkit

Returns the description of the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Get Description' src='rfmxvna_calkit_manager_calkit_get_description.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calkit Description returns the description of the Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_get_version.html language=enus -->
## TOPIC 00092: RFmxVNA Calkit Manager Calkit Get Version (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_get_version.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_get_version.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Get Version (VI)

Owning Palette:

Calkit

Returns the version string of the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Get Version' src='rfmxvna_calkit_manager_calkit_get_version.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calkit Version returns the version string of the Calkit. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_remove_calibration_element.html language=enus -->
## TOPIC 00093: RFmxVNA Calkit Manager Calkit Remove Calibration Element (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_remove_calibration_element.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_remove_calibration_element.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Remove Calibration Element (VI)

Owning Palette:

Calkit

Removes the Calibration Element identified by its Calibration Element ID from the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Remove Calibration Element' src='rfmxvna_calkit_manager_calkit_remove_calibration_element.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | Calibration Element ID specifies the ID of the Calibration Element within the Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_remove_connector.html language=enus -->
## TOPIC 00094: RFmxVNA Calkit Manager Calkit Remove Connector (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_remove_connector.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_remove_connector.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Remove Connector (VI)

Owning Palette:

Calkit

Removes a Connector element from the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Remove Connector' src='rfmxvna_calkit_manager_calkit_remove_connector.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | Connector ID specifies the ID of the Connector within the Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_set_description.html language=enus -->
## TOPIC 00095: RFmxVNA Calkit Manager Calkit Set Description (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_set_description.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_set_description.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Set Description (VI)

Owning Palette:

Calkit

Sets the description for the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Set Description' src='rfmxvna_calkit_manager_calkit_set_description.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | Calkit Description specifies the description of the Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_calkit_set_version.html language=enus -->
## TOPIC 00096: RFmxVNA Calkit Manager Calkit Set Version (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_calkit_set_version.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_calkit_set_version.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Calkit Set Version (VI)

Owning Palette:

Calkit

Sets the version string for the Calkit.

[IMAGE alt='RFmxVNA Calkit Manager Calkit Set Version' src='rfmxvna_calkit_manager_calkit_set_version.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the Calkit ID. Example: "ckit::MyCkitID" You can use the RFmxVNA Build Calkit String VI to build the selector string. |
|  | Calkit Version specifies the version string of the Calkit. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_create_calkit.html language=enus -->
## TOPIC 00097: RFmxVNA Calkit Manager Create Calkit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_create_calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_create_calkit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Create Calkit (VI)

Owning Palette:

Calkit Manager

Creates a new empty Calkit with the user defined Calkit ID in Calkit Manager. The user defined Calkit ID has to be unique among all Calkits in Calkit Manager.

[IMAGE alt='RFmxVNA Calkit Manager Create Calkit' src='rfmxvna_calkit_manager_create_calkit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Calkit ID specifies the ID for the Calkit in Calkit Manager. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_delete_calkit.html language=enus -->
## TOPIC 00098: RFmxVNA Calkit Manager Delete Calkit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_delete_calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_delete_calkit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Delete Calkit (VI)

Owning Palette:

Calkit Manager

Removes a Calkit from Calkit Manager and deletes the corresponding file, if it exists.

[IMAGE alt='RFmxVNA Calkit Manager Delete Calkit' src='rfmxvna_calkit_manager_delete_calkit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Calkit ID specifies the ID for the Calkit in Calkit Manager. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_export_calkit.html language=enus -->
## TOPIC 00099: RFmxVNA Calkit Manager Export Calkit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_export_calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_export_calkit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Export Calkit (VI)

Owning Palette:

Calkit Manager

Exports a Calkit to file.

[IMAGE alt='RFmxVNA Calkit Manager Export Calkit' src='rfmxvna_calkit_manager_export_calkit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Calkit ID specifies the ID for the Calkit in Calkit Manager. |
|  | Calkit File Path specifies the absoulte path to the calkit file (.nckt). |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_get_calkit_ids.html language=enus -->
## TOPIC 00100: RFmxVNA Calkit Manager Get Calkit IDs (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_get_calkit_ids.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_get_calkit_ids.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Get Calkit IDs (VI)

Owning Palette:

Fetch

Returns a list of Calkit IDs for all Calkits currently loaded in Calkit Manager.

[IMAGE alt='RFmxVNA Calkit Manager Get Calkit IDs' src='rfmxvna_calkit_manager_get_calkit_ids.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calkit IDs returns the list of Calkit IDs for all Calkit files currently loaded in Calkit Manager. |
|  | error in describes error conditions that occur before this node runs. |
|  | error out returns error information. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_import_calkit.html language=enus -->
## TOPIC 00101: RFmxVNA Calkit Manager Import Calkit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_import_calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_import_calkit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Import Calkit (VI)

Owning Palette:

Calkit Manager

Imports a Calkit file into the Calkit Manager.

[IMAGE alt='RFmxVNA Calkit Manager Import Calkit' src='rfmxvna_calkit_manager_import_calkit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calkit File Path specifies the absoulte path to the calkit file (.nckt). |
|  | error in describes error conditions that occur before this node runs. |
|  | error out returns error information. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_remove_calkit.html language=enus -->
## TOPIC 00102: RFmxVNA Calkit Manager Remove Calkit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_remove_calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_remove_calkit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Remove Calkit (VI)

Owning Palette:

Calkit Manager

Removes a Calkit from Calkit Manager.

[IMAGE alt='RFmxVNA Calkit Manager Remove Calkit' src='rfmxvna_calkit_manager_remove_calkit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Calkit ID specifies the ID for the Calkit in Calkit Manager. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calkit_manager_validate_calkit.html language=enus -->
## TOPIC 00103: RFmxVNA Calkit Manager Validate Calkit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calkit_manager_validate_calkit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calkit_manager_validate_calkit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calkit Manager Validate Calkit (VI)

Owning Palette:

Calkit Manager

Validates the consistency of a Calkit definition and returns the status of the validation.

[IMAGE alt='RFmxVNA Calkit Manager Validate Calkit' src='rfmxvna_calkit_manager_validate_calkit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Calkit ID specifies the ID for the Calkit in Calkit Manager. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calset_embed_fixture_(s2p).html language=enus -->
## TOPIC 00104: RFmxVNA Calset Embed Fixture (s2p) (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calset_embed_fixture_(s2p).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calset_embed_fixture_(s2p).html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calset Embed Fixture (s2p) (VI)

Embeds the inverse of a given fixture network into a Calset in memory.
The typical use case for this utility is to remove the effect of an adapter that was present during calibration but is not present during later measurements from the Calset itself such that corrected measurements can be performed without considering the calibration adapter in the measurement deembedding.

The fixture network must be known and the fixture S-parameters have to be provided as s2p-file.

A potential flip of the fixture network with respect to its S-parameter definitions can be configured by the ‘S-Parameter Orientation’.

The operation applies to one VNA port at a time, specified by ‘VNA Port’ parameter.

Depending on the parameter ‘New Calset Name’, a new Calset will be created or the input Calset itself will be updated.

You cannot specify both signal name in Selector String and Calset Name together.

If you specify ‘New Calset Name’ input, a new global calset will be created from original calset specified by Calset Name input and modified with embedding data. If you do not specify ‘New Calset Name’ input, the original calset itself will be modified with embedding data.

If you do not specify both signal name in Selector String and Calset Name, original calset refers to in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, original calset refers to in memory calset of the specified signal instance. If you specify only Calset Name, original calset refers to the global calset with the specified Calset Name.

[IMAGE alt='RFmxVNA Calset Embed Fixture (s2p)' src='rfmxvna_calset_embed_fixture_(s2p).gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Calset Name specifies the name of the calset. |
|  | VNA Port specifies the port name of the Calset VNA port. |
|  | S-Parameter Orientation specifies the orientation of the configured fixture network with respect to VNA port. Port1 Towards VNA (0) Specifies that port1 of the fixture is towards VNA port. Port2 Towards VNA (1) Specifies that port2 of the fixture is towards VNA port. |
| Port1 Towards VNA (0) | Specifies that port1 of the fixture is towards VNA port. |
| Port2 Towards VNA (1) | Specifies that port2 of the fixture is towards VNA port. |
|  | New Calset Name specifies the name under which the result Calset (with updated error coefficients) is to be saved. If empty string is provided, the updated Calset is saved back into the original Calset. That is, the original Calset is overwritten. |
|  | Fixture s2p File Path Specifies the path to the s2p file containing the fixture S-parameters. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calset_get_error_term.html language=enus -->
## TOPIC 00105: RFmxVNA Calset Get Error Term (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calset_get_error_term.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calset_get_error_term.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calset Get Error Term (VI)

Owning Palette:

Calset

Returns a specific error term from the Calset.

You cannot specify both signal name in Selector String and Calset Name together.

If you do not specify both signal name in Selector String and Calset Name, the error term will be returned from in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the error term will be returned from in memory calset of the specified signal instance. If you specify only Calset Name, the error term will returned from the global calset with the specified calset name.

|  | Note You can call this VI only after you call the RFmxVNA Calibration Save VI. |
| --- | --- |

[IMAGE alt='RFmxVNA Calset Get Error Term' src='rfmxvna_calset_get_error_term.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calset Name specifies the name of the calset. |
|  | Error Term Identifier specifies the type of error term in the calset. The error term can take the following values: Directivity (0) Directivity measured at Measurement Port (Source Port ignored). Source Match (1) Source Match measured at Measurement Port (Source Port ignored). Reflection Tracking (2) Reflection Tracking measured at Measurement Port (Source Port ignored). Transmission Tracking (3) Transmission Tracking measured at Measurement Port with Source Port being the source port. Load Match (4) Load Match measured at Measurement Port with Source Port being the source port. K (5) K measured at Measurement Port (Source Port ignored). alpha (6) alpha measured at Measurement Port (Source Port ignored). beta (7) beta measured at Measurement Port (Source Port ignored). gamma (8) gamma measured at Measurement Port (Source Port ignored). delta (9) delta measured at Measurement Port (Source Port ignored). Switch Term (10) Switch term measured at Measurement Port (Source Port ignored). The error term K, alpha, beta, gamma, and delta describe the relation of the outgoing and incident waves at the calibration plane (waves a and b) and the waves measured at VNA reference and measurement receiver (waves r and s) by the following matrix equation: + + + ++ + ¦ a ¦ ¦ alpha beta ¦¦ r ¦ ¦ ¦ = K * ¦ ¦¦ ¦ ¦ b ¦ ¦ gamma delta ¦¦ s ¦ + + + ++ + , where alpha, beta, gamma, and delta represent the complex elements of a transmission matrix and K represents a complex scaling factor. |
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
|  | Measurement Port specifies the VNA port name corresponding to the Error Term you queried. |
|  | Source Port specifies the VNA port name for which the Error Term is queried. This parameter is only required to query Error Term defined by port pairs. The valid values of the parameter Error Term Identifier defined for port pairs are Transmission Tracking and Load Match. |
|  | Error Term returns the computed error term from the calset. |
|  | error in describes error conditions that occur before this node runs. |
|  | error out returns error information. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calset_get_frequency_grid.html language=enus -->
## TOPIC 00106: RFmxVNA Calset Get Frequency Grid (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calset_get_frequency_grid.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calset_get_frequency_grid.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calset Get Frequency Grid (VI)

Owning Palette:

Calset

Returns the calibration frequency grid from the Calset.

You cannot specify both signal name in Selector String and Calset Name together.

If you do not specify both signal name in Selector String and Calset Name, the frequency grid will be returned from in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the frequency grid will be returned from in memory calset of the specified signal instance. If you specify only Calset Name, the frequency grid will returned from the global calset with the specified calset name.

|  | Note You can call this VI only after you call the RFmxVNA Calibration Save VI. |
| --- | --- |

[IMAGE alt='RFmxVNA Calset Get Frequency Grid' src='rfmxvna_calset_get_frequency_grid.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Calset Name specifies the name of the calset. |
|  | Error Term Identifier specifies the type of error term in the calset. The error term can take the following values: Directivity (0) Directivity measured at Measurement Port (Source Port ignored). Source Match (1) Source Match measured at Measurement Port (Source Port ignored). Reflection Tracking (2) Reflection Tracking measured at Measurement Port (Source Port ignored). Transmission Tracking (3) Transmission Tracking measured at Measurement Port with Source Port being the source port. Load Match (4) Load Match measured at Measurement Port with Source Port being the source port. K (5) K measured at Measurement Port (Source Port ignored). alpha (6) alpha measured at Measurement Port (Source Port ignored). beta (7) beta measured at Measurement Port (Source Port ignored). gamma (8) gamma measured at Measurement Port (Source Port ignored). delta (9) delta measured at Measurement Port (Source Port ignored). Switch Term (10) Switch term measured at Measurement Port (Source Port ignored). The error term K, alpha, beta, gamma, and delta describe the relation of the outgoing and incident waves at the calibration plane (waves a and b) and the waves measured at VNA reference and measurement receiver (waves r and s) by the following matrix equation: + + + ++ + ¦ a ¦ ¦ alpha beta ¦¦ r ¦ ¦ ¦ = K * ¦ ¦¦ ¦ ¦ b ¦ ¦ gamma delta ¦¦ s ¦ + + + ++ + , where alpha, beta, gamma, and delta represent the complex elements of a transmission matrix and K represents a complex scaling factor. |
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
|  | Frequency Grid (Hz) returns the calibration frequency grid from the calset. This value is expressed in Hz. |
|  | error in describes error conditions that occur before this node runs. |
|  | error out returns error information. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calset_load_from_file.html language=enus -->
## TOPIC 00107: RFmxVNA Calset Load from File (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calset_load_from_file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calset_load_from_file.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calset Load from File (VI)

Owning Palette:

Calset

Loads error-correction terms you saved in a calset file (.ncst) using [RFmxVNA Calset Save to File](rfmxvna_calset_save_to_file.html) VI. If error-correction terms already exist for the RFmx Signal instance you specified using the Selector String input, RFmx will replace those correction terms.

You cannot specify both signal name in Selector String and Calset Name together.

If you do not specify both signal name in Selector String and Calset Name, the error term will be loaded from specified file to in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the error term will be loaded from specified file to in memory calset of the specified signal instance. If you specify only Calset Name, the error term will be loaded from specified file to the global calset with the specified calset name.

[IMAGE alt='RFmxVNA Calset Load from File' src='rfmxvna_calset_load_from_file.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Calset Name specifies the name of the calset. |
|  | Calset File Path specifies the complete path to the file with .ncst extension from which the calset is to be loaded. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_calset_save_to_file.html language=enus -->
## TOPIC 00108: RFmxVNA Calset Save to File (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_calset_save_to_file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_calset_save_to_file.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Calset Save to File (VI)

Owning Palette:

Calset

Saves the error-correction terms to a calset file (*.ncst). You can call this VI only after you call [RFmxVNA Calibration Save](rfmxvna_calibration_save.html) VI.

You cannot specify both signal name in Selector String and Calset Name together.

If you do not specify both signal name in Selector String and Calset Name, the error term will be saved to specified file from in memory calset of default signal instance. If you do not specify Calset Name but specify signal name in Selector String, the error term will be saved to specified file from in memory calset of the specified signal instance. If you specify only Calset Name, the error term will be saved to specified file from the global calset with the specified calset name.

[IMAGE alt='RFmxVNA Calset Save to File' src='rfmxvna_calset_save_to_file.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Calset File Path specifies the absolute path to the calset file (*.ncst). If the path you specified does not end with '.ncst' file extension, then RFmx automatically adds the extension before saving the file to disk. If the path you specify points to an already existing calset file, then RFmx overwrites that file without warning. |
|  | Calset Name specifies the name of the calset. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_check_measurement_status.html language=enus -->
## TOPIC 00109: RFmxVNA Check Measurement Status (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_check_measurement_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_check_measurement_status.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Check Measurement Status (VI)

Owning Palette:

Utility

Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available.

[IMAGE alt='RFmxVNA Check Measurement Status' src='rfmxvna_check_measurement_status.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |
|  | done? indicates whether the measurement is complete. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_clear_all_named_results.html language=enus -->
## TOPIC 00110: RFmxVNA Clear All Named Results (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_clear_all_named_results.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_clear_all_named_results.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Clear All Named Results (VI)

Owning Palette:

Advanced

Clears all results for the signal that you specify in the Selector String parameter.

[IMAGE alt='RFmxVNA Clear All Named Results' src='rfmxvna_clear_all_named_results.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_clear_calset.html language=enus -->
## TOPIC 00111: RFmxVNA Clear Calset (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_clear_calset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_clear_calset.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Clear Calset (VI)

Owning Palette:

Calset

Deletes the specified calset.

You cannot specify both signal name in Selector String and Calset Name together.

If you do not specify both signal name in Selector String and Calset Name, in memory calset of default signal instance will be deleted if active on the signal. If you do not specify Calset Name but specify signal name in Selector String, the in memory calset of the specified signal instance will be deleted if active on the signal. If you specify only Calset Name, the global calset with the specified calset name will be deleted.

[IMAGE alt='RFmxVNA Clear Calset' src='rfmxvna_clear_calset.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Calset Name specifies the name of the calset. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_clear_named_result.html language=enus -->
## TOPIC 00112: RFmxVNA Clear Named Result (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_clear_named_result.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_clear_named_result.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Clear Named Result (VI)

Owning Palette:

Advanced

Clears a result instance specified by the result name in the Selector String parameter.

[IMAGE alt='RFmxVNA Clear Named Result' src='rfmxvna_clear_named_result.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_clone_signal_configuration.html language=enus -->
## TOPIC 00113: RFmxVNA Clone Signal Configuration (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_clone_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_clone_signal_configuration.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Clone Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal by copying all the property values from an existing signal instance.

[IMAGE alt='RFmxVNA Clone Signal Configuration' src='rfmxvna_clone_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | New Signal Name specifies the name of the new signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::NewSigName" "NewSigName" |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Old Signal Name specifies the name of an existing signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::OldSigName" "OldSigName" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_commit.html language=enus -->
## TOPIC 00114: RFmxVNA Commit (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_commit.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_commit.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Commit (VI)

Owning Palette:

Utility

Commits settings to the hardware. Calling this VI is optional. RFmxVNA commits settings to the hardware when you call the [RFmxVNA Initiate](rfmxvna_initiate.html) VI.

[IMAGE alt='RFmxVNA Commit' src='rfmxvna_commit.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_configure_correction_port_subset.html language=enus -->
## TOPIC 00115: RFmxVNA Configure Correction Port Subset (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_configure_correction_port_subset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_configure_correction_port_subset.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Configure Correction Port Subset (VI)

Owning Palette:

Correction

Configures the subset of ports to be corrected when [Correction Port Subset Enabled](/csh?topicname=rfmxvnaprop/attrd0000e.html) property is set to **True**.

[IMAGE alt='RFmxVNA Configure Correction Port Subset' src='rfmxvna_configure_correction_port_subset.gif']

|  | Port Subset specifies subset of ports to be corrected as an array of port names. |
| --- | --- |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_configure_frequency_list_(start_stop_points).html language=enus -->
## TOPIC 00116: RFmxVNA Configure Frequency List (Start Stop Points) (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_configure_frequency_list_(start_stop_points).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_configure_frequency_list_(start_stop_points).html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Configure Frequency List (Start Stop Points) (VI)

Owning Palette:

Configuration

Configures the list of frequencies at which the measurement needs to be performed. The start frequency and stop frequency points are inclusive in the frequency list.

[IMAGE alt='RFmxVNA Configure Frequency List (Start Stop Points)' src='rfmxvna_configure_frequency_list_(start_stop_points).gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | Start Frequency (Hz) specifies the lowest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
|  | Stop Frequency (Hz) specifies the highest frequency at which the measurement needs to be performed. This value is expressed in Hz. |
|  | Number of Points specifies the number of frequency points at which the measurement needs to be performed. This value is expressed in Hz. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_copy_calset.html language=enus -->
## TOPIC 00117: RFmxVNA Copy Calset (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_copy_calset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_copy_calset.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Copy Calset (VI)

Owning Palette:

Calset

Copies the source calset data into the new calset specified. This VI will not change the source calset data.

You cannot specify both signal name in Selector String and Source Calset Name together.

If you do not specify both signal name in Selector String and Source Calset Name, calset data from in memory calset of default signal instance will be copied to New Calset. If you do not specify Source Calset Name but specify signal name in Selector String, the calset data from in memory calset of the specified signal instance will be copied to New Calset. If you specify only Source Calset Name, the calset data from the global calset with the specified Source calset name will be copied to New Calset.

[IMAGE alt='RFmxVNA Copy Calset' src='rfmxvna_copy_calset.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | New Calset Name specifies the name of the new calset to which calset data will be copied. |
|  | Source Calset Name specifies the name of the source calset from which calset data will be copied. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_create_signal_configuration.html language=enus -->
## TOPIC 00118: RFmxVNA Create Signal Configuration (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_create_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_create_signal_configuration.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Create Signal Configuration (VI)

Owning Palette:

Advanced

Creates a new instance of a signal. RFmxVNA Signal concept is same as Channel concept in third party software.

[IMAGE alt='RFmxVNA Create Signal Configuration' src='rfmxvna_create_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_delete_signal_configuration.html language=enus -->
## TOPIC 00119: RFmxVNA Delete Signal Configuration (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_delete_signal_configuration.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_delete_signal_configuration.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Delete Signal Configuration (VI)

Owning Palette:

Advanced

Deletes an instance of a signal that you specify in the Signal Name parameter.

[IMAGE alt='RFmxVNA Delete Signal Configuration' src='rfmxvna_delete_signal_configuration.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Signal Name specifies the signal name for building the selector string. This input accepts the signal name with or without the "signal::" prefix. The default value is "" (empty string). Example: "" "signal::sig1" "sig1" |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_deselect_active_calset.html language=enus -->
## TOPIC 00120: RFmxVNA Deselect Active Calset (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_deselect_active_calset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_deselect_active_calset.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Deselect Active Calset (VI)

Owning Palette:

Calset

Deselects the calset which is active for the signal instance you specified using the signal name in Selector String input. This VI will not delete in memory signal calset or global calset.

[IMAGE alt='RFmxVNA Deselect Active Calset' src='rfmxvna_deselect_active_calset.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_get_all_calset_names.html language=enus -->
## TOPIC 00121: RFmxVNA Get All Calset Names (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_get_all_calset_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_get_all_calset_names.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Get All Calset Names (VI)

Owning Palette:

Calset

Returns all the global calset names.

[IMAGE alt='RFmxVNA Get All Calset Names' src='rfmxvna_get_all_calset_names.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Calset Names returns all the calset names from the global calsets. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_get_all_named_result_names.html language=enus -->
## TOPIC 00122: RFmxVNA Get All Named Result Names (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_get_all_named_result_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_get_all_named_result_names.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Get All Named Result Names (VI)

Owning Palette:

Advanced

Returns all the named result names of the signal that you specify in the Selector String parameter.

[IMAGE alt='RFmxVNA Get All Named Result Names' src='rfmxvna_get_all_named_result_names.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | Result Names returns an array of result names. |
|  | Default Result Exists? indicates whether the default result exists. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_initiate.html language=enus -->
## TOPIC 00123: RFmxVNA Initiate (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_initiate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_initiate.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Initiate (VI)

Owning Palette:

RFmx VNA VIs

Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the [RFmxVNA Wait for Measurement Complete](rfmxvna_wait_for_measurement_complete.html) VI or [RFmxVNA Check Measurement Status](rfmxvna_check_measurement_status.html) VI.

[IMAGE alt='RFmxVNA Initiate' src='rfmxvna_initiate.gif']

|  | Result Name specifies the name to be associated with measurement results. Provide a unique name, such as "r1" to enable fetching of multiple measurement results and traces. This input accepts the result name with or without the "result::" prefix. The default value is "" (empty string), which refers to the default result instance. Example: "" "result::r1" "r1" |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_property_node.html language=enus -->
## TOPIC 00124: RFmxVNA Property Node (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_property_node.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Property Node (VI)

Owning Palette:

RFmx VNA VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmxVNA properties.

[IMAGE alt='RFmxVNA Property Node' src='rfmxvna_property_node.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_reset_to_default.html language=enus -->
## TOPIC 00125: RFmxVNA Reset to Default (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_reset_to_default.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Reset to Default (VI)

Owning Palette:

Utility

Resets a signal to the default values.

[IMAGE alt='RFmxVNA Reset to Default' src='rfmxvna_reset_to_default.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_select_active_calset.html language=enus -->
## TOPIC 00126: RFmxVNA Select Active Calset (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_select_active_calset.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_select_active_calset.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Select Active Calset (VI)

Owning Palette:

Calset

Activates the specified calset to the signal instance you specified using the Selector String input.

If you do not specify both signal name in Selector String and Calset Name,the in memory calset will be activated for default signal instance. If you do not specify Calset Name but specify signal name in Selector String, in memory calset will be activated for the specified signal instance. If you specify only Calset Name, the global calset with the specified calset name will be activated for the default signal instance. If you specify both signal name in Selector string and Calset Name, the global calset with the specified calset name will be activated for the specified signal instance.

You can use the [RFmxVNA Get All Calset Names](rfmxvna_get_all_calset_names.html) VI to get the list of available global calsets.

[IMAGE alt='RFmxVNA Select Active Calset' src='rfmxvna_select_active_calset.gif']

|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
| --- | --- |
|  | Calset Name specifies the name of the calset. |
|  | Restore Configuration specifies whether the stimulus settings from the specified calset should be applied to the signal. None (0) Do not apply the stimulus settings from the calset. Stimulus (1) Applies the stimulus settings from the calset. |
| None (0) | Do not apply the stimulus settings from the calset. |
| Stimulus (1) | Applies the stimulus settings from the calset. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_select_measurement.html language=enus -->
## TOPIC 00127: RFmxVNA Select Measurement (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_select_measurement.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_select_measurement.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Select Measurement (VI)

Owning Palette:

RFmx VNA VIs

Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance.

Use the pull-down menu to select an instance of this VI.

#### RFmxVNA Select Measurement (Single)

Enables the measurement that you specify in the Measurement parameter and disables all other measurements.

[IMAGE alt='RFmxVNA Select Measurement (Single)' src='rfmxvna_select_measurement_(single).gif']

|  | Measurement specifies the measurement to perform. You can specify one or more of the following measurements. The default value is Sparams. SParams (0) Enables S-Parameter measurement. Waves (1) Enables Wave measurement. |
| --- | --- |
| SParams (0) | Enables S-Parameter measurement. |
| Waves (1) | Enables Wave measurement. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |

#### RFmxVNA Select Measurement (Multiple)

Enables all the measurements that you specify in the Measurements parameter and disables all other measurements.

[IMAGE alt='RFmxVNA Select Measurement (Multiple)' src='rfmxvna_select_measurement_(multiple).gif']

|  | Measurements specifies the measurement(s) to perform. You can specify one or more of the following measurements. The default is an empty array. SParams (0) Enables S-Parameter measurement. Waves (1) Enables Wave measurement. |
| --- | --- |
| SParams (0) | Enables S-Parameter measurement. |
| Waves (1) | Enables Wave measurement. |
|  | Instrument Handle In specifies the RFmx session refnum. |
|  | Selector String specifies a selector string comprising of the signal name. If you do not specify the signal name, the default signal instance is used. The default value is "" (empty string). Example: "" "signal::mysignal1" You can use the RFmxVNA Build Signal String VI to build the selector string. |
|  | Enable All Traces specifies whether to enable all traces for the selected measurement. The default value is FALSE. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_sparams_configure_s-parameter.html language=enus -->
## TOPIC 00128: RFmxVNA SParams Configure S-Parameter (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_sparams_configure_s-parameter.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_sparams_configure_s-parameter.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA SParams Configure S-Parameter (VI)

Owning Palette:

SParams

Configures the S-Parameter to be measured in format S<*receiver port number*><*source port number*>

Use "sparam<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxVNA SParams Configure S-Parameter' src='rfmxvna_sparams_configure_s-parameter.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "sparam0" "signal::sig1/sparam0" "result::r1/sparam0" "signal::sig1/result::r1/sparam0" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |
|  | S-Parameter specifies the S-Parameter to be measured. The default value is S11. Supported devices: NI-5663 |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_sparams_fetch.html language=enus -->
## TOPIC 00129: RFmxVNA SParams Fetch (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_sparams_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_sparams_fetch.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA SParams Fetch (VI)

Owning Palette:

Fetch

Fetches the S-Parameters (SParams) measurement results.

Use the pull-down menu to select an instance of this VI.

#### RFmxVNA SParams Fetch Real Data

Fetches the S-Parameter data for the S-Parameters whose [SParams Format](/csh?topicname=rfmxvnaprop/attrd01005.html) is **Magnitude** or **Phase**.

Use "sparam<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxVNA SParams Fetch Real Data' src='rfmxvna_sparams_fetch_real_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "sparam0" "signal::sig1/sparam0" "result::r1/sparam0" "signal::sig1/result::r1/sparam0" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Real Data returns the measured S-Parameter real array corresponding to the Frequency List (Hz). |

#### RFmxVNA SParams Fetch Complex Data

Fetches the S-Parameter data for the S-Parameters whose [SParams Format](/csh?topicname=rfmxvnaprop/attrd01005.html) is **Complex**.

Use "sparam<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxVNA SParams Fetch Complex Data' src='rfmxvna_sparams_fetch_complex_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and S-Parameter number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. Example: "sparam0" "signal::sig1/sparam0" "result::r1/sparam0" "signal::sig1/result::r1/sparam0" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Complex Data returns the measured S-Parameter complex array corresponding to the Frequency List (Hz). |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_wait_for_measurement_complete.html language=enus -->
## TOPIC 00130: RFmxVNA Wait for Measurement Complete (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_wait_for_measurement_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_wait_for_measurement_complete.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Wait for Measurement Complete (VI)

Owning Palette:

Utility

Waits for the specified number for seconds for all the measurements to complete.

[IMAGE alt='RFmxVNA Wait for Measurement Complete' src='rfmxvna_wait_for_measurement_complete.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Selector String specifies a selector string comprising of the signal name and result name. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. The default value is "" (empty string). Example: "" "signal::sig1" "result::r1" "signal::sig1/result::r1" You can use the RFmxVNA Build S-Parameter String VI to build the selector string. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_waves_configure_wave.html language=enus -->
## TOPIC 00131: RFmxVNA Waves Configure Wave (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_waves_configure_wave.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_waves_configure_wave.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Waves Configure Wave (VI)

Owning Palette:

Waves

Configures the wave to be measured in format a<*receiver port number*><*source port number*> or b<*receiver port number*><*source port number*>, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver.

Use "wave<*n*>" as the selector string to configure this VI.

[IMAGE alt='RFmxVNA Waves Configure Wave' src='rfmxvna_waves_configure_wave.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and wave number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. "wave0" "signal::sig1/wave0" "result::r1/wave0" "signal::sig1/result::r1/wave0" You can use the RFmxVNA Build Wave String VI to build the selector string. |
|  | Wave specifies the wave to be measured. The default value is b11. Supported devices: NI-5663 |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/rfmxvna_waves_fetch.html language=enus -->
## TOPIC 00132: RFmxVNA Waves Fetch (VI)

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/rfmxvna_waves_fetch.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/rfmxvna_waves_fetch.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmxVNA Waves Fetch (VI)

Owning Palette:

Fetch

Fetches the Waves measurement results.

Use the pull-down menu to select an instance of this VI.

#### RFmxVNA Waves Fetch Real Data

Fetches the wave data for the waves whose [Waves Format](/csh?topicname=rfmxvnaprop/attrd02006.html) is **Magnitude** or **Phase**.

Use "wave<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxVNA Waves Fetch Real Data' src='rfmxvna_waves_fetch_real_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and wave number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. "wave0" "signal::sig1/wave0" "result::r1/wave0" "signal::sig1/result::r1/wave0" You can use the RFmxVNA Build Wave String VI to build the selector string. |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Real Data returns the measured wave real array corresponding to the Frequency List (Hz). |

#### RFmxVNA Waves Fetch Complex Data

Fetches the Wave data for the Waves whose [Waves Format](/csh?topicname=rfmxvnaprop/attrd02006.html) is **Complex**.

Use "wave<*n*>" as the selector string to read results from this VI.

[IMAGE alt='RFmxVNA Waves Fetch Complex Data' src='rfmxvna_waves_fetch_complex_data.gif']

|  | Instrument Handle In specifies the RFmx session refnum. |
| --- | --- |
|  | Selector String specifies a selector string comprising of the signal name, result name, and wave number. If you do not specify the signal name, the default signal instance is used. If you do not specify the result name, the default result instance is used. "wave0" "signal::sig1/wave0" "result::r1/wave0" "signal::sig1/result::r1/wave0" You can use the RFmxVNA Build Wave String VI to build the selector string. |
|  | Timeout (s) specifies the timeout, in seconds, for fetching the specified measurement. Set this value to an appropriate time, longer than expected for fetching the measurement.A value of -1 specifies that the VI waits until the measurement is complete. The default value is 10. |
|  | error out returns error information. |
|  | error in describes error conditions that occur before this node runs. |
|  | Instrument Handle Out passes a reference of your RFmx session to the next VI. |
|  | Complex Data returns the measured wave complex array corresponding to the Frequency List (Hz). |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/spara_calelement_calkit_calkitmanager_config_pal.html language=enus -->
## TOPIC 00133: S-Parameter

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/spara_calelement_calkit_calkitmanager_config_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/spara_calelement_calkit_calkitmanager_config_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

S-Parameter

Owning Palette:

Calibration Element

Use the VIs on this palette to configure s-parameter based calibration element.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set Frequency | Defines the frequency array for the S-Parameter definition of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get Frequency | Returns the frequency array for the S-Parameter definition of the Calibration Element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S-Param Availability | Defines the S-Parameter availability. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S-Param Availability | Returns the S-Parameter availability. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S11 | Sets the S11 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S11 | Returns the S11 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S12 | Sets the S12 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S12 | Returns the S12 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S21 | Sets the S21 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S21 | Returns the S21 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set S22 | Sets the S22 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Get S22 | returns the S22 S-Parameter for the calibration element. |
| RFmxVNA Calkit Manager Calkit Calibration Element S-Parameter Set From File | Defines the touchstone file name from which the S-Parameter shall be read and assigned to the Calibration Element. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/sparams_pal.html language=enus -->
## TOPIC 00134: SParams

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/sparams_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/sparams_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

SParams

Owning Palette:

Configuration

Use the VIs on this palette to configure S-Parameter measurements. You can use the RFmxVNA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA SParams Configure S-Parameter | Configures the S-Parameter to be measured in format S<receiver port number><source port number> Use "sparam<n>" as the selector string to configure this VI. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/utility_pal.html language=enus -->
## TOPIC 00135: Utility

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/utility_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Utility

Owning Palette:

RFmx VNA VIs

Use the VIs on this palette to configure utility measurements. You can use the RFmxVNA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Commit | Commits settings to the hardware. Calling this VI is optional. RFmxVNA commits settings to the hardware when you call the RFmxVNA Initiate VI. |
| RFmxVNA Reset to Default | Resets a signal to the default values. |
| RFmxVNA Wait for Measurement Complete | Waits for the specified number for seconds for all the measurements to complete. |
| RFmxVNA Check Measurement Status | Checks the status of the measurement. Use this VI to check for any errors that may occur during measurement or to check whether the measurement is complete and results are available. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/vna_pal.html language=enus -->
## TOPIC 00136: RFmx VNA VIs

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/vna_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/vna_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

RFmx VNA VIs

Use the VIs on this palette to perform VNA measurements. You can use the RFmxVNA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Select Measurement | Specifies the measurements that you want to enable. To select a single measurement, use the Single Measurement instance. To select multiple measurements, use the Multiple Measurements instance. Use the pull-down menu to select an instance of this VI. |
| RFmxVNA Initiate | Initiates all enabled measurements. Call this VI after configuring the signal and measurement. This VI asynchronously launches measurements in the background and immediately returns to the caller program. You can fetch measurement results using the Fetch VIs or result properties in the property node. To get the status of measurements, use the RFmxVNA Wait for Measurement Complete VI or RFmxVNA Check Measurement Status VI. |
| RFmxVNA Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmxVNA properties. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure measurements. You can use the RFmxVNA Property Node VI to configure additional properties. |
| Fetch | Use the VIs on this palette to fetch measurement results and traces. |
| Utility | Use the VIs on this palette to configure utility measurements. You can use the RFmxVNA Property Node to configure additional properties. |
| Build String | Use the VIs on this palette to create strings for configurations that require a selector string. |
| Advanced | Use the VIs on this palette to use advanced features. |
| Calibration | Use the VIs on this palette to use calibration. |

<!--NI_TOPIC bundle=rfmx-vna-vi path=rfmxvnavi/waves_pal.html language=enus -->
## TOPIC 00137: Waves

- bundle_id: `rfmx-vna-vi`
- source_path: `rfmxvnavi/waves_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-vna-vi/raw/resource/enus/rfmxvnavi/waves_pal.html
- document_id: `rfmx-vna-vi`
- page_type: `leaf`
- content_type: ``

Waves

Owning Palette:

Configuration

Use the VIs on this palette to configure Wave measurements. You can use the RFmxVNA Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxVNA Waves Configure Wave | Configures the wave to be measured in format a<receiver port number><source port number> or b<receiver port number><source port number>, where 'a' specifies that the receiver is reference receiver and 'b' specifies that the receiver is test receiver. Use "wave<n>" as the selector string to configure this VI. |
