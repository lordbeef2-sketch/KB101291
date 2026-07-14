# NI DOCUMENT BUNDLE: rfmxinstr-labview-api-ref

<!--NI_BUNDLE_CHUNK bundle=rfmxinstr-labview-api-ref start=1 end=91 -->
<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=menus/categories/measurement/rfmx/rfinstr/dir-mnu.html language=enus -->
## TOPIC 00001: RFInstr

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/rfinstr/dir-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/rfinstr/dir-mnu.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette for configuring and fetching measurements. You can use the RFmxInstr Property Node to configure additional properties. © 2014–2026 National Instruments Corporation. All rights reserved. icon

### RFInstr

Use the VIs on this palette for configuring and fetching measurements. You can use the RFmxInstr Property Node to configure additional properties.

© 2014–2026 National Instruments Corporation. All rights reserved.

[IMAGE alt='icon' src='dir-mnu.png']

- [RFmxInstr Initialize NIRFSA VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-initialize-nirfsa-vi.html) Creates an RFmx session to the NI-RFSA supported device you specify through the Resource Name parameter, and returns an Instrument Handle Out that identifies the device in all subsequent RFmx VIs.
- [Configuration](../../../../../menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-configuration-mnu.html) Use the VIs on this palette to configure measurements. You can use the RFmxInstr Property Node to configure additional properties.
- [RFmxInstr Close VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-close-vi.html) Closes the RFmx session.
- [Utility](../../../../../menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-utility-mnu.html) Use the VIs on this palette to configure utility measurements. You can use the RFmxInstr Property Node to configure additional properties.
- [RFmxInstr Property Node VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-property-node-vi.html) Gets (reads), sets (writes), or resets (sets to default value) RFmx instrument control properties.
- [Build String](../../../../../menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-buildstring-mnu.html) Use the VI on this palette to create strings for configurations that require a selector string.
- [RFmxInstr VI Tree VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-vi-tree-vi.html) Displays all the VIs available in RFmxInstr for instrument configuration and control. The VIs are organized in the order they must be used in the program you create.
- [Calibration](../../../../../menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-calibration-mnu.html) Use the VIs on this palette to configure calibration measurements. You can use the RFmxInstr Property Node to configure additional properties.

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-buildstring-mnu.html language=enus -->
## TOPIC 00002: Build String

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-buildstring-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-buildstring-mnu.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VI on this palette to create strings for configurations that require a selector string. icon

### Build String

Use the VI on this palette to create strings for configurations that require a selector string.

[IMAGE alt='icon' src='rfmx-rfinstr-mx-buildstring-mnu.png']

- [RFmxInstr Build Calibration Plane String VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-build-calibration-plane-string-vi.html) Creates the selector string to use with external attenuation table VIs.
- [RFmxInstr Build Port String VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-build-port-string-vi.html) Creates the port string to use as the Selector String with external attenuation table VIs. On a MIMO session, this VI can be used to build port string to use as a selector string for configuring or reading port-specific properties and external attenuation table VIs.
- [RFmxInstr Build LO String VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-build-lo-string-vi.html) Creates the LO string to use as the Selector String for LO related properties.
- [RFmxInstr Build Module String VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-build-module-string-vi.html) Configures the module string to use as the Selector String for reading temperature of specific modules of the device.
- [RFmxInstr Build Instrument String VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-build-instrument-string-vi.html) Creates the instrument string to use as the Selector String for reading the recommended settings.

Parent topic:

RFInstr

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-calibration-mnu.html language=enus -->
## TOPIC 00003: Calibration

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-calibration-mnu.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-calibration-mnu.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use the VIs on this palette to configure calibration measurements. You can use the RFmxInstr Property Node to configure additional properties. icon

### Calibration

Use the VIs on this palette to configure calibration measurements. You can use the [RFmxInstr Property Node](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_property_node) to configure additional properties.

[IMAGE alt='icon' src='rfmx-rfinstr-mx-calibration-mnu.png']

- [RFmxInstr Self Calibrate VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-self-calibrate-vi.html) Self-calibrates the NI-RFSA device and associated modules that support self-calibration. If self-calibration completes successfully, the new calibration constants are stored immediately in the nonvolatile memory of the module. On a MIMO session, this VI self-calibrates all NI-RFSA devices and associated modules that support self-calibration.
- [RFmxInstr Self Calibrate Range VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-self-calibrate-range-vi.html) Self-calibrates all configurations within the specified frequency and reference level limits. If there is an open session for NI-RFSG for your device, it may remain open but cannot be used while this VI runs. NI recommends that no external signals are present on the RF In port while the calibration is taking place. For more information about Self Calibrate Range, refer to the niRFSA Self Calibrate Range VI topic for your device in the NI RF Vector Signal Analyzers Help . On a MIMO session, this VI self-calibrates all NI-RFSA devices and associated modules that support self-calibration.
- [RFmxInstr Is Self Calibrate Valid VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-is-self-calibrate-valid-vi.html) Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the Valid Steps parameter to the Steps To Omit parameter of the RFmxInstr Self Calibrate VI. On a MIMO session, use the Selector String parameter to get the self-calibration validity for a specific MIMO port.
- [Calibration Utility](../../../../../menus/categories/measurement/rfmx/rfinstr/rfmx-rfinstr-mx-calibrationutility-mnu.html) Use the VIs on this palette to configure calibration utility measurements. You can use the RFmxInstr Property Node to configure additional properties.

Parent topic:

RFInstr

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr13.html language=enus -->
## TOPIC 00004: Advanced:Phase Offset

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr13.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr13.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the offset to apply to the initial I and Q phases. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings t

### Advanced:Phase Offset

Specifies the offset to apply to the initial I and Q phases.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 0.

Valid values are -180 degrees to 180 degrees, inclusive.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Phase Offset |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr15.html language=enus -->
## TOPIC 00005: Advanced:Digitizer Dither Enabled

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr15.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr15.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether dithering is enabled on the digitizer. Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the ADC and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies of up to approximately 12 MHz

### Advanced:Digitizer Dither Enabled

Specifies whether dithering is enabled on the digitizer.

Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the ADC and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies of up to approximately 12 MHz.

**PXIe-5663/5663E/5665:** When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled.

For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When performing spectral measurements, this leakage can also appear as a wide, low-amplitude signal near the 12.5 MHz and 62.5 MHz frequencies. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT.

**PXIe-5668**: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power level with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.

|  | Note For the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Note

Enabled

The default value is **Enabled**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Digitizer Dither Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Disabled | 0 | Disables the property. |
| --- | --- | --- |
| Enabled | 1 | Enables the property. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr16.html language=enus -->
## TOPIC 00006: Advanced:FFT Width

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr16.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr16.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. The lower limit for all devices that support setting the FFT Width property is 7.325 kHz. PXIe-5663/5663E: The FFT width upper limit for the PXIe-5663/5663E depends on t

### Advanced:FFT Width

Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

The lower limit for all devices that support setting the FFT Width property is 7.325 kHz.

**PXIe-5663/5663E**: The FFT width upper limit for the PXIe-5663/5663E depends on the RF frequency and on the module revision of the PXIe-5601. For more information about determining which revision of the PXIe-5601 RF downconverter you have installed, refer to the Identifying Module Revision topic in the *NI RF Vector Signal Analyzers Help*.

Note

Note

Downconverter Center Frequency

The RFmx driver treats the device instantaneous bandwidth as the effective real-time bandwidth of the signal path. The span specifies the frequency range of the computed spectrum. A signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth. If the span you choose is greater than the device instantaneous bandwidth, the RFmx driver obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

**Supported devices**: PXIe-5663/5663E/5665, PXIe-5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | FFT Width |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr17.html language=enus -->
## TOPIC 00007: Advanced:OSP Delay Enabled

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr17.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr17.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. If you set this property to Disabled, the Reference Triggers bypass the OSP block and are processed immediately. Enabling this property requires the following e

### Advanced:OSP Delay Enabled

Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block.

If you set this property to **Disabled**, the Reference Triggers bypass the OSP block and are processed immediately.

Enabling this property requires the following equipment configurations:

- All digitizers being used must be the same model and hardware revision.
- All digitizers must use the same firmware.
- All digitizers must be configured with the same I/Q rate.
- All devices must use the same signal path.

For more information about the digitizer OSP block and Reference Triggers, refer to the following topics in the *NI High-Speed Digitizers Help*:

- PXIe-5622 Onboard Signal Processing (OSP)
- PXIe-5142 Onboard Signal Processing (OSP)
- PXIe-5622 Trigger Sources
- PXI-5142 Trigger Sources
- PXIe-5622 Block Diagram
- PXI-5142 Trigger Sources

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Enabled**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | OSP Delay Enabled |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Disabled | 0 | Disables the property. |
| --- | --- | --- |
| Enabled | 1 | Enables the property. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr18.html language=enus -->
## TOPIC 00008: Device Information:Device Temperature (deg C)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr18.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr18.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the current temperature of the module. This value is expressed in degrees Celsius. To use this property for PXIe-5830/5831/5832, you must first use the Selector string property to specify the name of the channel you are configuring. When you are reading the device temperature, you must speci

### Device Information:Device Temperature (deg C)

Returns the current temperature of the module. This value is expressed in degrees Celsius.

To use this property for PXIe-5830/5831/5832, you must first use the [Selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) property to specify the name of the channel you are configuring. When you are reading the device temperature, you must specify the context in the Selector String input as "module::<ModuleName>". You can also use the [RFmxInstr Build Module String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_module_string) VI to build the module string. For all other devices, the only valid value for the selector string is "" (empty string).

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the selector string to read this property. You can use the [RFmxInstr Build Port String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_port_string) VI to build the selector string. For PXIe-5830/5831/5832, you must specify the context in the selector string input as port::<deviceName>/<channelNumber>/module::<moduleName>.

Refer to the following table to determine which strings are valid for your configuration.

| Hardware Module | TRX Port Type | Selector String |
| --- | --- | --- |
| PXIe-3621/3622/3623 | - | if or "" (empty string) |
| PXIe-5820 | - | fpga |
| First connected mmRH-5582 | DIRECT TRX PORTS Only | rf0 |
| First connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf0switch0 |
| First connected mmRH-5582 | SWITCHED TRX PORTS [8-15] | rf0switch1 |
| Second connected mmRH-5582 | DIRECT TRX PORTS Only | rf1 |
| Second connected mmRH-5582 | SWITCHED TRX PORTS [0-7] | rf1switch0 |
| Second connected mmRH-5582 | SWITCHED TRX PORTS [8-15] | rf1switch1 |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Device Temperature (deg C) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr1b.html language=enus -->
## TOPIC 00009: Device Information:Instrument Firmware Revision

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr1b.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. On a MIMO session, use "port::<deviceName>/<channelNumber>" as the Selector string to read this property. You can use the RFmxInstr Build Port String VI to build th

