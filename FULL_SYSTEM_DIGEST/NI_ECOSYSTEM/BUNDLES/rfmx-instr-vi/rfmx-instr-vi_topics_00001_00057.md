# NI DOCUMENT BUNDLE: rfmx-instr-vi

<!--NI_BUNDLE_CHUNK bundle=rfmx-instr-vi start=1 end=57 -->
<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/buildstring_pal.html language=enus -->
## TOPIC 00001: Build String

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/buildstring_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/buildstring_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

Build String

Owning Palette:

RFmxInstr VIs

Use the VI on this palette to create strings for configurations that require a selector string.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Build Calibration Plane String | Creates the selector string to use with external attenuation table VIs. |
| RFmxInstr Build Port String | Creates the port string to use as the Selector String with external attenuation table VIs. On a MIMO session, this VI can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table VIs. |
| RFmxInstr Build LO String | Creates the LO string to use as the Selector String for LO related properties. |
| RFmxInstr Build Module String | Configures the module string to use as the Selector String for reading temperature of specific modules of the device. |
| RFmxInstr Build Instrument String | Creates the instrument string to use as the Selector String for reading the recommended settings. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/calibration_pal.html language=enus -->
## TOPIC 00002: Calibration

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/calibration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/calibration_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

Calibration

Owning Palette:

RFmxInstr VIs

Use the VIs on this palette to configure calibration measurements. You can use the [RFmxInstr Property Node](../rfmxinstrvi/rfmxinstr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Self Calibrate | Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this VI self-calibrates all NI-RFSA devices and associated modules that support self-calibration. Refer to the specifications document for your device for more information about how often to self-calibrate. For more information about Self Calibrate, refer to the niRFSA Self Cal VI topic for your device in the NI RF Vector Signal Analyzers Help. |
| RFmxInstr Self Calibrate Range | Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this VI runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the niRFSA Self Calibrate Range VI topic for your device in the NI RF Vector Signal Analyzers Help. On a MIMO session, this VI self-calibrates all NI-RFSA devices and associated modules that support self-calibration. |
| RFmxInstr Is Self Calibrate Valid | Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the Valid Steps parameter to the Steps To Omit parameter of the RFmxInstr Self Calibrate VI. On a MIMO session, use the Selector String parameter to get the self-calibration validity for a specific MIMO port. |

| Subpalette | Description |
| --- | --- |
| Calibration Utility | Use the VIs on this palette to configure calibration utility measurements. You can use the RFmxInstr Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/calibration_utility_pal.html language=enus -->
## TOPIC 00003: Calibration Utility

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/calibration_utility_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/calibration_utility_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

Calibration Utility

Owning Palette:

Calibration

Use the VIs on this palette to configure calibration utility measurements. You can use the [RFmxInstr Property Node](../rfmxinstrvi/rfmxinstr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Get Self Calibrate Last Date and Time | Returns the date and time of the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration date and time for a specific MIMO port. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842 |
| RFmxInstr Get Self Calibrate Last Temperature | Returns the temperature at the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration temperature for a specific MIMO port. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842 |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/configuration_pal.html language=enus -->
## TOPIC 00004: Configuration

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/configuration_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/configuration_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

Configuration

Owning Palette:

RFmxInstr VIs

Use the VIs on this palette to configure measurements. You can use the [RFmxInstr Property Node](../rfmxinstrvi/rfmxinstr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Configure Frequency Reference | Configures the Reference Clock and the frequency reference source. |
| RFmxInstr Configure RF Attenuation | Configures the nominal attenuation and the RFmx driver setting. |
| RFmxInstr Configure Mechanical Attenuation | Configures the mechanical attenuation and the RFmx driver attenuation hardware settings. |
| RFmxInstr Export Signal | Routes signals (triggers, clocks, and events) to the specified output terminal. |
| RFmxInstr Send Software Edge Trigger | Configures the software version of a trigger that you want to send. |

| Subpalette | Description |
| --- | --- |
| External Attenuation Table | Use the VIs on this palette to use external attenuation tables. You can use the RFmxInstr Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/external_attenuation_table_pal.html language=enus -->
## TOPIC 00005: External Attenuation Table

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/external_attenuation_table_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/external_attenuation_table_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

External Attenuation Table

Owning Palette:

Configuration

Use the VIs on this palette to use external attenuation tables. You can use the [RFmxInstr Property Node](../rfmxinstrvi/rfmxinstr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Configure External Attenuation Table | Stores the external attenuation table in the calibration plane specified by the Selector String parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. |
| RFmxInstr Configure S-parameter External Attenuation Table | Stores the S-parameter table in the calibration plane specified by the Selector String parameter. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. Supported devices: PXIe-5830/5831/5832/5840/5841 Note If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
|  | Note If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
| RFmxInstr Configure S-parameter External Attenuation Type | Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. Supported devices: PXIe-5830/5831/5832/5840/5841/5842 |
| RFmxInstr Configure External Attenuation Interpolation | Configures the external attenuation interpolation technique when interpolating S-parameters for the specified table. |
| RFmxInstr Load S-parameter External Attenuation Table from S2P File | Stores the S-parameter table from the S2P file in the calibration plane specified by the Selector String parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. |
| RFmxInstr Get S-parameter External Attenuation Type | Returns the type of S-parameter that is applied to the measurements on the specified port on a Calplane. You can use the Selector String input to specify the name of the Calplane and port to configure for S-parameter. Supported devices: PXIe-5830/5831/5832/5840/5841/5842 |
| RFmxInstr Get External Attenuation Table Actual Value | Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane. |
| RFmxInstr Select Active External Attenuation Table | Activates the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this VI selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 |
| RFmxInstr Delete External Attenuation Table | Deletes the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this VI deletes the external attenuation table for the specified MIMO port. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 |
| RFmxInstr Delete All External Attenuation Tables | Deletes all the external attenuation tables in the calibration plane specified by the Selector String parameter. On a MIMO session, this VI deletes all the external attenuation tables for the specified MIMO port. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 |
| RFmxInstr Enable Calibration Plane | Enables the calibration plane specified by the Selector String parameter for amplitude correction. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 |
| RFmxInstr Disable Calibration Plane | Disables the calibration plane specified by the Selector String parameter for amplitude correction. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/mimo_pal.html language=enus -->
## TOPIC 00006: MIMO

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/mimo_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/mimo_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

MIMO

Owning Palette:

Utility

Use the VIs on this palette to configure the RFmx MIMO measurements. You can use the [RFmxInstr Property Node](../rfmxinstrvi/rfmxinstr_property_node.html) to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Initialize NIRFSA (Array) | Creates an RFmx MIMO session to the NI-RFSA supported device(s) you specify through the Resource Names parameter, and returns an Instrument Handle Out that identifies the device(s) in all subsequent RFmx VIs. |
| RFmxInstr Get NIRFSA Session (Array) | Returns the NI-RFSA driver sessions used by RFmx. |
| RFmxInstr Initialize from NIRFSA Session (Array) | Initializes an RFmx session from existing NI-RFSA sessions. This VI resets all NI-RFSA properties to their default values and stops export of all the external signals and events. This VI also takes in active NI-RFSA sessions and returns an RFmx Handle that identifies devices in all subsequent RFmx VIs. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfinstr_pal.html language=enus -->
## TOPIC 00007: RFmxInstr VIs

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfinstr_pal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfinstr_pal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr VIs

Use the VIs on this palette for configuring and fetching measurements. You can use the RFmxInstr Property Node to configure additional properties.

| Palette Object | Description |
| --- | --- |
| RFmxInstr Initialize NIRFSA | Creates an RFmx session to the NI-RFSA supported device you specify through the Resource Name parameter, and returns an Instrument Handle Out that identifies the device in all subsequent RFmx VIs. |
| RFmxInstr Get Available Ports | Fetches the list of ports available for use based on your instrument configuration. On a MIMO session, this VI fetches all the ports for the initialized MIMO ports. |
| RFmxInstr Build Port String | Creates the port string to use as the Selector String with external attenuation table VIs. On a MIMO session, this VI can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table VIs. |
| RFmxInstr Close | Closes the RFmx session. |
| RFmxInstr Property Node | Gets (reads), sets (writes), or resets (sets to default value) RFmx instrument control properties. |
| RFmxInstr VI Tree | Displays all the VIs available in RFmxInstr for instrument configuration and control. The VIs are organized in the order they must be used in the program you create. |

| Subpalette | Description |
| --- | --- |
| Configuration | Use the VIs on this palette to configure measurements. You can use the RFmxInstr Property Node to configure additional properties. |
| Utility | Use the VIs on this palette to configure utility measurements. You can use the RFmxInstr Property Node to configure additional properties. |
| Build String | Use the VI on this palette to create strings for configurations that require a selector string. |
| Calibration | Use the VIs on this palette to configure calibration measurements. You can use the RFmxInstr Property Node to configure additional properties. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_build_calibration_plane_string.html language=enus -->
## TOPIC 00008: RFmxInstr Build Calibration Plane String (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_build_calibration_plane_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_build_calibration_plane_string.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Build Calibration Plane String (VI)

Owning Palette:

Build String

Creates the selector string to use with external attenuation table VIs.

[IMAGE alt='RFmxInstr Build Calibration Plane String' src='rfmxinstr_build_calibration_plane_string.gif']

|  | Calibration Plane Name specifies the calibration plane name for building the selector string. This input accepts the calibration plane name with or without the "calplane::" prefix. The default value is "" (empty string). Example: "" "calplane::plane0" "plane0" |
| --- | --- |
|  | Selector String returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_build_instrument_string.html language=enus -->
## TOPIC 00009: RFmxInstr Build Instrument String (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_build_instrument_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_build_instrument_string.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Build Instrument String (VI)

Owning Palette:

Build String

Creates the instrument string to use as the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) for reading the recommended settings.

[IMAGE alt='RFmxInstr Build Instrument String' src='rfmxinstr_build_instrument_string.gif']

|  | Instr Number specifies the instrument number for which you want the recommended settings to be read. |
| --- | --- |
|  | Selector String specifies the selector string. The default value is "" (empty string). Example: "" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_build_lo_string.html language=enus -->
## TOPIC 00010: RFmxInstr Build LO String (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_build_lo_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_build_lo_string.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Build LO String (VI)

Owning Palette:

Build String

Creates the LO string to use as the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) for LO related properties.

[IMAGE alt='RFmxInstr Build LO String' src='rfmxinstr_build_lo_string.gif']

|  | LO Index specifies the LO index for building the selector string. |
| --- | --- |
|  | Selector String specifies the selector string. The default value is "" (empty string). Example: "" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_build_module_string.html language=enus -->
## TOPIC 00011: RFmxInstr Build Module String (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_build_module_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_build_module_string.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Build Module String (VI)

Owning Palette:

Build String

Configures the module string to use as the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) for reading temperature of specific modules of the device.

[IMAGE alt='RFmxInstr Build Module String' src='rfmxinstr_build_module_string.gif']

|  | Module Name specifies the module for which you want the temperature to be read. |
| --- | --- |
|  | Selector String specifies the selector string. The default value is "" (empty string). Example: "" |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_build_port_string.html language=enus -->
## TOPIC 00012: RFmxInstr Build Port String (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_build_port_string.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_build_port_string.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Build Port String (VI)

Owning Palette:

RFmxInstr VIs

Creates the port string to use as the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) with external attenuation table VIs. On a MIMO session, this VI can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table VIs.

