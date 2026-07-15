# NI DOCUMENT BUNDLE: veristand-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=veristand-labview-api-ref start=1 end=250 -->
<!--NI_TOPIC bundle=veristand-labview-api-ref path=api-reference.html language=unavailable -->
## TOPIC 00001: Api Reference

- bundle_id: `veristand-labview-api-ref`
- source_path: `api-reference.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/api-reference.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-asynchronous-channels-mnu.html language=enus -->
## TOPIC 00002: Asynchronous Device Channels

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-asynchronous-channels-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-asynchronous-channels-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Asynchronous Device Channels VIs to track input and output overflows on asynchronous custom devices. icon

### Asynchronous Device Channels

Use the Asynchronous Device Channels VIs to track input and output overflows on asynchronous custom devices.

[IMAGE alt='icon' src='configuration-asynchronous-channels-mnu.png']

- [NI VeriStand - Add Input Overflow Count Channel VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-add-input-overflow-count-channel-vi.html) Adds an input overflow count channel to the device or device subsection specified by Parent Ref in . Input overflow count channels track the number of times the system fails to write data to an asynchronous custom device because the FIFO is full. A custom device can have only one input overflow count channel.
- [NI VeriStand - Add Output Underflow Count Channel VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-add-output-underflow-count-channel-vi.html) Adds an output underflow count channel to the device or device subsection specified by Parent Ref in . Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output underflow count channel.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-channel-properties-mnu.html language=enus -->
## TOPIC 00003: Channel Properties

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-channel-properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-channel-properties-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Channel Properties VIs to set properties of custom device channels, such as types, default values, units, faultability, and scalability. icon

### Channel Properties

Use the Channel Properties VIs to set properties of custom device channels, such as types, default values, units, faultability, and scalability.

[IMAGE alt='icon' src='configuration-channel-properties-mnu.png']

- [NI VeriStand - Set Custom Device Channel Default Value VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-default-value-vi.html) Sets the Default Value for the channel specified by Channel Ref in . The channel retains the Default Value until it receives a new value.
- [NI VeriStand - Set Custom Device Channel Type VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-type-vi.html) Sets whether the channel specified by Channel Ref in is an Input or an Output channel. Input channels receive values from the VeriStand Engine. Output channels send values to the VeriStand Engine.
- [NI VeriStand - Set Custom Device Channel Units VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-units-vi.html) Sets the units of measurement for a channel. Units can be any string that makes sense for your custom device.
- [NI VeriStand - Set Custom Device Channel Scalability VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-scalability-vi.html) Specifies whether you can scale a channel using the Channel Scaling & Calibration tool. Set Scalability to TRUE if the channel is a hardware channel that might require calibration or scaling into specific engineering units.
- [NI VeriStand - Set Custom Device Channel Faultability VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-faultability-vi.html) Specifies whether the VeriStand Engine can fault a channel using software fault insertion.

Parent topic:

Configuration

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-dependencies-mnu.html language=unavailable -->
## TOPIC 00004: Configuration Dependencies Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-dependencies-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-dependencies-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-asynchronous-device-properties-mnu.html language=unavailable -->
## TOPIC 00005: Configuration Device Properties Asynchronous Device Properties Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-asynchronous-device-properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-asynchronous-device-properties-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-mnu.html language=unavailable -->
## TOPIC 00006: Configuration Device Properties Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-timing-and-sync-device-properties-mnu.html language=unavailable -->
## TOPIC 00007: Configuration Device Properties Timing And Sync Device Properties Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-timing-and-sync-device-properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-timing-and-sync-device-properties-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-mnu.html language=enus -->
## TOPIC 00008: Configuration

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Configuration VIs to configure custom devices. You can add channels, sections, and dependencies, get and set information about items that appear under the device in the System Explorer window configuration tree, configure custom System Explorer window configuration pages for items, and confi

### Configuration

Use the Configuration VIs to configure custom devices. You can add channels, sections, and dependencies, get and set information about items that appear under the device in the **System Explorer** window configuration tree, configure custom **System Explorer** window configuration pages for items, and configure loop and timing information for asynchronous and timing and sync devices, respectively.

[IMAGE alt='icon' src='configuration-mnu.png']

- [NI VeriStand - Add Custom Device Channel VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-channel-vi.html) Adds a channel to the device or device subsection specified by Parent Ref in . If the Channel Name you specify already exists, this VI updates the Channel information ( Type , Units , etc.), properties, and the GUID for the configuration page.
- [NI VeriStand - Get Custom Device Channel Data VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-data-vi.html) Returns information about the channel specified by Channel Ref in .
- [NI VeriStand - Add Custom Device Section VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-section-vi.html) Adds a section with the name Section Name to the device specified by Parent Ref in . If the Section Name you specify already exists for that device, this VI updates the page GUID and the values of any properties.
- [NI VeriStand - Add Custom Device Waveform VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-waveform-vi.html) Adds a waveform item to the device or device subsection specified by Parent Ref in . If the Waveform Name you specify already exists, this VI updates the Waveform information ( Data Type , Units , etc.), properties, and the GUID for the configuration page.
- [NI VeriStand - Rename Custom Device Item VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-rename-custom-device-item-vi.html) Applies a New Name to the item specified by Item Ref in . If the New Name you specify already exists in the same section, this VI does nothing and the Request invalid? indicator returns TRUE.
- [NI VeriStand - Remove Custom Device Item VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-custom-device-item-vi.html) Removes the item specified by Item Ref in , along with any child items.
- [NI VeriStand - Move Custom Device Item VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-move-custom-device-item-vi.html) Moves a custom device item to a new location within the custom device hierarchy. For example, you can use this VI to move a channel from one section to another. If you try to move an item to a location outside of its owning custom device, this VI returns an error.
- [NI VeriStand - Get Custom Device Waveform Data VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-data-vi.html) Returns information about the waveform item specified by Waveform Ref in .
- [Asynchronous Device Channels](../../../../../menus/categories/ni-veristand/core/custom-device-api/configuration-asynchronous-channels-mnu.html) Use the Asynchronous Device Channels VIs to track input and output overflows on asynchronous custom devices.
- [Channel Properties](../../../../../menus/categories/ni-veristand/core/custom-device-api/configuration-channel-properties-mnu.html) Use the Channel Properties VIs to set properties of custom device channels, such as types, default values, units, faultability, and scalability.
- [Dependencies](../../../../../menus/categories/ni-veristand/core/custom-device-api/configuration-dependencies-mnu.html) Use the Dependencies VIs to manage the dependencies of a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you want to deploy to the target along with the custom device.
- [Item Properties](../../../../../menus/categories/ni-veristand/core/custom-device-api/item-properties-mnu.html) Use the Item Properties VIs to get and set properties of custom device items. A custom device item is anything that appears in the System Explorer window configuration tree, such as a channel within a custom device or the custom device itself.
- [Waveform Properties](../../../../../menus/categories/ni-veristand/core/custom-device-api/configuration-waveform-properties-mnu.html) Use the VIs on this palette to set properties of waveform items associated with a custom device, such as the data type and units.

Parent topic:

Custom Device API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/configuration-waveform-properties-mnu.html language=enus -->
## TOPIC 00009: Waveform Properties

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/configuration-waveform-properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/configuration-waveform-properties-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to set properties of waveform items associated with a custom device, such as the data type and units. icon

### Waveform Properties

Use the VIs on this palette to set properties of waveform items associated with a custom device, such as the data type and units.

[IMAGE alt='icon' src='configuration-waveform-properties-mnu.png']

- [NI VeriStand - Set Custom Device Waveform Data Type VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-data-type-vi.html) Sets whether the waveform data measured or generated is in double-precision floating-point form or complex double-precision floating-point form.
- [NI VeriStand - Set Custom Device Waveform Units VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-units-vi.html) Sets the units of measurement for a waveform. Units can be any string that makes sense for your custom device.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/custom-device-api-data-references-mnu.html language=enus -->
## TOPIC 00010: Data References

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/custom-device-api-data-references-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/custom-device-api-data-references-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Data References VIs in the RT Driver VI of an inline custom device to get and set custom device channel values. Do not use these VIs outside of an inline custom device. icon

### Data References

Use the Data References VIs in the RT Driver VI of an inline custom device to get and set custom device channel values. Do not use these VIs outside of an inline custom device.

[IMAGE alt='icon' src='custom-device-api-data-references-mnu.png']

- [NI VeriStand - Get Channel Data Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-data-reference-vi.html) Returns a 32-bit Channel Data Reference to the inline custom device channel specified by Channel Ref in . You can use the reference this VI returns with the Get Channel Value by Data Reference and Set Channel Value by Data Reference VIs.
- [NI VeriStand - Get Channel Block Data References VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-block-data-references-vi.html) Returns an array of 32-bit data references to the inline custom device channels specified by Channel Refs . This VI also returns the channel values. You can use the Block Data Refs with the Get Channel Values by Block Data Reference and Set Channel Values by Block Data Reference VIs.
- [NI VeriStand - Get Channel Value by Data Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-value-by-data-reference-vi.html) Returns the value of the custom device channel specified by Data Reference in . Use the Get Channel Data Reference VI to get the channel data reference for this VI. You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.
- [NI VeriStand - Get Channel Values by Block Data Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-values-by-block-data-reference-vi.html) Returns the values of the inline custom device channels specified by Block Data Ref . You can use this VI to get multiple channel values at one time. Use the Get Channel Block Data References VI to get the channel data references for this VI. You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.
- [NI VeriStand - Set Channel Value by Data Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-value-by-data-reference-vi.html) Sets the value of the custom device channel specified by Data Reference in . Use the Get Channel Data Reference VI to get the channel data reference for this VI. You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.
- [NI VeriStand - Set Channel Values by Block Data Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-values-by-block-data-reference-vi.html) Sets the values of the inline custom device channels specified by Block Data Ref . You can use this VI to get multiple channel values at one time. Use the Get Channel Block Data References VI to get the channel data references for this VI. You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/custom-device-api-mnu.html language=unavailable -->
## TOPIC 00011: Custom Device Api Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/custom-device-api-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/custom-device-api-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/custom-device-api-utilities-mnu.html language=enus -->
## TOPIC 00012: Utilities

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/custom-device-api-utilities-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/custom-device-api-utilities-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the custom device Utilities VIs to perform various functions within custom devices, such as adding sections, getting item and target references, and searching for items. icon

### Utilities

Use the custom device Utilities VIs to perform various functions within custom devices, such as adding sections, getting item and target references, and searching for items.

[IMAGE alt='icon' src='custom-device-api-utilities-mnu.png']

- [NI VeriStand - Search for Item VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.
- [NI VeriStand - Get Item Ref by Relative Path VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-item-ref-by-relative-path-vi.html) Returns a reference to a custom device item from a specified location relative to Section Ref in . Use one forward slash (/) as a separator between sections in the relative path. Like a standard file system, ".." traverses up the hierarchy one level. A leading forward slash indicates an absolute path from the root item of the hierarchy.
- [NI VeriStand - Get Target Ref VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-target-ref-vi.html) Gets a reference to the target on which the custom device that contains Item Ref in is running.
- [NI VeriStand - Not a Ref VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-not-a-ref-vi.html) Gets whether the Item Ref you specify is a valid reference.
- [NI VeriStand - Add Sections Recursively by Relative Path VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-add-sections-recursively-by-relative-path-vi.html) Recursively adds sections to a custom device section relative to the item specified by Section Ref in . This VI also sets the GUIDs for the configuration pages to associate with the new sections. If a section with the name you specify already exists, this VI does not overwrite the section.
- [NI VeriStand - Set Multiple Dependent Node Refs VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-set-multiple-dependent-node-refs-vi.html) Sets multiple properties, with dependent node references as values, on a custom device item. Dependent node references map to other nodes in the custom device, such as channels from which properties get their values.
- [NI VeriStand - Get Multiple Dependent Node Refs VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-multiple-dependent-node-refs-vi.html) Gets the dependent node references that are set as values for properties of an item you specify. Dependent node references map to other nodes in the custom device, such as channels from which properties get their values. All the properties must share the same base name. This VI increments a decimal appended to the Base Property Name until it cannot find any more properties.
- [NI VeriStand - Ref Constants VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-ref-constants-vi.html) Creates a global variable that you can use as a reference to the root item in the custom device hierarchy, or as an invalid reference.
- [NI VeriStand - Highlight Node in System Explorer VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-highlight-node-in-system-explorer-vi.html) Highlights a custom device item in the System Explorer window configuration tree.
- [NI VeriStand - Advanced Browsing Dialog VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-advanced-browsing-dialog-vi.html) Configures an advanced browsing dialog box for files that match the File Pattern you specify. This VI creates the same style browsing dialog that appears in NI VeriStand if you select Advanced browsing on the Folder Start Paths page of the Options dialog box.
- [NI VeriStand - Get Next Unique Label VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-next-unique-label-vi.html) Searches under the Parent Ref you specify for a base Label you specify and returns the next valid, or unused, full label that uses that base. This VI assumes that a valid full label is the base label with an incremented number appended to it.
- [NI VeriStand - Report Final Error Status VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-report-final-error-status-vi.html) Reports a final error status from an asynchronous custom device to the VeriStand Engine. The VeriStand Engine checks the error status when the system shuts down.
- [NI VeriStand - Get Channel FIFO Buffer Index VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-channel-fifo-buffer-index-vi.html) Gets the FIFO buffer index for the custom device channel specified by Channel Ref and determines which FIFO Buffer (input or output) contains the channel. Use this VI to determine which index to read or write a channel value to in the FIFO arrays for an asynchronous custom device. Use this VI with channels of asynchronous custom devices only.
- [NI VeriStand - Get All Channels VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-channels-vi.html) Gets an array of channel references for all the channels within the section specified by Section Ref in . The array includes references to both input and output channels. This VI performs a depth-first deep search.
- [NI VeriStand - Get All Waveforms VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-waveforms-vi.html) Gets an array of references for all the waveforms within the custom-device section specified by Section Ref in . This VI performs a depth-first deep search.
- [NI VeriStand - System Definition File Path VI](../../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-system-definition-file-path-vi.html) Returns the file path to the active NI VeriStand system definition file (.nivssdf) after the system definition is deployed.

Parent topic:

Custom Device API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/custom-device-api-waveform-data-mnu.html language=enus -->
## TOPIC 00013: Waveform Data

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/custom-device-api-waveform-data-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/custom-device-api-waveform-data-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: After you add a waveform to a custom device, use the VIs on this palette to publish waveform data or read waveform data from other sources in the VeriStand Engine for the custom device. icon

### Waveform Data

After you add a waveform to a custom device, use the VIs on this palette to publish waveform data or read waveform data from other sources in the VeriStand Engine for the custom device.

[IMAGE alt='icon' src='custom-device-api-waveform-data-mnu.png']

- [NI VeriStand - Get Waveform Data Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-waveform-data-reference-vi.html) Returns a data reference for a specific waveform item in a custom device. Use waveform data references to open a session that reads from or writes to the waveform.
- [NI VeriStand - Open Waveform Session VI](../../../../../vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-open-waveform-session-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Close Waveform Session VI](../../../../../vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-close-waveform-session-vi.html) Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use.
- [NI VeriStand - Start Waveform(s) VI](../../../../../vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-start-waveform-s-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.
- [NI VeriStand - Read Waveform(s) VI](../../../../../vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-read-waveform-s-vi.html) Reads data from a waveform(s) associated with the specified read session.
- [NI VeriStand - Write Waveform(s) VI](../../../../../vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-write-waveform-s-vi.html) Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again with a different start time.

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/item-properties-mnu.html language=enus -->
## TOPIC 00014: Item Properties

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/item-properties-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/item-properties-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Item Properties VIs to get and set properties of custom device items. A custom device item is anything that appears in the System Explorer window configuration tree, such as a channel within a custom device or the custom device itself. icon

### Item Properties

Use the Item Properties VIs to get and set properties of custom device items. A custom device item is anything that appears in the **System Explorer** window configuration tree, such as a channel within a custom device or the custom device itself.

[IMAGE alt='icon' src='item-properties-mnu.png']

- [NI VeriStand - Set Item Property VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-property-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [NI VeriStand - Set Item Description VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-description-vi.html) Sets the Description for an item.
- [NI VeriStand - Set Item GUID VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-guid-vi.html) Sets the GUID of the configuration page to associate with an item. You can use this VI to change the page associated with an item at run time.
- [NI VeriStand - Remove Item Property VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-item-property-vi.html) Removes the property specified by Property Name from a custom device item.
- [NI VeriStand - Get Item Property VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-property-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [NI VeriStand - Get Item Description VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-description-vi.html) Returns the Description of an item.
- [NI VeriStand - Get Item GUID VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-guid-vi.html) Returns the GUID of the configuration page associated with a custom device item, as defined in the custom device XML file.
- [NI VeriStand - Get Property Names List VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-property-names-list-vi.html) Returns all the Property Names of the properties associated with a custom device item.
- [NI VeriStand - Set Log File Producer Flag VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-set-log-file-producer-flag-vi.html) Sets a property for the specified custom device item that indicates whether the item produces log files. When TRUE, you can use the Data Logging control to download log files produced by the item.
- [Device Properties](../../../../../menus/categories/ni-veristand/core/custom-device-api/configuration-device-properties-mnu.html) Use the Device Properties VIs to get and set properties of a custom device, such as its execution mode, version, and driver VI.
- [Channel Properties](../../../../../menus/categories/ni-veristand/core/custom-device-api/configuration-channel-properties-mnu.html) Use the Channel Properties VIs to set properties of custom device channels, such as types, default values, units, faultability, and scalability.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/run-time-utilities-mnu.html language=enus -->
## TOPIC 00015: Driver Functions

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/run-time-utilities-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/run-time-utilities-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Driver Functions VIs to return lists of channels, convert Timed Loop priority values into numbers, and return the name of a Timed Loop. icon

### Driver Functions

Use the Driver Functions VIs to return lists of channels, convert Timed Loop priority values into numbers, and return the name of a Timed Loop.

[IMAGE alt='icon' src='run-time-utilities-mnu.png']

- [NI VeriStand - Get Custom Device Channel List VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-list-vi.html) Returns an array of references to all the input or output channels of a custom device.
- [NI VeriStand - Get Asynchronous Driver VI Timed Loop Name VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-asynchronous-driver-vi-timed-loop-name-vi.html) Returns the name of the Timed Loop that an asynchronous custom device uses. The VeriStand Engine synchronizes the start of this Timed Loop with the other system Timed Loops. Use the Timed Loop name this VI returns to ensure this synchronization occurs successfully.
- [NI VeriStand - Convert Timed Loop Priority to Number VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-convert-timed-loop-priority-to-number-vi.html) Converts a priority value (Low, Medium, or High) for the Timed Loop in which an asynchronous custom device runs into a numeric value that the Input node of a Timed Loop accepts. Use the NI VeriStand - Get Timed Loop Priority VI to get the priority value. You can use the NI VeriStand - Set Timed Loop Priority VI to set the priority value for a custom device Timed Loop.
- [NI VeriStand - Get Engine Rate VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-engine-rate-vi.html) Returns the target's Primary Control Loop rate in hertz. This VI will search for the owning target of the node passed in. If you pass a target node, it will return the target's rate.
- [NI VeriStand - Register Custom Device Engine Events VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-register-custom-device-engine-events-vi.html) Dynamically registers custom device engine events. This VI registers the events Shut Down, Message (Byte Array), and Message (String). The Shut Down event is triggered when the custom device engine shuts down. The Message events trigger when the NI VeriStand - Send Custom Device Message VI or a corresponding .NET method is called.
- [NI VeriStand - Get Custom Device Waveform List VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-list-vi.html) Returns an array of references to all the waveforms a custom device contains.
- [Waveform Data](../../../../../menus/categories/ni-veristand/core/custom-device-api/custom-device-api-waveform-data-mnu.html) After you add a waveform to a custom device, use the VIs on this palette to publish waveform data or read waveform data from other sources in the VeriStand Engine for the custom device.
- [Data References](../../../../../menus/categories/ni-veristand/core/custom-device-api/custom-device-api-data-references-mnu.html) Use the Data References VIs in the RT Driver VI of an inline custom device to get and set custom device channel values. Do not use these VIs outside of an inline custom device.
- [NI VeriStand - Notify New Log Files Complete VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-notify-new-log-files-complete-vi.html) Sends a notification to clients connected through the VeriStand Gateway that the specified custom device item completed a new log file.
- [NI VeriStand - Get SLSC Module Name VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-slsc-module-name-vi.html) Returns the SLSC module name that represents a custom device in System Explorer.

Parent topic:

Custom Device API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/system-explorer-utilities-mnu.html language=enus -->
## TOPIC 00016: System Explorer Functions

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/system-explorer-utilities-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/system-explorer-utilities-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the System Explorer Functions VIs to interact with the System Explorer window. icon

### System Explorer Functions

Use the System Explorer Functions VIs to interact with the **System Explorer** window.

[IMAGE alt='icon' src='system-explorer-utilities-mnu.png']

- [NI VeriStand - Unset Busy Cursor VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-unset-busy-cursor-vi.html) Releases the front panel cursor of the System Explorer window. Use this VI after a Page VI finishes initializing.
- [NI VeriStand - Signal When Ready for Shutdown VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-signal-when-ready-for-shutdown-vi.html) Signals that the System Explorer window is ready to go into idle mode. Ensure all changes are saved before calling this VI.
- [NI VeriStand - Get Event Refnum VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-event-refnum-vi.html) Returns a registered event refnum that the custom device Configuration VI, which is called when a user instantiates a new instance of a custom device, uses to respond to System Explorer window events.
- [NI VeriStand - Parse Incoming Command Data VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-parse-incoming-command-data-vi.html) Parses a System Explorer window user event and returns the appropriate Action command. You can wire the Action output to a Case Structure to configure how to respond to each command.
- [NI VeriStand - Pointer to Item Reference VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-pointer-to-item-reference-vi.html) Converts a pointer to a node in the system definition file into an item reference for the same node. You can use this VI to switch from the System Explorer .NET API to the Custom Device API VIs available in LabVIEW. The .NET API uses pointers to nodes. The LabVIEW VIs use references to items.
- [NI VeriStand - Item Reference to Pointer VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-item-reference-to-pointer-vi.html) Converts a reference to an item, or node, in a system definition file into a pointer to the same node. You can use this VI to switch from the Custom Device API VIs available in LabVIEW to the System Explorer .NET API. The .NET API uses pointers to nodes. The LabVIEW VIs use references to items.
- [NI VeriStand - Enable Dynamic Button VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-dynamic-button-vi.html) Enables a custom toolbar button for an item's System Explorer window configuration page. You can use this VI to only display the button when certain conditions are met.
- [NI VeriStand - Disable Dynamic Button VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-disable-dynamic-button-vi.html) Disables a custom toolbar button for an item's System Explorer window configuration page. Disabled buttons do not appear in the toolbar. You can use this VI to hide a button.
- [NI VeriStand - Enable System Explorer Update Buffer VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-system-explorer-update-buffer-vi.html) Enables the buffer for updates to the System Explorer window. Using this VI together with the Commit System Explorer Update Buffer VI can speed up item creation if you are creating or updating multiple custom device items at one time.
- [NI VeriStand - Commit System Explorer Update Buffer VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-commit-system-explorer-update-buffer-vi.html) Commits updates to the System Explorer window. Using this VI together with the Enable System Explorer Update Buffer VI can speed up item creation if you are creating or updating multiple custom device items at one time.

Parent topic:

Custom Device API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/custom-device-api/system-navigation-mnu.html language=enus -->
## TOPIC 00017: Navigation

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/custom-device-api/system-navigation-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/custom-device-api/system-navigation-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Navigation VIs to return references to items, parent items, and child items. icon

### Navigation

Use the Navigation VIs to return references to items, parent items, and child items.

[IMAGE alt='icon' src='system-navigation-mnu.png']

- [NI VeriStand - Get Item Children VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-children-vi.html) Returns a list of references to all child items of the item specified by Item Ref in . This list can include subsections and channels.
- [NI VeriStand - Get Item Parent VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-parent-vi.html) Returns a reference to the parent item of the item specified by Item Ref in .
- [NI VeriStand - Get Item Reference by Name VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-name-vi.html) Searches for Item Name in the device or section specified by Parent Ref in and, if found, returns a reference to the item.
- [NI VeriStand - Get Item Reference by Path VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-path-vi.html) Returns a reference to the custom device item specified by Item Path in .
- [NI VeriStand - Get Item Path VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-path-vi.html) Returns the System Explorer path to the custom device item specified by Item Ref in .
- [NI VeriStand - Get Item Data VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-data-vi.html) Returns information about the custom device item specified by Item Ref in , including the name of the item, the GUID of the associated configuration page, and whether the item is a channel.
- [NI VeriStand - Get Target Type VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-target-type-vi.html) Gets the type, or operating system, of the target on which a custom device is running.
- [NI VeriStand - Find next valid Label VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-find-next-valid-label-vi.html) Searches the custom device hierarchy for the Label you specify and determines whether another item is already using the label. If the label already is in use, this VI adds a value to the end of the label and increments that value until it finds a label that is not in use. Use this VI to avoid accidentally overwriting custom device items by specifying duplicate label names.
- [NI VeriStand - Get Item Root VI](../../../../../vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-root-vi.html) Returns the root node in the system definition file.

Parent topic:

Custom Device API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/alarm-manager-mnu.html language=unavailable -->
## TOPIC 00018: Alarm Manager Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/alarm-manager-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/alarm-manager-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/alarm-mnu.html language=unavailable -->
## TOPIC 00019: Alarm Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/alarm-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/alarm-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/api-mnu.html language=enus -->
## TOPIC 00020: Execution API

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/api-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/api-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Execution VIs to automate the operation of an NI VeriStand application. For example, you can control models running on the target, configure alarm states and read data from alarms, and access Workspace tools. icon

### Execution API

Use the Execution VIs to automate the operation of an NI VeriStand application. For example, you can control models running on the target, configure alarm states and read data from alarms, and access Workspace tools.

[IMAGE alt='icon' src='api-mnu.png']

- [Workspace](../../../../../menus/categories/ni-veristand/core/execution/workspace-mnu.html) Use the Workspace VIs to perform basic workspace operations such as getting and setting channel data.
- [Stimulus Profile](../../../../../menus/categories/ni-veristand/core/execution/stimulus-mnu.html) Use Stimulus Profile VIs to observe and control the stimulus profile manager and stimulus profile files.
- [Channel Fault](../../../../../menus/categories/ni-veristand/core/execution/channel-fault-manager-mnu.html) Use Channel Fault VIs to view, set, and clear channel faults.
- [Models](../../../../../menus/categories/ni-veristand/core/execution/model-manager-mnu.html) Use the Models VIs to control and observe models running on the target.
- [Alarms](../../../../../menus/categories/ni-veristand/core/execution/alarm-manager-mnu.html) Use the Alarms VIs to control and observe alarms on the target.
- [Project](../../../../../menus/categories/ni-veristand/core/execution/project-mnu.html) Use the Project VIs to open, deploy, undeploy, and control an NI VeriStand project, and to interact with the NI VeriStand Workspace window and tools.
- [Custom Device Communication](../../../../../menus/categories/ni-veristand/core/execution/custom-devices-mnu.html) Use the Custom Device Communication VIs to communicate with a custom device by sending messages or commands to the device.
- [Calibration](../../../../../menus/categories/ni-veristand/core/execution/calibration-mnu.html) Use the Calibration VIs to add and remove calibrations from hardware channels, and to read raw values from calibrated channels.
- [Waveform Streaming](../../../../../menus/categories/ni-veristand/core/execution/waveform-mnu.html) Use the VIs on this palette to stream waveform data being acquired or generated in an NI VeriStand system to a LabVIEW application.
- [Data Logging](../../../../../menus/categories/ni-veristand/core/execution/data-logging-mnu.html) Use the Data Logging VIs to configure and control host-side data logging operations. These VIs enable you to log channel data from a target to a file on the host computer while a system definition runs on the target. Use these VIs to log data from real-time sequences when you execute stimulus profiles.

Parent topic:

NI VeriStand

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/calibration-mnu.html language=enus -->
## TOPIC 00021: Calibration

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/calibration-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Calibration VIs to add and remove calibrations from hardware channels, and to read raw values from calibrated channels. icon

### Calibration

Use the Calibration VIs to add and remove calibrations from hardware channels, and to read raw values from calibrated channels.

[IMAGE alt='icon' src='calibration-mnu.png']

- [NI VeriStand - Open Calibration Reference VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-open-calibration-reference-vi.html) Opens a reference to the calibration manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.
- [NI VeriStand - Close Calibration Reference VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-close-calibration-reference-vi.html) Closes an open reference to the calibration tool on the VeriStand Gateway. Use this VI to close each calibration manager reference that you open with the Open Calibration Reference VI.
- [NI VeriStand - Get Raw Value VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-value-vi.html) Returns the value the specified channel measures or generates before NI VeriStand applies any calibration or scaling.
- [NI VeriStand - Get Raw Values VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-values-vi.html) Returns the values the specified channels measure or generate before NI VeriStand applies any calibration or scaling.
- [NI VeriStand - Set Calibration VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-set-calibration-vi.html) Applies a polynomial calibration to the specified channel, as defined by the Coefficients you specify.
- [NI VeriStand - Get Calibration VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-get-calibration-vi.html) Returns the coefficients of a polynomial calibration applied to the specified channel.
- [NI VeriStand - Remove Calibration VI](../../../../../vi-lib/ni-veristand/execution/calibration/ni-veristand-remove-calibration-vi.html) Removes the calibration applied to the specified channel.

Parent topic:

Execution API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/channel-fault-manager-mnu.html language=unavailable -->
## TOPIC 00022: Channel Fault Manager Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/channel-fault-manager-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/channel-fault-manager-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/custom-devices-mnu.html language=unavailable -->
## TOPIC 00023: Custom Devices Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/custom-devices-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/custom-devices-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/data-logging-configuration-advanced-mnu.html language=enus -->
## TOPIC 00024: Advanced

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/data-logging-configuration-advanced-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/data-logging-configuration-advanced-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the data logging configuration Advanced VIs to specify a minimum size for the data buffer and to configure attributes of completed log files. icon

### Advanced

Use the data logging configuration Advanced VIs to specify a minimum size for the data buffer and to configure attributes of completed log files.

[IMAGE alt='icon' src='data-logging-configuration-advanced-mnu.png']

- [Set Minimum Buffer Size VI](../../../../../vi-lib/ni-veristand/execution/datalogging/set-minimum-buffer-size-vi.html) Sets the minimum size of the buffer for logged data. Increasing the minimum buffer size can improve logging performance but requires additional memory resources. Decreasing the minimum buffer size can result in much larger TDMS and TDMS index files. Consider setting the minimum buffer size to at least 256 when logging data to TDMS files at high rates.
- [Set Completed File Attributes VI](../../../../../vi-lib/ni-veristand/execution/datalogging/set-completed-file-attributes-vi.html) Specifies whether log files in the specified data logging specification are set to read-only on completion.

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/data-logging-configuration-mnu.html language=unavailable -->
## TOPIC 00025: Data Logging Configuration Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/data-logging-configuration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/data-logging-configuration-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/data-logging-events-mnu.html language=enus -->
## TOPIC 00026: Events

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/data-logging-events-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/data-logging-events-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the data logging Events VIs to register and unregister for data logging events from the VeriStand Gateway. icon

### Events

Use the data logging Events VIs to register and unregister for data logging events from the VeriStand Gateway.

[IMAGE alt='icon' src='data-logging-events-mnu.png']

- [Register Data Logging Events VI](../../../../../vi-lib/ni-veristand/execution/datalogging/register-data-logging-events-vi.html) Registers for data logging events from the VeriStand Gateway. This VI returns a registered user event reference and information about the event.
- [Unregister Data Logging Events VI](../../../../../vi-lib/ni-veristand/execution/datalogging/unregister-data-logging-events-vi.html) Unregisters for data logging events from the VeriStand Gateway.

Parent topic:

Data Logging

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/data-logging-mnu.html language=enus -->
## TOPIC 00027: Data Logging

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/data-logging-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/data-logging-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Data Logging VIs to configure and control host-side data logging operations. These VIs enable you to log channel data from a target to a file on the host computer while a system definition runs on the target. Use these VIs to log data from real-time sequences when you execute stimulus profil

### Data Logging

Use the Data Logging VIs to configure and control host-side data logging operations. These VIs enable you to log channel data from a target to a file on the host computer while a system definition runs on the target. Use these VIs to log data from real-time sequences when you execute stimulus profiles.

[IMAGE alt='icon' src='data-logging-mnu.png']

- [Open Data Logging Manager Reference VI](../../../../../vi-lib/ni-veristand/execution/datalogging/open-data-logging-manager-reference-vi.html) Opens a connection to the data logging service on the VeriStand Gateway. You must open a reference to the Data Logging Manager to enable the host computer to log data from a target while a system definition is deployed and running.
- [Start Data Logging Session VI](../../../../../vi-lib/ni-veristand/execution/datalogging/start-data-logging-session-vi.html) Starts the data logging session specified by Data Logging Specification in . Use Session Name in to specify a unique name for the data logging session. You use this name to query and control logging operations during the logging session.
- [Close Data Logging Manager Reference VI](../../../../../vi-lib/ni-veristand/execution/datalogging/close-data-logging-manager-reference-vi.html) Closes the connection to the data logging service on the VeriStand Gateway.
- [Stop Data Logging Session VI](../../../../../vi-lib/ni-veristand/execution/datalogging/stop-data-logging-session-vi.html) Stops the data logging session specified by Session Name in and returns the paths to all log files generated during the session. This VI attempts to stop the data logging session regardless of any incoming errors.
- [Configuration](../../../../../menus/categories/ni-veristand/core/execution/data-logging-configuration-mnu.html) Use the data logging Configuration VIs to configure host-side logging operations in NI VeriStand. For example, you can use these VIs to specify the names, formats, and locations of log files, configure start and stop triggers, and set the rate of a logging operation.
- [Status](../../../../../menus/categories/ni-veristand/core/execution/data-logging-status-mnu.html) Use the data logging Status VIs to get information about the status of a host-side data logging operation. For example, you can access current or completed log files, get information about the current logging session, or get error information.
- [Events](../../../../../menus/categories/ni-veristand/core/execution/data-logging-events-mnu.html) Use the data logging Events VIs to register and unregister for data logging events from the VeriStand Gateway.

Parent topic:

Execution API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/data-logging-status-mnu.html language=enus -->
## TOPIC 00028: Status

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/data-logging-status-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/data-logging-status-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the data logging Status VIs to get information about the status of a host-side data logging operation. For example, you can access current or completed log files, get information about the current logging session, or get error information. icon

### Status

Use the data logging Status VIs to get information about the status of a host-side data logging operation. For example, you can access current or completed log files, get information about the current logging session, or get error information.

[IMAGE alt='icon' src='data-logging-status-mnu.png']

- [Get Completed Log Files VI](../../../../../vi-lib/ni-veristand/execution/datalogging/get-completed-log-files-vi.html) Gets the paths to all the log files created during the logging session specified by Session Name in .
- [Get Current Log File Info VI](../../../../../vi-lib/ni-veristand/execution/datalogging/get-current-log-file-info-vi.html) Gets information about the file to which Session Name in is currently logging data. If the session is not actively logging data to a file, Log File Path returns an empty array.
- [Get Data Logging Session Specification VI](../../../../../vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-specification-vi.html) Gets the reference to the data logging specification specified by Session Name in .
- [Get Data Logging Session State VI](../../../../../vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-state-vi.html) Gets the current state of the data logging specification specified by Session Name in .
- [Get Last Error VI](../../../../../vi-lib/ni-veristand/execution/datalogging/get-last-error-vi.html) Gets the last error returned by the data logging specification specified by Session Name in .

Parent topic:

Data Logging

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/macro-player-mnu.html language=enus -->
## TOPIC 00029: Macro Player

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/macro-player-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/macro-player-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Macro Player VIs to interact with the Macro Player tool on the VeriStand Gateway. You can use these VIs to load a macro (.nivsmacro) file you created using the Macro Recorder VIs or the Macro Recorder tool in NI VeriStand and to play back the commands NI VeriStand sent to an RT target or des

### Macro Player

Use the Macro Player VIs to interact with the Macro Player tool on the VeriStand Gateway. You can use these VIs to load a macro (.nivsmacro) file you created using the Macro Recorder VIs or the Macro Recorder tool in NI VeriStand and to play back the commands NI VeriStand sent to an RT target or desktop PC during the time the Macro Recorder ran.

[IMAGE alt='icon' src='macro-player-mnu.png']

- [NI VeriStand - Open Macro Player Reference VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-macro-player-reference-vi.html) Opens a reference to the Macro Player tool on the VeriStand Gateway. The Macro Player plays back macro files you record using the Macro Recorder VIs. You must open a reference to the Macro Player before using any other VIs on this palette.
- [NI VeriStand - Run Macro Player VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-run-macro-player-vi.html) Runs the Macro Player tool and specifies the speed at which to play back macro files you record using the Macro Recorder VIs or the Macro Recorder tool in NI VeriStand.
- [NI VeriStand - Stop Macro Player VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-stop-macro-player-vi.html) Stops the Macro Player. This VI returns the Macro Player to the idle state and resets the macro you are playing back to the beginning of the recording. If you want to be able to resume playback from the place where you stop it, use the Pause Macro Player VI instead.
- [NI VeriStand - Close Macro Player Reference VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-macro-player-reference-vi.html) Closes an open reference to the Macro Player tool on the VeriStand Gateway. Use this VI to close each Macro Player reference that you open with the Open Macro Player Reference VI.
- [NI VeriStand - Load Macro VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-load-macro-vi.html) Loads a previously recorded macro (.nivsmacro) file for playback. You can use the Macro Recorder VIs or the Macro Recorder tool in NI VeriStand to create macro files.
- [NI VeriStand - Get Macro Player Command Lines VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-command-lines-vi.html) Returns the commands the VeriStand Gateway sends to the RT target or desktop PC during recording. You must use the Open Command Line Notification (Macro Player) VI to open a reference to the command line of the Macro Player tool before you call this VI.
- [NI VeriStand - Get Macro Player State VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-get-macro-player-state-vi.html) Returns the current state of the Macro Player tool.
- [NI VeriStand - Wait For Macro Player Completion VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-wait-for-macro-player-completion-vi.html) Waits for the Macro Player tool to finish playing back the current macro file before continuing execution and returning a reference to the Macro Player.
- [NI VeriStand - Resume Macro Player VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-resume-macro-player-vi.html) Resumes the playback of a macro file that was paused using the Pause Macro Player VI. This VI plays back the file from the point at which the Pause Macro Player VI paused playback.
- [NI VeriStand - Pause Macro Player VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-pause-macro-player-vi.html) Pauses the playback of a macro file. Use the Resume Macro Player VI to restart playback from the point where this VI pauses it.
- [NI VeriStand - Open Percent Complete Notification VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-percent-complete-notification-vi.html) Opens a reference to messages the Macro Player sends that indicate the percentage of the macro file that has played back. This VI returns a user event that you can register and wire to an Event structure.
- [NI VeriStand - Close Percent Complete Notification VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-percent-complete-notification-vi.html) Closes an open reference to messages the Macro Player sends that indicate the percentage of the macro file that has played back. Use the Open Percent Complete Notification VI to open the reference this VI closes.
- [NI VeriStand - Open Error Message Notification VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-error-message-notification-vi.html) Opens a reference to error messages the Macro Player sends. This VI returns a user event that you can register and wire to an Event structure.
- [NI VeriStand - Close Error Message Notification VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-error-message-notification-vi.html) Closes an open reference to error messages the Macro Player sends. Use the Open Error Message Notification VI to open the reference this VI closes.
- [NI VeriStand - Open Command Line Notification (Macro Player) VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-open-command-line-notification-macro-player-vi.html) Opens a reference to the command line of the Macro Player tool. Opening this reference enables you to use the Get Macro Player Command Lines VI to read the commands the VeriStand Gateway sends to the RT target or desktop PC. This VI also returns a user event that you can register and wire to an Event structure.
- [NI VeriStand - Close Command Line Notification (Macro Player) VI](../../../../../vi-lib/ni-veristand/execution/macroplayer/ni-veristand-close-command-line-notification-macro-player-vi.html) Closes an open reference to the command line of the Macro Player tool. Use the Open Command Line Notification (Macro Player) VI to open the reference this VI closes.

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/macro-recorder-mnu.html language=enus -->
## TOPIC 00030: Macro Recorder

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/macro-recorder-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/macro-recorder-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Macro Recorder VIs to interact with the Macro Recorder tool on the VeriStand Gateway. You can use these VIs to record the commands NI VeriStand sends to an RT target or desktop PC, and to create a macro (.nivsmacro) file you can play back using the Macro Player VIs or the Macro Player tool i

### Macro Recorder

Use the Macro Recorder VIs to interact with the Macro Recorder tool on the VeriStand Gateway. You can use these VIs to record the commands NI VeriStand sends to an RT target or desktop PC, and to create a macro (.nivsmacro) file you can play back using the Macro Player VIs or the Macro Player tool in NI VeriStand.

[IMAGE alt='icon' src='macro-recorder-mnu.png']

- [NI VeriStand - Open Macro Recorder Reference VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-macro-recorder-reference-vi.html) Opens a reference to the Macro Recorder tool on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.
- [NI VeriStand - Save Macro VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-save-macro-vi.html) Saves the current macro recording. You must use the Stop Macro Recording VI to stop recording before you call this VI. This VI creates a file of the type .nivsmacro. You can use the Macro Player VIs to load the file this VI creates and to play back the saved recording.
- [NI VeriStand - Close Macro Recorder Reference VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-macro-recorder-reference-vi.html) Closes an open reference to the Macro Recorder tool on the VeriStand Gateway. Use this VI to close each MacroRecorder reference that you open with the Open Macro Recorder Reference VI.
- [NI VeriStand - Start Macro Recording VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-start-macro-recording-vi.html) Starts a new macro recording. If an unsaved macro file is in memory, this VI removes that file from memory and creates a new file when recording begins.
- [NI VeriStand - Resume Macro Recording VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-resume-macro-recording-vi.html) Resumes a stopped macro recording. Use this VI after the Stop Macro Recording VI to append information to the existing macro (.nivsmacro) file in memory.
- [NI VeriStand - Stop Macro Recording VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-stop-macro-recording-vi.html) Stops the current macro recording. This VI does not save the recording or remove the recording from memory. Use the Save Macro VI to save the recording.
- [NI VeriStand - Get Macro Recorder Command Lines VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-get-macro-recorder-command-lines-vi.html) Returns the commands the VeriStand Gateway sends to the RT target or desktop PC. You must use the Open Command Line Notification (Macro Recorder) VI to open a reference to the command line of the Macro Recorder tool before you call this VI.
- [NI VeriStand - Open Command Line Notification (Macro Recorder) VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-open-command-line-notification-macro-recorder-vi.html) Opens a reference to the command line of the Macro Recorder tool. Opening this reference enables you to use the Get Macro Recorder Command Lines VI to read the commands the VeriStand Gateway sends to the RT target or desktop PC. This VI also returns a user event that you can register and wire to an Event structure.
- [NI VeriStand - Close Command Line Notification (Macro Recorder) VI](../../../../../vi-lib/ni-veristand/execution/macrorecorder/ni-veristand-close-command-line-notification-macro-recorder-vi.html) Closes an open reference to the command line of the Macro Recorder tool. Use the Open Command Line Notification (Macro Recorder) VI to open the reference this VI closes.

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/model-manager-mnu.html language=unavailable -->
## TOPIC 00031: Model Manager Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/model-manager-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/model-manager-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/model-mnu.html language=enus -->
## TOPIC 00032: Model Execution

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/model-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/model-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Model Execution VIs to control and observe a specific model running on the target. icon

### Model Execution

Use the Model Execution VIs to control and observe a specific model running on the target.

[IMAGE alt='icon' src='model-mnu.png']

- [NI VeriStand - Open Model VI](../../../../../vi-lib/ni-veristand/execution/model/ni-veristand-open-model-vi.html) Opens a reference to a model. You must open a reference before using any other VIs on this palette.
- [NI VeriStand - Get Model Execution State VI](../../../../../vi-lib/ni-veristand/execution/model/ni-veristand-get-model-execution-state-vi.html) Returns the state and running time of the model you specify.
- [NI VeriStand - Set Model Execution State VI](../../../../../vi-lib/ni-veristand/execution/model/ni-veristand-set-model-execution-state-vi.html) Sets the current execution state of the model you specify.
- [NI VeriStand - Close Model VI](../../../../../vi-lib/ni-veristand/execution/model/ni-veristand-close-model-vi.html) Closes an open reference to a model. Use this VI to close each model reference that you open with the Open Model VI.
- [NI VeriStand - Save Model State VI](../../../../../vi-lib/ni-veristand/execution/model/ni-veristand-save-model-state-vi.html) Saves data about the current state of a model running on the target to a file you specify. You only can use this VI on your models and your compiled models you have built using The MathWorks, Inc. Simulink(R) software.
- [NI VeriStand - Restore Model State VI](../../../../../vi-lib/ni-veristand/execution/model/ni-veristand-restore-model-state-vi.html) Restores a model to the state defined by the file you specify. You only can use this VI on your models and your compiled models you have built using The MathWorks, Inc. Simulink(R) software.

Parent topic:

Models

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/project-control-mnu.html language=enus -->
## TOPIC 00033: Execution

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/project-control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/project-control-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Project Execution VIs to control the deployment and execution of an NI VeriStand project. icon

### Execution

Use the Project Execution VIs to control the deployment and execution of an NI VeriStand project.

[IMAGE alt='icon' src='project-control-mnu.png']

- [NI VeriStand - Run Project VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-run-project-vi.html) Runs an NI VeriStand project.
- [NI VeriStand - Deploy Project VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-deploy-project-vi.html) Deploys the system definition file associated with an NI VeriStand project to the target.
- [NI VeriStand - Connect Project VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-connect-project-vi.html) Connects an NI VeriStand project on the host computer to a target. This VI only establishes a connection to a target. It does not deploy the system definition file. Use the Deploy Project VI to deploy a system definition file to the target.
- [NI VeriStand - Undeploy Project VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-undeploy-project-vi.html) Undeploys the system definition file associated with an NI VeriStand project from the target. Undeploying the system definition file stops execution on the target.
- [NI VeriStand - Disconnect Project VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-disconnect-project-vi.html) Disconnects an NI VeriStand project from the target. This VI does not stop execution of the system definition file on the target. If you want to stop execution, use the Undeploy Project VI.

Parent topic:

Project

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/project-mnu.html language=enus -->
## TOPIC 00034: Project

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/project-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/project-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Project VIs to open, deploy, undeploy, and control an NI VeriStand project, and to interact with the NI VeriStand Workspace window and tools. icon

### Project

Use the Project VIs to open, deploy, undeploy, and control an NI VeriStand project, and to interact with the NI VeriStand **Workspace** window and tools.

[IMAGE alt='icon' src='project-mnu.png']

- [NI VeriStand - Open Project Reference VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-open-project-reference-vi.html) Opens a reference to an NI VeriStand project.
- [NI VeriStand - Close Project VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-close-project-vi.html) Closes an open NI VeriStand project.
- [NI VeriStand - Close Project Reference VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-close-project-reference-vi.html) Closes an open reference to an NI VeriStand project.
- [NI VeriStand - Quit Application VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-quit-application-vi.html) Sends a message to NI VeriStand to quit the project and application. When you call this VI, the project disconnects from any targets to which it is connected, closes all tools including the Workspace window, and shuts down. Then NI VeriStand quits completely
- [Execution](../../../../../menus/categories/ni-veristand/core/execution/project-control-mnu.html) Use the Project Execution VIs to control the deployment and execution of an NI VeriStand project.
- [Workspace Automation](../../../../../menus/categories/ni-veristand/core/execution/project-workspace-automation-mnu.html) Use the Workspace Automation VIs to access the NI VeriStand Workspace window and Workspace tools.

Parent topic:

Execution API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/project-workspace-automation-mnu.html language=enus -->
## TOPIC 00035: Workspace Automation

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/project-workspace-automation-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/project-workspace-automation-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Workspace Automation VIs to access the NI VeriStand Workspace window and Workspace tools. icon

### Workspace Automation

Use the Workspace Automation VIs to access the NI VeriStand **Workspace** window and Workspace tools.

[IMAGE alt='icon' src='project-workspace-automation-mnu.png']

- [NI VeriStand - Open Workspace Window VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-window-vi.html) Opens the Workspace window for an NI VeriStand project.
- [NI VeriStand - Close Workspace Window VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-close-workspace-window-vi.html) Closes the Workspace window for an NI VeriStand project.
- [NI VeriStand - Send Workspace Tool Message VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-send-workspace-tool-message-vi.html) Sends a message or command to a Workspace tool for an NI VeriStand project, as well as data required by the case that handles the command. You can use this method with any Workspace tool that registers to receive the command you specify.
- [NI VeriStand - Open Workspace Tool VI](../../../../../vi-lib/ni-veristand/execution/project/ni-veristand-open-workspace-tool-vi.html) Opens a Workspace tool for an NI VeriStand project.

Parent topic:

Project

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/stimulus-events-mnu.html language=unavailable -->
## TOPIC 00036: Stimulus Events Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/stimulus-events-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/stimulus-events-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/stimulus-mnu.html language=enus -->
## TOPIC 00037: Stimulus Profile

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/stimulus-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/stimulus-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use Stimulus Profile VIs to observe and control the stimulus profile manager and stimulus profile files. icon

### Stimulus Profile

Use Stimulus Profile VIs to observe and control the stimulus profile manager and stimulus profile files.

[IMAGE alt='icon' src='stimulus-mnu.png']

- [Open Stimulus Profile Session VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-stimulus-profile-session-vi.html) Connects to the VeriStand Gateway and creates a session with a name you specify.
- [Create Sequence Call VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-call-vi.html) Specifies a sequence to execute using a file path you specify.
- [Create Sequence Parameter Assignment VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/create-sequence-parameter-assignment-vi.html) Assigns a value to a real-time sequence parameter. The value can be a constant value, data in a file, or a mapping to a channel in a system definition file. Use this VI to create parameter assignment references to use with the Create Sequence Call VI. Wire data to the Channel input to determine the polymorphic instance to use or manually select the instance.
- [Deploy Stimulus Profile Session VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/deploy-stimulus-profile-session-vi.html) Deploys a stimulus profile session to an RT target.
- [Undeploy Stimulus Profile Session VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/undeploy-stimulus-profile-session-vi.html) Undeploys the stimulus profile session. Undeploying a session removes all data from that session and from any targets, and immediately terminates any running sequences.
- [Open Deployed Stimulus Profile Session VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/open-deployed-stimulus-profile-session-vi.html) Opens a reference to an existing stimulus profile session that has already been deployed.
- [Get All Deployed Stimulus Profile Sessions VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-deployed-stimulus-profile-sessions-vi.html) Queries the VeriStand Gateway and returns a list of all currently deployed stimulus profile sessions.
- [Session Control](../../../../../menus/categories/ni-veristand/core/execution/stimulus-session-control-mnu.html) Use the Session Control VIs to control the execution of an NI VeriStand stimulus profile.
- [Sequence Control](../../../../../menus/categories/ni-veristand/core/execution/stimulus-sequence-control-mnu.html) Use the Sequence Control VIs to control and observe real-time sequences in an NI VeriStand stimulus profile session.
- [Events](../../../../../menus/categories/ni-veristand/core/execution/stimulus-events-mnu.html) Use the Events VIs to register and unregister for events on NI VeriStand stimulus profile sessions and real-time sequences.
- [Utilities](../../../../../menus/categories/ni-veristand/core/execution/stimulus-utilities-mnu.html) Use the Utilities VIs to get information about a real-time sequence in an NI VeriStand stimulus profile session and to translate sequence return values into LabVIEW variant data types.

Parent topic:

Execution API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/stimulus-sequence-control-mnu.html language=enus -->
## TOPIC 00038: Sequence Control

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/stimulus-sequence-control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/stimulus-sequence-control-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Sequence Control VIs to control and observe real-time sequences in an NI VeriStand stimulus profile session. icon

### Sequence Control

Use the Sequence Control VIs to control and observe real-time sequences in an NI VeriStand stimulus profile session.

[IMAGE alt='icon' src='stimulus-sequence-control-mnu.png']

- [Run Sequence VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/run-sequence-vi.html) Runs or resumes a real-time sequence in an NI VeriStand stimulus profile session.
- [Pause Sequence VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/pause-sequence-vi.html) Pauses the execution of a real-time sequence in an NI VeriStand stimulus profile session.
- [Stop Sequence VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/stop-sequence-vi.html) Stops a real-time sequence in an NI VeriStand stimulus profile session, which causes the sequence to skip to the clean-up section. If you want to skip clean-up tasks, use the Abort Sequence VI.
- [Abort Sequence VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/abort-sequence-vi.html) Aborts a real-time sequence in an NI VeriStand stimulus profile session. This VI immediately terminates sequence execution, without performing any clean-up tasks. To perform clean-up tasks, use the Stop Sequence VI.
- [Get Sequence Call Info VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-call-info-vi.html) Returns a sequence call refnum for a real-time sequence in an NI VeriStand stimulus profile session.
- [Get Sequence Return Value VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-return-value-vi.html) Returns a reference to the return value of a sequence. The sequence must be complete or this VI returns an error.
- [Get Sequence State VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-state-vi.html) Returns the execution state of a real-time sequence (Idle, Running, SingleStepping, Paused, Complete).
- [Get Sequence Time VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-time-vi.html) Returns the sequence time in seconds. This time is a relative time from the start of the sequence and is based on the number of iterations the sequence has run and the delta t in seconds at which each iteration occurs.
- [Get All Sequence Names VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-all-sequence-names-vi.html) Returns a list of sequence names for all the real-time sequences in an NI VeriStand stimulus profile session.

Parent topic:

Stimulus Profile

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/stimulus-session-control-mnu.html language=unavailable -->
## TOPIC 00039: Stimulus Session Control Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/stimulus-session-control-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/stimulus-session-control-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/stimulus-utilities-mnu.html language=enus -->
## TOPIC 00040: Utilities

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/stimulus-utilities-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/stimulus-utilities-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Utilities VIs to get information about a real-time sequence in an NI VeriStand stimulus profile session and to translate sequence return values into LabVIEW variant data types. icon

### Utilities

Use the Utilities VIs to get information about a real-time sequence in an NI VeriStand stimulus profile session and to translate sequence return values into LabVIEW variant data types.

[IMAGE alt='icon' src='stimulus-utilities-mnu.png']

- [Get Sequence Info VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/get-sequence-info-vi.html) Returns information about a sequence in a stimulus profile session.
- [Data Value Ref to Variant VI](../../../../../vi-lib/ni-veristand/execution/sequenceexecutioninterface/data-value-ref-to-variant-vi.html) Translates the data value reference returned by the Get Sequence Return Value VI or a sequence complete event into a LabVIEW variant data type that corresponds to the data type of the sequence return value.

Parent topic:

Stimulus Profile

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/system-connection-mnu.html language=enus -->
## TOPIC 00041: System Connection

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/system-connection-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/system-connection-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the System Connection VIs to manage the connection between the VeriStand Gateway and targets in the system. icon

### System Connection

Use the System Connection VIs to manage the connection between the VeriStand Gateway and targets in the system.

[IMAGE alt='icon' src='system-connection-mnu.png']

- [NI VeriStand - Connect to System VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-connect-to-system-vi.html) Connects the VeriStand Gateway to the target(s) you define in the system definition file you specify.
- [NI VeriStand - Disconnect from System VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-disconnect-from-system-vi.html) Disconnects the VeriStand Gateway from one or more targets running the system definition file you specify.
- [NI VeriStand - Reconnect to System VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-reconnect-to-system-vi.html) Reconnects the VeriStand Gateway to a particular target.
- [NI VeriStand - Unlock Connection VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-unlock-connection-vi.html) Unlocks the current VeriStand Gateway connection.
- [NI VeriStand - Lock Connection VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-lock-connection-vi.html) Locks the current VeriStand Gateway connection. If the connection already is locked, you must provide the current password in order to set a new one.

Parent topic:

Workspace

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/udp-channel-streaming-mnu.html language=unavailable -->
## TOPIC 00042: Udp Channel Streaming Mnu

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/udp-channel-streaming-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/udp-channel-streaming-mnu.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/waveform-mnu.html language=enus -->
## TOPIC 00043: Waveform Streaming

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/waveform-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/waveform-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to stream waveform data being acquired or generated in an NI VeriStand system to a LabVIEW application. icon

### Waveform Streaming

Use the VIs on this palette to stream waveform data being acquired or generated in an NI VeriStand system to a LabVIEW application.

[IMAGE alt='icon' src='waveform-mnu.png']

- [Open Waveform Streaming Manager Reference VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/open-waveform-streaming-manager-reference-vi.html) Opens a reference to the waveform-stream manager on the VeriStand Gateway. You must open a reference before you register to receive waveform data and start streaming waveforms from the VeriStand Gateway.
- [Start Streaming Waveforms VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/start-streaming-waveforms-vi.html) Starts streaming waveform data to the VeriStand Gateway. Use this VI to allow an Event structure to start reading waveform values on the block diagram.
- [Stop Streaming Waveforms VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/stop-streaming-waveforms-vi.html) Stops streaming the specified waveforms to the VeriStand Gateway.
- [Close Waveform Streaming Manager Reference VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-streaming-manager-reference-vi.html) Closes an open reference to the waveform-stream manager on the VeriStand Gateway. Use this VI to close waveform-stream manager references you open with the Open Waveform Stream Manager Reference VI.
- [New Waveform Stream Specification VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/new-waveform-stream-specification-vi.html) Identifies a waveform whose data you want to stream to a host computer.
- [Set Condition for Waveform Stream VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-condition-for-waveform-stream-vi.html) Defines the condition under which NI VeriStand streams waveform data to a host computer.
- [Set Rate for Waveform Stream VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-rate-for-waveform-stream-vi.html) Sets whether to stream waveform values at the same rate the device acquires data or at a custom rate you specify. You must manually select the polymorphic instance to use.
- [Close Waveform Stream Specification VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/close-waveform-stream-specification-vi.html) Closes a waveform stream specification you opened with the New Waveform Stream Specification VI.
- [Register for Waveform Data Events VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/register-for-waveform-data-events-vi.html) Registers to receive waveform data from the specified WaveformStreamSpecifications . You can use this VI prior to starting waveform streams to generate an event registration refnum that allows an Event structure to stream data from waveforms. You must manually select the instance to use.
- [Unregister for Waveform Data Events VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/unregister-for-waveform-data-events-vi.html) Unregisters all waveform data events associated with the event registration refnum. Event structures that use this event registration refnum no longer receive any events. Wire data to the registered waveform data event (DBL) input to determine the polymorphic instance to use or manually select the instance.
- [Utilities](../../../../../menus/categories/ni-veristand/core/execution/waveform-utility-mnu.html) Use the VIs on this palette to perform various functions with waveforms, such as comparing stream specifications, changing the waveform streams that are registered for events, and returning delta T values for waveforms.

Parent topic:

Execution API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/waveform-utility-mnu.html language=enus -->
## TOPIC 00044: Utilities

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/waveform-utility-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/waveform-utility-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to perform various functions with waveforms, such as comparing stream specifications, changing the waveform streams that are registered for events, and returning delta T values for waveforms. icon

### Utilities

Use the VIs on this palette to perform various functions with waveforms, such as comparing stream specifications, changing the waveform streams that are registered for events, and returning delta T values for waveforms.

[IMAGE alt='icon' src='waveform-utility-mnu.png']

- [Set Waveform Streams for Data Event VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/set-waveform-streams-for-data-event-vi.html) Updates the event registration to apply to the waveform stream specifications you specify. This VI is useful for changing the waveforms for which you want to receive data events without stopping the current event-handling routine and re-registering for waveform-data events.
- [Get Waveform Streams for Data Event VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-streams-for-data-event-vi.html) Returns references to all waveform stream specifications for which you previously registered for events. Wire data to the registered waveform data event (DBL) in input to determine the polymorphic instance to use or manually select the instance.
- [Get Waveform dt Values VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/get-waveform-dt-values-vi.html) Returns an array of the delta T values for the specified waveform(s).
- [Compare Waveform Stream Specifications VI](../../../../../vi-lib/ni-veristand/execution/waveformstreaming/compare-waveform-stream-specifications-vi.html) Compares two waveform stream specifications to see if they define the same streaming operation. This VI compares the waveform paths, streaming rates, and conditions under which to stream data for the waveforms.

Parent topic:

Waveform Streaming

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/core/execution/workspace-mnu.html language=enus -->
## TOPIC 00045: Workspace

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/core/execution/workspace-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/core/execution/workspace-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the Workspace VIs to perform basic workspace operations such as getting and setting channel data. icon

### Workspace

Use the Workspace VIs to perform basic workspace operations such as getting and setting channel data.

[IMAGE alt='icon' src='workspace-mnu.png']

- [NI VeriStand - Open Workspace Manager Reference VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-open-workspace-manager-reference-vi.html) Opens a reference to the workspace manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.
- [NI VeriStand - Get Channel Value VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-channel-value-vi.html) Returns values of channels on the target. You can get values for a single channel, multiple channels, or vector values for a single channel. You must manually select the polymorphic instance to use.
- [NI VeriStand - Set Channel Value VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-set-channel-value-vi.html) Sets values of channels on the target. You must manually select the polymorphic instance to use.
- [NI VeriStand - Close Workspace Manager Reference VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-close-workspace-manager-reference-vi.html) Closes an open reference to the workspace manager on the VeriStand Gateway. Use this VI to close each workspace manager reference that you open with the Open Workspace Manager Reference VI.
- [NI VeriStand - Get Alias List VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-alias-list-vi.html) Returns lists of all the defined aliases and their corresponding channels.
- [NI VeriStand - Get System Node Channel List VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-channel-list-vi.html) Returns information about all the channels under the specified system node.
- [NI VeriStand - Get Multiple System Nodes Data VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-multiple-system-nodes-data-vi.html) Returns information about the system nodes you specify.
- [NI VeriStand - Get System Node Children VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-node-children-vi.html) Returns information about the nodes directly under the specified system node.
- [NI VeriStand - Get System State VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-get-system-state-vi.html) Gets the current state of the system to which the VeriStand Gateway is connected.
- [NI VeriStand - Open Engine State Change Notification VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-open-engine-state-change-notification-vi.html) Creates a reference to a user event that you can use to monitor the state of the VeriStand Engine.
- [NI VeriStand - Close Engine State Change Notification VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-close-engine-state-change-notification-vi.html) Destroys the user event created by the Open Engine State Change Notification VI.
- [NI VeriStand - Start Data Logging VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-start-data-logging-vi.html) Starts logging data for the specified Data Log Configuration Name .
- [NI VeriStand - Stop Data Logging VI](../../../../../vi-lib/ni-veristand/execution/workspace/ni-veristand-stop-data-logging-vi.html) Stops logging data for the specified Data Log Configuration Name .
- [Macro Recorder](../../../../../menus/categories/ni-veristand/core/execution/macro-recorder-mnu.html) Use the Macro Recorder VIs to interact with the Macro Recorder tool on the VeriStand Gateway. You can use these VIs to record the commands NI VeriStand sends to an RT target or desktop PC, and to create a macro (.nivsmacro) file you can play back using the Macro Player VIs or the Macro Player tool in NI VeriStand.
- [Macro Player](../../../../../menus/categories/ni-veristand/core/execution/macro-player-mnu.html) Use the Macro Player VIs to interact with the Macro Player tool on the VeriStand Gateway. You can use these VIs to load a macro (.nivsmacro) file you created using the Macro Recorder VIs or the Macro Recorder tool in NI VeriStand and to play back the commands NI VeriStand sent to an RT target or desktop PC during the time the Macro Recorder ran.
- [System Connection](../../../../../menus/categories/ni-veristand/core/execution/system-connection-mnu.html) Use the System Connection VIs to manage the connection between the VeriStand Gateway and targets in the system.
- [UDP Channel Streaming](../../../../../menus/categories/ni-veristand/core/execution/udp-channel-streaming-mnu.html) Use the UDP Channel Streaming VIs to manage sessions in which you stream data from channels via UDP connection.

Parent topic:

Execution API

<!--NI_TOPIC bundle=veristand-labview-api-ref path=menus/categories/ni-veristand/dir-mnu.html language=enus -->
## TOPIC 00046: NI VeriStand

- bundle_id: `veristand-labview-api-ref`
- source_path: `menus/categories/ni-veristand/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/menus/categories/ni-veristand/dir-mnu.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the NI VeriStand VIs to create and control tasks on the target and to interact with custom devices. icon