### Device Information:Instrument Firmware Revision

Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property. You can use the [RFmxInstr Build Port String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_port_string) VI to build the selector string.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Instr Firmware Rev |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr1c.html language=enus -->
## TOPIC 00010: Device Information:Instrument Model

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr1c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr1c.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns a string that contains the model number or name of the RF device that you are currently using. On a MIMO session, use "port::<deviceName>/<channelNumber>" as the Selector string to read this property. You can use the RFmxInstr Build Port String VI to build the selector string. Supported devi

### Device Information:Instrument Model

Returns a string that contains the model number or name of the RF device that you are currently using.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) to read this property. You can use the [RFmxInstr Build Port String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_port_string) VI to build the selector string.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Instr Model |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr2.html language=enus -->
## TOPIC 00011: Frequency Reference:Source

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr2.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr2.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequency reference source. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Selector Strings topic for informatio

### Frequency Reference:Source

Specifies the frequency reference source.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

All other devices default value is **OnboardClock**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Freq Ref Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Frequency Reference |
| Resettable | Yes |

| OnboardClock | OnboardClock | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: The RFmx driver locks the device to its onboard clock. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860: Lock to the PXIe-5860 onboard clock. |
| --- | --- | --- |
| RefIn | RefIn | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: The RFmx driver locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. |
| PXI_Clk | PXI_Clk | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5860: The RFmx driver locks the device to the PXI backplane clock. PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842/5860: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| ClkIn | ClkIn | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840/5860 with PXIe-5653: This configuration does not apply. |
| RefIn2 | RefIn2 |  |
| PXI_ClkMaster | PXI_ClkMaster | PXIe-5831 with PXIe-5653: The RFmx driver configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: The RFmx driver configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5840 with PXIe-5653: The RFmx driver configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clk. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr23.html language=enus -->
## TOPIC 00012: Trigger:Export Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr23.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr23.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in

### Trigger:Export Output Terminal

Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646 and PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Trigger Export Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists on only PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid on only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr28.html language=enus -->
## TOPIC 00013: Recommended Settings:Number of Records

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr28.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr28.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the recommended number of records to acquire to complete measurement averaging. This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option s

### Recommended Settings:Number of Records

Returns the recommended number of records to acquire to complete measurement averaging.

Note

- RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1" , or
- RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>" . Use " instr<n> " as the selector string to read this property.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Recommended Num Records |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr30.html language=enus -->
## TOPIC 00014: Advanced:IF Filter Bandwidth (Hz)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr30.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr30.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the IF filter path bandwidth for your device configuration. Note For composite devices, such as the PXIe-5665/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device. RFmx chooses an appropriate IF filter as default IF Filter based on m

### Advanced:IF Filter Bandwidth (Hz)

Specifies the IF filter path bandwidth for your device configuration.

|  | Note For composite devices, such as the PXIe-5665/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device. |
| --- | --- |

RFmx chooses an appropriate IF filter as default IF Filter based on measurement configuration, center frequency, cleaner spectrum and downconverter preselector.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | IF Filter BW (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr31.html language=enus -->
## TOPIC 00015: Advanced:RF Highpass Filter Frequency (Hz)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr31.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr31.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly. For multispan acquisiti

### Advanced:RF Highpass Filter Frequency (Hz)

Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.

 For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this property returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 0.

The valid values range from 0 to 26.5.

**Supported devices**: PXIe-5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Highpass Filter Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr32.html language=enus -->
## TOPIC 00016: Advanced:Subspan Overlap

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr32.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr32.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Use subspan overlap process to eliminate or reduce analyzer spurs. To enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition. If a value greater than 0 is specified, then for each spectral line in the resulting spectrum, the driver acquires

### Advanced:Subspan Overlap

Use subspan overlap process to eliminate or reduce analyzer spurs. To enable this feature, specify a non-zero percentage overlap between consecutive subspans in a spectrum acquisition.

If a value greater than 0 is specified, then for each spectral line in the resulting spectrum, the driver acquires data twice with slightly different hardware settings, so that the analyzer spurs, if any, are present at different frequencies in the two acquisitions. Typically, LO frequency is shifted between the acquisitions causing analyzer spurs that are relative to the LO frequency, to move from one frequency to another. Those spurs, which are present in only one of the acquisitions for each spectral line, get removed.

The subspan overlap feature will not remove any spurs from the Device Under Test or modify the signal being measured; unlike the analyzer spurs, the spurs in the signal being measured stay at a constant frequency in the two acquisitions.

Note

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 0.

Valid values

| PXIe-5820/5830/5831/5832/5840/5841/5860 | 0 |
| --- | --- |
| PXIe-5842 | 0, 50 |
| PXIe-5665/5668 | 0 to <100 |

**Supported devices**: PXIe-5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Subspan Overlap |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr34.html language=enus -->
## TOPIC 00017: Advanced:Downconverter Gain (dB)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr34.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr34.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this property. For a vector signal analyzer (VSA), the system is defined as the RF downconverter for all interfaces between th

### Advanced:Downconverter Gain (dB)

Returns the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this property.

For a vector signal analyzer (VSA), the system is defined as the RF downconverter for all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is N/A.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Downconverter Gain (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr3c.html language=enus -->
## TOPIC 00018: LO:LO Frequency (Hz)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr3c.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz. If you are using the vector signal analyzer with an external LO, use this property to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downcon

### LO:LO Frequency (Hz)

Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz.

If you are using the vector signal analyzer with an external LO, use this property to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this property after configuring the rest of the parameters returns the LO frequency needed by the device.

You can set this property to the actual LO frequency because RFmx corrects for any difference between expected and actual LO frequencies.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_lo_string) utility function to create the LO String. For all other devices, lo channel string is not allowed.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector Strings topic for information about the string syntax.

The default value is 0.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Frequency (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4.html language=enus -->
## TOPIC 00019: RF Attenuation:Auto

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver computes the RF attenuation. If you set this property to True, the RFmx driver chooses an attenuation setting based on the reference level configured on the personality. You do not need to use a selector string if you want to configure this property for all signal i

### RF Attenuation:Auto

Specifies whether the RFmx driver computes the RF attenuation.

If you set this property to **True**, the RFmx driver chooses an attenuation setting based on the reference level configured on the personality.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **True**.

**Supported devices**: PXIe-5663/5663E, PXIe-5665/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Attenuation Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure RF Attenuation |
| Resettable | Yes |

| False | 0 | Specifies that the RFmx driver uses the value configured using RF Attenuation Value property. |
| --- | --- | --- |
| True | 1 | Specifies that the RFmx driver computes the RF attenuation. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr44.html language=enus -->
## TOPIC 00020: MIMO:LO Sharing Mode

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr44.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr44.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RFmx session with the respective LO sharing mode. The following figures illustrate different connection configuration topologies for different LO Sharing modes. You must set the Num LO Sharing Groups property to 1 for the following LO connection configurations. You must set the Num LO

### MIMO:LO Sharing Mode

Specifies the RFmx session with the respective LO sharing mode.

The following figures illustrate different connection configuration topologies for different LO Sharing modes.

You must set the [Num LO Sharing Groups](attr61.html) property to 1 for the following LO connection configurations.

[IMAGE alt='image' src='Fig1.png']
 [IMAGE alt='image' src='Fig2.png']
 [IMAGE alt='image' src='Fig9.png']

You must set the Num LO Sharing Groups property to 2 for the following LO connection configurations.

[IMAGE alt='image' src='Fig3.png']
 [IMAGE alt='image' src='Fig4.png']

The default value is **Disabled**.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Sharing Mode |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Disabled | 0 | LO Sharing is disabled. |
| --- | --- | --- |
| External Star | 3 | The LO connection configuration is configured as External Star. |
| External Daisy Chain | 4 | The LO connection configuration is configured as External Daisy Chain. |
| Splitter and Daisy Chain | 5 | The LO connection configuration is configured as Splitter and Daisy Chain. With this option, the only allowed value for the Number of LO Sharing Groups property is 1. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr46.html language=enus -->
## TOPIC 00021: Advanced:Common Mode Level (V)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr46.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr46.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. You do not need to use a sel

### Advanced:Common Mode Level (V)

Specifies the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 0.

**Supported devices**: PXIe-5820

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Common Mode Level (V) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr47.html language=enus -->
## TOPIC 00022: Advanced:SMU Resource Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr47.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr47.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be

### Advanced:SMU Resource Name

Specifies the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name.

**Supported devices:** PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SMU Resource Name |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr48.html language=enus -->
## TOPIC 00023: Advanced:SMU Channel

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr48.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr48.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the output channel to be used for noise figure (NF) measurement in RFmx. The default value is 0. Remarks The following table lists the characteristics of this property. Short Name SMU Channel Data type cstr.png Permissions Read/Write High-level VIs N/A Resettable Yes

### Advanced:SMU Channel

Specifies the output channel to be used for noise figure (NF) measurement in RFmx.

The default value is 0.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | SMU Channel |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4d.html language=enus -->
## TOPIC 00024: Advanced:Overflow Error Reporting

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4d.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want

### Advanced:Overflow Error Reporting

Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Warning**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Overflow Error Reporting |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Warning | 0 | RFmx returns a warning when an ADC or an onboard signal processing (OSP) overflow occurs. |
| --- | --- | --- |
| Disabled | 1 | RFmx does not return an error or a warning when an ADC or OSP overflow occurs. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4e.html language=enus -->
## TOPIC 00025: LO:LO In Power (dBm)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4e.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level expected at the LO IN terminal when the LO Source property is set to LO_In. This value is expressed in dBm. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector

### LO:LO In Power (dBm)

Specifies the power level expected at the LO IN terminal when the [LO Source](/csh?topicname=attr3b.html) property is set to **LO_In**. This value is expressed in dBm.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_lo_string) utility function to create the LO String. For all other devices, lo channel string is not allowed.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Note

The default value is 0.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO In Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4f.html language=enus -->
## TOPIC 00026: LO:LO Out Power (dBm)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr4f.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the power level of the signal at the LO OUT terminal when the LO Export Enabled property is set to TRUE. This value is expressed in dBm. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to us

### LO:LO Out Power (dBm)

Specifies the power level of the signal at the LO OUT terminal when the [LO Export Enabled](/csh?topicname=attr21.html) property is set to TRUE. This value is expressed in dBm.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_lo_string) utility function to create the LO String. For all other devices, lo channel string is not allowed.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 0.

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Out Power (dBm) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5.html language=enus -->
## TOPIC 00027: RF Attenuation:Value (dB)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. The RFmx driver uses the value of this property as the attenuation setting when you set the RF Attenuation Auto property to False. PXIe-5663/5663E You can chang

### RF Attenuation:Value (dB)

Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB.

The RFmx driver uses the value of this property as the attenuation setting when you set the [RF Attenuation Auto](attr4.html) property to **False**.

