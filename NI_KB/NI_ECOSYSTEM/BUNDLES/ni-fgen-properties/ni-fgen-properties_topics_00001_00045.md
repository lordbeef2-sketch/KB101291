# NI DOCUMENT BUNDLE: ni-fgen-properties

<!--NI_BUNDLE_CHUNK bundle=ni-fgen-properties start=1 end=45 -->
<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_analogdatamask.html language=enus -->
## TOPIC 00001: Output:Data Mask:Analog Data Mask Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_analogdatamask.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_analogdatamask.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Output:Data Mask:Analog Data Mask Property

**Short Name:**Analog Data Mask

Property of [niFgen](cnifgen.html)

Specifies the mask to apply to the analog output data. The masked data is replaced with the data in the [Analog Static Value](pnifgen_analogstaticvalue.html) property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_drivervendor.html language=enus -->
## TOPIC 00002: Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_drivervendor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_drivervendor.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:Inherent IVI Attributes:Driver Identification:Driver Vendor Property

**Short Name:**Driver Vendor

Property of [niFgen](cnifgen.html)

Contains the name of the vendor that supplies NI-FGEN.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_dutycyclehigh.html language=enus -->
## TOPIC 00003: Standard Function:Duty Cycle High Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_dutycyclehigh.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_dutycyclehigh.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Standard Function:Duty Cycle High Property

**Short Name:**Duty Cycle High

Property of [niFgen](cnifgen.html)

Specifies the duty cycle of the square wave the signal generator is producing. Specify this property as a percentage of the time the square wave is high in a cycle.

**Units**: Percentage of time the waveform is high

**Default Value**: 50%

|  | Note This parameter only affects signal generator behavior when you set the Waveform property to NIFGEN_VAL_WFM_SQUARE. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_endpointcount.html language=enus -->
## TOPIC 00004: Arbitrary Waveform:Peer-to-Peer:Endpoint Count Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_endpointcount.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_endpointcount.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Peer-to-Peer:Endpoint Count Property

**Short Name:**Endpoint Count

Property of [niFgen](cnifgen.html)

Returns the number of peer-to-peer FIFO endpoints supported by the device.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_endpointsize.html language=enus -->
## TOPIC 00005: Arbitrary Waveform:Peer-to-Peer:Endpoint Size Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_endpointsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_endpointsize.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Peer-to-Peer:Endpoint Size Property

**Short Name:**Endpoint Size

Property of [niFgen](cnifgen.html)

Returns the size, in samples per channel, of the peer-to-peer endpoint. This property is [endpoint-based](/csh?topicname=siggenhelp/p2p_configuring_an_endpoint.html).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_endpointwindowaddresstype.html language=enus -->
## TOPIC 00006: Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address Type Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_endpointwindowaddresstype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_endpointwindowaddresstype.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Address Type Property

**Short Name:**Endpoint Window Address Type

Property of [niFgen](cnifgen.html)

Specifies the type of the [Endpoint Window Address](pnifgen_endpointwindowaddress.html) property. This property is [endpoint-based](/csh?topicname=siggenhelp/p2p_configuring_an_endpoint.html).

|  | Note You can only use this property when the Manual Configuration Enabled property is set to TRUE. |
| --- | --- |

**Default Value**: **Virtual**

| Physical (0) | Specifies a physical memory address. |
| --- | --- |
| Virtual (1) | Specifies a virtual memory address. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_endpointwindowsize.html language=enus -->
## TOPIC 00007: Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Size Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_endpointwindowsize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_endpointwindowsize.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Peer-to-Peer:Manual:Configuration:Endpoint Window Size Property

**Short Name:**Endpoint Window Size

Property of [niFgen](cnifgen.html)

Returns the size, in bytes, of the endpoint window. The endpoint window is also described by the [Endpoint Window Address](pnifgen_endpointwindowaddress.html) property and the [Endpoint Window Address Type](pnifgen_endpointwindowaddresstype.html) property. This property is [endpoint-based](/csh?topicname=siggenhelp/p2p_configuring_an_endpoint.html).