### NI VeriStand

Use the NI VeriStand VIs to create and control tasks on the target and to interact with custom devices.

[IMAGE alt='icon' src='dir-mnu.png']

- [Execution API](../../../menus/categories/ni-veristand/core/execution/api-mnu.html) Use the Execution VIs to automate the operation of an NI VeriStand application. For example, you can control models running on the target, configure alarm states and read data from alarms, and access Workspace tools.
- [Custom Device API](../../../menus/categories/ni-veristand/core/custom-device-api/custom-device-api-mnu.html) Use the Custom Device API VIs to interact with a custom device.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-boolean-vi.html language=enus -->
## TOPIC 00047: Get Item Property (Boolean) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-boolean-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (Boolean) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-boolean-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-file-vi.html language=enus -->
## TOPIC 00048: Get Item Property (Dependent File) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-file-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (Dependent File) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-dependent-file-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. OptionalInfo — OptionalInfo returns information about the dependent file, such as version information and the target operating system(s) to which it is configured to deploy. Version — Version returns version information for the dependency. RTDestination — RTDestination returns the destination directory, including the filename, for the dependency on the target. ForceDownload — ForceDownload is TRUE if the dependency is set to force-download. SupportedTarget — SupportedTarget indicates the target operating system(s) to which the custom device is set to deploy. MD5 — MD5 returns the MD5 message-digest for the file specified in Path. Item Ref out — Item Ref out returns a reference to the item in the custom device. Path — Path returns the path to the dependency, including the filename. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the Property Name. |
| --- |
| Version — Version returns version information for the dependency. RTDestination — RTDestination returns the destination directory, including the filename, for the dependency on the target. ForceDownload — ForceDownload is TRUE if the dependency is set to force-download. SupportedTarget — SupportedTarget indicates the target operating system(s) to which the custom device is set to deploy. MD5 — MD5 returns the MD5 message-digest for the file specified in Path. |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-node-pointer-vi.html language=enus -->
## TOPIC 00049: Get Item Property (Dependent Node Pointer) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-node-pointer-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-node-pointer-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (Dependent Node Pointer) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-dependent-node-pointer-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Dependent Node Ref — Dependent Node Ref returns a reference to the dependent node. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-double-array-vi.html language=unavailable -->
## TOPIC 00050: Get Item Property Double Array Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-double-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-double-array-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-double-vi.html language=unavailable -->
## TOPIC 00051: Get Item Property Double Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-double-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-i32-array-vi.html language=enus -->
## TOPIC 00052: Get Item Property (I32 Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-i32-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-i32-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (I32 Array) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-i32-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-i32-vi.html language=unavailable -->
## TOPIC 00053: Get Item Property I32 Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-i32-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-path-vi.html language=enus -->
## TOPIC 00054: Get Item Property (Path) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-path-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (Path) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-path-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-string-array-vi.html language=enus -->
## TOPIC 00055: Get Item Property (String Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-string-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-string-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (String Array) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-string-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-string-vi.html language=enus -->
## TOPIC 00056: Get Item Property (String) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-string-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (String) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-string-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-u16-vi.html language=unavailable -->
## TOPIC 00057: Get Item Property U16 Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-u16-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-u32-array-vi.html language=enus -->
## TOPIC 00058: Get Item Property (U32 Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-u32-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-u32-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (U32 Array) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-u32-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-u32-vi.html language=enus -->
## TOPIC 00059: Get Item Property (U32) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-u32-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (U32) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-u32-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-u64-vi.html language=unavailable -->
## TOPIC 00060: Get Item Property U64 Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-u64-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/get-item-property-variant-vi.html language=enus -->
## TOPIC 00061: Get Item Property (Variant) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/get-item-property-variant-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/get-item-property-variant-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### Get Item Property (Variant) VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='get-item-property-variant-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Default Value — Default Value specifies the default value of the property. If Property Name does not exist, Value returns this value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Value — Value returns the value of the property. error out — error out contains error information. This output provides standard error out functionality. Found? — Found? is TRUE if the VI found the Property Name. |
| --- |

