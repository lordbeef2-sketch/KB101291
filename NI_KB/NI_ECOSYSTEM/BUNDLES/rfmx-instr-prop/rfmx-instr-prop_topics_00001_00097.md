# NI DOCUMENT BUNDLE: rfmx-instr-prop

<!--NI_BUNDLE_CHUNK bundle=rfmx-instr-prop start=1 end=97 -->
<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr10.html language=enus -->
## TOPIC 00001: Advanced:Mixer Level (dBm) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr10.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr10.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Mixer Level (dBm) Property

**Short Name:**Mixer Level (dBm)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the mixer level. This value is expressed in dBm.

The mixer level represents the attenuation value to apply to the input RF signal as it reaches the first mixer in the signal chain. If you do not set this property, the RFmx driver automatically selects an optimal mixer level value based on the reference level.

If you set the [Mixer Level](attr10.html) and [Mixer Level Offset](attrf.html) properties at the same time, the RFmx driver returns an error.

This property is read-only for PXIe-5663/5663E devices.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default values**

| PXIe-5665/5668 | -10 |
| --- | --- |
| All other devices | N/A |

The valid values for this property depend on your device configuration.

**Supported devices**: PXIe-5663/5663E/5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr11.html language=enus -->
## TOPIC 00002: Advanced:IF Output Power Level Offset Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr11.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr11.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:IF Output Power Level Offset Property

**Short Name:**IF Output Power Level Offset

Property of [RFmxInstr](crfmxinstr.html)

Specifies the power offset by which to adjust the default IF output power level. This value is expressed in dB.

This property does not depend on absolute IF output power levels; therefore, you can use this property to adjust the IF output power level on all RFmx-supported devices without knowing the exact default value. Use this property to increase or decrease the nominal output level to achieve better measurement results.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.

**Supported devices**: PXIe-5663/5663E/5665, PXIe-5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr12.html language=enus -->
## TOPIC 00003: LO:LO Injection Side Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr12.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr12.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Injection Side Property

**Short Name:**LO Injection Side

Property of [RFmxInstr](crfmxinstr.html)

Specifies the LO injection side.

| PXIe-5663/5663E | For frequencies below 517.5 MHz or above 6.4125 GHz, the LO injection side is fixed, and the RFmx driver returns an error if you specify an incorrect value. If you do not configure this property, the RFmx driver selects the default LO injection side based on the downconverter center frequency. Reset this property to return to automatic behavior. |
| --- | --- |
| PXIe-5665 (3.6 GHz) | Setting this property to Low Side is not supported for this device. |
| PXIe-5665 (14 GHz) | Setting this property to Low Side is supported for this device for frequencies greater than 4 GHz, but this configuration is not calibrated, and device specifications are not guaranteed. |
| PXIe-5668 | Setting this property to Low Side is supported for some frequencies in high band, varying by the final IF frequency. This configuration is not calibrated and device specifications are not guaranteed. |

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default value:**

- PXIe-5663/5663E (frequencies < 3.0 GHz): High Side
- PXIe-5663/5663E (frequencies >= 3.0 GHz): Low Side
- PXIe-5665/5668: High Side

**Supported devices**: PXIe-5663/5663E/5665/5668

| High Side (0) | Configures the LO signal that the device generates at a frequency higher than the RF signal. This LO frequency is given by the following formula: fLO = fRF + fIF |
| --- | --- |
| Low Side (1) | Configures the LO signal that the device generates at a frequency lower than the RF signal. This LO frequency is given by the following formula: fLO = fRF – fIF |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr13.html language=enus -->
## TOPIC 00004: Advanced:Phase Offset Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr13.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr13.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Phase Offset Property

**Short Name:**Phase Offset

Property of [RFmxInstr](crfmxinstr.html)

Specifies the offset to apply to the initial I and Q phases.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.

Valid values are -180 degrees to 180 degrees, inclusive.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr15.html language=enus -->
## TOPIC 00005: Advanced:Digitizer Dither Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr15.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr15.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Digitizer Dither Enabled Property

**Short Name:**Digitizer Dither Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether dithering is enabled on the digitizer.

Dithering adds band-limited noise in the analog signal path to help reduce the quantization effects of the ADC and improve spectral performance. On the PXIe-5622, this out-of-band noise is added at low frequencies of up to approximately 12 MHz.

**PXIe-5663/5663E/5665:** When you enable dithering, the maximum signal level is reduced by up to 3 dB. This signal level reduction is accounted for in the nominal input ranges of the PXIe-5622. Therefore, you can overrange the input by up to 3 dB with dither disabled. For example, the +4 dBm input range can handle signal levels up to +7 dBm with dither disabled.

For wider bandwidth acquisitions, such as 40 MHz, disable dithering to eliminate residual leakage of the dither signal into the lower frequencies of the IF passband, which starts at 12.5 MHz and ends at 62.5 MHz. This leakage can slightly raise the noise floor in the lower frequencies, thus degrading the performance in high-sensitivity applications. When performing spectral measurements, this leakage can also appear as a wide, low-amplitude signal near the 12.5 MHz and 62.5 MHz frequencies. The width and amplitude of the signal depends on your resolution bandwidth and the type of time-domain window you apply to your FFT.

**PXIe-5668**: When you enable dithering, the maximum signal level is reduced by up to 2 dB. For the PXIe-5624, the maximum input power with dither off is 8 dBm and the maximum input power level with dither on is 6 dBm. When acquiring an 800 MHz bandwidth signal, the I/Q data contains the dither even if the dither signal is not in the displayed spectrum. The dither can affect actions like power level triggering.

|  | Note For the PXIe-5668, disabling dithering can negatively affect absolute amplitude accuracy. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

|  | Note For PXIe-5820/5830/5831/5832/5840/5841/5842, only Enabled is supported. |
| --- | --- |

The default value is **Enabled**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Disabled (0) | Disables the property. |
| --- | --- |
| Enabled (1) | Enables the property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr16.html language=enus -->
## TOPIC 00006: Advanced:FFT Width Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr16.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr16.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:FFT Width Property

**Short Name:**FFT Width

Property of [RFmxInstr](crfmxinstr.html)

Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition.

The lower limit for all devices that support setting the FFT Width property is 7.325 kHz.

**PXIe-5663/5663E**: The FFT width upper limit for the PXIe-5663/5663E depends on the RF frequency and on the module revision of the PXIe-5601. For more information about determining which revision of the PXIe-5601 RF downconverter you have installed, refer to the Identifying Module Revision topic in the *NI RF Vector Signal Analyzers Help*.

|  | Note The maximum FFT width for your device is constrained to 50 MHz or 25 MHz, depending on the digitizer option you purchased. |
| --- | --- |

|  | Note You can use the FFT Width property with in-band retuning. For more information about in-band retuning, refer to the Downconverter Center Frequency property. |
| --- | --- |

The RFmx driver treats the device instantaneous bandwidth as the effective real-time bandwidth of the signal path. The span specifies the frequency range of the computed spectrum. A signal analyzer can acquire a bandwidth only within the device instantaneous bandwidth. If the span you choose is greater than the device instantaneous bandwidth, the RFmx driver obtains multiple acquisitions and combines them into a single spectrum. By specifying the FFT width, you can control the specific bandwidth obtained in each signal acquisition.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Supported devices**: PXIe-5663/5663E/5665, PXIe-5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr17.html language=enus -->
## TOPIC 00007: Advanced:OSP Delay Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr17.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr17.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:OSP Delay Enabled Property

**Short Name:**OSP Delay Enabled

Property of [RFmxInstr](crfmxinstr.html)

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

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Enabled**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Disabled (0) | Disables the property. |
| --- | --- |
| Enabled (1) | Enables the property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr18.html language=enus -->
## TOPIC 00008: Device Information:Device Temperature (deg C) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr18.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr18.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Device Temperature (deg C) Property

**Short Name:**Device Temperature (deg C)

Property of [RFmxInstr](crfmxinstr.html)

Returns the current temperature of the module. This value is expressed in degrees Celsius.

To use this property for PXIe-5830/5831/5832, you must first use the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) property to specify the name of the channel you are configuring. When you are reading the device temperature, you must specify the context in the Selector String input as "module::<ModuleName>". You can also use the [RFmxInstr Build Module String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_module_string.html) VI to build the module string. For all other devices, the only valid value for the selector string is "" (empty string).

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the selector string to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string. For PXIe-5830/5831/5832, you must specify the context in the selector string input as port::<deviceName>/<channelNumber>/module::<moduleName>.

Refer to the following table to determine which strings are valid for your configuration.

| Hardware Module | TRX Port Type | Selector String |
| --- | --- | --- |
| PXIe-3621/3622/3623 | - | if or "" (empty string) |
| PXIe-5820 | - | fpga |
| First connected mmRH-5582 | DIRECT TRX PORTS Only | rf0 |
| SWITCHED TRX PORTS [0-7] | rf0switch0 |  |
| SWITCHED TRX PORTS [8-15] | rf0switch1 |  |
| Second connected mmRH-5582 | DIRECT TRX PORTS Only | rf1 |
| SWITCHED TRX PORTS [0-7] | rf1switch0 |  |
| SWITCHED TRX PORTS [8-15] | rf1switch1 |  |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr19.html language=enus -->
## TOPIC 00009: Device Information:Digitizer Temperature (deg C) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr19.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr19.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Digitizer Temperature (deg C) Property

**Short Name:**Digitizer Temperature (deg C)

Property of [RFmxInstr](crfmxinstr.html)

Returns the current temperature of the digitizer module. This value is expressed in degrees Celsius.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

|  | Note This property is not supported if you are using an external digitizer. |
| --- | --- |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr1a.html language=enus -->
## TOPIC 00010: Device Information:LO Temperature (deg C) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr1a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr1a.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:LO Temperature (deg C) Property

**Short Name:**LO Temperature (deg C)

Property of [RFmxInstr](crfmxinstr.html)

Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

|  | Note This property is not supported if you are using an external LO. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr1b.html language=enus -->
## TOPIC 00011: Device Information:Instrument Firmware Revision Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr1b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr1b.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Instrument Firmware Revision Property

**Short Name:**Instr Firmware Rev

Property of [RFmxInstr](crfmxinstr.html)

Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr1c.html language=enus -->
## TOPIC 00012: Device Information:Instrument Model Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr1c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr1c.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Instrument Model Property

**Short Name:**Instr Model

Property of [RFmxInstr](crfmxinstr.html)

Returns a string that contains the model number or name of the RF device that you are currently using.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr1d.html language=enus -->
## TOPIC 00013: Device Information:Module Revision Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr1d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr1d.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Module Revision Property

**Short Name:**Module Rev