|  | Note You can only use this property when the Manual Configuration Enabled property is set to TRUE. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedonboardreferenceclockoutputterminal.html language=enus -->
## TOPIC 00008: Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedonboardreferenceclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedonboardreferenceclockoutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Reference Clock:Onboard Reference Clock:Export Output Terminal Property

**Short Name:**Exported Onboard Reference Clock Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the terminal at which to export the onboard Reference Clock.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedreferenceclockoutputterminal.html language=enus -->
## TOPIC 00009: Clocks:Reference Clock:Export Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedreferenceclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedreferenceclockoutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Reference Clock:Export Output Terminal Property

**Short Name:**Exported Reference Clock Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the terminal at which to export the Reference Clock.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedsampleclockdivisor.html language=enus -->
## TOPIC 00010: Clocks:Sample Clock:Exported Sample Clock Divisor Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedsampleclockdivisor.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedsampleclockdivisor.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Sample Clock:Exported Sample Clock Divisor Property

**Short Name:**Exported Sample Clock Divisor

Property of [niFgen](cnifgen.html)

Specifies the factor by which to divide the update (Sample) Clock before it is exported.

To export the Sample Clock, use the [niFgen Export Signal](/csh?topicname=nifgenlv/nifgen_export_signal.html) VI or the [Exported Sample Clock Output Terminal](pnifgen_exportedsampleclockoutputterminal.html) property.

**Valid Values**: 1 to 4,096

**Default Value**: 1

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedsampleclockoutputterminal.html language=enus -->
## TOPIC 00011: Clocks:Sample Clock:Export Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedsampleclockoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedsampleclockoutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Sample Clock:Export Output Terminal Property

**Short Name:**Exported Sample Clock Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the terminal at which to export the Sample Clock. If you specify a divisor with the [Exported Sample Clock Divisor](pnifgen_exportedsampleclockdivisor.html) property, the Sample Clock exported with this property is the value of the Sample Clock after it is divided-down.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

|  | Note The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedsampleclocktimebaseoutputterminal.html language=enus -->
## TOPIC 00012: Clocks:Sample Clock Timebase:Export Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedsampleclocktimebaseoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedsampleclocktimebaseoutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Sample Clock Timebase:Export Output Terminal Property

**Short Name:**Exported Sample Clock Timebase Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the terminal at which to export the Sample Clock Timebase.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

If you specify a divisor with the [Exported Sample Clock Timebase Divisor](pnifgen_exportedsampleclocktimebasedivisor.html) property, the Sample Clock timebase exported with the Exported Sample Clock Timebase Output Terminal property is the value of the Sample Clock timebase after it is divided down.

|  | Note The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedscripttriggeroutputterminal.html language=enus -->
## TOPIC 00013: Triggers:Script:Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedscripttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedscripttriggeroutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Script:Output Terminal Property

**Short Name:**Exported Script Trigger Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the output terminal for the exported Script Trigger.

Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_exportedstarttriggeroutputterminal.html language=enus -->
## TOPIC 00014: Triggers:Start:Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_exportedstarttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_exportedstarttriggeroutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Start:Output Terminal Property

**Short Name:**Exported Start Trigger Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the destination terminal for exporting the Start Trigger.

For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_filetransferblocksize.html language=enus -->
## TOPIC 00015: Arbitrary Waveform:Data Transfer:File Transfer Block Size Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_filetransferblocksize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_filetransferblocksize.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Data Transfer:File Transfer Block Size Property

**Short Name:**File Transfer Block Size

Property of [niFgen](cnifgen.html)

Specifies the maximum number of samples to transfer at one time from the device to host memory. This property is used in conjunction with the [niFgen Create Waveform From File](/csh?topicname=nifgenlv/nifgen_create_waveform_poly.html) VI and the [niFgen Write Waveform From File](/csh?topicname=nifgenlv/nifgen_write_waveform_poly.html) VI.