Parent topic:

NI VeriStand - Get Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-channel-vi.html language=enus -->
## TOPIC 00062: NI VeriStand - Add Custom Device Channel VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-channel-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a channel to the device or device subsection specified by Parent Ref in. If the Channel Name you specify already exists, this VI updates the Channel information (Type, Units, etc.), properties, and the GUID for the configuration page. For existing channels, this VI does not delete properties. H

### NI VeriStand - Add Custom Device Channel VI

Adds a channel to the device or device subsection specified by **Parent Ref in**. If the **Channel Name** you specify already exists, this VI updates the **Channel** information (**Type**, **Units**, etc.), properties, and the **GUID** for the configuration page.

Note

Property names

[IMAGE alt='icon' src='ni-veristand-add-custom-device-channel-vi.png']

#### Inputs/Outputs

| Highlight? (F) — Highlight? specifies whether to make the current item the active item in the System Explorer window configuration tree. The default is FALSE. If you plan to add or move multiple items at once, National Instruments recommends you only highlight the first item. Highlighting every item as it is added or moved can negatively impact performance. GUID (Default Channel) — GUID is the GUID of the page to associate with the new channel, as defined in the custom device XML file. If you do not specify a GUID, this VI uses the default page for the channel type. Parent Ref in — Parent Ref in is the reference to the parent device or device subsection. Channel Name — Channel Name specifies the name of the new channel. If the name you specify already exists, this VI overwrites the existing channel settings and the values of any properties with names that match names you specify in the Property names array. Channel — Channel specifies the type, units, default value, faultability, and scalability of the channel. Type — Type specifies the type of the channel with respect to the custom device. 0 Input—Specifies that the channel receives input data. Select this option if the custom device receives input data from the VeriStand Engine. 1 Output—Specifies that the channel returns output values. Select this option if the custom device passes data to the VeriStand Engine. Units — Units specifies the units to associate with the channel. Default Value — Default Value specifies the default value of the channel. The channel retains this value until it receives a new value. Faultable — Faultable is TRUE if the channel can be faulted. Scalable — Scalable is TRUE if the channel can be scaled. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property names — Property names specifies names of properties to associate with the item. Property names are case-sensitive. Property Values — Property Values is an array of values that correspond one-to-one with the properties in the Property names array. Property values can be any standard LabVIEW data type. Parent Ref out — Parent Ref out returns the reference to the parent device or device subsection. Newly Created? — Newly Created? returns FALSE if the Channel Name you specify already exists for the custom device. Returns TRUE if the Channel Name you specify does not exist and the VI creates a new channel for the device. Channel Ref — Channel Ref returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Type — Type specifies the type of the channel with respect to the custom device. 0 Input—Specifies that the channel receives input data. Select this option if the custom device receives input data from the VeriStand Engine. 1 Output—Specifies that the channel returns output values. Select this option if the custom device passes data to the VeriStand Engine. Units — Units specifies the units to associate with the channel. Default Value — Default Value specifies the default value of the channel. The channel retains this value until it receives a new value. Faultable — Faultable is TRUE if the channel can be faulted. Scalable — Scalable is TRUE if the channel can be scaled. |  |
| 0 | Input—Specifies that the channel receives input data. Select this option if the custom device receives input data from the VeriStand Engine. |
| 1 | Output—Specifies that the channel returns output values. Select this option if the custom device passes data to the VeriStand Engine. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-dependencies-vi.html language=unavailable -->
## TOPIC 00063: Ni Veristand Add Custom Device Dependencies Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-dependencies-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-dependencies-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-section-vi.html language=enus -->
## TOPIC 00064: NI VeriStand - Add Custom Device Section VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-section-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-section-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a section with the name Section Name to the device specified by Parent Ref in. If the Section Name you specify already exists for that device, this VI updates the page GUID and the values of any properties. For existing sections, this VI does not delete properties. However, it does overwrite th

### NI VeriStand - Add Custom Device Section VI

Adds a section with the name **Section Name** to the device specified by **Parent Ref in**. If the **Section Name** you specify already exists for that device, this VI updates the page **GUID** and the values of any properties.

Note

Property names

[IMAGE alt='icon' src='ni-veristand-add-custom-device-section-vi.png']

#### Inputs/Outputs

| Highlight? (F) — Highlight? specifies whether to make the current item the active item in the System Explorer window configuration tree. The default is FALSE. If you plan to add or move multiple items at once, National Instruments recommends you only highlight the first item. Highlighting every item as it is added or moved can negatively impact performance. GUID (Default Section) — GUID is the GUID of the page to associate with the new section, as defined in the custom device XML file. If you do not specify a GUID, this VI uses the default section specification page. Parent Ref in — Parent Ref in is the reference to the parent device or device subsection. Section Name — Section Name is the name of the section to add to the custom device. If the Section Name you specify already exists, this VI updates only the GUID for the section. It does not affect any properties or child items. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property names — Property names specifies names of properties to associate with the item. Property names are case-sensitive. Property Values — Property Values is an array of values that correspond one-to-one with the properties in the Property names array. Property values can be any standard LabVIEW data type. Parent Ref out — Parent Ref out returns the reference to the parent device or device subsection. Newly Created? — Newly Created? returns FALSE if the Section Name you specify already exists for the custom device. Returns TRUE if the Section Name you specify does not exist and the VI creates a new section for the device. Section Ptr — Section Ptr returns the reference to the section. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-waveform-vi.html language=enus -->
## TOPIC 00065: NI VeriStand - Add Custom Device Waveform VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-waveform-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-add-custom-device-waveform-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds a waveform item to the device or device subsection specified by Parent Ref in. If the Waveform Name you specify already exists, this VI updates the Waveform information (Data Type, Units, etc.), properties, and the GUID for the configuration page. For existing waveforms, this VI does not delete

### NI VeriStand - Add Custom Device Waveform VI

Adds a waveform item to the device or device subsection specified by **Parent Ref in**. If the **Waveform Name** you specify already exists, this VI updates the **Waveform** information (**Data Type**, **Units**, etc.), properties, and the **GUID** for the configuration page.

Note

Property names

[IMAGE alt='icon' src='ni-veristand-add-custom-device-waveform-vi.png']

#### Inputs/Outputs

| Highlight? (F) — Highlight? specifies whether to make the current item the active item in the System Explorer window configuration tree. The default is FALSE. If you plan to add or move multiple items at once, National Instruments recommends you only highlight the first item. Highlighting every item as it is added or moved can negatively impact performance. GUID (Default Waveform) — GUID is the GUID of the page to associate with the new waveform, as defined in the custom device XML file. If you do not specify a GUID, this VI uses the default page for the waveform type. Parent Ref in — Parent Ref in is the reference to the parent device or device subsection. Waveform Name — Waveform Name specifies the name of the new waveform. If the name you specify already exists, this VI overwrites the existing waveform settings and the values of any properties with names that match names you specify in the Property names array. Waveform — Waveform specifies the data type and units of the waveform. Data Type — Data Type specifies the type of the waveform with respect to the custom device. 0 Double—Specifies to represent waveform data as double-precision, floating-point values. 1 Complex Double—Specifies to represent waveform data as complex double-precision, floating-point values. Units — Units specifies the units to associate with the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property names — Property names specifies names of properties to associate with the item. Property names are case-sensitive. Property Values — Property Values is an array of values that correspond one-to-one with the properties in the Property names array. Property values can be any standard LabVIEW data type. Parent Ref out — Parent Ref out returns the reference to the parent device or device subsection. Newly Created? — Newly Created? returns TRUE if a new waveform. This output is FALSE is the VI updates an existing waveform. Waveform Ref — Waveform Ref returns a reference to the waveform. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Data Type — Data Type specifies the type of the waveform with respect to the custom device. 0 Double—Specifies to represent waveform data as double-precision, floating-point values. 1 Complex Double—Specifies to represent waveform data as complex double-precision, floating-point values. Units — Units specifies the units to associate with the waveform. |  |
| 0 | Double—Specifies to represent waveform data as double-precision, floating-point values. |
| 1 | Complex Double—Specifies to represent waveform data as complex double-precision, floating-point values. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-add-input-overflow-count-channel-vi.html language=unavailable -->
## TOPIC 00066: Ni Veristand Add Input Overflow Count Channel Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-add-input-overflow-count-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-add-input-overflow-count-channel-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-add-output-underflow-count-channel-vi.html language=enus -->
## TOPIC 00067: NI VeriStand - Add Output Underflow Count Channel VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-add-output-underflow-count-channel-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-add-output-underflow-count-channel-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Adds an output underflow count channel to the device or device subsection specified by Parent Ref in. Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output

### NI VeriStand - Add Output Underflow Count Channel VI

Adds an output underflow count channel to the device or device subsection specified by **Parent Ref in**. Output underflow count channels track the number of times the system fails to read data from an asynchronous custom device because there is no data to read. A custom device can have only one output underflow count channel.

[IMAGE alt='icon' src='ni-veristand-add-output-underflow-count-channel-vi.png']

#### Inputs/Outputs

| Highlight? (F) — Highlight? specifies whether to make the current item the active item in the System Explorer window configuration tree. The default is FALSE. If you plan to add or move multiple items at once, National Instruments recommends you only highlight the first item. Highlighting every item as it is added or moved can negatively impact performance. Parent Ref in — Parent Ref in is the reference to the parent device or device subsection. Channel Name — Channel Name specifies the name of the new channel. If the name you specify already exists, this VI takes no action and returns a reference to the existing channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Parent Ref out — Parent Ref out returns the reference to the parent device or device subsection. Channel Ref — Channel Ref returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Asynchronous Device Channels

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-commit-system-explorer-update-buffer-vi.html language=enus -->
## TOPIC 00068: NI VeriStand - Commit System Explorer Update Buffer VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-commit-system-explorer-update-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-commit-system-explorer-update-buffer-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Commits updates to the System Explorer window. Using this VI together with the Enable System Explorer Update Buffer VI can speed up item creation if you are creating or updating multiple custom device items at one time. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in describes erro

### NI VeriStand - Commit System Explorer Update Buffer VI

Commits updates to the **System Explorer** window. Using this VI together with the Enable System Explorer Update Buffer VI can speed up item creation if you are creating or updating multiple custom device items at one time.