Property of [RFmxInstr](crfmxinstr.html)

Returns the revision of the RF downconverter module.

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

|  | Note For PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842, this property returns the revision of the VST module. |
| --- | --- |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr1e.html language=enus -->
## TOPIC 00014: Device Information:Serial Number Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr1e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr1e.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Serial Number Property

**Short Name:**Serial Number

Property of [RFmxInstr](crfmxinstr.html)

Returns the serial number of the RF downconverter module.

|  | Note For PXIe-5644/5645/5646 and PXIe-5820/5840/5841/5842, this property returns the serial number of the VST module. For PXIe-5830/5831/5832, this property returns the serial number of PXIe-3621/3622/3623. |
| --- | --- |

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr1f.html language=enus -->
## TOPIC 00015: Device Information:Preselector Present Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr1f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr1f.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:Preselector Present Property

**Short Name:**Preselector Present

Property of [RFmxInstr](crfmxinstr.html)

Indicates whether a preselector is available on the RF downconverter module.

| TRUE | A preselector is available on the downconverter. |
| --- | --- |
| FALSE | No preselector is available on the downconverter. |

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2.html language=enus -->
## TOPIC 00016: Frequency Reference:Source Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Frequency Reference:Source Property

**Short Name:**Freq Ref Source

Property of [RFmxInstr](crfmxinstr.html)

Specifies the frequency reference source.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

All other devices default value is **OnboardClock**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| OnboardClock (OnboardClock) | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to the PXIe-5652 LO source onboard clock. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. On versions of the PXIe-5663/5663E that lack a REF OUT2 connector on the PXIe-5652, connect the REF IN/OUT connector on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: The RFmx driver locks the PXIe-5665 to the PXIe-5653 LO source onboard clock. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN terminal. PXIe-5668: Lock the PXIe-5668 to the PXIe-5653 LO SOURCE onboard clock. Connect the LO2 OUT connector on the PXIe-5606 to the CLK IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: The RFmx driver locks the device to its onboard clock. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. PXIe-5842: Lock to the associated PXIe-5655 onboard clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| --- | --- |
| RefIn (RefIn) | PXIe-5663/5663E: Connect the external signal to the PXIe-5652 REF IN/OUT connector. Connect the REF OUT2 connector (if it exists) on the PXIe-5652 to the PXIe-5622 CLK IN terminal. PXIe-5665: Connect the external signal to the PXIe-5653 REF IN connector. Connect the 100 MHz REF OUT terminal on the PXIe-5653 to the PXIe-5622 CLK IN connector. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5668: Connect the external signal to the PXIe-5653 REF IN connector. Connect the LO2 OUT on the PXIe-5606 to the CLK IN connector on the PXIe-5622. If your external clock signal frequency is set to a frequency other than 10 MHz, set the Frequency Reference Frequency property according to the frequency of your external clock signal. PXIe-5644/5645/5646, PXIe-5820/5840/5841/5842: The RFmx driver locks the device to the signal at the external REF IN connector. PXIe-5830/5831/5832: For PXIe-5830, connect the PXIe-5820 REF IN connector to the PXIe-3621 REF OUT connector. For PXIe-5831, connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. For PXIe-5832, connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. For PXIe-5830, lock the external signal to the PXIe-3621 REF IN connector. For PXIe-5831, lock the external signal to the PXIe-3622 REF IN connector. For PXIe-5832, lock the external signal to the PXIe-3623 REF IN connector. PXIe-5831 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3622 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3622 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5832 with PXIe-5653: Connect the PXIe-5820 REF IN connector to the PXIe-3623 REF OUT connector. Connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-3623 REF IN connector. Lock the external signal to the PXIe-5653 REF IN connector. PXIe-5842: Lock to the signal at the REF IN connector on the associated PXIe-5655. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| PXI_Clk (PXI_Clk) | PXIe-5668: Lock the PXIe-5653 to the PXI backplane clock. Connect the PXIe-5606 LO2 OUT to the LO2 IN connector on the PXIe-5624. PXIe-5644/5645/5646, PXIe-5663/5663E/5665, and PXIe-5820/5840/5841: The RFmx driver locks the device to the PXI backplane clock. PXIe-5830/5831/5832 with PXIe-5653/5841 with PXIe-5655, PXIe-5842: The RFmx driver locks the device to the PXI backplane clock. Cables between modules are required as shown in the Getting Started Guide for the instrument. |
| ClkIn (ClkIn) | PXIe-5663/5663E: The RFmx driver locks the PXIe-5663/5663E to an external 10 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the FREQ REF IN connector on the PXIe-5652. PXIe-5665: The RFmx driver locks the PXIe-5665 to an external 100 MHz signal. Connect the external signal to the PXIe-5622 CLK IN connector, and connect the PXIe-5622 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5668: Lock the PXIe-5668 to an external 100 MHz signal. Connect the external signal to the CLK IN connector on the PXIe-5624, and connect the PXIe-5624 CLK OUT connector to the REF IN connector on the PXIe-5653. Set the Frequency Reference Frequency property to 100 MHz. PXIe-5644/5645/5646, PXIe-5820/5830/5831/5831 with PXIe-5653/5832/5832 with PXIe-5653/5840/5841/5842/5840 with PXIe-5653: This configuration does not apply. |
| RefIn2 (RefIn2) |  |
| PXI_ClkMaster (PXI_ClkMaster) | PXIe-5831 with PXIe-5653: The RFmx driver configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3622 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5832 with PXIe-5653: The RFmx driver configures the PXIe-5653 to export the reference clock and configures the PXIe-5820 and PXIe-3623 to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXI chassis REF IN connector. PXIe-5840 with PXIe-5653: The RFmx driver configures the PXIe-5653 to export the reference clock, and configures the PXIe-5840 to use PXI_Clk. For best performance, configure all other devices in the system to use PXI_Clk as the reference clock source. You must connect the PXIe-5653 REF OUT (10 MHz) connector to the PXIe-5840 REF IN connector for this configuration. PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842: This configuration does not apply. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Frequency Reference |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr20.html language=enus -->
## TOPIC 00017: Device Information:RF Preamp Present Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr20.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr20.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Device Information:RF Preamp Present Property

**Short Name:**RF Preamp Present

Property of [RFmxInstr](crfmxinstr.html)

Indicates whether an RF preamplifier is available on the RF downconverter module.

| TRUE | A preamplifier is available on the downconverter. |
| --- | --- |
| FALSE | No preamplifier is available on the downconverter. |

On a MIMO session, use "port::<deviceName>/<channelNumber>" as the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) to read this property. You can use the [RFmxInstr Build Port String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_port_string.html) VI to build the selector string.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr21.html language=enus -->
## TOPIC 00018: LO:LO Export Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr21.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr21.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Export Enabled Property

**Short Name:**LO Export Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether to enable the LO OUT terminals on the installed devices.

| TRUE | Enables the LO OUT terminals. |
| --- | --- |
| FALSE | Disables the LO OUT terminals |

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default value**:

- PXIe-5663/5663E: TRUE
- PXIe-5644/5645/5646, PXIe-5665/5668, PXIe-5830/5831/5832/5840/5841/5842: FALSE

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr22.html language=enus -->
## TOPIC 00019: Frequency Reference:Exported Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr22.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr22.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Frequency Reference:Exported Terminal Property

**Short Name:**Freq Ref Export Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies a comma-separated list of the terminals at which to export the frequency reference.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| None () | The Reference Clock is not exported. This value is not valid for the PXIe-5644/5645/5646. |
| --- | --- |
| RefOut (RefOut) | Export the clock on the REF IN/OUT terminal on the PXIe-5652, the REF OUT terminals on the PXIe-5653, or the REF OUT terminal on the PXIe-5694, PXIe-5644/5645/5646, or PXIe-5820/5830/5831/5832/5840/5841. |
| RefOut2 (RefOut2) | Export the clock on the REF OUT2 terminal on the PXIe-5652. This value is valid only for the PXIe-5663E. |
| ClkOut (ClkOut) | Export the Reference Clock on the CLK OUT terminal on the Digitizer. This value is not valid for the PXIe-5644/5645/5646 or PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr23.html language=enus -->
## TOPIC 00020: Trigger:Export Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr23.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr23.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Export Output Terminal Property

**Short Name:**Trigger Export Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646 and PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists on only PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector on PXIe-5142 and PXIe-5624. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for the PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid on only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr24.html language=enus -->
## TOPIC 00021: Trigger:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr24.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr24.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Terminal Name Property

**Short Name:**Trigger Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/RefTrigger , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/RefTrigger , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/RefTrigger , where DigitizerName is the name of your associated digitizer module in MAX.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr25.html language=enus -->
## TOPIC 00022: Advanced:Cleaner Spectrum Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr25.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr25.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Cleaner Spectrum Property

**Short Name:**Cleaner Spectrum

Property of [RFmxInstr](crfmxinstr.html)

Specifies how to obtain the lowest noise floor or faster measurement speed.

| PXIe-5665 | Sets the FFT Width property to take narrower bandwidth acquisitions and avoid digitizer spurs. Uses IF filters to reduce the noise floor for frequencies below 80 MHz. |
| --- | --- |
| PXIe-5644/5645/5646, PXIe-5840/5841/5842 | Returns the best possible spectrum. |
| PXIe-5668 | Returns the best possible spectrum. To provide the best spectrum measurement, the acquisition is reduced to 100 MHz segments for any center frequency. |
| Other devices | This property is ignored. |

|  | Note Some measurements, such as Spurious Emissions enable the Cleaner Spectrum property by default. You can speed up those measurements by disabling the Cleaner Spectrum property. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Disabled**.

**Supported devices**: PXIe-5665, PXIe-5668, PXIe-5644/5645/5646, PXIe-5840/5841/5842

| Disabled (0) | Disable this property to get faster measurement speed. |
| --- | --- |
| Enabled (1) | Enable this property to get the lowest noise floor and avoid digitizer spurs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr27.html language=enus -->
## TOPIC 00023: Recommended Settings:Acquisition Type Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr27.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr27.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Acquisition Type Property

**Short Name:**Recommended Acquisition Type

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended acquisition type for the last committed measurement configuration.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

| IQ (0) | Indicates that the recommended acquisition type is I/Q. Use the Analyze (IQ) VI to perform the measurement. |
| --- | --- |
| Spectral (1) | Indicates that the recommended acquisition type is Spectral. Use Analyze (Spectrum) VI to perform the measurement. |
| IQ or Spectral (2) | Indicates that the recommended acquisition type is I/Q or Spectral. Use either Analyze (IQ) or Analyze (Spectrum) VI to perform the measurement. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr28.html language=enus -->
## TOPIC 00024: Recommended Settings:Number of Records Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr28.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr28.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Number of Records Property