If the requested value is not evenly divisible by the required increment, this property is coerced up to the next 64-sample increment (32-sample increment for complex samples).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_flatfilterpassband.html language=enus -->
## TOPIC 00016: Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_flatfilterpassband.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_flatfilterpassband.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Onboard Signal Processing:FIR Filter:Flat:Passband Property

**Short Name:**Flat Filter Passband

Property of [niFgen](cnifgen.html)

Specifies the passband value to use when calculating the FIR filter coefficients. The FIR filter is designed to be flat to passband × I/Q rate. This property is used only when the [Filter Type](pnifgen_filtertype.html) property is set to **Flat**.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_fpgabitfilepath.html language=enus -->
## TOPIC 00017: Instrument:FPGA Bitfile Path Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_fpgabitfilepath.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_fpgabitfilepath.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:FPGA Bitfile Path Property

**Short Name:**FPGA Bitfile Path

Property of [niFgen](cnifgen.html)

Gets the absolute file path to the bitfile loaded on the FPGA.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_frequency.html language=enus -->
## TOPIC 00018: Standard Function:Standard Function Mode:Frequency Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_frequency.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_frequency.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Standard Function:Standard Function Mode:Frequency Property

**Short Name:**Frequency

Property of [niFgen](cnifgen.html)

Controls the frequency of the standard waveform that the signal generator produces.

**Units**: hertz (Hz)

**Default Value**: None

|  | Note This parameter does not affect signal generator behavior when you set the Waveform property to NIFGEN_VAL_WFM_DC. For NIFGEN_VAL_WFM_SINE , the range is between 0 MHz and 16 MHz, but the range is between 0 MHz and 1 MHz for all other waveforms. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Standard Waveform |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_frequencylistdurationquantum.html language=enus -->
## TOPIC 00019: Standard Function:Frequency List Mode:Frequency List Duration Quantum Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_frequencylistdurationquantum.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_frequencylistdurationquantum.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Standard Function:Frequency List Mode:Frequency List Duration Quantum Property

**Short Name:**Frequency List Duration Quantum

Property of [niFgen](cnifgen.html)

Returns the quantum that all durations must be a multiple of in a frequency list.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Query Freq List Capabilities |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_idlebehavior.html language=enus -->
## TOPIC 00020: Output:Advanced:Idle Behavior Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_idlebehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_idlebehavior.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Output:Advanced:Idle Behavior Property

**Short Name:**Idle Behavior

Property of [niFgen](cnifgen.html)

Specifies the behavior of the output during the Idle state.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| Hold Last Value (400) | While in the Idle state, the output signal remains at the last voltage generated prior to entering the Idle state. |
| --- | --- |
| Jump To Value (401) | While in the Idle state, the output signal remains at the value configured in the Idle Value property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_iqrate.html language=enus -->
## TOPIC 00021: Arbitrary Waveform:Onboard Signal Processing:IQ Rate Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_iqrate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_iqrate.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Onboard Signal Processing:IQ Rate Property

**Short Name:**IQ Rate

Property of [niFgen](cnifgen.html)

Specifies the rate at which the user-provided waveform data is generated when the [OSP Enabled](pnifgen_ospenabled.html) property is set to TRUE.

NI-FGEN sets the [Sample Rate](pnifgen_samplerate.html) property of the signal generator to the product of the IQ Rate, [FIR Interpolation Factor](pnifgen_firinterpolation.html), and [CIC Interpolation Factor](pnifgen_cicinterpolation.html) properties. When the [Data Processing Mode](pnifgen_dataprocessingmode.html) property is set to **Real**, the IQ Rate value is the rate at which the signal generator processes real (I) data. When the Data Processing Mode property is set to **Complex**, the IQ Rate value is the rate at which the signal generator processes complex (I/Q) data.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_loadimpedance.html language=enus -->
## TOPIC 00022: Output:Load Impedance Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_loadimpedance.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_loadimpedance.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Output:Load Impedance Property

**Short Name:**Load Impedance