[IMAGE alt='RFmxInstr Build Port String' src='rfmxinstr_build_port_string.gif']

|  | Port Name specifies the port for building the selector string. |
| --- | --- |
|  | Device Name specifies the name of the initialized device for building the selector string. |
|  | Channel Number specifies the channel for building the selector string. Specify 0 as the value for this parameter. |
|  | Selector String specifies the calibration plane string when used for building port string for the external attenuation table VIs. If you do not specify the calibration plane string, the default calibration plane instance is used. The default value is "" (empty string). Example: "" "calplane::plane0" You can use the RFmxInstr Build Calibration Plane String VI to build the selector string. |
|  | Selector String Out returns the selector string created by this VI. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_check_acquisition_status.html language=enus -->
## TOPIC 00013: RFmxInstr Check Acquisition Status (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_check_acquisition_status.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_check_acquisition_status.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Check Acquisition Status (VI)

Owning Palette:

Utility

Checks the status of the acquisition. Use this VI to check for any errors that may occur during acquisition, or to check whether RFmx has completed the acquisition operation.

[IMAGE alt='RFmxInstr Check Acquisition Status' src='rfmxinstr_check_acquisition_status.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | done? indicates whether the acquisition is complete. The default value is FALSE. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_check_if_list_exists.html language=enus -->
## TOPIC 00014: RFmxInstr Check if List Exists (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_check_if_list_exists.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_check_if_list_exists.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Check if List Exists (VI)

Owning Palette:

Utility

Returns whether the list you specify in the **List Name** parameter exists, and also returns the corresponding personality of the list, if the list exists. This VI does not support an empty ("") list name.

[IMAGE alt='RFmxInstr Check if List Exists' src='rfmxinstr_check_if_list_exists.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | List Name specifies the name of the list. This parameter accepts the list name with or without the "list::" prefix. Example: "list::samplelist1" "samplelist1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | List Exists? indicates whether the list exists or not. FALSE Indicates that the list does not exist. TRUE Indicates that the list exists. |
| FALSE | Indicates that the list does not exist. |
| TRUE | Indicates that the list exists. |
|  | Personality indicates the personality of the list if the list exists. None (0) Indicates that the given list does not exist. SpecAn (1) Indicates that the list personality is SpecAn. Demod (2) Indicates that the list personality is Demod. LTE (4) Indicates that the list personality is LTE. GSM (8) Indicates that the list personality is GSM. WCDMA (16) Indicates that the list personality is WCDMA. CDMA2k (32) Indicates that the list personality is CDMA2k. TDSCDMA (64) Indicates that the list personality is TD-SCDMA. EVDO (128) Indicates that the list personality is EV-DO. NR (256) Indicates that the list personality is NR. WLAN (512) Indicates that the list personality is WLAN. BT (1024) Indicates that the list personality is BT. |
| None (0) | Indicates that the given list does not exist. |
| SpecAn (1) | Indicates that the list personality is SpecAn. |
| Demod (2) | Indicates that the list personality is Demod. |
| LTE (4) | Indicates that the list personality is LTE. |
| GSM (8) | Indicates that the list personality is GSM. |
| WCDMA (16) | Indicates that the list personality is WCDMA. |
| CDMA2k (32) | Indicates that the list personality is CDMA2k. |
| TDSCDMA (64) | Indicates that the list personality is TD-SCDMA. |
| EVDO (128) | Indicates that the list personality is EV-DO. |
| NR (256) | Indicates that the list personality is NR. |
| WLAN (512) | Indicates that the list personality is WLAN. |
| BT (1024) | Indicates that the list personality is BT. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_check_if_signal_configuration_exists.html language=enus -->
## TOPIC 00015: RFmxInstr Check if Signal Configuration Exists (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_check_if_signal_configuration_exists.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_check_if_signal_configuration_exists.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Check if Signal Configuration Exists (VI)

Owning Palette:

Utility

Returns whether the signal you specify in the **Signal Name** parameter exists, and also returns the corresponding personality of the signal, if the signal exists. This VI does not support an empty ("") signal name.

[IMAGE alt='RFmxInstr Check if Signal Configuration Exists' src='rfmxinstr_check_if_signal_configuration_exists.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Signal Name specifies the name of the signal. This parameter accepts the signal name with or without the "signal::" prefix. Example: "signal::sig1" "sig1" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Signal Configuration Exists? indicates whether the signal exists or not. FALSE Indicates that the signal does not exist. TRUE Indicates that the signal exists. |
| FALSE | Indicates that the signal does not exist. |
| TRUE | Indicates that the signal exists. |
|  | Personality indicates the personality of the signal if the signal exists. None (0) Indicates that the given signal does not exist. SpecAn (1) Indicates that the signal personality is SpecAn. Demod (2) Indicates that the signal personality is Demod. LTE (4) Indicates that the signal personality is LTE. GSM (8) Indicates that the signal personality is GSM. WCDMA (16) Indicates that the signal personality is WCDMA. CDMA2k (32) Indicates that the signal personality is CDMA2k. TDSCDMA (64) Indicates that the signal personality is TD-SCDMA. EVDO (128) Indicates that the signal personality is EV-DO. NR (256) Indicates that the signal personality is NR. WLAN (512) Indicates that the signal personality is WLAN. BT (1024) Indicates that the signal personality is BT. |
| None (0) | Indicates that the given signal does not exist. |
| SpecAn (1) | Indicates that the signal personality is SpecAn. |
| Demod (2) | Indicates that the signal personality is Demod. |
| LTE (4) | Indicates that the signal personality is LTE. |
| GSM (8) | Indicates that the signal personality is GSM. |
| WCDMA (16) | Indicates that the signal personality is WCDMA. |
| CDMA2k (32) | Indicates that the signal personality is CDMA2k. |
| TDSCDMA (64) | Indicates that the signal personality is TD-SCDMA. |
| EVDO (128) | Indicates that the signal personality is EV-DO. |
| NR (256) | Indicates that the signal personality is NR. |
| WLAN (512) | Indicates that the signal personality is WLAN. |
| BT (1024) | Indicates that the signal personality is BT. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_close.html language=enus -->
## TOPIC 00016: RFmxInstr Close (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_close.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_close.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Close (VI)

Owning Palette:

RFmxInstr VIs

Closes the RFmx session.

[IMAGE alt='RFmxInstr Close' src='rfmxinstr_close.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Force Destroy? indicates whether to forcefully destroy the RFmx session. The default value is FALSE. TRUE Forcefully destroys the RFmx session. You do not have to call the RFmxInstr Close VI multiple times. Destroying the RFmx session invalidates all references to the session. FALSE Destroys the RFmx session only if you call the RFmxInstr Close VI a number of times equal to the number of times you obtained a reference to the RFmx session. |
| TRUE | Forcefully destroys the RFmx session. You do not have to call the RFmxInstr Close VI multiple times. Destroying the RFmx session invalidates all references to the session. |
| FALSE | Destroys the RFmx session only if you call the RFmxInstr Close VI a number of times equal to the number of times you obtained a reference to the RFmx session. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_external_attenuation_interpolation.html language=enus -->
## TOPIC 00017: RFmxInstr Configure External Attenuation Interpolation (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_external_attenuation_interpolation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_external_attenuation_interpolation.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure External Attenuation Interpolation (VI)

Owning Palette:

External Attenuation Table

Configures the external attenuation interpolation technique when interpolating S-parameters for the specified table.

#### RFmxInstr Configure External Attenuation Interpolation (Linear)

Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this VI performs a linear interpolation based on the entries above and below the row in the table.

|  | Note Currently interpolation is supported only for S-parameter tables. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Configure External Attenuation Interpolation (Linear)' src='rfmxinstr_configure_external_attenuation_interpolation_(linear).gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Format specifies the format of parameters to interpolate. The default value is Real and Imaginary. Real and Imaginary (0) Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. Magnitude and Phase (1) Results in a linear interpolation. Magnitude and Phase (dB) (2) Results in a linear interpolation. |
| Real and Imaginary (0) | Results in a linear interpolation of the real portion of the complex number and a separate linear interpolation of the complex portion. |
| Magnitude and Phase (1) | Results in a linear interpolation. |
| Magnitude and Phase (dB) (2) | Results in a linear interpolation. |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxInstr Configure External Attenuation Interpolation (Nearest)

Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used.

|  | Note Currently interpolation is supported only for S-parameter tables. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Configure External Attenuation Interpolation (Nearest)' src='rfmxinstr_configure_external_attenuation_interpolation_(nearest).gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxInstr Configure External Attenuation Interpolation (Spline)

Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this VI performs a spline interpolation based on the entries above and below the row in the table.

|  | Note Currently interpolation is supported only for S-parameter tables. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Configure External Attenuation Interpolation (Spline)' src='rfmxinstr_configure_external_attenuation_interpolation_(spline).gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_external_attenuation_table.html language=enus -->
## TOPIC 00018: RFmxInstr Configure External Attenuation Table (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_external_attenuation_table.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_external_attenuation_table.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure External Attenuation Table (VI)

Owning Palette:

External Attenuation Table

Stores the external attenuation table in the calibration plane specified by the **Selector String** parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane.

If there is only one table configured in any calibration plane, it is automatically selected as the active table.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Configure External Attenuation Table' src='rfmxinstr_configure_external_attenuation_table.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Frequency specifies an array of frequencies in the external attenuation table. This value is expressed in Hz. |
|  | External Attenuation specifies an array of attenuations corresponding to the frequency specified by the Frequency parameter. This value is expressed in dB. |
|  | Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_frequency_reference.html language=enus -->
## TOPIC 00019: RFmxInstr Configure Frequency Reference (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_frequency_reference.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_frequency_reference.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure Frequency Reference (VI)

Owning Palette:

Configuration

Configures the Reference Clock and the frequency reference source.

[IMAGE alt='RFmxInstr Configure Frequency Reference' src='rfmxinstr_configure_frequency_reference.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Frequency Reference Source specifies the frequency reference source. The default value for PXIe-5840 with PXIe-5653 is RefIn2, else the default value is OnboardClock. OnboardClock (OnboardClock) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. RefIn (RefIn) PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXI_Clk (PXI_Clk) PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842: Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5842: RFmx locks the device to the PXI backplane clock. ClkIn (ClkIn) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842: This configuration does not apply. RefIn2 (RefIn2) Configure open NI-RFSG sessions to the device to use RefIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842: This configuration does not apply. PXI_ClkMaster (PXI_ClkMaster) PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842: This configuration does not apply. |
| OnboardClock (OnboardClock) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| RefIn (RefIn) | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| PXI_Clk (PXI_Clk) | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842: Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5842: RFmx locks the device to the PXI backplane clock. |
| ClkIn (ClkIn) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842: This configuration does not apply. |
| RefIn2 (RefIn2) | Configure open NI-RFSG sessions to the device to use RefIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842: This configuration does not apply. |
| PXI_ClkMaster (PXI_ClkMaster) | PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842: This configuration does not apply. |
|  | Frequency specifies the Reference Clock rate when the Frequency Reference Source parameter is set to ClkIn or RefIn. This value is expressed in Hz. The default value is 10 MHz. |
|  | Selector String specifies a Selector String comprising of the signal name. You do not need to use a selector string, if you want to configure this parameter for all signal instances. Example: "signal::sig1" You can use the personality specific Build String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_mechanical_attenuation.html language=enus -->
## TOPIC 00020: RFmxInstr Configure Mechanical Attenuation (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_mechanical_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_mechanical_attenuation.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure Mechanical Attenuation (VI)

Owning Palette:

Configuration

Configures the mechanical attenuation and the RFmx driver attenuation hardware settings.

**Supported devices:** PXIe-5663/5663E, PXIe-5665, PXIe-5668

[IMAGE alt='RFmxInstr Configure Mechanical Attenuation' src='rfmxinstr_configure_mechanical_attenuation.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Mechanical Attenuation Auto specifies whether RFmx automatically chooses an attenuation setting based on the hardware settings. The default value is True. False (0) Specifies that RFmx uses the value configured in the Mechanical Attenuation parameter. True (1) Specifies that the measurement computes the mechanical attenuation. |
| False (0) | Specifies that RFmx uses the value configured in the Mechanical Attenuation parameter. |
| True (1) | Specifies that the measurement computes the mechanical attenuation. |
|  | Mechanical Attenuation specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. |
|  | Selector String specifies a Selector String comprising of the signal name. You do not need to use a selector string, if you want to configure this parameter for all signal instances. Example: "signal::sig1" You can use the personality specific Build String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_rf_attenuation.html language=enus -->
## TOPIC 00021: RFmxInstr Configure RF Attenuation (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_rf_attenuation.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_rf_attenuation.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure RF Attenuation (VI)

Owning Palette:

Configuration

Configures the nominal attenuation and the RFmx driver setting.

**Supported devices:** PXIe-5663/5663E, PXIe-5665, PXIe-5668

[IMAGE alt='RFmxInstr Configure RF Attenuation' src='rfmxinstr_configure_rf_attenuation.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | RF Attenuation Auto specifies whether RFmx computes the RF attenuation. If you set this parameter to True, RFmx automatically chooses an attenuation setting based on the reference level configured on the personality. The default value is True. False (0) Specifies that RFmx uses the value configured using RF Attenuation parameter. True (1) Specifies that RFmx computes the RF attenuation automatically. |
| False (0) | Specifies that RFmx uses the value configured using RF Attenuation parameter. |
| True (1) | Specifies that RFmx computes the RF attenuation automatically. |
|  | RF Attenuation specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. If you set the RF Attenuation Auto parameter to True, RFmx chooses an attenuation setting automatically. |
|  | Selector String specifies a Selector String comprising of the signal name. You do not need to use a selector string, if you want to configure this parameter for all signal instances. Example: "signal::sig1" You can use the personality specific Build String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_s-parameter_external_attenuation_table.html language=enus -->
## TOPIC 00022: RFmxInstr Configure S-parameter External Attenuation Table (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_s-parameter_external_attenuation_table.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_s-parameter_external_attenuation_table.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure S-parameter External Attenuation Table (VI)

Owning Palette:

External Attenuation Table

Stores the S-parameter table in the calibration plane specified by the **Selector String** parameter. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane.

**Supported devices**: PXIe-5830/5831/5832/5840/5841

|  | Note If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
| --- | --- |

[IMAGE alt='RFmxInstr Configure S-parameter External Attenuation Table' src='rfmxinstr_configure_s-parameter_external_attenuation_table.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Frequency specifies an array of frequencies in the S-parameter table. This value is expressed in Hz. |
|  | S-parameters specifies the S-parameters for each frequency. The first index indicates the corresponding frequency entry, the second index corresponds to the target port for the S-parameter, and the third index corresponds to the the source port. For example, to index the s21 parameter for the fourth frequency in the table, you would use {3, 1, 0} as the indexes since they are zero-based. |
|  | S-parameters Orientation specifies the orientation of the data in the S-parameter table relative to the port you specify. The default value is Port2 Towards DUT. Port1 Towards DUT (0) Port 1 of the S2P is oriented towards the DUT. Port2 Towards DUT (1) Port 2 of the S2P is oriented towards the DUT. |
| Port1 Towards DUT (0) | Port 1 of the S2P is oriented towards the DUT. |
| Port2 Towards DUT (1) | Port 2 of the S2P is oriented towards the DUT. |
|  | Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_configure_s-parameter_external_attenuation_type.html language=enus -->
## TOPIC 00023: RFmxInstr Configure S-parameter External Attenuation Type (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_configure_s-parameter_external_attenuation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_configure_s-parameter_external_attenuation_type.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Configure S-parameter External Attenuation Type (VI)

Owning Palette:

External Attenuation Table

Configures the type of S-parameter to apply to measurements on the specified port for a Calplane. You can use the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) input to specify the name of the Calplane and port to configure for S-parameter.

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Configure S-parameter External Attenuation Type' src='rfmxinstr_configure_s-parameter_external_attenuation_type.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | S-parameter Type specifies the type of S-parameter which applies to measurements on the specified port for a Calplane. If you set this parameter to Scalar or Vector, RFmx adjusts the instrument settings and the returned data to remove the effects of the external network between the instrument and the DUT. PXIe-5831/5832: Valid values for this parameter are Scalar and Vector. Vector is only supported for TRX ports in a semiconductor test system (STS). PXIe-5840/5841/5842: The only valid value for this parameter is Scalar. The default value is Scalar. Scalar (1) De-embeds the measurement using the gain term. Vector (2) De-embeds the measurement using the gain term and the reflection term. |
| Scalar (1) | De-embeds the measurement using the gain term. |
| Vector (2) | De-embeds the measurement using the gain term and the reflection term. |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure S-parameter external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_delete_all_external_attenuation_tables.html language=enus -->
## TOPIC 00024: RFmxInstr Delete All External Attenuation Tables (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_delete_all_external_attenuation_tables.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_delete_all_external_attenuation_tables.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Delete All External Attenuation Tables (VI)

Owning Palette:

External Attenuation Table

Deletes all the external attenuation tables in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this VI deletes all the external attenuation tables for the specified MIMO port.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Delete All External Attenuation Tables' src='rfmxinstr_delete_all_external_attenuation_tables.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If you specify "calplane::all", all the calibration planes are deleted. On a MIMO session, the default "" (empty string) deletes all the external attenuation tables for all MIMO Ports. To delete an external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::all" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::all/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_delete_external_attenuation_table.html language=enus -->
## TOPIC 00025: RFmxInstr Delete External Attenuation Table (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_delete_external_attenuation_table.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_delete_external_attenuation_table.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Delete External Attenuation Table (VI)

Owning Palette:

External Attenuation Table

Deletes the external attenuation table set by the **Table Name** parameter in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this VI deletes the external attenuation table for the specified MIMO port.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Delete External Attenuation Table' src='rfmxinstr_delete_external_attenuation_table.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, the default "" (empty string) deletes the active external attenuation table for all the MIMO Ports. To delete an external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_disable_calibration_plane.html language=enus -->
## TOPIC 00026: RFmxInstr Disable Calibration Plane (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_disable_calibration_plane.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_disable_calibration_plane.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Disable Calibration Plane (VI)

Owning Palette:

External Attenuation Table

Disables the calibration plane specified by the **Selector String** parameter for amplitude correction.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Disable Calibration Plane' src='rfmxinstr_disable_calibration_plane.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If you specify "calplane::all", all the calibration planes are disabled. Example: "" "calplane::plane0" "calplane::all" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_enable_calibration_plane.html language=enus -->
## TOPIC 00027: RFmxInstr Enable Calibration Plane (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_enable_calibration_plane.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_enable_calibration_plane.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Enable Calibration Plane (VI)

Owning Palette:

External Attenuation Table

Enables the calibration plane specified by the **Selector String** parameter for amplitude correction.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Enable Calibration Plane' src='rfmxinstr_enable_calibration_plane.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies the calibration plane name in which the external attenuation table or S-parameter is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If "calplane::all" is specified, all the calibration planes are enabled. Example: "" "calplane::plane0" "calplane::all" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_export_signal.html language=enus -->
## TOPIC 00028: RFmxInstr Export Signal (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_export_signal.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_export_signal.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Export Signal (VI)

Owning Palette:

Configuration

Routes signals (triggers, clocks, and events) to the specified output terminal.

|  | Note This VI is not supported on a MIMO session. |
| --- | --- |

[IMAGE alt='RFmxInstr Export Signal' src='rfmxinstr_export_signal.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Export Signal Source controls the source to export signals. Start Trigger (0) Start trigger is sourced. Ref Trigger (1) Reference trigger is sourced. Advance Trigger (2) Advance trigger is sourced. Ready for Start Event (3) Ready for Start event is sourced. Ready for Advance Event (4) Ready for Advance event is sourced. Ready for Ref Event (5) Ready for Reference event is sourced. End of Record Event (6) End of Record event is sourced. Done Event (7) Done event is sourced. Reference Clock (8) Reference clock is sourced. |
| Start Trigger (0) | Start trigger is sourced. |
| Ref Trigger (1) | Reference trigger is sourced. |
| Advance Trigger (2) | Advance trigger is sourced. |
| Ready for Start Event (3) | Ready for Start event is sourced. |
| Ready for Advance Event (4) | Ready for Advance event is sourced. |
| Ready for Ref Event (5) | Ready for Reference event is sourced. |
| End of Record Event (6) | End of Record event is sourced. |
| Done Event (7) | Done event is sourced. |
| Reference Clock (8) | Reference clock is sourced. |
|  | Export Signal Output Terminal specifies the terminal where the signal is exported. You can also choose not to export any signal. The default value is "" (empty string). Do not export signal (()) The signal is not exported. ClkOut (ClkOut) Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842. RefOut (RefOut) The signal is exported to the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842. RefOut2 (RefOut2) The signal is exported to the REF OUT2 terminal on the LO. This connector exists only on some versions of the PXIe-5652. PFI0 (PFI0) The signal is exported to the PFI 0 connector on the PXIe-5142 and PXIe-5624. PFI1 (PFI1) The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. PXI_Trig0 (PXI_Trig0) The signal is exported to the PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The signal is exported to the PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The signal is exported to the PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The signal is exported to the PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The signal is exported to the PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The signal is exported to the PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The signal is exported to the PXI trigger line 6. PXIe_DStarC (PXIe_DStarC) The signal is exported to the PXI DStar C trigger line. This value is valid only on PXIe-5820/5830/5831/5832/5840/5841/5842. |
| Do not export signal (()) | The signal is not exported. |
| ClkOut (ClkOut) | Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut (RefOut) | The signal is exported to the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | The signal is exported to the REF OUT2 terminal on the LO. This connector exists only on some versions of the PXIe-5652. |
| PFI0 (PFI0) | The signal is exported to the PFI 0 connector on the PXIe-5142 and PXIe-5624. |
| PFI1 (PFI1) | The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | The signal is exported to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The signal is exported to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The signal is exported to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The signal is exported to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The signal is exported to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The signal is exported to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The signal is exported to the PXI trigger line 6. |
| PXIe_DStarC (PXIe_DStarC) | The signal is exported to the PXI DStar C trigger line. This value is valid only on PXIe-5820/5830/5831/5832/5840/5841/5842. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_fetch_raw_iq_(1rec).html language=enus -->
## TOPIC 00029: RFmxInstr Fetch Raw IQ (1Rec) (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_fetch_raw_iq_(1rec).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_fetch_raw_iq_(1rec).html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Fetch Raw IQ (1Rec) (VI)

Fetches I/Q data from a single record in an acquisition.

[IMAGE alt='RFmxInstr Fetch Raw IQ (1Rec)' src='rfmxinstr_fetch_raw_iq_(1rec).gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout (s)specifies the timeout, in seconds, for fetching the raw IQ data. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies the VI immediately returns available data. The default value is 10. |
|  | Record to Fetch specifies the record to retrieve. Record numbers are zero-based. The default value is 0. |
|  | Samples to Read specifies the number of samples to fetch. A value of -1 specifies that RFmx fetches all samples. The default value is -1. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | IQ Data returns the acquired data as a cluster. t0 returns the start time of the first sample. The timestamp corresponds to the difference, in seconds, between the returned first sample and the reference trigger location. dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. Y returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I 2 + Q 2) / 2R, where R is the input impedance in ohms. For RFmx, R = 50 ohms. |
|  | t0 returns the start time of the first sample. The timestamp corresponds to the difference, in seconds, between the returned first sample and the reference trigger location. |
|  | dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. |
|  | Y returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I 2 + Q 2) / 2R, where R is the input impedance in ohms. For RFmx, R = 50 ohms. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_available_ports.html language=enus -->
## TOPIC 00030: RFmxInstr Get Available Ports (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_available_ports.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_available_ports.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get Available Ports (VI)

Owning Palette:

Utility

Fetches the list of ports available for use based on your instrument configuration. On a MIMO session, this VI fetches all the ports for the initialized MIMO ports.

[IMAGE alt='RFmxInstr Get Available Ports' src='rfmxinstr_get_available_ports.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Available Ports returns a list of available ports. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_external_attenuation_table_actual_value.html language=enus -->
## TOPIC 00031: RFmxInstr Get External Attenuation Table Actual Value (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_external_attenuation_table_actual_value.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_external_attenuation_table_actual_value.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get External Attenuation Table Actual Value (VI)

Owning Palette:

External Attenuation Table

Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane.

On a MIMO session, this VI returns the external attenuation table actual value for a specified port. You can use the **Selector String** parameter to specify the name of the signal, calibration plane, and MIMO port to return the external attenuation table actual value.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Get External Attenuation Table Actual Value' src='rfmxinstr_get_external_attenuation_table_actual_value.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a Selector String comprising of the signal name and calibration plane name. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, you must use "port::<deviceName>/<channelNumber>" as part of the selector string to read the external attenuation table actual value for the specified port. If you do not specify the signal name, the value is returned for the last committed signal instance. Example: "" "signal::sig1" "calplane::plane0" "signal::sig1/calplane::plane0" "port::rfsa1/0" "signal::sig1/port::rfsa1/0" "calplane::plane0/port::rfsa1/0" "signal::sig1/calplane::plane0/port::rfsa1/0" |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | External Attenuation returns the external attenuation table actual value applied to the measurements for a specified signal and calibration plane. This further includes interpolation of the external attenuation table based on the specified signal. On a MIMO session, this value corresponds to a specified port. This value is expressed in dB. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_list_names.html language=enus -->
## TOPIC 00032: RFmxInstr Get List Names (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_list_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_list_names.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get List Names (VI)

Owning Palette:

Utility

Returns the list names and the corresponding selected personality type from the **Personality Filter** parameter. When you set the **Personality Filter** parameter to **All**, this VI returns the available list names for all supported personalities.

[IMAGE alt='RFmxInstr Get List Names' src='rfmxinstr_get_list_names.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Personality Filter specifies the personality filter to get the list names. You can specify one or more of the following personalities. The default value is All. SpecAn (1) Specifies the SpecAn personality. Demod (2) Specifies the Demod personality. LTE (4) Specifies the LTE personality. GSM (8) Specifies the GSM personality. WCDMA (16) Specifies the WCDMA personality. CDMA2k (32) Specifies the CDMA2k personality. TDSCDMA (64) Specifies the TD-SCDMA personality. EVDO (128) Specifies the EV-DO personality. NR (256) Specifies the NR personality. WLAN (512) Specifies the WLAN personality. BT (1024) Specifies the BT personality. All (2147483647) Specifies all the personalities. |
| SpecAn (1) | Specifies the SpecAn personality. |
| Demod (2) | Specifies the Demod personality. |
| LTE (4) | Specifies the LTE personality. |
| GSM (8) | Specifies the GSM personality. |
| WCDMA (16) | Specifies the WCDMA personality. |
| CDMA2k (32) | Specifies the CDMA2k personality. |
| TDSCDMA (64) | Specifies the TD-SCDMA personality. |
| EVDO (128) | Specifies the EV-DO personality. |
| NR (256) | Specifies the NR personality. |
| WLAN (512) | Specifies the WLAN personality. |
| BT (1024) | Specifies the BT personality. |
| All (2147483647) | Specifies all the personalities. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | List Names returns an array of the list names. |
|  | Personalities returns an array of personalities where each entry corresponds to the personality of each list name in the List Names array. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_nirfsa_session.html language=enus -->
## TOPIC 00033: RFmxInstr Get NIRFSA Session (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_nirfsa_session.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_nirfsa_session.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get NIRFSA Session (VI)

Owning Palette:

Utility

Returns the NI-RFSA driver session used by RFmx.

|  | Note Do not close the NI-RFSA driver session before calling the RFmxInstr Close VI. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. |
| --- | --- |

[IMAGE alt='RFmxInstr Get NIRFSA Session' src='rfmxinstr_get_nirfsa_session.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | NI RFSA Session specifies the NI-RFSA session for the device. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_nirfsa_session_(array).html language=enus -->
## TOPIC 00034: RFmxInstr Get NIRFSA Session (Array) (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_nirfsa_session_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_nirfsa_session_(array).html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get NIRFSA Session (Array) (VI)

Owning Palette:

MIMO

Returns the NI-RFSA driver sessions used by RFmx.

|  | Note Do not close the NI-RFSA driver sessions before calling the RFmxInstr Close VI. Closing the NI-RFSA driver sessions before closing RFmx session would lead to unpredictable behavior. |
| --- | --- |

[IMAGE alt='RFmxInstr Get NIRFSA Session (Array)' src='rfmxinstr_get_nirfsa_session_(array).gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | NI RFSA Sessions specifies the NI-RFSA sessions for the device. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_s-parameter_external_attenuation_type.html language=enus -->
## TOPIC 00035: RFmxInstr Get S-parameter External Attenuation Type (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_s-parameter_external_attenuation_type.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_s-parameter_external_attenuation_type.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get S-parameter External Attenuation Type (VI)

Owning Palette:

External Attenuation Table

Returns the type of S-parameter that is applied to the measurements on the specified port on a Calplane. You can use the [Selector String](/csh?topicname=rfmxspecan/selector_string.html) input to specify the name of the Calplane and port to configure for S-parameter.

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Get S-parameter External Attenuation Type' src='rfmxinstr_get_s-parameter_external_attenuation_type.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session if you do not specify the port name, this VI will return an error. To get S-parameter external attenuation type from a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | S-parameter Type returns the type of S-parameter which is applied to measurements on the specified port of a Calplane. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_self_calibrate_last_date_and_time.html language=enus -->
## TOPIC 00036: RFmxInstr Get Self Calibrate Last Date and Time (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_self_calibrate_last_date_and_time.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_self_calibrate_last_date_and_time.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get Self Calibrate Last Date and Time (VI)

Owning Palette:

Calibration Utility

Returns the date and time of the last successful self-calibration. On a MIMO session, use the **Selector String** parameter to get the last successful self-calibration date and time for a specific MIMO port.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

|  | Note For PXIe-5644/5645/5646 devices, you must select Image Suppression for the Self Calibrate Step parameter. |
| --- | --- |

[IMAGE alt='RFmxInstr Get Self Calibrate Last Date and Time' src='rfmxinstr_get_self_calibrate_last_date_and_time.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Self Calibrate Step specifies the self-calibration step to query for the last successful self-calibration date and time data. The default value is Preselector Alignment. Preselector Alignment (1) Selects the Preselector Alignment self-calibration step. Gain Reference (2) Selects the Gain Reference self-calibration step. IF Flatness (4) Selects the IF Flatness self-calibration step. Digitizer Self Cal (8) Selects the Digitizer Self Cal self-calibration step. LO Self Cal (10) Selects the LO Self Cal self-calibration step. Amplitude Accuracy (20) Selects the Amplitude Accuracy self-calibration step. Residual LO Power (40) Selects the Residual LO Power self-calibration step. Image Suppression (80) Selects the Image Suppression self-calibration step. Synthesizer Alignment (100) Selects the Synthesizer Alignment self-calibration step. DC Offset (200) Selects the DC Offset self-calibration step. |
| Preselector Alignment (1) | Selects the Preselector Alignment self-calibration step. |
| Gain Reference (2) | Selects the Gain Reference self-calibration step. |
| IF Flatness (4) | Selects the IF Flatness self-calibration step. |
| Digitizer Self Cal (8) | Selects the Digitizer Self Cal self-calibration step. |
| LO Self Cal (10) | Selects the LO Self Cal self-calibration step. |
| Amplitude Accuracy (20) | Selects the Amplitude Accuracy self-calibration step. |
| Residual LO Power (40) | Selects the Residual LO Power self-calibration step. |
| Image Suppression (80) | Selects the Image Suppression self-calibration step. |
| Synthesizer Alignment (100) | Selects the Synthesizer Alignment self-calibration step. |
| DC Offset (200) | Selects the DC Offset self-calibration step. |
|  | Selector String specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string). Example: "" "port::myrfsa1/0" You can use the RFmxInstr Build Port String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Time Stamp returns the date and time of the last successful self-calibration. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_self_calibrate_last_temperature.html language=enus -->
## TOPIC 00037: RFmxInstr Get Self Calibrate Last Temperature (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_self_calibrate_last_temperature.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_self_calibrate_last_temperature.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get Self Calibrate Last Temperature (VI)

Owning Palette:

Calibration Utility

Returns the temperature at the last successful self-calibration. On a MIMO session, use the **Selector String** parameter to get the last successful self-calibration temperature for a specific MIMO port.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842

|  | Note For PXIe-5644/5645/5646 devices, you must select Image Suppression for the Self Calibrate Step parameter. |
| --- | --- |

[IMAGE alt='RFmxInstr Get Self Calibrate Last Temperature' src='rfmxinstr_get_self_calibrate_last_temperature.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Self Calibrate Step specifies the self-calibration step to query for the last successful self-calibration temperature data. The default value is Preselector Alignment. Preselector Alignment (1) Selects the Preselector Alignment self-calibration step. Gain Reference (2) Selects the Gain Reference self-calibration step. IF Flatness (4) Selects the IF Flatness self-calibration step. Digitizer Self Cal (8) Selects the Digitizer Self Cal self-calibration step. LO Self Cal (10) Selects the LO Self Cal self-calibration step. Amplitude Accuracy (20) Selects the Amplitude Accuracy self-calibration step. Residual LO Power (40) Selects the Residual LO Power self-calibration step. Image Suppression (80) Selects the Image Suppression self-calibration step. Synthesizer Alignment (100) Selects the Synthesizer Alignment self-calibration step. DC Offset (200) Selects the DC Offset self-calibration step. |
| Preselector Alignment (1) | Selects the Preselector Alignment self-calibration step. |
| Gain Reference (2) | Selects the Gain Reference self-calibration step. |
| IF Flatness (4) | Selects the IF Flatness self-calibration step. |
| Digitizer Self Cal (8) | Selects the Digitizer Self Cal self-calibration step. |
| LO Self Cal (10) | Selects the LO Self Cal self-calibration step. |
| Amplitude Accuracy (20) | Selects the Amplitude Accuracy self-calibration step. |
| Residual LO Power (40) | Selects the Residual LO Power self-calibration step. |
| Image Suppression (80) | Selects the Image Suppression self-calibration step. |
| Synthesizer Alignment (100) | Selects the Synthesizer Alignment self-calibration step. |
| DC Offset (200) | Selects the DC Offset self-calibration step. |
|  | Selector String specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string). Example: "" "port::myrfsa1/0" You can use the RFmxInstr Build Port String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Temperature returns the temperature at the last self-calibration. This value is expressed in degree Celsius. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_get_signal_configuration_names.html language=enus -->
## TOPIC 00038: RFmxInstr Get Signal Configuration Names (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_get_signal_configuration_names.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_get_signal_configuration_names.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Get Signal Configuration Names (VI)

Owning Palette:

Utility

Returns the signal names and the corresponding selected personality type from the **Personality Filter** parameter.

[IMAGE alt='RFmxInstr Get Signal Configuration Names' src='rfmxinstr_get_signal_configuration_names.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Personality Filter specifies the personality filter to get the signal configuration names. You can specify one or more of the following personalities. The default value is All. SpecAn (1) Specifies the SpecAn personality. Demod (2) Specifies the Demod personality. LTE (4) Specifies the LTE personality. GSM (8) Specifies the GSM personality. WCDMA (16) Specifies the WCDMA personality. CDMA2k (32) Specifies the CDMA2k personality. TDSCDMA (64) Specifies the TD-SCDMA personality. EVDO (128) Specifies the EV-DO personality. NR (256) Specifies the NR personality. WLAN (512) Specifies the WLAN personality. BT (1024) Specifies the BT personality. All (2147483647) Specifies all the personalities. |
| SpecAn (1) | Specifies the SpecAn personality. |
| Demod (2) | Specifies the Demod personality. |
| LTE (4) | Specifies the LTE personality. |
| GSM (8) | Specifies the GSM personality. |
| WCDMA (16) | Specifies the WCDMA personality. |
| CDMA2k (32) | Specifies the CDMA2k personality. |
| TDSCDMA (64) | Specifies the TD-SCDMA personality. |
| EVDO (128) | Specifies the EV-DO personality. |
| NR (256) | Specifies the NR personality. |
| WLAN (512) | Specifies the WLAN personality. |
| BT (1024) | Specifies the BT personality. |
| All (2147483647) | Specifies all the personalities. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Signal Names returns an array of the signal names. |
|  | Personalities returns an array of personalities where each entry corresponds to the personality of each signal name in the Signal Names array. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_initialize.html language=enus -->
## TOPIC 00039: RFmxInstr Initialize (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_initialize.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_initialize.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Initialize (VI)

Owning Palette:

Utility

Creates an RFmx session to the signal/network analyzer you specify through the **Resource Name** parameter, and returns an **Instrument Handle Out** that identifies this device in all subsequent RFmx VIs.

|  | Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| --- | --- |

[IMAGE alt='RFmxInstr Initialize' src='rfmxinstr_initialize.gif']

|  | Resource Name specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |  |
| --- | --- | --- |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |
|  | Option String sets the initial value of certain properties for the session. The following properties are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about properties used in this parameter, refer to NI RF Vector Signal Analyzers Help. The format of this string is "PropertyName=Value", where PropertyName is the name of the property and Value is the value to which the property is set. For example, you can simulate a PXIe-5663E device using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple properties, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx use yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". While using this mode, you are responsible for waveform acquisition and RFmx will perform analysis on the I/Q waveform or Spectrum you specify. You must use personality specific Analyze functions to perform the measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. To use external NI source measure units (SMU) as the noise source power supply for the Noise Figure (NF) measurement, use "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You must allocate a dedicated SMU channel for RFmx. Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. |  |
|  | Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
|  | Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |  |
|  | Created New? is TRUE if the VI created a new session, or FALSE if the VI returned a reference to an existing session. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_initialize_from_nirfsa_session.html language=enus -->
## TOPIC 00040: RFmxInstr Initialize from NIRFSA Session (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_initialize_from_nirfsa_session.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_initialize_from_nirfsa_session.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Initialize from NIRFSA Session (VI)

Owning Palette:

Utility

Initializes an RFmx session from an existing NI-RFSA session. This VI resets all NI-RFSA properties to their default values and stops export of all the external signals and events. This VI also takes in an active NI-RFSA session and returns an RFmx Handle that identifies the device in all subsequent RFmx VIs.

|  | Note Do not close the NI-RFSA driver session before calling the RFmxInstr Close VI. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. Closing the RFmx session will not close the NI-RFSA driver session. |
| --- | --- |

[IMAGE alt='RFmxInstr Initialize from NIRFSA Session' src='rfmxinstr_initialize_from_nirfsa_session.gif']

|  | NI-RFSA Handle In identifies the NI-RFSA session. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RFmx Handle Out passes a reference of the RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_initialize_from_nirfsa_session_(array).html language=enus -->
## TOPIC 00041: RFmxInstr Initialize from NIRFSA Session (Array) (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_initialize_from_nirfsa_session_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_initialize_from_nirfsa_session_(array).html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Initialize from NIRFSA Session (Array) (VI)

Owning Palette:

MIMO

Initializes an RFmx session from existing NI-RFSA sessions. This VI resets all NI-RFSA properties to their default values and stops export of all the external signals and events. This VI also takes in active NI-RFSA sessions and returns an RFmx Handle that identifies devices in all subsequent RFmx VIs.

|  | Note Do not close the NI-RFSA driver sessions before calling the RFmxInstr Close VI. Closing NI-RFSA driver sessions before closing an RFmx session would lead to unpredictable behavior. Closing the RFmx session will not close the NI-RFSA driver sessions. |
| --- | --- |

[IMAGE alt='RFmxInstr Initialize from NIRFSA Session (Array)' src='rfmxinstr_initialize_from_nirfsa_session_(array).gif']

|  | NI-RFSA Handles In identifies the NI-RFSA sessions. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RFmx Handle Out passes a reference of the RFmx session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_initialize_nirfsa.html language=enus -->
## TOPIC 00042: RFmxInstr Initialize NIRFSA (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_initialize_nirfsa.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_initialize_nirfsa.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Initialize NIRFSA (VI)

Owning Palette:

RFmxInstr VIs

Creates an RFmx session to the NI-RFSA supported device you specify through the **Resource Name** parameter, and returns an **Instrument Handle Out** that identifies the device in all subsequent RFmx VIs.

|  | Note Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends disabling SFP debug. SFP debug can be enabled/disabled from either the RF Signal Analyzer panel in InstrumentStudio, the RFSA Soft Front Panel, or the RFmx Debug Configuration Utility. |
| --- | --- |

[IMAGE alt='RFmxInstr Initialize NIRFSA' src='rfmxinstr_initialize_nirfsa.gif']

|  | Resource Name specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |  |
| --- | --- | --- |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |
|  | Option String sets the initial value of certain properties for the session. The following properties are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about properties used in this parameter, refer to NI RF Vector Signal Analyzers Help. The format of this string is "PropertyName=Value", where PropertyName is the name of the property and Value is the value to which the property is set. For example, you can simulate a PXIe-5663E device using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple properties, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx use yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". While using this mode, you are responsible for waveform acquisition and RFmx will perform analysis on the I/Q waveform or Spectrum you specify. You must use personality specific Analyze functions to perform the measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. To use external NI source measure units (SMU) as the noise source power supply for the Noise Figure (NF) measurement, use "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You must allocate a dedicated SMU channel for RFmx. Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. |  |
|  | Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. |  |
|  | Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. |  |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |  |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |  |
|  | Created New? is TRUE if the VI created a new session, or FALSE if the VI returned a reference to an existing session. |  |
|  | error out contains error information. This output provides standard error out functionality. |  |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_initialize_nirfsa_(array).html language=enus -->
## TOPIC 00043: RFmxInstr Initialize NIRFSA (Array) (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_initialize_nirfsa_(array).html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_initialize_nirfsa_(array).html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Initialize NIRFSA (Array) (VI)

Owning Palette:

MIMO

Creates an RFmx MIMO session to the NI-RFSA supported device(s) you specify through the **Resource Names** parameter, and returns an **Instrument Handle Out** that identifies the device(s) in all subsequent RFmx VIs.

**Supported devices:** PXIe-5840/5841/5842, PXIe-5830/5831/5832

[IMAGE alt='RFmxInstr Initialize NIRFSA (Array)' src='rfmxinstr_initialize_nirfsa_(array).gif']

|  | Resource Names specifies the resource names of the devices to initialize. The following example shows how to specify the resource names. Device Type Syntax [myRFmxDevice0, myRFmxDevice1.,] RFmx device, device name is "myRFmxDevice0" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in the example. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. |
| --- | --- |
| Device Type | Syntax |
| [myRFmxDevice0, myRFmxDevice1.,] | RFmx device, device name is "myRFmxDevice0" |
|  | Option String sets the initial value of certain properties for the session. The following properties are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about properties used in this parameter, refer to NI RF Vector Signal Analyzers Help. The format of this string is "PropertyName=Value", where PropertyName is the name of the property and Value is the value to which the property is set. For example, you can simulate a PXIe-5840 device using the following string: "Simulate=1, RFmxSetup=Model:5840" To set multiple properties, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx use yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1;MaxNumWfms:<n>", where "n" represents the maximum number of waveforms that can be used for the MIMO measurement. While using this mode, you are responsible for waveform acquisition and RFmx will perform analysis on the I/Q waveform(s) or Spectrum(s) you specify. You must use personality specific Analyze functions to perform the measurements. To use external NI source measure units (SMU) as the noise source power supply for the noise figure (NF) measurement, use "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You must allocate a dedicated SMU channel for RFmx. Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. |
|  | Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Created New? is TRUE if the VI created a new session, or FALSE if the VI returned a reference to an existing session. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_is_self_calibrate_valid.html language=enus -->
## TOPIC 00044: RFmxInstr Is Self Calibrate Valid (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_is_self_calibrate_valid.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_is_self_calibrate_valid.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Is Self Calibrate Valid (VI)

Owning Palette:

Calibration

Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the **Valid Steps** parameter to the **Steps To Omit** parameter of the [RFmxInstr Self Calibrate](../rfmxinstrvi/rfmxinstr_self_calibrate.html) VI. On a MIMO session, use the **Selector String** parameter to get the self-calibration validity for a specific MIMO port.

**Supported devices:** PXIe-5663/5663E/5665/5668

[IMAGE alt='RFmxInstr Is Self Calibrate Valid' src='rfmxinstr_is_self_calibrate_valid.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Selector String specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string). Example: "" "port::myrfsa1/0" You can use the RFmxInstr Build Port String VI to build the selector string. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | Self Calibrate Valid returns TRUE if all the calibration data is valid and FALSE if any of the calibration data is invalid. |
|  | Valid Steps returns an array of valid steps. Preselector Alignment (1) Indicates the Preselector Alignment calibration data is valid. This step generates coefficients to align the preselector across the frequency range for your device. Gain Reference (2) Indicates the Gain Reference calibration data is valid. This step measures the changes in gain since the last external calibration was run. IF Flatness (4) Indicates the IF Flatness calibration data is valid. This step measures the IF response of the entire system for each of the supported IF filters. Digitizer Self Cal (8) Indicates the Digitizer Self Cal calibration data is valid. This step calls for digitizer self-calibration if the digitizer is associated with the RF downconverter. LO Self Cal (10) Indicates the LO Self Cal calibration data is valid. This step calls for LO self-calibration if the LO source module is associated with the RF downconverter. |
| Preselector Alignment (1) | Indicates the Preselector Alignment calibration data is valid. This step generates coefficients to align the preselector across the frequency range for your device. |
| Gain Reference (2) | Indicates the Gain Reference calibration data is valid. This step measures the changes in gain since the last external calibration was run. |
| IF Flatness (4) | Indicates the IF Flatness calibration data is valid. This step measures the IF response of the entire system for each of the supported IF filters. |
| Digitizer Self Cal (8) | Indicates the Digitizer Self Cal calibration data is valid. This step calls for digitizer self-calibration if the digitizer is associated with the RF downconverter. |
| LO Self Cal (10) | Indicates the LO Self Cal calibration data is valid. This step calls for LO self-calibration if the LO source module is associated with the RF downconverter. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_load_configurations.html language=enus -->
## TOPIC 00045: RFmxInstr Load Configurations (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_load_configurations.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_load_configurations.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Load Configurations (VI)

Owning Palette:

Utility

Loads the properties of an RFmx session saved in a file. This file can be generated using [RFmxInstr Save All Configurations](../rfmxinstrvi/rfmxinstr_save_all_configurations.html) VI or using the RF Signal Analyzer panel in InstrumentStudio.

You can specify the configurations to skip while loading from a file using the [Load Options](/csh?topicname=rfmxinstrprop/attra3.html) property.

|  | Note If the file contains a named signal configuration which is already present in the session, then this VI will return an error. NI recommendeds to call the RFmxInstr Reset Entire Session VI to delete all the named signal configurations in the session. |
| --- | --- |

[IMAGE alt='RFmxInstr Load Configurations' src='rfmxinstr_load_configurations.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | File Path specifies the complete path to the file from which the configurations are to be loaded. Default file extension: .rfmxconfig |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_load_s-parameter_external_attenuation_table_from_s2p_file.html language=enus -->
## TOPIC 00046: RFmxInstr Load S-parameter External Attenuation Table from S2P File (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_load_s-parameter_external_attenuation_table_from_s2p_file.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_load_s-parameter_external_attenuation_table_from_s2p_file.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Load S-parameter External Attenuation Table from S2P File (VI)

Owning Palette:

External Attenuation Table

Stores the S-parameter table from the S2P file in the calibration plane specified by the **Selector String** parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane.

|  | Note If there is only one table configured in any calibration plane, it is automatically selected as the active table. |
| --- | --- |

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Load S-parameter External Attenuation Table from S2P File' src='rfmxinstr_load_s-parameter_external_attenuation_table_from_s2p_file.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | S2P File Path specifies the path to the S2P file that contains S-parameter table information for the specified port. |
|  | S-parameters Orientation specifies the orientation of the data in the S-parameter table relative to the port you specify. The default value is Port2 Towards DUT. Port1 Towards DUT (0) Port 1 of the S2P is oriented towards the DUT. Port2 Towards DUT (1) Port 2 of the S2P is oriented towards the DUT. |
| Port1 Towards DUT (0) | Port 1 of the S2P is oriented towards the DUT. |
| Port2 Towards DUT (1) | Port 2 of the S2P is oriented towards the DUT. |
|  | Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_property_node.html language=enus -->
## TOPIC 00047: RFmxInstr Property Node (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_property_node.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_property_node.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Property Node (VI)

Owning Palette:

RFmxInstr VIs

Gets (reads), sets (writes), or resets (sets to default value) RFmx instrument control properties.

[IMAGE alt='RFmxInstr Property Node' src='rfmxinstr_property_node.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_reset_driver.html language=enus -->
## TOPIC 00048: RFmxInstr Reset Driver (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_reset_driver.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_reset_driver.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Reset Driver (VI)

Owning Palette:

Utility

Restores the NI-RFSA driver state to a default state to avoid RFmx using any hardware or driver state that was set by the RF toolkits or other custom NI-RFSA code.

Use this VI when you switch back to using RFmx to perform measurements after you have used the NI-RFSA handle to perform measurements with RF toolkits or you have used other custom NI-RFSA code. Unlike the [RFmxInstr Reset to Default](../rfmxinstrvi/rfmxinstr_reset_to_default.html) VI, the RfmxInstr Reset Driver VI does not reset RFmx properties configured on the RFmx session. Hence, you do not need to set RFmx properties again when switching back to RFmx measurements. Refer to RFmx SpecAn CHP - WCDMA ModAcc - CHP Example (LabVIEW) for more information about using RFmx to perform measurements.

[IMAGE alt='RFmxInstr Reset Driver' src='rfmxinstr_reset_driver.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_reset_entire_session.html language=enus -->
## TOPIC 00049: RFmxInstr Reset Entire Session (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_reset_entire_session.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_reset_entire_session.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Reset Entire Session (VI)

Owning Palette:

Utility

Deletes all the named signal in the session and resets all properties for the default signal instances of already loaded personalities in the session.

This VI disables all the calibration planes.

[IMAGE alt='RFmxInstr Reset Entire Session' src='rfmxinstr_reset_entire_session.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_reset_to_default.html language=enus -->
## TOPIC 00050: RFmxInstr Reset to Default (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_reset_to_default.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_reset_to_default.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Reset to Default (VI)

Owning Palette:

Utility

Resets the RFmxInstr properties to their default values.

This VI disables all the calibration planes.

[IMAGE alt='RFmxInstr Reset to Default' src='rfmxinstr_reset_to_default.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_save_all_configurations.html language=enus -->
## TOPIC 00051: RFmxInstr Save All Configurations (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_save_all_configurations.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_save_all_configurations.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Save All Configurations (VI)

Owning Palette:

Utility

Saves all the configured properties in the RFmx session to a file in the specified file path. Use this VI to save the current state of the RFmx session. On a MIMO session, this VI saves all the configured properties for the specified MIMO port.

|  | Note List configurations, reference waveforms and external attenuation tables are not saved by this VI. |
| --- | --- |

[IMAGE alt='RFmxInstr Save All Configurations' src='rfmxinstr_save_all_configurations.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | File Path specifies the complete path to the file to which the configurations are to be saved. Default file extension: .rfmxconfig |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_select_active_external_attenuation_table.html language=enus -->
## TOPIC 00052: RFmxInstr Select Active External Attenuation Table (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_select_active_external_attenuation_table.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_select_active_external_attenuation_table.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Select Active External Attenuation Table (VI)

Owning Palette:

External Attenuation Table

Activates the external attenuation table set by the **Table Name** parameter in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this VI selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Select Active External Attenuation Table' src='rfmxinstr_select_active_external_attenuation_table.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Table Name specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" |
|  | Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, the default "" (empty string) selects the active external attenuation table for all the MIMO Ports. To configure external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" |
|  | Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_self_calibrate.html language=enus -->
## TOPIC 00053: RFmxInstr Self Calibrate (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_self_calibrate.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_self_calibrate.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Self Calibrate (VI)

Owning Palette:

Calibration

Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this VI self-calibrates all NI-RFSA devices and associated modules that support self-calibration.

Refer to the specifications document for your device for more information about how often to self-calibrate. For more information about Self Calibrate, refer to the *niRFSA Self Cal VI* topic for your device in the *NI RF Vector Signal Analyzers Help*.

|  | Note For PXIe-5644/5645/5646, RFmx internally closes the RFSA session, performs self-calibration and opens a new session for the same device. If the RFSA session has been accessed from RFmx, using the RFmxInstr Get NIRFSA Session VI before calling the RFmxInstr Self Calibrate VI, the RFSA session will become invalid upon calling the RFmxInstr Self Calibrate. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Self Calibrate' src='rfmxinstr_self_calibrate.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Steps To Omit specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that all calibration steps are performed. The only valid value for PXIe-5820/5830/5831/5832/5840/5841/5842 is an empty array. Preselector Alignment (1) Omits the Preselector Alignment step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the preselector alignment specifications are not guaranteed. This step applies only to the PXIe-5605/5606. Gain Reference (2) Omits the Gain Reference step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. IF Flatness (4) Omits the IF Flatness step. If you omit this step and the niRFSA Is Self Cal, valid VI indicates the calibration data for this step is invalid, the IF flatness specifications are not guaranteed. Digitizer Self Cal (8) Omits the Digitizer Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. LO Self Cal (10) Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the LO PLL may fail to lock. Amplitude Accuracy (20) Not used by this VI. Residual LO Power (40) Not used by this VI. Image Suppression (80) Not used by this VI. Synthesizer Alignment (100) Not used by this VI. DC Offset (200) Not used by this VI. |
| Preselector Alignment (1) | Omits the Preselector Alignment step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the preselector alignment specifications are not guaranteed. This step applies only to the PXIe-5605/5606. |
| Gain Reference (2) | Omits the Gain Reference step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. |
| IF Flatness (4) | Omits the IF Flatness step. If you omit this step and the niRFSA Is Self Cal, valid VI indicates the calibration data for this step is invalid, the IF flatness specifications are not guaranteed. |
| Digitizer Self Cal (8) | Omits the Digitizer Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the absolute accuracy of the device is not guaranteed. |
| LO Self Cal (10) | Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the LO PLL may fail to lock. |
| Amplitude Accuracy (20) | Not used by this VI. |
| Residual LO Power (40) | Not used by this VI. |
| Image Suppression (80) | Not used by this VI. |
| Synthesizer Alignment (100) | Not used by this VI. |
| DC Offset (200) | Not used by this VI. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_self_calibrate_range.html language=enus -->
## TOPIC 00054: RFmxInstr Self Calibrate Range (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_self_calibrate_range.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_self_calibrate_range.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Self Calibrate Range (VI)

Owning Palette:

Calibration

Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this VI runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the *niRFSA Self Calibrate Range* VI topic for your device in the *NI RF Vector Signal Analyzers Help*. On a MIMO session, this VI self-calibrates all NI-RFSA devices and associated modules that support self-calibration.

**Supported devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

|  | Note This VI does not update self-calibration date and temperature. Self-calibration range data is not saved to your device if you restart the system. |
| --- | --- |

[IMAGE alt='RFmxInstr Self Calibrate Range' src='rfmxinstr_self_calibrate_range.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Steps To Omit specifies which calibration steps to skip during the self-calibration process. The default value is an empty array, which indicates that all calibration steps are performed. The only valid value for the PXIe-5820/5830/5831/5832/5840/5841/5842 is an empty array. Preselector Alignment (1) Not used by this VI. Gain Reference (2) Not used by this VI. IF Flatness (4) Not used by this VI. Digitizer Self Cal (8) Not used by this VI. LO Self Cal (10) Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the LO PLL may fail to lock. Amplitude Accuracy (20) Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted. Residual LO Power (40) Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted. Image Suppression (80) Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted. Synthesizer Alignment (100) Omits the VCO Alignment step. If you omit this step, the LO PLL will not get adjusted. DC Offset (200) Omits the DC Offset step. |
| Preselector Alignment (1) | Not used by this VI. |
| Gain Reference (2) | Not used by this VI. |
| IF Flatness (4) | Not used by this VI. |
| Digitizer Self Cal (8) | Not used by this VI. |
| LO Self Cal (10) | Omits the LO Self Cal step. If you omit this step and the niRFSA Is Self Cal Valid VI indicates the calibration data for this step is invalid, the LO PLL may fail to lock. |
| Amplitude Accuracy (20) | Omits the Amplitude Accuracy step. If you omit this step, the absolute accuracy of the device is not adjusted. |
| Residual LO Power (40) | Omits the Residual LO Power step. If you omit this step, the Residual LO Power performance is not adjusted. |
| Image Suppression (80) | Omits the Image Suppression step. If you omit this step, the Residual Sideband Image performance is not adjusted. |
| Synthesizer Alignment (100) | Omits the VCO Alignment step. If you omit this step, the LO PLL will not get adjusted. |
| DC Offset (200) | Omits the DC Offset step. |
|  | Min Frequency specifies the minimum frequency for the custom self calibration range. This value is expressed in Hz. Note For PXIe-5830/5831/5832, only the applicable ports within the specified frequency range are calibrated. |
|  | Note For PXIe-5830/5831/5832, only the applicable ports within the specified frequency range are calibrated. |
|  | Max Frequency specifies the maximum frequency for the custom self calibration range. This value is expressed in Hz. |
|  | Min Ref Level specifies the minimum reference level for the custom self calibration range. This value is expressed in dBm. |
|  | Max Ref Level specifies the maximum reference level for the custom self calibration range. This value is expressed dBm. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_send_software_edge_trigger.html language=enus -->
## TOPIC 00055: RFmxInstr Send Software Edge Trigger (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_send_software_edge_trigger.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_send_software_edge_trigger.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Send Software Edge Trigger (VI)

Owning Palette:

Configuration

Configures the software version of a trigger that you want to send.

#### RFmxInstr Send Software Edge Start Trigger

Sends a trigger to the waiting device when you choose a software version of Start trigger. You can also use this VI to override a hardware trigger.

This VI returns an error if:

- You configure an invalid trigger.
- You have not previously called the RFmx Initiate VI.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Send Software Edge Start Trigger' src='rfmxinstr_send_software_edge_start_trigger.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

#### RFmxInstr Send Software Edge Advance Trigger

Sends a trigger to the waiting device when you choose a software version of the Advance trigger. You can also use this VI to override a hardware trigger.

This VI returns an error if:

- You configure an invalid trigger.
- You have not previously called the RFmx Initiate VI.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

[IMAGE alt='RFmxInstr Send Software Edge Advance Trigger' src='rfmxinstr_send_software_edge_advance_trigger.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_vi_tree.html language=enus -->
## TOPIC 00056: RFmxInstr VI Tree (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_vi_tree.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_vi_tree.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr VI Tree (VI)

Owning Palette:

RFmxInstr VIs

Displays all the VIs available in RFmxInstr for instrument configuration and control. The VIs are organized in the order they must be used in the program you create.

[IMAGE alt='RFmxInstr VI Tree' src='rfmxinstr_vi_tree.gif']

<!--NI_TOPIC bundle=rfmx-instr-vi path=rfmxinstrvi/rfmxinstr_wait_for_acquisition_complete.html language=enus -->
## TOPIC 00057: RFmxInstr Wait for Acquisition Complete (VI)

- bundle_id: `rfmx-instr-vi`
- source_path: `rfmxinstrvi/rfmxinstr_wait_for_acquisition_complete.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-vi/raw/resource/enus/rfmxinstrvi/rfmxinstr_wait_for_acquisition_complete.html
- document_id: `rfmx-instr-vi`
- page_type: `leaf`
- content_type: ``

RFmxInstr Wait for Acquisition Complete (VI)

Owning Palette:

Utility

Waits and blocks the data flow until the acquisition is complete. This VI is typically called after a specific initiate VI.

[IMAGE alt='RFmxInstr Wait for Acquisition Complete' src='rfmxinstr_wait_for_acquisition_complete.gif']

|  | Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. |
| --- | --- |
|  | Timeout specifies the time to wait for an ongoing acquisition to complete before returning a timeout error. A value of -1 specifies that the VI waits indefinitely for acquisition to complete. This value is expressed in seconds. The default value is 10. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | Instrument Handle Out passes a reference of the instrument session to the next VI. |
|  | error out contains error information. This output provides standard error out functionality. |