**Short Name:**Recommended Num Records

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended number of records to acquire to complete measurement averaging.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr29.html language=enus -->
## TOPIC 00025: Recommended Settings:Trigger Min Quiet Time (s) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr29.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr29.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Trigger Min Quiet Time (s) Property

**Short Name:**Recommended Trigger Min Quiet Time (s)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2a.html language=enus -->
## TOPIC 00026: Recommended Settings:IQ:Acquisition Time (s) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2a.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:IQ:Acquisition Time (s) Property

**Short Name:**Recommended Acquisition Time (s)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended acquisition time for I/Q acquisition. This value is expressed in seconds.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2b.html language=enus -->
## TOPIC 00027: Recommended Settings:IQ:Minimum Sample Rate (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2b.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:IQ:Minimum Sample Rate (Hz) Property

**Short Name:**Recommended Min Sample Rate (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended minimum sample rate for I/Q acquisition. This value is expressed in Hz.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2c.html language=enus -->
## TOPIC 00028: Recommended Settings:IQ:Pre Trigger Time (s) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2c.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:IQ:Pre Trigger Time (s) Property

**Short Name:**Recommended Pre Trigger Time (s)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended pretrigger time for I/Q acquisition. This value is expressed in seconds.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2d.html language=enus -->
## TOPIC 00029: Recommended Settings:Spectral:Acquisition Span (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2d.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Spectral:Acquisition Span (Hz) Property

**Short Name:**Recommended Acquisition Span (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended acquisition span for spectral acquisition. This value is expressed in Hz.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2e.html language=enus -->
## TOPIC 00030: Recommended Settings:Spectral:FFT Window Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2e.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Spectral:FFT Window Property

**Short Name:**Recommended FFT Window

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended FFT window type for spectral acquisition.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

| None (0) | Indicates that the measurement does not use FFT windowing to reduce spectral leakage. |
| --- | --- |
| Flat Top (1) | Indicates a Flat Top FFT window type. |
| Hanning (2) | Indicates a Hanning FFT window type. |
| Hamming (3) | Indicates a Hamming FFT window type. |
| Gaussian (4) | Indicates a Gaussian FFT window type. |
| Blackman (5) | Indicates a Blackman FFT window type. |
| Blackman-Harris (6) | Indicates a Blackman-Harris FFT window type. |
| Kaiser-Bessel (7) | Indicates a Kaiser-Bessel FFT window type. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr2f.html language=enus -->
## TOPIC 00031: Recommended Settings:Spectral:Resolution Bandwidth (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr2f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr2f.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Spectral:Resolution Bandwidth (Hz) Property

**Short Name:**Recommended RBW (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended FFT bin width for spectral acquisition. This value is expressed in Hz.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr3.html language=enus -->
## TOPIC 00032: Frequency Reference:Frequency (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr3.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Frequency Reference:Frequency (Hz) Property

**Short Name:**Freq Ref Frequency (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the Reference Clock rate, when the [Frequency Reference Source](attr2.html) property is set to **ClkIn** or **RefIn**. This value is expressed in Hz.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 10 MHz.

**Valid values**

| PXIe-5644/5645/5646, PXIe-5663/5663E, PXIe-5820/5830/5831/5832/5840/5841/5842 | 10 MHz |
| --- | --- |
| PXIe-5665/5668 | 5 MHz to 100 MHz (inclusive), in increments of 1 MHz |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Frequency Reference |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr30.html language=enus -->
## TOPIC 00033: Advanced:IF Filter Bandwidth (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr30.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr30.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:IF Filter Bandwidth (Hz) Property

**Short Name:**IF Filter BW (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the IF filter path bandwidth for your device configuration.

|  | Note For composite devices, such as the PXIe-5665/5668, the IF filter path bandwidth includes all IF filters across the component modules of a composite device. |
| --- | --- |

RFmx chooses an appropriate IF filter as default IF Filter based on measurement configuration, center frequency, cleaner spectrum and downconverter preselector.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Supported devices**: PXIe-5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr31.html language=enus -->
## TOPIC 00034: Advanced:RF Highpass Filter Frequency (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr31.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr31.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:RF Highpass Filter Frequency (Hz) Property

**Short Name:**RF Highpass Filter Freq (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly.

 For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this property returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.

The valid values range from 0 to 26.5.

**Supported devices**: PXIe-5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr32.html language=enus -->
## TOPIC 00035: Advanced:Subspan Overlap Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr32.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr32.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Subspan Overlap Property

**Short Name:**Subspan Overlap

Property of [RFmxInstr](crfmxinstr.html)

Specifies the amount of overlap between consecutive subspans in a multispan spectrum acquisition. Overlapping subspans can reduce the power level of spurs in the acquired data. The value you specify determines the amount of shift as a percentage of subspan width.

Specifying a value of 0 disables subspan overlap. In this case, the RFmx driver uses either a single-span acquisition or a multispan acquisition without overlap, depending on the frequency range requested and the current device settings.

Specifying a value greater than 0 causes the RFmx driver to use a multispan acquisition with the specified overlap even in situations in which it would normally use a single-span acquisition. The RFmx driver acquires data within the overlapped percentage and uses the minimum of the acquired values.

|  | Note RFmx may apply further shifts to the specified value to accommodate fixed-frequency edges of components such as preselectors. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.

**Valid values**

| PXIe-5820/5830/5831/5832/5840/5841 | 0 |
| --- | --- |
| PXIe-5842 | 0, 50 |
| PXIe-5665/5668 | 0 to <100 |

**Supported devices**: PXIe-5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr34.html language=enus -->
## TOPIC 00036: Advanced:Downconverter Gain (dB) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr34.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr34.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Downconverter Gain (dB) Property

**Short Name:**Downconverter Gain (dB)

Property of [RFmxInstr](crfmxinstr.html)

Returns the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this property.

For a vector signal analyzer (VSA), the system is defined as the RF downconverter for all interfaces between the RF IN connector on the RF downconverter front panel and the IF IN connector on the digitizer front panel. For a spectrum monitoring receiver, the system is defined as the RF preselector, RF downconverter, and IF conditioning modules including all interfaces between the RF IN connector on the RF preselector module front panel and the IF IN connector on the digitizer front panel.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is N/A.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr35.html language=enus -->
## TOPIC 00037: LO:Downconverter Frequency Offset (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr35.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr35.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:Downconverter Frequency Offset (Hz) Property

**Short Name:**Downconverter Frequency Offset (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies an offset from the center frequency value for the downconverter. Use this property to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this property to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz.

NI recommends using the [LO Leakage Avoidance Enabled](attr37.html) property instead of the Downconverter Frequency Offset property. The LO Leakage Avoidance Enabled property automatically configures the Downconverter Frequency Offset property to an appropriate offset based on the bandwidth or span of the measurement.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default values:** For spectrum acquisition types, the RFmx driver automatically calculates the default value to avoid residual LO power. For I/Q acquisition types, the default value is 0 Hz. If the center frequency is set to a non-multiple of [LO Frequency Step Size](attr5f.html) property, this property is set to compensate for the difference.

The following valid values correspond to their respective devices:

| PXIe-5646 | -100 MHz to +100 MHz |
| --- | --- |
| PXIe-5830/5831/5832/5840/5841 | -500 MHz to +500 MHz |
| PXIe-5842 | -1 GHz to +1 GHz |
| Other devices | -42 MHz to +42 MHz |

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr36.html language=enus -->
## TOPIC 00038: Advanced:RF Attenuation Step Size (dB) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr36.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr36.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:RF Attenuation Step Size (dB) Property

**Short Name:**RF Attenuation Step Size (dB)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default values**:

| PXIe-5601/5663/5663E | 0.0 |
| --- | --- |
| PXIe-5603/5665 (3.6 GHz) | 1.0 |
| PXIe-5605/5665 (14 GHz), PXIe-5606/5668 | 5.0 |

**Valid values**:

| PXIe-5601/5663/5663E | 0.0 to 93.0, continuous |
| --- | --- |
| PXIe-5603/5665 (3.6 GHz) | 1.0 to 74.0, in 1 dB steps |
| PXIe-5605/5665 (14 GHz) (low band), PXIe-5606/5668 (low band) | 1.0 to 106.0, in 1 dB steps |
| PXIe-5605/5665 (14 GHz) (high band), PXIe-5606/5668 (high band) | 5.0 to 75.0, in 5 dB steps |

**Supported devices**: PXIe-5663, PXIe-5665, PXIe-5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr37.html language=enus -->
## TOPIC 00039: LO:LO Leakage Avoidance Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr37.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr37.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Leakage Avoidance Enabled Property

**Short Name:**LO Leakage Avoidance Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition.

This property is ignored if:

- the bandwidth required by the measurement is more than the available instrument bandwidth after offsetting the LO.
- you set the Downconverter Center Frequency or Downconverter Frequency Offset properties.

|  | Note When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set this property to False when the LO Source property is set to Automatic_SG_SA_Shared. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value for PXIe-5830/5831/5832/5840/5841/5842 is **True**, else the default value is **False**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

| False (0) | RFmx does not modify the Downconverter Frequency Offset property. |
| --- | --- |
| True (1) | RFmx calculates the required LO offset based on the measurement configuration and appropriately sets the Downconverter Frequency Offset property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr38.html language=enus -->
## TOPIC 00040: Advanced:Amplitude Settling Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr38.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr38.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Amplitude Settling Property

**Short Name:**Amplitude Settling

Property of [RFmxInstr](crfmxinstr.html)

Specifies the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate VI.

Any specified amplitude settling value that is above the acceptable minimum value is coerced down to the closest valid value.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr39.html language=enus -->
## TOPIC 00041: Recommended Settings:Center Frequency (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr39.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr39.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Recommended Settings:Center Frequency (Hz) Property

**Short Name:**Recommended Center Frequency (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Returns the recommended center frequency of the RF signal. This value is expressed in Hz.

|  | Note This property is supported only when: RFmxInstr Initialize NIRFSA VI or the RFmxInstr Initialize VI is called with option string "AnalysisOnly=1", or RFmxInstr Initialize NIRFSA (Array) VI is called with option string "AnalysisOnly=1;MaxNumWfms:<n>". Use "instr<n>" as the selector string to read this property. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr3a.html language=enus -->
## TOPIC 00042: LO:LO2 Export Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr3a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr3a.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO2 Export Enabled Property

**Short Name:**LO2 Export Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether to enable the LO2 OUT terminals in the installed devices.

Set this property to **Enabled** to export the 4 GHz LO signal from the LO2 IN terminal to the LO2 OUT terminal. You can also export the LO2 signal by setting the [LO Export Enabled](attr21.html) property to TRUE.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Disabled**.

**Supported Devices:** PXIe-5665/5668

| Disabled (0) | Disables the LO2 OUT terminals. |
| --- | --- |
| Enabled (1) | Enables the LO2 OUT terminals. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr3b.html language=enus -->
## TOPIC 00043: LO:LO Source Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr3b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr3b.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Source Property

**Short Name:**LO Source

Property of [RFmxInstr](crfmxinstr.html)

Specifies the local oscillator (LO) signal source used to downconvert the RF input signal.

If this property is set to "" (empty string), RFmx uses the internal LO source. For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

If no signal downconversion is required, this property is ignored.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Onboard**.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

| None (None) | Specifies that no LO source is required to downconvert the RF input signal. |
| --- | --- |
| Onboard (Onboard) | Specifies that the onboard synthesizer is used to generate the LO signal that downconverts the RF input signal. PXIe-5831: This configuration uses the onboard LO of the PXIe-3622, using the LO2 stage. PXIe-5831 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3622. PXIe-5832: This configuration uses the onboard LO of the PXIe-3623, using the LO2 stage. PXIe-5832 with PXIe-5653: This configuration uses the onboard LO of the PXIe-5653 when associated with the PXIe-3623. PXIe-5840 with PXIe-5653: If the center frequency is greater than or equal to 3.2 GHz, this configuration uses the PXIe-5653 LO source. For frequencies less than 3.2 GHz, this configuration uses the PXIe-5840 internal LO. If RFmx is operating in Spectrum mode, this configuration uses the PXIe-5840 internal LO regardless of the frequency. PXIe-5842: This configuration uses the onboard LO of the PXIe-5655. |
| LO_In (LO_In) | Specifies that the LO source used to downconvert the RF input signal is connected to the LO IN connector on the front panel. |
| Secondary (Secondary) | Specifies that the LO source uses the PXIe-5830/5831/5832/5840 internal LO. This value is valid on only the PXIe-5840 with PXIe-5653, PXIe-5831 with PXIe-5653 (LO1 stage only), or PXIe-5832 with PXIe-5653 (LO1 stage only). |
| SG_SA_Shared (SG_SA_Shared) | Specifies that the internal LO can be shared between RFmx and RFSG sessions. RFmx selects an internal synthesizer and the synthesizer signal is switched to both the RX and TX mixers. This value is valid only on PXIe-5830/5831/5832/5841/5842. |
| Automatic_SG_SA_Shared (Automatic_SG_SA_Shared) | Specifies whether RFmx automatically configures the signal analyzer to use the LO utilized by the signal generator on the same vector signal transceiver (VST) based on the configured measurements. When using instruments that do not have LOs with excellent phase noise and to minimize the contribution of the instrument's phase noise affecting your measurements, NI recommends to share the LO between the signal generator (SG) and the signal analyzer (SA). This value is recommended in test setups that use a VST with NI-RFSG to generate a signal at the DUT's input and RFmx to measure the signal at the DUT's output. This value automatically: determines whether the SG LO can be shared with SA based on the test instrument used, selected measurement, and the measurement settings. configures instrument specific properties on SA to share the LO between the generator and analyzer, whenever possible. To enable automatically sharing SG LO with SA, you must first setup the required device specific physical connections mentioned below and then follow the steps in the recommended order. PXIe-5840/5841/5842: SG LO is shared with SA via an external path. Hence, you must connect RF Out LO Out to RF In LO In using a cable. PXIe-5830/5831/5832: SG LO is shared with SA via an internal path. Hence, an external cable connection is not required. NI recommends the following order of steps: Set LO Source property to Automatic SG SA Shared in NI-RFSG (or enable Automatic SG SA shared LO on NI-RFSG Playback Library). Set LO Source property to Automatic_SG_SA_Shared in RFmx. Configure any additional settings on RFSG and RFmx, including selecting waveforms. Initiate RFSG. Initiate RFmx. Note When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. Examples Refer to following VIs for examples in RFmx WLAN and RFmx NR that show the behavior of Automatic SG SA Shared LO. <LabVIEW directory>\\examples\\RFmx\\WLAN\\RFmxWLAN FEM Test with Automatic SG SA Shared LO.vi <LabVIEW directory>\\examples\\RFmx\\NR\\RFmxNR FEM Test with Automatic SG SA Shared LO.vi This value is valid only on PXIe-5830/5831/5832/5840/5841/5842. |
|  | Note When using a DPD applied signal for performing measurements like ModAcc, PvT, or TXP, you must set the LO Leakage Avoidance Enabled property to False and LO Source property to Automatic_SG_SA_Shared. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr3c.html language=enus -->
## TOPIC 00044: LO:LO Frequency (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr3c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr3c.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Frequency (Hz) Property

**Short Name:**LO Frequency (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz.

If you are using the vector signal analyzer with an external LO, use this property to specify the LO frequency that the external LO source passes into the LO IN or LO1 IN connector on the RF downconverter front panel. If you are using an external LO, reading the value of this property after configuring the rest of the parameters returns the LO frequency needed by the device.

You can set this property to the actual LO frequency because RFmx corrects for any difference between expected and actual LO frequencies.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the Selector Strings topic for information about the string syntax.

The default value is 0.

**Supported Devices:** PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr4.html language=enus -->
## TOPIC 00045: RF Attenuation:Auto Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr4.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr4.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

RF Attenuation:Auto Property

**Short Name:**RF Attenuation Auto

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the RFmx driver computes the RF attenuation.

If you set this property to **True**, the RFmx driver chooses an attenuation setting based on the reference level configured on the personality.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **True**.

**Supported devices**: PXIe-5663/5663E, PXIe-5665/5668

| False (0) | Specifies that the RFmx driver uses the value configured using RF Attenuation Value property. |
| --- | --- |
| True (1) | Specifies that the RFmx driver computes the RF attenuation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure RF Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr41.html language=enus -->
## TOPIC 00046: Selector String Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr41.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr41.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Selector String Property

**Short Name:**Selector String

Property of [RFmxInstr](crfmxinstr.html)

Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node.

When there are multiple instances of a property, you must specify the property instance to configure or read by using the Selector String property in a property node.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Write Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr44.html language=enus -->
## TOPIC 00047: MIMO:LO Sharing Mode Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr44.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr44.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

MIMO:LO Sharing Mode Property

**Short Name:**LO Sharing Mode

Property of [RFmxInstr](crfmxinstr.html)

Specifies the RFmx session with the respective LO sharing mode.

The following figures illustrate different connection configuration topologies for different LO Sharing modes.

You must set the [Num LO Sharing Groups](attr61.html) property to 1 for the following LO connection configurations.

[IMAGE alt='image' src='fig1.png']

[IMAGE alt='image' src='fig2.png']

You must set the Num LO Sharing Groups property to 2 for the following LO connection configurations.

[IMAGE alt='image' src='fig3.png']

[IMAGE alt='image' src='fig4.png']

The default value is **Disabled**.

| Disabled (0) | LO Sharing is disabled. |
| --- | --- |
| External Star (3) | The LO connection configuration is configured as External Star. |
| External Daisy Chain (4) | The LO connection configuration is configured as External Daisy Chain. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr46.html language=enus -->
## TOPIC 00048: Advanced:Common Mode Level (V) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr46.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr46.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Common Mode Level (V) Property

**Short Name:**Common Mode Level (V)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.

**Supported devices**: PXIe-5820

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr47.html language=enus -->
## TOPIC 00049: Advanced:SMU Resource Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr47.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr47.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:SMU Resource Name Property

**Short Name:**SMU Resource Name

Property of [RFmxInstr](crfmxinstr.html)

Specifies the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name.

**Supported devices:** PXIe-4138, PXIe-4139, PXIe-4139 (40 W), and PXIe-4143 SMUs.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr48.html language=enus -->
## TOPIC 00050: Advanced:SMU Channel Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr48.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr48.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:SMU Channel Property

**Short Name:**SMU Channel

Property of [RFmxInstr](crfmxinstr.html)

Specifies the output channel to be used for noise figure (NF) measurement in RFmx.

The default value is 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr4d.html language=enus -->
## TOPIC 00051: Advanced:Overflow Error Reporting Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr4d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr4d.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Overflow Error Reporting Property

**Short Name:**Overflow Error Reporting

Property of [RFmxInstr](crfmxinstr.html)

Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Warning**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5840/5841/5842

| Warning (0) | RFmx returns a warning when an ADC or an onboard signal processing (OSP) overflow occurs. |
| --- | --- |
| Disabled (1) | RFmx does not return an error or a warning when an ADC or OSP overflow occurs. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr4e.html language=enus -->
## TOPIC 00052: LO:LO In Power (dBm) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr4e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr4e.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO In Power (dBm) Property

**Short Name:**LO In Power (dBm)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the power level expected at the LO IN terminal when the [LO Source](attr3b.html) property is set to **LO_In**. This value is expressed in dBm.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

|  | Note For PXIe-5644/5645/5646, this property is always read-only. |
| --- | --- |

The default value is 0.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr4f.html language=enus -->
## TOPIC 00053: LO:LO Out Power (dBm) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr4f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr4f.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Out Power (dBm) Property

**Short Name:**LO Out Power (dBm)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the power level of the signal at the LO OUT terminal when the [LO Export Enabled](attr21.html) property is set to TRUE. This value is expressed in dBm.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr5.html language=enus -->
## TOPIC 00054: RF Attenuation:Value (dB) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr5.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr5.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

RF Attenuation:Value (dB) Property

**Short Name:**RF Attenuation (dB)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB.

The RFmx driver uses the value of this property as the attenuation setting when you set the [RF Attenuation Auto](attr4.html) property to **False**.

| PXIe-5663/5663E | You can change the attenuation value to modify the amount of noise and distortion. Higher attenuation levels increase the noise level but decreases distortion; lower attenuation levels decrease the noise level but increases distortion. |
| --- | --- |
| PXIe-5603/5605/5665/5668 | Refer to the PXIe-5665 or the PXIe-5668 RF Attenuation and Signal Levels topic in the NI RF Vector Signal Analyzers Help for more information about configuring attenuation. |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The valid values for this property depend on the device configuration.

**Supported devices**: PXIe-5663/5663E/5603/5605/5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure RF Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr50.html language=enus -->
## TOPIC 00055: LO:VCO Frequency Step Size (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr50.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr50.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:VCO Frequency Step Size (Hz) Property

**Short Name:**LO VCO Freq Step Size (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz.

|  | Note Do not set this property with the LO Frequency Step Size property. |
| --- | --- |

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 1 MHz.

**Supported devices**: PXIe-5830/5831/5832

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr5a.html language=enus -->
## TOPIC 00056: LO:LO PLL Fractional Mode Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr5a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr5a.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO PLL Fractional Mode Property

**Short Name:**LO PLL Fractional Mode

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether to use fractional mode for the LO phase-locked loop (PLL).

Fractional mode provides a finer frequency step resolution, but may result in non harmonic spurs. Refer to the specifications document of your device for more information about fractional mode and non harmonic spurs.

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

|  | Note The LO PLL Fractional Mode attribute is applicable only when using the internal LO. |
| --- | --- |

|  | Note For PXIe-5831 with PXIe-5653, PXIe-5832 with PXIe-5653, this property is ignored if the PXIe-5653 is used as the LO source. |
| --- | --- |

The default value is **Enabled**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

| Disabled (0) | Indicates that the property is disabled. |
| --- | --- |
| Enabled (1) | Indicates that the property is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr5b.html language=enus -->
## TOPIC 00057: Advanced:Optimize Path For Signal Bandwidth Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr5b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr5b.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Optimize Path For Signal Bandwidth Property

**Short Name:**Optimize Path For Signal Bandwidth

Property of [RFmxInstr](crfmxinstr.html)

Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency.

You can disable this property to avoid changes to the RF path when changing the signal bandwidth.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Automatic**.

**Supported devices**: PXIe-5830/5831/5832/5841/5842

| Disabled (0) | Disables the optimized path for signal bandwidth. |
| --- | --- |
| Enabled (1) | Enables the optimized path for signal bandwidth. |
| Automatic (2) | Automatically enables the optimized path based on other configurations. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr5c.html language=enus -->
## TOPIC 00058: Advanced:Input Isolation Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr5c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr5c.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Input Isolation Enabled Property

**Short Name:**Input Isolation Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether input isolation is enabled.

Enabling this property isolates the input signal at the RF IN connector on the RF downconverter from the rest of the RF downconverter signal path. Disabling this property reintegrates the input signal into the RF downconverter signal path.

|  | Note If you enable input isolation for your device, the device impedance is changed from the characteristic 50-ohm impedance. A change in the device impedance may increase the VSWR value higher than the device specifications. |
| --- | --- |

For PXIe-5830/5831/5832, input isolation is supported for all available ports for your hardware configuration.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Disabled**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Disabled (0) | Indicates that the property is disabled. |
| --- | --- |
| Enabled (1) | Indicates that the property is enabled. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr5e.html language=enus -->
## TOPIC 00059: Advanced:Thermal Correction Headroom Range (deg C) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr5e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr5e.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Thermal Correction Headroom Range (deg C) Property

**Short Name:**Thermal Correction Headroom Range (deg C)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the expected thermal operating range of the instrument from the self-calibration temperature returned from the [Device Temperature](attr18.html) property. This value is expressed in degree Celsius.

For example, if this property is set to 5.0, and the device is self-calibrated at 35 degrees Celsius, then you can expect to run the device from 30 degrees Celsius to 40 degrees Celsius with corrected accuracy and no overflows. Setting this property with a smaller value can result in improved dynamic range, but you must ensure thermal stability while the instrument is running. Operating the instrument outside of the specified range may cause degraded performance and ADC or DSP overflows.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default value**

| PXIe-5830/5831/5832/5842 | 5 |
| --- | --- |
| PXIe-5840/5841 | 10 |

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr5f.html language=enus -->
## TOPIC 00060: LO:LO Frequency Step Size (Hz) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr5f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr5f.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:LO Frequency Step Size (Hz) Property

**Short Name:**LO Freq Step Size (Hz)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the step size for tuning the LO phase-locked loop (PLL).

You can only tune the LO frequency in multiples of the LO Frequency Step Size property. Therefore, the LO frequency can be offset from the requested center frequency by as much as half of the LO Frequency Step Size property. This offset is corrected by digitally frequency shifting the LO frequency to the value requested in [Downconverter Center Frequency](../rfmxinstrprop/attrd.html) property.

|  | Note For PXIe-5831 with PXIe-5653, PXIe-5832 with PXIe-5653, this property is ignored if PXIe-5653 is used as the LO source. |
| --- | --- |

The valid values for this property depend on the [LO PLL Fractional Mode](attr5a.html) property.

**PXIe-5644/5645/5646:** If you set the LO PLL Fractional Mode property to **Disabled**, the specified value is coerced to the nearest valid value.

**PXIe-5840:** If you set the LO PLL Fractional Mode property to **Disabled**, the specified value is coerced to the nearest valid value that is less than or equal to the desired step size.

| LO PLL Fractional Mode Enabled Property Setting | LO Frequency Step Size Property Valid Values on PXIe-5644/5645 | LO Frequency Step Size Property Valid Values on PXIe-5646 | LO Frequency Step Size Property Valid Values on PXIe-5840/5841 | LO Frequency Step Size Property Valid Values on PXIe-5830/5831/5832 | LO Frequency Step Size Property Valid Values on PXIe-5841 with PXIe-5655, PXIe-5842* |  |
| --- | --- | --- | --- | --- | --- | --- |
| LO1 | LO2 |  |  |  |  |  |
| Enabled | 50 kHz to 24 MHz | 50 kHz to 25 MHz | 50 kHz to 100 MHz | 8 Hz to 400 MHz | 4 kHz to 400 MHz | 1 nHz to 50 MHz |
| Disabled | 4 MHz, 5 MHz, 6 MHz, 12 MHz, 24 MHz | 2 MHz, 5 MHz, 10 MHz, 25 MHz | 1 MHz, 5 MHz, 10 MHz, 25 MHz, 50 MHz, 100 MHz | -- | -- |  |

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default values**

| PXIe-5644/5645/5646 | 200 kHz |
| --- | --- |
| PXIe-5830 | 2 MHz |
| PXIe-5831/5832 (RF port) | 8 MHz |
| PXIe-5831/5832 (IF port) | 2 MHz, 4 MHz |
| PXIe-5840/5841 | 500 kHz |
| PXIe-5842 | 1 Hz |

|  | Note The default value for PXIe-5831/5832 depends on the frequency range of the selected port for your instrument configuration. Use RFmxInstr Get Available Ports VI to get the valid port names. |
| --- | --- |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6.html language=enus -->
## TOPIC 00061: Mechanical Attenuation:Auto Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Mechanical Attenuation:Auto Property

**Short Name:**Mechanical Attenuation Auto

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **True**.

**Supported devices**: PXIe-5663/5663E/5665/5668

| False (0) | Specifies that the RFmx driver uses the value configured in the Mechanical Attenuation Value property. |
| --- | --- |
| True (1) | Specifies that the measurement computes the mechanical attenuation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Mechanical Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr61.html language=enus -->
## TOPIC 00062: MIMO:Number of LO Sharing Groups Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr61.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr61.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

MIMO:Number of LO Sharing Groups Property

**Short Name:**Num LO Sharing Groups

Property of [RFmxInstr](crfmxinstr.html)

Specifies the RFmx session with the number of LO sharing groups.

The default value is 1.

The valid values are 1 and 2.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr62.html language=enus -->
## TOPIC 00063: Trigger:Start:Type Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr62.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr62.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Start:Type Property

**Short Name:**Start Trigger Type

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the start trigger is a digital edge or a software trigger.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| None (0) | No start trigger is configured. |
| --- | --- |
| Digital Edge (1) | The start trigger is not asserted until a digital edge is detected. The source of the digital edge is specified by the Start Trigger Digital Edge Source property. |
| Software (3) | The start trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr Send Software Edge Trigger VI. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr63.html language=enus -->
## TOPIC 00064: Trigger:Start:Digital Edge:Source Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr63.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr63.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Start:Digital Edge:Source Property

**Short Name:**Start Trigger Digital Edge Source

Property of [RFmxInstr](crfmxinstr.html)

Specifies the source terminal for the start trigger. This property is used only when you set the [Start Trigger Type](../rfmxinstrprop/attr62.html) property to **Digital Edge**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value of this property is "" (empty string).

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| PFI0 (PFI0) | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 (PFI1) | The trigger is received on PFI 1. |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842 and for digital edge advance triggers on PXIe-5663E/5665. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr64.html language=enus -->
## TOPIC 00065: Trigger:Start:Digital Edge:Edge Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr64.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr64.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Start:Digital Edge:Edge Property

**Short Name:**Start Trigger Digital Edge

Property of [RFmxInstr](crfmxinstr.html)

Specifies the active edge for the start trigger. This property is used only when you set the [Start Trigger Type](../rfmxinstrprop/attr62.html) property to **Digital Edge**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Rising Edge**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Rising Edge (0) | The trigger asserts on the rising edge of the signal. |
| --- | --- |
| Falling Edge (1) | The trigger asserts on the falling edge of the signal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr65.html language=enus -->
## TOPIC 00066: Trigger:Start:Export Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr65.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr65.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Start:Export Output Terminal Property

**Short Name:**Start Trigger Export Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the exported start trigger.

You can also choose not to export any signal.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on PXIe-5652, and the REF OUT terminal on PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr66.html language=enus -->
## TOPIC 00067: Trigger:Start:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr66.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr66.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Start:Terminal Name Property

**Short Name:**Start Trigger Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/StartTrigger , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/StartTrigger , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/StartTrigger , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr67.html language=enus -->
## TOPIC 00068: Trigger:Advance:Type Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr67.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr67.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Advance:Type Property

**Short Name:**Advance Trigger Type

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the advance trigger is a digital edge or a software trigger.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **None**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| None (0) | No advance trigger is configured. |
| --- | --- |
| Digital Edge (1) | The advance trigger is not asserted until a digital edge is detected. The source of the digital edge is specified with the Advance Trigger Digital Edge Source property. |
| Software (3) | The advance trigger is not asserted until a software trigger occurs. You can assert the software trigger by calling the RFmxInstr Send Software Edge Trigger VI. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr68.html language=enus -->
## TOPIC 00069: Trigger:Advance:Digital Edge:Source Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr68.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr68.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Advance:Digital Edge:Source Property

**Short Name:**Advance Trigger Digital Edge Source

Property of [RFmxInstr](crfmxinstr.html)

Specifies the source terminal for the advance trigger.

This property is used only when the [Advance Trigger Type](../rfmxinstrprop/attr67.html) property is set to **Digital Edge**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value of this property is "" (empty string).

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| PFI0 (PFI0) | The trigger is received on PFI 0. |
| --- | --- |
| PFI1 (PFI1) | The trigger is received on PFI 1. |
| PXI_Trig0 (PXI_Trig0) | The trigger is received on PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | The trigger is received on PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | The trigger is received on PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | The trigger is received on PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | The trigger is received on PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | The trigger is received on PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | The trigger is received on PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | The trigger is received on PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | The trigger is received on the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarB (PXIe_DStarB) | The trigger is received on the PXIe DStar B trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |
| TimerEvent (TimerEvent) | The trigger is received from the timer event. This value is valid only for PXIe-5820/5840/5841/5842 and for digital edge advance triggers on PXIe-5663E/5665. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr69.html language=enus -->
## TOPIC 00070: Trigger:Advance:Export Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr69.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr69.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Advance:Export Output Terminal Property

**Short Name:**Advance Trigger Export Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the exported advance trigger.

You can also choose not to export any signal.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | TExports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6a.html language=enus -->
## TOPIC 00071: Trigger:Advance:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6a.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6a.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Trigger:Advance:Terminal Name Property

**Short Name:**Advance Trigger Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/AdvanceTrigger , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/AdvanceTrigger , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/AdvanceTrigger , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6b.html language=enus -->
## TOPIC 00072: Event:Ready For Start:Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6b.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6b.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Ready For Start:Output Terminal Property

**Short Name:**Ready For Start Event Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the Ready for Start event.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6c.html language=enus -->
## TOPIC 00073: Event:Ready For Start:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6c.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6c.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Ready For Start:Terminal Name Property

**Short Name:**Ready For Start Event Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/ReadyForStartEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/ReadyForStartEvent , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/ReadyForStartEvent , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6d.html language=enus -->
## TOPIC 00074: Event:Ready For Advance:Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6d.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6d.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Ready For Advance:Output Terminal Property

**Short Name:**Ready For Advance Event Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the Ready for Advance event.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6e.html language=enus -->
## TOPIC 00075: Event:Ready For Advance:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6e.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6e.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Ready For Advance:Terminal Name Property

**Short Name:**Ready For Advance Event Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/ReadyForAdvanceEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/ReadyForAdvanceEvent , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/ReadyForAdvanceEvent , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr6f.html language=enus -->
## TOPIC 00076: Event:Ready For Reference:Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr6f.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr6f.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Ready For Reference:Output Terminal Property

**Short Name:**Ready For Reference Event Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the Ready for Reference event.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr7.html language=enus -->
## TOPIC 00077: Mechanical Attenuation:Value (dB) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr7.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr7.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Mechanical Attenuation:Value (dB) Property

**Short Name:**Mechanical Attenuation (dB)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB.

The RFmx driver uses the value of this property as the attenuation setting when you set the [Mechanical Attenuation Auto](attr6.html) property to **False**.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Valid values**

| PXIe-5663/5663E | 0, 16 |
| --- | --- |
| PXIe-5665 (3.6 GHz) | 0, 10, 20, 30 |
| PXIe-5665 (14 GHz), PXIe-5668 | 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75 |

**Supported devices**: PXIe-5663/5663E, PXIe-5665, PXIe-5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | RFmxInstr Configure Mechanical Attenuation |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr70.html language=enus -->
## TOPIC 00078: Event:Ready For Reference:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr70.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr70.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Ready For Reference:Terminal Name Property

**Short Name:**Ready For Reference Event Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/ReadyForReferenceEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/ReadyForReferenceEvent , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/ReadyForReferenceEvent , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr71.html language=enus -->
## TOPIC 00079: Event:End Of Record:Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr71.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr71.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:End Of Record:Output Terminal Property

**Short Name:**End Of Record Event Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the End of Record event.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr72.html language=enus -->
## TOPIC 00080: Event:End Of Record:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr72.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr72.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:End Of Record:Terminal Name Property

**Short Name:**End Of Record Event Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/EndOfRecordEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/EndOfRecordEvent , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/EndOfRecordEvent , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr73.html language=enus -->
## TOPIC 00081: Event:Done:Output Terminal Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr73.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr73.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Done:Output Terminal Property

**Short Name:**Done Event Output Terminal

Property of [RFmxInstr](crfmxinstr.html)

Specifies the destination terminal for the Done event.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Do not export signal**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

| Do not export signal () | Does not export the signal. |
| --- | --- |
| ClkOut (ClkOut) | Exports the signal to the CLK OUT connector on the PXIe-5622/5624 front panel. |
| RefOut (RefOut) | Exports the signal to the REF IN/OUT terminal on the PXIe-5652, and the REF OUT terminal on the PXIe-5644/5645/5646 and PXIe-5820/5830/5831/5832/5840/5841/5842. |
| RefOut2 (RefOut2) | Exports the signal to the REF OUT2 terminal on the LO. This connector exists only on PXIe-5652. |
| PFI0 (PFI0) | Exports the signal to the PFI 0 connector. |
| PFI1 (PFI1) | Exports the signal to the PFI 1 connector on PXIe-5142 and PXIe-5622. |
| PXI_Trig0 (PXI_Trig0) | Exports the signal to the PXI trigger line 0. |
| PXI_Trig1 (PXI_Trig1) | Exports the signal to the PXI trigger line 1. |
| PXI_Trig2 (PXI_Trig2) | Exports the signal to the PXI trigger line 2. |
| PXI_Trig3 (PXI_Trig3) | Exports the signal to the PXI trigger line 3. |
| PXI_Trig4 (PXI_Trig4) | Exports the signal to the PXI trigger line 4. |
| PXI_Trig5 (PXI_Trig5) | Exports the signal to the PXI trigger line 5. |
| PXI_Trig6 (PXI_Trig6) | Exports the signal to the PXI trigger line 6. |
| PXI_Trig7 (PXI_Trig7) | Exports the signal to the PXI trigger line 7. |
| PXI_STAR (PXI_STAR) | Exports the signal to the PXI star trigger line. This value is not valid for PXIe-5644/5645/5646. |
| PXIe_DStarC (PXIe_DStarC) | Exports the signal to the PXIe DStar C trigger line. This value is valid only for PXIe-5820/5830/5831/5832/5840/5841/5842. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr74.html language=enus -->
## TOPIC 00082: Event:Done:Terminal Name Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr74.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr74.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Event:Done:Terminal Name Property

**Short Name:**Done Event Terminal Name

Property of [RFmxInstr](crfmxinstr.html)

Returns the fully qualified signal name as a string.

The standard format is as follows:

- PXIe-5820/5840/5841/5842 : /ModuleName/ai/0/DoneEvent , where ModuleName is the name of your device in MAX.
- PXIe-5830/5831/5832 : /BasebandModule/ai/0/DoneEvent , where BasebandModule is the name of your device in MAX.
- All other devices : /DigitizerName/DoneEvent , where DigitizerName is the name of your associated digitizer module in MAX.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | No |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr75.html language=enus -->
## TOPIC 00083: Advanced:Self Calibration:Self Cal Validity Check Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr75.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr75.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Self Calibration:Self Cal Validity Check Property

**Short Name:**Self Cal Validity Check

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the RFmx driver validates the self-calibration data.

You can specify the time interval required to perform the check using the [Self Cal Validity Check Time Interval](../rfmxinstrprop/attr76.html) property.

NI recommends to perform self-calibration using the [RFmxInstr Self Calibrate](/csh?topicname=rfmxinstrvi/rfmxinstr_self_calibrate.html) VI when RFmx reports an invalid self-calibration data warning.

|  | Note The RFmx driver does not consider self-calibration range data during self calibration validity check. |
| --- | --- |

The default value is **Off**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5833/5840/5841/5842

| Off (0) | Indicates that RFmx does not check whether device self-calibration data is valid. |
| --- | --- |
| Enabled (1) | Indicates that RFmx checks whether device self-calibration data is valid and reports a warning from the RFmx Commit and RFmx Initiate VIs when the data is invalid. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr76.html language=enus -->
## TOPIC 00084: Advanced:Self Calibration:Self Cal Validity Check Time Interval (s) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr76.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr76.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Self Calibration:Self Cal Validity Check Time Interval (s) Property

**Short Name:**Self Cal Validity Check Time Interval (s)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds.

When you call RFmx Commit or Initiate VIs by enabling the [Self Cal Validity Check](../rfmxinstrprop/attr75.html) property, the RFmx driver checks if the amount of time specified by the Self Calibration Validity Check Time Interval property has elapsed before validating the calibration data.

The default value is 30 seconds.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5820/5830/5831/5832/5833/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr77.html language=enus -->
## TOPIC 00085: Advanced:Temperature Read Interval (s) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr77.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr77.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Temperature Read Interval (s) Property

**Short Name:**Temperature Read Interval (s)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds.

When you call the RFmx Initiate VI, RFmx checks if the amount of time specified by this property has elapsed before reading the hardware temperature.

|  | Note RFmx ignores Temperature Read Interval property if you read the Downconverter Gain property. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 30 seconds.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr78.html language=enus -->
## TOPIC 00086: Advanced:Thermal Correction Temperature Resolution (deg C) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr78.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr78.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Thermal Correction Temperature Resolution (deg C) Property

**Short Name:**Thermal Correction Temperature Resolution (deg C)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

**Default value**

| PXIe-5830/5831/5832/5842 | 0.2 |
| --- | --- |
| PXIe-5840/5841 | 1.0 |

**Supported devices**: PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr8.html language=enus -->
## TOPIC 00087: LO:Tuning Speed Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr8.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr8.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:Tuning Speed Property

**Short Name:**Tuning Speed

Property of [RFmxInstr](crfmxinstr.html)

Makes tradeoffs between tuning speed and phase noise.

|  | Note This property is not supported if you are using an external LO. |
| --- | --- |

For PXIe-5830/5831/5832, if you want to configure or read on LO1 or LO2 channel, use "lo1" or "lo2" as part of the selector string. You do not need to use a selector string or use "lo1, lo2" as part of the selector string if you want to configure this property for both channels. You can also use [RFmxInstr Build LO String](/csh?topicname=rfmxinstrvi/rfmxinstr_build_lo_string.html) utility function to create the LO String. For all other devices, lo channel string is not allowed.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read on that signal instance. Refer to the [Selector string](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

|  | Note The PXIe-5830/5831/5832/5840/5841/5842 supports only Medium for this property. |
| --- | --- |

**Default value**: **Normal** for PXIe-5663/5663E/5665/5668, **Medium** for PXIe-5644/5645/5646 and PXIe-5830/5831/5832/5840/5841/5842

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

| Normal (0) | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an underdamped response. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a narrow loop bandwidth. |
| --- | --- |
| Medium (1) | Specifies that the RF downconverter module uses a medium loop bandwidth. This value is not supported on PXIe-5663/5663E/5665/5668 devices. |
| Fast (2) | PXIe-5665/5668: Adjusts the YIG main coil on the LO for an overdamped response. Setting this property to Fast allows the frequency to settle significantly faster for some frequency transitions at the expense of increased phase noise. PXIe-5663/5663E/5644/5645/5646: Specifies that the RF downconverter module uses a wide loop bandwidth. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr80.html language=enus -->
## TOPIC 00088: Advanced:Number of Raw IQ Records Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr80.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr80.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Number of Raw IQ Records Property

**Short Name:**Num Raw IQ Records

Property of [RFmxInstr](crfmxinstr.html)

Returns the number of raw IQ records to acquire to complete measurement averaging.

|  | Note This property returns a value of 0 when RFmx cannot provide I/Q data for the specified measurement configuration. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attr9.html language=enus -->
## TOPIC 00089: Advanced:Frequency Settling Units Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attr9.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attr9.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Frequency Settling Units Property

**Short Name:**Freq Settling Units

Property of [RFmxInstr](crfmxinstr.html)

Specifies the delay duration units and interpretation for LO settling.

Specify the actual settling value using the [Frequency Settling](attra.html) property.

|  | Note The Frequency Settling Units property is not supported if you are using an external LO. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **PPM**.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

| PPM (0) | Specifies the frequency settling in parts per million (ppm). |
| --- | --- |
| Seconds After Lock (1) | Specifies the frequency settling in time after lock (seconds). |
| Seconds After I/O (2) | Specifies the frequency settling in time after I/O (seconds). |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attra.html language=enus -->
## TOPIC 00090: Advanced:Frequency Settling Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attra.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attra.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Frequency Settling Property

**Short Name:**Freq Settling

Property of [RFmxInstr](crfmxinstr.html)

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

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0.1.

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attra3.html language=enus -->
## TOPIC 00091: Load Configurations: Load Options Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attra3.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attra3.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Load Configurations: Load Options Property

**Short Name:**Load Options

Property of [RFmxInstr](crfmxinstr.html)

Specifies the configurations to skip while loading from a file using the [RFmxInstr Load Configurations](/csh?topicname=rfmxinstrvi/rfmxinstr_load_configurations.html)VI .

The default value is an empty array.

| Skip None (0) | RFmx loads all the configurations to the session. |
| --- | --- |
| Skip RFInstr (1) | RFmx skips loading the RFmxInstr configurations to the session. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attrb.html language=enus -->
## TOPIC 00092: Advanced:Channel Coupling Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attrb.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attrb.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Channel Coupling Property

**Short Name:**Channel Coupling

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter.

|  | NoteFor the PXIe-5665/5668, this property must be set to AC Coupled when the DC block is present, and set to DC Coupled when the DC block is not present to ensure device specifications are met and proper calibration data is used. For more information about removing or attaching the DC block, refer to the PXIe-5665 Theory of Operation or the PXIe-5668 Theory of Operation topics in the NI RF Vector Signal Analyzers Help. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **AC Coupled**.

**Valid values**

- PXIe-5665 (3.6 GHz): AC Coupled DC Coupled
- PXIe-5665 (14 GHz): AC Coupled, DC Coupled
- PXIe-5668: AC Coupled

**Supported devices**: PXIe-5665/5668

| AC Coupled (0) | Specifies that the RF input channel is AC-coupled. For low frequencies (<10 MHz), accuracy decreases because RFmxInstr does not calibrate the configuration. |
| --- | --- |
| DC Coupled (1) | Specifies that the RF input channel is DC-coupled. The RFmx driver enforces a minimum RF attenuation for device protection. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attrc.html language=enus -->
## TOPIC 00093: Advanced:Downconverter Preselector Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attrc.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attrc.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Downconverter Preselector Enabled Property

**Short Name:**Preselector Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the tunable preselector is enabled on the downconverter.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is **Disabled**.

**Supported devices**: PXIe-5663/5663E/5665/5668, PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842

| Disabled (0) | Disables the preselector. |
| --- | --- |
| Enabled (1) | The preselector is automatically enabled when it is in the signal path and is automatically disabled when it is not in the signal path. Use the Preselector Present property to determine if the downconverter has a preselector. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attrd.html language=enus -->
## TOPIC 00094: LO:Downconverter Center Frequency Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attrd.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attrd.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

LO:Downconverter Center Frequency Property

**Short Name:**Downconverter Freq

Property of [RFmxInstr](crfmxinstr.html)

Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz.

After you set this property, the RF downconverter is locked to that frequency until the value is changed or the property is reset. Locking the downconverter to a fixed value allows frequencies within the instantaneous bandwidth of the downconverter to be measured without the overhead of retuning the LO and waiting for the LO to settle. This method is called in-band retuning and it has the highest benefit on analyzers that have larger LO settling times. After setting the downconverter center frequency, you can set the center frequency to the frequencies at which you want to take the measurements.

If you want to avoid the LO leakage or DC offset of analyzers that use a direct conversion architecture, it is more convenient to use the [Downconverter Frequency Offset](attr35.html) or [LO Leakage Avoidance Enabled](attr37.html) properties.

If you set this property, any measurements outside the instantaneous bandwidth of the device are invalid. To disable in-band retuning, reset this property or call the [RFmxInstr Reset to Default](/csh?topicname=rfmxinstrvi/rfmxinstr_reset_to_default.html) VI.

|  | Note This property is not supported on a MIMO session. |
| --- | --- |

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is the carrier frequency or spectrum center frequency.

Valid Values: Any supported tuning frequency of the device.

|  | Note PXIe-5820: The only valid value for this property is 0 Hz. |
| --- | --- |

**Supported devices**: PXIe-5644/5645/5646, PXIe-5663/5663E/5665/5668, PXIe-5820/5830/5831/5832/5840/5841/5842

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attre.html language=enus -->
## TOPIC 00095: Advanced:Preamp Enabled Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attre.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attre.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Preamp Enabled Property

**Short Name:**Preamp Enabled

Property of [RFmxInstr](crfmxinstr.html)

Specifies whether the RF preamplifier is enabled in the system.

PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842: If you set this property to **Automatic**, RFmx selects the preamplifier state based on the value of the Reference Level property and the center frequency. For PXIe-5830/5831/5832, the value is not coerced.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value for PXIe-5644/5645/5646 and PXIe-5830/5831/5832/5840/5841/5842 is **Automatic**, else the default value is **Disabled**.

| Disabled (0) | Disables the RF preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668 |
| --- | --- |
| Enabled (1) | Enables the RF preamplifier when it is in the signal path and disables it when it is not in the signal path. Only devices with an RF preamplifier on the downconverter and an RF preselector support this option. Use the RF Preamp Present property to determine whether the downconverter has a preamplifier. Supported Devices: PXIe-5663/5663E/5665/5668 |
| Automatic (3) | Automatically enables the RF preamplifier based on the value of the reference level. Supported Devices: PXIe-5644/5645/5646, PXIe-5830/5831/5832/5840/5841/5842 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/attrf.html language=enus -->
## TOPIC 00096: Advanced:Mixer Level Offset (dB) Property

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/attrf.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/attrf.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

Advanced:Mixer Level Offset (dB) Property

**Short Name:**Mixer Level Offset (dB)

Property of [RFmxInstr](crfmxinstr.html)

Specifies the number of dB by which to adjust the device mixer level.

Specifying a positive value for this property configures the device for moderate distortion and low noise, and specifying a negative value results in low distortion and higher noise.
 You cannot set the [Mixer Level Offset](attrf.html) and [Mixer Level](attr10.html) properties at the same time.

You do not need to use a selector string if you want to configure this property for all signal instances. Specify the signal name in the selector string if you want to configure or read that signal instance. Refer to the [Selector Strings](/csh?topicname=rfmxspecan/selector_string.html) topic for information about the string syntax.

The default value is 0. The default value specifies device settings that are the best compromise between distortion and noise.

**Supported devices**: PXIe-5663/5663E/5665/5668

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Resettable | Yes |

<!--NI_TOPIC bundle=rfmx-instr-prop path=rfmxinstrprop/crfmxinstr.html language=enus -->
## TOPIC 00097: RFmxInstr Properties

- bundle_id: `rfmx-instr-prop`
- source_path: `rfmxinstrprop/crfmxinstr.html`
- source_url: https://docs-be.ni.com/bundle/rfmx-instr-prop/raw/resource/enus/rfmxinstrprop/crfmxinstr.html
- document_id: `rfmx-instr-prop`
- page_type: `leaf`
- content_type: ``

RFmxInstr Properties

Use the RFmxInstr properties to access options for configuring and fetching measurements.

| Property | Description |
| --- | --- |
| Selector String | Specifies the selector string used to access all subsequent selector string-based properties in this instance of the property node. Details |
| Frequency Reference:Source | Specifies the frequency reference source. Details |
| Frequency Reference:Frequency (Hz) | Specifies the Reference Clock rate, when the Frequency Reference Source property is set to ClkIn or RefIn. This value is expressed in Hz. Details |
| Frequency Reference:Exported Terminal | Specifies a comma-separated list of the terminals at which to export the frequency reference. Details |
| RF Attenuation:Auto | Specifies whether the RFmx driver computes the RF attenuation. Details |
| RF Attenuation:Value (dB) | Specifies the nominal attenuation setting for all attenuators before the first mixer in the RF signal chain. This value is expressed in dB. Details |
| Mechanical Attenuation:Auto | Specifies whether the RFmx driver chooses an attenuation setting based on the hardware settings. Details |
| Mechanical Attenuation:Value (dB) | Specifies the level of mechanical attenuation for the RF path. This value is expressed in dB. Details |
| LO:LO Leakage Avoidance Enabled | Specifies whether to reduce the effects of the instrument leakage by placing the LO outside the band of acquisition. Details |
| LO:LO Source | Specifies the local oscillator (LO) signal source used to downconvert the RF input signal. Details |
| LO:LO Frequency (Hz) | Specifies the LO signal frequency for the configured center frequency. This value is expressed in Hz. Details |
| LO:LO Export Enabled | Specifies whether to enable the LO OUT terminals on the installed devices. Details |
| LO:LO2 Export Enabled | Specifies whether to enable the LO2 OUT terminals in the installed devices. Details |
| LO:LO In Power (dBm) | Specifies the power level expected at the LO IN terminal when the LO Source property is set to LO_In. This value is expressed in dBm. Details |
| LO:LO Out Power (dBm) | Specifies the power level of the signal at the LO OUT terminal when the LO Export Enabled property is set to TRUE. This value is expressed in dBm. Details |
| LO:Tuning Speed | Makes tradeoffs between tuning speed and phase noise. Details |
| LO:Downconverter Frequency Offset (Hz) | Specifies an offset from the center frequency value for the downconverter. Use this property to offset the measurement away from the LO leakage or DC Offset of analyzers that use a direct conversion architecture. You must set this property to half the bandwidth or span of the measurement + guardband. The guardband is needed to ensure that the LO leakage is not inside the analog or digital filter rolloffs. This value is expressed in Hz. Details |
| LO:Downconverter Center Frequency | Enables in-band retuning and specifies the current frequency of the RF downconverter. This value is expressed in Hz. Details |
| LO:LO Injection Side | Specifies the LO injection side. Details |
| LO:LO Frequency Step Size (Hz) | Specifies the step size for tuning the LO phase-locked loop (PLL). Details |
| LO:VCO Frequency Step Size (Hz) | Specifies the step size for tuning the internal voltage-controlled oscillator (VCO) used to generate the LO signal. The valid values for LO1 include 1 Hz to 50 MHz and for LO2 include 1 Hz to 100 MHz. Details |
| LO:LO PLL Fractional Mode | Specifies whether to use fractional mode for the LO phase-locked loop (PLL). Details |
| Trigger:Export Output Terminal | Specifies the destination terminal for the exported Reference Trigger. You can also choose not to export any signal. Details |
| Trigger:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Trigger:Start:Type | Specifies whether the start trigger is a digital edge or a software trigger. Details |
| Trigger:Start:Digital Edge:Source | Specifies the source terminal for the start trigger. This property is used only when you set the Start Trigger Type property to Digital Edge. Details |
| Trigger:Start:Digital Edge:Edge | Specifies the active edge for the start trigger. This property is used only when you set the Start Trigger Type property to Digital Edge. Details |
| Trigger:Start:Export Output Terminal | Specifies the destination terminal for the exported start trigger. Details |
| Trigger:Start:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Trigger:Advance:Type | Specifies whether the advance trigger is a digital edge or a software trigger. Details |
| Trigger:Advance:Digital Edge:Source | Specifies the source terminal for the advance trigger. Details |
| Trigger:Advance:Export Output Terminal | Specifies the destination terminal for the exported advance trigger. Details |
| Trigger:Advance:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Event:Ready For Start:Output Terminal | Specifies the destination terminal for the Ready for Start event. Details |
| Event:Ready For Start:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Event:Ready For Advance:Output Terminal | Specifies the destination terminal for the Ready for Advance event. Details |
| Event:Ready For Advance:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Event:Ready For Reference:Output Terminal | Specifies the destination terminal for the Ready for Reference event. Details |
| Event:Ready For Reference:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Event:End Of Record:Output Terminal | Specifies the destination terminal for the End of Record event. Details |
| Event:End Of Record:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Event:Done:Output Terminal | Specifies the destination terminal for the Done event. Details |
| Event:Done:Terminal Name | Returns the fully qualified signal name as a string. Details |
| Device Information:Device Temperature (deg C) | Returns the current temperature of the module. This value is expressed in degrees Celsius. Details |
| Device Information:Digitizer Temperature (deg C) | Returns the current temperature of the digitizer module. This value is expressed in degrees Celsius. Details |
| Device Information:LO Temperature (deg C) | Returns the current temperature of the LO module associated with the device. This value is expressed in degrees Celsius. Details |
| Device Information:Serial Number | Returns the serial number of the RF downconverter module. Details |
| Device Information:Instrument Model | Returns a string that contains the model number or name of the RF device that you are currently using. Details |
| Device Information:Module Revision | Returns the revision of the RF downconverter module. Details |
| Device Information:Instrument Firmware Revision | Returns a string containing the firmware revision information of the RF downconverter for the composite device you are currently using. Details |
| Device Information:Preselector Present | Indicates whether a preselector is available on the RF downconverter module. Details |
| Device Information:RF Preamp Present | Indicates whether an RF preamplifier is available on the RF downconverter module. Details |
| Advanced:Preamp Enabled | Specifies whether the RF preamplifier is enabled in the system. Details |
| Advanced:Channel Coupling | Specifies whether the RF IN connector is AC- or DC-coupled on the downconverter. Details |
| Advanced:Downconverter Preselector Enabled | Specifies whether the tunable preselector is enabled on the downconverter. Details |
| Advanced:Mixer Level (dBm) | Specifies the mixer level. This value is expressed in dBm. Details |
| Advanced:Mixer Level Offset (dB) | Specifies the number of dB by which to adjust the device mixer level. Details |
| Advanced:RF Attenuation Step Size (dB) | Specifies the step size for the RF attenuation level. This value is expressed in dB. The actual RF attenuation is coerced up to the next highest multiple of the specified step size. If the mechanical attenuators are not available to implement the coerced RF attenuation, the solid state attenuators are used. Details |
| Advanced:OSP Delay Enabled | Specifies whether to enable the digitizer OSP block to delay Reference Triggers, along with the data samples, moving through the OSP block. Details |
| Advanced:Phase Offset | Specifies the offset to apply to the initial I and Q phases. Details |
| Advanced:FFT Width | Specifies the FFT width of the device. The FFT width is the effective bandwidth of the signal path during each signal acquisition. Details |
| Advanced:Cleaner Spectrum | Specifies how to obtain the lowest noise floor or faster measurement speed. Details |
| Advanced:IF Output Power Level Offset | Specifies the power offset by which to adjust the default IF output power level. This value is expressed in dB. Details |
| Advanced:Digitizer Dither Enabled | Specifies whether dithering is enabled on the digitizer. Details |
| Advanced:IF Filter Bandwidth (Hz) | Specifies the IF filter path bandwidth for your device configuration. Details |
| Advanced:Frequency Settling Units | Specifies the delay duration units and interpretation for LO settling. Details |
| Advanced:Frequency Settling | Specifies the value used for LO frequency settling. Details |
| Advanced:RF Highpass Filter Frequency (Hz) | Specifies the maximum corner frequency of the high pass filter in the RF signal path. The device uses the highest frequency high-pass filter option below or equal to the value you specify and returns a coerced value. Specifying a value of 0 disables high pass filtering silly. For multispan acquisitions, the device uses the appropriate filter for each subspan during acquisition, depending on the details of your application and the value you specify. In multispan acquisition spectrum applications, this property returns the value you specified rather than a coerced value if multiple high-pass filters are used during the acquisition. Details |
| Advanced:Subspan Overlap | Specifies the amount of overlap between consecutive subspans in a multispan spectrum acquisition. Overlapping subspans can reduce the power level of spurs in the acquired data. The value you specify determines the amount of shift as a percentage of subspan width. Details |
| Advanced:Downconverter Gain (dB) | Returns the net signal gain for the device at the current RFmx settings and temperature. RFmx scales the acquired I/Q and spectrum data from the digitizer using the value of this property. Details |
| Advanced:Amplitude Settling | Specifies the amplitude settling accuracy value. This value is expressed in decibels. RFmx waits until the RF power attains the specified accuracy level after calling the RFmx Initiate VI. Details |
| Advanced:Overflow Error Reporting | Configures error reporting for ADC and overflows occurred during onboard signal processing. Overflows lead to clipping of the waveform. Details |
| Advanced:Common Mode Level (V) | Specifies the common-mode level presented at each differential input terminal. The common-mode level shifts both positive and negative terminals in the same direction. This must match the common-mode level of the device under test (DUT). This value is expressed in Volts. Details |
| Advanced:SMU Resource Name | Specifies the resource name assigned by Measurement and Automation Explorer (MAX) for NI Source Measure Units (SMU) which is used as the noise source power supply for Noise Figure (NF) measurement, for example, PXI1Slot3, where PXI1Slot3 is an instrument resource name. SMU Resource Name can also be a logical IVI name. Details |
| Advanced:SMU Channel | Specifies the output channel to be used for noise figure (NF) measurement in RFmx. Details |
| Advanced:Optimize Path For Signal Bandwidth | Optimizes RF path for the signal bandwidth that is centered on the IQ carrier frequency. Details |
| Advanced:Input Isolation Enabled | Specifies whether input isolation is enabled. Details |
| Advanced:Thermal Correction Headroom Range (deg C) | Specifies the expected thermal operating range of the instrument from the self-calibration temperature returned from the Device Temperature property. This value is expressed in degree Celsius. Details |
| Advanced:Temperature Read Interval (s) | Specifies the minimum time difference between temperature sensor readings. This value is expressed in seconds. Details |
| Advanced:Thermal Correction Temperature Resolution (deg C) | Specifies the temperature change required before RFmx recalculates the thermal correction settings when entering the running state. This value is expressed in degree Celsius. Details |
| Advanced:Number of Raw IQ Records | Returns the number of raw IQ records to acquire to complete measurement averaging. Details |
| Advanced:Self Calibration:Self Cal Validity Check | Specifies whether the RFmx driver validates the self-calibration data. Details |
| Advanced:Self Calibration:Self Cal Validity Check Time Interval (s) | Specifies the minimum time between two self calibration validity checks. This value is expressed in seconds. Details |
| MIMO:LO Sharing Mode | Specifies the RFmx session with the respective LO sharing mode. Details |
| MIMO:Number of LO Sharing Groups | Specifies the RFmx session with the number of LO sharing groups. Details |
| Load Configurations: Load Options | Specifies the configurations to skip while loading from a file using the RFmxInstr Load Configurations VI . Details |
| Recommended Settings:Acquisition Type | Returns the recommended acquisition type for the last committed measurement configuration. Details |
| Recommended Settings:Center Frequency (Hz) | Returns the recommended center frequency of the RF signal. This value is expressed in Hz. Details |
| Recommended Settings:Number of Records | Returns the recommended number of records to acquire to complete measurement averaging. Details |
| Recommended Settings:Trigger Min Quiet Time (s) | Returns the recommended minimum quiet time during which the signal level must be below the trigger value for triggering to occur. This value is expressed in seconds. Details |
| Recommended Settings:IQ:Acquisition Time (s) | Returns the recommended acquisition time for I/Q acquisition. This value is expressed in seconds. Details |
| Recommended Settings:IQ:Minimum Sample Rate (Hz) | Returns the recommended minimum sample rate for I/Q acquisition. This value is expressed in Hz. Details |
| Recommended Settings:IQ:Pre Trigger Time (s) | Returns the recommended pretrigger time for I/Q acquisition. This value is expressed in seconds. Details |
| Recommended Settings:Spectral:Acquisition Span (Hz) | Returns the recommended acquisition span for spectral acquisition. This value is expressed in Hz. Details |
| Recommended Settings:Spectral:FFT Window | Returns the recommended FFT window type for spectral acquisition. Details |
| Recommended Settings:Spectral:Resolution Bandwidth (Hz) | Returns the recommended FFT bin width for spectral acquisition. This value is expressed in Hz. Details |