Property of [niFgen](cnifgen.html)

Specifies the load impedance connected to the analog output of the channel.

If the load impedance is set to -1.0, NI-FGEN matches the load impedance to the [Output Impedance](pnifgen_outputimpedance.html) property value. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_logicalname.html language=enus -->
## TOPIC 00023: Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_logicalname.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_logicalname.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:Inherent IVI Attributes:Advanced Session Information:Logical Name Property

**Short Name:**Logical Name

Property of [niFgen](cnifgen.html)

Returns the logical name you specified when opening the current IVI session.

You may pass a logical name to the [niFgen Initialize](/csh?topicname=nifgenlv/nifgen_initialize.html) VI or the [niFgen Initialize With Options](/csh?topicname=nifgenlv/nifgen_initialize_with_options.html) VI. The IVI Configuration utility must contain an entry for the logical name. The logical name entry refers to a virtual instrument section in the IVI Configuration file. The virtual instrument section specifies a physical device and initial user options.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_majorversion.html language=enus -->
## TOPIC 00024: Instrument:Obsolete:Major Version Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_majorversion.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_majorversion.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:Obsolete:Major Version Property

**Short Name:**Major Version

Property of [niFgen](cnifgen.html)

Returns the major version number of NI-FGEN.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | niFgen Revision Query |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_manualconfigurationenabled.html language=enus -->
## TOPIC 00025: Arbitrary Waveform:Peer-to-Peer:Manual:Manual Configuration Enabled Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_manualconfigurationenabled.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_manualconfigurationenabled.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Peer-to-Peer:Manual:Manual Configuration Enabled Property

**Short Name:**Manual Configuration Enabled

Property of [niFgen](cnifgen.html)

Enables (TRUE) or disables (FALSE) manual configuration for a peer-to-peer endpoint. Enabling this property disables automatic NI-P2P stream manager flow control and Done Notifications.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_markereventdelayunits.html language=enus -->
## TOPIC 00026: Events:Marker:Advanced:Delay Units Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_markereventdelayunits.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_markereventdelayunits.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Events:Marker:Advanced:Delay Units Property

**Short Name:**Marker Event Delay Units

Property of [niFgen](cnifgen.html)

Specifies the units used for the [Marker Event Delay Value](pnifgen_markereventdelayvalue.html) property.

| Sample Clock Periods (101) | The delay is specified in Sample Clock periods and then coerced up by NI-FGEN to the nearest Sample Clock period. |
| --- | --- |
| Seconds (102) | The delay is specified in seconds and then coerced up by NI-FGEN to the nearest Sample Clock period. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_markereventdelayvalue.html language=enus -->
## TOPIC 00027: Events:Marker:Advanced:Delay Value Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_markereventdelayvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_markereventdelayvalue.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Events:Marker:Advanced:Delay Value Property

**Short Name:**Marker Event Delay Value

Property of [niFgen](cnifgen.html)

Specifies the amount of delay applied to a Marker Event with respect to the analog output of the signal generator.

A positive delay value indicates that the Marker Event occurs after the analog data, while a negative delay value indicates that the Marker Event occurs before the analog data. The default value is zero, which aligns the Marker Event with the analog output.

You can specify the units of the delay value using the [Marker Event Delay Units](pnifgen_markereventdelayunits.html) property.

**Default Value**: 0

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_sampleclocksource.html language=enus -->
## TOPIC 00028: Clocks:Sample Clock:Source Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_sampleclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_sampleclocksource.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Sample Clock:Source Property

**Short Name:**Sample Clock Source

Property of [niFgen](cnifgen.html)

Specifies the Sample Clock source.