[IMAGE alt='icon' src='ni-veristand-commit-system-explorer-update-buffer-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Explorer Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-convert-timed-loop-priority-to-number-vi.html language=unavailable -->
## TOPIC 00069: Ni Veristand Convert Timed Loop Priority To Number Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-convert-timed-loop-priority-to-number-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-convert-timed-loop-priority-to-number-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-disable-dynamic-button-vi.html language=unavailable -->
## TOPIC 00070: Ni Veristand Disable Dynamic Button Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-disable-dynamic-button-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-disable-dynamic-button-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-dynamic-button-vi.html language=enus -->
## TOPIC 00071: NI VeriStand - Enable Dynamic Button VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-dynamic-button-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-dynamic-button-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables a custom toolbar button for an item's System Explorer window configuration page. You can use this VI to only display the button when certain conditions are met. You configure the buttons associated with an item in the Custom Device XML file. icon Inputs/Outputs cstr.png Button ID Button ID i

### NI VeriStand - Enable Dynamic Button VI

Enables a custom toolbar button for an item's **System Explorer** window configuration page. You can use this VI to only display the button when certain conditions are met.

Note

[IMAGE alt='icon' src='ni-veristand-enable-dynamic-button-vi.png']

#### Inputs/Outputs

| Button ID — Button ID is the unique ID that identifies the button in the Custom Device XML file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Explorer Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-system-explorer-update-buffer-vi.html language=enus -->
## TOPIC 00072: NI VeriStand - Enable System Explorer Update Buffer VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-system-explorer-update-buffer-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-enable-system-explorer-update-buffer-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the buffer for updates to the System Explorer window. Using this VI together with the Commit System Explorer Update Buffer VI can speed up item creation if you are creating or updating multiple custom device items at one time. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in

### NI VeriStand - Enable System Explorer Update Buffer VI

Enables the buffer for updates to the **System Explorer** window. Using this VI together with the Commit System Explorer Update Buffer VI can speed up item creation if you are creating or updating multiple custom device items at one time.

[IMAGE alt='icon' src='ni-veristand-enable-system-explorer-update-buffer-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Explorer Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-find-next-valid-label-vi.html language=enus -->
## TOPIC 00073: NI VeriStand - Find next valid Label VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-find-next-valid-label-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-find-next-valid-label-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches the custom device hierarchy for the Label you specify and determines whether another item is already using the label. If the label already is in use, this VI adds a value to the end of the label and increments that value until it finds a label that is not in use. Use this VI to avoid accide

### NI VeriStand - Find next valid Label VI

Searches the custom device hierarchy for the **Label** you specify and determines whether another item is already using the label. If the label already is in use, this VI adds a value to the end of the label and increments that value until it finds a label that is not in use. Use this VI to avoid accidentally overwriting custom device items by specifying duplicate label names.

[IMAGE alt='icon' src='ni-veristand-find-next-valid-label-vi.png']

#### Inputs/Outputs

| Try requested Label only? — Try requested Label only? specifies whether the VI suggests a new label if Label is already in use. If TRUE, this VI only checks Label for validity, and does not suggest a new label. Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Label — Label is the label you want to check. Start Value (1) — Start Value specifies the value from which to start searching for valid labels. For example, if you know the custom device contains nine channels labeled Input, you can specify a value of 10 to save time testing the first nine matches. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Label out — Label out returns the Label, if it is valid, or an alternative if Label is already in use. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. Requested label not in use? — Requested label not in use? is TRUE if Label is valid and not already in use. |
| --- |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-asynchronous-driver-vi-timed-loop-name-vi.html language=enus -->
## TOPIC 00074: NI VeriStand - Get Asynchronous Driver VI Timed Loop Name VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-asynchronous-driver-vi-timed-loop-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-asynchronous-driver-vi-timed-loop-name-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the name of the Timed Loop that an asynchronous custom device uses. The VeriStand Engine synchronizes the start of this Timed Loop with the other system Timed Loops. Use the Timed Loop name this VI returns to ensure this synchronization occurs successfully. icon Inputs/Outputs cu64.png Devic

### NI VeriStand - Get Asynchronous Driver VI Timed Loop Name VI

Returns the name of the Timed Loop that an asynchronous custom device uses. The VeriStand Engine synchronizes the start of this Timed Loop with the other system Timed Loops. Use the Timed Loop name this VI returns to ensure this synchronization occurs successfully.

[IMAGE alt='icon' src='ni-veristand-get-asynchronous-driver-vi-timed-loop-name-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Device Timed Loop Name — Device Timed Loop Name returns the name of the Timed Loop. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-block-data-references-vi.html language=unavailable -->
## TOPIC 00075: Ni Veristand Get Channel Block Data References Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-block-data-references-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-block-data-references-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-data-reference-vi.html language=enus -->
## TOPIC 00076: NI VeriStand - Get Channel Data Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-data-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-data-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a 32-bit Channel Data Reference to the inline custom device channel specified by Channel Ref in. You can use the reference this VI returns with the Get Channel Value by Data Reference and Set Channel Value by Data Reference VIs. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the

### NI VeriStand - Get Channel Data Reference VI

Returns a 32-bit **Channel Data Reference** to the inline custom device channel specified by **Channel Ref in**. You can use the reference this VI returns with the Get Channel Value by Data Reference and Set Channel Value by Data Reference VIs.

[IMAGE alt='icon' src='ni-veristand-get-channel-data-reference-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. Channel Ref in — Channel Ref in is the reference to the channel. Access — Access specifies whether to create channel data references with read or write access. 0 Read (default)—Creates channel data references with read access. Select this option if you plan to use the reference to get channel data. 1 Write—Creates channel data references with write access. Select this option if you plan to use the reference to set channel data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Channel Data Reference — Channel Data Reference returns the 32-bit data reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Read (default)—Creates channel data references with read access. Select this option if you plan to use the reference to get channel data. |
| 1 | Write—Creates channel data references with write access. Select this option if you plan to use the reference to set channel data. |

Parent topic:

Data References

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-value-by-data-reference-vi.html language=enus -->
## TOPIC 00077: NI VeriStand - Get Channel Value by Data Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-value-by-data-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-value-by-data-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value of the custom device channel specified by Data Reference in. Use the Get Channel Data Reference VI to get the channel data reference for this VI. You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to H

### NI VeriStand - Get Channel Value by Data Reference VI

Returns the value of the custom device channel specified by **Data Reference in**. Use the Get Channel Data Reference VI to get the channel data reference for this VI.

You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.

Note

[IMAGE alt='icon' src='ni-veristand-get-channel-value-by-data-reference-vi.png']

#### Inputs/Outputs

| Data Reference in — Data Reference in is the 32-bit data reference to a custom device channel. Use the Get Channel Data Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Value — Value returns the value of the specified channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Data References

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-values-by-block-data-reference-vi.html language=enus -->
## TOPIC 00078: NI VeriStand - Get Channel Values by Block Data Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-values-by-block-data-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-channel-values-by-block-data-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the values of the inline custom device channels specified by Block Data Ref. You can use this VI to get multiple channel values at one time. Use the Get Channel Block Data References VI to get the channel data references for this VI. You can use this VI in the Execute Model case of an Inline

### NI VeriStand - Get Channel Values by Block Data Reference VI

Returns the values of the inline custom device channels specified by **Block Data Ref**. You can use this VI to get multiple channel values at one time. Use the Get Channel Block Data References VI to get the channel data references for this VI.

You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.

[IMAGE alt='icon' src='ni-veristand-get-channel-values-by-block-data-reference-vi.png']

#### Inputs/Outputs

| Block Data Ref — Block Data Ref specifies the references to the channels. Use the Get Channel Block Data Values VI to get these references. Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. Values Array in — Values Array in contains the values of the channels. Use the NI VeriStand - Get Channel Block Data References VI to get this array. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Block Data Ref dup — Block Data Ref dup returns the 32-bit channel data references. Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. Values Array out — Values Array out returns the values of the channels. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. |
| Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. |

Parent topic:

Data References

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-data-vi.html language=unavailable -->
## TOPIC 00079: Ni Veristand Get Custom Device Channel Data Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-data-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-list-vi.html language=enus -->
## TOPIC 00080: NI VeriStand - Get Custom Device Channel List VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-channel-list-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array of references to all the input or output channels of a custom device. icon Inputs/Outputs cenum.png Channel Type Channel Type specifies the type of channels. 0 Input—Specifies that the channels receive input data. Select this option if the custom device receives input data from the

### NI VeriStand - Get Custom Device Channel List VI

Returns an array of references to all the input or output channels of a custom device.

[IMAGE alt='icon' src='ni-veristand-get-custom-device-channel-list-vi.png']

#### Inputs/Outputs

| Channel Type — Channel Type specifies the type of channels. 0 Input—Specifies that the channels receive input data. Select this option if the custom device receives input data from the VeriStand Engine. 1 Output—Specifies that the channels return output values. Select this option if the custom device passes data to the VeriStand Engine. Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Specified Channel Ref List — Specified Channel Ref List returns an array of references to all the Channel Type channels of the custom device. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Input—Specifies that the channels receive input data. Select this option if the custom device receives input data from the VeriStand Engine. |
| 1 | Output—Specifies that the channels return output values. Select this option if the custom device passes data to the VeriStand Engine. |

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-decimation-vi.html language=enus -->
## TOPIC 00081: NI VeriStand - Get Custom Device Decimation VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-decimation-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-decimation-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Decimation of a custom device, which determines how many iterations of the Primary Control Loop occur between calls to the custom device. A value of 1 indicates no decimation. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the reference to the custom device. cerrcodeclst.png

### NI VeriStand - Get Custom Device Decimation VI

Returns the **Decimation** of a custom device, which determines how many iterations of the Primary Control Loop occur between calls to the custom device. A value of 1 indicates no decimation.

[IMAGE alt='icon' src='ni-veristand-get-custom-device-decimation-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Decimation — Decimation returns the decimation factor. For example, a decimation of 4 indicates that the Primary Control Loop calls the custom device on every fourth iteration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-dependencies-vi.html language=enus -->
## TOPIC 00082: NI VeriStand - Get Custom Device Dependencies VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-dependencies-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-dependencies-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns all dependencies of a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you must deploy to the target along with the custom device. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the reference to the custom device. cerrcodec

### NI VeriStand - Get Custom Device Dependencies VI

Returns all dependencies of a custom device. Dependencies are any files, such as DLLs or VIs, that the custom device requires and that you must deploy to the target along with the custom device.

[IMAGE alt='icon' src='ni-veristand-get-custom-device-dependencies-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Dependencies — Dependencies returns an array containing information about the dependencies of the custom device. Source — source describes the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. Path — Path returns the path to the dependency, including the filename. Type — Type indicates whether Path is an absolute or relative path. For relative paths, Type indicates to which directory the path is relative. 0 Absolute—Indicates that the path is an absolute path. 1 To Base—Indicates that the path is relative to the base NI VeriStand path. 2 To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. 3 To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. RT Destination — RT Destination returns the destination directory, including the filename, for the dependency on the target. ForceDownload? — Force Download? is TRUE if the dependency is set to download every time you deploy to the target, regardless of whether the file has changed. SupportedTarget — SupportedTarget indicates the target operating system(s) to which the custom device is set to deploy. 0 All—Indicates the custom device is set to deploy to all supported operating systems. 1 PharLap—Indicates the custom device is set to deploy to a Phar Lap operating system. 2 VxWorks—Indicates the custom device is set to deploy to a VxWorks operating system. 3 Windows—Indicates the custom device is set to deploy to a Windows operating system. 4 Linux_32_ARM—Indicates the custom device is set to deploy to a Linux_32_ARM operating system. 5 Linux_x64—Indicates the custom device is set to deploy to a Linux_x64 operating system. 6 PharLap & Windows—Indicates the custom device is set to deploy to Phar Lap and Windows operating systems. 7 PharLap & VxWorks—Indicates the custom device is set to deploy to Phar Lap and VxWorks operating systems. 8 VxWorks & Windows—Indicates the custom device is set to deploy VxWorks and Windows operating systems. Version — Version returns version information for the dependency. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Source — source describes the origin of the error or warning and is, in most cases, the name of the node that produced the error or warning. Path — Path returns the path to the dependency, including the filename. Type — Type indicates whether Path is an absolute or relative path. For relative paths, Type indicates to which directory the path is relative. 0 Absolute—Indicates that the path is an absolute path. 1 To Base—Indicates that the path is relative to the base NI VeriStand path. 2 To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. 3 To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. RT Destination — RT Destination returns the destination directory, including the filename, for the dependency on the target. ForceDownload? — Force Download? is TRUE if the dependency is set to download every time you deploy to the target, regardless of whether the file has changed. SupportedTarget — SupportedTarget indicates the target operating system(s) to which the custom device is set to deploy. 0 All—Indicates the custom device is set to deploy to all supported operating systems. 1 PharLap—Indicates the custom device is set to deploy to a Phar Lap operating system. 2 VxWorks—Indicates the custom device is set to deploy to a VxWorks operating system. 3 Windows—Indicates the custom device is set to deploy to a Windows operating system. 4 Linux_32_ARM—Indicates the custom device is set to deploy to a Linux_32_ARM operating system. 5 Linux_x64—Indicates the custom device is set to deploy to a Linux_x64 operating system. 6 PharLap & Windows—Indicates the custom device is set to deploy to Phar Lap and Windows operating systems. 7 PharLap & VxWorks—Indicates the custom device is set to deploy to Phar Lap and VxWorks operating systems. 8 VxWorks & Windows—Indicates the custom device is set to deploy VxWorks and Windows operating systems. Version — Version returns version information for the dependency. |  |
| Path — Path returns the path to the dependency, including the filename. Type — Type indicates whether Path is an absolute or relative path. For relative paths, Type indicates to which directory the path is relative. 0 Absolute—Indicates that the path is an absolute path. 1 To Base—Indicates that the path is relative to the base NI VeriStand path. 2 To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. 3 To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. |  |
| 0 | Absolute—Indicates that the path is an absolute path. |
| 1 | To Base—Indicates that the path is relative to the base NI VeriStand path. |
| 2 | To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. |
| 3 | To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. |
| 0 | All—Indicates the custom device is set to deploy to all supported operating systems. |
| 1 | PharLap—Indicates the custom device is set to deploy to a Phar Lap operating system. |
| 2 | VxWorks—Indicates the custom device is set to deploy to a VxWorks operating system. |
| 3 | Windows—Indicates the custom device is set to deploy to a Windows operating system. |
| 4 | Linux_32_ARM—Indicates the custom device is set to deploy to a Linux_32_ARM operating system. |
| 5 | Linux_x64—Indicates the custom device is set to deploy to a Linux_x64 operating system. |
| 6 | PharLap & Windows—Indicates the custom device is set to deploy to Phar Lap and Windows operating systems. |
| 7 | PharLap & VxWorks—Indicates the custom device is set to deploy to Phar Lap and VxWorks operating systems. |
| 8 | VxWorks & Windows—Indicates the custom device is set to deploy VxWorks and Windows operating systems. |

Parent topic:

Dependencies

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-driver-vi.html language=enus -->
## TOPIC 00083: NI VeriStand - Get Custom Device Driver VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-driver-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-driver-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the execution mode and driver VI paths for a custom device. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the reference to the custom device. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input

### NI VeriStand - Get Custom Device Driver VI

Returns information about the execution mode and driver VI paths for a custom device.

[IMAGE alt='icon' src='ni-veristand-get-custom-device-driver-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Execution mode — Execution mode returns information about when the custom device runs with respect to other operations performed by the VeriStand Engine. 0 Asynchronous—Indicates that the custom device executes in a parallel loop to the Primary Control Loop. The device uses RT FIFOs to read and write data from and to the Primary Control Loop. 1 Inline HW Interface—Indicates that the custom device executes inline in the Primary Control Loop. This mode contains a Read Data from HW section of code that executes near the beginning of the Primary Control Loop iteration and a Write Data to HW section of code that executes near the end of the Primary Control Loop iteration. The Read Data from HW code outputs data to NI VeriStand, while the Write Data to HW code reads input data from NI VeriStand. 2 Inline Model Interface—Indicates that the custom device executes inline in the Primary Control Loop. This mode contains an Execute Model section of code that executes in the middle of the Primary Control Loop iteration. This code reads input data, performs a calculation, and then writes output data to NI VeriStand. Using the Inline Model Interface mode enables you to process data acquired from hardware inputs and send the processed values to hardware outputs with no latency. 3 Inline Timing and Sync—Indicates that the custom device executes inline in the Primary Control Loop as a timing and sync device. This mode of execution is identical to the Inline HW Interface mode, except that this option creates a timing and sync device, rather than a custom device. 4 Asynchronous Timing and Sync—Indicates that the custom device executes as a timing and sync device in a parallel loop to the Primary Control Loop. This mode of execution is identical to the Asynchronous mode, except that this option creates a timing and sync device, rather than a custom device. Device Ref out — Device Ref out returns a reference to the custom device. Driver VI Path (RT) — Driver VI Path (RT) returns the path to the top-level driver VI on the target. Driver VI Path (Host) — Driver VI Path (Host) returns the path to the driver VI on the host computer you are using to build the custom device. Path — Path returns the path to the driver VI, including the filename. Type — Type indicates whether Path is an absolute or relative path. For relative paths, Type indicates to which directory the path is relative. 0 Absolute—Indicates that the path is an absolute path. 1 To Base—Indicates that the path is relative to the base NI VeriStand path. 2 To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. 3 To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Asynchronous—Indicates that the custom device executes in a parallel loop to the Primary Control Loop. The device uses RT FIFOs to read and write data from and to the Primary Control Loop. |
| 1 | Inline HW Interface—Indicates that the custom device executes inline in the Primary Control Loop. This mode contains a Read Data from HW section of code that executes near the beginning of the Primary Control Loop iteration and a Write Data to HW section of code that executes near the end of the Primary Control Loop iteration. The Read Data from HW code outputs data to NI VeriStand, while the Write Data to HW code reads input data from NI VeriStand. |
| 2 | Inline Model Interface—Indicates that the custom device executes inline in the Primary Control Loop. This mode contains an Execute Model section of code that executes in the middle of the Primary Control Loop iteration. This code reads input data, performs a calculation, and then writes output data to NI VeriStand. Using the Inline Model Interface mode enables you to process data acquired from hardware inputs and send the processed values to hardware outputs with no latency. |
| 3 | Inline Timing and Sync—Indicates that the custom device executes inline in the Primary Control Loop as a timing and sync device. This mode of execution is identical to the Inline HW Interface mode, except that this option creates a timing and sync device, rather than a custom device. |
| 4 | Asynchronous Timing and Sync—Indicates that the custom device executes as a timing and sync device in a parallel loop to the Primary Control Loop. This mode of execution is identical to the Asynchronous mode, except that this option creates a timing and sync device, rather than a custom device. |
| Path — Path returns the path to the driver VI, including the filename. Type — Type indicates whether Path is an absolute or relative path. For relative paths, Type indicates to which directory the path is relative. 0 Absolute—Indicates that the path is an absolute path. 1 To Base—Indicates that the path is relative to the base NI VeriStand path. 2 To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. 3 To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. |  |
| 0 | Absolute—Indicates that the path is an absolute path. |
| 1 | To Base—Indicates that the path is relative to the base NI VeriStand path. |
| 2 | To Common Data Dir—Indicates that the path is relative to the path to the <Common Data> directory. |
| 3 | To Application Data Dir—Indicates that the path is relative to the NI VeriStand application data directory. |

Parent topic:

Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-version-vi.html language=enus -->
## TOPIC 00084: NI VeriStand - Get Custom Device Version VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-version-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-version-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns version information for a custom device. You can use the Value string this VI returns as an input to code that specifies different actions based on the version. For example, you can check the version string to determine whether to update device dependencies or, if you are bringing a custom d

### NI VeriStand - Get Custom Device Version VI

Returns version information for a custom device. You can use the **Value** string this VI returns as an input to code that specifies different actions based on the version. For example, you can check the version string to determine whether to update device dependencies or, if you are bringing a custom device forward into a new version of NI VeriStand, to determine whether to run mutation code.

Note

[IMAGE alt='icon' src='ni-veristand-get-custom-device-version-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Value — Value returns version information for the custom device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-data-vi.html language=enus -->
## TOPIC 00085: NI VeriStand - Get Custom Device Waveform Data VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-data-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the waveform item specified by Waveform Ref in. icon Inputs/Outputs cu64.png Waveform Ref in Waveform Ref in is the reference to the waveform. You must add a custom device waveform to use this parameter. cerrcodeclst.png error in (no error) error in describes error conditio

### NI VeriStand - Get Custom Device Waveform Data VI

Returns information about the waveform item specified by **Waveform Ref in**.

[IMAGE alt='icon' src='ni-veristand-get-custom-device-waveform-data-vi.png']

#### Inputs/Outputs

| Waveform Ref in — Waveform Ref in is the reference to the waveform. You must add a custom device waveform to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. GUID — GUID returns the GUID of the configuration page associated with the item, as defined in the custom device XML file. Waveform Ref out — Waveform Ref out returns a reference to the waveform. You can wire this output to other custom device Configuration VIs. Waveform Name — Waveform Name returns the name of the waveform. Waveform — Waveform returns the data type and units of the waveform. Data Type — Data Type returns the data type of the waveform. 0 Double—Indicates the waveform measures or generates data in double-precision floating-point format. 1 Complex Double—Indicates the waveform measures or generates data in complex double-precision floating-point format. Units — Units returns the units associated with the waveform. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the specified waveform. |  |
| --- | --- |
| Data Type — Data Type returns the data type of the waveform. 0 Double—Indicates the waveform measures or generates data in double-precision floating-point format. 1 Complex Double—Indicates the waveform measures or generates data in complex double-precision floating-point format. Units — Units returns the units associated with the waveform. |  |
| 0 | Double—Indicates the waveform measures or generates data in double-precision floating-point format. |
| 1 | Complex Double—Indicates the waveform measures or generates data in complex double-precision floating-point format. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-list-vi.html language=unavailable -->
## TOPIC 00086: Ni Veristand Get Custom Device Waveform List Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-custom-device-waveform-list-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-engine-rate-vi.html language=unavailable -->
## TOPIC 00087: Ni Veristand Get Engine Rate Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-engine-rate-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-engine-rate-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-event-refnum-vi.html language=unavailable -->
## TOPIC 00088: Ni Veristand Get Event Refnum Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-event-refnum-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-event-refnum-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-fifo-depth-vi.html language=enus -->
## TOPIC 00089: NI VeriStand - Get FIFO Depth VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-fifo-depth-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-fifo-depth-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the depths, or buffer sizes, of the FIFOs of an asynchronous custom device. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the reference to the custom device. cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input pr

### NI VeriStand - Get FIFO Depth VI

Returns the depths, or buffer sizes, of the FIFOs of an asynchronous custom device.

[IMAGE alt='icon' src='ni-veristand-get-fifo-depth-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Size FIFO Source — Size FIFO Source returns the depth of the FIFO at the source. This output reflects the size of the buffer for incoming data. Size FIFO Sink — Size FIFO Sink returns the depth of the FIFO at the sink. This output reflects the size of the buffer for outgoing data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Asynchronous Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-children-vi.html language=enus -->
## TOPIC 00090: NI VeriStand - Get Item Children VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-children-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-children-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of references to all child items of the item specified by Item Ref in. This list can include subsections and channels. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in t

### NI VeriStand - Get Item Children VI

Returns a list of references to all child items of the item specified by **Item Ref in**. This list can include subsections and channels.

[IMAGE alt='icon' src='ni-veristand-get-item-children-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Child Refs — Child Refs returns an array of references to all the child items of the item specified by Item Ref in. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-data-vi.html language=enus -->
## TOPIC 00091: NI VeriStand - Get Item Data VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-data-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns information about the custom device item specified by Item Ref in, including the name of the item, the GUID of the associated configuration page, and whether the item is a channel. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom dev

### NI VeriStand - Get Item Data VI

Returns information about the custom device item specified by **Item Ref in**, including the name of the item, the GUID of the associated configuration page, and whether the item is a channel.

[IMAGE alt='icon' src='ni-veristand-get-item-data-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Item Info — Item Info contains information about the item. Name — Name returns the name of the item. Is Channel — Is Channel is TRUE if the item is a channel. GUID — GUID returns the GUID of the configuration page associated with the item, as defined in the custom device XML file. Is Waveform — Is Waveform is TRUE if the item is a waveform. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |
| Name — Name returns the name of the item. Is Channel — Is Channel is TRUE if the item is a channel. GUID — GUID returns the GUID of the configuration page associated with the item, as defined in the custom device XML file. Is Waveform — Is Waveform is TRUE if the item is a waveform. |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-description-vi.html language=enus -->
## TOPIC 00092: NI VeriStand - Get Item Description VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-description-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-description-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Description of an item. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. cerrcodeclst.png err

### NI VeriStand - Get Item Description VI

Returns the **Description** of an item.

[IMAGE alt='icon' src='ni-veristand-get-item-description-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Description — Description is the description. You can display an item description on the configuration page for the item. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-guid-vi.html language=unavailable -->
## TOPIC 00093: Ni Veristand Get Item Guid Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-guid-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-guid-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-parent-vi.html language=enus -->
## TOPIC 00094: NI VeriStand - Get Item Parent VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-parent-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-parent-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to the parent item of the item specified by Item Ref in. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a s

### NI VeriStand - Get Item Parent VI

Returns a reference to the parent item of the item specified by **Item Ref in**.

[IMAGE alt='icon' src='ni-veristand-get-item-parent-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Parent Ref — Parent Ref returns the reference to the parent item. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-path-vi.html language=unavailable -->
## TOPIC 00095: Ni Veristand Get Item Path Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-path-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-property-vi.html language=enus -->
## TOPIC 00096: NI VeriStand - Get Item Property VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-property-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the Value of a specific item Property Name. Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the

### NI VeriStand - Get Item Property VI

Returns the **Value** of a specific item **Property Name**. Properties do not inherit within a custom device, so **Item Ref in** must reference the specific item on which the property is set. 

For instances with a **Default Value** input, the **Value** output returns this value if the **Property Name** is not found for the specified item. Wire data to the **Default Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='ni-veristand-get-item-property-vi.png']

- [Get Item Property (Boolean) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-boolean-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (Double Array) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-double-array-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (Double) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-double-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (I32) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-i32-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (Path) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-path-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (String) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-string-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (U16) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-u16-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (Variant) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-variant-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (Dependent File) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-file-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (Dependent Node Pointer) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-dependent-node-pointer-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (U32) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-u32-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (U32 Array) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-u32-array-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (I32 Array) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-i32-array-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (String Array) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-string-array-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.
- [Get Item Property (U64) VI](../../../vi-lib/ni-veristand/custom-device-api/get-item-property-u64-vi.html) Returns the Value of a specific item Property Name . Properties do not inherit within a custom device, so Item Ref in must reference the specific item on which the property is set. For instances with a Default Value input, the Value output returns this value if the Property Name is not found for the specified item. Wire data to the Default Value input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-name-vi.html language=enus -->
## TOPIC 00097: NI VeriStand - Get Item Reference by Name VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-name-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches for Item Name in the device or section specified by Parent Ref in and, if found, returns a reference to the item. icon Inputs/Outputs cu64.png Parent Ref in Parent Ref in is the reference to the parent device or device subsection. cstr.png Item Name Item Name specifies the name of the item.

### NI VeriStand - Get Item Reference by Name VI

Searches for **Item Name** in the device or section specified by **Parent Ref in** and, if found, returns a reference to the item.

[IMAGE alt='icon' src='ni-veristand-get-item-reference-by-name-vi.png']

#### Inputs/Outputs

| Parent Ref in — Parent Ref in is the reference to the parent device or device subsection. Item Name — Item Name specifies the name of the item. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Parent Ref out — Parent Ref out returns the reference to the parent device or device subsection. Item Ref — Item Ref returns the reference to the item. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-path-vi.html language=enus -->
## TOPIC 00098: NI VeriStand - Get Item Reference by Path VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-reference-by-path-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to the custom device item specified by Item Path in. icon Inputs/Outputs cstr.png Item Path in Item Path in is the path to the item in the System Explorer tree, expressed as a string. cu64.png Root Ref Root Ref is the reference to the root node of the system definition. If you lo

### NI VeriStand - Get Item Reference by Path VI

Returns a reference to the custom device item specified by **Item Path in**.

[IMAGE alt='icon' src='ni-veristand-get-item-reference-by-path-vi.png']

#### Inputs/Outputs

| Item Path in — Item Path in is the path to the item in the System Explorer tree, expressed as a string. Root Ref — Root Ref is the reference to the root node of the system definition. If you load multiple system definitions at a time, you can use Root Ref to specify in which system definition to look for the item path. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Path out — Item Path out returns the path to the item. Item Ref — Item Ref returns the reference to the item. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-root-vi.html language=enus -->
## TOPIC 00099: NI VeriStand - Get Item Root VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-root-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-item-root-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the root node in the system definition file. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. cer

### NI VeriStand - Get Item Root VI

Returns the root node in the system definition file.

[IMAGE alt='icon' src='ni-veristand-get-item-root-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Root Ref out — Root Ref out returns the reference to the root item in the system definition file. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-loop-flags-vi.html language=unavailable -->
## TOPIC 00100: Ni Veristand Get Loop Flags Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-loop-flags-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-loop-flags-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-loop-type-vi.html language=enus -->
## TOPIC 00101: NI VeriStand - Get Loop Type VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-loop-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-loop-type-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the type of loop (While Loop or Timed Loop) that an asynchronous custom device uses. If Loop type is 1 - Timed Loop, this VI also returns whether the loop uses the device clock as its timing source. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the reference to the custom devic

### NI VeriStand - Get Loop Type VI

Returns the type of loop (While Loop or Timed Loop) that an asynchronous custom device uses. If **Loop type** is 1 - Timed Loop, this VI also returns whether the loop uses the device clock as its timing source.

[IMAGE alt='icon' src='ni-veristand-get-loop-type-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Loop type — Loop type returns the loop type. 0 While Loop—Indicates that the custom device runs in a While Loop. 1 Timed Loop—Indicates that the custom device runs in a Timed Loop. Use Device Clock — Use Device Clock indicates whether the Timed Loop uses the Primary Control Loop's timing source to run pseudo-synchronously with that loop. If TRUE, the system passes the timing source from the Primary Control Loop to the custom device driver VI. The Primary Control Loop runs the custom device Timed Loop after NI VeriStand sets the outputs of the custom device. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | While Loop—Indicates that the custom device runs in a While Loop. |
| 1 | Timed Loop—Indicates that the custom device runs in a Timed Loop. |

Parent topic:

Asynchronous Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-property-names-list-vi.html language=unavailable -->
## TOPIC 00102: Ni Veristand Get Property Names List Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-property-names-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-property-names-list-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-slsc-module-name-vi.html language=enus -->
## TOPIC 00103: NI VeriStand - Get SLSC Module Name VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-slsc-module-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-slsc-module-name-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the SLSC module name that represents a custom device in System Explorer. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as

### NI VeriStand - Get SLSC Module Name VI

Returns the SLSC module name that represents a custom device in System Explorer.

[IMAGE alt='icon' src='ni-veristand-get-slsc-module-name-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. SLSC Module — SLSC Module is the SLSC module name that represents the custom device in System Explorer. Make sure that the module name is assigned to the slot in System Explorer that represents the physical position of the custom device in the SLSC chassis. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-target-type-vi.html language=enus -->
## TOPIC 00104: NI VeriStand - Get Target Type VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-target-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-target-type-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the type, or operating system, of the target on which a custom device is running. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, s

### NI VeriStand - Get Target Type VI

Gets the type, or operating system, of the target on which a custom device is running.

[IMAGE alt='icon' src='ni-veristand-get-target-type-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Target Type — Target Type returns the operating system on which the custom device is running. 0 PharLap—Indicates a Phar Lap operating system. 1 VxWorks—Indicates a VxWorks operating system. 2 Windows—Indicates a Windows operating system. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | PharLap—Indicates a Phar Lap operating system. |
| 1 | VxWorks—Indicates a VxWorks operating system. |
| 2 | Windows—Indicates a Windows operating system. |

Parent topic:

Navigation

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-timed-loop-priority-vi.html language=unavailable -->
## TOPIC 00105: Ni Veristand Get Timed Loop Priority Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-timed-loop-priority-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-timed-loop-priority-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.html language=enus -->
## TOPIC 00106: NI VeriStand - Get Timing and Sync Custom Device Is RTSI 0 Capable Flag VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Indicates whether the timing and sync custom device specified by Device Ref in can drive the RTSI 0 line. This line is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system. icon Inputs/Outputs cu64.png Device Ref in Device Ref in is the reference to the c

### NI VeriStand - Get Timing and Sync Custom Device Is RTSI 0 Capable Flag VI

Indicates whether the timing and sync custom device specified by **Device Ref in** can drive the RTSI 0 line. This line is a digital line that sends a clock signal that synchronizes all hardware I/O devices in the system.

[IMAGE alt='icon' src='ni-veristand-get-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Is RTSI 0 Capable — Is RTSI 0 Capable is TRUE if the device can drive the RTSI 0 line. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Timing and Sync Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-get-waveform-data-reference-vi.html language=unavailable -->
## TOPIC 00107: Ni Veristand Get Waveform Data Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-get-waveform-data-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-get-waveform-data-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-item-reference-to-pointer-vi.html language=enus -->
## TOPIC 00108: NI VeriStand - Item Reference to Pointer VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-item-reference-to-pointer-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-item-reference-to-pointer-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Converts a reference to an item, or node, in a system definition file into a pointer to the same node. You can use this VI to switch from the Custom Device API VIs available in LabVIEW to the System Explorer .NET API. The .NET API uses pointers to nodes. The LabVIEW VIs use references to items. icon

### NI VeriStand - Item Reference to Pointer VI

Converts a reference to an item, or node, in a system definition file into a pointer to the same node. You can use this VI to switch from the Custom Device API VIs available in LabVIEW to the System Explorer .NET API. The .NET API uses pointers to nodes. The LabVIEW VIs use references to items.

[IMAGE alt='icon' src='ni-veristand-item-reference-to-pointer-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Node Pointer — Node Pointer returns the pointer to the node. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

System Explorer Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-move-custom-device-item-vi.html language=enus -->
## TOPIC 00109: NI VeriStand - Move Custom Device Item VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-move-custom-device-item-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-move-custom-device-item-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Moves a custom device item to a new location within the custom device hierarchy. For example, you can use this VI to move a channel from one section to another. If you try to move an item to a location outside of its owning custom device, this VI returns an error. icon Inputs/Outputs cbool.png Highl

### NI VeriStand - Move Custom Device Item VI

Moves a custom device item to a new location within the custom device hierarchy. For example, you can use this VI to move a channel from one section to another. If you try to move an item to a location outside of its owning custom device, this VI returns an error.

[IMAGE alt='icon' src='ni-veristand-move-custom-device-item-vi.png']

#### Inputs/Outputs

| Highlight? (F) — Highlight? specifies whether to make the current item the active item in the System Explorer window configuration tree. The default is FALSE. If you plan to add or move multiple items at once, National Instruments recommends you only highlight the first item. Highlighting every item as it is added or moved can negatively impact performance. Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. New Parent Ref in — New Parent Ref in is the reference to the parent node to move the item to. This can be the top-level of the custom device or a subsection of the device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Moved? — Moved? returns TRUE if the item moved successfully. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-notify-new-log-files-complete-vi.html language=enus -->
## TOPIC 00110: NI VeriStand - Notify New Log Files Complete VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-notify-new-log-files-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-notify-new-log-files-complete-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a notification to clients connected through the VeriStand Gateway that the specified custom device item completed a new log file. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in

### NI VeriStand - Notify New Log Files Complete VI

Sends a notification to clients connected through the VeriStand Gateway that the specified custom device item completed a new log file.

[IMAGE alt='icon' src='ni-veristand-notify-new-log-files-complete-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Log File Paths — Log File Path specifies the path or paths to the log file(s) on the local target. timeout in ms (10000) — timeout in ms specifies the time, in milliseconds, that the NI VeriStand Engine waits for available space in the log notification queue if the queue is full. The default is 10,000 milliseconds. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. timed out? — timed out? returns TRUE if the amount of time specified by timeout in ms (10000) elapses before the notification is successfully sent. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-parse-incoming-command-data-vi.html language=unavailable -->
## TOPIC 00111: Ni Veristand Parse Incoming Command Data Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-parse-incoming-command-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-parse-incoming-command-data-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-pointer-to-item-reference-vi.html language=unavailable -->
## TOPIC 00112: Ni Veristand Pointer To Item Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-pointer-to-item-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-pointer-to-item-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-register-custom-device-engine-events-vi.html language=enus -->
## TOPIC 00113: NI VeriStand - Register Custom Device Engine Events VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-register-custom-device-engine-events-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-register-custom-device-engine-events-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Dynamically registers custom device engine events. This VI registers the events Shut Down, Message (Byte Array), and Message (String). The Shut Down event is triggered when the custom device engine shuts down. The Message events trigger when the NI VeriStand - Send Custom Device Message VI or a corr

### NI VeriStand - Register Custom Device Engine Events VI

Dynamically registers custom device engine events. This VI registers the events Shut Down, Message (Byte Array), and Message (String). The Shut Down event is triggered when the custom device engine shuts down. The Message events trigger when the NI VeriStand - Send Custom Device Message VI or a corresponding .NET method is called.

[IMAGE alt='icon' src='ni-veristand-register-custom-device-engine-events-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. Custom Device Engine Event Ref — Custom Device Engine Event Ref returns the reference to the event registration. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Driver Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-custom-device-item-vi.html language=unavailable -->
## TOPIC 00114: Ni Veristand Remove Custom Device Item Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-custom-device-item-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-custom-device-item-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-item-property-vi.html language=enus -->
## TOPIC 00115: NI VeriStand - Remove Item Property VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-item-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-remove-item-property-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Removes the property specified by Property Name from a custom device item. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a sec

### NI VeriStand - Remove Item Property VI

Removes the property specified by **Property Name** from a custom device item.

[IMAGE alt='icon' src='ni-veristand-remove-item-property-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Removed — Removed is TRUE if the VI successfully removes the property. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-rename-custom-device-item-vi.html language=enus -->
## TOPIC 00116: NI VeriStand - Rename Custom Device Item VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-rename-custom-device-item-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-rename-custom-device-item-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a New Name to the item specified by Item Ref in. If the New Name you specify already exists in the same section, this VI does nothing and the Request invalid? indicator returns TRUE. icon Inputs/Outputs cbool.png Force Rename (F) Force Rename (F) renames the node even if it is protected. cu6

### NI VeriStand - Rename Custom Device Item VI

Applies a **New Name** to the item specified by **Item Ref in**. If the **New Name** you specify already exists in the same section, this VI does nothing and the **Request invalid?** indicator returns TRUE.

[IMAGE alt='icon' src='ni-veristand-rename-custom-device-item-vi.png']

#### Inputs/Outputs

| Force Rename (F) — Force Rename (F) renames the node even if it is protected. Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. New Name — New Name is the new name to apply to the item. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Request invalid? — Request invalid? returns TRUE if the New Name you specify already exists in the section of the custom device that contains the item. All items in a section must have unique names. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Configuration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-reset-custom-device-dependencies-vi.html language=unavailable -->
## TOPIC 00117: Ni Veristand Reset Custom Device Dependencies Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-reset-custom-device-dependencies-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-reset-custom-device-dependencies-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-value-by-data-reference-vi.html language=unavailable -->
## TOPIC 00118: Ni Veristand Set Channel Value By Data Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-value-by-data-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-value-by-data-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-values-by-block-data-reference-vi.html language=enus -->
## TOPIC 00119: NI VeriStand - Set Channel Values by Block Data Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-values-by-block-data-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-channel-values-by-block-data-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the values of the inline custom device channels specified by Block Data Ref. You can use this VI to get multiple channel values at one time. Use the Get Channel Block Data References VI to get the channel data references for this VI. You can use this VI in the Execute Model case of an Inline Mo

### NI VeriStand - Set Channel Values by Block Data Reference VI

Sets the values of the inline custom device channels specified by **Block Data Ref**. You can use this VI to get multiple channel values at one time. Use the Get Channel Block Data References VI to get the channel data references for this VI.

You can use this VI in the Execute Model case of an Inline Model Interface custom device, or in the Read Data from HW or Write Data to HW cases of an Inline Hardware Interface custom device. Do not use this VI outside of an inline custom device.

Note

[IMAGE alt='icon' src='ni-veristand-set-channel-values-by-block-data-reference-vi.png']

#### Inputs/Outputs

| Block Data Ref — Block Data Ref specifies the references to the channels. Use the Get Channel Block Data Values VI to get these references. Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. Values Array in — Values Array in specifies the values for the channels. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Block Data Ref dup — Block Data Ref dup returns the 32-bit channel data references. Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. Values Array out — Values Array out returns the values of the channels. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. |
| Data Reference — Data Reference is the Channel Data Reference of the first channel in the block. Offset — Offset is the index in the Channel Refs array for the first channel in the block. Length — Length is the total bytes of contiguous data in the block. |

Parent topic:

Data References

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-default-value-vi.html language=enus -->
## TOPIC 00120: NI VeriStand - Set Custom Device Channel Default Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-default-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-default-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Default Value for the channel specified by Channel Ref in. The channel retains the Default Value until it receives a new value. icon Inputs/Outputs cu64.png Channel Ref in Channel Ref in is the reference to the channel. cdbl.png Default Value Default Value specifies the default value of the

### NI VeriStand - Set Custom Device Channel Default Value VI

Sets the **Default Value** for the channel specified by **Channel Ref in**. The channel retains the **Default Value** until it receives a new value.

[IMAGE alt='icon' src='ni-veristand-set-custom-device-channel-default-value-vi.png']

#### Inputs/Outputs

| Channel Ref in — Channel Ref in is the reference to the channel. Default Value — Default Value specifies the default value of the channel. The channel retains this value until it receives a new value. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Channel Ref out — Channel Ref out returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-faultability-vi.html language=enus -->
## TOPIC 00121: NI VeriStand - Set Custom Device Channel Faultability VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-faultability-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-faultability-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the VeriStand Engine can fault a channel using software fault insertion. icon Inputs/Outputs cu64.png Channel Ref in Channel Ref in is the reference to the channel. cbool.png Faultability Faultability is TRUE if the channel can be faulted. cerrcodeclst.png error in (no error) error

### NI VeriStand - Set Custom Device Channel Faultability VI

Specifies whether the VeriStand Engine can fault a channel using software fault insertion.

[IMAGE alt='icon' src='ni-veristand-set-custom-device-channel-faultability-vi.png']

#### Inputs/Outputs

| Channel Ref in — Channel Ref in is the reference to the channel. Faultability — Faultability is TRUE if the channel can be faulted. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Channel Ref out — Channel Ref out returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-scalability-vi.html language=enus -->
## TOPIC 00122: NI VeriStand - Set Custom Device Channel Scalability VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-scalability-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-scalability-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether you can scale a channel using the Channel Scaling & Calibration tool. Set Scalability to TRUE if the channel is a hardware channel that might require calibration or scaling into specific engineering units. icon Inputs/Outputs cu64.png Channel Ref in Channel Ref in is the reference

### NI VeriStand - Set Custom Device Channel Scalability VI

Specifies whether you can scale a channel using the Channel Scaling & Calibration tool. Set **Scalability** to TRUE if the channel is a hardware channel that might require calibration or scaling into specific engineering units.

[IMAGE alt='icon' src='ni-veristand-set-custom-device-channel-scalability-vi.png']

#### Inputs/Outputs

| Channel Ref in — Channel Ref in is the reference to the channel. Scalability — Scalability is TRUE if the channel can be scaled. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Channel Ref out — Channel Ref out returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-type-vi.html language=enus -->
## TOPIC 00123: NI VeriStand - Set Custom Device Channel Type VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-type-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets whether the channel specified by Channel Ref in is an Input or an Output channel. Input channels receive values from the VeriStand Engine. Output channels send values to the VeriStand Engine. icon Inputs/Outputs cu64.png Channel Ref in Channel Ref in is the reference to the channel. cenum.png T

### NI VeriStand - Set Custom Device Channel Type VI

Sets whether the channel specified by **Channel Ref in** is an Input or an Output channel. Input channels receive values from the VeriStand Engine. Output channels send values to the VeriStand Engine.

[IMAGE alt='icon' src='ni-veristand-set-custom-device-channel-type-vi.png']

#### Inputs/Outputs

| Channel Ref in — Channel Ref in is the reference to the channel. Type — Type specifies the type of the channel with respect to the custom device. 0 Input—Specifies that the channel receives input data. Select this option if the custom device receives input data from the VeriStand Engine. 1 Output—Specifies that the channel returns output values. Select this option if the custom device passes data to the VeriStand Engine. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Channel Ref out — Channel Ref out returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Input—Specifies that the channel receives input data. Select this option if the custom device receives input data from the VeriStand Engine. |
| 1 | Output—Specifies that the channel returns output values. Select this option if the custom device passes data to the VeriStand Engine. |

Parent topic:

Channel Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-units-vi.html language=enus -->
## TOPIC 00124: NI VeriStand - Set Custom Device Channel Units VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-units-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-channel-units-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the units of measurement for a channel. Units can be any string that makes sense for your custom device. icon Inputs/Outputs cu64.png Channel Ref in Channel Ref in is the reference to the channel. cstr.png Units Units specifies the units to associate with the channel. cerrcodeclst.png error in

### NI VeriStand - Set Custom Device Channel Units VI

Sets the units of measurement for a channel. **Units** can be any string that makes sense for your custom device.

[IMAGE alt='icon' src='ni-veristand-set-custom-device-channel-units-vi.png']

#### Inputs/Outputs

| Channel Ref in — Channel Ref in is the reference to the channel. Units — Units specifies the units to associate with the channel. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Channel Ref out — Channel Ref out returns a reference to the channel. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-decimation-vi.html language=unavailable -->
## TOPIC 00125: Ni Veristand Set Custom Device Decimation Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-decimation-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-decimation-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-drivers-vi.html language=unavailable -->
## TOPIC 00126: Ni Veristand Set Custom Device Drivers Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-drivers-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-drivers-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-version-vi.html language=enus -->
## TOPIC 00127: NI VeriStand - Set Custom Device Version VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-version-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-version-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies information to store with a custom device, such as version information. For example, you later can read the Value string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code.

### NI VeriStand - Set Custom Device Version VI

Specifies information to store with a custom device, such as version information. For example, you later can read the **Value** string to determine whether to update device dependencies or, if you are migrating a custom device to a new version of NI VeriStand, to determine whether to run mutation code. Use the NI VeriStand - Get Custom Device Version VI to return the information this VI specifies.

Note

[IMAGE alt='icon' src='ni-veristand-set-custom-device-version-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. Value — Value specifies version or other information to store with the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-data-type-vi.html language=unavailable -->
## TOPIC 00128: Ni Veristand Set Custom Device Waveform Data Type Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-data-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-data-type-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-units-vi.html language=enus -->
## TOPIC 00129: NI VeriStand - Set Custom Device Waveform Units VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-units-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-custom-device-waveform-units-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the units of measurement for a waveform. Units can be any string that makes sense for your custom device. icon Inputs/Outputs cu64.png Waveform Ref in Waveform Ref in is the reference to the waveform. You must add a custom device waveform to use this parameter. cstr.png Units Units specifies th

### NI VeriStand - Set Custom Device Waveform Units VI

Sets the units of measurement for a waveform. Units can be any string that makes sense for your custom device.

[IMAGE alt='icon' src='ni-veristand-set-custom-device-waveform-units-vi.png']

#### Inputs/Outputs

| Waveform Ref in — Waveform Ref in is the reference to the waveform. You must add a custom device waveform to use this parameter. Units — Units specifies the units to associate with the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Waveform Ref out — Waveform Ref out returns a reference to the waveform. You can wire this output to other custom device Configuration VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Waveform Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-fifo-depth-vi.html language=unavailable -->
## TOPIC 00130: Ni Veristand Set Fifo Depth Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-fifo-depth-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-fifo-depth-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-description-vi.html language=enus -->
## TOPIC 00131: NI VeriStand - Set Item Description VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-description-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-description-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the Description for an item. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. cstr.png Description D

### NI VeriStand - Set Item Description VI

Sets the **Description** for an item.

[IMAGE alt='icon' src='ni-veristand-set-item-description-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Description — Description specifies the description. You can display the description of an item on the configuration page for the item. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-guid-vi.html language=enus -->
## TOPIC 00132: NI VeriStand - Set Item GUID VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-guid-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-guid-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the GUID of the configuration page to associate with an item. You can use this VI to change the page associated with an item at run time. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the de

### NI VeriStand - Set Item GUID VI

Sets the **GUID** of the configuration page to associate with an item. You can use this VI to change the page associated with an item at run time.

[IMAGE alt='icon' src='ni-veristand-set-item-guid-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. GUID — GUID specifies the GUID of the page to associate with the item. A valid GUID is any GUID that is defined in the custom device XML file or any System Explorer XML file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Refresh System Explorer Tree? (F) — Refresh System Explorer Tree? specifies whether to refresh the System Explorer window configuration tree after applying the new GUID. The default is FALSE, which specifies not to refresh the tree. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-property-vi.html language=enus -->
## TOPIC 00133: NI VeriStand - Set Item Property VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-item-property-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. T

### NI VeriStand - Set Item Property VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

Note

[IMAGE alt='icon' src='ni-veristand-set-item-property-vi.png']

- [Set Item Property (Boolean) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-boolean-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (Double Array) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-double-array-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (Double) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-double-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (I32) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-i32-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (Path) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-path-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (String) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-string-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (U16) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-u16-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (Variant) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-variant-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (Dependent Node Pointer) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-node-pointer-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (U32) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-u32-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (Dependent File) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-file-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (U32 Array) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-u32-array-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (I32 Array) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-i32-array-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (String Array) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-string-array-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.
- [Set Item Property (U64) VI](../../../vi-lib/ni-veristand/custom-device-api/set-item-property-u64-vi.html) Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance.

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-log-file-producer-flag-vi.html language=enus -->
## TOPIC 00134: NI VeriStand - Set Log File Producer Flag VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-log-file-producer-flag-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-log-file-producer-flag-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a property for the specified custom device item that indicates whether the item produces log files. When TRUE, you can use the Data Logging control to download log files produced by the item. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A cu

### NI VeriStand - Set Log File Producer Flag VI

Sets a property for the specified custom device item that indicates whether the item produces log files. When TRUE, you can use the Data Logging control to download log files produced by the item.

[IMAGE alt='icon' src='ni-veristand-set-log-file-producer-flag-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Log File Producer — Log File Producer specifies whether the custom device item produces log files. TRUE specifies the item produces log files. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Item Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-loop-flags-vi.html language=enus -->
## TOPIC 00135: NI VeriStand - Set Loop Flags VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-loop-flags-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-loop-flags-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the flags that determine what steps the custom device skips. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a

### NI VeriStand - Set Loop Flags VI

Sets the flags that determine what steps the custom device skips.

[IMAGE alt='icon' src='ni-veristand-set-loop-flags-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Loop Flags — Loop Flags sets the state of loop flags. Disable "Execute Model" — Disable "Execute Model" determines whether to skip the Execute Model step of an Inline Model Custom Device. Disable "Read Data from HW" — Disable "Read Data from HW" determines whether to skip the Read Data from HW step of an Inline HW Custom Device. Disable "Write Data to HW" — Disable "Write Data to HW" determines whether to skip the Write Data to HW step of an Inline HW Custom Device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| Disable "Execute Model" — Disable "Execute Model" determines whether to skip the Execute Model step of an Inline Model Custom Device. Disable "Read Data from HW" — Disable "Read Data from HW" determines whether to skip the Read Data from HW step of an Inline HW Custom Device. Disable "Write Data to HW" — Disable "Write Data to HW" determines whether to skip the Write Data to HW step of an Inline HW Custom Device. |

Parent topic:

Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-loop-type-vi.html language=enus -->
## TOPIC 00136: NI VeriStand - Set Loop Type VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-loop-type-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-loop-type-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the asynchronous custom device uses a While Loop or a Timed Loop. If Loop type is 1 - Timed Loop, you can use the Use Device Clock input to synchronize the loop to the Primary Control Loop's timing source. Do not use this VI on inline custom devices. You also can use the NI VeriSta

### NI VeriStand - Set Loop Type VI

Specifies whether the asynchronous custom device uses a While Loop or a Timed Loop. If **Loop type** is 1 - Timed Loop, you can use the **Use Device Clock** input to synchronize the loop to the Primary Control Loop's timing source. Do not use this VI on inline custom devices.

Note

[IMAGE alt='icon' src='ni-veristand-set-loop-type-vi.png']

#### Inputs/Outputs

| Device Ref in — Device Ref in is the reference to the custom device. Loop type — Loop type specifies the loop type. 0 While Loop—Specifies that the custom device runs in a While Loop. 1 Timed Loop—Specifies that the custom device runs in a Timed Loop. Use Device Clock (Timed Loops only) — Use Device Clock (Timed Loops only) specifies whether to synchronize the Timed Loop with the Primary Control Loop's timing source. If Loop type is 0 - While Loop, this input must be FALSE. The default is FALSE. If TRUE, the system passes the timing source from the Primary Control Loop to the custom device driver VI. The Primary Control Loop runs the custom device Timed Loop after NI VeriStand sets the outputs of the custom device. This prevents the Primary Control Loop from running late if the custom device finishes late. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | While Loop—Specifies that the custom device runs in a While Loop. |
| 1 | Timed Loop—Specifies that the custom device runs in a Timed Loop. |

Parent topic:

Asynchronous Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-timed-loop-priority-vi.html language=unavailable -->
## TOPIC 00137: Ni Veristand Set Timed Loop Priority Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-timed-loop-priority-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-timed-loop-priority-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-set-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.html language=unavailable -->
## TOPIC 00138: Ni Veristand Set Timing And Sync Custom Device Is Rtsi 0 Capable Flag Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-set-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-set-timing-and-sync-custom-device-is-rtsi-0-capable-flag-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-signal-when-ready-for-shutdown-vi.html language=unavailable -->
## TOPIC 00139: Ni Veristand Signal When Ready For Shutdown Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-signal-when-ready-for-shutdown-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-signal-when-ready-for-shutdown-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-specify-custom-device-execution-mode-vi.html language=enus -->
## TOPIC 00140: NI VeriStand - Specify Custom Device Execution Mode VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-specify-custom-device-execution-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-specify-custom-device-execution-mode-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the execution mode of a custom device. Ensure the driver VI for the custom device is based on the template associated with the Execution Mode you specify. You can set the custom device execution mode only when you configure the device. The user cannot update this information at run time. i

### NI VeriStand - Specify Custom Device Execution Mode VI

Specifies the execution mode of a custom device. Ensure the driver VI for the custom device is based on the template associated with the **Execution Mode** you specify.

Note

[IMAGE alt='icon' src='ni-veristand-specify-custom-device-execution-mode-vi.png']

#### Inputs/Outputs

| Execution Mode — Execution Mode specifies when the custom device runs with respect to other operations performed by the VeriStand Engine. 0 Asynchronous—(Default) Specifies that the custom device executes in a parallel loop to the Primary Control Loop. The device uses RT FIFOs to read and write data from and to the Primary Control Loop. 1 Inline HW Interface—Specifies that the custom device executes inline in the Primary Control Loop. This mode contains a Read Data from HW section of code that executes near the beginning of the Primary Control Loop iteration and a Write Data to HW section of code that executes near the end of the Primary Control Loop iteration. The Read Data from HW code outputs data to NI VeriStand, while the Write Data to HW code reads input data from NI VeriStand. 2 Inline Model Interface—Specifies that the custom device executes inline in the Primary Control Loop. This mode contains an Execute Model section of code that executes in the middle of the Primary Control Loop iteration. This code reads input data, performs a calculation, and then writes output data to NI VeriStand. Using the Inline Model Interface mode enables you to process data acquired from hardware inputs and send the processed values to hardware outputs with no latency. 3 Inline Timing and Sync—Specifies that the custom device executes inline in the Primary Control Loop as a timing and sync device. This mode of execution is identical to the Inline HW Interface mode, except that choosing this option creates a timing and sync device, rather than a custom device. 4 Asynchronous Timing and Sync—Specifies that the custom device executes as a timing and sync device in a parallel loop to the Primary Control Loop. This mode of execution is identical to the Asynchronous mode, except that choosing this option creates a timing and sync device, rather than a custom device. Device Ref in — Device Ref in is the reference to the custom device. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Device Ref out — Device Ref out returns a reference to the custom device. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| 0 | Asynchronous—(Default) Specifies that the custom device executes in a parallel loop to the Primary Control Loop. The device uses RT FIFOs to read and write data from and to the Primary Control Loop. |
| 1 | Inline HW Interface—Specifies that the custom device executes inline in the Primary Control Loop. This mode contains a Read Data from HW section of code that executes near the beginning of the Primary Control Loop iteration and a Write Data to HW section of code that executes near the end of the Primary Control Loop iteration. The Read Data from HW code outputs data to NI VeriStand, while the Write Data to HW code reads input data from NI VeriStand. |
| 2 | Inline Model Interface—Specifies that the custom device executes inline in the Primary Control Loop. This mode contains an Execute Model section of code that executes in the middle of the Primary Control Loop iteration. This code reads input data, performs a calculation, and then writes output data to NI VeriStand. Using the Inline Model Interface mode enables you to process data acquired from hardware inputs and send the processed values to hardware outputs with no latency. |
| 3 | Inline Timing and Sync—Specifies that the custom device executes inline in the Primary Control Loop as a timing and sync device. This mode of execution is identical to the Inline HW Interface mode, except that choosing this option creates a timing and sync device, rather than a custom device. |
| 4 | Asynchronous Timing and Sync—Specifies that the custom device executes as a timing and sync device in a parallel loop to the Primary Control Loop. This mode of execution is identical to the Asynchronous mode, except that choosing this option creates a timing and sync device, rather than a custom device. |

Parent topic:

Device Properties

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-unset-busy-cursor-vi.html language=enus -->
## TOPIC 00141: NI VeriStand - Unset Busy Cursor VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-unset-busy-cursor-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-unset-busy-cursor-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Releases the front panel cursor of the System Explorer window. Use this VI after a Page VI finishes initializing. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ierrco

### NI VeriStand - Unset Busy Cursor VI

Releases the front panel cursor of the **System Explorer** window. Use this VI after a Page VI finishes initializing.

[IMAGE alt='icon' src='ni-veristand-unset-busy-cursor-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

System Explorer Functions

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/ni-veristand-update-custom-device-flag-vi.html language=unavailable -->
## TOPIC 00142: Ni Veristand Update Custom Device Flag Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/ni-veristand-update-custom-device-flag-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/ni-veristand-update-custom-device-flag-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-boolean-vi.html language=enus -->
## TOPIC 00143: Set Item Property (Boolean) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-boolean-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-boolean-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (Boolean) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-boolean-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-file-vi.html language=enus -->
## TOPIC 00144: Set Item Property (Dependent File) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-file-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (Dependent File) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-dependent-file-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Path — Path specifies the path to the dependent file. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. OptionalInfo — OptionalInfo specifies optional information about the dependent file, such as version information and the target operating system(s) to which it is configured to deploy. Version — Version specifies version information for the dependency. RTDestination — RTDestination specifies the destination directory, including the filename, for the dependency on the target. RTDestination must be an absolute path. ForceDownload — ForceDownload specifies whether to force the download of the dependency. This terminal must be FALSE. SupportedTarget — SupportedTarget specifies the target operating system(s) to which you are deploying the custom device. 0 All—Specifies that you are deploying the custom device to all supported operating systems. 1 PharLap—(Default) Specifies that you are deploying the custom device to a Phar Lap operating system. 2 VxWorks—Specifies that you are deploying the custom device to a VxWorks operating system. 3 Windows—Specifies that you are deploying the custom device to a Windows operating system. 4 Linux_32_ARM—Specifies that you are deploying the custom device to a Linux_32_ARM operating system. 5 Linux_x64—Specifies that you are deploying the custom device to a Linux_x64 operating system. 6 PharLap & Windows—Specifies that you are deploying the custom device to Phar Lap and Windows operating systems. 7 PharLap & VxWorks—Specifies that you are deploying the custom device to Phar Lap and VxWorks operating systems. 8 VxWorks & Windows—Specifies that you are deploying the custom device to VxWorks and Windows operating systems. MD5 — MD5 specifies an MD5 message-digest for the file specified in Path. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |  |
| --- | --- |
| Version — Version specifies version information for the dependency. RTDestination — RTDestination specifies the destination directory, including the filename, for the dependency on the target. RTDestination must be an absolute path. ForceDownload — ForceDownload specifies whether to force the download of the dependency. This terminal must be FALSE. SupportedTarget — SupportedTarget specifies the target operating system(s) to which you are deploying the custom device. 0 All—Specifies that you are deploying the custom device to all supported operating systems. 1 PharLap—(Default) Specifies that you are deploying the custom device to a Phar Lap operating system. 2 VxWorks—Specifies that you are deploying the custom device to a VxWorks operating system. 3 Windows—Specifies that you are deploying the custom device to a Windows operating system. 4 Linux_32_ARM—Specifies that you are deploying the custom device to a Linux_32_ARM operating system. 5 Linux_x64—Specifies that you are deploying the custom device to a Linux_x64 operating system. 6 PharLap & Windows—Specifies that you are deploying the custom device to Phar Lap and Windows operating systems. 7 PharLap & VxWorks—Specifies that you are deploying the custom device to Phar Lap and VxWorks operating systems. 8 VxWorks & Windows—Specifies that you are deploying the custom device to VxWorks and Windows operating systems. MD5 — MD5 specifies an MD5 message-digest for the file specified in Path. |  |
| 0 | All—Specifies that you are deploying the custom device to all supported operating systems. |
| 1 | PharLap—(Default) Specifies that you are deploying the custom device to a Phar Lap operating system. |
| 2 | VxWorks—Specifies that you are deploying the custom device to a VxWorks operating system. |
| 3 | Windows—Specifies that you are deploying the custom device to a Windows operating system. |
| 4 | Linux_32_ARM—Specifies that you are deploying the custom device to a Linux_32_ARM operating system. |
| 5 | Linux_x64—Specifies that you are deploying the custom device to a Linux_x64 operating system. |
| 6 | PharLap & Windows—Specifies that you are deploying the custom device to Phar Lap and Windows operating systems. |
| 7 | PharLap & VxWorks—Specifies that you are deploying the custom device to Phar Lap and VxWorks operating systems. |
| 8 | VxWorks & Windows—Specifies that you are deploying the custom device to VxWorks and Windows operating systems. |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-node-pointer-vi.html language=unavailable -->
## TOPIC 00145: Set Item Property Dependent Node Pointer Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-node-pointer-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-dependent-node-pointer-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-double-array-vi.html language=enus -->
## TOPIC 00146: Set Item Property (Double Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-double-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-double-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (Double Array) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-double-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-double-vi.html language=enus -->
## TOPIC 00147: Set Item Property (Double) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-double-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-double-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (Double) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-double-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-i32-array-vi.html language=enus -->
## TOPIC 00148: Set Item Property (I32 Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-i32-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-i32-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (I32 Array) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-i32-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-i32-vi.html language=enus -->
## TOPIC 00149: Set Item Property (I32) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-i32-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-i32-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (I32) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-i32-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-path-vi.html language=unavailable -->
## TOPIC 00150: Set Item Property Path Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-path-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-string-array-vi.html language=enus -->
## TOPIC 00151: Set Item Property (String Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-string-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-string-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (String Array) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-string-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. The strings in this array must consist of printable characters only. Tip If your array includes binary strings, use the Flatten to String function to convert the array to a single string. You then can use the String instance of this VI and set Binary String to TRUE. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-string-vi.html language=enus -->
## TOPIC 00152: Set Item Property (String) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-string-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (String) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-string-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Binary String (T) — Binary String is TRUE if the Value string contains binary data, such as if it is created by the Flatten to String function. The default is TRUE, which works for any string regardless of whether the string contains binary data. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-u16-vi.html language=enus -->
## TOPIC 00153: Set Item Property (U16) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-u16-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-u16-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (U16) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-u16-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-u32-array-vi.html language=enus -->
## TOPIC 00154: Set Item Property (U32 Array) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-u32-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-u32-array-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (U32 Array) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-u32-array-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-u32-vi.html language=unavailable -->
## TOPIC 00155: Set Item Property U32 Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-u32-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-u32-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-u64-vi.html language=enus -->
## TOPIC 00156: Set Item Property (U64) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-u64-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-u64-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets a Property Name and Value for an item property and saves this information in the system definition file. If the Property Name you specify already exists, this VI overwrites the property. Wire data to the Value input to determine the polymorphic instance to use or manually select the instance. i

### Set Item Property (U64) VI

Sets a **Property Name** and **Value** for an item property and saves this information in the system definition file. If the **Property Name** you specify already exists, this VI overwrites the property. Wire data to the **Value** input to determine the polymorphic instance to use or manually select the instance.

[IMAGE alt='icon' src='set-item-property-u64-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Property Name — Property Name specifies the name of the property. Property names are case-sensitive. Value — Value specifies the value of the property. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Replaced — Replaced is TRUE if this VI overwrites the value of an existing property. |
| --- |

Parent topic:

NI VeriStand - Set Item Property VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-api/set-item-property-variant-vi.html language=unavailable -->
## TOPIC 00157: Set Item Property Variant Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-api/set-item-property-variant-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-api/set-item-property-variant-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-add-sections-recursively-by-relative-path-vi.html language=enus -->
## TOPIC 00158: NI VeriStand - Add Sections Recursively by Relative Path VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-add-sections-recursively-by-relative-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-add-sections-recursively-by-relative-path-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Recursively adds sections to a custom device section relative to the item specified by Section Ref in. This VI also sets the GUIDs for the configuration pages to associate with the new sections. If a section with the name you specify already exists, this VI does not overwrite the section. icon Input

### NI VeriStand - Add Sections Recursively by Relative Path VI

Recursively adds sections to a custom device section relative to the item specified by **Section Ref in**. This VI also sets the GUIDs for the configuration pages to associate with the new sections. If a section with the name you specify already exists, this VI does not overwrite the section.

[IMAGE alt='icon' src='ni-veristand-add-sections-recursively-by-relative-path-vi.png']

#### Inputs/Outputs

| GUID (Default Section) — GUID is the GUID of the page to associate with the new section, as defined in the custom device XML file. If you do not specify a GUID, this VI uses the default section specification page. Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. Relative Section Path — Relative Section Path specifies the relative path to the section(s) you want to create. Example Path Corresponding Location in Custom Device Hierarchy My Inputs/abc <section>/My Inputs/abc My Inputs/abc/ <section>/My Inputs/abc ./My Inputs/abc <section>/My Inputs/abc ../../Other Section <section grandparent>/<section parent>/Other Section /My Controller/abc <root>/My Controller/abc error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Item Ref — Item Ref returns the reference to the newly created section. error out — error out contains error information. This output provides standard error out functionality. Added — Added is TRUE if the VI adds the section(s) successfully. |  |
| --- | --- |
| Example Path | Corresponding Location in Custom Device Hierarchy |
| My Inputs/abc | <section>/My Inputs/abc |
| My Inputs/abc/ | <section>/My Inputs/abc |
| ./My Inputs/abc | <section>/My Inputs/abc |
| ../../Other Section | <section grandparent>/<section parent>/Other Section |
| /My Controller/abc | <root>/My Controller/abc |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-advanced-browsing-dialog-vi.html language=enus -->
## TOPIC 00159: NI VeriStand - Advanced Browsing Dialog VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-advanced-browsing-dialog-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-advanced-browsing-dialog-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures an advanced browsing dialog box for files that match the File Pattern you specify. This VI creates the same style browsing dialog that appears in NI VeriStand if you select Advanced browsing on the Folder Start Paths page of the Options dialog box. The NI VeriStand user must select Advanc

### NI VeriStand - Advanced Browsing Dialog VI

Configures an advanced browsing dialog box for files that match the **File Pattern** you specify. This VI creates the same style browsing dialog that appears in NI VeriStand if you select **Advanced browsing** on the **Folder Start Paths** page of the **Options** dialog box.

Note

Advanced Browsing

Browse

[IMAGE alt='icon' src='ni-veristand-advanced-browsing-dialog-vi.png']

#### Inputs/Outputs

| Pattern Label — Pattern Label specifies a label to display in the file dialog box next to the File Pattern. If you do not wire this input or it contains an empty string, the default label next to any custom File Pattern is Custom Pattern. CtlRef — CtlRef is a reference to the LabVIEW control that launches the dialog box. The control must be a cluster that contains a path control and a Boolean control, where the path control contains the paths users enter, and the Boolean control represents the Browse button or option. Dialog Title — Dialog Title specifies text to display in the title bar of the dialog box. Paths — Paths specifies paths that appear in the Path pull-down menu of the browsing dialog box. A user can select the Paths you add to quickly display all the files in a directory that match the required File Pattern. Note The browsing dialog performs a recursive search to find all the files in a directory and its subdirectories that match the File Pattern. For better performance, specify deeper directory Paths. For example, specify C:\\Documents and Settings\\My Documents instead of C:\\. Most recent path — Most recent path specifies the most recently entered path in the browsing dialog. The browsing dialog box uses this input to determine the directory to display when a user clicks the Browse option in the Path pull-down menu. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. File Pattern — File Pattern restricts the files displayed in the dialog box to those that match the File Pattern. Selected file — Selected file returns the full path to the file selected using this dialog box. Most recent folder — Most recent folder returns the path to the directory or folder that contains the Selected file. error out — error out contains error information. This output provides standard error out functionality. Valid? — Valid? is TRUE if the user navigates to a valid file location. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-channels-vi.html language=enus -->
## TOPIC 00160: NI VeriStand - Get All Channels VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-channels-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-channels-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of channel references for all the channels within the section specified by Section Ref in. The array includes references to both input and output channels. This VI performs a depth-first deep search. icon Inputs/Outputs cu64.png Section Ref in Section Ref in is a reference to a section

### NI VeriStand - Get All Channels VI

Gets an array of channel references for all the channels within the section specified by **Section Ref in**. The array includes references to both input and output channels.

This VI performs a depth-first deep search.

[IMAGE alt='icon' src='ni-veristand-get-all-channels-vi.png']

#### Inputs/Outputs

| Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Channel Refs — Channel Refs returns the array of channel references. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds channels in Section Ref in. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-waveforms-vi.html language=enus -->
## TOPIC 00161: NI VeriStand - Get All Waveforms VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-waveforms-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-all-waveforms-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets an array of references for all the waveforms within the custom-device section specified by Section Ref in. This VI performs a depth-first deep search. icon Inputs/Outputs cu64.png Section Ref in Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Sec

### NI VeriStand - Get All Waveforms VI

Gets an array of references for all the waveforms within the custom-device section specified by **Section Ref in**.

This VI performs a depth-first deep search.

[IMAGE alt='icon' src='ni-veristand-get-all-waveforms-vi.png']

#### Inputs/Outputs

| Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Waveform Refs — Waveform Refs returns the array of waveform references. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds waveforms in Section Ref in. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-channel-fifo-buffer-index-vi.html language=unavailable -->
## TOPIC 00162: Ni Veristand Get Channel Fifo Buffer Index Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-channel-fifo-buffer-index-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-channel-fifo-buffer-index-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-item-ref-by-relative-path-vi.html language=enus -->
## TOPIC 00163: NI VeriStand - Get Item Ref by Relative Path VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-item-ref-by-relative-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-item-ref-by-relative-path-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a reference to a custom device item from a specified location relative to Section Ref in. Use one forward slash (/) as a separator between sections in the relative path. Like a standard file system, ".." traverses up the hierarchy one level. A leading forward slash indicates an absolute path

### NI VeriStand - Get Item Ref by Relative Path VI

Returns a reference to a custom device item from a specified location relative to **Section Ref in**. Use one forward slash (/) as a separator between sections in the relative path. Like a standard file system, ".." traverses up the hierarchy one level. A leading forward slash indicates an absolute path from the root item of the hierarchy.

[IMAGE alt='icon' src='ni-veristand-get-item-ref-by-relative-path-vi.png']

#### Inputs/Outputs

| Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. Relative Item Path — Relative Item Path specifies the relative path to the item. Example Path Corresponding Location in Custom Device Hierarchy My Inputs/abc <section>/My Inputs/abc My Inputs/abc/ <section>/My Inputs/abc ./My Inputs/abc <section>/My Inputs/abc ../../Other Section <section grandparent>/<section parent>/Other Section /My Controller/abc <root>/My Controller/abc error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Item Ref — Item Ref returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |  |
| --- | --- |
| Example Path | Corresponding Location in Custom Device Hierarchy |
| My Inputs/abc | <section>/My Inputs/abc |
| My Inputs/abc/ | <section>/My Inputs/abc |
| ./My Inputs/abc | <section>/My Inputs/abc |
| ../../Other Section | <section grandparent>/<section parent>/Other Section |
| /My Controller/abc | <root>/My Controller/abc |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-multiple-dependent-node-refs-vi.html language=enus -->
## TOPIC 00164: NI VeriStand - Get Multiple Dependent Node Refs VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-multiple-dependent-node-refs-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-multiple-dependent-node-refs-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the dependent node references that are set as values for properties of an item you specify. Dependent node references map to other nodes in the custom device, such as channels from which properties get their values. All the properties must share the same base name. This VI increments a decimal

### NI VeriStand - Get Multiple Dependent Node Refs VI

Gets the dependent node references that are set as values for properties of an item you specify. Dependent node references map to other nodes in the custom device, such as channels from which properties get their values. 

All the properties must share the same base name. This VI increments a decimal appended to the **Base Property Name** until it cannot find any more properties.

[IMAGE alt='icon' src='ni-veristand-get-multiple-dependent-node-refs-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Base Property Name — Base Property Name specifies the base name of the properties to get Dependent Node Refs for. Property names are case-sensitive. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. Dependent Node Refs — Dependent Node Refs returns the dependent node references that are set as property values on the item. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-next-unique-label-vi.html language=unavailable -->
## TOPIC 00165: Ni Veristand Get Next Unique Label Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-next-unique-label-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-next-unique-label-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-target-ref-vi.html language=unavailable -->
## TOPIC 00166: Ni Veristand Get Target Ref Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-target-ref-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-get-target-ref-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-highlight-node-in-system-explorer-vi.html language=unavailable -->
## TOPIC 00167: Ni Veristand Highlight Node In System Explorer Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-highlight-node-in-system-explorer-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-highlight-node-in-system-explorer-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-not-a-ref-vi.html language=unavailable -->
## TOPIC 00168: Ni Veristand Not A Ref Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-not-a-ref-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-not-a-ref-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-ref-constants-vi.html language=enus -->
## TOPIC 00169: NI VeriStand - Ref Constants VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-ref-constants-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-ref-constants-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates a global variable that you can use as a reference to the root item in the custom device hierarchy, or as an invalid reference. icon Data type cu64.png Invalid Ref Invalid Ref is an invalid reference. cu64.png Root Item Ref Root Item Ref is a reference to the root item in the custom device hi

### NI VeriStand - Ref Constants VI

Creates a global variable that you can use as a reference to the root item in the custom device hierarchy, or as an invalid reference.

[IMAGE alt='icon' src='ni-veristand-ref-constants-vi.png']

#### Data type

| Invalid Ref — Invalid Ref is an invalid reference. Root Item Ref — Root Item Ref is a reference to the root item in the custom device hierarchy. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-report-final-error-status-vi.html language=enus -->
## TOPIC 00170: NI VeriStand - Report Final Error Status VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-report-final-error-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-report-final-error-status-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reports a final error status from an asynchronous custom device to the VeriStand Engine. The VeriStand Engine checks the error status when the system shuts down. icon Inputs/Outputs cnotern.png Status Notifier Status Notifier is a notifier refnum to the error cluster that contains the final error st

### NI VeriStand - Report Final Error Status VI

Reports a final error status from an asynchronous custom device to the VeriStand Engine. The VeriStand Engine checks the error status when the system shuts down.

[IMAGE alt='icon' src='ni-veristand-report-final-error-status-vi.png']

#### Inputs/Outputs

| Status Notifier — Status Notifier is a notifier refnum to the error cluster that contains the final error status. This VI returns the error status to the VeriStand Engine and checks when the system is shutting down. Filter FIFO & Shutdown Errors (T) — Filter FIFO & Shutdown Errors specifies whether to filter errors returned by RT FIFO functions. RT FIFO errors are generally expected, because the VeriStand Engine shuts down the input and output FIFOs for the custom device as part of the device shut down process. The default is TRUE, filter errors. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-guid-vi.html language=enus -->
## TOPIC 00171: NI VeriStand - Search for All Items by GUID VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-guid-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-guid-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use. icon Inputs/Outputs cu64.png Section Ref in Section Ref in is a reference to a section of a cust

### NI VeriStand - Search for All Items by GUID VI

Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-search-for-all-items-by-guid-vi.png']

#### Inputs/Outputs

| Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. Item GUID — Item GUID specifies the unique GUID of the configuration page associated with the item. Find All? (T) — Find All? (T) if true, continues searching after first match. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Item Refs — Item Refs returns references to all the items that match the search criteria. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

NI VeriStand - Search for Item VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-name-vi.html language=enus -->
## TOPIC 00172: NI VeriStand - Search for All Items by Name VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-name-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use. icon Inputs/Outputs cu64.png Section Ref in Section Ref in is a reference to a section of a cust

### NI VeriStand - Search for All Items by Name VI

Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-search-for-all-items-by-name-vi.png']

#### Inputs/Outputs

| Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. Item Name — Item Name specifies the name of the item. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Item Refs — Item Refs returns references to all the items that match the search criteria. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

NI VeriStand - Search for Item VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-property-vi.html language=unavailable -->
## TOPIC 00173: Ni Veristand Search For All Items By Property Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-property-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-guid-vi.html language=enus -->
## TOPIC 00174: NI VeriStand - Search for Item by GUID VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-guid-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-guid-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use. icon Inputs/Outputs cenum.png Direction (Down) Direction (Down) specifies the direction in which

### NI VeriStand - Search for Item by GUID VI

Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-search-for-item-by-guid-vi.png']

#### Inputs/Outputs

| Direction (Down) — Direction (Down) specifies the direction in which to search. 0 Down (default)—Searches from the Section Ref in down through the custom device hierarchy. 1 Up—Searches up from the Section Ref in up through the custom device hierarchy. Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. Item GUID — Item GUID specifies the unique GUID of the configuration page associated with the item. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Item Ref — Item Ref returns the reference to the item. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |  |
| --- | --- |
| 0 | Down (default)—Searches from the Section Ref in down through the custom device hierarchy. |
| 1 | Up—Searches up from the Section Ref in up through the custom device hierarchy. |

Parent topic:

NI VeriStand - Search for Item VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-name-vi.html language=enus -->
## TOPIC 00175: NI VeriStand - Search for Item by Name VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-name-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-name-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use. icon Inputs/Outputs cu64.png Section Ref in Section Ref in is a reference to a section of a cust

### NI VeriStand - Search for Item by Name VI

Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-search-for-item-by-name-vi.png']

#### Inputs/Outputs

| Section Ref in — Section Ref in is a reference to a section of a custom device. You can use the Add Custom Device Section VI to get this reference. Item Name — Item Name specifies the name of the item. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Section Ref out — Section Ref out returns the reference to the section. Item Ref — Item Ref returns the reference to the item. error out — error out contains error information. This output provides standard error out functionality. Found — Found is TRUE if the VI finds the item. |
| --- |

Parent topic:

NI VeriStand - Search for Item VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-property-vi.html language=unavailable -->
## TOPIC 00176: Ni Veristand Search For Item By Property Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-property-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-property-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-vi.html language=enus -->
## TOPIC 00177: NI VeriStand - Search for Item VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use. icon

### NI VeriStand - Search for Item VI

Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.

[IMAGE alt='icon' src='ni-veristand-search-for-item-vi.png']

- [NI VeriStand - Search for Item by Name VI](../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-name-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.
- [NI VeriStand - Search for Item by GUID VI](../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-guid-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.
- [NI VeriStand - Search for Item by Property VI](../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-item-by-property-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.
- [NI VeriStand - Search for All Items by Name VI](../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-name-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.
- [NI VeriStand - Search for All Items by GUID VI](../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-guid-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.
- [NI VeriStand - Search for All Items by Property VI](../../../../vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-search-for-all-items-by-property-vi.html) Searches a custom device section for the item(s) you specify. You can search for one or multiple items by name, GUID, or property name and value. You must manually select the polymorphic instance to use.

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-set-multiple-dependent-node-refs-vi.html language=enus -->
## TOPIC 00178: NI VeriStand - Set Multiple Dependent Node Refs VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-set-multiple-dependent-node-refs-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-set-multiple-dependent-node-refs-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets multiple properties, with dependent node references as values, on a custom device item. Dependent node references map to other nodes in the custom device, such as channels from which properties get their values. icon Inputs/Outputs cu64.png Item Ref in Item Ref in is a reference to an item in a

### NI VeriStand - Set Multiple Dependent Node Refs VI

Sets multiple properties, with dependent node references as values, on a custom device item. Dependent node references map to other nodes in the custom device, such as channels from which properties get their values.

[IMAGE alt='icon' src='ni-veristand-set-multiple-dependent-node-refs-vi.png']

#### Inputs/Outputs

| Item Ref in — Item Ref in is a reference to an item in a custom device. A custom device item is any item that appears under the device in the System Explorer window configuration tree, such as a section or a channel. Base Property Name — Base Property Name specifies the base name of the property. This VI appends an incremented decimal number to the base property name for each reference in the Dependent Node Refs array. Property names are case-sensitive. Dependent Node Refs — Dependent Node Refs specifies the dependent node references to set as property values on the item. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Item Ref out — Item Ref out returns a reference to the item in the custom device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-system-definition-file-path-vi.html language=enus -->
## TOPIC 00179: NI VeriStand - System Definition File Path VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-system-definition-file-path-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-tools/custom-device-utility-library/ni-veristand-system-definition-file-path-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the file path to the active NI VeriStand system definition file (.nivssdf) after the system definition is deployed. icon Inputs/Outputs cerrcodeclst.png error in (no error) error in describes error conditions that occur before this node runs. This input provides standard error in functionali

### NI VeriStand - System Definition File Path VI

Returns the file path to the active NI VeriStand system definition file (.nivssdf) after the system definition is deployed.

[IMAGE alt='icon' src='ni-veristand-system-definition-file-path-vi.png']

#### Inputs/Outputs

| error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. SDF path — SDF path is the path to the current NI VeriStand system definition file. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utilities

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-close-multiple-waveforms-read-session-cdb-vi.html language=unavailable -->
## TOPIC 00180: Ni Veristand Close Multiple Waveforms Read Session Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-close-multiple-waveforms-read-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-close-multiple-waveforms-read-session-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-open-multiple-waveforms-read-session-cdb-vi.html language=enus -->
## TOPIC 00181: NI VeriStand - Open Multiple Waveforms Read Session (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-open-multiple-waveforms-read-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-open-multiple-waveforms-read-session-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Multiple Waveforms Read Session (CDB) VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-multiple-waveforms-read-session-cdb-vi.png']

#### Inputs/Outputs

| Communication Properties — Communication Properties contains elements that set the size of the queue used to store data the custom device reads and writes. National Instruments recommends changing these values only if you notice data loss is occurring. WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. CDB Waveform Data References — CDB Waveform Data References is an array of data references to waveforms, which you must first generate. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Read Session (CDB) — Multiple Waveforms Read Session (CDB) returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |
| Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |

Parent topic:

NI VeriStand - Open Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-read-multiple-waveforms-cdb-vi.html language=unavailable -->
## TOPIC 00182: Ni Veristand Read Multiple Waveforms Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-read-multiple-waveforms-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-read-multiple-waveforms-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-close-multiple-waveforms-read-session-dbl-vi.html language=enus -->
## TOPIC 00183: NI VeriStand - Close Multiple Waveforms Read Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-close-multiple-waveforms-read-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-close-multiple-waveforms-read-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Multiple_Waveforms_Read_(DBL)lvclass.png Multiple Waveforms Read Session (DBL) Multiple Waveforms Read Sessi

### NI VeriStand - Close Multiple Waveforms Read Session (DBL) VI

Closes a waveform read or write session. Wire data to the **Single Waveform Read Session (DBL)** input to specify the instance to use.

[IMAGE alt='icon' src='ni-veristand-close-multiple-waveforms-read-session-dbl-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Read Session (DBL) — Multiple Waveforms Read Session (DBL) is a reference to the waveform session. You must open a waveform session to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Close Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-open-multiple-waveforms-read-session-dbl-vi.html language=enus -->
## TOPIC 00184: NI VeriStand - Open Multiple Waveforms Read Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-open-multiple-waveforms-read-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-open-multiple-waveforms-read-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Multiple Waveforms Read Session (DBL) VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-multiple-waveforms-read-session-dbl-vi.png']

#### Inputs/Outputs

| Communication Properties — Communication Properties contains elements that set the size of the queue used to store data the custom device reads and writes. National Instruments recommends changing these values only if you notice data loss is occurring. WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. DBL Waveform Data References — DBL Waveform Data References is an array of data references to waveforms, which you must first generate. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Read Session (DBL) — Multiple Waveforms Read Session (DBL) returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |
| Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |

Parent topic:

NI VeriStand - Open Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-read-multiple-waveforms-dbl-vi.html language=enus -->
## TOPIC 00185: NI VeriStand - Read Multiple Waveforms (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-read-multiple-waveforms-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-read-multiple-waveforms-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a waveform(s) associated with the specified read session. This VI executes whenever any waveform returns data, and the VI returns data from only that waveform. You can identify the specific waveform that returned data. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Mult

### NI VeriStand - Read Multiple Waveforms (DBL) VI

Reads data from a waveform(s) associated with the specified read session.

Note

[IMAGE alt='icon' src='ni-veristand-read-multiple-waveforms-dbl-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Read Session (DBL) in — Multiple Waveforms Read Session (DBL) in is a reference to the waveform session. You must open a waveform session to use this parameter. timeout in ms (-1) — timeout in ms specifies the time in milliseconds to wait for an element to become available in the queue if the queue is empty. The default is -1, indicating never to time out. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Read Session (DBL) out — Multiple Waveforms Read Session (DBL) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. Data — Data returns an array of values read from any waveform that returns data. Properties — Properties contains the following elements that describe the waveform Data this VI returns: Data reference — Data reference returns the data reference for the waveform in the read session that returned Data. t0 at start — t0 at start specifies the start time of the first sample in the waveform. This element does not return the start time of the first sample in the Data. However, you can calculate the start time of the first sample read during a particular read operation. dt — dt returns the time interval in seconds between data points in the waveform. offset from start (samples) — offset from start (samples) specifies the number of samples by which the first sample in the Data array is offset from the first sample in the waveform. error out — error out contains error information. This output provides standard error out functionality. timed out? — timed out? returns TRUE if space in the queue did not become available before the function times out. timed out? also returns TRUE if this function encounters an error. |
| --- |
| Data reference — Data reference returns the data reference for the waveform in the read session that returned Data. t0 at start — t0 at start specifies the start time of the first sample in the waveform. This element does not return the start time of the first sample in the Data. However, you can calculate the start time of the first sample read during a particular read operation. dt — dt returns the time interval in seconds between data points in the waveform. offset from start (samples) — offset from start (samples) specifies the number of samples by which the first sample in the Data array is offset from the first sample in the waveform. |

Parent topic:

NI VeriStand - Read Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-close-multiple-waveforms-write-session-cdb-vi.html language=enus -->
## TOPIC 00186: NI VeriStand - Close Multiple Waveforms Write Session (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-close-multiple-waveforms-write-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-close-multiple-waveforms-write-session-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Multiple_Waveforms_Write_(CDB)lvclass.png Multiple Waveforms Write Session (CDB) Multiple Waveforms Write Se

### NI VeriStand - Close Multiple Waveforms Write Session (CDB) VI

Closes a waveform read or write session. Wire data to the **Single Waveform Read Session (DBL)** input to specify the instance to use.

[IMAGE alt='icon' src='ni-veristand-close-multiple-waveforms-write-session-cdb-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Write Session (CDB) — Multiple Waveforms Write Session (CDB) is a reference to the waveform session. You must open a waveform session to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Close Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-open-multiple-waveforms-write-session-cdb-vi.html language=enus -->
## TOPIC 00187: NI VeriStand - Open Multiple Waveforms Write Session (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-open-multiple-waveforms-write-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-open-multiple-waveforms-write-session-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Multiple Waveforms Write Session (CDB) VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-multiple-waveforms-write-session-cdb-vi.png']

#### Inputs/Outputs

| Communication Properties — Communication Properties contains elements that set the size of the queue used to store data the custom device reads and writes. National Instruments recommends changing these values only if you notice data loss is occurring. WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. CDB Waveform Data References — CDB Waveform Data References is an array of data references to waveforms, which you must first generate. dt — dt specifies the time interval in seconds between data points in the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Write Session (CDB) — Multiple Waveforms Write Session (CDB) returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |
| Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |

Parent topic:

NI VeriStand - Open Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-cdb-vi.html language=unavailable -->
## TOPIC 00188: Ni Veristand Start Multiple Waveforms Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-multi-t0-cdb-vi.html language=enus -->
## TOPIC 00189: NI VeriStand - Start Multiple Waveforms Multi t0 (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-multi-t0-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-multi-t0-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib

### NI VeriStand - Start Multiple Waveforms Multi t0 (CDB) VI

Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-start-multiple-waveforms-multi-t0-cdb-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Write Session (CDB) in — Multiple Waveforms Write Session (CDB) in is a reference to the waveform session. You must open a waveform session to use this parameter. t0s — t0s is an array of waveform start times to use when writing waveform data. These values are typically available from the source of the waveform data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Write Session (CDB) out — Multiple Waveforms Write Session (CDB) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Start Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-write-multiple-waveforms-cdb-vi.html language=unavailable -->
## TOPIC 00190: Ni Veristand Write Multiple Waveforms Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-write-multiple-waveforms-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-write-multiple-waveforms-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-close-multiple-waveforms-write-session-dbl-vi.html language=enus -->
## TOPIC 00191: NI VeriStand - Close Multiple Waveforms Write Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-close-multiple-waveforms-write-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-close-multiple-waveforms-write-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Multiple_Waveforms_Write_(DBL)lvclass.png Multiple Waveforms Write Session (DBL) Multiple Waveforms Write Se

### NI VeriStand - Close Multiple Waveforms Write Session (DBL) VI

Closes a waveform read or write session. Wire data to the **Single Waveform Read Session (DBL)** input to specify the instance to use.

[IMAGE alt='icon' src='ni-veristand-close-multiple-waveforms-write-session-dbl-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Write Session (DBL) — Multiple Waveforms Write Session (DBL) is a reference to the waveform session. You must open a waveform session to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Close Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-open-multiple-waveforms-write-session-dbl-vi.html language=enus -->
## TOPIC 00192: NI VeriStand - Open Multiple Waveforms Write Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-open-multiple-waveforms-write-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-open-multiple-waveforms-write-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Multiple Waveforms Write Session (DBL) VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-multiple-waveforms-write-session-dbl-vi.png']

#### Inputs/Outputs

| Communication Properties — Communication Properties contains elements that set the size of the queue used to store data the custom device reads and writes. National Instruments recommends changing these values only if you notice data loss is occurring. WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. DBL Waveform Data References — DBL Waveform Data References is an array of data references to waveforms, which you must first generate. dt — dt specifies the time interval in seconds between data points in the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Write Session (DBL) — Multiple Waveforms Write Session (DBL) returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| WPL — WPL transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |
| Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |

Parent topic:

NI VeriStand - Open Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-dbl-vi.html language=unavailable -->
## TOPIC 00193: Ni Veristand Start Multiple Waveforms Dbl Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-dbl-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-multi-t0-dbl-vi.html language=enus -->
## TOPIC 00194: NI VeriStand - Start Multiple Waveforms Multi t0 (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-multi-t0-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-multi-t0-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib

### NI VeriStand - Start Multiple Waveforms Multi t0 (DBL) VI

Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-start-multiple-waveforms-multi-t0-dbl-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Write Session (DBL) in — Multiple Waveforms Write Session (DBL) in is a reference to the waveform session. You must open a waveform session to use this parameter. t0s — t0s is an array of waveform start times to use when writing waveform data. These values are typically available from the source of the waveform data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Write Session (DBL) out — Multiple Waveforms Write Session (DBL) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Start Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-write-multiple-waveforms-dbl-vi.html language=enus -->
## TOPIC 00195: NI VeriStand - Write Multiple Waveforms (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-write-multiple-waveforms-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-write-multiple-waveforms-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again w

### NI VeriStand - Write Multiple Waveforms (DBL) VI

Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-write-multiple-waveforms-dbl-vi.png']

#### Inputs/Outputs

| Multiple Waveforms Write Session (DBL) in — Multiple Waveforms Write Session (DBL) in is a reference to the waveform session. You must open a waveform session to use this parameter. Data — Data is a 2D array of values to write to the waveforms, where each row corresponds to a waveform in the write session. Each column corresponds to a sample for each waveform. The order of the waveforms in the array corresponds to the order in which you provided the waveform data references when you opened the write session. timeout in ms (0) — timeout in ms specifies the time in milliseconds to wait for available space in the queue that transfers data to the Waveform Processing Loop (WPL) if the queue is full. The default is 0, indicating to time out immediately without sending data to the WPL. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Multiple Waveforms Write Session (DBL) out — Multiple Waveforms Write Session (DBL) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. timed out? — timed out? returns TRUE if space in the queue did not become available before the function times out. timed out? also returns TRUE if this function encounters an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Write Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-close-waveform-session-vi.html language=unavailable -->
## TOPIC 00196: Ni Veristand Close Waveform Session Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-close-waveform-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-close-waveform-session-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-open-waveform-session-vi.html language=enus -->
## TOPIC 00197: NI VeriStand - Open Waveform Session VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-open-waveform-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-open-waveform-session-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Waveform Session VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-waveform-session-vi.png']

- [NI VeriStand - Open Single Waveform Read Session (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-open-single-waveform-read-session-dbl-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Single Waveform Write Session (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-open-single-waveform-write-session-dbl-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Multiple Waveforms Read Session (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-open-multiple-waveforms-read-session-dbl-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Multiple Waveforms Write Session (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-open-multiple-waveforms-write-session-dbl-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Single Waveform Read Session (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-open-single-waveform-read-session-cdb-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Single Waveform Write Session (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-open-single-waveform-write-session-cdb-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Multiple Waveforms Read Session (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-open-multiple-waveforms-read-session-cdb-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.
- [NI VeriStand - Open Multiple Waveforms Write Session (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-open-multiple-waveforms-write-session-cdb-vi.html) Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

Parent topic:

Waveform Data

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-read-waveform-s-vi.html language=enus -->
## TOPIC 00198: NI VeriStand - Read Waveform(s) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-read-waveform-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-read-waveform-s-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a waveform(s) associated with the specified read session. icon

### NI VeriStand - Read Waveform(s) VI

Reads data from a waveform(s) associated with the specified read session.

[IMAGE alt='icon' src='ni-veristand-read-waveform-s-vi.png']

- [NI VeriStand - Read Single Waveform (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-read-single-waveform-dbl-vi.html) Reads data from a waveform(s) associated with the specified read session.
- [NI VeriStand - Read Multiple Waveforms (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-dbl/ni-veristand-read-multiple-waveforms-dbl-vi.html) Reads data from a waveform(s) associated with the specified read session.
- [NI VeriStand - Read Single Waveform (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-read-single-waveform-cdb-vi.html) Reads data from a waveform(s) associated with the specified read session.
- [NI VeriStand - Read Multiple Waveforms (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-read-cdb/ni-veristand-read-multiple-waveforms-cdb-vi.html) Reads data from a waveform(s) associated with the specified read session.

Parent topic:

Waveform Data

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-start-waveform-s-vi.html language=enus -->
## TOPIC 00199: NI VeriStand - Start Waveform(s) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-start-waveform-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-start-waveform-s-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time. icon

### NI VeriStand - Start Waveform(s) VI

Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-start-waveform-s-vi.png']

- [NI VeriStand - Start Single Waveform (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-start-single-waveform-dbl-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.
- [NI VeriStand - Start Multiple Waveforms (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-dbl-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.
- [NI VeriStand - Start Multiple Waveforms Multi t0 (DBL) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-dbl/ni-veristand-start-multiple-waveforms-multi-t0-dbl-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.
- [NI VeriStand - Start Single Waveform (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-start-single-waveform-cdb-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.
- [NI VeriStand - Start Multiple Waveforms (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-cdb-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.
- [NI VeriStand - Start Multiple Waveforms Multi t0 (CDB) VI](../../../vi-lib/ni-veristand/custom-device-waveform-api/multiple-waveforms-write-cdb/ni-veristand-start-multiple-waveforms-multi-t0-cdb-vi.html) Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.

Parent topic:

Waveform Data

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-write-waveform-s-vi.html language=unavailable -->
## TOPIC 00200: Ni Veristand Write Waveform S Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-write-waveform-s-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/ni-veristand-write-waveform-s-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-close-single-waveform-read-session-cdb-vi.html language=unavailable -->
## TOPIC 00201: Ni Veristand Close Single Waveform Read Session Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-close-single-waveform-read-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-close-single-waveform-read-session-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-open-single-waveform-read-session-cdb-vi.html language=unavailable -->
## TOPIC 00202: Ni Veristand Open Single Waveform Read Session Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-open-single-waveform-read-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-open-single-waveform-read-session-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-read-single-waveform-cdb-vi.html language=enus -->
## TOPIC 00203: NI VeriStand - Read Single Waveform (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-read-single-waveform-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-cdb/ni-veristand-read-single-waveform-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Reads data from a waveform(s) associated with the specified read session. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Single_Waveform_Read_(CDB)lvclass.png Single Waveform Read Session (CDB) in Single Waveform Read Session (CDB) in is a reference to the waveform session. You must op

### NI VeriStand - Read Single Waveform (CDB) VI

Reads data from a waveform(s) associated with the specified read session.

[IMAGE alt='icon' src='ni-veristand-read-single-waveform-cdb-vi.png']

#### Inputs/Outputs

| Single Waveform Read Session (CDB) in — Single Waveform Read Session (CDB) in is a reference to the waveform session. You must open a waveform session to use this parameter. timeout in ms (-1) — timeout in ms specifies the time in milliseconds to wait for an element to become available in the queue if the queue is empty. The default is -1, indicating never to time out. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Single Waveform Read Session (CDB) out — Single Waveform Read Session (CDB) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. Data — Data returns an array of values read from the waveform. Properties — Properties contains the following elements that describe the waveform Data this VI returns: Data reference — Data reference returns the data reference for the waveform in the read session that returned Data. t0 at start — t0 at start specifies the start time of the first sample in the waveform. This element does not return the start time of the first sample in the Data. However, you can calculate the start time of the first sample read during a particular read operation. dt — dt returns the time interval in seconds between data points in the waveform. offset from start (samples) — offset from start (samples) specifies the number of samples by which the first sample in the Data array is offset from the first sample in the waveform. error out — error out contains error information. This output provides standard error out functionality. timed out? — timed out? returns TRUE if space in the queue did not become available before the function times out. timed out? also returns TRUE if this function encounters an error. |
| --- |
| Data reference — Data reference returns the data reference for the waveform in the read session that returned Data. t0 at start — t0 at start specifies the start time of the first sample in the waveform. This element does not return the start time of the first sample in the Data. However, you can calculate the start time of the first sample read during a particular read operation. dt — dt returns the time interval in seconds between data points in the waveform. offset from start (samples) — offset from start (samples) specifies the number of samples by which the first sample in the Data array is offset from the first sample in the waveform. |

Parent topic:

NI VeriStand - Read Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-close-single-waveform-read-session-dbl-vi.html language=enus -->
## TOPIC 00204: NI VeriStand - Close Single Waveform Read Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-close-single-waveform-read-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-close-single-waveform-read-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Single_Waveform_Read_(DBL)lvclass.png Single Waveform Read Session (DBL) Single Waveform Read Session (DBL)

### NI VeriStand - Close Single Waveform Read Session (DBL) VI

Closes a waveform read or write session. Wire data to the **Single Waveform Read Session (DBL)** input to specify the instance to use.

[IMAGE alt='icon' src='ni-veristand-close-single-waveform-read-session-dbl-vi.png']

#### Inputs/Outputs

| Single Waveform Read Session (DBL) — Single Waveform Read Session (DBL) is a reference to the waveform session. You must open a waveform session to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Close Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-open-single-waveform-read-session-dbl-vi.html language=unavailable -->
## TOPIC 00205: Ni Veristand Open Single Waveform Read Session Dbl Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-open-single-waveform-read-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-open-single-waveform-read-session-dbl-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-read-single-waveform-dbl-vi.html language=unavailable -->
## TOPIC 00206: Ni Veristand Read Single Waveform Dbl Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-read-single-waveform-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-read-dbl/ni-veristand-read-single-waveform-dbl-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-close-single-waveform-write-session-cdb-vi.html language=enus -->
## TOPIC 00207: NI VeriStand - Close Single Waveform Write Session (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-close-single-waveform-write-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-close-single-waveform-write-session-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Single_Waveform_Write_(CDB)lvclass.png Single Waveform Write Session (CDB) Single Waveform Write Session (CD

### NI VeriStand - Close Single Waveform Write Session (CDB) VI

Closes a waveform read or write session. Wire data to the **Single Waveform Read Session (DBL)** input to specify the instance to use.

[IMAGE alt='icon' src='ni-veristand-close-single-waveform-write-session-cdb-vi.png']

#### Inputs/Outputs

| Single Waveform Write Session (CDB) — Single Waveform Write Session (CDB) is a reference to the waveform session. You must open a waveform session to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Close Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-open-single-waveform-write-session-cdb-vi.html language=enus -->
## TOPIC 00208: NI VeriStand - Open Single Waveform Write Session (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-open-single-waveform-write-session-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-open-single-waveform-write-session-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Single Waveform Write Session (CDB) VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-single-waveform-write-session-cdb-vi.png']

#### Inputs/Outputs

| Communication Properties — Communication Properties contains elements that set the size of the queue used to store data the custom device reads and writes. National Instruments recommends changing these values only if you notice data loss is occurring. WPL — WPL which transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. CDB Waveform Data Reference — CDB Waveform Data Reference is a data reference to a waveform, which you must first generate. dt — dt specifies the time interval in seconds between data points in the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Single Waveform Write Session (CDB) — Single Waveform Write Session (CDB) returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| WPL — WPL which transfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |
| Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |

Parent topic:

NI VeriStand - Open Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-start-single-waveform-cdb-vi.html language=unavailable -->
## TOPIC 00209: Ni Veristand Start Single Waveform Cdb Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-start-single-waveform-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-start-single-waveform-cdb-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-write-single-waveform-cdb-vi.html language=enus -->
## TOPIC 00210: NI VeriStand - Write Single Waveform (CDB) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-write-single-waveform-cdb-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-cdb/ni-veristand-write-single-waveform-cdb-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again w

### NI VeriStand - Write Single Waveform (CDB) VI

Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-write-single-waveform-cdb-vi.png']

#### Inputs/Outputs

| Single Waveform Write Session (CDB) in — Single Waveform Write Session (CDB) in is a reference to the waveform session. You must open a waveform session to use this parameter. Data — Data is an array of values to write to the waveform. timeout in ms (0) — timeout in ms specifies the time in milliseconds to wait for available space in the queue that transfers data to the Waveform Processing Loop (WPL) if the queue is full. The default is 0, indicating to time out immediately without sending data to the WPL. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Single Waveform Write Session (CDB) out — Single Waveform Write Session (CDB) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. timed out? — timed out? returns TRUE if space in the queue did not become available before the function times out. timed out? also returns TRUE if this function encounters an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Write Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-close-single-waveform-write-session-dbl-vi.html language=enus -->
## TOPIC 00211: NI VeriStand - Close Single Waveform Write Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-close-single-waveform-write-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-close-single-waveform-write-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes a waveform read or write session. Wire data to the Single Waveform Read Session (DBL) input to specify the instance to use. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib_Single_Waveform_Write_(DBL)lvclass.png Single Waveform Write Session (DBL) Single Waveform Write Session (DB

### NI VeriStand - Close Single Waveform Write Session (DBL) VI

Closes a waveform read or write session. Wire data to the **Single Waveform Read Session (DBL)** input to specify the instance to use.

[IMAGE alt='icon' src='ni-veristand-close-single-waveform-write-session-dbl-vi.png']

#### Inputs/Outputs

| Single Waveform Write Session (DBL) — Single Waveform Write Session (DBL) is a reference to the waveform session. You must open a waveform session to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. With the following exception, this input provides standard error in functionality. This node runs normally even if an error occurred before this node runs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Close Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-open-single-waveform-write-session-dbl-vi.html language=enus -->
## TOPIC 00212: NI VeriStand - Open Single Waveform Write Session (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-open-single-waveform-write-session-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-open-single-waveform-write-session-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whet

### NI VeriStand - Open Single Waveform Write Session (DBL) VI

Opens a session for reading data from or writing data to a specific waveform or waveforms associated with a custom device. You must manually select the instance to use according to the number of waveforms with which you want to interact, whether the data type of the waveforms is DBL or CDB, and whether you want to read or write waveform data.

[IMAGE alt='icon' src='ni-veristand-open-single-waveform-write-session-dbl-vi.png']

#### Inputs/Outputs

| Communication Properties — Communication Properties contains elements that set the size of the queue used to store data the custom device reads and writes. National Instruments recommends changing these values only if you notice data loss is occurring. WPL — WPLtransfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. DBL Waveform Data Reference — DBL Waveform Data Reference is a data reference to a waveform, which you must first generate. dt — dt specifies the time interval in seconds between data points in the waveform. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Single Waveform Write Session (DBL) — Single Waveform Write Session (DBL) returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| WPL — WPLtransfers the waveform data through the system. Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |
| Custom Queue Size — Custom Queue Size specifies the number of elements you want the queue to hold. Specify -1 to allow the queue to hold an unlimited number of elements. NI VeriStand uses this value only if Use Custom Queue Size? is TRUE. Otherwise, NI VeriStand automatically determines the queue size. Use Custom Queue Size? — Use Custom Queue Size? specifies whether to apply the Custom Queue Size you specify. |

Parent topic:

NI VeriStand - Open Waveform Session VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-start-single-waveform-dbl-vi.html language=enus -->
## TOPIC 00213: NI VeriStand - Start Single Waveform (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-start-single-waveform-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-start-single-waveform-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time. icon Inputs/Outputs cNI__VS_Custom_Device_Waveform_API_lvlib

### NI VeriStand - Start Single Waveform (DBL) VI

Sets the start time (t0) for the waveform data you want to write with the Write Waveform(s) VI. NI VeriStand considers all data the custom device writes to a waveform be continuous unless this VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-start-single-waveform-dbl-vi.png']

#### Inputs/Outputs

| Single Waveform Write Session (DBL) in — Single Waveform Write Session (DBL) in is a reference to the waveform session. You must open a waveform session to use this parameter. t0 — t0 is the waveform start time to use when writing waveform data. This value is typically available from the source of the waveform data. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Single Waveform Write Session (DBL) out — Single Waveform Write Session (DBL) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Start Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-write-single-waveform-dbl-vi.html language=enus -->
## TOPIC 00214: NI VeriStand - Write Single Waveform (DBL) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-write-single-waveform-dbl-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/custom-device-waveform-api/single-waveform-write-dbl/ni-veristand-write-single-waveform-dbl-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again w

### NI VeriStand - Write Single Waveform (DBL) VI

Writes an array of values to the waveform(s) associated with the specified write session. Use the Start Waveform(s) VI prior to this VI to set the waveform start time (t0) or start times. NI VeriStand considers all data this VI writes to be continuous unless the Start Waveform(s) VI executes again with a different start time.

[IMAGE alt='icon' src='ni-veristand-write-single-waveform-dbl-vi.png']

#### Inputs/Outputs

| Single Waveform Write Session (DBL) in — Single Waveform Write Session (DBL) in is a reference to the waveform session. You must open a waveform session to use this parameter. Data — Data is an array of values to write to the waveform. timeout in ms (0) — timeout in ms specifies the time in milliseconds to wait for available space in the queue that transfers data to the Waveform Processing Loop (WPL) if the queue is full. The default is 0, indicating to time out immediately without sending data to the WPL. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Single Waveform Write Session (DBL) out — Single Waveform Write Session (DBL) out returns a reference to the waveform session. Wire this reference to other Waveform Data VIs to interact with the data. timed out? — timed out? returns TRUE if space in the queue did not become available before the function times out. timed out? also returns TRUE if this function encounters an error. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Write Waveform(s) VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-close-alarm-vi.html language=enus -->
## TOPIC 00215: NI VeriStand - Close Alarm VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-close-alarm-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-close-alarm-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to an alarm. Use this VI to close each alarm reference that you open with the Open Alarm VI. icon Inputs/Outputs cgnrn.png Alarm Alarm is a reference to an alarm running on the target. You must open a reference to an alarm to use this parameter. cerrcodeclst.png error in (no

### NI VeriStand - Close Alarm VI

Closes an open reference to an alarm. Use this VI to close each alarm reference that you open with the Open Alarm VI.

[IMAGE alt='icon' src='ni-veristand-close-alarm-vi.png']

#### Inputs/Outputs

| Alarm — Alarm is a reference to an alarm running on the target. You must open a reference to an alarm to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Alarm State

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-get-alarm-data-vi.html language=unavailable -->
## TOPIC 00216: Ni Veristand Get Alarm Data Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-get-alarm-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-get-alarm-data-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-open-alarm-vi.html language=enus -->
## TOPIC 00217: NI VeriStand - Open Alarm VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-open-alarm-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-open-alarm-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to an alarm. You must open a reference before using any other VIs on this palette. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. I

### NI VeriStand - Open Alarm VI

Opens a reference to an alarm. You must open a reference before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-alarm-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. Alarm Name — Alarm Name specifies the name of the alarm to which you want to open a reference. Target Name ("": default target) — Target Name specifies the name of the target on which the alarm is running. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Alarm — Alarm is a reference to an alarm running on the target. You can wire this output to other Alarm State VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Alarm State

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-acknowledgement-status-vi.html language=unavailable -->
## TOPIC 00218: Ni Veristand Set Alarm Acknowledgement Status Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-acknowledgement-status-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-acknowledgement-status-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-data2-vi.html language=enus -->
## TOPIC 00219: NI VeriStand - Set Alarm Data

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-data2-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-data2-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets high limit, low limit, corresponding procedure name, delay duration, trip value, priority, state, mode, group number, priority number, name, and full name information about the alarm you specify. icon Inputs/Outputs cgnrn.png Alarm in Alarm in is a reference to an alarm on the target. You must

### NI VeriStand - Set Alarm Data

Sets high limit, low limit, corresponding procedure name, delay duration, trip value, priority, state, mode, group number, priority number, name, and full name information about the alarm you specify.

[IMAGE alt='icon' src='ni-veristand-set-alarm-data2-vi.png']

#### Inputs/Outputs

| Alarm in — Alarm in is a reference to an alarm on the target. You must open a reference to an alarm to use this parameter. Alarm Data — Alarm Data is a cluster containing information about the alarm you specify in the Open Alarm VI. Watch Channel — Watch Channel specifies the channel to monitor for alarm conditions. High Limit Constant — High Limit Constant specifies whether the high limit is a constant value or the value of a channel in the system. If TRUE, the high limit is the value specified by High Limit. If FALSE, the high limit is the value of the channel specified by High Limit Channel. High Limit Channel — High Limit Channel specifies the channel that determines the high limit value if High Limit Constant is FALSE. If the value of Watch Channel exceeds this limit, the alarm is triggered. High Limit — High Limit specifies the value to use for the high limit if High Limit Constant is TRUE. If the value of Watch Channel exceeds this limit, the alarm is triggered. Low Limit Constant — Low Limit Constant specifies whether the low limit is a constant value or the value of a channel in the system. If TRUE, the low limit is the value specified by Low Limit. If FALSE, the low limit is the value of the channel specified by Low Limit Channel. Low Limit Channel — Low Limit Channel specifies the channel that determines the low limit value if Low Limit Constant is FALSE. If the value of Watch Channel falls below this limit, the alarm is triggered. Low Limit — Low Limit specifies the value to use for the low limit if Low Limit Constant is TRUE. If the value of Watch Channel falls below this limit, the alarm is triggered. Procedure Name — Procedure Name specifies the procedure to initiate when an alarm occurs. Delay — Delay specifies the amount of time the Watch Channel value must be outside the alarm limits before the alarm is triggered. Trip Value — Trip Value specifies the value at which to trigger the alarm. Priority — Priority is deprecated in NI VeriStand 2011 and later. Use Priority Number instead. Setting Priority to Low, Medium, or High automatically sets Priority Number to 25, 15, and 5 respectively. 0 Low (default)—Specifies a low priority alarm. 1 Medium—Specifies a medium priority alarm. 2 High—Specifies a high priority alarm. State — State specifies the state of the alarm. 0 Disabled (default)—Specifies that the alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. 1 Enabled—Specifies that the alarm is active. The alarm trips if the channel value exceeds the high or low limits. 2 Tripped—Specifies that the alarm procedure associated with this alarm initiates when the channel value exceed the high or low limits. 3 Delayed Trip—Specifies that even when the alarm threshold is met, a specified amount of time must pass before the alarm is tripped. 4 Indicate—Specifies that the Watch Channel value is outside of the high and low limits, but the alarm was not tripped because the Mode is set to Indicate Only. Mode — Mode specifies the mode setting for the alarm. 0 Normal (default)—Specifies that the alarm trips if the channel value exceeds the high or low limits. 1 Indicate Only—Specifies that the alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. Group Number — Group Number specifies the number of the group to which the alarm belongs. Priority Number — Priority Number specifies the priority of the alarm. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. Name — Name specifies the name of the alarm. Full Name — Full Name specifies the full path to the alarm for which to set the data. You must enter the full path to the alarm, for example, Targets/Controller/Alarms/Alarm1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Alarm out — Alarm out is a reference to an alarm on the target. You can wire this output to other Alarm State VIs. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Watch Channel — Watch Channel specifies the channel to monitor for alarm conditions. High Limit Constant — High Limit Constant specifies whether the high limit is a constant value or the value of a channel in the system. If TRUE, the high limit is the value specified by High Limit. If FALSE, the high limit is the value of the channel specified by High Limit Channel. High Limit Channel — High Limit Channel specifies the channel that determines the high limit value if High Limit Constant is FALSE. If the value of Watch Channel exceeds this limit, the alarm is triggered. High Limit — High Limit specifies the value to use for the high limit if High Limit Constant is TRUE. If the value of Watch Channel exceeds this limit, the alarm is triggered. Low Limit Constant — Low Limit Constant specifies whether the low limit is a constant value or the value of a channel in the system. If TRUE, the low limit is the value specified by Low Limit. If FALSE, the low limit is the value of the channel specified by Low Limit Channel. Low Limit Channel — Low Limit Channel specifies the channel that determines the low limit value if Low Limit Constant is FALSE. If the value of Watch Channel falls below this limit, the alarm is triggered. Low Limit — Low Limit specifies the value to use for the low limit if Low Limit Constant is TRUE. If the value of Watch Channel falls below this limit, the alarm is triggered. Procedure Name — Procedure Name specifies the procedure to initiate when an alarm occurs. Delay — Delay specifies the amount of time the Watch Channel value must be outside the alarm limits before the alarm is triggered. Trip Value — Trip Value specifies the value at which to trigger the alarm. Priority — Priority is deprecated in NI VeriStand 2011 and later. Use Priority Number instead. Setting Priority to Low, Medium, or High automatically sets Priority Number to 25, 15, and 5 respectively. 0 Low (default)—Specifies a low priority alarm. 1 Medium—Specifies a medium priority alarm. 2 High—Specifies a high priority alarm. State — State specifies the state of the alarm. 0 Disabled (default)—Specifies that the alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. 1 Enabled—Specifies that the alarm is active. The alarm trips if the channel value exceeds the high or low limits. 2 Tripped—Specifies that the alarm procedure associated with this alarm initiates when the channel value exceed the high or low limits. 3 Delayed Trip—Specifies that even when the alarm threshold is met, a specified amount of time must pass before the alarm is tripped. 4 Indicate—Specifies that the Watch Channel value is outside of the high and low limits, but the alarm was not tripped because the Mode is set to Indicate Only. Mode — Mode specifies the mode setting for the alarm. 0 Normal (default)—Specifies that the alarm trips if the channel value exceeds the high or low limits. 1 Indicate Only—Specifies that the alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. Group Number — Group Number specifies the number of the group to which the alarm belongs. Priority Number — Priority Number specifies the priority of the alarm. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. Name — Name specifies the name of the alarm. Full Name — Full Name specifies the full path to the alarm for which to set the data. You must enter the full path to the alarm, for example, Targets/Controller/Alarms/Alarm1. |  |
| 0 | Low (default)—Specifies a low priority alarm. |
| 1 | Medium—Specifies a medium priority alarm. |
| 2 | High—Specifies a high priority alarm. |
| 0 | Disabled (default)—Specifies that the alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. |
| 1 | Enabled—Specifies that the alarm is active. The alarm trips if the channel value exceeds the high or low limits. |
| 2 | Tripped—Specifies that the alarm procedure associated with this alarm initiates when the channel value exceed the high or low limits. |
| 3 | Delayed Trip—Specifies that even when the alarm threshold is met, a specified amount of time must pass before the alarm is tripped. |
| 4 | Indicate—Specifies that the Watch Channel value is outside of the high and low limits, but the alarm was not tripped because the Mode is set to Indicate Only. |
| 0 | Normal (default)—Specifies that the alarm trips if the channel value exceeds the high or low limits. |
| 1 | Indicate Only—Specifies that the alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. |

Parent topic:

Alarm State

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-mode-vi.html language=unavailable -->
## TOPIC 00220: Ni Veristand Set Alarm Mode Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-mode-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-set-alarm-mode-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarm/ni-veristand-set-enabled-state-vi.html language=unavailable -->
## TOPIC 00221: Ni Veristand Set Enabled State Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarm/ni-veristand-set-enabled-state-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarm/ni-veristand-set-enabled-state-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-close-alarm-manager-reference-vi.html language=enus -->
## TOPIC 00222: NI VeriStand - Close Alarm Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-close-alarm-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-close-alarm-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the alarm manager on the VeriStand Gateway. Use this VI to close each alarm manager reference that you open with the Open Alarm Manager Reference VI. icon Inputs/Outputs cgnrn.png AlarmManager AlarmManager is a reference to the alarm manager on the VeriStand Gateway. You

### NI VeriStand - Close Alarm Manager Reference VI

Closes an open reference to the alarm manager on the VeriStand Gateway. Use this VI to close each alarm manager reference that you open with the Open Alarm Manager Reference VI.

[IMAGE alt='icon' src='ni-veristand-close-alarm-manager-reference-vi.png']

#### Inputs/Outputs

| AlarmManager — AlarmManager is a reference to the alarm manager on the VeriStand Gateway. You must open a reference to the alarm manager to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-get-alarm-list-vi.html language=enus -->
## TOPIC 00223: NI VeriStand - Get Alarm List VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-get-alarm-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-get-alarm-list-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all the alarms running on the target. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the alarms are running. cgnrn.png AlarmManager in AlarmManager in is a reference to the alarm manager on the VeriStand Gateway. You must open a reference to th

### NI VeriStand - Get Alarm List VI

Returns a list of all the alarms running on the target.

[IMAGE alt='icon' src='ni-veristand-get-alarm-list-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the alarms are running. AlarmManager in — AlarmManager in is a reference to the alarm manager on the VeriStand Gateway. You must open a reference to the alarm manager to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AlarmManager out — AlarmManager out is a reference to the alarm manager on the VeriStand Gateway. You can wire this output to other Alarms VIs. alarms — alarms returns a list of all the alarms running on the target. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-get-multiple-alarms-data-vi.html language=enus -->
## TOPIC 00224: NI VeriStand - Get Multiple Alarms Data VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-get-multiple-alarms-data-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-get-multiple-alarms-data-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns high limit, low limit, corresponding procedure name, delay duration, trip value, priority, state, mode, group number, priority number, name, and full name information about the alarms you specify. icon Inputs/Outputs cstr.png Target Target specifies the name of the target on which the alarms

### NI VeriStand - Get Multiple Alarms Data VI

Returns high limit, low limit, corresponding procedure name, delay duration, trip value, priority, state, mode, group number, priority number, name, and full name information about the alarms you specify.

[IMAGE alt='icon' src='ni-veristand-get-multiple-alarms-data-vi.png']

#### Inputs/Outputs

| Target — Target specifies the name of the target on which the alarms are running. AlarmManager in — AlarmManager in is a reference to the alarm manager on the VeriStand Gateway. You must open a reference to the alarm manager to use this parameter. Alarm Names — Alarm Names specifies the alarms whose data this VI returns. timeout (ms) — timeout (ms) specifies the time, in milliseconds, for the VI to read data from the alarm manager before returning an error. The default is 10000. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AlarmManager out — AlarmManager out is a reference to the alarm manager on the VeriStand Gateway. You can wire this output to other Alarms VIs. Alarms Data — Alarms Data is a cluster containing information about the alarms you specify in Alarm Names. Watch Channel — Watch Channel returns the channel being monitored for alarm conditions. High Limit Constant — High Limit Constant indicates whether the high limit is a constant value or the value of a channel in the system. If TRUE, the high limit is the value indicated by High Limit. If FALSE, the high limit is the value of the channel indicated by High Limit Channel. High Limit Channel — High Limit Channel indicates the channel that determines the high limit value if High Limit Constant is FALSE. If the value of Watch Channel exceeds this limit, the alarm is triggered. High Limit — High Limit indicates the value used for the high limit if High Limit Constant is TRUE. If the value of Watch Channel exceeds this limit, the alarm is triggered. Low Limit Constant — Low Limit Constant indicates whether the low limit is a constant value or the value of a channel in the system. If TRUE, the low limit is the value indicated by Low Limit. If FALSE, the low limit is the value of the channel indicated by Low Limit Channel. Low Limit Channel — Low Limit Channel indicates the channel that determines the low limit value if Low Limit Constant is FALSE. If the value of Watch Channel falls below this limit, the alarm is triggered. Low Limit — Low Limit indicates the value used for the low limit if Low Limit Constant is TRUE. If the value of Watch Channel falls below this limit, the alarm is triggered. Procedure Name — Procedure Name indicates the procedure that initiates when an alarm occurs. Delay — Delay indicates the amount of time to wait before the alarm triggers. Trip Value — Trip Value indicates the value at which the alarm last was triggered. Priority — Priority is deprecated in NI VeriStand 2011 and later. Use Priority Number instead. Setting Priority to Low, Medium, or High automatically sets Priority Number to 25, 15, and 5 respectively. 0 Low (default)—Indicates a low priority alarm. 1 Medium—Indicates a medium priority alarm. 2 High—Indicates a high priority alarm. State — State indicates the current state of the alarm. 0 Disabled (default)—Indicates that the alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. 1 Enabled—Indicates that the alarm is active. The alarm trips if the channel value exceeds the high or low limits. 2 Tripped—Indicates that the alarm procedure associated with this alarm has been initiated. 3 Delayed Trip—Indicates that when the alarm threshold is met, a specified amount of time must pass before the alarm is tripped. 4 Indicate—Indicates that the channel has returned values outside of the high and low limits, but the alarm was not tripped because the Mode is set to Indicate Only. Mode — Mode indicates the current mode setting for the alarm. 0 Normal (default)—Indicates that the alarm trips if the channel value exceeds the high or low limits. 1 Indicate Only—Indicates that the alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. Group Number — Group Number indicates the number of the group to which the alarm belongs. Priority Number — Priority Number indicates the priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. Name — Name returns the name of the alarm. Full Name — Full Name returns the full path to the alarm for which the data is set. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Watch Channel — Watch Channel returns the channel being monitored for alarm conditions. High Limit Constant — High Limit Constant indicates whether the high limit is a constant value or the value of a channel in the system. If TRUE, the high limit is the value indicated by High Limit. If FALSE, the high limit is the value of the channel indicated by High Limit Channel. High Limit Channel — High Limit Channel indicates the channel that determines the high limit value if High Limit Constant is FALSE. If the value of Watch Channel exceeds this limit, the alarm is triggered. High Limit — High Limit indicates the value used for the high limit if High Limit Constant is TRUE. If the value of Watch Channel exceeds this limit, the alarm is triggered. Low Limit Constant — Low Limit Constant indicates whether the low limit is a constant value or the value of a channel in the system. If TRUE, the low limit is the value indicated by Low Limit. If FALSE, the low limit is the value of the channel indicated by Low Limit Channel. Low Limit Channel — Low Limit Channel indicates the channel that determines the low limit value if Low Limit Constant is FALSE. If the value of Watch Channel falls below this limit, the alarm is triggered. Low Limit — Low Limit indicates the value used for the low limit if Low Limit Constant is TRUE. If the value of Watch Channel falls below this limit, the alarm is triggered. Procedure Name — Procedure Name indicates the procedure that initiates when an alarm occurs. Delay — Delay indicates the amount of time to wait before the alarm triggers. Trip Value — Trip Value indicates the value at which the alarm last was triggered. Priority — Priority is deprecated in NI VeriStand 2011 and later. Use Priority Number instead. Setting Priority to Low, Medium, or High automatically sets Priority Number to 25, 15, and 5 respectively. 0 Low (default)—Indicates a low priority alarm. 1 Medium—Indicates a medium priority alarm. 2 High—Indicates a high priority alarm. State — State indicates the current state of the alarm. 0 Disabled (default)—Indicates that the alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. 1 Enabled—Indicates that the alarm is active. The alarm trips if the channel value exceeds the high or low limits. 2 Tripped—Indicates that the alarm procedure associated with this alarm has been initiated. 3 Delayed Trip—Indicates that when the alarm threshold is met, a specified amount of time must pass before the alarm is tripped. 4 Indicate—Indicates that the channel has returned values outside of the high and low limits, but the alarm was not tripped because the Mode is set to Indicate Only. Mode — Mode indicates the current mode setting for the alarm. 0 Normal (default)—Indicates that the alarm trips if the channel value exceeds the high or low limits. 1 Indicate Only—Indicates that the alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. Group Number — Group Number indicates the number of the group to which the alarm belongs. Priority Number — Priority Number indicates the priority of the alarm running on the target. Lower numbers specify a higher alarm priority. For example, 4 is higher priority than 31. Name — Name returns the name of the alarm. Full Name — Full Name returns the full path to the alarm for which the data is set. |  |
| 0 | Low (default)—Indicates a low priority alarm. |
| 1 | Medium—Indicates a medium priority alarm. |
| 2 | High—Indicates a high priority alarm. |
| 0 | Disabled (default)—Indicates that the alarm is inactive. The alarm does not trip even if the channel value exceeds the high or low limits. |
| 1 | Enabled—Indicates that the alarm is active. The alarm trips if the channel value exceeds the high or low limits. |
| 2 | Tripped—Indicates that the alarm procedure associated with this alarm has been initiated. |
| 3 | Delayed Trip—Indicates that when the alarm threshold is met, a specified amount of time must pass before the alarm is tripped. |
| 4 | Indicate—Indicates that the channel has returned values outside of the high and low limits, but the alarm was not tripped because the Mode is set to Indicate Only. |
| 0 | Normal (default)—Indicates that the alarm trips if the channel value exceeds the high or low limits. |
| 1 | Indicate Only—Indicates that the alarm only monitors and indicates the channel value. The alarm does not trip even if the channel value exceeds the high or low limits. |

Parent topic:

Alarms

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-open-alarm-manager-reference-vi.html language=enus -->
## TOPIC 00225: NI VeriStand - Open Alarm Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-open-alarm-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/alarmmanager/ni-veristand-open-alarm-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the alarm manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot n

### NI VeriStand - Open Alarm Manager Reference VI

Opens a reference to the alarm manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-alarm-manager-reference-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. AlarmManager — AlarmManager is a reference to the alarm manager on the VeriStand Gateway. You can wire this output to other Alarms VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Alarms

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-close-calibration-reference-vi.html language=enus -->
## TOPIC 00226: NI VeriStand - Close Calibration Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-close-calibration-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-close-calibration-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the calibration tool on the VeriStand Gateway. Use this VI to close each calibration manager reference that you open with the Open Calibration Reference VI. icon Inputs/Outputs cgnrn.png Calibration Calibration is a reference to the calibration manager on the VeriStand Ga

### NI VeriStand - Close Calibration Reference VI

Closes an open reference to the calibration tool on the VeriStand Gateway. Use this VI to close each calibration manager reference that you open with the Open Calibration Reference VI.

[IMAGE alt='icon' src='ni-veristand-close-calibration-reference-vi.png']

#### Inputs/Outputs

| Calibration — Calibration is a reference to the calibration manager on the VeriStand Gateway. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-get-calibration-vi.html language=unavailable -->
## TOPIC 00227: Ni Veristand Get Calibration Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-get-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-get-calibration-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-value-vi.html language=enus -->
## TOPIC 00228: NI VeriStand - Get Raw Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the value the specified channel measures or generates before NI VeriStand applies any calibration or scaling. icon Inputs/Outputs cgnrn.png Calibration In Calibration In is a reference to the calibration manager on the VeriStand Gateway. You must open a reference to the calibration manager t

### NI VeriStand - Get Raw Value VI

Returns the value the specified channel measures or generates before NI VeriStand applies any calibration or scaling.

[IMAGE alt='icon' src='ni-veristand-get-raw-value-vi.png']

#### Inputs/Outputs

| Calibration In — Calibration In is a reference to the calibration manager on the VeriStand Gateway. You must open a reference to the calibration manager to use this parameter. Channel Name — Channel Name specifies the channel for which you want to return raw values. You must enter the full path to the channel, for example, Targets/Controller/Chassis/DAQ/Device1/Analog Input/AI0. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Calibration Out — Calibration Out is a reference to the calibration manager on the VeriStand Gateway. You can wire this output to other Calibration VIs. Value — Value returns the value the channel measures or generates before NI VeriStand applies any calibration or scaling. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-values-vi.html language=unavailable -->
## TOPIC 00229: Ni Veristand Get Raw Values Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-values-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-get-raw-values-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-open-calibration-reference-vi.html language=unavailable -->
## TOPIC 00230: Ni Veristand Open Calibration Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-open-calibration-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-open-calibration-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-remove-calibration-vi.html language=unavailable -->
## TOPIC 00231: Ni Veristand Remove Calibration Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-remove-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-remove-calibration-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/calibration/ni-veristand-set-calibration-vi.html language=enus -->
## TOPIC 00232: NI VeriStand - Set Calibration VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/calibration/ni-veristand-set-calibration-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/calibration/ni-veristand-set-calibration-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Applies a polynomial calibration to the specified channel, as defined by the Coefficients you specify. icon Inputs/Outputs cgnrn.png Calibration In Calibration In is a reference to the calibration manager on the VeriStand Gateway. You must open a reference to the calibration manager to use this para

### NI VeriStand - Set Calibration VI

Applies a polynomial calibration to the specified channel, as defined by the **Coefficients** you specify.

[IMAGE alt='icon' src='ni-veristand-set-calibration-vi.png']

#### Inputs/Outputs

| Calibration In — Calibration In is a reference to the calibration manager on the VeriStand Gateway. You must open a reference to the calibration manager to use this parameter. Channel Name — Channel Name specifies the channel to which you want to apply calibration. You must enter the full path to the channel, for example, Targets/Controller/Chassis/DAQ/Device1/Analog Input/AI0. You can calibrate FPGA and single-point DAQ channels in running system definitions, as well as custom-device channels marked as scalable. Coefficients — Coefficients is an array of coefficients that define the polynomial calibration, where each element is the coefficient for an order, and the coefficients are in ascending order. error in — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Calibration Out — Calibration Out is a reference to the calibration manager on the VeriStand Gateway. You can wire this output to other Calibration VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Calibration

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-all-faults-vi.html language=unavailable -->
## TOPIC 00233: Ni Veristand Clear All Faults Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-all-faults-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-all-faults-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-fault-vi.html language=enus -->
## TOPIC 00234: NI VeriStand - Clear Fault VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-fault-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-fault-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the fault on the specified channel. icon Inputs/Outputs cgnrn.png ChannelFault in ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. cstr.png Channel Channel specifies the channel

### NI VeriStand - Clear Fault VI

Clears the fault on the specified channel.

[IMAGE alt='icon' src='ni-veristand-clear-fault-vi.png']

#### Inputs/Outputs

| ChannelFault in — ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. Channel — Channel specifies the channel for which you want to clear a fault. You must enter the full path to the channel, for example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ChannelFault out — ChannelFault out is a reference to the channel fault manager on the VeriStand Gateway. You can wire this output to other Channel Fault VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-multiple-faults-vi.html language=enus -->
## TOPIC 00235: NI VeriStand - Clear Multiple Faults VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-multiple-faults-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-clear-multiple-faults-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Clears the fault from all specified channels. icon Inputs/Outputs cgnrn.png ChannelFault in ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. c1dstr.png Channels Channels specifies an ar

### NI VeriStand - Clear Multiple Faults VI

Clears the fault from all specified channels.

[IMAGE alt='icon' src='ni-veristand-clear-multiple-faults-vi.png']

#### Inputs/Outputs

| ChannelFault in — ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. Channels — Channels specifies an array of channels for which you want to clear a fault. You must enter the full path to the channel, for example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ChannelFault out — ChannelFault out is a reference to the channel fault manager on the VeriStand Gateway. You can wire this output to other Channel Fault VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-close-fault-manager-reference-vi.html language=enus -->
## TOPIC 00236: NI VeriStand - Close Fault Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-close-fault-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-close-fault-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to the channel fault manager on the VeriStand Gateway. Use this VI to close each channel fault manager reference that you open with the Open Fault Manager Reference VI. icon Inputs/Outputs cgnrn.png ChannelFault ChannelFault is a reference to the channel fault manager on the

### NI VeriStand - Close Fault Manager Reference VI

Closes an open reference to the channel fault manager on the VeriStand Gateway. Use this VI to close each channel fault manager reference that you open with the Open Fault Manager Reference VI.

[IMAGE alt='icon' src='ni-veristand-close-fault-manager-reference-vi.png']

#### Inputs/Outputs

| ChannelFault — ChannelFault is a reference to the channel fault manager on the VeriStand Gateway. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-get-fault-list-vi.html language=enus -->
## TOPIC 00237: NI VeriStand - Get Fault List VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-get-fault-list-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-get-fault-list-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a list of all faulted channels. You can create faulted channels manually using the Channel Fault Manager tool or programmatically using the Set Fault Value VI. icon Inputs/Outputs cgnrn.png ChannelFault in ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway.

### NI VeriStand - Get Fault List VI

Returns a list of all faulted channels. You can create faulted channels manually using the Channel Fault Manager tool or programmatically using the Set Fault Value VI.

[IMAGE alt='icon' src='ni-veristand-get-fault-list-vi.png']

#### Inputs/Outputs

| ChannelFault in — ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ChannelFault out — ChannelFault out is a reference to the channel fault manager on the VeriStand Gateway. You can wire this output to other Channel Fault VIs. Channels — Channels returns a list of all faulted channels. Values — Values returns a list of the fault values for all faulted channels. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-get-fault-value-vi.html language=enus -->
## TOPIC 00238: NI VeriStand - Get Fault Value VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-get-fault-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-get-fault-value-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fault value of the specified channel. icon Inputs/Outputs cgnrn.png ChannelFault in ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. cstr.png Channel Channel specifies the c

### NI VeriStand - Get Fault Value VI

Returns the fault value of the specified channel.

[IMAGE alt='icon' src='ni-veristand-get-fault-value-vi.png']

#### Inputs/Outputs

| ChannelFault in — ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. Channel — Channel specifies the channel for which you want to return the faulted value. You must enter the full path to the channel, for example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ChannelFault out — ChannelFault out is a reference to the channel fault manager on the VeriStand Gateway. You can wire this output to other Channel Fault VIs. Faulted — Faulted indicates whether the specified channel is faulted. A value of TRUE indicates the channel is faulted. Fault Value — Fault Value returns the fault value of the specified channel. If the specified channel is not a faulted channel, Fault Value returns 0. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-open-fault-manager-reference-vi.html language=enus -->
## TOPIC 00239: NI VeriStand - Open Fault Manager Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-open-fault-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-open-fault-manager-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Opens a reference to the channel fault manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette. icon Inputs/Outputs cstr.png Gateway IP Address ("": localhost) Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in

### NI VeriStand - Open Fault Manager Reference VI

Opens a reference to the channel fault manager on the VeriStand Gateway. You must open a reference before using any other VIs on this palette.

[IMAGE alt='icon' src='ni-veristand-open-fault-manager-reference-vi.png']

#### Inputs/Outputs

| Gateway IP Address ("": localhost) — Gateway IP Address specifies the IP address of the VeriStand Gateway. This address can be in IP dot notation or it can be a hostname. If you do not specify an address, LabVIEW establishes a connection to the local computer. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ChannelFault — ChannelFault is a reference to the channel fault manager on the VeriStand Gateway. You can wire this output to other Channel Fault VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-set-fault-value-vi.html language=unavailable -->
## TOPIC 00240: Ni Veristand Set Fault Value Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-set-fault-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-set-fault-value-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-set-multiple-faults-vi.html language=enus -->
## TOPIC 00241: NI VeriStand - Set Multiple Faults VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-set-multiple-faults-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/channelfaultmanager/ni-veristand-set-multiple-faults-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sets the fault value for all specified channels. icon Inputs/Outputs cgnrn.png ChannelFault in ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. c1dstr.png Channels Channels specifies an

### NI VeriStand - Set Multiple Faults VI

Sets the fault value for all specified channels.

[IMAGE alt='icon' src='ni-veristand-set-multiple-faults-vi.png']

#### Inputs/Outputs

| ChannelFault in — ChannelFault in is a reference to the channel fault manager on the VeriStand Gateway. You must open a reference to the channel fault manager to use this parameter. Channels — Channels specifies an array of channels for which you want to set the value. You must enter the full path to the channel, for example, Targets/Controller/Simulation Models/Models/delay_random/Inports/In1. Fault Values — Fault Values specifies the fault values of the specified array of channels. Each value in this Fault Values input corresponds to the channel in the Channels input with the same array index. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. ChannelFault out — ChannelFault out is a reference to the channel fault manager on the VeriStand Gateway. You can wire this output to other Channel Fault VIs. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Channel Fault

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/customdevice/ni-veristand-close-custom-device-reference-vi.html language=enus -->
## TOPIC 00242: NI VeriStand - Close Custom Device Reference VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/customdevice/ni-veristand-close-custom-device-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/customdevice/ni-veristand-close-custom-device-reference-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Closes an open reference to a custom device. This VI acts on references you open to send messages to a custom device, such as references the Open Custom Device Reference creates. icon Inputs/Outputs cgnrn.png Custom Device Custom Device is the reference to the custom device. Use the Open Custom Devi

### NI VeriStand - Close Custom Device Reference VI

Closes an open reference to a custom device. This VI acts on references you open to send messages to a custom device, such as references the Open Custom Device Reference creates.

[IMAGE alt='icon' src='ni-veristand-close-custom-device-reference-vi.png']

#### Inputs/Outputs

| Custom Device — Custom Device is the reference to the custom device. Use the Open Custom Device Reference VI to get this reference. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Custom Device Communication

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/customdevice/ni-veristand-open-custom-device-reference-vi.html language=unavailable -->
## TOPIC 00243: Ni Veristand Open Custom Device Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/customdevice/ni-veristand-open-custom-device-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/customdevice/ni-veristand-open-custom-device-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-byte-array-vi.html language=unavailable -->
## TOPIC 00244: Ni Veristand Send Custom Device Message Byte Array Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-byte-array-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-byte-array-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-string-vi.html language=enus -->
## TOPIC 00245: NI VeriStand - Send Custom Device Message (String) VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-string-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-string-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Sends a message or command to a custom device in an NI VeriStand project, as well as data required by the case that handles the command. You can use this VI with any custom device that registers to receive the Command you specify. icon Inputs/Outputs cgnrn.png Custom Device in Custom Device in is th

### NI VeriStand - Send Custom Device Message (String) VI

Sends a message or command to a custom device in an NI VeriStand project, as well as data required by the case that handles the command. You can use this VI with any custom device that registers to receive the **Command** you specify.

[IMAGE alt='icon' src='ni-veristand-send-custom-device-message-string-vi.png']

#### Inputs/Outputs

| Custom Device in — Custom Device in is the reference to the custom device. Use the Open Custom Device Reference VI to get this reference. Command — Command specifies the message or command to send. Data — Data specifies any data required by the case of the device's RT Driver VI that handles the Command. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Timeout ms (5000) — Timeout ms specifies the time in milliseconds that the VI waits for a response from the custom device before returning an error. The default is 5,000. Custom Device out — Custom Device out returns the reference to the custom device. Response — Response returns the response from the custom device to the Command. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

NI VeriStand - Send Custom Device Message VI

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-vi.html language=unavailable -->
## TOPIC 00246: Ni Veristand Send Custom Device Message Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/customdevice/ni-veristand-send-custom-device-message-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/close-data-logging-manager-reference-vi.html language=unavailable -->
## TOPIC 00247: Close Data Logging Manager Reference Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/close-data-logging-manager-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/close-data-logging-manager-reference-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/get-completed-log-files-vi.html language=enus -->
## TOPIC 00248: Get Completed Log Files VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/get-completed-log-files-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/get-completed-log-files-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets the paths to all the log files created during the logging session specified by Session Name in. icon Inputs/Outputs cgnrn.png Data Logging Manager Ref in Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. cstr.png Session Name in Session Name in s

### Get Completed Log Files VI

Gets the paths to all the log files created during the logging session specified by **Session Name in**.

[IMAGE alt='icon' src='get-completed-log-files-vi.png']

#### Inputs/Outputs

| Data Logging Manager Ref in — Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. Session Name in — Session Name in specifies the name of the current data logging session. You use this name to query and control logging operations during the logging session. To avoid overwriting data, use unique session names for each data logging session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Data Logging Manager Ref out — Data Logging Manager Ref out returns the reference to the data logging service. Session Name out — Session Name out returns the name of the current data logging session. Log File Paths — Log File Paths returns the paths to all log files generated during the current data logging session. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Status

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/get-current-log-file-info-vi.html language=enus -->
## TOPIC 00249: Get Current Log File Info VI

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/get-current-log-file-info-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/get-current-log-file-info-vi.html
- source_language: `enus`
- document_id: `veristand-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets information about the file to which Session Name in is currently logging data. If the session is not actively logging data to a file, Log File Path returns an empty array. icon Inputs/Outputs cgnrn.png Data Logging Manager Ref in Data Logging Manager Ref in is the reference to the data logging

### Get Current Log File Info VI

Gets information about the file to which **Session Name in** is currently logging data. If the session is not actively logging data to a file, **Log File Path** returns an empty array.

[IMAGE alt='icon' src='get-current-log-file-info-vi.png']

#### Inputs/Outputs

| Data Logging Manager Ref in — Data Logging Manager Ref in is the reference to the data logging service on the VeriStand Gateway. Session Name in — Session Name in specifies the name of the current data logging session. You use this name to query and control logging operations during the logging session. To avoid overwriting data, use unique session names for each data logging session. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Size — Size returns the size of the file, in bytes. Data Logging Manager Ref out — Data Logging Manager Ref out returns the reference to the data logging service. Session Name out — Session Name out returns the name of the current data logging session. Log File Path — Log File Path returns the path to the log file. error out — error out contains error information. This output provides standard error out functionality. Start Time — Start Time returns the start time of the log file. |
| --- |

Parent topic:

Status

<!--NI_TOPIC bundle=veristand-labview-api-ref path=vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-specification-vi.html language=unavailable -->
## TOPIC 00250: Get Data Logging Session Specification Vi

- bundle_id: `veristand-labview-api-ref`
- source_path: `vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-specification-vi.html`
- source_url: https://docs-be.ni.com/bundle/veristand-labview-api-ref/raw/resource/enus/vi-lib/ni-veristand/execution/datalogging/get-data-logging-session-specification-vi.html
- source_language: `unavailable`
- document_id: `veristand-labview-api-ref`
- page_type: ``
- content_type: ``

SOURCE STATUS: UNAVAILABLE. NI's documentation sitemap advertises this topic path, but the NI raw documentation service returned HTTP 404 for the English, German, Japanese, and Chinese locale records at corpus build time. No substitute content was fabricated.