| PXIe-5663/5663E | You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level but decreases distortion; lower attenuation levels decrease the noise level but increases distortion. |
| --- | --- |
| PXIe-5603/5605/5665/5668 | Refer to the PXIe-5665 or the PXIe-5668 RF Attenuation and Signal Levels topic in the NI RF Vector Signal Analyzers Help for more information about configuring attenuation. |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The valid values for this property depend on the device configuration.

**Supported devices**: PXIe-5663/5663E/5603/5605/5665/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | RF Attenuation (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure RF Attenuation |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5e.html language=enus -->
## TOPIC 00028: Advanced:Thermal Correction Headroom Range (deg C)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5e.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the expected thermal operating range of the instrument from the self-calibration temperature returned from the Device Temperature property. This value is expressed in degree Celsius. For example, if this property is set to 5.0, and the device is self-calibrated at 35 degrees Celsius, then

### Advanced:Thermal Correction Headroom Range (deg C)

Specifies the expected thermal operating range of the instrument from the self-calibration temperature returned from the [Device Temperature](/csh?topicname=attr18.html) property. This value is expressed in degree Celsius.

For example, if this property is set to 5.0, and the device is self-calibrated at 35 degrees Celsius, then you can expect to run the device from 30 degrees Celsius to 40 degrees Celsius with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Default value

| PXIe-5830/5831/5832/5842/5860 | 5 |
| --- | --- |
| PXIe-5840/5841 | 10 |

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Thermal Correction Headroom Range (deg C) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5f.html language=enus -->
## TOPIC 00029: LO:LO Frequency Step Size (Hz)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr5f.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the step size for tuning the LO phase-locked loop (PLL). You can only tune the LO frequency in multiples of the LO Frequency Step Size property. Therefore, the LO frequency can be offset from the requested center frequency by as much as half of the LO Frequency Step Size property. This off

### LO:LO Frequency Step Size (Hz)

Specifies the step size for tuning the LO phase-locked loop (PLL).

You can only tune the LO frequency in multiples of the LO Frequency Step Size property. Therefore, the LO frequency can be offset from the requested center frequency by as much as half of the LO Frequency Step Size property. This offset is corrected by digitally frequency shifting the LO frequency to the value requested in [Downconverter Center Frequency](/csh?context=rfmxinstr_rfmxinstrprop_attrd) property.

Note

The valid values for this property depend on the [LO PLL Fractional Mode](attr5a.html) property.

**PXIe-5644/5645/5646:** If you set the LO PLL Fractional Mode property to **Disabled**, the specified value is coerced to the nearest valid value.

**PXIe-5840:** If you set the LO PLL Fractional Mode property to **Disabled**, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

| LO PLL Fractional Mode Enabled Property Setting | LO Frequency Step Size Property Valid Values on PXIe-5644/5645 | LO Frequency Step Size Property Valid Values on PXIe-5646 | LO Frequency Step Size Property Valid Values on PXIe-5840/5841 | LO Frequency Step Size Property Valid Values on PXIe-5830/5831/5832 | LO Frequency Step Size Property Valid Values on PXIe-5841 with PXIe-5655, PXIe-5842* |
| --- | --- | --- | --- | --- | --- |
| Enabled | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | LO1: 8 Hz to 400 MHz LO2: 4 kHz to 400 MHz | 1 nHz to 50 MHz |
| Disabled | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | LO1: -- LO2: -- | 1 nHz to 50 MHz |

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Default values

| PXIe-5644/5645/5646 | 200 kHz |
| --- | --- |
| PXIe-5830 | 2 MHz |
| PXIe-5831/5832 (RF port) | 8 MHz |
| PXIe-5831/5832 (IF port) | 2 MHz, 4 MHz |
| PXIe-5840/5841 | 500 kHz |
| PXIe-5842 | 1 Hz |

Note

RFmxInstr Get Available Ports

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Freq Step Size (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6.html language=enus -->
## TOPIC 00030: Mechanical Attenuation:Auto

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal insta

### Mechanical Attenuation:Auto

Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **True**.

**Supported devices**: PXIe-5663/5663E/5665/5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mechanical Attenuation Auto |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Mechanical Attenuation |
| Resettable | Yes |

| False | 0 | Specifies that the RFmx driver uses the value configured in the Mechanical Attenuation Value property. |
| --- | --- | --- |
| True | 1 | Specifies that the measurement computes the mechanical attenuation. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr61.html language=enus -->
## TOPIC 00031: MIMO:Number of LO Sharing Groups

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr61.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr61.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the RFmx session with the number of LO sharing groups. The default value is 1. The valid values are 1 and 2. Remarks The following table lists the characteristics of this property. Short Name Num LO Sharing Groups Data type ci32.png Permissions Read/Write High-level VIs N/A Resettable Yes

### MIMO:Number of LO Sharing Groups

Specifies the RFmx session with the number of LO sharing groups.

The default value is 1.

The valid values are 1 and 2.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Num LO Sharing Groups |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr62.html language=enus -->
## TOPIC 00032: Trigger:Start:Type

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr62.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr62.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the start trigger is a digital edge or a software trigger. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the Se

### Trigger:Start:Type

Specifies whether the start trigger is a digital edge or a software trigger.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| None | 0 | No start trigger is configured. |
| --- | --- | --- |
| Digital Edge | 1 | The start trigger is not asserted until a digital edge is detected. The source of the digital edge is specified by the Start Trigger Digital Edge Source property. |
| Software | 3 | The start trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr Send Software Edge Trigger VI. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr63.html language=enus -->
## TOPIC 00033: Trigger:Start:Digital Edge:Source

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr63.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr63.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the start trigger. This property is used only when you set the Start Trigger Type property to Digital Edge. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if yo

### Trigger:Start:Digital Edge:Source

Specifies the source terminal for the start trigger. This property is used only when you set the [Start Trigger Type](/csh?context=rfmxinstr_rfmxinstrprop_attr62) property to **Digital Edge**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value of this property is "" (empty string).

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
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
| PXI_STAR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarB | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| TimerEvent | TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |
| DIO/PFI0 | DIO/PFI0 | The trigger is received on PFI 0 of the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | The trigger is received on PFI 1 of the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | The trigger is received on PFI 2 of the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | The trigger is received on PFI 3 of the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | The trigger is received on PFI 4 of the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | The trigger is received on PFI 5 of the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | The trigger is received on PFI 6 of the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | The trigger is received on PFI 7 of the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr64.html language=enus -->
## TOPIC 00034: Trigger:Start:Digital Edge:Edge

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr64.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr64.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the active edge for the start trigger. This property is used only when you set the Start Trigger Type property to Digital Edge. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you wa

### Trigger:Start:Digital Edge:Edge

Specifies the active edge for the start trigger. This property is used only when you set the [Start Trigger Type](/csh?context=rfmxinstr_rfmxinstrprop_attr62) property to **Digital Edge**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Rising Edge**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Digital Edge |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Rising Edge | 0 | The trigger asserts on the rising edge of the signal. |
| --- | --- | --- |
| Falling Edge | 1 | The trigger asserts on the falling edge of the signal. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr65.html language=enus -->
## TOPIC 00035: Trigger:Start:Export Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr65.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr65.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the exported start trigger. You can also choose not to export any signal. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the

### Trigger:Start:Export Output Terminal

Specifies the destination terminal for the exported start trigger.

You can also choose not to export any signal.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Export Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr66.html language=enus -->
## TOPIC 00036: Trigger:Start:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr66.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr66.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/StartTrigger, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/StartTrigger, where BasebandModule is the name of your device

### Trigger:Start:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/StartTrigger , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/StartTrigger , where BasebandModule is the name of your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/StartTrigger, , where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- All other devices : /DigitizerName/StartTrigger , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Start Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr67.html language=enus -->
## TOPIC 00037: Trigger:Advance:Type

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr67.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr67.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the advance trigger is a digital edge or a software trigger. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the

### Trigger:Advance:Type

Specifies whether the advance trigger is a digital edge or a software trigger.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Type |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| None | 0 | No advance trigger is configured. |
| --- | --- | --- |
| Digital Edge | 1 | The advance trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the Advance Trigger Digital Edge Source property. |
| Software | 3 | The advance trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr Send Software Edge Trigger VI. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr68.html language=enus -->
## TOPIC 00038: Trigger:Advance:Digital Edge:Source

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr68.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr68.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the source terminal for the advance trigger. This property is used only when the Advance Trigger Type property is set to Digital Edge. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if

### Trigger:Advance:Digital Edge:Source

Specifies the source terminal for the advance trigger.

This property is used only when the [Advance Trigger Type](/csh?context=rfmxinstr_rfmxinstrprop_attr67) property is set to **Digital Edge**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value of this property is "" (empty string).

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Digital Edge Source |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
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
| PXI_STAR | PXI_STAR | The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarB | PXIe_DStarB | The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| TimerEvent | TimerEvent | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842/5860 and for digital edge advance triggers on PXIe-5663E/5665. |
| DIO/PFI0 | DIO/PFI0 | The trigger is received on PFI 0 of the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | The trigger is received on PFI 1 of the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | The trigger is received on PFI 2 of the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | The trigger is received on PFI 3 of the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | The trigger is received on PFI 4 of the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | The trigger is received on PFI 5 of the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | The trigger is received on PFI 6 of the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | The trigger is received on PFI 7 of the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr69.html language=enus -->
## TOPIC 00039: Trigger:Advance:Export Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr69.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr69.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the exported advance trigger. You can also choose not to export any signal. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in th

### Trigger:Advance:Export Output Terminal

Specifies the destination terminal for the exported advance trigger.

You can also choose not to export any signal.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Export Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6a.html language=enus -->
## TOPIC 00040: Trigger:Advance:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6a.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6a.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/AdvanceTrigger, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/AdvanceTrigger, where BasebandModule is the name of your de

### Trigger:Advance:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/AdvanceTrigger , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/AdvanceTrigger , where BasebandModule is the name of your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/AdvanceTrigger, , where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- All other devices : /DigitizerName/AdvanceTrigger , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Advance Trigger Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6b.html language=enus -->
## TOPIC 00041: Event:Ready For Start:Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6b.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Start event. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or rea

### Event:Ready For Start:Output Terminal

Specifies the destination terminal for the Ready for Start event.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Start Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6c.html language=enus -->
## TOPIC 00042: Event:Ready For Start:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6c.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6c.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForStartEvent, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForStartEvent, where BasebandModuleis the name of

### Event:Ready For Start:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/ReadyForStartEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/ReadyForStartEvent , where BasebandModule is the name of the baseband module for your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/ReadyForStartEvent , where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- All other devices : /DigitizerName/ReadyForStartEvent , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Start Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6d.html language=enus -->
## TOPIC 00043: Event:Ready For Advance:Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6d.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Advance event. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or r

### Event:Ready For Advance:Output Terminal

Specifies the destination terminal for the Ready for Advance event.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Advance Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6e.html language=enus -->
## TOPIC 00044: Event:Ready For Advance:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6e.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForAdvanceEvent, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForAdvanceEvent, where BasebandModule is the nam

### Event:Ready For Advance:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/ReadyForAdvanceEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/ReadyForAdvanceEvent , where BasebandModule is the name of your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/ReadyForAdvanceEvent , where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1)
- All other devices : /DigitizerName/ReadyForAdvanceEvent , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Advance Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6f.html language=enus -->
## TOPIC 00045: Event:Ready For Reference:Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr6f.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Ready for Reference event. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or

### Event:Ready For Reference:Output Terminal

Specifies the destination terminal for the Ready for Reference event.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Reference Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr7.html language=enus -->
## TOPIC 00046: Mechanical Attenuation:Value (dB)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr7.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr7.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. The RFmx driver uses the value of this property as the attenuation setting when you set the Mechanical Attenuation Auto property to False. You do not need to use a selector string if you want to configure t

### Mechanical Attenuation:Value (dB)

Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB.

The RFmx driver uses the value of this property as the attenuation setting when you set the [Mechanical Attenuation Auto](attr6.html) property to **False**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Valid values

| PXIe-5663/5663E | 0, 16 |
| --- | --- |
| PXIe-5665 (3.6 GHz) | 0, 10, 20, 30 |
| PXIe-5665 (14 GHz), PXIe-5668 | 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75 |

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Mechanical Attenuation (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Mechanical Attenuation |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr70.html language=enus -->
## TOPIC 00047: Event:Ready For Reference:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr70.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr70.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/ReadyForReferenceEvent, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/ReadyForReferenceEvent, where BasebandModule is the

### Event:Ready For Reference:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/ReadyForReferenceEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/ReadyForReferenceEvent , where BasebandModule is the name of your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/ReadyForReferenceEvent , where BasebandModule is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- All other devices : /DigitizerName/ReadyForReferenceEvent , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Ready For Reference Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr71.html language=enus -->
## TOPIC 00048: Event:End Of Record:Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr71.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr71.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the End of Record event. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read

### Event:End Of Record:Output Terminal

Specifies the destination terminal for the End of Record event.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | End Of Record Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr72.html language=enus -->
## TOPIC 00049: Event:End Of Record:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr72.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr72.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/EndOfRecordEvent, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/EndOfRecordEvent, where BasebandModule is the name of you

### Event:End Of Record:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/EndOfRecordEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/EndOfRecordEvent , where BasebandModule is the name of your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/EndOfRecordEvent , where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- All other devices : /DigitizerName/EndOfRecordEvent , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | End Of Record Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr73.html language=enus -->
## TOPIC 00050: Event:Done:Output Terminal

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr73.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr73.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the destination terminal for the Done event. This property is not supported on a MIMO session. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that sign

### Event:Done:Output Terminal

Specifies the destination terminal for the Done event.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Output Terminal |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Do not export signal |  | Does not export the signal. |
| --- | --- | --- |
| ClkOut | ClkOut | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut | RefOut | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut2 | RefOut2 | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 | PFI0 | Exports the signal to the PFI 0 connector. For the PXIe-5841 with PXIe-5655, the signal is exported to the PXIe-5841 PFI 0. |
| PFI1 | PFI1 | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 | PXI_Trig0 | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 | PXI_Trig1 | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 | PXI_Trig2 | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 | PXI_Trig3 | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 | PXI_Trig4 | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 | PXI_Trig5 | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 | PXI_Trig6 | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 | PXI_Trig7 | Exports the signal to the PXI trigger line 7. |
| PXI_STAR | PXI_STAR | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC | PXIe_DStarC | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| DIO/PFI0 | DIO/PFI0 | Exports the signal to the PFI 0 on the DIO front panel connector. |
| DIO/PFI1 | DIO/PFI1 | Exports the signal to the PFI 1 on the DIO front panel connector. |
| DIO/PFI2 | DIO/PFI2 | Exports the signal to the PFI 2 on the DIO front panel connector. |
| DIO/PFI3 | DIO/PFI3 | Exports the signal to the PFI 3 on the DIO front panel connector. |
| DIO/PFI4 | DIO/PFI4 | Exports the signal to the PFI 4 on the DIO front panel connector. |
| DIO/PFI5 | DIO/PFI5 | Exports the signal to the PFI 5 on the DIO front panel connector. |
| DIO/PFI6 | DIO/PFI6 | Exports the signal to the PFI 6 on the DIO front panel connector. |
| DIO/PFI7 | DIO/PFI7 | Exports the signal to the PFI 7 on the DIO front panel connector. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr74.html language=enus -->
## TOPIC 00051: Event:Done:Terminal Name

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr74.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr74.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the fully qualified signal name as a string. The standard format is as follows: PXIe-5820/5840/5841/5842: /ModuleName/ai/0/DoneEvent, where ModuleName is the name of your device in MAX. PXIe-5830/5831/5832: /BasebandModule/ai/0/DoneEvent, where BasebandModule is the name of your device in MA

### Event:Done:Terminal Name

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/DoneEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/DoneEvent , where BasebandModule is the name of your device in MAX.
- PXIe-5860 : /ModuleName/ai/ChannelNumber/DoneEvent , where ModuleName is the name of your device in MAX and ChannelNumber is the channel number (0 or 1).
- All other devices : /DigitizerName/DoneEvent , where DigitizerName is the name of your associated digitizer module in MAX.

Note

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Done Event Terminal Name |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr75.html language=enus -->
## TOPIC 00052: Advanced:Self Calibration:Self Cal Validity Check

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr75.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr75.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies whether the RFmx driver validates the self-calibration data. You can specify the time interval required to perform the check using the Self Cal Validity Check Time Interval property. NI recommends to perform self-calibration using the RFmxInstr Self Calibrate VI when RFmx reports an invali

### Advanced:Self Calibration:Self Cal Validity Check

Specifies whether the RFmx driver validates the self-calibration data.

You can specify the time interval required to perform the check using the [Self Cal Validity Check Time Interval](/csh?context=rfmxinstr_rfmxinstrprop_attr76) property.

NI recommends to perform self-calibration using the [RFmxInstr Self Calibrate](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_self_calibrate) VI when RFmx reports an invalid self-calibration data warning.

Note

The default value is **Off**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5833/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Self Cal Validity Check |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Off | 0 | Indicates that RFmx does not check whether device self-calibration data is valid. |
| --- | --- | --- |
| Enabled | 1 | Indicates that RFmx checks whether device self-calibration data is valid and reports a warning from the RFmx Commit and RFmx Initiate VIs when the data is invalid. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr76.html language=enus -->
## TOPIC 00053: Advanced:Self Calibration:Self Cal Validity Check Time Interval (s)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr76.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr76.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds. When you call RFmx Commit or Initiate VIs by enabling the Self Cal Validity Check property, the RFmx driver checks if the amount of time specified by the Self Calibration Validity Check Time

### Advanced:Self Calibration:Self Cal Validity Check Time Interval (s)

Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds.

When you call RFmx Commit or Initiate VIs by enabling the [Self Cal Validity Check](/csh?context=rfmxinstr_rfmxinstrprop_attr75) property, the RFmx driver checks if the amount of time specified by the Self Calibration Validity Check Time Interval property has elapsed before validating the calibration data.

The default value is 30 seconds.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5833/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Self Cal Validity Check Time Interval (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr77.html language=enus -->
## TOPIC 00054: Advanced:Temperature Read Interval (s)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr77.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr77.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds. When you call the RFmx Initiate VI, RFmx checks if the amount of time specified by this property has elapsed before reading the hardware temperature. RFmx ignores Temperature Read Interval

### Advanced:Temperature Read Interval (s)

Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds.

When you call the RFmx Initiate VI, RFmx checks if the amount of time specified by this property has elapsed before reading the hardware temperature.

Note

Downconverter Gain

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 30 seconds.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Temperature Read Interval (s) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr78.html language=enus -->
## TOPIC 00055: Advanced:Thermal Correction Temperature Resolution (deg C)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr78.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr78.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal

### Advanced:Thermal Correction Temperature Resolution (deg C)

Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Default value

| PXIe-5830/5831/5832/5842/5860 | 0.2 |
| --- | --- |
| PXIe-5840/5841 | 1.0 |

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Thermal Correction Temperature Resolution (deg C) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr8.html language=enus -->
## TOPIC 00056: LO:Tuning Speed

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr8.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Makes tradeoffs between tuning speed and phase noise. This property is not supported if you are using an external LO. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "l

### LO:Tuning Speed

Makes tradeoffs between tuning speed and phase noise.

Note

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_build_lo_string) utility function to create the LO String. For all other devices, lo channel string is not allowed.

Note

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

Note

Medium

**Default value**: **Normal** for PXIe-5663/5663E/5665/5668, **Medium** for PXIe-5644/5645/5646 and PXIe-5830/5831/5832/5840/5841/5842

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Tuning Speed |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| Normal | 0 | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an underdamped response. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a narrow loop bandwidth. |
| --- | --- | --- |
| Medium | 1 | Specifies that the RF downconverter module uses a medium loop bandwidth. This value is not supported on PXIe-5663/5663E/5665/5668 devices. |
| Fast | 2 | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an overdamped response. Setting this property to Fast allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a wide loop bandwidth. |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr80.html language=enus -->
## TOPIC 00057: Advanced:Number of Raw IQ Records

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr80.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr80.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the number of raw IQ records to acquire to complete measurement averaging. This property returns a value of 0 when RFmx cannot provide I/Q data for the specified measurement configuration. Remarks The following table lists the characteristics of this property. Short Name Num Raw IQ Records D

### Advanced:Number of Raw IQ Records

Returns the number of raw IQ records to acquire to complete measurement averaging.

Note

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Num Raw IQ Records |
| --- | --- |
| Data type |  |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attr9.html language=enus -->
## TOPIC 00058: Advanced:Frequency Settling Units

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attr9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attr9.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the delay duration units and interpretation for LO settling. Specify the actual settling value using the Frequency Settling property. Note The Frequency Settling Units property is not supported if you are using an external LO. You do not need to use a selector string if you want to configu

### Advanced:Frequency Settling Units

Specifies the delay duration units and interpretation for LO settling.

Specify the actual settling value using the [Frequency Settling](attra.html) property.

|  | Note The Frequency Settling Units property is not supported if you are using an external LO. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is **PPM**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Freq Settling Units |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

| PPM | 0 | Specifies the frequency settling in parts per million (ppm). |
| --- | --- | --- |
| Seconds After Lock | 1 | Specifies the frequency settling in time after lock (seconds). |
| Seconds After I/O | 2 | Specifies the frequency settling in time after I/O (seconds). |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attra.html language=enus -->
## TOPIC 00059: Advanced:Frequency Settling

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attra.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attra.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the value used for LO frequency settling. Specify the units and interpretation for this scalar value using the Frequency Settling Units property. Valid values Frequency Settling Units Property Value PXIe-5663/5663E PXIe-5665/5668 PXIe-5644/5645/5646 PXIe-5830/5831/5832/5840/5841/5842, PXIe

### Advanced:Frequency Settling

Specifies the value used for LO frequency settling.

Specify the units and interpretation for this scalar value using the [Frequency Settling Units](attr9.html) property.

**Valid values**

| Frequency Settling Units Property Value | PXIe-5663/5663E | PXIe-5665/5668 | PXIe-5644/5645/5646 | PXIe-5830/5831/5832/5840/5841/5842, PXIe-5831 with PXIe-5653 (using PXIe-3622 LO), PXIe-5832 with PXIe-5653 (using PXIe-3623 LO) | PXIe-5831 with PXIe-5653 (using PXIe-5653 LO) and PXIe-5832 with PXIe-5653 (using PXIe-5653 LO) |
| --- | --- | --- | --- | --- | --- |
| Seconds After Lock | 2 µs to 80 ms, resolution of approximately 2 µs | 4 µs to 80 ms, resolution of approximately 4 µs | 1 µs to 65 ms, resolution of 1 µs | 1 µs to 10s, resolution of 1 µs | 4 µs to 80 ms, resolution of approximately 4 µs |
| Seconds After I/O | 0 µs to 80 ms, resolution of 1 µs | 0 µs to 80 ms, resolution of 1 µs | 1 µs to 65 ms, resolution of 1 µs | 0 µs to 10s, resolution of 1 µs | 0 µs to 80 ms, resolution of 1 µs |
| PPM | 1.0, 0.1, 0.01 | 1.0, 0.1, 0.01, 0.001 | 1.0, 0.1, 0.01 | 1.0 to 0.01 | 1.0 to 0.01 |

|  | Note This property is not supported if you are using an external LO. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax.

The default value is 0.1.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Freq Settling |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attra3.html language=enus -->
## TOPIC 00060: Load Configurations: Load Options

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attra3.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attra3.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the configurations to skip while loading from a file using the RFmxInstr Load Configurations VI . Skip None (0) RFmx loads all the configurations to the session. Skip RFInstr (1) RFmx skips loading the RFmxInstr configurations to the session The default value is an empty array. Remarks The

### Load Configurations: Load Options

Specifies the configurations to skip while loading from a file using the [RFmxInstr Load Configurations](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_load_configurations)VI .

| Skip None (0) | RFmx loads all the configurations to the session. |
| --- | --- |
| Skip RFInstr (1) | RFmx skips loading the RFmxInstr configurations to the session |

The default value is an empty array.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | Load Options |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attrb8.html language=enus -->
## TOPIC 00061: MIMO:LO Splitter:Loss:Frequency (Hz)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attrb8.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attrb8.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies the frequencies corresponding to the insertion loss inherent to the RF Splitter, as specified by the LO Splitter Loss property. This value is expressed in Hz. You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the Selector

### MIMO:LO Splitter:Loss:Frequency (Hz)

Specifies the frequencies corresponding to the insertion loss inherent to the RF Splitter, as specified by the [LO Splitter Loss](/csh?topicname=attrb8.html) property. This value is expressed in Hz.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is an empty array.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Splitter Loss Freq (Hz) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=resource/objmgr/rfmxinstr-rc/rfmxinstr/attrb9.html language=enus -->
## TOPIC 00062: MIMO:LO Splitter:Loss:Loss (dB)

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `resource/objmgr/rfmxinstr-rc/rfmxinstr/attrb9.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/resource/objmgr/rfmxinstr-rc/rfmxinstr/attrb9.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Specifies an array of the insertion losses inherent to the RF Splitter. This value is expressed in dB. You must specify the frequencies at which the losses were measured using the LO Splitter Loss Freq property. You do not need to use a selector string to configure or read this property for the defa

### MIMO:LO Splitter:Loss:Loss (dB)

Specifies an array of the insertion losses inherent to the RF Splitter. This value is expressed in dB.

You must specify the frequencies at which the losses were measured using the [LO Splitter Loss Freq](attrb9.html) property.

You do not need to use a selector string to configure or read this property for the default signal instance. Refer to the [Selector Strings](/csh?context=rfmxspecan_rfmxspecan_selector_string) topic for information about the string syntax for named signals.

The default value is an empty array.

#### Remarks

The following table lists the [characteristics](/csh?productcategories=147794&context=lvcore_lvprop_flags) of this property.

| Short Name | LO Splitter Loss (dB) |
| --- | --- |
| Data type |  |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

Parent topic:

RFmxInstr Properties

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-nearest-vi.html language=enus -->
## TOPIC 00063: RFmxInstr Configure External Attenuation Interpolation (Nearest) VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-nearest-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-nearest-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used. Currently interpolation is supported only for S-parameter tables. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644

### RFmxInstr Configure External Attenuation Interpolation (Nearest) VI

Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used.

Note

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-configure-external-attenuation-interpolation-nearest-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Table Name — Table Name specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxInstr Configure External Attenuation Interpolation VI

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-spline-vi.html language=enus -->
## TOPIC 00064: RFmxInstr Configure External Attenuation Interpolation (Spline) VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-spline-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-spline-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this VI performs a spline interpolation based on the entries above and below the row in the table. Currently interpolation is support

### RFmxInstr Configure External Attenuation Interpolation (Spline) VI

Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this VI performs a spline interpolation based on the entries above and below the row in the table.

Note

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-configure-external-attenuation-interpolation-spline-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Table Name — Table Name specifies the name to be associated with either the S-parameter table or the external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFmxInstr Configure External Attenuation Interpolation VI

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-vi.html language=enus -->
## TOPIC 00065: RFmxInstr Configure External Attenuation Interpolation VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the external attenuation interpolation technique when interpolating S-parameters for the specified table. icon

### RFmxInstr Configure External Attenuation Interpolation VI

Configures the external attenuation interpolation technique when interpolating S-parameters for the specified table.

[IMAGE alt='icon' src='rfmxinstr-configure-external-attenuation-interpolation-vi.png']

- [RFmxInstr Configure External Attenuation Interpolation (Nearest) VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-nearest-vi.html) Selects the nearest interpolation method when interpolating S-parameters for a specified table. The parameters of the table nearest to the carrier frequency are used.
- [RFmxInstr Configure External Attenuation Interpolation (Linear) VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-linear-vi.html) Selects the linear interpolation method when interpolating S-parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this VI performs a linear interpolation based on the entries above and below the row in the table.
- [RFmxInstr Configure External Attenuation Interpolation (Spline) VI](../../../../../vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-interpolation-spline-vi.html) Selects the spline interpolation method when interpolating parameters for the specified table. If the carrier frequency does not match a row in the S-parameter table, this VI performs a spline interpolation based on the entries above and below the row in the table.

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-table-vi.html language=enus -->
## TOPIC 00066: RFmxInstr Configure External Attenuation Table VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-external-attenuation-table-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the external attenuation table in the calibration plane specified by the Selector String parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane. If there is only one table configured in any calibration plane, it is automati

### RFmxInstr Configure External Attenuation Table VI

Stores the external attenuation table in the calibration plane specified by the **Selector String** parameter. On a MIMO session, the external attenuation table is stored for each MIMO port in the specified calibration plane.

If there is only one table configured in any calibration plane, it is automatically selected as the active table.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-configure-external-attenuation-table-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session if you do not specify the port name, this configuration is applied to all MIMO ports in the session for the default calibration plane instance. To configure external attenuation table for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Table Name — Table Name specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" Frequency (Hz) — Frequency specifies an array of frequencies in the external attenuation table. This value is expressed in Hz. External Attenuation (dB) — External Attenuation specifies an array of attenuations corresponding to the frequency specified by the Frequency parameter. This value is expressed in dB. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-frequency-reference-vi.html language=enus -->
## TOPIC 00067: RFmxInstr Configure Frequency Reference VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-frequency-reference-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-configure-frequency-reference-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Configures the Reference Clock and the frequency reference source. icon Inputs/Outputs cstr.png Selector String Selector String specifies a Selector String comprising of the signal name. You do not need to use a selector string, if you want to configure this parameter for all signal instances. Examp

### RFmxInstr Configure Frequency Reference VI

Configures the Reference Clock and the frequency reference source.

[IMAGE alt='icon' src='rfmxinstr-configure-frequency-reference-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a Selector String comprising of the signal name. You do not need to use a selector string, if you want to configure this parameter for all signal instances. Example: "signal::sig1" You can use the personality specific Build String VI to build the selector string. Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Frequency Reference Source — Frequency Reference Source specifies the frequency reference source. The default value for PXIe-5840 with PXIe-5653 is RefIn2, else the default value is OnboardClock. OnboardClock (OnboardClock) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the PXIe-5860 onboard clock RefIn (RefIn) PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. PXI_Clk (PXI_Clk) PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842: Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the PXI backplane clock. ClkIn (ClkIn) PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. RefIn2 (RefIn2) Configure open NI-RFSG sessions to the device to use RefIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. PXI_ClkMaster (PXI_ClkMaster) PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. Frequency (Hz) — Frequency specifies the Reference Clock rate when the Frequency Reference Source parameter is set to ClkIn or RefIn. This value is expressed in Hz. The default value is 10 MHz. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| OnboardClock (OnboardClock) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: RFmx locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842/5860: RFmx locks the device to its onboard clock. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the PXIe-5860 onboard clock |
| RefIn (RefIn) | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: RFmx locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5860:Lock to the signal at the REF IN connector on the PXIe-5860. |
| PXI_Clk (PXI_Clk) | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5830/5831/5832/5841 with PXIe-5655/5842: Lock LO module to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841/5842/5860: RFmx locks the device to the PXI backplane clock. |
| ClkIn (ClkIn) | PXIe-5663/5663E: RFmx locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: RFmx locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. |
| RefIn2 (RefIn2) | Configure open NI-RFSG sessions to the device to use RefIn for the PXIe-5840 or OnboardClock for the PXIe-5840 with PXIe-5653. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, and PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5860: This configuration does not apply. |
| PXI_ClkMaster (PXI_ClkMaster) | PXIe-5831 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: RFmx configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842/5860: This configuration does not apply. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-delete-all-external-attenuation-tables-vi.html language=enus -->
## TOPIC 00068: RFmxInstr Delete All External Attenuation Tables VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-delete-all-external-attenuation-tables-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-delete-all-external-attenuation-tables-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all the external attenuation tables in the calibration plane specified by the Selector String parameter. On a MIMO session, this VI deletes all the external attenuation tables for the specified MIMO port. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-583

### RFmxInstr Delete All External Attenuation Tables VI

Deletes all the external attenuation tables in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this VI deletes all the external attenuation tables for the specified MIMO port.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-delete-all-external-attenuation-tables-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If you specify "calplane::all", all the calibration planes are deleted. On a MIMO session, the default "" (empty string) deletes all the external attenuation tables for all MIMO Ports. To delete an external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::all" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::all/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-disable-calibration-plane-vi.html language=enus -->
## TOPIC 00069: RFmxInstr Disable Calibration Plane VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-disable-calibration-plane-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-disable-calibration-plane-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Disables the calibration plane specified by the Selector String parameter for amplitude correction. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png Selector String Selector String specifies the calibr

### RFmxInstr Disable Calibration Plane VI

Disables the calibration plane specified by the **Selector String** parameter for amplitude correction.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-disable-calibration-plane-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If you specify "calplane::all", all the calibration planes are disabled. Example: "" "calplane::plane0" "calplane::all" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-enable-calibration-plane-vi.html language=enus -->
## TOPIC 00070: RFmxInstr Enable Calibration Plane VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-enable-calibration-plane-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-enable-calibration-plane-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Enables the calibration plane specified by the Selector String parameter for amplitude correction. Supported devices: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860 icon Inputs/Outputs cstr.png Selector String Selector String specifies the calibra

### RFmxInstr Enable Calibration Plane VI

Enables the calibration plane specified by the **Selector String** parameter for amplitude correction.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-enable-calibration-plane-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which the external attenuation table or S-parameter is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). If "calplane::all" is specified, all the calibration planes are enabled. Example: "" "calplane::plane0" "calplane::all" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-export-signal-vi.html language=enus -->
## TOPIC 00071: RFmxInstr Export Signal VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-export-signal-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-export-signal-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Routes signals (triggers, clocks, and events) to the specified output terminal. This VI is not supported on a MIMO session. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initiali

### RFmxInstr Export Signal VI

Routes signals (triggers, clocks, and events) to the specified output terminal.

Note

[IMAGE alt='icon' src='rfmxinstr-export-signal-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Export Signal Source — Export Signal Source controls the source to export signals. Start Trigger (0) Start trigger is sourced. Ref Trigger (1) Reference trigger is sourced. Advance Trigger (2) Advance trigger is sourced. Ready for Start Event (3) Ready for Start event is sourced. Ready for Advance Event (4) Ready for Advance event is sourced. Ready for Ref Event (5) Ready for Reference event is sourced. End of Record Event (6) End of Record event is sourced. Done Event (7) Done event is sourced. Reference Clock (8) Reference clock is sourced. Export Signal Output Terminal — Export Signal Output Terminal specifies the terminal where the signal is exported. You can also choose not to export any signal. The default value is "" (empty string). Do not export signal (()) The signal is not exported. ClkOut (ClkOut) Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RefOut (RefOut) The signal is exported to the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. RefOut2 (RefOut2) The signal is exported to the REF OUT2 terminal on the LO. This connector exists only on some versions of the PXIe-5652. PFI0 (PFI0) The signal is exported to the PFI 0 connector on the PXIe-5142 and PXIe-5624. PFI1 (PFI1) The signal is exported to the PFI 1 connector on the PXIe-5142 and PXIe-5622. PXI_Trig0 (PXI_Trig0) The signal is exported to the PXI trigger line 0. PXI_Trig1 (PXI_Trig1) The signal is exported to the PXI trigger line 1. PXI_Trig2 (PXI_Trig2) The signal is exported to the PXI trigger line 2. PXI_Trig3 (PXI_Trig3) The signal is exported to the PXI trigger line 3. PXI_Trig4 (PXI_Trig4) The signal is exported to the PXI trigger line 4. PXI_Trig5 (PXI_Trig5) The signal is exported to the PXI trigger line 5. PXI_Trig6 (PXI_Trig6) The signal is exported to the PXI trigger line 6. PXIe_DStarC (PXIe_DStarC) The signal is exported to the PXI DStar C trigger line. This value is valid only on PXIe-5820/5830/5831/5832/5840/5841/5842/5860. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Start Trigger (0) | Start trigger is sourced. |
| Ref Trigger (1) | Reference trigger is sourced. |
| Advance Trigger (2) | Advance trigger is sourced. |
| Ready for Start Event (3) | Ready for Start event is sourced. |
| Ready for Advance Event (4) | Ready for Advance event is sourced. |
| Ready for Ref Event (5) | Ready for Reference event is sourced. |
| End of Record Event (6) | End of Record event is sourced. |
| Done Event (7) | Done event is sourced. |
| Reference Clock (8) | Reference clock is sourced. |
| Do not export signal (()) | The signal is not exported. |
| ClkOut (ClkOut) | Export the Reference Clock on the CLK OUT terminal on the digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
| RefOut (RefOut) | The signal is exported to the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |
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
| PXIe_DStarC (PXIe_DStarC) | The signal is exported to the PXI DStar C trigger line. This value is valid only on PXIe-5820/5830/5831/5832/5840/5841/5842/5860. |

Parent topic:

Configuration

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-fetch-raw-iq-1rec-vi.html language=enus -->
## TOPIC 00072: RFmxInstr Fetch Raw IQ (1Rec) VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-fetch-raw-iq-1rec-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-fetch-raw-iq-1rec-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Fetches I/Q data from a single record in an acquisition. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. cdbl.pn

### RFmxInstr Fetch Raw IQ (1Rec) VI

Fetches I/Q data from a single record in an acquisition.

[IMAGE alt='icon' src='rfmxinstr-fetch-raw-iq-1rec-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout (s)specifies the timeout, in seconds, for fetching the raw IQ data. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies the VI immediately returns available data. The default value is 10. Record to Fetch — Record to Fetch specifies the record to retrieve. Record numbers are zero-based. The default value is 0. Samples to Read — Samples to Read specifies the number of samples to fetch. A value of -1 specifies that RFmx fetches all samples. The default value is -1. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. IQ Data — IQ Data returns the acquired data as a cluster. t0 — t0 returns the start time of the first sample. The timestamp corresponds to the difference, in seconds, between the returned first sample and the reference trigger location. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. Y — Y returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I 2 + Q 2) / 2R, where R is the input impedance in ohms. For RFmx, R = 50 ohms. error out — error out contains error information. This output provides standard error out functionality. |
| --- |
| t0 — t0 returns the start time of the first sample. The timestamp corresponds to the difference, in seconds, between the returned first sample and the reference trigger location. dt — dt returns the time interval between data points in the acquired signal. The I/Q data sample rate is the reciprocal of this value. Y — Y returns the complex-value time domain data array. The real and imaginary parts of this complex data array correspond to the in-phase (I) and quadrature-phase (Q) data, respectively. To calculate the instantaneous power of a sampled I/Q point, use the equation (I 2 + Q 2) / 2R, where R is the input impedance in ohms. For RFmx, R = 50 ohms. |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-external-attenuation-table-actual-value-vi.html language=enus -->
## TOPIC 00073: RFmxInstr Get External Attenuation Table Actual Value VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-external-attenuation-table-actual-value-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-external-attenuation-table-actual-value-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane. On a MIMO session, this VI returns the external attenuation table actual value for a specified port. You can use the Selector String parameter to specify the name of

### RFmxInstr Get External Attenuation Table Actual Value VI

Returns the external attenuation table actual value that is applied to the measurements for a specified signal and calibration plane.

On a MIMO session, this VI returns the external attenuation table actual value for a specified port. You can use the **Selector String** parameter to specify the name of the signal, calibration plane, and MIMO port to return the external attenuation table actual value.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-get-external-attenuation-table-actual-value-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a Selector String comprising of the signal name and calibration plane name. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, you must use "port::<deviceName>/<channelNumber>" as part of the selector string to read the external attenuation table actual value for the specified port. If you do not specify the signal name, the value is returned for the last committed signal instance. Example: "" "signal::sig1" "calplane::plane0" "signal::sig1/calplane::plane0" "port::rfsa1/0" "signal::sig1/port::rfsa1/0" "calplane::plane0/port::rfsa1/0" "signal::sig1/calplane::plane0/port::rfsa1/0" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. External Attenuation (dB) — External Attenuation returns the external attenuation table actual value applied to the measurements for a specified signal and calibration plane. This further includes interpolation of the external attenuation table based on the specified signal. On a MIMO session, this value corresponds to a specified port. This value is expressed in dB. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-list-names-vi.html language=enus -->
## TOPIC 00074: RFmxInstr Get List Names VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-list-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-list-names-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the list names and the corresponding selected personality type from the Personality Filter parameter. When you set the Personality Filter parameter to All, this VI returns the available list names for all supported personalities. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In In

### RFmxInstr Get List Names VI

Returns the list names and the corresponding selected personality type from the **Personality Filter** parameter. When you set the **Personality Filter** parameter to **All**, this VI returns the available list names for all supported personalities.

[IMAGE alt='icon' src='rfmxinstr-get-list-names-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Personality Filter — Personality Filter specifies the personality filter to get the list names. You can specify one or more of the following personalities. The default value is All. SpecAn (1) Specifies the SpecAn personality. Demod (2) Specifies the Demod personality. LTE (4) Specifies the LTE personality. GSM (8) Specifies the GSM personality. WCDMA (16) Specifies the WCDMA personality. CDMA2k (32) Specifies the CDMA2k personality. TDSCDMA (64) Specifies the TD-SCDMA personality. EVDO (128) Specifies the EV-DO personality. NR (256) Specifies the NR personality. WLAN (512) Specifies the WLAN personality. BT (1024) Specifies the BT personality. All (2147483647) Specifies all the personalities. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. List Names — List Names returns an array of the list names. Personalities — Personalities returns an array of personalities where each entry corresponds to the personality of each list name in the List Names array. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-nirfsa-session-vi.html language=enus -->
## TOPIC 00075: RFmxInstr Get NIRFSA Session VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-nirfsa-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-nirfsa-session-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the NI-RFSA driver session used by RFmx. Do not close the NI-RFSA driver session before calling the RFmxInstr Close VI. Closing the NI-RFSA driver session before closing RFmx session would lead to unpredictable behavior. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument

### RFmxInstr Get NIRFSA Session VI

Returns the NI-RFSA driver session used by RFmx.

Note

RFmxInstr Close

[IMAGE alt='icon' src='rfmxinstr-get-nirfsa-session-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. NI RFSA Session — NI RFSA Session specifies the NI-RFSA session for the device. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-self-calibrate-last-date-and-time-vi.html language=enus -->
## TOPIC 00076: RFmxInstr Get Self Calibrate Last Date and Time VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-self-calibrate-last-date-and-time-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-self-calibrate-last-date-and-time-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the date and time of the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration date and time for a specific MIMO port. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840

### RFmxInstr Get Self Calibrate Last Date and Time VI

Returns the date and time of the last successful self-calibration. On a MIMO session, use the **Selector String** parameter to get the last successful self-calibration date and time for a specific MIMO port.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842/5860

Note

Image Suppression

Self Calibrate Step

[IMAGE alt='icon' src='rfmxinstr-get-self-calibrate-last-date-and-time-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string). Example: "" "port::myrfsa1/0" You can use the RFmxInstr Build Port String VI to build the selector string. Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Self Calibrate Step — Self Calibrate Step specifies the self-calibration step to query for the last successful self-calibration date and time data. The default value is Preselector Alignment. Preselector Alignment (1) Selects the Preselector Alignment self-calibration step. Gain Reference (2) Selects the Gain Reference self-calibration step. IF Flatness (4) Selects the IF Flatness self-calibration step. Digitizer Self Cal (8) Selects the Digitizer Self Cal self-calibration step. LO Self Cal (10) Selects the LO Self Cal self-calibration step. Amplitude Accuracy (20) Selects the Amplitude Accuracy self-calibration step. Residual LO Power (40) Selects the Residual LO Power self-calibration step. Image Suppression (80) Selects the Image Suppression self-calibration step. Synthesizer Alignment (100) Selects the Synthesizer Alignment self-calibration step. DC Offset (200) Selects the DC Offset self-calibration step. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. Time Stamp — Time Stamp returns the date and time of the last successful self-calibration. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-self-calibrate-last-temperature-vi.html language=enus -->
## TOPIC 00077: RFmxInstr Get Self Calibrate Last Temperature VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-self-calibrate-last-temperature-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-self-calibrate-last-temperature-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the temperature at the last successful self-calibration. On a MIMO session, use the Selector String parameter to get the last successful self-calibration temperature for a specific MIMO port. Supported Devices: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/583

### RFmxInstr Get Self Calibrate Last Temperature VI

Returns the temperature at the last successful self-calibration. On a MIMO session, use the **Selector String** parameter to get the last successful self-calibration temperature for a specific MIMO port.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831 (IF only)/5832 (IF only)/5840/5841/5842/5860

Note

Image Suppression

Self Calibrate Step

[IMAGE alt='icon' src='rfmxinstr-get-self-calibrate-last-temperature-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string). Example: "" "port::myrfsa1/0" You can use the RFmxInstr Build Port String VI to build the selector string. Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Self Calibrate Step — Self Calibrate Step specifies the self-calibration step to query for the last successful self-calibration temperature data. The default value is Preselector Alignment. Preselector Alignment (1) Selects the Preselector Alignment self-calibration step. Gain Reference (2) Selects the Gain Reference self-calibration step. IF Flatness (4) Selects the IF Flatness self-calibration step. Digitizer Self Cal (8) Selects the Digitizer Self Cal self-calibration step. LO Self Cal (10) Selects the LO Self Cal self-calibration step. Amplitude Accuracy (20) Selects the Amplitude Accuracy self-calibration step. Residual LO Power (40) Selects the Residual LO Power self-calibration step. Image Suppression (80) Selects the Image Suppression self-calibration step. Synthesizer Alignment (100) Selects the Synthesizer Alignment self-calibration step. DC Offset (200) Selects the DC Offset self-calibration step. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. Temperature (deg C) — Temperature returns the temperature at the last self-calibration. This value is expressed in degree Celsius. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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

Parent topic:

Calibration Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-signal-configuration-names-vi.html language=enus -->
## TOPIC 00078: RFmxInstr Get Signal Configuration Names VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-signal-configuration-names-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-get-signal-configuration-names-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns the signal names and the corresponding selected personality type from the Personality Filter parameter. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI

### RFmxInstr Get Signal Configuration Names VI

Returns the signal names and the corresponding selected personality type from the **Personality Filter** parameter.

[IMAGE alt='icon' src='rfmxinstr-get-signal-configuration-names-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Personality Filter — Personality Filter specifies the personality filter to get the signal configuration names. You can specify one or more of the following personalities. The default value is All. SpecAn (1) Specifies the SpecAn personality. Demod (2) Specifies the Demod personality. LTE (4) Specifies the LTE personality. GSM (8) Specifies the GSM personality. WCDMA (16) Specifies the WCDMA personality. CDMA2k (32) Specifies the CDMA2k personality. TDSCDMA (64) Specifies the TD-SCDMA personality. EVDO (128) Specifies the EV-DO personality. NR (256) Specifies the NR personality. WLAN (512) Specifies the WLAN personality. BT (1024) Specifies the BT personality. All (2147483647) Specifies all the personalities. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. Signal Names — Signal Names returns an array of the signal names. Personalities — Personalities returns an array of personalities where each entry corresponds to the personality of each signal name in the Signal Names array. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
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

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-initialize-vi.html language=enus -->
## TOPIC 00079: RFmxInstr Initialize VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-initialize-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-initialize-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Creates an RFmx session to the signal/network analyzer you specify through the Resource Name parameter, and returns an Instrument Handle Out that identifies this device in all subsequent RFmx VIs. Enabling the SFP (Soft Front Panel) debug has a performance impact. For best performance, NI recommends

### RFmxInstr Initialize VI

Creates an RFmx session to the signal/network analyzer you specify through the **Resource Name** parameter, and returns an **Instrument Handle Out** that identifies this device in all subsequent RFmx VIs.

Note

[IMAGE alt='icon' src='rfmxinstr-initialize-vi.png']

#### Inputs/Outputs

| Resource Name — Resource Name specifies the resource name of the device to initialize. The following table shows examples of how to specify the resource name. Example # Device Type Syntax 1 myRFmxDevice RFmx device, device name is "myRFmxDevice" 2 myLogicalName IVI logical name or virtual instrument, name is "myLogicalName" For NI-DAQmx devices, the syntax is the device name specified in MAX, as shown in Example 1. Typical default names for NI-DAQmx devices in MAX are Dev1 or PXI1Slot2. You can rename an NI-DAQmx device by right-clicking the name in MAX, selecting Rename from the pull-down menu, and entering a new name. You can also pass the name of an IVI logical name configured with the IVI Configuration utility. For additional information about IVI, refer to the IVI section of the Measurement & Automation Explorer Help. Note For multichannel devices such as the PXIe-5860, the resource name must include the channel number to use. The channel number is specified by appending /ChannelNumber to the device name, where ChannelNumber is the channel number (0, 1, etc.). For example, if the device name is PXI1Slot2 and you want to use channel 0, use the resource name PXI1Slot2/0. Option String — Option String sets the initial value of certain properties for the session. The following properties are used in this parameter: RFmxSetup Simulate AnalysisOnly For more information about properties used in this parameter, refer to NI RF Vector Signal Analyzers Help. The format of this string is "PropertyName=Value", where PropertyName is the name of the property and Value is the value to which the property is set. For example, you can simulate a PXIe-5663E device using either of the following strings: "Simulate=1, RFmxSetup=Model:5663E" "Simulate=1, RFmxSetup=Model:5601; Digitizer:5622; LO:5652; LOBoardType:PXIe" To set multiple properties, separate their assignments with a comma. To use FPGA extensions, specify the custom LabVIEW FPGA bitfile to use with the bitfile specifier within the RFmxSetup string. For example, "RFmxSetup=bitfile:yourbitfile.lvbitx" specifies that RFmx use yourbitfile.lvbitx as the LabVIEW FPGA bitfile for the session. To use AnalysisOnly mode, specify the string as "AnalysisOnly=1". While using this mode, you are responsible for waveform acquisition and RFmx will perform analysis on the I/Q waveform or Spectrum you specify. You must use personality specific Analyze functions to perform the measurements. Note To simulate a device using the PXIe-5622 (25 MHz) digitizer, set the Digitizer field to 5622_25MHz_DDC and the Simulate field to 1. You can set the Digitizer field to 5622_25MHz_DDC only when using the PXIe-5665. To use external NI source measure units (SMU) as the noise source power supply for the Noise Figure (NF) measurement, use "NoiseSourcePowerSupply" as the specifier within the RFmxSetup string. For example, "RFmxSetup= NoiseSourcePowerSupply:myDCPower[0]" configures RFmx to use channel 0 on myDCPower SMU device for powering the noise source. You must allocate a dedicated SMU channel for RFmx. Note RFmx supports PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. Created New? — Created New? is TRUE if the VI created a new session, or FALSE if the VI returned a reference to an existing session. error out — error out contains error information. This output provides standard error out functionality. |  |  |
| --- | --- | --- |
| Example # | Device Type | Syntax |
| 1 | myRFmxDevice | RFmx device, device name is "myRFmxDevice" |
| 2 | myLogicalName | IVI logical name or virtual instrument, name is "myLogicalName" |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-is-self-calibrate-valid-vi.html language=enus -->
## TOPIC 00080: RFmxInstr Is Self Calibrate Valid VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-is-self-calibrate-valid-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-is-self-calibrate-valid-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the Valid Steps parameter to the Steps To Omit parameter of the RFmxInstr Self Calibrate VI. On a MIMO session, use the Selector Stri

### RFmxInstr Is Self Calibrate Valid VI

Returns an array to indicate which calibration steps contain valid calibration data. To omit steps with the valid calibration data from self-calibration, you can pass the **Valid Steps** parameter to the **Steps To Omit** parameter of the [RFmxInstr Self Calibrate](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_self_calibrate) VI. On a MIMO session, use the **Selector String** parameter to get the self-calibration validity for a specific MIMO port.

**Supported devices:** PXIe-5663/5663E/5665/5668

[IMAGE alt='icon' src='rfmxinstr-is-self-calibrate-valid-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies a Selector String comprising of a MIMO port on a MIMO session. The default value is "" (empty string). Example: "" "port::myrfsa1/0" You can use the RFmxInstr Build Port String VI to build the selector string. Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. Self Calibrate Valid — Self Calibrate Valid returns TRUE if all the calibration data is valid and FALSE if any of the calibration data is invalid. Valid Steps — Valid Steps returns an array of valid steps. Preselector Alignment (1) Indicates the Preselector Alignment calibration data is valid. This step generates coefficients to align the preselector across the frequency range for your device. Gain Reference (2) Indicates the Gain Reference calibration data is valid. This step measures the changes in gain since the last external calibration was run. IF Flatness (4) Indicates the IF Flatness calibration data is valid. This step measures the IF response of the entire system for each of the supported IF filters. Digitizer Self Cal (8) Indicates the Digitizer Self Cal calibration data is valid. This step calls for digitizer self-calibration if the digitizer is associated with the RF downconverter. LO Self Cal (10) Indicates the LO Self Cal calibration data is valid. This step calls for LO self-calibration if the LO source module is associated with the RF downconverter. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Preselector Alignment (1) | Indicates the Preselector Alignment calibration data is valid. This step generates coefficients to align the preselector across the frequency range for your device. |
| Gain Reference (2) | Indicates the Gain Reference calibration data is valid. This step measures the changes in gain since the last external calibration was run. |
| IF Flatness (4) | Indicates the IF Flatness calibration data is valid. This step measures the IF response of the entire system for each of the supported IF filters. |
| Digitizer Self Cal (8) | Indicates the Digitizer Self Cal calibration data is valid. This step calls for digitizer self-calibration if the digitizer is associated with the RF downconverter. |
| LO Self Cal (10) | Indicates the LO Self Cal calibration data is valid. This step calls for LO self-calibration if the LO source module is associated with the RF downconverter. |

Parent topic:

Calibration

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-load-configurations-vi.html language=enus -->
## TOPIC 00081: RFmxInstr Load Configurations VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-load-configurations-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-load-configurations-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Loads the properties of an RFmx session saved in a file. This file can be generated using RFmxInstr Save All Configurations VI or using the RF Signal Analyzer panel in InstrumentStudio. You can specify the configurations to skip while loading from a file using the Load Options property. If the file

### RFmxInstr Load Configurations VI

Loads the properties of an RFmx session saved in a file. This file can be generated using [RFmxInstr Save All Configurations](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_save_all_configurations) VI or using the RF Signal Analyzer panel in InstrumentStudio.

You can specify the configurations to skip while loading from a file using the [Load Options](/csh?context=rfmxinstr_rfmxinstrprop_attra3) property.

Note

RFmxInstr Reset Entire Session

[IMAGE alt='icon' src='rfmxinstr-load-configurations-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. File Path — File Path specifies the complete path to the file from which the configurations are to be loaded. Default file extension: .rfmxconfig error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-load-s-parameter-external-attenuation-table-from-s2p-file-vi.html language=enus -->
## TOPIC 00082: RFmxInstr Load S-parameter External Attenuation Table from S2P File VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-load-s-parameter-external-attenuation-table-from-s2p-file-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-load-s-parameter-external-attenuation-table-from-s2p-file-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Stores the S-parameter table from the S2P file in the calibration plane specified by the Selector String parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane. If there is only one tab

### RFmxInstr Load S-parameter External Attenuation Table from S2P File VI

Stores the S-parameter table from the S2P file in the calibration plane specified by the **Selector String** parameter. S-parameter tables are used for fixture de-embedding. On a MIMO session, the S-parameter table is stored for each MIMO port in the specified calibration plane.

Note

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-load-s-parameter-external-attenuation-table-from-s2p-file-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which the external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all MIMO ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Table Name — Table Name specifies the name to be associated with S-parameter table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" S2P File Path — S2P File Path specifies the path to the S2P file that contains S-parameter table information for the specified port. error in (no error) — error in (no error) describes error conditions that occur before this node runs. This input provides standard error in functionality. S-parameter Orientation — S-parameter Orientation specifies the orientation of the data in the S-parameter table relative to the port you specify. The default value is Port2 Towards DUT. Port1 Towards DUT (0) Port 1 of the S2P is oriented towards the DUT. Port2 Towards DUT (1) Port 2 of the S2P is oriented towards the DUT. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |  |
| --- | --- |
| Port1 Towards DUT (0) | Port 1 of the S2P is oriented towards the DUT. |
| Port2 Towards DUT (1) | Port 2 of the S2P is oriented towards the DUT. |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-property-node-vi.html language=enus -->
## TOPIC 00083: RFmxInstr Property Node VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-property-node-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-property-node-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Gets (reads), sets (writes), or resets (sets to default value) RFmx instrument control properties. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFS

### RFmxInstr Property Node VI

Gets (reads), sets (writes), or resets (sets to default value) RFmx instrument control properties.

[IMAGE alt='icon' src='rfmxinstr-property-node-vi.png']

#### Inputs/Outputs

| — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Property — RFmx Instr Property Node is used to get (read), set (write), or reset (set to default value) RFmx instrument control properties. — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

RFInstr

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-driver-vi.html language=enus -->
## TOPIC 00084: RFmxInstr Reset Driver VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-driver-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-driver-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Restores the NI-RFSA driver state to a default state to avoid RFmx using any hardware or driver state that was set by the RF toolkits or other custom NI-RFSA code. Use this VI when you switch back to using RFmx to perform measurements after you have used the NI-RFSA handle to perform measurements wi

### RFmxInstr Reset Driver VI

Restores the NI-RFSA driver state to a default state to avoid RFmx using any hardware or driver state that was set by the RF toolkits or other custom NI-RFSA code.

Use this VI when you switch back to using RFmx to perform measurements after you have used the NI-RFSA handle to perform measurements with RF toolkits or you have used other custom NI-RFSA code. Unlike the [RFmxInstr Reset to Default](/csh?context=rfmxinstr_rfmxinstrvi_rfmxinstr_reset_to_default) VI, the RfmxInstr Reset Driver VI does not reset RFmx properties configured on the RFmx session. Hence, you do not need to set RFmx properties again when switching back to RFmx measurements. Refer to [RFmx SpecAn CHP - WCDMA ModAcc - CHP Example (LabVIEW)](https://decibel.ni.com/content/docs/DOC-39161) for more information about using RFmx to perform measurements.

[IMAGE alt='icon' src='rfmxinstr-reset-driver-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-entire-session-vi.html language=enus -->
## TOPIC 00085: RFmxInstr Reset Entire Session VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-entire-session-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-entire-session-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Deletes all the named signal in the session and resets all properties for the default signal instances of already loaded personalities in the session. This VI disables all the calibration planes. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In identifies the instrume

### RFmxInstr Reset Entire Session VI

Deletes all the named signal in the session and resets all properties for the default signal instances of already loaded personalities in the session.

This VI disables all the calibration planes.

[IMAGE alt='icon' src='rfmxinstr-reset-entire-session-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-to-default-vi.html language=enus -->
## TOPIC 00086: RFmxInstr Reset to Default VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-to-default-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-reset-to-default-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Resets the RFmxInstr properties to their default values. This VI disables all the calibration planes. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RF

### RFmxInstr Reset to Default VI

Resets the RFmxInstr properties to their default values.

This VI disables all the calibration planes.

[IMAGE alt='icon' src='rfmxinstr-reset-to-default-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-select-active-external-attenuation-table-vi.html language=enus -->
## TOPIC 00087: RFmxInstr Select Active External Attenuation Table VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-select-active-external-attenuation-table-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-select-active-external-attenuation-table-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Activates the external attenuation table set by the Table Name parameter in the calibration plane specified by the Selector String parameter. On a MIMO session, this VI selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correctio

### RFmxInstr Select Active External Attenuation Table VI

Activates the external attenuation table set by the **Table Name** parameter in the calibration plane specified by the **Selector String** parameter. On a MIMO session, this VI selects the active external attenuation table for the specified MIMO port. The specified table will be used for amplitude correction during measurement.

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842/5860

[IMAGE alt='icon' src='rfmxinstr-select-active-external-attenuation-table-vi.png']

#### Inputs/Outputs

| Selector String — Selector String specifies the calibration plane name in which either S-parameter or external attenuation table is stored. This input accepts the calibration plane name with the "calplane::" prefix. If you do not specify the calibration plane name, the default calibration plane instance is used. The default value is "" (empty string). On a MIMO session, the default "" (empty string) selects the active external attenuation table for all the MIMO Ports. To configure external attenuation type for a specific MIMO port, use the port specifier with or without the calplane name. Example: "calplane::plane1/port::myrfsa1/0". Note For PXIe-5830/5831/5832 devices, port names should also be specified along with Calplane names. Hence, the valid selector string is "calplane::<calplaneName>/port::<portName>". If you specify "port::all", all ports are considered configured. For a MIMO port, the valid selector string is "calplane::<calplaneName>/port::<deviceName>/<channelNumber>/<portName>". If you specify "port::all", all ports are considered configured. Use RFmxInstr Get Available Ports VI to get the valid port names. Example: "" "calplane::plane0" "calplane::plane0/port::if0" "port::if0" "calplane::plane0/port::all" "calplane::plane0/port::myrfsa1/0" "calplane::plane0/port::myrfsa1/0, port::myrfsa2/0" "calplane::plane0/port::myrfsa1/0/if0" Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Table Name — Table Name specifies the name to be associated with external attenuation table within a calibration plane. Provide a unique name, such as "table1" to configure the table. The default value is "" (empty string). Example: "" "table1" error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

External Attenuation Table

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-vi-tree-vi.html language=enus -->
## TOPIC 00088: RFmxInstr VI Tree VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-vi-tree-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-vi-tree-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Displays all the VIs available in RFmxInstr for instrument configuration and control. The VIs are organized in the order they must be used in the program you create. icon

### RFmxInstr VI Tree VI

Displays all the VIs available in RFmxInstr for instrument configuration and control. The VIs are organized in the order they must be used in the program you create.

[IMAGE alt='icon' src='rfmxinstr-vi-tree-vi.png']

Parent topic:

RFInstr

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-wait-for-acquisition-complete-vi.html language=enus -->
## TOPIC 00089: RFmxInstr Wait for Acquisition Complete VI

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-wait-for-acquisition-complete-vi.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/rfmxinstr-wait-for-acquisition-complete-vi.html
- document_id: `rfmxinstr-labview-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Waits and blocks the data flow until the acquisition is complete. This VI is typically called after a specific initiate VI. icon Inputs/Outputs cgenclassrntag.png Instrument Handle In Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initiali

### RFmxInstr Wait for Acquisition Complete VI

Waits and blocks the data flow until the acquisition is complete. This VI is typically called after a specific initiate VI.

[IMAGE alt='icon' src='rfmxinstr-wait-for-acquisition-complete-vi.png']

#### Inputs/Outputs

| Instrument Handle In — Instrument Handle In identifies the instrument session. Instrument Handle In is obtained from the RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize NIRFSA (Array) VI. Timeout (s) — Timeout specifies the time to wait for an ongoing acquisition to complete before returning a timeout error. A value of -1 specifies that the VI waits indefinitely for acquisition to complete. This value is expressed in seconds. The default value is 10. error in (no error) — error in describes error conditions that occur before this node runs. This input provides standard error in functionality. Instrument Handle Out — Instrument Handle Out passes a reference of the instrument session to the next VI. error out — error out contains error information. This output provides standard error out functionality. |
| --- |

Parent topic:

Utility

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/standard-functionality-for-error-in-parameters.html language=enus -->
## TOPIC 00090: Using the Standard Functionality for error in Parameters

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/standard-functionality-for-error-in-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/standard-functionality-for-error-in-parameters.html
- document_id: `rfmxinstr-labview-api-ref`
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

<!--NI_TOPIC bundle=rfmxinstr-labview-api-ref path=vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/standard-functionality-for-error-out-parameters.html language=enus -->
## TOPIC 00091: Using the Standard Functionality for error out Parameters

- bundle_id: `rfmxinstr-labview-api-ref`
- source_path: `vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/standard-functionality-for-error-out-parameters.html`
- source_url: https://docs-be.ni.com/bundle/rfmxinstr-labview-api-ref/raw/resource/enus/vi-lib/rfmx/rfinstr/mx/rfmxinstr-llb/standard-functionality-for-error-out-parameters.html
- document_id: `rfmxinstr-labview-api-ref`
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