|  | Note The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| Onboard Clock ("OnboardClock") | Specifies that the onboard clock is used as the Sample Clock source. |
| --- | --- |
| Clock In ("ClkIn") | Specifies that the signal at the CLK IN front panel connector is used as the Sample Clock source. |
| PXI STAR Line ("PXI_Star") | Specifies that the PXI_STAR trigger line is used as the Sample Clock source. |
| PXI Trigger Line 0/RTSI 0 ("PXI_Trig0") | Specifies that the PXI or RTSI line 0 is used as the Sample Clock source. |
| PXI Trigger Line 1/RTSI 1 ("PXI_Trig1") | Specifies that the PXI or RTSI line 1 is used as the Sample Clock source. |
| PXI Trigger Line 2/RTSI 2 ("PXI_Trig2") | Specifies that the PXI or RTSI line 2 is used as the Sample Clock source. |
| PXI Trigger Line 3/RTSI 3 ("PXI_Trig3") | Specifies that the PXI or RTSI line 3 is used as the Sample Clock source. |
| PXI Trigger Line 4/RTSI 4 ("PXI_Trig4") | Specifies that the PXI or RTSI line 4 is used as the Sample Clock source. |
| PXI Trigger Line 5/RTSI 5 ("PXI_Trig5") | Specifies that the PXI or RTSI line 5 is used as the Sample Clock source. |
| PXI Trigger Line 6/RTSI 6 ("PXI_Trig6") | Specifies that the PXI or RTSI line 6 is used as the Sample Clock source. |
| PXI Trigger Line 7/RTSI 7 ("PXI_Trig7") | Specifies that the PXI or RTSI line 7 is used as the Sample Clock source. |
| DDC Clock In ("DDC_ClkIn") | Specifies that the Sample Clock from DDC connector is used as the Sample Clock source. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Sample Clock Source |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_sampleclocktimebaserate.html language=enus -->
## TOPIC 00029: Clocks:Sample Clock Timebase:Rate Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_sampleclocktimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_sampleclocktimebaserate.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Sample Clock Timebase:Rate Property

**Short Name:**Sample Clock Timebase Rate

Property of [niFgen](cnifgen.html)

Specifies the Sample Clock Timebase rate. This property applies only to external Sample Clock timebases.

|  | Note The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_sampleclocktimebasesource.html language=enus -->
## TOPIC 00030: Clocks:Sample Clock Timebase:Source Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_sampleclocktimebasesource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_sampleclocktimebasesource.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Clocks:Sample Clock Timebase:Source Property

**Short Name:**Sample Clock Timebase Source

Property of [niFgen](cnifgen.html)

Specifies the Sample Clock Timebase source.

|  | Note The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| Onboard Clock ("OnboardClock") | Specifies that the onboard Sample Clock timebase is used as the source. |
| --- | --- |
| Clock In ("ClkIn") | Specifies that the external signal on the CLK IN front panel connector is used as the source. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_scripttogenerate.html language=enus -->
## TOPIC 00031: Arbitrary Waveform:Script Mode:Script to Generate Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_scripttogenerate.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_scripttogenerate.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Script Mode:Script to Generate Property

**Short Name:**Script to Generate

Property of [niFgen](cnifgen.html)

Specifies which script the signal generator uses. To configure the signal generator to run a particular script, set this property to the name of the script.

Use the [niFgen Write Script](/csh?topicname=nifgenlv/nifgen_write_script.html) VI to create multiple scripts. Use this property when the [Output Mode](pnifgen_outputmode.html) property is set to **NIFGEN_VAL_OUTPUT_SCRIPT**.

|  | Note The signal generator must not be in the Generating state when you change this property. To change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_scripttriggerdigitaledge-edge.html language=enus -->
## TOPIC 00032: Triggers:Script:Digital Edge:Edge Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_scripttriggerdigitaledge-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_scripttriggerdigitaledge-edge.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Script:Digital Edge:Edge Property

**Short Name:**Script Trigger Digital Edge - Edge

Property of [niFgen](cnifgen.html)

Specifies the active edge for the Script Trigger. This property is used when the [Script Trigger Type](pnifgen_scripttriggertype.html) property is set to **Digital Edge**.

| Rising Edge (101) | Occurs when the signal transitions from low level to high level. |
| --- | --- |
| Falling Edge (102) | Occurs when the signal transitions from high level to low level. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_spaceavailableinendpoint.html language=enus -->
## TOPIC 00033: Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_spaceavailableinendpoint.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_spaceavailableinendpoint.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Peer-to-Peer:Space Available In Endpoint Property

**Short Name:**Space Available In Endpoint

Property of [niFgen](cnifgen.html)

Returns the current space available in the endpoint in samples per channel. You can use this property when priming the endpoint with initial data through the [niFgen Write P2P Endpoint I16](/csh?topicname=nifgenlv/nifgen_write_p2p_endpoint_i16.html) VI to determine how many samples you can write. You also can use this property to characterize the performance and measure the latency of the peer-to-peer stream as data moves across the bus. This property is [endpoint-based](/csh?topicname=siggenhelp/p2p_configuring_an_endpoint.html).

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_spaceavailinstreamingwfm.html language=enus -->
## TOPIC 00034: Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_spaceavailinstreamingwfm.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_spaceavailinstreamingwfm.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Arbitrary Waveform:Data Transfer:Streaming:Space Available in Streaming Waveform Property

**Short Name:**Space Available in Streaming Waveform

Property of [niFgen](cnifgen.html)

Returns the space available in the streaming waveform for writing new data.

Use this property in conjunction with the [Streaming Waveform Handle](pnifgen_streamingwaveformhandle.html) property or the [Streaming Waveform Name](pnifgen_streamingwaveformname.html) property.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read Only |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_startedeventactivelevel.html language=enus -->
## TOPIC 00035: Events:Started:Level:Active Level Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_startedeventactivelevel.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_startedeventactivelevel.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Events:Started:Level:Active Level Property

**Short Name:**Started Event Active Level

Property of [niFgen](cnifgen.html)

Specifies the output polarity of the Started Event.

| Active High (101) | When the operation has started, the Started Event level is high. |
| --- | --- |
| Active Low (102) | When the operation has started, the Started Event level is high. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_starttriggerdigitaledge-edge.html language=enus -->
## TOPIC 00036: Triggers:Start:Digital Edge:Edge Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_starttriggerdigitaledge-edge.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_starttriggerdigitaledge-edge.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Start:Digital Edge:Edge Property

**Short Name:**Start Trigger Digital Edge - Edge

Property of [niFgen](cnifgen.html)

Specifies the active edge for the Start Trigger. This property is used only when the [Start Trigger Type](pnifgen_starttriggertype.html) property is set to **Digital Edge**.

| Rising Edge (101) | Occurs when the signal transitions from low level to high level. |
| --- | --- |
| Falling Edge (102) | Occurs when the signal transitions from high level to low level. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_starttriggerdigitaledge-source.html language=enus -->
## TOPIC 00037: Triggers:Start:Digital Edge:Source Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_starttriggerdigitaledge-source.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_starttriggerdigitaledge-source.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Start:Digital Edge:Source Property

**Short Name:**Start Trigger Digital Edge - Source

Property of [niFgen](cnifgen.html)

Specifies the source terminal for the Start Trigger. This property is used only when the [Start Trigger Type](pnifgen_starttriggertype.html) property is set to **Digital Edge**.

You can specify any valid source terminal for this property. Valid sources can be found in the Routes topic for your device or in Measurement & Automation Explorer under the **Device Routes** tab.

Source terminals can be specified in two ways. If your device is named Dev1 and your terminal is PFI0, then the terminal can be specified as a fully qualified terminal name, "/Dev1/PFI0". You can also specify the terminal using PFI 0.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger (poly) |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_synchronizationsource.html language=enus -->
## TOPIC 00038: Instrument:5401/5411/5431:Synchronization Source Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_synchronizationsource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_synchronizationsource.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:5401/5411/5431:Synchronization Source Property

**Short Name:**Synchronization Source

Property of [niFgen](cnifgen.html)

Specifies the source of the synchronization signal to use.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| NIFGEN_VAL_NONE (1000) | No synchronization source is used. |
| --- | --- |
| NIFGEN_VAL_RTSI_0 (141) | RTSI line 0 |
| NIFGEN_VAL_RTSI_1 (142) | RTSI line 1 |
| NIFGEN_VAL_RTSI_2 (143) | RTSI line 2 |
| NIFGEN_VAL_RTSI_3 (144) | RTSI line 3 |
| NIFGEN_VAL_RTSI_4 (145) | RTSI line 4 |
| NIFGEN_VAL_RTSI_5 (146) | RTSI line 5 |
| NIFGEN_VAL_RTSI_6 (147) | RTSI line 6 |
| NIFGEN_VAL_TTL0 (111) | PXI TRIG0 or VXI TTL0 |
| NIFGEN_VAL_TTL1 (112) | PXI TRIG1 or VXI TTL1 |
| NIFGEN_VAL_TTL2 (113) | PXI TRIG2 or VXI TTL2 |
| NIFGEN_VAL_TTL3 (114) | PXI TRIG3 or VXI TTL3 |
| NIFGEN_VAL_TTL4 (115) | PXI TRIG4 or VXI TTL4 |
| NIFGEN_VAL_TTL5 (116) | PXI TRIG5 or VXI TTL5 |
| NIFGEN_VAL_TTL6 (117) | PXI TRIG6 or VXI TTL6 |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_syncoutoutputterminal.html language=enus -->
## TOPIC 00039: Standard Function:Sync Out Output Terminal Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_syncoutoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_syncoutoutputterminal.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Standard Function:Sync Out Output Terminal Property

**Short Name:**Sync Out Output Terminal

Property of [niFgen](cnifgen.html)

Specifies the terminal at which to export the SYNC OUT signal. This property is not supported for all devices. For a list of the terminals available on your device, refer to the Routes topic for your device or the **Device Routes** tab in MAX.

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Export Signal |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_terminalconfiguration.html language=enus -->
## TOPIC 00040: Output:Terminal Configuration Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_terminalconfiguration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_terminalconfiguration.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Output:Terminal Configuration Property

**Short Name:**Terminal Configuration

Property of [niFgen](cnifgen.html)

Specifies whether to analyze gain and offset values based on single-ended or [differential](/csh?topicname=siggenhelp/fund_differential_output.html) operation.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| Single Ended (300) | Specifies single-ended operation. |
| --- | --- |
| Differential (301) | Specifies differential operation. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_triggermode.html language=enus -->
## TOPIC 00041: Triggers:Trigger Mode Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_triggermode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_triggermode.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Triggers:Trigger Mode Property

**Short Name:**Trigger Mode

Property of [niFgen](cnifgen.html)

Controls the trigger mode.

**Default Value**: **NIFGEN_VAL_CONTINUOUS**

| NIFGEN_VAL_SINGLE (1) | Specifies that the signal generator operates in Single Trigger mode. |
| --- | --- |
| NIFGEN_VAL_CONTINUOUS (2) | Specifies that the signal generator operates in Continuous Trigger mode. |
| NIFGEN_VAL_STEPPED (3) | Specifies that the signal generator operates in Stepped Trigger mode. |
| NIFGEN_VAL_BURST (4) | Specifies that the signal generator operates in Burst Trigger mode. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | niFgen Configure Trigger Mode |
| Channel-based | Yes |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_updateclocksource.html language=enus -->
## TOPIC 00042: Instrument:Obsolete:Update Clock Source Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_updateclocksource.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_updateclocksource.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:Obsolete:Update Clock Source Property

**Short Name:**Update Clock Source

Property of [niFgen](cnifgen.html)

Controls the Update Clock source.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| NIFGEN_VAL_INTERNAL (0) | Internal update clock |
| --- | --- |
| NIFGEN_VAL_EXTERNAL (1) | External update clock given on the IO connector |
| NIFGEN_VAL_CLK_IN (1202) | Coaxial CLK IN connector on the board front panel |
| NIFGEN_VAL_DDC_CLK_IN (1203) | DDC CLK IN line of the Digital Data & Control connector |
| NIFGEN_VAL_PXI_STAR (131) | (PXI only) PXI star trigger line. This choice is valid only in PXI chassis slots 3 through 15. |
| NIFGEN_VAL_RTSI_0 (141) | RTSI line 0 |
| NIFGEN_VAL_RTSI_1 (142) | RTSI line 1 |
| NIFGEN_VAL_RTSI_2 (143) | RTSI line 2 |
| NIFGEN_VAL_RTSI_3 (144) | RTSI line 3 |
| NIFGEN_VAL_RTSI_4 (145) | RTSI line 4 |
| NIFGEN_VAL_RTSI_5 (146) | RTSI line 5 |
| NIFGEN_VAL_RTSI_6 (147) | RTSI line 6 |
| NIFGEN_VAL_RTSI_7 (1010) | (PCI only) RTSI line 7 |
| NIFGEN_VAL_OTHER_TERMINAL (1018) | Uses another device terminal. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_videowaveformtype.html language=enus -->
## TOPIC 00043: Instrument:5401/5411/5431:Video Waveform Type Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_videowaveformtype.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_videowaveformtype.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Instrument:5401/5411/5431:Video Waveform Type Property

**Short Name:**Video Waveform Type

Property of [niFgen](cnifgen.html)

Specifies the waveform type the NI 5431 generates. Setting this property ensures the oscillator crystal is set to the proper frequency.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| NIFGEN_VAL_PAL_B (0) | PAL B Video Type |
| --- | --- |
| NIFGEN_VAL_PAL_D (1) | PAL D Video Type |
| NIFGEN_VAL_PAL_G (2) | PAL G Video Type |
| NIFGEN_VAL_PAL_H (3) | PAL H Video Type |
| NIFGEN_VAL_PAL_I (4) | PAL I Video Type |
| NIFGEN_VAL_PAL_M (5) | PAL M Video Type |
| NIFGEN_VAL_PAL_N (6) | PAL N Video Type |
| NIFGEN_VAL_NTSC_M (7) | NTSC M Video Type |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | No |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_waitbehavior.html language=enus -->
## TOPIC 00044: Output:Advanced:Wait Behavior Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_waitbehavior.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_waitbehavior.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Output:Advanced:Wait Behavior Property

**Short Name:**Wait Behavior

Property of [niFgen](cnifgen.html)

Specifies the behavior of the output while waiting for a Script Trigger or during a wait instruction.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

| Hold Last Value (400) | While in a wait state, the output signal remains at the last voltage generated prior to entering the wait state. |
| --- | --- |
| Jump To Value (401) | While in a wait state, the output signal remains at the value configured in the Wait Value property. |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | No |
| Resettable | Yes |

<!--NI_TOPIC bundle=ni-fgen-properties path=nifgenpropref/pnifgen_waitvalue.html language=enus -->
## TOPIC 00045: Output:Advanced:Wait Value Property

- bundle_id: `ni-fgen-properties`
- source_path: `nifgenpropref/pnifgen_waitvalue.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-properties/raw/resource/enus/nifgenpropref/pnifgen_waitvalue.html
- document_id: `ni-fgen-properties`
- page_type: `leaf`
- content_type: ``

### Output:Advanced:Wait Value Property

**Short Name:**Wait Value

Property of [niFgen](cnifgen.html)

Specifies the value to generate while waiting. You must set the [Wait Behavior](pnifgen_waitbehavior.html) property to **Jump To Value** to use this property.

|  | Note You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the niFgen Abort Generation VI or wait for the generation to complete. |
| --- | --- |

#### Remarks

The following table lists the characteristics of this property.

| Datatype |  |
| --- | --- |
| Permissions | Read/Write |
| High-level VIs | N/A |
| Channel-based | Yes |
| Resettable | Yes |
