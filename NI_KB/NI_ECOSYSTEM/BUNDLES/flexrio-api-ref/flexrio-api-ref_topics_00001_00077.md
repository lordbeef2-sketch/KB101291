# NI DOCUMENT BUNDLE: flexrio-api-ref

<!--NI_BUNDLE_CHUNK bundle=flexrio-api-ref start=1 end=77 -->
<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_analogedgetriggerrising.html language=enus -->
## TOPIC 00001: kFlexRIO_AnalogEdgeTriggerRising

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_analogedgetriggerrising.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_analogedgetriggerrising.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_AnalogEdgeTriggerRising

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeBool | uint32_t | Read/Write | Trigger | None | None |

#### Description

Specifies whether to use a rising edge for the analog edge trigger.

**Defined Values**

| 0 | false | Specifies a falling edge trigger. |
| --- | --- | --- |
| 1 | true | Specifies a rising edge trigger. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_calibrationdatetime.html language=enus -->
## TOPIC 00002: kFlexRIO_CalibrationDateTime

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_calibrationdatetime.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_calibrationdatetime.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_CalibrationDateTime

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeUInt64 | uint64_t | Read Only | N/A | None | niFlexRIO_ReadCalibrationData |

#### Description

Indicates the time of the last write to calibration storage in seconds since 12:00 a.m., January 1, 1904 [01-01-1904 00:00:00].

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_calibrationstoragesize.html language=enus -->
## TOPIC 00003: kFlexRIO_CalibrationStorageSize

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_calibrationstoragesize.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_calibrationstoragesize.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_CalibrationStorageSize

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | N/A | None | None |

#### Description

Indicates the size in bytes of available calibration storage.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_channelnyquistzone.html language=enus -->
## TOPIC 00004: kFlexRIO_AiChannelNyquistZone

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_channelnyquistzone.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_channelnyquistzone.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_AiChannelNyquistZone

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | Channel | None | None |

#### Description

Specifies the Nyquist Zone in which the input signal resides. This property is for use in undersampling applications and is useful for improving interleaving spur performance.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_decimationfilterband.html language=enus -->
## TOPIC 00005: kFlexRIO_AiDecimationFilterBand

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_decimationfilterband.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_decimationfilterband.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_AiDecimationFilterBand

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | Channel | None | None |

#### Description

Specifies a highpass or lowpass filter response for the ADC decimation filter. If the signal resides in the first Nyquist zone, use the lowpass filter. If the signal resides in the second Nyquist zone, use the highpass filter. This property is for use in undersampling applications.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_digitalstarttriggersource.html language=enus -->
## TOPIC 00006: kFlexRIO_DigitalStartTriggerSource

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_digitalstarttriggersource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_digitalstarttriggersource.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_DigitalStartTriggerSource

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeString | char* | Read/Write | Trigger | None | None |

#### Description

Specifies the source of the digital start trigger.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_diovoltage.html language=enus -->
## TOPIC 00007: kFlexRIO_DioVoltage

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_diovoltage.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_diovoltage.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_DioVoltage

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeDouble | double | Read/Write | N/A | None | None |

#### Description

Specifies the DIO voltage. No coercion is performed, so the provided value must be exact.

**Valid Values (volts)**

3.3

2.5

1.8

1.5

1.2

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_fpgatemperature.html language=enus -->
## TOPIC 00008: kFlexRIO_FpgaTemperature

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_fpgatemperature.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_fpgatemperature.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_FpgaTemperature

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeDouble | double | Read Only | N/A | None | None |

#### Description

Indicates the current FPGA temperature in degrees Celsius.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_iocfilterenable.html language=enus -->
## TOPIC 00009: kFlexRIO_IocFilterEnable

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_iocfilterenable.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_iocfilterenable.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_IocFilterEnable

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeBool | uint32_t | Read/Write | N/A | None | None |

#### Description

Enables the interleaving offset correction filter for the ADC.

For devices with interleaving ADCs, the data stream may require additional processing to remove the interleaving spur caused by offset errors between the ADC cores. This property is used to enable or disable this functionality. This attribute is only present on devices that support this functionality.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_ioerror.html language=enus -->
## TOPIC 00010: kFlexRIO_IoError

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_ioerror.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_ioerror.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_IoError

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | N/A | None | None |

#### Description

Reports error codes when the I/O module enters an error state.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_ioready.html language=enus -->
## TOPIC 00011: kFlexRIO_IoReady

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_ioready.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_ioready.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_IoReady

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeBool | uint32_t | Read/Write | N/A | None | None |

#### Description

Indicates whether the I/O is ready.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_phasedacvalue.html language=enus -->
## TOPIC 00012: kFlexRIO_PhaseDacValue

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_phasedacvalue.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_phasedacvalue.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_PhaseDacValue

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | N/A | None | None |

#### Description

Specifies the value of the clock phase digital-to-analog converter (DAC).

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_powerlimit.html language=enus -->
## TOPIC 00013: kFlexRIO_PowerLimit

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_powerlimit.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_powerlimit.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_PowerLimit

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeDouble | double | Read Only | N/A | None | None |

#### Description

Indicates the level of total power consumption in watts at which the device shuts down to prevent damage.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_referenceclockrate.html language=enus -->
## TOPIC 00014: kFlexRIO_ReferenceClockRate

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_referenceclockrate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_referenceclockrate.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_ReferenceClockRate

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeDouble | double | Read Only | N/A | None | None |

#### Description

Indicates the rate of the reference clock.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_referenceclocksource.html language=enus -->
## TOPIC 00015: kFlexRIO_ReferenceClockSource

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_referenceclocksource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_referenceclocksource.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_ReferenceClockSource

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | N/A | None | niFlexRIO_ConfigureForReferenceClock |

#### Description

Specifies the Reference Clock source. The Reference Clock is the clock to which a device phase locks another, usually faster, clock. A common source for the Reference Clock is the 10 MHz oscillator signal that is present on the PXI backplane.

**Defined Values**

| 1 | kFlexRIO_RefClkSrc_Onboard | Specifies the onboard Reference Clock. |
| --- | --- | --- |
| 2 | kFlexRIO_RefClkSrc_PXI_Clk10 | Specifies a PXI backplane clock. |
| 3 | kFlexRIO_RefClkSrc_External | Specifies an external Reference Clock. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampleclocksource.html language=enus -->
## TOPIC 00016: kFlexRIO_SampleClockSource

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampleclocksource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampleclocksource.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_SampleClockSource

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeInt32 | int32_t | Read/Write | N/A | None | None |

#### Description

Specifies the sample clock source.

**Defined Values**

| 0 | kFlexRIO_SampleClkSrc_Internal | Specifies an internally generated sample clock. |
| --- | --- | --- |
| 1 | kFlexRIO_SampleClkSrc_External | Specifies an external clock terminal on the front panel. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampleclocktimebaserate.html language=enus -->
## TOPIC 00017: kFlexRIO_SampleClockTimebaseRate

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampleclocktimebaserate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampleclocktimebaserate.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_SampleClockTimebaseRate

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeDouble | double | Read/Write | N/A | None | None |

#### Description

Specifies the sample clock timebase rate.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampledt.html language=enus -->
## TOPIC 00018: kFlexRIO_SampleDt

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampledt.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_sampledt.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_SampleDt

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeDouble | double | Read/Write | Stream | None | None |

#### Description

Specifies the time interval between samples. This value is used to populate the waveform infomation during a stream read. This value is set by default but can be set manually. Setting this value to 0 allows the driver to override.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_starttriggerfortclkoutputterminal.html language=enus -->
## TOPIC 00019: kFlexRIO_StartTriggerForTClkOutputTerminal

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_starttriggerfortclkoutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_starttriggerfortclkoutputterminal.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_StartTriggerForTClkOutputTerminal

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeString | char* | Read/Write | Trigger | None | None |

#### Description

Specifies the export destination for the TClk conditioned start trigger.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/attrkflexrio_starttriggeroutputterminal.html language=enus -->
## TOPIC 00020: kFlexRIO_StartTriggerOutputTerminal

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/attrkflexrio_starttriggeroutputterminal.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/attrkflexrio_starttriggeroutputterminal.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

kFlexRIO_StartTriggerOutputTerminal

#### Specific Attribute

| Attribute ID type | Datatype | Access | Applies to | Coercion | High Level Functions |
| --- | --- | --- | --- | --- | --- |
| FlexRIO_AttributeString | char* | Read/Write | Trigger | None | None |

#### Description

Specifies the export destination for the start trigger.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/channel_packer.html language=enus -->
## TOPIC 00021: Channel Packer

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/channel_packer.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/channel_packer.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Channel Packer

Repackages inbound data into a larger output array. For example, a module that produces 2 samples per clock can be reformatted into one that produces 8 samples per data valid at 1/4 the frequency. In the FlexRIO design libraries, this is used to format the data into words that can be more efficiently used with DRAM. The selected output samples per clock should be set to a value that allows this VI to produce a unit that completely fills a DRAM word. For example, if the DRAM interface is 512 bits wide and 16-bit data is being stored, then you should set the output to have 32 samples (512/16 = 32).

[IMAGE alt='Channel Packer' src='../flexrio_api_fpga_v1_lvlib_channel_packerc.gif']

|  | output spc specifies the output samples per clock cycle. Set this parameter to a value that allows this VI to produce a unit that completely fills a DRAM word. For example, if the DRAM interface is 512 bits wide and 16-bit data is stored, set the output to 32 samples (512/16 = 32). |
| --- | --- |
|  | Array in specifies an array of channel data. |
|  | data valid specifies whether the input data is valid. |
|  | Array out returns the input data repackaged into a larger output array. |
|  | full indicates when the requested output samples per clock is met. This value is TRUE for one clock cycle when the last required data valid is received. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/create_resource.html language=enus -->
## TOPIC 00022: Create Resource

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/create_resource.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/create_resource.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Create Resource

Creates a reference to a DRAM FIFO. Select the instance that corresponds to the data width of the DRAM being accessed.

#### Create 64x1 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 64x1 DRAM FIFO' src='../create_64x1_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U64 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 64x2 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 64x2 DRAM FIFO' src='../create_64x2_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U64 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U64 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 128x1 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 128x1 DRAM FIFO' src='../create_128x1_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U128 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 128x2 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 128x2 DRAM FIFO' src='../create_128x2_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U128 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U128 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 256x1 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 256x1 DRAM FIFO' src='../create_256x1_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U256 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 256x2 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 256x2 DRAM FIFO' src='../create_256x2_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U256 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U256 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 384x1 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 384x1 DRAM FIFO' src='../create_384x1_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U384 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 384x2 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 384x2 DRAM FIFO' src='../create_384x2_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U384 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U384 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 512x1 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 512x1 DRAM FIFO' src='../create_512x1_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U512 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

#### Create 512x2 DRAM FIFO (VI)

Creates a reference to a DRAM FIFO.

[IMAGE alt='Create 512x2 DRAM FIFO' src='../create_512x2_dram_fifo.gif']

|  | memory refnum identifies a memory item implemented using DRAM through which to stream data. Use the U512 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
| --- | --- |
|  | memory refnum 2 identifies a second memory item implemented using DRAM through which to stream data. Use the U512 custom control at <LabVIEW>\\instr.lib\\_niInstr\\Memory\\v1\\FPGA\\Memory\\Public as the data type when configuring the memory properties of this memory item. If the DRAM FIFO is executed in simulation mode, this parameter must point to a memory item that allocates 1MB of memory or less. Simulating more than 1MB of DRAM memory may result in an error. |
|  | actual # of DRAM elements defines the depth of the FIFO. This value must equal the actual number of elements indicated on the Memory Properties page for the memory item. Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | Note The address length does not double for the x2 implementation. The DRAM data width doubles in size. |
|  | DRAM FIFO ref out returns the reference to the DRAM FIFO. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/dram_to_channel_arbiter.html language=enus -->
## TOPIC 00023: DRAM to Channel Arbiter

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/dram_to_channel_arbiter.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/dram_to_channel_arbiter.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

DRAM to Channel Arbiter

Identifies the channel contained in the current DRAM word.

[IMAGE alt='DRAM to Channel Arbiter' src='../flexrio_api_fpga_v1_lvlib_dram_to_channel_arbiterc.gif']

|  | reset resets the state of this VI. |
| --- | --- |
|  | channels enabled specifies which channels are enabled. |
|  | input valid indicates whether the input data is valid on this clock cycle. |
|  | channel count specifies the number of channels enabled. |
|  | valid channel outputs a bitmask that indicates which channel is valid. |
|  | output valid indicates whether the output data is is valid on this clock cycle. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/enableqsfplowpowermode.html language=enus -->
## TOPIC 00024: Enable QSFP Low Power Mode (VI)

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/enableqsfplowpowermode.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/enableqsfplowpowermode.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Enable QSFP Low Power Mode (VI)

Enables low power mode for the QSFP+ modules connected to all ports. True enables low power mode. False enables high power mode.

[IMAGE alt='enable_low_power_qsfp' src='../enable_low_power_qsfp.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA interface palette. |
| --- | --- |
|  | enable enables low power mode for the QSFP+ modules connected to both PORT 0 and PORT 1. Choose true to enable low power mode. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fpga interface out returns a reference to the VI on the FPGA interface palette. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/flexrio_host_customattributeread.html language=enus -->
## TOPIC 00025: FlexRIO Host Custom Attribute Read

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/flexrio_host_customattributeread.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/flexrio_host_customattributeread.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Custom Attribute Read

Queries the current value of the specified attribute.

[IMAGE alt='FlexRIO Host Custom Attribute Read VI' src='../flexrio_host_customattributeread.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Attribute specifies which custom attribute to query. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | Value returns the value read from the specified custom attribute. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/flexrio_host_customattributewrite.html language=enus -->
## TOPIC 00026: FlexRIO Host Custom Attribute Write

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/flexrio_host_customattributewrite.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/flexrio_host_customattributewrite.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Custom Attribute Write

Writes a value to the specified custom attribute.

[IMAGE alt='FlexRIO Host Custom Attribute Write VI' src='../flexrio_host_customattributewrite.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Attribute specifies which custom attribute to write to. |
|  | Value specifies the value to write to the specified attribute. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/flexrio_host_get_device_status.html language=enus -->
## TOPIC 00027: FlexRIO Host Get Device Status

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/flexrio_host_get_device_status.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/flexrio_host_get_device_status.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Get Device Status

Queries the current status of the specified hardware device.

|  |
| --- |

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | Device State returns the device's status as an enum. Values: Status Description Normal The device is operating normally. Internal Error 1 — Internal Error 2 — Internal Error 3 — Internal Error 4 — Internal Error 5 — Fan Slowed The device fan has slowed. Refer to the NI-7931R/7932R/7935R User Manual for information about troubleshooting the fan. Fan Stopped The device fan has stopped. Refer to the NI-7931R/7932R/7935R User Manual for information about troubleshooting the fan. PLL Loss of Lock The phase-locked loop (PLL) has become unlocked. Ensure that the PLL is operating in the frequency range listed in your device's specifications document. Internal Error 6 — Internal Error 7 — Internal Error 8 — Internal Error 9 — Thermal Shutdown The FPGA has overheated and the device has shut down. Refer to the NI-7931R/7932R/7935R User Manual for more information about power/thermal protection and shutdown. Power Shutdown The device has shut down. Refer to the NI-7931R/7932R/7935R User Manual for more information about power/thermal protection and shutdown. Fixed Logic Version Mismatch The device is unusable due to an incompatible firmware version. Use the RIO Device Setup Utility to update the flash with a new bitfile. USB Over Current The USB device is overdrawing current. Refer to your device's specifications document for allowable current draw. Internal Error 10 — |
| Status | Description |
| Normal | The device is operating normally. |
| Internal Error 1 | — |
| Internal Error 2 | — |
| Internal Error 3 | — |
| Internal Error 4 | — |
| Internal Error 5 | — |
| Fan Slowed | The device fan has slowed. Refer to the NI-7931R/7932R/7935R User Manual for information about troubleshooting the fan. |
| Fan Stopped | The device fan has stopped. Refer to the NI-7931R/7932R/7935R User Manual for information about troubleshooting the fan. |
| PLL Loss of Lock | The phase-locked loop (PLL) has become unlocked. Ensure that the PLL is operating in the frequency range listed in your device's specifications document. |
| Internal Error 6 | — |
| Internal Error 7 | — |
| Internal Error 8 | — |
| Internal Error 9 | — |
| Thermal Shutdown | The FPGA has overheated and the device has shut down. Refer to the NI-7931R/7932R/7935R User Manual for more information about power/thermal protection and shutdown. |
| Power Shutdown | The device has shut down. Refer to the NI-7931R/7932R/7935R User Manual for more information about power/thermal protection and shutdown. |
| Fixed Logic Version Mismatch | The device is unusable due to an incompatible firmware version. Use the RIO Device Setup Utility to update the flash with a new bitfile. |
| USB Over Current | The USB device is overdrawing current. Refer to your device's specifications document for allowable current draw. |
| Internal Error 10 | — |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/flexrioapi_fpga.html language=enus -->
## TOPIC 00028: FlexRIO API FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/flexrioapi_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/flexrioapi_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO API FPGA VIs

Expand this book for more information about FlexRIO API FPGA VIs.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/flexrioapi_host.html language=enus -->
## TOPIC 00029: FlexRIO API VI Reference

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/flexrioapi_host.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/flexrioapi_host.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO API VI Reference

FlexRIO VIs provide common functionality including streaming, synchronization, clocking configuration, and I/O configuration. You can use the FlexRIO API with the default FPGA image to acquire data with your FlexRIO device without programming to the FPGA.

| Palette Object | Description |
| --- | --- |
| Open | Opens a streaming session to the specified FlexRIO device using the default FPGA image and creates a session reference you can use to identify this streaming session in subsequent FlexRIO API VI calls. |
| Configure Stream | Configures enabled channels and number of samples in the stream. |
| Start Stream | Activates a stream. |
| Read Stream | Returns data read from a specified stream. |
| Close | Closes the streaming session, destroys the session reference, and deallocates resources associated with that session. Call this VI once for each unique named session that you have created. |

| Subpalette | Description |
| --- | --- |
| Utility | Use the Utility VIs for tasks such as signal routing and reading and writing configuration data to the FlexRIO device's flash memory. |
| Configuration | Use the Configuration VIs to configure triggers and clock properties. |
| Stream | Use the Stream VIs to configure streaming properties such as enabled channels and the number of samples to transfer. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/frio_hostinterface_attributes.html language=enus -->
## TOPIC 00030: FlexRIO Host Interface Attributes

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/frio_hostinterface_attributes.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/frio_hostinterface_attributes.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Interface Attributes

| Attribute | Type | Description |
| --- | --- | --- |
| IO Module Present | Bool | TRUE if an adapter module is detected by the FlexRIO device. |
| IO Module Power Good | Bool | Displays the status of TB_Power_Good signal from the adapter module. |
| Vcco Programmed Successfully | Bool | TRUE if Vcco was programmed successfully. |
| PXI_CLK10 Present(NI PXI-795xR only) | Bool | TRUE if the FlexRIO device can detect the PXI_CLK10 clock. |
| IO Module I/O Enabled | Bool | TRUE if the adapter module I/O is enabled. |
| IO Module Power Enabled | Bool | TRUE if the adapter module power is enabled. |
| EEPROM Power Enabled | Bool | TRUE if the power is enabled to the EEPROM on the adapter module. |
| IO Module Power Good Timed Out | Bool | TRUE if the adapter module did not drive the TB_Power_Good pin within the time the FlexRIO device expected. |
| IO Module ID Mismatch | Bool | TRUE if the IO Module ID expected by the current VI downloaded to the FPGA is different from the ID of the adapter module that is currently connected to the FlexRIO device. |
| IO Module ID Read Timeout | Bool | TRUE if the IO Module ID expected by the current VI downloaded to the FPGA was not received within the time the FlexRIO device expected. |
| Inserted IO Module ID | U32 | Returns the IO Module ID of the adapter module that is currently connected to the FlexRIO device. |
| Expected IO Module ID | U32 | Returns the I/O Module ID that the current VI downloaded to the FPGA is configured to use. |
| Current Temperature | U32 | Returns the current temperature of the PCB temperature sensor in units of 0.25 °. |
| Vcco A Value (raw)(NI PXI-795xR and NI PXIe-796xR only) | U32 | Returns the Vcco A raw DAC value. |
| Vcco B Value (raw)(NI PXI-795xR and NI PXIe-796xR only) | U32 | Returns the Vcco B raw DAC value. |
| Signature | U32 | Returns the 32-bit signature for the FlexRIO device. |
| Revision | U32 | Returns the present FPGA revision in YYMMDDHH format. |
| Oldest Compatible Revision | U32 | Contains the latest date at which a modification was performed on this FPGA which would break software compatibility, in YYMMDDHH format, if the software built for a date after this value is considered to be compatible. |
| IO Module State | U32 | Returns the current state of the IO Module manager. |
| I2CMux | U32 | Returns the current owner of the I2C Bus.Possible values are: None, Hardware, Software, and LVFPGA |
| Inserted IO Module Has EEPROM | Bool | Returns TRUE if the inserted adapter module has an EEPROM that can be detected, or FALSE if no EEPROM is detected. |
| Expected IO Module Has EEPROM | Bool | Returns TRUE if the expected adapter module has an EEPROM, or FALSE if no EEPROM is expected. |
| Is IO Module Supported | Bool | Returns TRUE if adapter modules are supported by the selected FlexRIO device. |
| PXIe_CLK100 Locked?(NI PXIe-796xR NI PXIe-797xR only) | Bool | Returns TRUE if the base clock PLL is locked to the PXIe 100 MHz Clock. |
| Serial Number | U32 | Returns the serial number of the FlexRIO FPGA module. |
| IO Module Serial Number | U32 | Returns the serial number of the FlexRIO adapter module. |
| Fan Speed(NI-793xR only) | U32 | Returns the speed of the device fan in RPM. |
| FAN PWM(NI-793xR only) | U32 | Returns the PWM (pulse width modulation) duty cycle, in units of percentage, of the device fan. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/frio_lv_hostvis.html language=enus -->
## TOPIC 00031: FlexRIO LabVIEW Host VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/frio_lv_hostvis.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/frio_lv_hostvis.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO LabVIEW Host VIs

All FlexRIO Host VIs are found in the following LLB: 
C:\Program Files\National Instruments\LabVIEW\vi.lib\FlexRIO\FlexRIO_HostInterface.llb

NI recommends using the [System Configuration API](ni.com/docs/csh?context=flexrio_flexriointegratedmerge_sysconfigapi) in all cases where you are querying an attribute.

|  | Caution The Host VIs provide low-level access to the FlexRIO device. Improper use of these VIs can damage the FlexRIO and put it in an unrecoverable state. |
| --- | --- |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_control_iomodpower.html language=enus -->
## TOPIC 00032: FlexRIO Host Control IO Module Power

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_control_iomodpower.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_control_iomodpower.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Control IO Module Power

Use this VI to enable or disable power to the adapter module.

|  | Note This VI returns an error if the inserted adapter module does not match the IO Module ID expected by the current VI downloaded to the FlexRIO FPGA. |
| --- | --- |

[IMAGE alt='FlexRIO Host Control IO Module Power VI' src='../host_controliomodpower.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Enabled—When TRUE, power to the adapter module is enabled if it is compatible with the bitstream currently downloaded to the FPGA. When FALSE, power to the adapter module is disabled. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_eepromread32.html language=enus -->
## TOPIC 00033: FlexRIO Host EEPROM Read 32

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_eepromread32.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_eepromread32.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host EEPROM Read 32

Use this VI to read an unsigned 32-bit number from the adapter module EEPROM at the specified address.

[IMAGE alt='FlexRIO Host EEPROM Read 32 VI' src='../host_eepromread32.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Address specifies the EEPROM byte address to read from. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | Data returns the data that was read from the EEPROM at the specified byte address. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_eepromwrite32.html language=enus -->
## TOPIC 00034: FlexRIO Host EEPROM Write 32

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_eepromwrite32.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_eepromwrite32.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host EEPROM Write 32

Use this VI to write an unsigned 32-bit number to the adapter module EEPROM at the specified address.

[IMAGE alt='FlexRIO Host EEPROM Write 32 VI' src='../host_eepromwrite32.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Address specifies the EEPROM byte address to write to. |
|  | Data specifies the 32-bit data value to write to the EEPROM. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_getdeviceshutdownlimit.html language=enus -->
## TOPIC 00035: FlexRIO Host Get Device Shutdown Limit

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_getdeviceshutdownlimit.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_getdeviceshutdownlimit.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Get Device Shutdown Limit

This VI returns the device's thermal shutdown limit.

[IMAGE alt='host get device status' src='../flexrio_host_getdeviceshutdownlimit.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Shutdown Type Description - specifies what type of shutdown to configure. Valid values: Thermal Total Power 3.3V Power 12V Power |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | Value in deg C or mW returns the device's thermal shutdown limit. If you specified Thermal in Shutdown Type, this value is returned in °C. If you specified Total Power, 3.3V Power or 12V Power in Shutdown Type, this value is returned in mW. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_i2caccesscontrol.html language=enus -->
## TOPIC 00036: FlexRIO Host I2C Access Control

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_i2caccesscontrol.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_i2caccesscontrol.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host I<sup>2</sup>C Access Control

Use this VI to acquire or release software access to the adapter module I<sup>2</sup>C bus. FlexRIO firmware has an arbiter that controls access to the I<sup>2</sup>C bus on the adapter module interface. Before issuing any I<sup>2</sup>C bus commands to the adapter module, software must first acquire access to the I<sup>2</sup>C bus. The FlexRIO host interface gives you the ability to perform raw I<sup>2</sup>C bus cycles by using the FlexRIO Host I2C Issue Bus Cycle VI. Because this VI makes no assumptions about I<sup>2</sup>C command composition, you must use the FlexRIO Host I2C Access Control VI to acquire and release access to the bus before and after issuing your I<sup>2</sup>C command.

|  | Note You do not need to use this VI with the FlexRIO EEPROM Host Interface VIs. The FlexRIO Host Interface VIs all acquire and release access to the I2C bus internally. |
| --- | --- |

|  | Note When you are finished acquiring access to the I2C bus, you must always release software access to the I2C bus. |
| --- | --- |

[IMAGE alt='FlexRIO Host I2C Access Control VI' src='../host_i2caccesscontrol.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Method specifies whether you want to acquire or release access to the I2C bus. |
|  | Timeout in msec (1000) specifies the number of milliseconds the VI waits before timing out. -1 indicates that the timeout waits indefinitely. The default is 1000 ms. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_i2cissuebuscycle.html language=enus -->
## TOPIC 00037: FlexRIO Host I2C Issue Bus Cycle

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_i2cissuebuscycle.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_i2cissuebuscycle.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host I<sup>2</sup>C Issue Bus Cycle

Use this VI to issue a single cycle on the I<sup>2</sup>C bus. Choosing multiple instances of this VI simultaneously also allows you to issue custom I<sup>2</sup>C commands on the adapter module I<sup>2</sup>C bus. This is useful for accessing custom I<sup>2</sup>C circuitry that may exist on custom adapter modules.

|  | Note Before calling this VI, you must first acquire software access to the I2C bus by calling the FlexRIO Host I2C Access Control VI. |
| --- | --- |

[IMAGE alt='FlexRIO Host I2C Issue Bus Cycle VI' src='../host_i2cissuebuscycle.gif']

|  | Start bit?—When TRUE, causes the I2C controller to issue a start bit with the I2C bus cycle. When FALSE, the I2C controller does not issue a start bit with the I2C bus cycle. |
| --- | --- |
|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
|  | Command specifies whether the I2C bus cycle is performing a write or read operation. |
|  | Write Data is the raw data that is written to the I2C bus when performing a write operation. |
|  | Expect Ack?—When TRUE, causes the I2C controller to wait for an acknowledge bit before finishing the I2C bus cycle. When FALSE, the I2C controller does not wait for an acknowledge bit. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | Stop bit?—When TRUE, causes the I2C controller to issue a stop bit with the I2C bus cycle. When FALSE, the I2C controller does not issue a stop bit with the I2C bus cycle. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | Read Data is the raw data that was read from the I2C bus when performing a read operation. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_programiomodid.html language=enus -->
## TOPIC 00038: FlexRIO Host Program IO Module ID

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_programiomodid.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_programiomodid.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Program IO Module ID

Use this VI to program the IO Module ID to the EEPROM on the adapter module.

|  | Note Only use this VI to program custom adapter modules. Do not use this VI to reprogram the IO Module ID on an adapter module that you did not manufacture. |
| --- | --- |

[IMAGE alt='FlexRIO Host Program IO Module ID VI' src='../host_programiomodid.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | IO Module ID specifies the unique, 32-bit IO Module ID of your adapter module. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_queryattribute.html language=enus -->
## TOPIC 00039: FlexRIO Host Query Attribute

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_queryattribute.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_queryattribute.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Query Attribute

Use this VI to query the current value of the [selected attribute](frio_hostinterface_attributes.html).

[IMAGE alt='FlexRIO Host Query Attribute VI' src='../host_queryattribute.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Attribute specifies which attribute to query. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | Value returns the value of specified attribute. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_queryiomodid.html language=enus -->
## TOPIC 00040: FlexRIO Host Query IO Module ID

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_queryiomodid.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_queryiomodid.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Query IO Module ID

Use this VI to read the IO Module ID from the adapter module.

[IMAGE alt='FlexRIO Host Query IO Module ID VI' src='../host_queryiomodid.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | IO Module ID returns the IO Module ID of the connected adapter module. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_queryiomodmgrstate.html language=enus -->
## TOPIC 00041: FlexRIO Host Query IO Module Manager State

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_queryiomodmgrstate.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_queryiomodmgrstate.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Query IO Module Manager State

Use this VI to query the current state of the connected adapter module.

[IMAGE alt='FlexRIO Host Query IO Module Manager State VI' src='../host_queryiomodmgrstate.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | State returns the current state of the adapter module. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_redetectiomod.html language=enus -->
## TOPIC 00042: FlexRIO Host Redetect IO Module

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_redetectiomod.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_redetectiomod.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Redetect IO Module

Use this VI to cause the selected FlexRIO device to redetect the adapter module.

[IMAGE alt='FlexRIO Host Redetect IO Module VI' src='../host_redetectiomod.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/host_setdeviceshutdownlimit.html language=enus -->
## TOPIC 00043: FlexRIO Host Set Device Shutdown Limit

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/host_setdeviceshutdownlimit.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/host_setdeviceshutdownlimit.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Host Set Device Shutdown Limit

Use this VI to set the device's thermal shutdown limit.

[IMAGE alt='host get device status' src='../flexrio_host_setdeviceshutdownlimit.gif']

|  | RIO Device specifies the resource name of the FlexRIO device that this VI should use. You can configure the resource name for each FlexRIO device in your system by using Measurement & Automation Explorer (MAX). |
| --- | --- |
|  | Shutdown Type Description - specifies what type of shutdown to configure. Valid values: Thermal Total Power 3.3V Power 12V Power |
|  | Value in deg C or mW specifies the device's thermal shutdown limit. If you specified Thermal in Shutdown Type, this value is specified in °C. If you specified Total Power, 3.3V Power or 12V Power in Shutdown Type, this value is specified in mW. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | RIO Device Out returns a duplicate of the RIO Device value. Use this terminal to chain multiple FlexRIO host interface VIs together. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. If status is TRUE, code is a nonzero error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where and why an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_basicelements_fpga.html language=enus -->
## TOPIC 00044: Basic Elements FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_basicelements_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_basicelements_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Basic Elements FPGA VIs

#### Detect Falling Edge.vi

Detects a transition from TRUE to FALSE on the input signal.

Use the Detect Falling Edge VI inside a single-cycle Timed Loop.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Detect Falling Edge.vi' src='../idl_basicelements_fpgac.gif']

**Input Parameters**

**signal** specifies the signal in which to detect a TRUE to FALSE transition.

**Output Parameters**

**edge detected** indicates whether a TRUE to FALSE transition is detected on the input signal.

#### Detect Rising Edge.vi

Detects a transition from FALSE to TRUE on the input signal.

Use the Detect Rising Edge VI inside a single-cycle Timed Loop.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Detect Rising Edge.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_detect_rising_edgec.gif']

**Input Parameters**

**signal** specifies the signal in which to detect a FALSE to TRUE transition.

**Output Parameters**

**edge detected** indicates whether a FALSE to TRUE transition is detected on the input signal.

#### Synchronous Latch.vi

The VI stores information about the previous TRUE values of the signal. You can reset the VI to search for another TRUE value of the same signal.

If the value of the **set** parameter is TRUE and the value of the **clear** parameter is FALSE, the VI output is TRUE.

If the value of the **clear** parameter is TRUE and the value of the **set** parameter is FALSE, the VI output is FALSE.

If the values of both the **set** and the **clear** parameters are FALSE, the output of the VI remains unchanged from the previous value.

If the values of both the **set** and the **clear** parameters are TRUE, the VI output is FALSE.

The internal state of the VI is not reset when the owning VI stops execution. The internal state of the VI is reset to FALSE when the owning VI is compiled or loaded. The internal state is also reset when the value of the **clear** parameter is set to TRUE.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Synchronous Latch.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_synchronous_latchc.gif']

**Input Parameters**

**set** specifies that the internal state of the VI is set to TRUE.

**clear** specifies that the internal state of the VI is set to FALSE.

**Output Parameters**

**out** indicates the internal state retained within the VI.

#### Read U128 FIFO.vi

Reads data from a 128-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read method, and exposes handshaking signals that control when to read data from the FIFO.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Read U128 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_read_u128_fifoc.gif']

**Input Parameters**

**fifo** specifies the reference to the FIFO from which to read data. Configure the FIFO to use a 128-bit data type. Use the following typedef of this library to configure the FIFO's data type: <instr.lib>\_niInstr\Basic Elements\v1\FPGA\Public\U128.ctl.

**ready for output** specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data.

**Output Parameters**

**output data** returns the data read from the FIFO.

**output data.high** returns the higher 64-bits of the 128-bit data read from the FIFO.

**output data.low** returns the lower 64-bits of the 128-bit data read from the FIFO.

**output valid** indicates whether the output data read from the FIFO is valid during the current clock cycle.

#### Read U16 FIFO.vi

Reads data from a 16-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read method, and exposes handshaking signals to control when data is read from the FIFO.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Read U16 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_read_u16_fifoc.gif']

**Input Parameters**

**fifo** specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U16 datatype.

**ready for output** specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data.

**Output Parameters**

**output data** returns the data read from the FIFO.

**output valid** indicates whether the output data read from the FIFO is valid during the current clock cycle.

#### Read U32 FIFO.vi

Reads data from a 32-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read method, and exposes handshaking signals to control when data is read from the FIFO.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Read U32 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_read_u32_fifoc.gif']

**Input Parameters**

**fifo** specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U32 datatype.

**ready for output** specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data.

**Output Parameters**

**output data** returns the data read from the FIFO.

**output valid** indicates whether the output data read from the FIFO is valid during the current clock cycle.

#### Read U64 FIFO.vi

Reads data from a 64-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read method, and exposes handshaking signals to control when data is read from the FIFO.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Read U64 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_read_u64_fifoc.gif']

**Input Parameters**

**fifo** specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U64 datatype.

**ready for output** specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data.

**Output Parameters**

**output data** returns the data read from the FIFO.

**output valid** indicates whether the output data read from the FIFO is valid during the current clock cycle.

#### Read U8 FIFO.vi

Reads data from an 8-bit FIFO. The VI is a wrapper around the LabVIEW FPGA FIFO Read method, and exposes handshaking signals to control when data is read from the FIFO.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Read U8 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_read_u8_fifoc.gif']

**Input Parameters**

**fifo** specifies the reference to the FIFO from which to read data. Configure the FIFO to use the U8 datatype.

**ready for output** specifies whether the consumer of the data read from the FIFO is ready to accept new data. If you set this parameter to TRUE, the consumer is ready to accept new data and this VI is allowed to read data from the FIFO. If you set this parameter to FALSE, this VI does not return new data.

**Output Parameters**

**output data** returns the data read from the FIFO.

**output valid** indicates whether the output data read from the FIFO is valid during the current clock cycle.

#### Write U128 FIFO.vi

Writes data to a 128-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write method, and exposes handshaking signals that inform the user when the FIFO is ready to accept new data.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Write U128 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_write_u128_fifoc.gif']

**Input Parameters**

**input data** specifies the data to write to the FIFO.

**input data.high** specifies the higher 64-bits of the data to write to the FIFO.

**input data.low** specifies the lower 64-bits of the data to be write to the FIFO.

**reset** resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, assert the **reset** signal, and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE.

**fifo** specifies the reference to the FIFO to which data must be written. Configure the FIFO to use a 128-bit data type. Use the following typedef of this library to configure the FIFO's data type: <instr.lib>\_niInstr\Basic Elements\v1\FPGA\Public\U128.ctl.

**input valid** specifies whether the **input data** parameter written to the FIFO is valid during the current clock cycle. The **input data** is written to the FIFO only if it is valid.

**Output Parameters**

**ready for input** indicates whether this VI is ready to write new data to the FIFO in the next clock cycle.

#### Write U16 FIFO.vi

Writes data to a 16-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write method, and exposes handshaking signals that inform the user when the FIFO is ready to accept new data.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Write U16 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_write_u16_fifoc.gif']

**Input Parameters**

**input data** specifies the data to write to the FIFO.

**reset** resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, assert the **reset** signal, and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE.

**fifo** specifies the reference to the FIFO to which data must be written. Configure the FIFO to use the U16 datatype.

**input valid** specifies whether the **input data** being written to the FIFO is valid during the current clock cycle. The **input data** is written to the FIFO only if it is valid.

**Output Parameters**

**ready for input** indicates whether this VI is ready to write new data to the FIFO in the next clock cycle.

#### Write U32 FIFO.vi

Writes data to a 32-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write method and exposes handshaking signals that inform the user when the FIFO is ready to accept new data.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Write U32 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_write_u32_fifoc.gif']

**Input Parameters**

**input data** specifies the data to be written to the FIFO.

**reset** resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, assert the **reset** signal, and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE.

**fifo** specifies the reference to the FIFO to which data must be written. Configure the FIFO to use the U32 datatype.

**input valid** specifies whether the **input data** parameter written to the FIFO is valid during the current clock cycle. The **input data** is written to the FIFO only if it is valid.

**Output Parameters**

**ready for input** indicates whether this VI is ready to write new data to the FIFO in the next clock cycle.

#### Write U64 FIFO.vi

Writes data to a 64-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write method and exposes handshaking signals that inform the user when the FIFO is ready to accept new data.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Write U64 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_write_u64_fifoc.gif']

**Input Parameters**

**input data** specifies the data to be written to the FIFO.

**reset** resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To do so, assert the **reset** signal and call the LabVIEW FPGA FIFO Clear method. No data is written to the FIFO if this parameter is set to TRUE.

**fifo** specifies the reference to the FIFO to which data must be written. Configure the FIFO to use the U64 datatype.

**input valid** specifies whether the **input data** parameter written to the FIFO is valid during the current clock cycle. The **input data** is written to the FIFO only if it is valid.

**Output Parameters**

**ready for input** indicates whether this VI is ready to write new data to the FIFO in the next clock cycle.

#### Write U8 FIFO.vi

Writes data to an 8-bit FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write method, and exposes handshaking signals that inform the user when the FIFO is ready to accept new data.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Write U8 FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_write_u8_fifoc.gif']

**Input Parameters**

**input data** specifies the data to be written to the FIFO.

**reset** resets the handshaking logic directly in front of the LabVIEW FPGA FIFO Write method. This parameter does not reset the entire FIFO. To reset the entire FIFO, the **reset** signal must be asserted and call the LabVIEW FPGA FIFO Clear method should be called. No data is written to the FIFO if this parameter is set to TRUE.

**fifo** specifies the reference to the FIFO to which data must be written. The FIFO should be configured to use the U8 datatype.

**input valid** specifies whether the **input data** parameter written to the FIFO is valid during the current clock cycle. The **input data** is written to the FIFO only if it is valid.

**Output Parameters**

**ready for input** indicates whether this VI is ready to write new data to the FIFO in the next clock cycle.

#### Read FIFO.vi

Reads data from a FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Read method, and exposes handshaking signals to control when data is read from the FIFO.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Read FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_read_fifoc.gif']

#### Write FIFO.vi

Writes data to a FIFO. This VI is a wrapper around the LabVIEW FPGA FIFO Write method, and exposes handshaking signals that inform the user when the FIFO is ready to accept new data.

[IMAGE alt='niInstr Basic Elements v1 FPGA.lvlib:Write FIFO.vi' src='../niinstr_basic_elements_v1_fpga.lvlib_write_fifoc.gif']

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_channel_fpga.html language=enus -->
## TOPIC 00045: Channel FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_channel_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_channel_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Channel FPGA VIs

#### Select And Interleave.vi

Interleaves data from specified channels into a single array. This VI can interleave a number of channels equal to a power of 2 (1, 2, 4, ...).

Triggers and channel data remain aligned with each other when passed through this VI.

[IMAGE alt='niInstr Channel v1 FPGA.lvlib:Select And Interleave.vi' src='../idl_channel_fpgac.gif']

**Input Parameters**

**data in** specifies the data samples to interleave. Each element in this array contains the data from a single channel.

**triggers in** specifies the triggers to pass through the VI. Triggers remain aligned with the **data in** input data. This VI does not manipulate the triggers in any other way.

**input valid** specifies whether the **data in** input contains valid data.

**channel enable mask** specifies which channels will be interleaved. Each bit in this value represents a channel, with bit 0 representing channel 0.

**number of channels to interleave** specifies the number of channels to interleave. This value must be a power of 2.

**reset** resets the registers in the **output valid** path when set to TRUE, allowing for deterministic startup behavior. The registers in the **channel out** path are not reset. However, the **output valid** output returns FALSE while the **reset** input is asserted.

**Output Parameters**

**channel status** contains information about the internal status of the VI.

**channel status.next packed index** specifies the index in **interleaved data out** where this VI will place the next **data in** input sample.

**interleaved data out** contains the interleaved channel data.

**triggers out** contains the trigger information aligned with the interleaved channel data.

**sample format out** contains information about the data in the **interleaved data out** output. Other VIs may require this information.

**output valid** indicates whether the **interleaved data out** output contains valid data. This parameter returns TRUE during clock cycles in which **interleaved data out** contains a valid data sample. Otherwise, this parameter returns FALSE.

#### Select.vi

Returns the channel of **data in** at **channel index**. This VI has a pipeline of 1.

[IMAGE alt='niInstr Channel v1 FPGA.lvlib:Select.vi' src='../niinstr_channel_v1_fpga.lvlib_selectc.gif']

**Input Parameters**

**data in** specifies the data samples for each channel. Each element in this array contains the data from a single channel.

**input valid** specifies whether the **data in** input contains valid data.

**channel index** specifies the index of the channel data to output. Each channel in the **data in** input corresponds to an index, starting with index 0.

**reset** resets the registers in the **output valid** path when set to TRUE, allowing for deterministic startup behavior. The registers in the **channel out** path are not reset. However, the **output valid** output returns FALSE while the **reset** input is asserted.

**Output Parameters**

**channel out** returns the channel data specified by the **channel index** input.

**output valid** indicates whether the **channel out** parameter contains valid data. This parameter returns TRUE during clock cycles in which the **channel out** output contains a valid data sample. Otherwise, this parameter returns FALSE.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4lite.html language=enus -->
## TOPIC 00046: AXI4-Lite

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4lite.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4lite.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

AXI4-Lite

#### Add Address Map Element.vi

Adds the specified Address Map Element to the Address Space Collection.

[IMAGE alt='add address map element' src='../add_address_map_element.gif']

**Input Parameters**

**niInstr AXI4-Lite address space collection v1 FPGA in** is a reference to the Address Space Collection passed in from the previous VI.

**address map element in** contains information related to a specific address map.

**address map element in.UID** is the unique identifier of the address map element.

**address map element in.version** is the version of the address map element.

**address map element in.oldest compatible version** is the oldest version of the address map that is compatible with the current version.

**address map element in.instance** is the specific instance of the specified address map.

**address map element in.number of children** is the number of address map elements which are children of the current address map element.

**address map element in.offset** is the register offset of the Address Map Element on the hardware.

**Output Parameters**

**niInstr AXI4-Lite address space collection v1 FPGA out** passes a reference to the Address Space Collection to the next VI.

#### Create Resources.vi

Creates a new FPGA resource of the selected type.

[IMAGE alt='create resource' src='../create_resources.gif']

This VI contains the following instance VI:

- AXI4-Lite FXP32x1.vi

#### AXI4-Lite FXP32x1

Creates a new FPGA resource of the selected type.

**Input Parameters**

**m_axis_tdata** is the resource to use as TDATA.

**m_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4sreader.html language=enus -->
## TOPIC 00047: AXI4-S Reader

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4sreader.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4sreader.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

AXI4-S Reader

#### Create Reader Resources.vi

Creates resources required for the AXI4-Stream Reader.

[IMAGE alt='create reader resources' src='../axi4_s_reader_create_resources_poly.gif']

|  | Caution Do not place this VI into a case structure or it will not compile correctly. |
| --- | --- |

This VI contains the following instance VIs:

- AXI4-Stream Reader FXP32x1.vi
- AXI4-Stream Reader FXP64x1.vi
- AXI4-Stream Reader FXP64x2.vi
- AXI4-Stream Reader FXP64x4.vi

#### AXI4-Stream Reader FXP32x1.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**m_axis_tdata** is the resource to use as TDATA.

**m_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### AXI4-Stream Reader FXP64x1.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**m_axis_tdata** is the resource to use as TDATA.

**m_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### AXI4-Stream Reader FXP64x2.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**m_axis_tdata** is the resource to use as TDATA.

**m_axis_tdata.m_axis_tdata_0** is the resource to use for the first portion of TDATA.

**m_axis_tdata.m_axis_tdata_1** is the resource to use for the second portion of TDATA.

**m_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### AXI4-Stream Reader FXP64x4.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**m_axis_tdata** is the resource to use as TDATA.

**m_axis_tdata.m_axis_tdata_0** is the resource to use for the first portion of TDATA.

**m_axis_tdata.m_axis_tdata_1** is the resource to use for the second portion of TDATA.

**m_axis_tdata.m_axis_tdata_2** is the resource to use for the third portion of TDATA.

**m_axis_tdata.m_axis_tdata_3** is the resource to use for the fourth portion of TDATA.

**m_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Add Resource.vi

Adds a resource to the AXI4-Stream Writer.

[IMAGE alt='add address map element' src='../axi4_s_reader_add_resource_poly.gif']

|  | Caution Do not place this VI into a case structure or it will not compile correctly. |
| --- | --- |

This VI contains the following instance VIs:

- Enable TLAST.vi
- Enable TREADY.vi
- Enable TSTRB (Stream Reader FXP 32x1).vi
- Enable TKEEP (Stream Reader FXP 32x1).vi
- Enable TSTRB (Stream Reader FXP 64x1).vi
- Enable TKEEP (Stream Reader FXP 64x1).vi
- Enable TSTRB (Stream Reader FXP 64x2).vi
- Enable TKEEP (Stream Reader FXP 64x2).vi
- Enable TSTRB (Stream Reader FXP 64x4).vi
- Enable TKEEP (Stream Reader FXP 64x4).vi

#### Enable TLAST.vi

Enables TLAST to be compiled as part of the AXI4-Stream Writer interface.

[IMAGE alt='enable TLAST' src='../enable_tlast.gif']

**Input Parameters**

**m_axis_tlast** is the signal to use for TLAST.

**niInstr AXI4-Stream Writer v1 FPGA in** receives a reference to the AXI4-Stream Writer from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Writer v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### Enable TREADY.vi

Enables TREADY to be compiled as part of the AXI4-Stream Writer interface.

[IMAGE alt='enable TREADY' src='../enable_tready.gif']

**Input Parameters**

**m_axis_tready** specifies the FPGA resource to use for TREADY.

**niInstr AXI4-Stream Writer v1 FPGA in** receives a reference to the AXI4-Stream Writer from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Writer v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### Enable TSTRB (Stream Reader FXP 32x1).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 32x1).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TSTRB (Stream Reader FXP 64x1).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 64x1).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TSTRB (Stream Reader FXP 64x2).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 64x2).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TSTRB (Stream Reader FXP 64x4).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 64x4).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Read.vi

Performs a read operation on the AXI4-Stream Reader.

[IMAGE alt='Read' src='../read.gif']

**Input Parameters**

**niInstr AXI4-Stream Reader v1 FPGA in** takes in a reference to the AXI4-Stream Reader from the previous VI.

**ready for output** specifies whether the AXI4-Stream Reader is ready to transmit data.

**Output Parameters**

**tlast** is the TLAST signal for the AXI4-Stream Reader.

**tdata** is the TDATA signal for the AXI4-Stream Reader.

**tstrb** is the TSTRB signal for the AXI4-Stream Reader.

**tkeep** is the TKEEP signal for the AXI4-Stream Reader.

**output valid** is true when the output is valid.

**tuser** is the TUSER signal for the AXI4-Stream Reader.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4swriter.html language=enus -->
## TOPIC 00048: AXI4-S Writer

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4swriter.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_clip_adapters_axi4swriter.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

AXI4-S Writer

#### Create Writer Resources.vi

Creates a new FPGA resource of the selected type.

[IMAGE alt='create writer resources' src='../axi4_s_writer_create_resources_poly.gif']

|  | Caution Do not place this VI into a case structure or it will not compile correctly. |
| --- | --- |

This VI contains the following instance VIs:

- AXI4-Stream Writer FXP32x1.vi
- AXI4-Stream Writer FXP64x1.vi
- AXI4-Stream Writer FXP64x2.vi
- AXI4-Stream Writer FXP64x4.vi

#### AXI4-Stream Writer FXP32x1.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**s_axis_tdata** is the FPGA resource to use as TDATA.

**s_axis_tvalid** is the FPGA resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Writer FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### AXI4-Stream Writer FXP64x1.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**s_axis_tdata** is the FPGA resource to use as TDATA.

**s_axis_tvalid** is the FPGA resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Writer FXP64x1 v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### AXI4-Stream Writer FXP64x2.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**s_axis_tdata** is the FPGA resource to use as TDATA.

**s_axis_tdata.s_axis_tdata_0** is the resource to use for the first portion of TDATA.

**s_axis_tdata.s_axis_tdata_1** is the resource to use for the second portion of TDATA.

**s_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Writer FXP64x2 v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### AXI4-Stream Writer FXP64x4.vi

Creates a new FPGA resource of the selected type.

**Input Parameters**

**s_axis_tdata** is the resource to use as TDATA.

**s_axis_tdata.s_axis_tdata_0** is the resource to use for the first portion of TDATA.

**s_axis_tdata.s_axis_tdata_1** is the resource to use for the second portion of TDATA.

**s_axis_tdata.s_axis_tdata_2** is the resource to use for the third portion of TDATA.

**s_axis_tdata.s_axis_tdata_3** is the resource to use for the fourth portion of TDATA.

**s_axis_tvalid** is the resource to use as TVALID.

**Output Parameters**

**niInstr AXI4-Stream Writer FXP64x4 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Add Resource.vi

Adds a resource to the AXI4-Stream Writer.

[IMAGE alt='add address map element' src='../axi4_s_writer_add_resource_poly.gif']

|  | Caution Do not place this VI into a case structure or it will not compile correctly. |
| --- | --- |

This VI contains the following instance VIs:

- Enable TLAST.vi
- Enable TREADY.vi
- Enable TSTRB (Stream Reader FXP 32x1).vi
- Enable TKEEP (Stream Reader FXP 32x1).vi
- Enable TSTRB (Stream Reader FXP 64x1).vi
- Enable TKEEP (Stream Reader FXP 64x1).vi
- Enable TSTRB (Stream Reader FXP 64x2).vi
- Enable TKEEP (Stream Reader FXP 64x2).vi
- Enable TSTRB (Stream Reader FXP 64x4).vi
- Enable TKEEP (Stream Reader FXP 64x4).vi

#### Enable TLAST.vi

Enables TLAST to be compiled as part of the AXI4-Stream Writer interface.

[IMAGE alt='enable TLAST' src='../enable_tlast.gif']

**Input Parameters**

**m_axis_tlast** is the signal to use for TLAST.

**niInstr AXI4-Stream Writer v1 FPGA in** receives a reference to the AXI4-Stream Writer from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Writer v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### Enable TREADY.vi

Enables TREADY to be compiled as part of the AXI4-Stream Writer interface.

[IMAGE alt='enable TREADY' src='../enable_tready.gif']

**Input Parameters**

**m_axis_tready** specifies the FPGA resource to use for TREADY.

**niInstr AXI4-Stream Writer v1 FPGA in** receives a reference to the AXI4-Stream Writer from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Writer v1 FPGA out** passes a reference to the AXI4-Stream Writer to the next VI.

#### Enable TSTRB (Stream Reader FXP 32x1).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 32x1).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP32x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TSTRB (Stream Reader FXP 64x1).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 64x1).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x1 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TSTRB (Stream Reader FXP 64x2).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 64x2).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x2 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TSTRB (Stream Reader FXP 64x4).vi

Controls whether to generate TSTRB as part of the FPGA bitstream.

[IMAGE alt='enable TSTRB' src='../enable_tstrb.gif']

**Input Parameters**

**m_axis_tstrb** is the resource to use as TSTRB.

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Enable TKEEP (Stream Reader FXP 64x4).vi

Controls whether to generate TKEEP as part of the FPGA bitstream.

[IMAGE alt='Enable TKEEP' src='../enable_tkeep.gif']

**Input Parameters**

**m_axis_tkeep** is the resource to use as TKEEP.

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA in** receives a reference to the AXI4-Stream Reader from the previous VI.

**Output Parameters**

**niInstr AXI4-Stream Reader FXP64x4 v1 FPGA out** passes a reference to the AXI4-Stream Reader to the next VI.

#### Write.vi

Performs a write operation on the AXI4-Stream Writer.

[IMAGE alt='write' src='../write.gif']

**Input Parameters**

**tdata** is the data to write using the AXI4-Stream Writer.

**tlast** indicates whether this data is at the boundary of a packet.

**niInstr AXI4-Stream Writer v1 FPGA in** takes in a reference to the AXI4-Stream Writer from the previous VI.

**tstrb** is the byte qualifier which indicates whether the content of the associated byte of **tdata** is a data byte or a position byte.

**tkeep** is the byte qualifier which indicates whether to process the associated TDATA byte. Bytes associated with a deasserted TKEEP are null bytes and can be removed from the data stream.

**input valid** indicates whether or not the data on this clock cycle is valid.

**tuser** is user-defined sideband information that can be transmitted alongside the data stream.

**Output Parameters**

**ready for input** indicates whether the bus interface is ready to receive more data.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_datamanip_host.html language=enus -->
## TOPIC 00049: Data Manipulation Host VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_datamanip_host.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_datamanip_host.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Data Manipulation Host VIs

#### Reshape.vi

Changes the dimension size(s) of an array according to the size value(s). The elements of the array are not changed or initialized.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Reshape.vi' src='../idl_datamanip_hostc.gif']

**Input Parameters**

**array** specifies the array to reshaped.

**size or dimension size** specifies the dimension(s) of **array**.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**reshaped array** is an array of the size specified by **size**. If **size** is larger than the size of **array**, new uninitialized elements are added to the end. While the size of **array** may be changed, no elements in the array will be changed.

**allocated more space** indicates if the function resulted in new memory being allocated.

**error out** contains error information. This output provides standard **error out** functionality.

#### Typecast, Deinterleave, and Scale.vi

Replaces portions of **data in** at the point you specify in **data in index 0** and **data in index 1** using **new data**. The function takes **new data** and typecasts the array using the type specified in **typecast type**. The resulting type casted data is deinterleaved and scaled before being placed in **data in**. The deinterleaving and scaling must be specified by you in **deinterleave factor** and **scaling coefficients**. The resulting data is provided in **data out**. The number of elements operated on are indicated by **index 0 elements scaled** and **index 1 elements scaled**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Typecast, Deinterleave, and Scale.vi' src='../niinstr_data_manipulation_v1_host.lvlib_typecast,_deinterleave,_and_scalec.gif']

**Input Parameters**

**data in** specifies the array **new data** will be deinterleaved and scaled into.

**deinterleave factor** specifies the number of elements that will be deinterleaved from the 1D array **new data** into the 2D array **data in**. Each deinterleaved element from **new data** is placed into a different dimension of **data out**. If **new data** has a size greater than **data in** then the number of elements moved is truncated to the amount of space available.

**scaling coefficients** specifies the array of coefficients to be used to scale **data in**. Each index corresponds to a row in the 2D array **data in**.

**new data** is the array that will be operated on and placed into the 2D array specified by **data in**.

**data in index 0** specifies the row of **data in** to begin replacing.

**data in index 1** specifies the column of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**typecast type** specifies the type to cast **new data** to before completing the rest of the operations.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**index 0 elements scaled** indicates the actual number of row elements updated in **data out**.

**index 1 elements scaled** indicates the actual number of column elements updated in **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

#### Typecast and Deinterleave.vi

Replaces portions of **data in** at the point you specify in **data in index 0** and **data in index 1** using **new data**. The function takes **new data** and typecasts the array to the type of **data out**. The resulting type casted data is deinterleaved before being placed in **data in**. The deinterleaving must be specified by you in **deinterleave factor**. The resulting data is provided in **data out**. The number of elements operated on are indicated by **index 0 elements deinterleaved** and **index 1 elements deinterleaved**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Typecast and Deinterleave.vi' src='../niinstr_data_manipulation_v1_host.lvlib_typecast_and_deinterleavec.gif']

**Input Parameters**

**data in** specifies the array **new data** will be deinterleaved into.

**deinterleave factor** specifies the number of elements that will be deinterleaved from the 1D array **new data** into the 2D array **data in**. Each deinterleaved element from **new data** is placed into a different dimension of **data out**. If **new data** has a size greater than **data in** then the number of elements moved is truncated to the amount of space available.

**new data** is the array that will be operated on and placed into the 2D array specified by **data in**.

**data in index 0** specifies the row of **data in** to begin replacing.

**data in index 1** specifies the column of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**index 0 elements deinterleaved** indicates the actual number of row elements updated in **data out**.

**index 1 elements deinterleaved** indicates the actual number of column elements updated in **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

#### Deinterleave and Scale.vi

Replaces portions of **data in** at the point you specify in **data in index 0** and **data in index 1** using **new data**. **new data** is deinterleaved and scaled before being placed in **data in**. The deinterleaving and scaling must be specified by you in **deinterleave factor** and **scaling coefficients**. The resulting data is provided in **data out**. The number of elements operated on are indicated by **index 0 elements scaled** and **index 1 elements scaled**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Deinterleave and Scale.vi' src='../niinstr_data_manipulation_v1_host.lvlib_deinterleave_and_scalec.gif']

**Input Parameters**

**data in** specifies the array **new data** will be deinterleaved and scaled into.

**deinterleave factor** specifies the number of elements that will be deinterleaved from the 1D array **new data** into the 2D array **data in**. Each deinterleaved element from **new data** is placed into a different dimension of **data out**. If **new data** has a size greater than **data in** then the number of elements moved is truncated to the amount of space available.

**scaling coefficients** specifies the array of coefficients to be used to scale **data in**. Each index corresponds to a row in the 2D array **data in**.

**new data** is the array that will be operated on and placed into the 2D array specified by **data in**.

**data in index 0** specifies the row of **data in** to begin replacing.

**data in index 1** specifies the column of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**index 0 elements scaled** indicates the actual number of row elements updated in **data out**.

**index 1 elements scaled** indicates the actual number of column elements updated in **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

#### Typecast and Copy.vi

Replaces portions of **data in** at the point you specify in **data in index** using **new data**. The function takes **new data** and typecasts the array to the type of **data out** before being placed in **data in**. The resulting data is provided in **data out**. The number of elements operated on is indicated by **elements copied**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Typecast and Copy.vi' src='../niinstr_data_manipulation_v1_host.lvlib_typecast_and_copyc.gif']

**Input Parameters**

**data in** specifies the array **new data** will be copied into.

**new data** is the array that will be operated on and placed into the array specified by **data in**.

**data in index** specifies the index of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**elements copied** indicates the actual number of elements copied into **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

#### Deinterleave.vi

Replaces portions of **data in** at the point you specify in **data in index 0** and **data in index 1** using **new data**. The function deinterleaves **new data** before placing the result in **data in**. The deinterleaving must be specified by you in **deinterleave factor**. The resulting data is provided in **data out**. The number of elements operated on are indicated by **index 0 elements deinterleaved** and **index 1 elements deinterleaved**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Deinterleave.vi' src='../niinstr_data_manipulation_v1_host.lvlib_deinterleavec.gif']

**Input Parameters**

**data in** specifies the array **new data** will be deinterleaved into.

**deinterleave factor** specifies the number of elements that will be deinterleaved from the 1D array **new data** into the 2D array **data in**. Each deinterleaved element from **new data** is placed into a different dimension of **data out**. If **new data** has a size greater than **data in** then the number of elements moved is truncated to the amount of space available.

**new data** is the array that will be operated on and placed into the 2D array specified by **data in**.

**data in index 0** specifies the row of **data in** to begin replacing.

**data in index 1** specifies the column of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**index 0 elements deinterleaved** indicates the actual number of row elements updated in **data out**.

**index 1 elements deinterleaved** indicates the actual number of column elements updated in **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

#### Scale.vi

Replaces portions of **data in** at the point you specify in **data in** index using **new data**. **new data** is scaled before being placed in **data in**. The scaling must be specified by you in **scaling coefficients**. The resulting data is provided in **data out**. The number of elements operated on is indicated by **elements scaled**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Scale.vi' src='../niinstr_data_manipulation_v1_host.lvlib_scalec.gif']

**Input Parameters**

**data in** specifies the array **new data** will be scaled into.

**scaling coefficients** specifies the coefficients to be used to scale **data in**.

**new data** is the array that will be operated on and placed into the array specified by **data in**.

**data in index** specifies the index of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**elements scaled** indicates the actual number of elements scaled into **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

#### Typecast and Scale.vi

Replaces portions of **data in** at the point you specify in **data in index** using **new data**. The function takes **new data** and typecasts the array using the type specified in **typecast type**. The resulting type casted data is scaled before being placed in **data in**. The scaling must be specified by you in **scaling coefficients**. The resulting data is provided in **data out**. The number of elements operated on are indicated by **elements scaled**. This VI is optimized to minimize buffer allocations and maximize throughput.

[IMAGE alt='niInstr Data Manipulation v1 Host.lvlib:Typecast and Scale.vi' src='../niinstr_data_manipulation_v1_host.lvlib_typecast_and_scalec.gif']

**Input Parameters**

**data in** specifies the array **new data** will be scaled into.

**scaling coefficient** specifies the coefficients to be used to scale 'data in</B

**new data** is the array that will be operated on and placed into the array specified by **data in**.

**data in index** specifies the index of **data in** to begin replacing.

**new data index** specifies the index of **new data** to begin copying from.

**typecast type** specifies the type to cast **new data** to before completing the rest of the operations.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**data out** is the array this function returns with the updated elements.

**index elements scaled** indicates the actual number of elements updated in **data out**.

**error out** contains error information. This output provides standard **error out** functionality.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_datatrigger_fpga.html language=enus -->
## TOPIC 00050: Data Trigger FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_datatrigger_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_datatrigger_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Data Trigger FPGA VIs

#### Edge.vi

Generates a trigger when the input data sample meets the hysteresis conditions on either a rising or falling edge of the input. You can use the **configuration** input to set the triggering and hysteresis conditions for this VI.

[IMAGE alt='niInstr Data Trigger v1 FPGA.lvlib:Edge.vi' src='../idl_datatrigger_fpgac.gif']

**Input Parameters**

**data in** is the data sample input. This VI compares this input to the thresholds specified in the **configuration** input. This parameter is either a single value or an array of values, depending on how many samples per data clock cycle your host VI sends to the FPGA.

**reset** resets the VI to its default state. Setting this value to TRUE clears the internal handshaking buffers, writes a FALSE value to the **ready for output** and **input valid** buffers, and returns FALSE for the **trigger** and **output valid** output parameters. This parameter does not affect the value of the **data in** input parameter. Since the outputs of this VI are buffered, it takes one FPGA clock cycle for changes to this parameter to affect the **trigger** and **output valid** output parameters.

**configuration** contains trigger configuration settings.

**configuration.highLevel** specifies the value that **data in** must exceed in order to trigger on a positive slope after crossing the hysteresis threshold. Refer to the **trigger slope** element of this cluster for more information.

**configuration.lowLevel** specifies the value that **data in** must be less than in order to trigger on a negative slope after crossing the hysteresis threshold. Refer to the **trigger slope** element of this cluster for more information.

**configuration.trigger slope** specifies how the hysteresis threshold is calculated, and whether this VI should trigger when the input data is rising or falling.

**Positive** - configures this VI to trigger when two conditions are met. First, a sample from **data in** must fall below the difference between the **highLevel** and **lowLevel** values specified in this cluster. Then, a different sample from **data in** must rise above the **highLevel** value. This second sample is the data sample that causes this VI to trigger.

**Negative** - configures this VI to trigger when two conditions are met. First, a sample from **data in** must exceed the sum of the **highLevel** and **lowLevel** values specified in this cluster. Then, a different sample from **data in** must fall below the **lowLevel** value. This second sample is the data sample that causes this VI to trigger.

**arm (T)** specifies whether or not this VI should be able to trigger, regardless of the value of the **data in** input. Setting this value to TRUE allows this VI to trigger. Setting this value to FALSE prevents this VI from triggering.

**input valid** specifies whether the **data in** input contains valid data. If this value is TRUE, the data is valid and this VI can trigger. If this value is FALSE, the data is invalid and this VI will not trigger.

**ready for output (T)** indicates to the next VI whether or not the output of this VI is valid.

**Output Parameters**

**data out** returns the value from the **data in** input. This value is pipelined and time-aligned with the **trigger** output.

**trigger** is the trigger signal. This output is TRUE if the sample from **data in** meets the trigger conditions. The default value is FALSE.

**trigger index out** returns the index of the sample in the **data in** input parameter that caused this VI to trigger. If multiple elements of **data in** caused this VI to trigger, this parameter returns the index of the first sample to meet the trigger conditions. If your **data in** input is a single value rather than an array, this parameter will always return 0.

**output valid** returns the value from the **input valid** input. This parameter indicates whether or not the **data in** input contains valid data. This parameter does not indicate whether or not the **trigger** output is valid.

**datapath delay** indicates the number of FPGA clock cycles necessary for this VI to process input data and return associated output data. This parameter has a constant value of 2.

**ready for input** indicates whether or not this VI is ready to receive input data. This output is TRUE when this VI is prepared to receive input data, and FALSE when this VI is not prepared to receive input data.

#### Level.vi

Generates a trigger when the input data sample is more than or less than a specified value. You can use the **configuration** input to set the triggering conditions for this VI.

[IMAGE alt='niInstr Data Trigger v1 FPGA.lvlib:Level.vi' src='../niinstr_data_trigger_v1_fpga.lvlib_levelc.gif']

**Input Parameters**

**data in** is the data sample input. This VI compares this input to the **level** specified in the **configuration** input. This parameter is either a single value or an array of values, depending on how many samples per data clock cycle you acquire from the FPGA.

**reset** resets the VI to its default state. Setting this value to TRUE clears the internal handshaking buffers, writes a FALSE value to the **ready for output** and **input valid** buffers, and returns FALSE for the **trigger** and **output valid** output parameters. This parameter does not affect the value of the **data in** input parameter. Since the outputs of this VI are buffered, it takes one FPGA clock cycle for changes to this parameter to affect the **trigger** and **output valid** output parameters.

**configuration** contains trigger configuration settings.

**configuration.level** is the value that the **data in** value is compared to. This parameter has the same data type as the **data in** input.

**configuration.trigger when** specifies whether the VI triggers when **data in** is more than or less than **level**.

**Trigger Above** - The VI will trigger if **data in** is more than **level**.

**Trigger Below** - The VI will trigger if **data in** is less than **level**.

**arm (T)** specifies whether or not this VI should be able to trigger, regardless of the value of the **data in** input. Setting this value to TRUE allows this VI to trigger. Setting this value to FALSE prevents this VI from triggering.

**input valid** specifies whether the **data in** input contains valid data. If this value is TRUE, the data is valid and this VI can trigger. If this value is FALSE, the data is invalid and this VI will not trigger.

**ready for output (T)** indicates to the next VI whether or not the output of this VI is valid.

**Output Parameters**

**data out** returns the value from the **data in** input. This value is pipelined and time-aligned with the **trigger** output.

**trigger** is the trigger signal. This output is TRUE if the sample from **data in** meets the trigger conditions. The default value is FALSE.

**trigger index out** returns the index of the sample in the **data in** input parameter that caused this VI to trigger. If multiple elements of **data in** caused this VI to trigger, this parameter returns the index of the first sample to meet the trigger conditions. If your **data in** input is a single value rather than an array, this parameter will always return 0.

**output valid** returns the value from the **input valid** input. This parameter indicates whether or not the **data in** input contains valid data. This parameter does not indicate whether or not the **trigger** output is valid.

**datapath delay** indicates the number of FPGA clock cycles necessary for this VI to process input data and return associated output data. This parameter has a constant value of 2.

**ready for input** indicates whether or not this VI is ready to receive input data. This output is TRUE when this VI is prepared to receive input data, and FALSE when this VI is not prepared to receive input data.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_dsp_fpga.html language=enus -->
## TOPIC 00051: Digital Signal Processing FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_dsp_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_dsp_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Digital Signal Processing FPGA VIs

#### Digital Gain - Real - 1 spc.vi

Digitally controls the **data in** signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in * gain

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

3 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 50

Slice LUTs:: 80

Block RAMs (18kb): 0

DSP48E(1)s: 1

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - Real - 1 spc.vi' src='../idl_dsp_fpgac.gif']

#### Digital Gain - Real - 2 spc.vi

Digitally controls the **data in** signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in * gain

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 130

Slice LUTs:: 170

Block RAMs (18kb): 0

DSP48E(1)s: 2

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - Real - 2 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_real_2_spcc.gif']

#### Digital Gain - Real - 4 spc.vi

Digitally controls the **data in** signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in * gain

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 260

Slice LUTs:: 320

Block RAMs (18kb): 0

DSP48E(1)s: 4

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - Real - 4 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_real_4_spcc.gif']

#### Digital Gain - Real - 8 spc.vi

Digitally controls the **data in** signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in * gain

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 510

Slice LUTs:: 670

Block RAMs (18kb): 0

DSP48E(1)s: 8

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - Real - 8 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_real_8_spcc.gif']

#### Digital Gain - Real - 16 spc.vi

Digitally controls the **data in** signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in * gain

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

5 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 1360

Slice LUTs:: 1310

Block RAMs (18kb): 0

DSP48E(1)s: 16

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - Real - 16 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_real_16_spcc.gif']

#### Digital Gain - 1 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * gain I

data out.Q <= data in.Q * gain Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

3 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 100

Slice LUTs:: 150

Block RAMs (18kb): 0

DSP48E(1)s: 2

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - 1 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_1_spcc.gif']

#### Digital Gain - 2 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * gain I

data out.Q <= data in.Q * gain Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 250

Slice LUTs:: 325

Block RAMs (18kb): 0

DSP48E(1)s: 4

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - 2 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_2_spcc.gif']

#### Digital Gain - 4 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * gain I

data out.Q <= data in.Q * gain Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 500

Slice LUTs:: 650

Block RAMs (18kb): 0

DSP48E(1)s: 8

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - 4 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_4_spcc.gif']

#### Digital Gain - 8 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * gain I

data out.Q <= data in.Q * gain Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 950

Slice LUTs:: 1275

Block RAMs (18kb): 0

DSP48E(1)s: 16

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - 8 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_8_spcc.gif']

#### Digital Gain - 16 spc.vi

Digitally controls the I and Q signal levels. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * gain I

data out.Q <= data in.Q * gain Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

5 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 2550

Slice LUTs:: 2550

Block RAMs (18kb): 0

DSP48E(1)s: 32

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital Gain - 16 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_gain_16_spcc.gif']

#### Digital_Offset_Real - 1 spc.vi

Digitally controls the **data in** offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in + offset

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 50

Slice LUTs:: 60

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_Real - 1 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_real_1_spcc.gif']

#### Digital_Offset_Real - 2 spc.vi

Digitally controls the **data in** offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in + offset

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 90

Slice LUTs:: 100

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_Real - 2 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_real_2_spcc.gif']

#### Digital_Offset_Real - 4 spc.vi

Digitally controls the **data in** offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in + offset

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 170

Slice LUTs:: 200

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_Real - 4 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_real_4_spcc.gif']

#### Digital_Offset_Real - 8 spc.vi

Digitally controls the **data in** offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in + offset

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 330

Slice LUTs:: 390

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_Real - 8 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_real_8_spcc.gif']

#### Digital_Offset_Real - 16 spc.vi

Digitally controls the **data in** offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out <= data in + offset

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 650

Slice LUTs:: 770

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_Real - 16 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_real_16_spcc.gif']

#### Digital_Offset_1 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I + offset I

data out.Q <= data in.Q + offset Q

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 100

Slice LUTs:: 125

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_1 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_1_spcc.gif']

#### Digital_Offset_2 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I + offset I

data out.Q <= data in.Q + offset Q

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 175

Slice LUTs:: 250

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_2 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_2_spcc.gif']

#### Digital_Offset_4 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I + offset I

data out.Q <= data in.Q + offset Q

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 325

Slice LUTs:: 450

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_4 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_4_spcc.gif']

#### Digital_Offset_8 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I + offset I

data out.Q <= data in.Q + offset Q

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 625

Slice LUTs:: 900

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_8 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_8_spcc.gif']

#### Digital_Offset_16 spc.vi

Digitally controls the I and Q offset. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I + offset I

data out.Q <= data in.Q + offset Q

**Data Type**

This VI automatically adapts to real or complex **data in** types. It also automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

1 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 1250

Slice LUTs:: 1800

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Digital_Offset_16 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_digital_offset_16_spcc.gif']

#### Equalization - 11 cps - 1x oc - 32 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a matrix operation, and can also be used as a general purpose complex filter. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * I Inline - data in.Q * Q Cross

data out.Q <= data in.Q * Q Inline + data in.I * I Cross

Where "*" represents convolution, and I Inline, Q Cross, Q Inline, and I Cross are the sets of coefficients for the four filters.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Throughput**

This VI can consume one I/Q sample at most once every eleven single-cycle Timed Loop clock cycles. **ready for input** will deassert for ten clock cycles after every assertion of **input valid**.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 50 clock cycles to complete. The coefficients are not modified during a reset.

**Programming**

Each of the four FIR filters has 32 coefficients. The default value for all of the coefficients is 0. There are no requirements to the symmetry of the coefficients. Load the filter coefficients using the **filter coefficients** input.

For 1 sample per cycle, load the coefficients in natural order (0, 1, 2, 3 ...)

Complete the following steps to load the coefficients:

1. Select the filter to load using **filter select**.

2. Set **coef load** to TRUE and then FALSE, to begin the load sequence.

3. For each coefficient: write a coefficient to **coef data** and set **coef write** TRUE, then set **coef write** FALSE.

The new coefficients are applied automatically while they are being written. For the most consistent output behavior, hold the **reset** input TRUE while loading the coefficients.

You can use the Digital Filter Design Toolkit to calculate coefficients for your desired filtering application.

**Pipeline Delay**

40 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 1000

Slice LUTs:: 1200

Block RAMs (18kb): 0

DSP48E(1)s: 12

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib_Equalization - 11 cps - 1x oc - 32 coef.vi' src='../niinstr_dsp_v1_fpga_lvlib_equalization_11_cps_1x_oc_32_coefc.gif']

#### Equalization - 1 spc - 3x oc - 33 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a matrix operation, and can also be used as a general purpose complex filter. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * I Inline - data in.Q * Q Cross

data out.Q <= data in.Q * Q Inline + data in.I * I Cross

Where "*" represents convolution, and I Inline, Q Cross, Q Inline, and I Cross are the sets of coefficients for the four filters.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 50 clock cycles to complete. The coefficients are not modified during a reset.

**Programming**

Each of the four FIR filters has 33 coefficients. The default value for all of the coefficients is 0. There are no requirements to the symmetry of the coefficients. Load the filter coefficients using the **filter coefficients** input.

For 1 sample per cycle, load the coefficients in natural order (0, 1, 2, 3 ...)

Complete the following steps to load the coefficients:

1. Select the filter to load using **filter select**.

2. Set **coef load** to TRUE and then FALSE, to begin the load sequence.

3. For each coefficient: write a coefficient to **coef data** and set **coef write** TRUE, then set **coef write** FALSE.

The new coefficients are applied automatically while they are being written. For the most consistent output behavior, hold the **reset** input TRUE while loading the coefficients.

You can use the Digital Filter Design Toolkit to calculate coefficients for your desired filtering application.

**Pipeline Delay**

11 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 2850

Slice LUTs:: 1300

Block RAMs (18kb): 0

DSP48E(1)s: 52

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

130 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Equalization - 1 spc - 3x oc - 33 coef.vi' src='../niinstr_dsp_v1_fpga_lvlib_equalization_1_spc_3x_oc_33_coefc.gif']

#### Equalization - 2 spc - 3x oc - 48 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a matrix operation, and can also be used as a general purpose complex filter. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * I Inline - data in.Q * Q Cross

data out.Q <= data in.Q * Q Inline + data in.I * I Cross

Where "*" represents convolution, and I Inline, Q Cross, Q Inline, and I Cross are the sets of coefficients for the four filters.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 50 clock cycles to complete. The coefficients are not modified during a reset.

**Programming**

Each of the four FIR filters has 48 coefficients. The default value for all of the coefficients is 0. There are no requirements to the symmetry of the coefficients. Load the filter coefficients using the **filter coefficients** input.

For multiple samples per cycle, load the coefficients with an SPC step size, and wrap back to the beginning when you reach the end.

For example, four samples per cycle and 32 coefficients uses the following order:

0, 4, 8, 12, 16, 20, 24, 28, 1, 5, 9, 13, 17, 21, 25, 29, 2, 6, 10, 14, 18, 22, 26, 30, 3, 7, 11, 15, 19, 23, 27, 31

Complete the following steps to load the coefficients:

1. Select the filter to load using **filter select**.

2. Set **coef load** to TRUE and then FALSE, to begin the load sequence.

3. For each coefficient: write a coefficient to **coef data** and set **coef write** TRUE, then set **coef write** FALSE.

The new coefficients are applied automatically while they are being written. For the most consistent output behavior, hold the **reset** input TRUE while loading the coefficients.

You can use the Digital Filter Design Toolkit to calculate coefficients for your desired filtering application.

**Pipeline Delay**

13 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 8100

Slice LUTs:: 3650

Block RAMs (18kb): 0

DSP48E(1)s: 144

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

130 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Equalization - 2 spc - 3x oc - 48 coef.vi' src='../niinstr_dsp_v1_fpga_lvlib_equalization_2_spc_3x_oc_48_coefc.gif']

#### Equalization - 4 spc - 2x oc - 32 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a matrix operation, and can also be used as a general purpose complex filter. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * I Inline - data in.Q * Q Cross

data out.Q <= data in.Q * Q Inline + data in.I * I Cross

Where "*" represents convolution, and I Inline, Q Cross, Q Inline, and I Cross are the sets of coefficients for the four filters.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 50 clock cycles to complete. The coefficients are not modified during a reset.

**Programming**

Each of the four FIR filters has 32 coefficients. The default value for all of the coefficients is 0. There are no requirements to the symmetry of the coefficients. Load the filter coefficients using the **filter coefficients** input.

For multiple samples per cycle, load the coefficients with an SPC step size, and wrap back to the beginning when you reach the end.

For example, four samples per cycle and 32 coefficients uses the following order:

0, 4, 8, 12, 16, 20, 24, 28, 1, 5, 9, 13, 17, 21, 25, 29, 2, 6, 10, 14, 18, 22, 26, 30, 3, 7, 11, 15, 19, 23, 27, 31

Complete the following steps to load the coefficients:

1. Select the filter to load using **filter select**.

2. Set **coef load** to TRUE and then FALSE, to begin the load sequence.

3. For each coefficient: write a coefficient to **coef data** and set **coef write** TRUE, then set **coef write** FALSE.

The new coefficients are applied automatically while they are being written. For the most consistent output behavior, hold the **reset** input TRUE while loading the coefficients.

You can use the Digital Filter Design Toolkit to calculate coefficients for your desired filtering application.

**Pipeline Delay**

17 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 16500

Slice LUTs:: 7550

Block RAMs (18kb): 0

DSP48E(1)s: 288

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

130 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Equalization - 4 spc - 2x oc - 32 coef.vi' src='../niinstr_dsp_v1_fpga_lvlib_equalization_4_spc_2x_oc_32_coefc.gif']

#### Equalization - 8 spc - 2x oc - 32 coef.vi

Equalizes the analog response of a device. This VI implements four FIR filters as a matrix operation, and can also be used as a general purpose complex filter. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * I Inline - data in.Q * Q Cross

data out.Q <= data in.Q * Q Inline + data in.I * I Cross

Where "*" represents convolution, and I Inline, Q Cross, Q Inline, and I Cross are the sets of coefficients for the four filters.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 50 clock cycles to complete. The coefficients are not modified during a reset.

**Programming**

Each of the four FIR filters has 32 coefficients. The default value for all of the coefficients is 0. There are no requirements to the symmetry of the coefficients. Load the filter coefficients using the **filter coefficients** input.

For multiple samples per cycle, load the coefficients with an SPC step size, and wrap back to the beginning when you reach the end.

For example, four samples per cycle and 32 coefficients uses the following order:

0, 4, 8, 12, 16, 20, 24, 28, 1, 5, 9, 13, 17, 21, 25, 29, 2, 6, 10, 14, 18, 22, 26, 30, 3, 7, 11, 15, 19, 23, 27, 31

Complete the following steps to load the coefficients:

1. Select the filter to load using **filter select**.

2. Set **coef load** to TRUE and then FALSE, to begin the load sequence.

3. For each coefficient: write a coefficient to **coef data** and set **coef write** TRUE, then set **coef write** FALSE.

The new coefficients are applied automatically while they are being written. For the most consistent output behavior, hold the **reset** input TRUE while loading the coefficients.

You can use the Digital Filter Design Toolkit to calculate coefficients for your desired filtering application.

**Pipeline Delay**

17 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 35500

Slice LUTs:: 16900

Block RAMs (18kb): 0

DSP48E(1)s: 576

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

130 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Equalization - 8 spc - 2x oc - 32 coef.vi' src='../niinstr_dsp_v1_fpga_lvlib_equalization_8_spc_2x_oc_32_coefc.gif']

#### Halfband Decimator - IQ - 4 CPS - 2x OC.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Throughput**

This VI can consume one I/Q sample at most once every four single-cycle Timed Loop clock cycles. **ready for input** will deassert for three clock cycles after every assertion of **input valid**.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 550

Slice LUTs: 350

Block RAMs (18kb): 0

DSP48E(1)s: 2

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 4 CPS - 2x OC.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_4_cps_2x_occ.gif']

#### Halfband Decimator - IQ - 2 CPS - 2x OC.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Throughput**

This VI can consume one I/Q sample at most once every two single-cycle Timed Loop clock cycles. **ready for input** will deassert for one clock cycles after every assertion of **input valid**.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 800

Slice LUTs:: 500

Block RAMs (18kb): 0

DSP48E(1)s: 4

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 2 CPS - 2x OC.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_2_cps_2x_occ.gif']

#### Halfband Decimator - IQ - 1 SPC - 2x OC.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 1200

Slice LUTs:: 800

Block RAMs (18kb): 0

DSP48E(1)s: 8

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 1 SPC - 2x OC.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_1_spc_2x_occ.gif']

#### Halfband Decimator - IQ - 2 spc - 2x oc.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 2000

Slice LUTs:: 1300

Block RAMs (18kb): 0

DSP48E(1)s: 16

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 2 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_2_spc_2x_occ.gif']

#### Halfband Decimator - IQ - 4 spc - 2x oc.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 3800

Slice LUTs:: 2500

Block RAMs (18kb): 0

DSP48E(1)s: 32

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 4 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_4_spc_2x_occ.gif']

#### Halfband Decimator - IQ - 8 spc - 2x oc.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 7400

Slice LUTs:: 4800

Block RAMs (18kb): 0

DSP48E(1)s: 64

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 8 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_8_spc_2x_occ.gif']

#### Halfband Decimator - IQ - 16 spc - 2x oc.vi

Decimates the input signal **data in** by a factor of two using a low-pass halfband FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 100 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 14 single-cycle Timed Loop clock cycles.

**Group delay**

14.5 output samples.

**Performance**

Decimation Factor: 2

Anti-alias low-pass filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias low-pass filter stopband rejection (from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 14500

Slice LUTs:: 9300

Block RAMs (18kb): 0

DSP48E(1)s: 128

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Halfband Decimator - IQ - 16 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_halfband_decimator_iq_16_spc_2x_occ.gif']

#### Integer Decimator - real - NAP - 2 spc.vi

Decimates the input signal **data in** by an integer decimation factor, without filtering for alias protection. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**decimation factor**

This signal specifies the decimation factor and its acceptable range is 0 to 65,535. Decimation is performed by discarding input data based on the value specified in this signal. When **decimation factor** is set to 0 or 1, no decimation is performed. For example, when **decimation factor** is 4, every fourth input data is output.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. An internal reset is initiated any time the **decimation factor** changes.

**output calculated**

This signal provides information on which input data is part of the decimated data. For example, for a **data in** array size of two, when **output calculated** = FT (FALSE, True), input **data in**[0] is part of the decimation data. When **output calculated** = FF, no input data in the current clock is part of the decimated data. This signal has the same number of pipeline stages as the data path.

**Pipeline Delay**

2 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Kintex 7**

Slice flip-flops: 151

Slice LUTs:: 99

Block RAMs (18kb): 0

DSP48E(1)s: 0

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Kintex 7**

180 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib_Integer_Decimator_real_NAP_ 2_spcc.vi' src='../niinstr_dsp_v1_fpga_lvlib_integer_decimator_real_nap_2_spcc.gif']

#### Fractional Decimator - 10 cps - 1x oc.vi

Decimates the input signal **data in** according to the **output sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Throughput**

This VI can consume one I/Q sample at most once every ten single-cycle Timed Loop clock cycles. **ready for input** will deassert for nine clock cycles after every assertion of **input valid**.

**Data Rate**

The **output sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to decimation factors of [65,536.0 down to 1.0]. It produces **data out** outputs at a sample rate equal to the normalized **output sample rate**.

decimation factor = 1 / **output sample rate**

output data rate (in Hz) = input data rate (in Hz) * **output sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** is asserted

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 1100 clock cycles to complete. An internal reset is initiated any time the **output sample rate** changes.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** varies between 49 and 1599, depending on the **output sample rate** value.

**Group delay of the anti-alias filter**

decimation factor <= 16: group delay = 15 output samples

16 < decimation factor <= 128: group delay = (256 / decimation factor) + 15 output samples

128 < decimation factor <= 2,048: group delay = (2,056 / decimation factor) + 15 output samples

2,048 < decimation factor <= 32,768: group delay = (34,624 / decimation factor) + 15 output samples

32,768 < decimation factor <= 65,536: group delay (65,344 / decimation factor) + 15 output samples

**Performance**

Decimation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 1.53e-5 / input data rate (in Hz)

Anti-alias filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias filter stopband rejection(from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 2800

Slice LUTs:: 6100

Block RAMs (18kb): 25

DSP48E(1)s: 34

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

xxx MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Decimator - 10 cps - 1x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_decimator_10_cps_1x_occ.gif']

#### Fractional Decimator - 1 spc - 2x oc.vi

Decimates the input signal **data in** according to the **output sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **output sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to decimation factors of [65,536.0 down to 1.0]. It produces **data out** outputs at a sample rate equal to the normalized **output sample rate**.

decimation factor = 1 / **output sample rate**

output data rate (in Hz) = input data rate (in Hz) * **output sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** is asserted

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 1100 clock cycles to complete. An internal reset is initiated any time the **output sample rate** changes.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** varies between 33 and 827, depending on the **output sample rate** value.

**Group delay of the anti-alias filter**

decimation factor <= 16: group delay = 15 output samples

16 < decimation factor <= 128: group delay = (256 / decimation factor) + 15 output samples

128 < decimation factor <= 2,048: group delay = (2,056 / decimation factor) + 15 output samples

2,048 < decimation factor <= 32,768: group delay = (34,624 / decimation factor) + 15 output samples

32,768 < decimation factor <= 65,536: group delay (65,344 / decimation factor) + 15 output samples

**Performance**

Decimation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 1.53e-5 / input data rate (in Hz)

Anti-alias filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias filter stopband rejection(from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 10300

Slice LUTs:: 6100

Block RAMs (18kb): 77

DSP48E(1)s: 72

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Decimator - 1 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_decimator_1_spc_2x_occ.gif']

#### Fractional Decimator - 1 spc - 3x oc.vi

Decimates the input signal **data in** according to the **output sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **output sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to decimation factors of [65,536.0 down to 1.0]. It produces **data out** outputs at a sample rate equal to the normalized **output sample rate**.

decimation factor = 1 / **output sample rate**

output data rate (in Hz) = input data rate (in Hz) * **output sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** is asserted

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 1100 clock cycles to complete. An internal reset is initiated any time the **output sample rate** changes.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** varies between 25 and 559, depending on the **output sample rate** value.

**Group delay of the anti-alias filter**

decimation factor <= 16: group delay = 15 output samples

16 < decimation factor <= 128: group delay = (256 / decimation factor) + 15 output samples

128 < decimation factor <= 2,048: group delay = (2,056 / decimation factor) + 15 output samples

2,048 < decimation factor <= 32,768: group delay = (34,624 / decimation factor) + 15 output samples

32,768 < decimation factor <= 65,536: group delay (65,344 / decimation factor) + 15 output samples

**Performance**

Decimation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 1.53e-5 / input data rate (in Hz)

Anti-alias filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias filter stopband rejection(from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 7700

Slice LUTs:: 4900

Block RAMs (18kb): 50

DSP48E(1)s: 50

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

125 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Decimator - 1 spc - 3x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_decimator_1_spc_3x_occ.gif']

#### Fractional Decimator - 2 spc - 2x oc.vi

Decimates the input signal **data in** according to the **output sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **output sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to decimation factors of [65,536.0 down to 1.0]. It produces **data out** outputs at a sample rate equal to the normalized **output sample rate**.

decimation factor = 1 / **output sample rate**

output data rate (in Hz) = input data rate (in Hz) * **output sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** is asserted

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**Output Calculated**

**Output calculated** indicates when a new output sample has been calculated in the decimator and points to the last input sample used in the convolution to calculate the output sample. In contrast, **output valid** asserts only when all of the samples on **data out** are valid.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 1100 clock cycles to complete. An internal reset is initiated any time the **output sample rate** changes.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** varies between 33 and 33597, depending on the **output sample rate** value.

Complete the following steps to measure the pipeline delay of the Fractional Decimator for a specific **output sample rate**:

1. Select an **output sample rate**.

2. Assert and deassert **reset**.

3. Wait for **ready for input** to return TRUE.

4. Assert **input valid** and count the number of cycles from the first **input valid** to the first **output calculated**. The count is equal to the pipeline delay for the selected **output sample rate**.

**Group delay of the anti-alias filter**

decimation factor <= 16: group delay = 15 output samples

16 < decimation factor <= 128: group delay = (256 / decimation factor) + 15 output samples

128 < decimation factor <= 2,048: group delay = (2,056 / decimation factor) + 15 output samples

2,048 < decimation factor <= 32,768: group delay = (34,624 / decimation factor) + 15 output samples

32,768 < decimation factor <= 65,536: group delay (65,344 / decimation factor) + 15 output samples

**Performance**

Decimation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 1.53e-5 / input data rate (in Hz)

Anti-alias filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias filter stopband rejection(from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 19228

Slice LUTs:: 12400

Block RAMs (18kb): 140

DSP48E(1)s: 140

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Decimator - 2 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_decimator_2_spc_2x_occ.gif']

#### Fractional Decimator - 2 spc - 3x oc.vi

Decimates the input signal **data in** according to the **output sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **output sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to decimation factors of [65,536.0 down to 1.0]. It produces **data out** outputs at a sample rate equal to the normalized **output sample rate**.

decimation factor = 1 / **output sample rate**

output data rate (in Hz) = input data rate (in Hz) * **output sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** is asserted

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**Output Calculated**

**Output calculated** indicates when a new output sample has been calculated in the decimator and points to the last input sample used in the convolution to calculate the output sample. In contrast, **output valid** asserts only when all of the samples on **data out** are valid.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 1100 clock cycles to complete. An internal reset is initiated any time the **output sample rate** changes.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** varies between 25 and 33330, depending on the **output sample rate** value.

Complete the following steps to measure the pipeline delay of the Fractional Decimator for a specific **output sample rate**:

1. Select an **output sample rate**.

2. Assert and deassert **reset**.

3. Wait for **ready for input** to return TRUE.

4. Assert **input valid** and count the number of cycles from the first **input valid** to the first **output calculated**. The count is equal to the pipeline delay for the selected **output sample rate**.

**Group delay of the anti-alias filter**

decimation factor <= 16: group delay = 15 output samples

16 < decimation factor <= 128: group delay = (256 / decimation factor) + 15 output samples

128 < decimation factor <= 2,048: group delay = (2,056 / decimation factor) + 15 output samples

2,048 < decimation factor <= 32,768: group delay = (34,624 / decimation factor) + 15 output samples

32,768 < decimation factor <= 65,536: group delay (65,344 / decimation factor) + 15 output samples

**Performance**

Decimation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 1.53e-5 / input data rate (in Hz)

Anti-alias filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias filter stopband rejection(from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 13935

Slice LUTs:: 9100

Block RAMs (18kb): 92

DSP48E(1)s: 96

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

125 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Decimator - 2 spc - 3x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_decimator_2_spc_3x_occ.gif']

#### Fractional Decimator - 4 spc - 2x oc.vi

Decimates the input signal **data in** according to the **output sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **output sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to decimation factors of [65,536.0 down to 1.0]. It produces **data out** outputs at a sample rate equal to the normalized **output sample rate**.

decimation factor = 1 / **output sample rate**

output data rate (in Hz) = input data rate (in Hz) * **output sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** is asserted

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**Output Calculated**

**Output calculated** indicates when a new output sample has been calculated in the decimator and points to the last input sample used in the convolution to calculate the output sample. In contrast, **output valid** asserts only when all of the samples on **data out** are valid.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 1100 clock cycles to complete. An internal reset is initiated any time the **output sample rate** changes.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** varies between 33 and 49981, depending on the **output sample rate** value.

Complete the following steps to measure the pipeline delay of the Fractional Decimator for a specific **output sample rate**:

1. Select an **output sample rate**.

2. Assert and deassert **reset**.

3. Wait for **ready for input** to return TRUE.

4. Assert **input valid** and count the number of cycles from the first **input valid** to the first **output calculated**. The count is equal to the pipeline delay for the selected **output sample rate**.

**Group delay of the anti-alias filter**

decimation factor <= 16: group delay = 15 output samples

16 < decimation factor <= 128: group delay = (256 / decimation factor) + 15 output samples

128 < decimation factor <= 2,048: group delay = (2,056 / decimation factor) + 15 output samples

2,048 < decimation factor <= 32,768: group delay = (34,624 / decimation factor) + 15 output samples

32,768 < decimation factor <= 65,536: group delay (65,344 / decimation factor) + 15 output samples

**Performance**

Decimation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 1.53e-5 / input data rate (in Hz)

Anti-alias filter passband ripple (to 0.4 * output data rate): 0 dB to -0.01 dB

Anti-alias filter stopband rejection(from 0.6 * output data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 39400

Slice LUTs:: 25600

Block RAMs (18kb): 352

DSP48E(1)s: 274

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Decimator - 4 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_decimator_4_spc_2x_occ.gif']

#### Fractional Interpolator - 1 spc - 2x oc.vi

Interpolates the input signal **data in** according to **input sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **input sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to interpolation factors of [65,536.0 down to 1.0]. This VI attempts to return a new **data out** output every cycle. It consumes valid **data in** inputs at a sample rate equal to the normalized **input sample rate**.

interpolation factor = 1 / **input sample rate**

output data rate (in Hz) = input data rate (in Hz) / **input sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**input consumed** asserts whenever an input sample is read from the internal FIFO and processed. Use this signal to synchronize other events or data with the output data from this VI.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 120 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 30 single-cycle Timed Loop clock cycles.

**Group delay of the anti-image filter**

15 input samples

**Performance**

Interpolation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 3.81e-6 / input data rate (in Hz)

Anti-image filter passband ripple (to 0.4 * input data rate): 0 dB to -0.01 dB

Anti-image filter stopband rejection(from 0.6 * input data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 4000

Slice LUTs:: 1900

Block RAMs (18kb): 30

DSP48E(1)s: 46

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Interpolator - 1 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_interpolator_1_spc_2x_occ.gif']

#### Fractional Interpolator - 1 spc - 3x oc.vi

Interpolates the input signal **data in** according to **input sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **input sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to interpolation factors of [65,536.0 down to 1.0]. This VI attempts to return a new **data out** output every cycle. It consumes valid **data in** inputs at a sample rate equal to the normalized **input sample rate**.

interpolation factor = 1 / **input sample rate**

output data rate (in Hz) = input data rate (in Hz) / **input sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**input consumed** asserts whenever an input sample is read from the internal FIFO and processed. Use this signal to synchronize other events or data with the output data from this VI.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 120 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 23 single-cycle Timed Loop clock cycles.

**Group delay of the anti-image filter**

15 input samples

**Performance**

Interpolation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 3.81e-6 / input data rate (in Hz)

Anti-image filter passband ripple (to 0.4 * input data rate): 0 dB to -0.01 dB

Anti-image filter stopband rejection(from 0.6 * input data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 2800

Slice LUTs:: 1400

Block RAMs (18kb): 20

DSP48E(1)s: 31

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

125 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Interpolator - 1 spc - 3x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_interpolator_1_spc_3x_occ.gif']

#### Fractional Interpolator - 2 spc - 2x oc.vi

Interpolates the input signal **data in** according to **input sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at two times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **input sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to interpolation factors of [65,536.0 down to 1.0]. This VI attempts to return a new **data out** output every cycle. It consumes valid **data in** inputs at a sample rate equal to the normalized **input sample rate**.

interpolation factor = 1 / **input sample rate**

output data rate (in Hz) = input data rate (in Hz) / **input sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**input consumed** asserts whenever an input sample is read from the internal FIFO and processed. Use this signal to synchronize other events or data with the output data from this VI.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 120 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 31 single-cycle Timed Loop clock cycles.

**Group delay of the anti-image filter**

15 input samples

**Performance**

Interpolation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 3.81e-6 / input data rate (in Hz)

Anti-image filter passband ripple (to 0.4 * input data rate): 0 dB to -0.01 dB

Anti-image filter stopband rejection(from 0.6 * input data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 7800

Slice LUTs:: 3600

Block RAMs (18kb): 60

DSP48E(1)s: 92

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Interpolator - 2 spc - 2x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_interpolator_2_spc_2x_occ.gif']

#### Fractional Interpolator - 2 spc - 3x oc.vi

Interpolates the input signal **data in** according to **input sample rate** and **delay** using an FIR filter implementation. This VI must be used in a single-cycle Timed Loop.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Over-clocking**

This VI must be used in a single-cycle Timed Loop and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

**Data Rate**

The **input sample rate** input may be in the range of [1.52588E-5 to 1.0]. This corresponds to interpolation factors of [65,536.0 down to 1.0]. This VI attempts to return a new **data out** output every cycle. It consumes valid **data in** inputs at a sample rate equal to the normalized **input sample rate**.

interpolation factor = 1 / **input sample rate**

output data rate (in Hz) = input data rate (in Hz) / **input sample rate**

The input data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

input data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the input data rate is 60 MHz.

**Delay**

The **delay** input delays the input data. The valid range for **delay** is [-0.5 to +0.5].

delay (in seconds) = **delay** / input data rate (in Hz)

**input consumed** asserts whenever an input sample is read from the internal FIFO and processed. Use this signal to synchronize other events or data with the output data from this VI.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called. A reset operation takes 120 clock cycles to complete.

**Pipeline Delay**

The pipeline delay from the first **input valid** to the first **output valid** is 24 single-cycle Timed Loop clock cycles.

**Group delay of the anti-image filter**

15 input samples

**Performance**

Interpolation Range: [1.0 to 65,536.0]

Output Sample Rate Resolution: 7.11e-15 * input data rate (in Hz)

Delay Range: [-0.5 to +0.5] (corresponds to -0.5 to +0.5 input data rate periods)

Delay Resolution: 3.81e-6 / input data rate (in Hz)

Anti-image filter passband ripple (to 0.4 * input data rate): 0 dB to -0.01 dB

Anti-image filter stopband rejection(from 0.6 * input data rate): > 85 dB

**Approximate resource usage in a Xilinx Virtex-6**

Slice flip-flops: 5250

Slice LUTs:: 2500

Block RAMs (18kb): 40

DSP48E(1)s: 62

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-6 (-1)**

125 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Fractional Interpolator - 2 spc - 3x oc.vi' src='../niinstr_dsp_v1_fpga_lvlib_fractional_interpolator_2_spc_3x_occ.gif']

#### Frequency Shift - 1 spc.vi

Applies a digital frequency shift to the I/Q data. A numerically-controlled oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q data using a complex multiplier. The net effect is to shift the complex spectrum to the left or right in the frequency domain. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * cosine - data in.Q * sine

data out.Q <= data in.I * sine + data in.Q * cosine

Where "*" represents scalar multiplication.

The **frequency shift** input may be in the range of [-0.5 to +0.5), where negative values shift the complex spectrum to the left and positive values shift the complex spectrum to the right. The amount of frequency shift (in Hz) is determined by multiplying the data rate (in Hz) by the **frequency shift** input.

Frequency Shift (in Hz) = **frequency shift** * data rate (in Hz)

The data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the data rate is 60 MHz.

The **phase** input may be in the range of [-0.5 to +0.5), which corresponds to phase shifting the sine and cosine signals -180 degrees to +180 degrees.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

12 single-cycle Timed Loop clock cycles

**Performance**

Frequency Range: [-0.5 to +0.5) * data rate

Frequency Resolution: 3.56e-15 * data rate

Phase Range: [-0.5 to +0.5) (corresponds to -180 to +180 degrees)

Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees)

Spurious Free Dynamic Range: > 105 dBFS

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 375

Slice LUTs:: 600

Block RAMs (18kb): 1

DSP48E(1)s: 6

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Frequency Shift - 1 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_frequency_shift_1_spcc.gif']

#### Frequency Shift - 2 spc.vi

Applies a digital frequency shift to the I/Q data. A numerically-controlled oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q data using a complex multiplier. The net effect is to shift the complex spectrum to the left or right in the frequency domain. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * cosine - data in.Q * sine

data out.Q <= data in.I * sine + data in.Q * cosine

Where "*" represents scalar multiplication.

The **frequency shift** input may be in the range of [-0.5 to +0.5), where negative values shift the complex spectrum to the left and positive values shift the complex spectrum to the right. The amount of frequency shift (in Hz) is determined by multiplying the data rate (in Hz) by the **frequency shift** input.

Frequency Shift (in Hz) = **frequency shift** * data rate (in Hz)

The data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the data rate is 60 MHz.

The **phase** input may be in the range of [-0.5 to +0.5), which corresponds to phase shifting the sine and cosine signals -180 degrees to +180 degrees.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

13 single-cycle Timed Loop clock cycles

**Performance**

Frequency Range: [-0.5 to +0.5) * data rate

Frequency Resolution: 3.56e-15 * data rate

Phase Range: [-0.5 to +0.5) (corresponds to -180 to +180 degrees)

Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees)

Spurious Free Dynamic Range: > 105 dBFS

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 875

Slice LUTs:: 1110

Block RAMs (18kb): 2

DSP48E(1)s: 12

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Frequency Shift - 2 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_frequency_shift_2_spcc.gif']

#### Frequency Shift - 4 spc.vi

Applies a digital frequency shift to the I/Q data. A numerically-controlled oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q data using a complex multiplier. The net effect is to shift the complex spectrum to the left or right in the frequency domain. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * cosine - data in.Q * sine

data out.Q <= data in.I * sine + data in.Q * cosine

Where "*" represents scalar multiplication.

The **frequency shift** input may be in the range of [-0.5 to +0.5), where negative values shift the complex spectrum to the left and positive values shift the complex spectrum to the right. The amount of frequency shift (in Hz) is determined by multiplying the data rate (in Hz) by the **frequency shift** input.

Frequency Shift (in Hz) = **frequency shift** * data rate (in Hz)

The data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the data rate is 60 MHz.

The **phase** input may be in the range of [-0.5 to +0.5), which corresponds to phase shifting the sine and cosine signals -180 degrees to +180 degrees.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

13 single-cycle Timed Loop clock cycles

**Performance**

Frequency Range: [-0.5 to +0.5) * data rate

Frequency Resolution: 3.56e-15 * data rate

Phase Range: [-0.5 to +0.5) (corresponds to -180 to +180 degrees)

Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees)

Spurious Free Dynamic Range: > 105 dBFS

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 1650

Slice LUTs:: 2325

Block RAMs (18kb): 4

DSP48E(1)s: 24

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Frequency Shift - 4 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_frequency_shift_4_spcc.gif']

#### Frequency Shift - 8 spc.vi

Applies a digital frequency shift to the I/Q data. A numerically-controlled oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q data using a complex multiplier. The net effect is to shift the complex spectrum to the left or right in the frequency domain. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * cosine - data in.Q * sine

data out.Q <= data in.I * sine + data in.Q * cosine

Where "*" represents scalar multiplication.

The **frequency shift** input may be in the range of [-0.5 to +0.5), where negative values shift the complex spectrum to the left and positive values shift the complex spectrum to the right. The amount of frequency shift (in Hz) is determined by multiplying the data rate (in Hz) by the **frequency shift** input.

Frequency Shift (in Hz) = **frequency shift** * data rate (in Hz)

The data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the data rate is 60 MHz.

The **phase** input may be in the range of [-0.5 to +0.5), which corresponds to phase shifting the sine and cosine signals -180 degrees to +180 degrees.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

13 single-cycle Timed Loop clock cycles

**Performance**

Frequency Range: [-0.5 to +0.5) * data rate

Frequency Resolution: 3.56e-15 * data rate

Phase Range: [-0.5 to +0.5) (corresponds to -180 to +180 degrees)

Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees)

Spurious Free Dynamic Range: > 105 dBFS

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 3175

Slice LUTs:: 4600

Block RAMs (18kb): 8

DSP48E(1)s: 48

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Frequency Shift - 8 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_frequency_shift_8_spcc.gif']

#### Frequency Shift - 16 spc.vi

Applies a digital frequency shift to the I/Q data. A numerically-controlled oscillator (NCO) creates a cosine/sine pair, which is then multiplied by the I/Q data using a complex multiplier. The net effect is to shift the complex spectrum to the left or right in the frequency domain. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= data in.I * cosine - data in.Q * sine

data out.Q <= data in.I * sine + data in.Q * cosine

Where "*" represents scalar multiplication.

The **frequency shift** input may be in the range of [-0.5 to +0.5), where negative values shift the complex spectrum to the left and positive values shift the complex spectrum to the right. The amount of frequency shift (in Hz) is determined by multiplying the data rate (in Hz) by the **frequency shift** input.

Frequency Shift (in Hz) = **frequency shift** * data rate (in Hz)

The data rate is defined by the clock frequency of the single-cycle Timed Loop (SCTL), the number of samples per cycle (SPC) in **data in**, and the fraction of cycles on which **input valid** is asserted.

data rate = SCTL clock frequency * SPC * fraction of cycles on which **input valid** assertion

For example if the SCTL is clocked at 120 MHz, one SPC is used, and the **input valid** signal is asserted on every other cycle, then the data rate is 60 MHz.

The **phase** input may be in the range of [-0.5 to +0.5), which corresponds to phase shifting the sine and cosine signals -180 degrees to +180 degrees.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

13 single-cycle Timed Loop clock cycles

**Performance**

Frequency Range: [-0.5 to +0.5) * data rate

Frequency Resolution: 3.56e-15 * data rate

Phase Range: [-0.5 to +0.5) (corresponds to -180 to +180 degrees)

Phase Resolution: 4.77e-7 (corresponds to 0.00017 degrees)

Spurious Free Dynamic Range: > 105 dBFS

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 6225

Slice LUTs:: 9150

Block RAMs (18kb): 16

DSP48E(1)s: 96

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Frequency Shift - 16 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_frequency_shift_16_spcc.gif']

#### IQ Impairments - 1 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= (pre-gain offset I + data in.I) * inline gain I +

(pre-gain offset Q + data in.Q) * cross gain Q + post-gain offset I

data out.Q <= (pre-gain offset Q + data in.Q) * inline gain Q +

(pre-gain offset I + data in.I) * cross gain I + post-gain offset Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 100

Slice LUTs:: 225

Block RAMs (18kb): 0

DSP48E(1)s: 4

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Impairments - 1 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_impairments_1_spcc.gif']

#### IQ Impairments - 2 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= (pre-gain offset I + data in.I) * inline gain I +

(pre-gain offset Q + data in.Q) * cross gain Q + post-gain offset I

data out.Q <= (pre-gain offset Q + data in.Q) * inline gain Q +

(pre-gain offset I + data in.I) * cross gain I + post-gain offset Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 175

Slice LUTs:: 425

Block RAMs (18kb): 0

DSP48E(1)s: 8

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Impairments - 2 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_impairments_2_spcc.gif']

#### IQ Impairments - 4 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= (pre-gain offset I + data in.I) * inline gain I +

(pre-gain offset Q + data in.Q) * cross gain Q + post-gain offset I

data out.Q <= (pre-gain offset Q + data in.Q) * inline gain Q +

(pre-gain offset I + data in.I) * cross gain I + post-gain offset Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 325

Slice LUTs:: 875

Block RAMs (18kb): 0

DSP48E(1)s: 16

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Impairments - 4 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_impairments_4_spcc.gif']

#### IQ Impairments - 8 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= (pre-gain offset I + data in.I) * inline gain I +

(pre-gain offset Q + data in.Q) * cross gain Q + post-gain offset I

data out.Q <= (pre-gain offset Q + data in.Q) * inline gain Q +

(pre-gain offset I + data in.I) * cross gain I + post-gain offset Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 650

Slice LUTs:: 1725

Block RAMs (18kb): 0

DSP48E(1)s: 32

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Impairments - 8 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_impairments_8_spcc.gif']

#### IQ Impairments - 16 spc.vi

Modifies the I/Q data to apply signal impairments. This VI must be used in a single-cycle Timed Loop.

This VI provides the following functionality:

data out.I <= (pre-gain offset I + data in.I) * inline gain I +

(pre-gain offset Q + data in.Q) * cross gain Q + post-gain offset I

data out.Q <= (pre-gain offset Q + data in.Q) * inline gain Q +

(pre-gain offset I + data in.I) * cross gain I + post-gain offset Q

Where "*" represents scalar multiplication.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Overflows**

Overflows on **data in.overflow** are pipelined along with the data path, combined with overflows that occur inside of this VI, and output on **data out.overflow**.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

5 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 2175

Slice LUTs:: 3550

Block RAMs (18kb): 0

DSP48E(1)s: 64

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Impairments - 16 spc.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_impairments_16_spcc.gif']

#### IQ Power Level Trigger - 1 spc - 18 bit Legacy.vi

Creates triggers based on the trigger configuration and the power of the input data.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Configuration**

Use the **configuration** input to configure the trigger.

**trig rising edge** specifies if the output **trigger** is sensitive to the increase or decrease of the input data power with respect to the **trig level**. A value of TRUE creates triggers when the **input data** power level rises above the **trig level** threshold, and a value of FALSE creates triggers when the **input data** power level falls below the **trig level** threshold.

**min quiet time** specifies the minimum quiet time of the **input data** power with respect to the **trig level** threshold, in units of valid samples. If the power of **input data** crosses the **trig level** threshold before the **min quiet time** has expired, the trigger is ignored and the **min quiet time** state is reset. The minimum **min quiet time** is one valid sample, and a minimum quiet time of zero is coerced to a value of one internally.

**trig level** specifies the threshold for the **input data** power. The power of the **input data** is calculated using the following formula:

signal power = (input data.I)^2 + (input data.Q)^2

**Ready for Trigger**

Specifies whether the downstream node that is accepting the **trigger** output is ready to receive a trigger. While the **ready for trigger** input is FALSE, a **trigger** will not be produced. The quiet time counter and edge detection circuitry are reset if the **ready for trigger** input is FALSE. The default value is TRUE.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

5 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 212

Slice LUTs:: 244

Block RAMs (18kb): 0

DSP48E(1)s: 2

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Power Level Trigger - 1 spc - 18 bit Legacy.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_power_level_trigger_1_spc_18_bit_legacyc.gif']

#### IQ Power Level Trigger - 1 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input data.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Configuration**

Use the **configuration** input to configure the trigger.

**trig rising edge** specifies if the output **trigger** is sensitive to the increase or decrease of the input data power with respect to the **trig level**. A value of TRUE creates triggers when the **input data** power level rises above the **trig level** threshold, and a value of FALSE creates triggers when the **input data** power level falls below the **trig level** threshold.

**min quiet time** specifies the minimum quiet time of the **input data** power with respect to the **trig level** threshold, in units of valid samples. If the power of **input data** crosses the **trig level** threshold before the **min quiet time** has expired, the trigger is ignored and the **min quiet time** state is reset. The minimum **min quiet time** is one valid sample, and a minimum quiet time of zero is coerced to a value of one internally.

**trig level** specifies the threshold for the **input data** power. The power of the **input data** is calculated using the following formula:

signal power = (input data.I)^2 + (input data.Q)^2

**Ready for Trigger**

Specifies whether the downstream node that is accepting the **trigger** output is ready to receive a trigger. While the **ready for trigger** input is FALSE, a **trigger** will not be produced. The quiet time counter and edge detection circuitry are reset if the **ready for trigger** input is FALSE. The default value is TRUE.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

3 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 37

Slice LUTs:: 142

Block RAMs (18kb): 0

DSP48E(1)s: 2

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Power Level Trigger - 1 spc - 18 bit.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_power_level_trigger_1_spc_18_bitc.gif']

#### IQ Power Level Trigger - 1 spc - 25 bit.vi

Creates triggers based on the trigger configuration and the power of the input data.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Configuration**

Use the **configuration** input to configure the trigger.

**trig rising edge** specifies if the output **trigger** is sensitive to the increase or decrease of the input data power with respect to the **trig level**. A value of TRUE creates triggers when the **input data** power level rises above the **trig level** threshold, and a value of FALSE creates triggers when the **input data** power level falls below the **trig level** threshold.

**min quiet time** specifies the minimum quiet time of the **input data** power with respect to the **trig level** threshold, in units of valid samples. If the power of **input data** crosses the **trig level** threshold before the **min quiet time** has expired, the trigger is ignored and the **min quiet time** state is reset. The minimum **min quiet time** is one valid sample, and a minimum quiet time of zero is coerced to a value of one internally.

**trig level** specifies the threshold for the **input data** power. The power of the **input data** is calculated using the following formula:

signal power = (input data.I)^2 + (input data.Q)^2

**Ready for Trigger**

Specifies whether the downstream node that is accepting the **trigger** output is ready to receive a trigger. While the **ready for trigger** input is FALSE, a **trigger** will not be produced. The quiet time counter and edge detection circuitry are reset if the **ready for trigger** input is FALSE. The default value is TRUE.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

6 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 104

Slice LUTs:: 225

Block RAMs (18kb): 0

DSP48E(1)s: 4

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Power Level Trigger - 1 spc - 25 bit.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_power_level_trigger_1_spc_25_bitc.gif']

#### IQ Power Level Trigger - 2 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input data.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Configuration**

Use the **configuration** input to configure the trigger.

**trig rising edge** specifies if the output **trigger** is sensitive to the increase or decrease of the input data power with respect to the **trig level**. A value of TRUE creates triggers when the **input data** power level rises above the **trig level** threshold, and a value of FALSE creates triggers when the **input data** power level falls below the **trig level** threshold.

**min quiet time** specifies the minimum quiet time of the **input data** power with respect to the **trig level** threshold, in units of valid samples. If the power of **input data** crosses the **trig level** threshold before the **min quiet time** has expired, the trigger is ignored and the **min quiet time** state is reset. The minimum **min quiet time** is one valid sample, and a minimum quiet time of zero is coerced to a value of one internally.

**trig level** specifies the threshold for the **input data** power. The power of the **input data** is calculated using the following formula:

signal power = (input data.I)^2 + (input data.Q)^2

**Ready for Trigger**

Specifies whether the downstream node that is accepting the **trigger** output is ready to receive a trigger. While the **ready for trigger** input is FALSE, a **trigger** will not be produced. The quiet time counter and edge detection circuitry are reset if the **ready for trigger** input is FALSE. The default value is TRUE.

**Data Index**

Specifies the array index of **data in** where the **trigger** occurred. The index of the first sample that meets the trigger criteria is returned.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 48

Slice LUTs:: 212

Block RAMs (18kb): 0

DSP48E(1)s: 4

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Power Level Trigger - 2 spc - 18 bit.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_power_level_trigger_2_spc_18_bitc.gif']

#### IQ Power Level Trigger - 4 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input data.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Configuration**

Use the **configuration** input to configure the trigger.

**trig rising edge** specifies if the output **trigger** is sensitive to the increase or decrease of the input data power with respect to the **trig level**. A value of TRUE creates triggers when the **input data** power level rises above the **trig level** threshold, and a value of FALSE creates triggers when the **input data** power level falls below the **trig level** threshold.

**min quiet time** specifies the minimum quiet time of the **input data** power with respect to the **trig level** threshold, in units of valid samples. If the power of **input data** crosses the **trig level** threshold before the **min quiet time** has expired, the trigger is ignored and the **min quiet time** state is reset. The minimum **min quiet time** is one valid sample, and a minimum quiet time of zero is coerced to a value of one internally.

**trig level** specifies the threshold for the **input data** power. The power of the **input data** is calculated using the following formula:

signal power = (input data.I)^2 + (input data.Q)^2

**Ready for Trigger**

Specifies whether the downstream node that is accepting the **trigger** output is ready to receive a trigger. While the **ready for trigger** input is FALSE, a **trigger** will not be produced. The quiet time counter and edge detection circuitry are reset if the **ready for trigger** input is FALSE. The default value is TRUE.

**Data Index**

Specifies the array index of **data in** where the **trigger** occurred. The index of the first sample that meets the trigger criteria is returned.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 50

Slice LUTs:: 438

Block RAMs (18kb): 0

DSP48E(1)s: 8

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Power Level Trigger - 4 spc - 18 bit.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_power_level_trigger_4_spc_18_bitc.gif']

#### IQ Power Level Trigger - 8 spc - 18 bit.vi

Creates triggers based on the trigger configuration and the power of the input data.

**Data Type**

This VI automatically adapts to the **data in** array size. Arrays represent parallel samples from one data stream. For array sizes greater than one, the first element ('data in'[0]) is the oldest sample in the array.

**Configuration**

Use the **configuration** input to configure the trigger.

**trig rising edge** specifies if the output **trigger** is sensitive to the increase or decrease of the input data power with respect to the **trig level**. A value of TRUE creates triggers when the **input data** power level rises above the **trig level** threshold, and a value of FALSE creates triggers when the **input data** power level falls below the **trig level** threshold.

**min quiet time** specifies the minimum quiet time of the **input data** power with respect to the **trig level** threshold, in units of valid samples. If the power of **input data** crosses the **trig level** threshold before the **min quiet time** has expired, the trigger is ignored and the **min quiet time** state is reset. The minimum **min quiet time** is one valid sample, and a minimum quiet time of zero is coerced to a value of one internally.

**trig level** specifies the threshold for the **input data** power. The power of the **input data** is calculated using the following formula:

signal power = (input data.I)^2 + (input data.Q)^2

**Ready for Trigger**

Specifies whether the downstream node that is accepting the **trigger** output is ready to receive a trigger. While the **ready for trigger** input is FALSE, a **trigger** will not be produced. The quiet time counter and edge detection circuitry are reset if the **ready for trigger** input is FALSE. The default value is TRUE.

**Data Index**

Specifies the array index of **data in** where the **trigger** occurred. The index of the first sample that meets the trigger criteria is returned.

**Reset**

Toggle the **reset** input to TRUE and then FALSE to reset the internal state of this VI. While in reset, **ready for input** and **output valid** are FALSE and **input valid** is ignored. This VI starts a reset operation when the **reset** input is set to TRUE or when the LabVIEW FPGA reset method is called.

**Pipeline Delay**

4 single-cycle Timed Loop clock cycles

**Approximate resource usage in a Xilinx Virtex-5 or Virtex-6**

Slice flip-flops: 54

Slice LUTs:: 708

Block RAMs (18kb): 0

DSP48E(1)s: 16

**Approximate maximum single-cycle Timed Loop clock rate in a Xilinx Virtex-5 or Virtex-6 (-1)**

160 MHz

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Power Level Trigger - 8 spc - 18 bit.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_power_level_trigger_8_spc_18_bitc.gif']

#### IQ Data to U32.vi

Converts a cluster of I/Q data into separate I and Q data in the fixed-point format, typecasts the separate I and Q data to convert them to I16 values, and bundles the two I16 values into a U32. Overflows are reported from the I/Q data and fixed-point casts.

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:IQ Data to U32.vi' src='../niinstr_dsp_v1_fpga_lvlib_iq_data_to_u32c.gif']

**Input Parameters**

**IQ data** specifies a bundle of real and imaginary (I/Q) data.

**IQ data.I** specifies the bundled real (I) data.

**IQ data.Q** specifies the bundled imaginary (Q) data.

**IQ data.overflow** specifies whether the I/Q data has overflowed.

**Output Parameters**

**U32 data** returns the I/Q data that is bundled into U32 data, with I in the lower 16 bits and Q in the upper 16 bits.

**overflow** indicates whether the I/Q data or any of the typecasts to the U32 data have overflowed.

#### U32 to IQ Data.vi

Splits the **U32 data** input into two I16 values and converts each I16 value into separate I and Q data in the fixed-point format. This VI bundles the separate I and Q data into an I/Q data cluster, with an option to specify an overflow.

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:U32 to IQ Data.vi' src='../niinstr_dsp_v1_fpga_lvlib_u32_to_iq_datac.gif']

**Input Parameters**

**U32 data** specifies the U32 I/Q data, with I in the lower 16 bits and Q in the upper 16 bits.

**overflow** specifies whether the I/Q data has overflowed.

**Output Parameters**

**IQ data** returns a bundle of real and imaginary (I/Q) data.

**IQ data.I** returns the bundled real (I) data.

**IQ data.Q** returns the bundled imaginary (Q) data.

**IQ data.overflow** indicates whether the I/Q data has overflowed.

#### Complex Multiply.vi

Implements a complex multiply using DSP48E blocks.

This VI provides the following functionality:

**IQ Out** = **IQ In 1** * **IQ In 2**

Where "*" represents complex multiplication.

**Pipeline Delay**

5 single-cycle Timed Loop clock cycles

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Complex Multiply.vi' src='../niinstr_dsp_v1_fpga_lvlib_complex_multiplyc.gif']

#### NCO.vi

Creates a cosine/sine pair at the specified frequency. The frequency range is -0.5 to 0.5, and is relative to the input data rate. The spectral performance is 105 dBFS SFDR.

**Pipeline Delay**

6 single-cycle Timed Loop clock cycles

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:NCO.vi' src='../niinstr_dsp_v1_fpga_lvlib_ncoc.gif']

#### Non-symmetric FIR.vi

Implements a general purpose FIR filter. This VI must be used in a single-cycle Timed Loop, and requires an additional in-phase clock at three times the frequency of the single-cycle Timed Loop clock.

The filter coefficients are loaded sequentially using the **filter coefficients** input. Load the coefficients in sequential order: 0, 1, 2, ... 32. There are no requirements to the symmetry of the coefficients.

Complete the following steps to load the coefficients:

1. Set **coef load** high, then low to begin the load sequence.

2. For 33 times: write the coefficient to **coef data** and set **coef write** high, then set **coef write** low.

The new coefficients are applied automatically as they are being written.

You can use the Digital Filter Design Toolkit to calculate coefficients for your desired filtering application.

**Pipeline Delay**

9 single-cycle Timed Loop clock cycles

[IMAGE alt='niInstr_DSP_v1_FPGA_lvlib:Non-symmetric FIR.vi' src='../niinstr_dsp_v1_fpga_lvlib_non-symmetric_firc.gif']

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_fiforb_fpga.html language=enus -->
## TOPIC 00052: FIFO Register Bus FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_fiforb_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_fiforb_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FIFO Register Bus FPGA VIs

#### Create Resources.vi

Creates a FIFO Register Bus using an existing DMA FIFO. You must specify which FIFO is used to retrieve instructions.

[IMAGE alt='niInstr FIFO Register Bus v1 FPGA.lvclass:Create Resources.vi' src='../idl_fiforb_fpgac.gif']

**Input Parameters**

**instruction fifo** specifies the DMA FIFO used to send register instructions to the device. The DMA FIFO must meet the following requirements:

-The DMA FIFO must be instantiated in the LabVIEW project and must have a pre-defined name based on the value passed to the **bus instance** parameter of the **Open Session** VI in the FIFO Register Bus Host library. The format of the name is "reg.host instruction fifo N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "reg.host instruction fifo 0", the instance number of this library is 0.

-The DMA FIFO type must be Host to Target.

-The DMA FIFO data type must be U64.

**Output Parameters**

**fifo register bus** returns a reference to the created FIFO Register Bus. This reference may be used as an instruction producer. You must use this reference as the **fifo register bus** input for the **Host Interface** VI of this library.

#### Host Interface.vi

Connects required controls and indicator signals to FIFO Register Bus resources. This VI must be placed in a Single Cycle Timed Loop and connected to any FIFO Register Bus that is used as an Instruction Producer.

[IMAGE alt='niInstr FIFO Register Bus v1 FPGA.lvclass:Host Interface.vi' src='../niinstr_fifo_register_bus_v1_fpga.lvclass_host_interfacec.gif']

**Input Parameters**

**fifo register bus** provides the resources required to link communication between this host interface, and the register configuration object. This parameter is obtained from the **Create Resources** VI in this library.

**fifo reg bus ctrl 0** controls this instance of the FIFO Register Bus FPGA library.

This parameter must be wired to a control on the top-level FPGA VI, because it must be accessible to the FIFO Register Bus Host library from the FPGA Interface Read/Write Control function. The control must have a pre-defined name based on the value passed to the **bus instance** output of the **Open Session** VI in the FIFO Register Bus Host library. The format of the name is "fifo reg bus ctrl N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "fifo reg bus ctrl 0", the instance number of this library is 0.

**Output Parameters**

**fifo reg bus status 0** indicates the status of the FIFO Register Bus FPGA library.

This parameter must be wired to an indicator on the top-level FPGA VI, because it must be accessible to the FIFO Register Bus Host library from the FPGA Interface Read/Write Control function. The indicator must have a pre-defined name based on the value passed to the **bus instance** output of the **Open Session** VI in the FIFO Register Bus Host library. The format of the name is "fifo reg bus status N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "fifo reg bus status 0", the instance number of this library is 0.

**fifo reg bus data 0** returns data from a FIFO Register Bus read operation.

This parameter must be wired to an indicator on the top-level FPGA VI, because it must be accessible to the FIFO Register Bus Host library from the FPGA Interface Read/Write Control function. The indicator must have a pre-defined name based on the value passed to the **bus instance** output of the **Open Session** VI in the FIFO Register Bus Host library. The format of the name is "fifo reg bus data N", where N is the instance number of the FIFO Register Bus Host library and FIFO Register Bus FPGA library. For example, if the name is "fifo reg bus data 0", the instance number of this library is 0.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_fiforb_host.html language=enus -->
## TOPIC 00053: FIFO Register Bus Host VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_fiforb_host.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_fiforb_host.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FIFO Register Bus Host VIs

#### Open Session.vi

Creates an instruction target session that communicates with an FPGA target using a DMA FIFO. This session can communicate with a corresponding instance of the FIFO Register Bus library on the FPGA.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Open Session.vi' src='../idl_fiforb_hostc.gif']

**Input Parameters**

**fpga ref** specifies a reference to an FPGA VI with a FIFO Register Bus host interface.

**bus instance** specifies which instance of the FIFO Register Bus library this VI should create. Multiple FIFO Register Bus instances may be created in an FPGA VI.

**Note**: This library supports a maximum of eight instances with **bus instance** values of 0 through 7.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Reset.vi

Resets the FIFO register bus.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Reset.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_resetc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Close Session.vi

Closes the session and frees any allocated resources.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Close Session.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_close_sessionc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**error out** contains error information. This output provides standard **error out** functionality.

#### Set Instruction FIFO Depth.vi

Sets the depth of the instruction FIFO. The depth of the FIFO affects the number of instructions that can be queued in the internal buffer.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Set Instruction FIFO Depth.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_set_instruction_fifo_depthc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**instruction fifo depth** specifies the depth, in elements, of the host memory part of the Host to Target DMA FIFO used to transfer instructions from this instance of the FIFO Register Bus Host library to the corresponding instance of the FIFO Register Bus FPGA library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Get Instruction FIFO Depth.vi

Returns the current depth setting of the instruction FIFO.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Get Instruction FIFO Depth.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_get_instruction_fifo_depthc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**instruction fifo depth** returns the depth, in elements, of the host memory part of the Host to Target DMA FIFO used to transfer instructions from this instance of the FIFO Register Bus Host library to the corresponding instance of the FIFO Register Bus FPGA library.

**error out** contains error information. This output provides standard **error out** functionality.

#### Read.vi

Returns a single value read from the target. The **read instruction** input specifies the subsystem ID and address of the data source.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Read.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_readc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**read instruction** specifies the location of the data to read through a **subsystem** ID and an **address**.

**read instruction.subsystem** is the subsystem ID of the register to read.

**read instruction.address** is the address of the register to read.

**timeout (1000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**data** returns the value read from the register subsystem and address specified in the **read instruction** input.

**error out** contains error information. This output provides standard **error out** functionality.

#### Write.vi

Writes a single value to the target. The **write instruction** input specifies the subsystem ID and address of the write destination.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Write.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_writec.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**write instruction** specifies the **data** to write and the destination location. The destination is specified through a **subsystem** ID and an **address**.

**write instruction.subsystem** is the subsystem ID of the write destination.

**write instruction.address** is the address of the write destination.

**write instruction.data** is the data to write.

**timeout (1000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if **wait until committed** is set to TRUE and the write is not verified before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**wait until committed (T)** indicates whether this VI should stop running until it verifies that the target has received and processed the information in the **write instruction** input. This is an optional parameter.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Read Array.vi

Returns one or more values read from the target. The **read instructions** input specifies an array of subsystem IDs and addresses of data sources.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Read Array.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_read_arrayc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**read instructions** specifies an array of locations of data to read. Each element in this array contains a **subsystem** ID and an **address**.

**read instructions.subsystem** is the subsystem ID of the register to read.

**read instructions.address** is the address of the register to read.

**timeout (1000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**data** returns an array of the data read from the register subsystems and addresses specified in the **read instructions** input array.

**error out** contains error information. This output provides standard **error out** functionality.

#### Write Array.vi

Writes one or more values to the target. The **write instructions** input specifies an array of subsystem IDs and addresses of the write destinations.

[IMAGE alt='niInstr FIFO Register Bus v1 Host.lvclass:Write Array.vi' src='../niinstr_fifo_register_bus_v1_host.lvclass_write_arrayc.gif']

**Input Parameters**

**session in** identifies your session. **session in** is obtained from the **Open Session** VI of this library.

**write instructions** specifies an array of **data** to write and destinations to write the data to. Each destination is specified by a **subsystem** ID and an **address**.

**write instructions.subsystem** is the subsystem ID of the write destination.

**write instructions.address** is the address of the write destination.

**write instructions.data** is the data to write.

**timeout (1000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if **wait until committed** is set to TRUE and the write is not verified before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**wait until committed (T)** indicates whether this VI should stop running until it verifies that the target has received and processed the information in the **write instruction** input. This is an optional parameter.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_instfwk_fpga.html language=enus -->
## TOPIC 00054: Instruction Framework FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_instfwk_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_instfwk_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Instruction Framework FPGA VIs

#### Create Resources.vi

Creates a register configuration object that you can use to connect instruction producers with subsystems. Use the **Add Subsystems** VI and **Add Producer** VI to connect libraries that are compatible with the Instruction Framework library.

[IMAGE alt='niInstr Instruction Framework Top Level Bus v1 FPGA.lvlib:Register Configuration.lvclass:Create Resources.vi' src='../idl_instfwk_fpgac.gif']

**Input Parameters**

**register clock** specifies the clock source for the register configuration process. This clock source is also used for the **Bus Interface** VI of each address space, and the **Fetch Instruction** VI of each instruction producer.

**Output Parameters**

**register configuration** returns the newly created register configuration object.

#### Add Subsystems.vi

Connects address spaces to an existing register configuration object.

[IMAGE alt='niInstr Instruction Framework Top Level Bus v1 FPGA.lvlib:Register Configuration.lvclass:Add Subsystems.vi' src='../niinstr_instruction_framework_top_level_bus_v1_fpga.lvlib_register_configuration.lvclass_add_subsystemsc.gif']

**Input Parameters**

**register configuration in** identifies the register configuration object. This parameter is obtained from the **Create Resources** VI of this library.

**subsystems** specifies an address space collection to add to the register configuration. Each address space contained by the collection is added as a separate subsystem.

**Output Parameters**

**register configuration out** passes the modified register configuration object to the next VI.

#### Add Producer.vi

Connects an instruction producer to an existing register configuration object.

[IMAGE alt='niInstr Instruction Framework Top Level Bus v1 FPGA.lvlib:Register Configuration.lvclass:Add Producer.vi' src='../niinstr_instruction_framework_top_level_bus_v1_fpga.lvlib_register_configuration.lvclass_add_producerc.gif']

**Input Parameters**

**register configuration in** identifies the register configuration object. This parameter is obtained from the **Create Resources** VI of this library.

**instruction producer** specifies an instruction producer to add to the register configuration.

**Output Parameters**

**register configuration out** passes the modified register configuration object to the next VI.

#### Process.vi

Fetches and consumes instructions. This VI sends instructions from instruction producers to address spaces, then returns responses from the address spaces back to the instruction producers. Place this VI at the end of a configuration chain.

[IMAGE alt='niInstr Instruction Framework Top Level Bus v1 FPGA.lvlib:Register Configuration.lvclass:Process.vi' src='../niinstr_instruction_framework_top_level_bus_v1_fpga.lvlib_register_configuration.lvclass_processc.gif']

**Input Parameters**

**register configuration** identifies the register configuration object. This parameter is obtained from the **Create Resources** VI.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_instfwk_host.html language=enus -->
## TOPIC 00055: Instruction Framework Host VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_instfwk_host.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_instfwk_host.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Instruction Framework Host VIs

#### Context Read.vi

Returns a single value read from the target. Data source is specified by context and address.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Context Read.vi' src='../idl_instfwk_hostc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**context in** identifies the address space to read data from. This value is obtained from the **Subsystem Lookup** VI of this library.

**address** specifies the address to read data from, relative to the address space associated with the **context in** input.

**timeout (5000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**context out** passes a reference to the context to the next VI.

**data** returns the data read from the address space.

**error out** contains error information. This output provides standard **error out** functionality.

#### Context Write.vi

Writes a single value to the target. Destination is specified by context and address.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Context Write.vi' src='../niinstr_instruction_target_v1_host.lvclass_context_writec.gif']

**Input Parameters**

**instruction target in** identifies your session.

**context in** identifies the address space to write data to. This value is obtained from the **Subsystem Lookup** VI of this library.

**address** specifies the address to write data to, relative to the address space associated with the **context in** input.

**data** specifies the data to write to the address space.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**timeout (5000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to its target, or if **wait until committed** is set to TRUE and the write is not verified before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**wait until committed (T)** indicates whether this VI should stop running until it verifies that the target has received and processed the information in the **data** input. This is an optional parameter.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**context out** passes a reference to the context to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Context Read Array.vi

Returns one or more values read from the target. Data sources are specified by context and an array of addresses.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Context Read Array.vi' src='../niinstr_instruction_target_v1_host.lvclass_context_read_arrayc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**context in** identifies the address space to read data from. This value is obtained from the **Subsystem Lookup** VI of this library.

**addresses** specifies a list of addresses to read data from, relative to the address space associated with the **context in** input.

**timeout (5000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**context out** passes a reference to the context to the next VI.

**data** returns an array of data read from the address space.

**error out** contains error information. This output provides standard **error out** functionality.

#### Context Write Array.vi

Writes one or more values to the target. Destinations are specified by context and the addresses in the **write instructions** array.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Context Write Array.vi' src='../niinstr_instruction_target_v1_host.lvclass_context_write_arrayc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**context in** identifies the address space to write data to. This value is obtained from the **Subsystem Lookup** VI of this library.

**write instructions** is an array. Each element of the array contains **data** to write and the **address** to write the data to.

**write instructions.address** is the address to write to, relative to the address space associated with the **context in** input.

**write instructions.data** is the data to write.

**timeout (5000 ms)** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to its target, or if **wait until committed** is set to TRUE and the write has not been verified before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**wait until committed (T)** indicates whether this VI should stop running until it verifies that the target has received and processed the information in the **data** input. This is an optional parameter.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**context out** passes a reference to the context to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Read Subsystem Map.vi

Retrieves information about the subsystem map from a given target. Returns a list of which address spaces have been connected to the bus, and the routing context required to communicate with these address spaces.

[IMAGE alt='niInstr Subsystem Map v1 Host.lvclass:Read Subsystem Map.vi' src='../niinstr_subsystem_map_v1_host.lvclass_read_subsystem_mapc.gif']

**Input Parameters**

**instruction target in** specifies the target to read the subsystem map from.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**subsystem map** contains the address space map data.

**error out** contains error information. This output provides standard **error out** functionality.

#### Subsystem Lookup.vi

Returns the context for a given address space.

[IMAGE alt='niInstr Subsystem Map v1 Host.lvclass:Subsystem Lookup.vi' src='../niinstr_subsystem_map_v1_host.lvclass_subsystem_lookupc.gif']

**Input Parameters**

**subsystem map in** is the address space map data obtained from the **Read Subsystem Map** VI of this library.

**set error if not found (T)** specifies whether or not this VI should return an error if the lookup fails.

**UID** is the unique identifier of the address space to look up.

**instance** specifies the instance of the address space to look up.

**parent context** specifies a context for the parent of the address space to look up. This parameter is obtained from the **context** output of a previous instance of this VI.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**found?** is TRUE if the address space lookup was successful.

**subsystem map out** passes the subsystem map to the next VI.

**context** contains lookup and routing information necessary to reference the address space found by this VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Subsystem Version Check.vi

Performs a version check, comparing a potential host code version to the version reported by an address space on the target.

[IMAGE alt='niInstr Subsystem Map v1 Host.lvclass:Subsystem Version Check.vi' src='../niinstr_subsystem_map_v1_host.lvclass_subsystem_version_checkc.gif']

**Input Parameters**

**subsystem map in** is the address space map data obtained from the **Read Subsystem Map** VI of this library.

**set error if version mismatch (T)** specifies whether this VI should return an error if the version found is not within the range specified by the **version** and **oldest compatible version** inputs.

**context** specifies the address space to version check.

**version** specifies the version of the host code that is performing the version check.

**oldest compatible version** specifies the oldest version that the host code is backwards-compatible with.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**subsystem map out** passes the subsystem map to the next VI.

**target too old** is TRUE if the target address space is too old to be compatible with the specified **oldest compatible version** of the host code.

**target too new** is TRUE if the target address space is too new and is not backwards-compatible with the specified **version** of the host code.

**error out** contains error information. This output provides standard **error out** functionality.

#### Read.vi

Returns a single value read from the target. The **read instruction** input specifies the subsystem ID and address of the data source.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Read.vi' src='../niinstr_instruction_target_v1_host.lvclass_readc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**read instruction** specifies the location of the data to read through a **subsystem** ID and an **address**.

**read instruction.subsystem** is the subsystem ID of the register to read.

**read instruction.address** is the address of the register to read.

**timeout** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**data** returns the value read from the register subsystem and address specified in the **read instruction** input.

**error out** contains error information. This output provides standard **error out** functionality.

#### Write.vi

Writes a single value to the target. The **write instruction** input specifies the subsystem ID and address of the write destination.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Write.vi' src='../niinstr_instruction_target_v1_host.lvclass_writec.gif']

**Input Parameters**

**instruction target in** identifies your session.

**write instruction** specifies the **data** to write and the destination location. The destination is specified through a **subsystem** ID and an **address**.

**write instruction.subsystem** is the subsystem ID of the write destination.

**write instruction.address** is the address of the write destination.

**write instruction.data** is the data to write.

**timeout** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if **wait until committed** is set to TRUE and the write is not verified before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**wait until committed** indicates whether this VI should stop running until it verifies that the target has received and processed the information in the **write instruction** input. This is an optional parameter.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Read Array.vi

Returns one or more values read from the target. The **read instructions** input specifies an array of subsystem IDs and addresses of data sources.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Read Array.vi' src='../niinstr_instruction_target_v1_host.lvclass_read_arrayc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**read instructions** specifies an array of locations of data to read. Each element in this array contains a **subsystem** ID and an **address**.

**read instructions.subsystem** is the subsystem ID of the register to read.

**read instructions.address** is the address of the register to read.

**timeout** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the register read does not complete and data is not returned before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**data** returns an array of the data read from the register subsystems and addresses specified in the **read instructions** input array.

**error out** contains error information. This output provides standard **error out** functionality.

#### Write Array.vi

Writes one or more values to the target. The **write instructions** input specifies an array of subsystem IDs and addresses of the write destinations.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Write Array.vi' src='../niinstr_instruction_target_v1_host.lvclass_write_arrayc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**write instructions** specifies an array of **data** to write and destinations to write the data to. Each destination is specified by a **subsystem** ID and an **address**.

**write instructions.subsystem** is the subsystem ID of the write destination.

**write instructions.address** is the address of the write destination.

**write instructions.data** is the data to write.

**timeout** specifies the minimum number of milliseconds for this VI to wait before timing out. This VI times out if the session cannot write to the target, or if **wait until committed** is set to TRUE and the write is not verified before the **timeout** that you specify elapses. Set this parameter to -1 if you want this VI to wait indefinitely.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**wait until committed** indicates whether this VI should stop running until it verifies that the target has received and processed the information in the **write instruction** input. This is an optional parameter.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Contextualize Read.vi

Applies a context to an address and returns the resulting **read instruction**. This context is used by other VIs in this library to access this address for read or write operations.

[IMAGE alt='niInstr Instruction Framework Context v1 Host.lvclass:Contextualize Read.vi' src='../niinstr_instruction_framework_context_v1_host.lvclass_contextualize_read.gif']

**Input Parameters**

**context in** specifies the address space used to create the **read instruction**.

**address** specifies the address to read data from. This address is relative to the address space specified by **context in**.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**context out** passes a reference to the context to the next VI.

**read instruction** returns the data required to read data from an register.

**read instruction.subsystem** is the subsystem ID of the register to read.

**read instruction.address** is the address of the register to read.

**error out** contains error information. This output provides standard **error out** functionality.

#### Contextualize Write.vi

Applies a context to an address and returns the resulting **write instruction**. This context is used by other VIs in this library to access this address for read or write operations.

[IMAGE alt='niInstr Instruction Framework Context v1 Host.lvclass:Contextualize Write.vi' src='../niinstr_instruction_framework_context_v1_host.lvclass_contextualize_writec.gif']

**Input Parameters**

**context in** specifies the address space used to create the **write instruction**.

**address** specifies the address to write data to. This address is relative to the address space specified by **context in**.

**data** is the data to write.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**context out** passes a reference to the context to the next VI.

**write instruction** returns the information needed to write to a location.

**write instruction.subsystem** is the subsystem ID of the write destination.

**write instruction.address** is the address of the write destination.

**write instruction.data** is the data to write.

**error out** contains error information. This output provides standard **error out** functionality.

#### Reset.vi

Resets the specified Instruction Target.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Reset.vi' src='../niinstr_instruction_target_v1_host.lvclass_resetc.gif']

**Input Parameters**

**instruction target in** identifies your session.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**instruction target out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Get Subsystem Information.vi

Returns identifying information about a given subsystem.

[IMAGE alt='niInstr Instruction Target v1 Host.lvclass:Get Subsystem Information.vi' src='../get_subsystem_information.gif']

**Input Parameters**

**subsystem map in** is the address space map data obtained from the 'Read Subsystem Map' VI of this library.

**context in** specifies the address space whose information will be returned.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**subsystem map out** passes the subsystem map to the next VI.

**context out** passes the context to the next VI.

**subsystem information** returns information about the address space associated with context in.

**subsystem information.UID** is the unique identifier of the address space.

**subsystem information.instance** is the instance among address spaces having the same UID.

**subsystem information.version** is the current version of the FPGA code.

**subsystem information.oldest compatible version** is the oldest version that the FPGA code is backwards-compatible with.

**error out** contains error information. This output provides standard error out functionality.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_mracq_fpga.html language=enus -->
## TOPIC 00056: Multirecord Acquisition FPGA VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_mracq_fpga.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_mracq_fpga.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Multirecord Acquisition FPGA VIs

#### Create Status DMA FIFO Resources.vi

Instantiates the internal DMA status resources that the Multirecord Acquisition FPGA library uses and bundles them with the external resource that you specify.

[IMAGE alt='niInstr Multirecord Acquisition Common v1 FPGA.lvclass:Create Status DMA FIFO Resources.vi' src='../idl_mracq_fpgac.gif']

**Input Parameters**

**status dma fifo in** specifies the DMA FIFO, instantiated in the LabVIEW project, that the host uses to read status information about the acquisition state. The DMA FIFO must have a predefined name based on the value passed to the **fifo instance** input. The format of the name is 'acq.status fifo N', where N is the **fifo instance**. For example, if the name is 'acq.status fifo 0', the **fifo instance** must be 0.

The simplest method to instantiate a LabVIEW FPGA DMA FIFO is to copy and paste the FIFO from a sample project that already contains the FIFO, and update its configuration as required. Click the Create Project button on the LabVIEW Getting Started window to view the sample project.

**fifo instance** specifies the status DMA FIFO instance number. This number must match the suffix of the FIFO name passed to **status dma fifo in**.

**Output Parameters**

**status dma fifo out** returns a reference to the status dma FIFO resource. This reference should be wired to the Create Resources VI.

#### Create Fetch DMA FIFO Resources.vi

Instantiates the internal DMA fetch resources that the Multirecord Acquisition FPGA library uses and bundles them with the external resource that you specify.

[IMAGE alt='niInstr Multirecord Acquisition Common v1 FPGA.lvclass:Create Fetch DMA FIFO Resources.vi' src='../niinstr_multirecord_acquisition_common_v1_fpga.lvclass_create_fetch_dma_fifo_resourcesc.gif']

**Input Parameters**

**fetch dma fifo in** specifies the DMA FIFO, instantiated in the LabVIEW project, that the host uses to fetch acquired waveforms from the device. The DMA FIFO must have a predefined name based on the value passed to the **fifo instance** input. The format of the name is 'acq.fetch fifo N', where N is the **fifo instance**. For example, if the name is 'acq.fetch fifo 0', the **fifo instance** must be 0.

The simplest method to instantiate a LabVIEW FPGA DMA FIFO is to copy and paste the FIFO from a sample project that already contains the FIFO, and update its configuration as required. Click the Create Project button on the LabVIEW Getting Started window to view the sample project.

**fifo instance** specifies the fetch DMA FIFO instance number. This number must match the suffix of the FIFO name passed to **fetch dma fifo in**.

**Output Parameters**

**fetch dma fifo out** returns a reference to the fetch dma FIFO resource. This reference should be wired to the Create Resources VI.

#### Create Resources.vi

Instantiates the internal memories, FIFOs, and other resources that the Multirecord Acquisition FPGA library uses and bundles them with the external resources that you specify.

Wire the **acquisition** output of this VI to the other Multirecord Acquisition FPGA VIs that are used with this acquisition library instance in your FPGA application.

[IMAGE alt='niInstr Multirecord Acquisition Common v1 FPGA.lvclass:Create Resources.vi' src='../niinstr_multirecord_acquisition_common_v1_fpga.lvclass_create_resourcesc.gif']

**Input Parameters**

**memory clock** specifies the clock domain used in the low-level read and write operations to DRAM. Use a faster clock to get better memory throughput and a slower clock to help the FPGA compilation meet timing constraints. The ideal clock rate for maximum throughput is the native DRAM clock rate of the FPGA target. The frequency of this clock can vary across different types of FPGA targets. Refer to the help file for the hardware that you use as the LabVIEW FPGA target for more information about the native DRAM clock rate.

**instance** specifies the instance number of this Multirecord Acquisition FPGA library instantiation. The value that you specify for **instance** must be equal to the instance number that you specify in the Open Session VI of the Multirecord Acquisition host library.

**memory** specifies the LabVIEW FPGA memory instatiated in the LabVIEW project that stores the acquired waveforms. This memory must either use DRAM or Block RAM for its implementation. DRAM is, instantiated in the LabVIEW project, while Block RAM is VI Defined. The data type of this memory must match the type specified by the instance of the VI you are using.

The simplest method to instantiate a LabVIEW FPGA DRAM memory is to copy and paste an equivalent memory item from a sample project that already contains the memory item, and update its configuration as required. Click the **Create Project** button on the LabVIEW **Getting Started** window to view the sample project.

**memory size (bytes)** specifies the size in bytes of the memory specified by **memory**.

**status dma fifo resource** specifies the DMA FIFO resource that the host uses to read status information about the acquisition state. The DMA FIFO resource is created by the Create Status DMA FIFO Resources VI.

**fetch dma fifo resource** specifies the DMA FIFO resource that the host uses to fetch acquired waveforms from the device. The DMA FIFO resource is created by the Create Fetch DMA FIFO Resources VI.

**Output Parameters**

**acquisition resources** returns the internal resources and resources that you specify, which this instance of the Multirecord Acquisition FPGA library uses. Wire this parameter to other Multirecord Acquisition VIs that you use with this instance of the Multirecord Acquisition library.

**acquisition subsystem** returns the resources used by the Multirecord Acquisition FPGA Library to communicate with the host. Connect this wire to the Instruction Framework library using the Add Subsystem VI.

#### Set Input FIFO.vi

Specifies the FIFO used as the write FIFO. This FIFO accepts the samples that you write to the Write VI and transfers them to the memory clock domain to write to memory.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Set Input FIFO.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_set_input_fifoc.gif']

#### Set Request FIFO.vi

Specifies the FIFO used to queue record read requests. This FIFO resides in the memory clock domain.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Set Request FIFO.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_set_request_fifoc.gif']

#### Set Retrieve FIFO.vi

Specifies the FIFO used to retrieve record data that you request from memory. This FIFO accepts samples read directly from the memory and transfers them to the clock domain to retrieve record data using the Retrieve Record VI.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Set Retrieve FIFO.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_set_retrieve_fifoc.gif']

#### Set Timestamp FIFO.vi

Specifies the FIFO used to capture timestamp values. This FIFO accepts timestamp values that you write to the Write VI and transfers the timestamp values to the memory clock domain to correlate to the correct record data that you write to memory.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Set Timestamp FIFO.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_set_timestamp_fifoc.gif']

#### Process.vi

Contains the free-running process of the Multirecord Acquisition FPGA library. This process implements the various state machines and services needed to provide the core Multirecord Acquisition functionality. This VI also implements interaction with DRAM memory.

At least one instance of this VI must be present in your FPGA design for each instance of the Multirecord Acquisition library.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Process.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_processc.gif']

**Input Parameters**

**acquisition resources** specifies the resources that the current instance of the library uses. You can obtain this value from the Create Resources VI of the Multirecord Acquisition FPGA library.

#### Retrieve Record.vi

Retrieves the record data that you previously requested from the device. You can request the record data using the Fetch Single Record VI, Fetch Multiple Records VI, or Request Record VI in the Multirecord Acquisition host library.

All samples that you retrieve from this VI are presented in the order in which they were fetched. You can add FPGA logic to perform FPGA-side processing of the record data after this VI.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Retrieve Record.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_retrieve_recordc.gif']

**Input Parameters**

**acquisition resources** specifies the resources that the current instance of the Multirecord Acquisition library uses. You can obtain this value from the Create Resources VI of the Multirecord Acquisition FPGA library.

**output array size** specifies the requested array size of **data**. This value must be a constant and a power of 2. If you are retrieving multiple channels, this value must be a multiple of the number of channels in the request.

**ready for output** specifies whether the logic that comes after this VI is ready to accept a new data value.

**Output Parameters**

**channels** returns the number of channels contained in **data**.

**data** returns the data sample that the VI retrieves. If data contains multiple channels then the channels are returned in an interleaved format starting with channel 0.

**retrieve data info** returns information about the request.

**retrieve data info.last sample of request** indicates that **data** contains the last sample of the current request. Wire this value to the Write to Fetch DMA FIFO VI.

**retrieve data info.token** specifies a user defined value that is specified by the host using Fetch Single Record, Fetch Multiple Records, or Request Record VIs.

**output valid** indicates whether the **data** output contains valid data. **output valid** returns TRUE for the clock cycles in which **data** contains a valid data sample. Otherwise, **output valid** returns FALSE.

#### Write to Fetch DMA FIFO.vi

Writes data to the Fetch DMA FIFO. Use the Fetch FIFO to transmit record data from the FPGA to the record fetch VIs on the host.

Connect this VI to the Retrieve Record VI on the FPGA. You can add custom logic between these two VIs to perform custom FPGA processing on the record data.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Write to Fetch DMA FIFO.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_write_to_fetch_dma_fifoc.gif']

**Input Parameters**

**data** specifies the data sample to write to the Fetch DMA FIFO.

**acquisition resources** specifies the resources that the current instance of the Multirecord Acquisition library uses. You can obtain this value from the Create Resources VI of this library.

**channels** specifies the number of channels contained in **data**.

**last sample of request** specifies that **data** contains the last sample of the current request. Wire this value from the Retrieve Record VI.

**input valid** specifies whether the **data** input contains valid data.

**Output Parameters**

**ready for input** indicates whether this VI is ready to accept a new data value on the next clock cycle. **ready for input** returns TRUE if the Write to Fetch DMA FIFO VI is ready to accept a new data value on the next clock cycle. **ready for input** returns FALSE if the VI is not ready to accept a new data value on the next clock cycle.

#### Write.vi

Writes sample data into record memory, which is stored in DRAM/Block RAM. This VI evaluates various acquisition triggers and decides whether to acquire each data value into record memory. This VI organizes the stream of data values into discrete records based on the acquisition configuration and behavior of the acquisition triggers.

Whenever records are acquired, this VI also returns state information about the acquisition. The host application can read the acquired records from DRAM/Block RAM using the Fetch Single Record VI and the Fetch Multiple Records VI of the Multirecord Acquisition host library.

[IMAGE alt='niInstr Multirecord Acquisition v1 FPGA.lvclass:Write.vi' src='../niinstr_multirecord_acquisition_v1_fpga.lvclass_writec.gif']

**Input Parameters**

**data** specifies the data sample to write to the Multirecord Acquisition library.

**acquisition resources** specifies the resources that the current instance of the Multirecord Acquisition library uses. You can obtain this value from the Create Resources VI of the Multirecord Acquisition FPGA library.

**triggers** specifies the triggers that the Write VI uses to determine when to start and stop storing samples for a record.

**triggers.start trigger (T)** specifies the acquisition Start Trigger. After the Initiate VI on the host initiates the acquisition, the Write VI waits for **start trigger** to assert prior to acquiring any record data to memory. Set **start trigger** to TRUE to assert the trigger. This trigger is a level-sensitive signal that is evaluated only once at the beginning of the acquisition.

**triggers.advance trigger (T)** specifies the record Advance Trigger. After you acquire each record fully, the Write VI waits for **advance trigger** input to assert prior to acquiring any data for the next record. Set **advance trigger** to TRUE to assert the trigger. This trigger is a level-sensitive signal that is evaluated once at the beginning of each record.

The Advance Trigger is not evaluated prior to acquiring the first record. The Advance Trigger is evaluated prior to acquiring all other records.

If the acquisition is configured for an infinite number of samples, this trigger is ignored.

**triggers.reference trigger (T)** specifies the record Reference Trigger. If you configure this acquisition for a finite number of samples, the Write VI uses the Reference Trigger to bind the number of samples that you write to each record. The Write VI continually acquires samples to record memory until **reference trigger** asserts. After **reference trigger** asserts, this VI acquires a finite number of samples beyond the Reference Trigger. The number of samples that the Write VI acquires beyond the Reference Trigger is based on the acquisition configuration and can be determined by the following formula:

Reference Trigger = (number of samples in record) â€” (number of pretrigger samples)

Set **reference trigger** to TRUE to assert the trigger. This trigger is a level-sensitive signal.

If you configure the acquisition for an infinite number of samples, the Write VI ignores this trigger.

**triggers.start trigger index** specifies the index of the sample that corresponds to the Start Trigger. Use this input when supplying more than one sample per FPGA clock cycle.

**triggers.advance trigger index** specifies the index of the sample that corresponds to the Advance Trigger. Use this input when supplying more than one sample per FPGA clock cycle.

**triggers.reference trigger index** specifies the index of the sample that corresponds to the Reference Trigger. Use this input when supplying more than one sample per FPGA clock cycle.

**triggers.reference trigger correction cycle count** specifies the number of FPGA clock cycles in the past where the Reference Trigger actually occurred. You can retrieve this value on the host. Use this input with synchronization.

**sample format** specifies additional information about **data**.

**sample format** specifies additional information about **data**. Use this optional input to specify that **data** contains more than one channel. Typically this input is either unwired or provided by the Channel Library.

**data valid** specifies whether the **data** input contains valid data.

**timestamp** specifies the timestamp associated with a particular record. The number of timestamp values per record written to the Write VI must match the **timestamps per record** input on the Configure Acquisition VI in the Multirecord Acquisition host library.

Although stored timestamp values are guaranteed to be correlated with records, they are not correlated with individual samples in those records. The application that uses the Multirecord Acquisition FPGA library must provide sample-level timestamp correlation, if required.

If you do not write the required number of timestamps for each record, the record acquisition process stalls, which may eventually cause a write overflow condition.

**timestamp.timestamp** specifies the timestamp value to associated with a particular record.

**timestamp.timestamp valid** specifies whether the **timestamp** input contains a valid timestamp value.

**Output Parameters**

**status** indicates the current status of the acquisition state machine.

**status.idle** indicates whether the acquisition state machine is currently idle. If you do not initiate an acquisition, the acquisition is idle.

**status.number of records acquired** returns the number of records acquired in the current acquisition.

**status.write overflow** indicates whether a write overflow occurred. All acquired samples are written into the Write FIFO before they are stored in memory. A write overflow is treated as a non-recoverable acquisition error because the acquired data is lost.

The following factors affect the likelihood of a write overflow:

Memory grant time â€” The memory write/read grant time affects the way the FPGA arbitrates between write and read access to DRAM. Ensure that memory writes have sufficient bandwidth relative to the front-end input sample rate.

Status FIFO depth â€” The Status FIFO reports information about acquired records to the host. If the Status FIFO is full, the acquisition FPGA logic prevents writes to memory. Eventually, this can cause the Write FIFO to fill up and overflow. Ensure that the Status FIFO is deep enough for the rate at which the host consumes this FIFO. The host consumes the entire Status FIFO each time you fetch a record or query the acquisition status.

Write FIFO depth â€” The Write FIFO on the FPGA must be deep enough to absorb DRAM latencies. DRAM write latencies vary based on memory grant time and the inherent DRAM physical access overhead.

Insufficient number of timestamps â€” The number of timestamps per record that are provided to the Write VI of the Multirecord Acquisition FPGA library must match the value of the **timestamps per record** input of the Configure Acquisition VI. If the FPGA code does not capture the correct number of timestamps per record, the record acquisition stalls. Eventually, this can cause the Write FIFO to fill up and overflow.

**events** reports various events that occur during the acquisition. Use these events to synchronize external logic with the state of the acquisition.

**events.ready for start** indicates whether the Write VI is ready to receive and react to the assertion of **triggers.start trigger**.

**events.ready for advance** indicates whether the Write VI is ready to receive and react to the assertion of **triggers.advance trigger**.

**events.ready for reference** indicates whether the Write VI is ready to receive and react to the assertion of **triggers.reference trigger**.

**events.end of record** indicates whether the Write VI acquired the last data sample for a record.

**events.done** indicates whether the acquisition is complete. The acquisition is complete after the last record of the acquisition is acquired to memory.

**events.start trigger** indicates whether a trigger is detected on **triggers.start trigger**.

**events.advance trigger** indicates whether a trigger is detected on **triggers.advance trigger**.

**events.reference trigger** indicates whether a trigger is detected on **triggers.reference trigger**.

**record acquisition in progress** indicates whether a record is currently being acquired. Acquisition of a record begins after the Start Trigger or Advance Trigger asserts.

**ready for input** indicates whether this VI is ready to accept a new data value on the next clock cycle. When set to TRUE, this VI is ready to accept a new data value on the next clock cycle. When set to FALSE, this VI is not ready to accept a new data value on the next clock cycle.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_mracq_host.html language=enus -->
## TOPIC 00057: Multirecord Acquisition Host VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_mracq_host.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_mracq_host.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Multirecord Acquisition Host VIs

#### Abort.vi

Stops the signal or record acquisition on the FPGA. The acquisition stops immediately. Therefore, after you call the Abort VI, the most recently acquired record may be incomplete. After stopping the acquisition, the Abort VI retains the acquisition state to enable you to fetch previously acquired records even after you abort the acquisition. You cannot use this VI to abort a pending fetch.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Abort.vi' src='../idl_mracq_hostc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition Host library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Check Write Overflow.vi

Checks for a Write FIFO overflow error on the FPGA. All acquired samples are written into the Write FIFO before they are eventually stored in memory. A Write FIFO overflow is treated as a non-recoverable acquisition error, because the acquired data is lost.

The following factors affect the likelihood of a write overflow:

Memory grant times â€” The memory write/read grant time affects the way the FPGA arbitrates between write and read access to the memory. Ensure that memory writes have sufficient bandwidth relative to the front-end input sample rate.

Status FIFO depth â€” The Status FIFO reports information about acquired records to the host. If the Status FIFO is full, memory writes are delayed. Eventually, this can cause the Write FIFO to fill up and overflow. Ensure that the Status FIFO is deep enough for the rate that the host consumes the Status FIFO. The host consumes the entire Status FIFO each time you fetch a record or query the acquisition status.

Write FIFO depth â€” The Write FIFO on the FPGA must be deep enough to absorb the DRAM latencies. The DRAM write latencies vary based on memory grant time and inherent DRAM physical access overhead.

Insufficient number of timestamps - The number of timestamps per record that are provided to the Write VI of the Multirecord Acquisition FPGA library must match the value of the **timestamps per record** input of the Configure Acquisition VI. If the FPGA code does not capture the proper number of timestamps per record, the record acquisition stalls. Eventually, this can cause the Write FIFO to fill up and overflow.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Check Write Overflow.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_check_write_overflowc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**overflow occurred** indicates whether a write overflow occurred.

**error out** contains error information. This output provides standard **error out** functionality.

#### Close Session.vi

Closes the session to the Multirecord Acquisition library, destroys the session reference, and deallocates resources associated with the session.

Calling the Close Session VI does not abort an acquisition that is in progress. You cannot use this VI to abort a pending fetch.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Close Session.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_close_sessionc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**error in** describes error conditions that occur before this node runs. With the following exception, this input provides standard **error in** functionality. This node runs normally even if an error occurred before this node runs.

**Output Parameters**

**error out** contains error information. This output provides standard **error out** functionality.

#### Configure Acquisition.vi

Configures the parameters for multiple records in an acquisition. You must run this VI before initiating an acquisition.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Configure Acquisition.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_configure_acquisitionc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**number of records is finite** specifies whether to acquire a finite number of records, or to acquire records continuously. The default value is TRUE.

**number of samples is finite** specifies whether to acquire a finite number of samples, or to acquire samples continuously. The default value is TRUE.

**number of records** specifies the number of records to acquire if **number of records is finite** is set to TRUE. The default value is 1.

**number of samples** specifies the number of samples per record if **number of samples is finite** is set to TRUE. The default value is 1,000.

**pretrigger samples** specifies the number of samples to store for each record that was acquired in the time period immediately before the Reference Trigger occurred. The default value is 0.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**additional acquisition configuration** specifies additional advanced configurations.

**additional acquisition configuration.record padding (samples)** specifies additional padding to allocate for a record. This parameter can be useful in combination with adjusting the Reference Trigger position. The default value is 0.

**additional acquisition configuration.require finite records to fit in memory** specifies that the requested number of records and samples must fit into memory for finite acquisitions. This parameter ensures that requested data cannot be overwritten for finite acquisitions. The default is TRUE.

**additional acquisition configuration.timestamps per record** specifies the number of timestamp values the FPGA captures for each record. This value must match the number of timestamps per record provided to the Write VI of the Multirecord Acquisition FPGA library. The default value is 0.

**additional acquisition configuration.status fifo depth (records)** Sets the depth of the record status DMA FIFO. The Status FIFO reports information about the current state of the acquisition to the host.

Ensure that the Status FIFO is deep enough for the rate at which the host consumes this FIFO. If the Status FIFO is full, memory writes are delayed. Eventually, this can cause the Write FIFO to fill up and overflow. The host consumes the entire Status FIFO each time you fetch a record or query acquisition status. The value is specified in units of records. The default value is 10,000 records.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**record allocation info** returns information about the allocation of records in onboard memory. This information can be useful in determining maximum number of records or samples that can fit in memory.

**error out** contains error information. This output provides standard **error out** functionality.

#### Fetch Multiple Records.vi

Fetches data from multiple records in an acquisition. The fetch operation transfers acquired waveform data from the DRAM/Block RAM on the device to computer memory. The data was acquired to the DRAM/Block RAM by the hardware after the acquisition was initiated.

If the number of samples specified in **number of samples** is not available after the time duration specified by **timeout**, the Fetch Multiple Records VI returns a timeout error with no data.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Fetch Multiple Records.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_fetch_multiple_recordsc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**starting record** specifies the first record to retrieve. Record numbers are zero-based. The default value is 0.

**number of records** specifies the number of records to fetch. The default value is 1.

**fetch relative to** specifies the reference location within the acquired record from which the Fetch Multiple Records VI begins fetching data.

**First Sample**: the fetch starts at the first sample acquired by the device. If the device wraps data in its memory buffer, the first sample is no longer available. In this case, the VI returns an error if **fetch offset** specifies a location that is within the overwritten portion of the memory buffer.

**Reference Trigger Sample**: the fetch starts relative to the Reference Trigger.

**First Pretrigger Sample**: the fetch starts relative to the first pretrigger sample acquired. If you do not configure a Reference Trigger, **First Pretrigger Sample** behaves the same as **First Sample** because there are no pretrigger samples.

**Most Recent Sample**: the fetch starts relative to the most recently acquired sample. The value of **fetch offset** must be negative. This VI doesn't support this option. Consider using the Fetch Single Record VI instead.

**Current Read Position**: the fetch starts after the last fetched sample. This VI doesn't support this option. Consider using the Fetch Single Record VI instead.

**number of samples** specifies the number of samples to fetch. The default value is 0.

**timeout (ms)** specifies the time, in milliseconds, allotted for the Fetch Multiple Records VI to complete execution of each record before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. A value of 0 is not supported. The default value is 10,000. You cannot abort a pending fetch using the Abort VI or Close VI.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**fetch offset** specifies the offset relative to the position specified by **fetch relative to**, from which to start fetching data. **fetch offset** can be a positive or negative value. The default value is 0.

**token** specifies a value that is passed with the record request. The value is returned by the Retrieve Record VI in the FPGA. You can use this information to configure FPGA processing in the retrieve loop.

**scaling coefficients** specifies scaling coefficients for instances of this VI that return double data. The VI uses the coefficients to scale the requested data. Each index of the array corresponds to a channel. The data is multiplied by the gain factor prior to adding the specified offset, using the following equation:

**data** = (binary hardware data * gain / maximum binary value) + offset.

A gain value of 1 and an offset value of 0 has no effect on the binary data. The default behavior does not change the binary data.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**data** returns the acquired records. Each waveform corresponds to a record. If the fetch contains multiple channels, all waveforms for a record are returned before proceeding to the next record. For example a two channel, two record acquisition returns four waveforms:

array index 0 = Channel0 Record0

array index 1 = Channel1 Record0

array index 2 = Channel0 Record1

array index 3 = Channel1 Record1

**requested records info** returns additional information about each record returned by **data**. There is one element in the **requested records info** array for each record.

**requested records info.number of samples** returns the number of samples in the record.

**requested records info.starting sample number** returns the sample number of the first sample in the returned record data. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample.

**requested records info.number of channels** returns the number of channels in the record data.

**requested records info.timestamps** returns the timestamp values that were captured for the record.

**error out** contains error information. This output provides standard **error out** functionality.

#### Fetch Single Record.vi

Fetches data from a single record in an acquisition. The fetch operation transfers waveform data, which is acquired by the hardware, from the memory on the device to the computer memory.

If the number of samples specified in **number of samples** is not available after the time duration specified by **timeout**, the Fetch Single Record VI returns a timeout error with no data.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Fetch Single Record.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_fetch_single_recordc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**record number** specifies the record to retrieve. Record numbers are zero-based. The default value is 0.

**fetch relative to** specifies the reference location within the acquired record from which the Fetch Single Record VI begins fetching data.

**First Sample**: the fetch starts at the first sample acquired by the device. If the device wraps data in its memory buffer, the first sample is no longer available. In this case, the VI returns an error if the **fetch offset** parameter specifies a location that is within the overwritten portion of the memory buffer.

**Reference Trigger Sample**: the fetch starts relative to the Reference Trigger.

**First Pretrigger Sample**: the fetch starts relative to the first pretrigger sample acquired. If you do not configure a Reference Trigger, **First Pretrigger Sample** behaves the same as **First Sample** because there are no pretrigger samples.

**Most Recent Sample**: the fetch starts relative to the most recently acquired sample. The value of **fetch offset** must be negative.

**Current Read Position**: the fetch starts after the last fetched sample.

**number of samples** specifies the number of samples to fetch. The default value is 1,000.

**timeout (ms)** specifies the time, in milliseconds, allotted for the Fetch Single Record VI to complete before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies that the VI immediately returns available data. The default value is 10,000. You cannot abort a pending fetch using the Abort VI or Close VI.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**fetch offset** specifies the offset relative to the position specified by **fetch relative to**, from which to start fetching data. Offset can be a positive or negative value. The default value is 0.

**token** specifies a value that is passed with the record request. The value is returned by the Retrieve Record VI in the FPGA. This information can be used by the user to configure FPGA processing in the retrieve loop.

**scaling coefficient** specifies user defined scaling coefficients for instances of this VI that return double data. The VI will use the coefficients to scale the requested data. The data is multiplied by the gain factor prior to adding the specified offset, as shown in the following equation:

**data** = binary hardware data * gain / maximum binary value + offset.

A gain value of 1 and an offset value of 0 has no effect on the binary data. The default behavior does not change the binary data.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**data** returns the acquired record. If more than one channel is returned, each waveform corresponds to a channel.

**requested record info** returns additional information about the fetched record data.

**requested record info.number of samples** returns the number of samples in the record.

**requested record info.starting sample number** returns the sample number of the first sample in the returned record data. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample.

**requested records info.number of channels** returns the number of channels in the record data.

**requested record info.timestamps** returns the timestamp values that were captured for the record.

**error out** contains error information. This output provides standard **error out** functionality.

#### Get Acquisition Status.vi

Checks the status of the acquisition. This VI determines the number of acquired records and checks the state of the record for which acquisition is happening. This VI also reports write overflow conditions.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Get Acquisition Status.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_get_acquisition_statusc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**overflow occurred** indicates whether a write overflow occurred. Refer to the Check Write Overflow VI for more information about write overflows.

**session out** passes a reference to your session to the next VI.

**done** indicates whether all records have been acquired.

**records done** returns the number of records that have been completely acquired.

**current record status** returns information about the record that is currently being acquired.

**current record status.started** indicates whether a record is currently being acquired.

**current record status.reference trigger detected** indicates whether the Reference Trigger has been detected for the currently acquiring record.

**current record status.reference trigger sample number** returns the sample number that corresponds to the Reference Trigger sample for the currently acquiring record. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample.

**current record status.samples written** returns the total number of samples acquired for the currently acquiring record. This parameter returns 0 if you set **query hw for number of samples written for current record** to FALSE.

**error out** contains error information. This output provides standard **error out** functionality.

#### Get Fetch Backlog.vi

Returns the number of samples that are available to be fetched from the specified fetch position.

The combination of **fetch relative to** and **fetch offset** identify a specific sample within the acquired record. This VI reports the number of samples that are available to fetch starting at the specified sample.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Get Fetch Backlog.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_get_fetch_backlogc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**record number** specifies the record from which to read the backlog. Record numbers are zero-based. The default value is 0.

**fetch relative to** specifies the reference location within the acquired record from which to read the backlog.

**First Sample**: The backlog calculation starts relative to the first sample acquired by the device. If the device wraps data in its memory buffer, the first sample is no longer available. In this case, the VI returns an error if **fetch offset** specifies a location that is within the overwritten portion of the memory buffer.

**Reference Trigger Sample**: The backlog calculation starts relative to the sample that was acquired with the Reference Trigger.

**First Pretrigger Sample**: The backlog calculation starts relative to the first pretrigger sample acquired. If you do not configure a Reference Trigger, **First Pretrigger Sample** behaves the same as **First Sample** because there are no pretrigger samples.

**Most Recent Sample**: The backlog calculation starts relative to the most recently acquired sample. The value of **fetch offset** must be negative.

**Current Read Position**: The backlog calculation starts after the last fetched sample.

**fetch offset** specifies the offset relative to the position, which is specified by **fetch relative to**, from which to calculate the backlog. **fetch offset** can be a positive or negative value. The default value is 0.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**fetch backlog** returns the number of samples available to be fetched.

**error out** contains error information. This output provides standard **error out** functionality.

#### Get Number of Outstanding Record Requests.vi

Returns the number of record read requests that were submitted to the device but are not yet complete. A record read request is complete after the host retrieves the associated record data from the device.

Use this low-level VI primarily with the Request Record and Retrieve Record VIs. This VI effectively reports the number of times your application must call the Retrieve Record VI to retrieve all record data that was previously requested.

You do not need to use this VI when using the Fetch Single Record VI or Fetch Multiple Records VI. Use this VI with the Request Record VI and Retrieve Record VI to pipeline the process on the host that manages requesting and retrieving data from the device. The Fetch Single Record VI or Fetch Multiple Records VI performs these lower level record request and retrieval mechanisms for you.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Get Number of Outstanding Record Requests.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_get_number_of_outstanding_record_requestsc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**number of outstanding record requests** returns the total number of record read requests that were submitted to the device but are not yet complete.

**error out** contains error information. This output provides standard **error out** functionality.

#### Get Record Status.vi

Returns detailed acquisition state information about a specified record.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Get Record Status.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_get_record_statusc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**record number** specifies the record number for which to obtain status information. Record numbers are zero-based. The default value is 0.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**record status** returns status information about the specified record.

**record status.state** returns the acquisition state of the record.

**Not Started**: the first sample has not yet been acquired for this record.

**Being Acquired**: the record is currently being acquired into device memory.

**Completed**: the last sample for the record has been acquired into the memory. The record is available to fetch from the device.

**Overwritten**: the record was previously acquired, but it was overwritten in memory. The record is not available to fetch.

**record status.ref trigger detected** indicates whether the Write VI of the Multirecord Acquisition FPGA library detected the Reference Trigger for the specified record.

**record status.ref trigger sample number** returns the sample number that corresponds to the Reference Trigger sample for the specified record. Sample numbers are zero-based. Sample numbers always start at zero for each record and increment by one for each acquired sample.

**record status.first pretrigger sample number** returns the sample number that corresponds to the first pretrigger sample for the specified record. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample.

**record status.samples written** returns the total number of samples acquired for the specified record.

**record status.current read position** returns the sample number of the current read position within the record. This parameter denotes the current position of the record read pointer when fetching records relative to **current read position**. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample.

**record status.first valid sample** returns the sample number of the oldest sample that is available to be fetched from the device. Sample numbers are zero-based. Sample numbers always start at zero for each record and increment by one for each acquired sample.

**record status.last valid sample to request** returns the sample number of the newest sample that can be fetched. Sample numbers are zero-based. Sample numbers always start at zero for each record and increment by one for each acquired sample.

**record status.timestamps** returns the timestamp values that were captured for the record.

**error out** contains error information. This output provides standard **error out** functionality.

#### Initiate.vi

Starts a new acquisition on the FPGA. You must configure the acquisition using the Configure Acquisition VI prior to calling the Initiate VI. Only call the Initiate VI when there is no acquisition in progress, otherwise subsequent fetches will not return samples.

After calling this VI, the FPGA is sensitive to the various acquisition triggers such as Start, Reference, and Advance Triggers. After triggering conditions are satisfied, the FPGA immediately begins acquiring data into record memory in the DRAM or Block RAM.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Initiate.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_initiatec.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Open Session.vi

Opens a session to the instance of the Multirecord Acquisition library on the device that is connected to the instance of **register bus session in**. Use **session out** to identify the Multirecord Acquisition library in all subsequent Multirecord Acquisition VIs.

[IMAGE alt='niInstr Multirecord Acquisition Common v1 Host.lvclass:Open Session.vi' src='../niinstr_multirecord_acquisition_common_v1_host.lvclass_open_sessionc.gif']

**Input Parameters**

**register bus** specifies a reference to the Register Bus session, which identifies the instance of the Register Bus library to which this instance of the Multirecord Acquisition library is connected in the FPGA.

**fpga interface** specifies the reference to the FPGA interface.

**subsystem map** specifies the reference to the subsystem map. This reference is provided by calling the Read Subsystem Map VI from the Instruction Framework host library.

**instance** specifies the instance number of the Multirecord Acquisition FPGA library for which to open a session. This value must match the value of **instance** of the Create Resources VI in the Multirecord Acquisition FPGA library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Request Record.vi

Submits a request to read a particular record from the device. This VI does not wait for the record data to be retrieved from the device. This VI completes execution immediately after submitting the record read request.

Use this low-level VI primarily with the Retrieve Record VI. You do not need to use the Request Record VI when using the Fetch Single Record VI or Fetch Multiple Records VI. Use the Request Record VI along with the Retrieve Record VI to pipeline the process on the host that manages requesting and retrieving data from the device. The Fetch Single Record VI or Fetch Multiple Records VI performs these lower level record request and retrieval mechanisms for you.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Request Record.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_request_recordc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**record number** Specifies the record number to request. Record numbers are zero-based. The default value is 0.

**starting sample number** specifies the first sample number of the block of record samples to request. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each acquired sample.

**number of samples** Specifies the number of samples to request. The default value is 1,000.

**token** specifies a value that is passed with the record request. The value is returned by the Retrieve Record VI in the FPGA. You can use this information to configure FPGA processing in the retrieve loop.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Reset.vi

Resets the host session and the instance of the Multirecord Acquisition FPGA library to which this session is connected.

This VI aborts any active acquisition on the device. This VI does not change the current settings for Read Memory Grant Time, Write Memory Grant Time, Fetch FIFO Depth, or Status FIFO Depth.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Reset.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_resetc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Retrieve Record.vi

Retrieves record data that you requested using the Request Record VI. The Retrieve Record VI retrieves samples in the same order in which they were originally requested. When returning multiple channels, this VI returns the data interleaved with channel 0 starting at array index 0. Use the Get Number of Outstanding Record Requests VI to determine the number of pending record requests.

This is a low-level VI that is used primarily with the Request Record VI. You do not need to use this VI when using the Fetch Single Record VI or Fetch Multiple Records VI. The Retrieve Record VI, along with the Request Record VI, is useful if you want to pipeline the process on the host that manages requesting and retrieving data from the device. The Fetch Single Record VI or Fetch Multiple Records VI effectively wraps these lower level record request and retrieval mechanisms.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Retrieve Record.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_retrieve_recordc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**samples to retrieve (-1)** specifies the number of samples that the VI must retrieve. A value of -1 specifies that this VI must retrieve all samples that were specified in the original Request Record VI call. National Instruments recommends that you set **samples to retrieve** to -1. However, you can adjust **samples to retrieve** to retrieve partial samples of a record request. The default value is -1.

**timeout (ms)** specifies the time, in milliseconds, allotted for the Retrieve Record VI to complete before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. The default value is 10,000. You cannot abort a pending fetch using the Abort VI or Close VI.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**data** returns the record data that was retrieved from the device. When returning multiple channels, the data is returned interleaved with channel 0 starting at array index 0.

**requested record info** returns information about the original record request.

**requested record info.number of samples** returns the number of samples that were retrieved.

**requested record info.starting sample number** returns the sample number of the first sample in the retrieved data. Sample numbers are zero-based. Sample numbers start at zero for each record and increment by one for each sample that is acquired.

**requested records info.number of channels** returns the number of channels in the record data.

**requested record info.timestamps** returns the timestamp values that were captured for this record.

**done with retrieve** indicates when all requested samples have been retrieved. EDVR instances of this VI must be called in a loop until this parameter returns TRUE. You can use EDVR instances of this VI to optimize performance by allowing access to the low-level data buffer.

**error out** contains error information. This output provides standard **error out** functionality.

#### Set Fetch FIFO Depth.vi

Sets the depth of the DMA FIFO that fetches record data from the device. When deciding the depth of the DMA FIFO, you must consider the size of the fetched records and the number of record requests to queue up simultaneously. For optimal performance, the DMA FIFO must be large enough to satisfy each of these constraints.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Set Fetch FIFO Depth.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_set_fetch_fifo_depthc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**fifo depth (bytes)** specifies the depth, in bytes, of the DMA FIFO.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Set Memory Read Grant Time.vi

Configures the read grant time setting of the time-slot arbiter that controls DRAM access on the device.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Set Memory Read Grant Time.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_set_memory_read_grant_timec.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**grant time (clocks)** specifies the number of back-to-back clock cycles to allocate for memory read operations. These are clock cycles of the process clock that is wired to the Create Resources VI of the Multirecord Acquisition FPGA instance of the Multirecord Acquisition library. The default value is 0.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Set Memory Write Grant Time.vi

Configures the write grant time setting of the time-slot arbiter that controls DRAM access on the device.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Set Memory Write Grant Time.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_set_memory_write_grant_timec.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**grant time (clocks)** specifies the number of back-to-back clock cycles to allocate for memory write operations. These are clock cycles of the process clock that is wired to the Create Resources VI of the Multirecord Acquisition FPGA instance of the Multirecord Acquisition library. The default value is 0.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard **error out** functionality.

#### Wait for Samples.vi

Waits for the requested number of samples to be available. The VI returns the starting sample number of the request. You can use **starting sample number** with the Request Record VI. You must run this VI after initiating an acquisition.

[IMAGE alt='niInstr Multirecord Acquisition v1 Host.lvclass:Wait for Samples.vi' src='../niinstr_multirecord_acquisition_v1_host.lvclass_wait_for_samplesc.gif']

**Input Parameters**

**session in** specifies your session. **session in** is obtained from the Open Session VI of the Multirecord Acquisition host library.

**record number** specifies the record to retrieve. Record numbers are zero-based.

**fetch relative to** specifies the reference location within the acquired record for this VI to wait for before returning.

**number of samples** specifies the number of samples to request.

**timeout (ms)** specifies the time, in milliseconds, allotted for the Fetch Multiple Records VI to complete execution before returning a timeout error. A value of -1 specifies that the VI waits until all data is available. A value of 0 specifies that the VI immediately returns available data. The default value is 10,000. A pending wait can not be aborted using the Abort VI or Close VI.

**fetch offset** specifies the offset relative to the position specified by the **fetch relative to** input, from which to start fetching data. Offset can be a positive or negative value. The default value is 0.

**error in** describes error conditions that occur before this node runs. This input provides standard **error in** functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**starting sample number** Indicates the first sample number of the block of record samples. Sample numbers are zero based. Sample numbers start at zero for each record and increment by one for each sample that is acquired.

**number of samples (coerced)** indicates the actual number of samples the function waited for. This value may be coerced depending on the configured acquisition settings.

**error out** contains error information. This output provides standard **error out** functionality.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_streaming_ll_vis.html language=enus -->
## TOPIC 00058: Low Level Streaming VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_streaming_ll_vis.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_streaming_ll_vis.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Low Level Streaming VIs

#### Data_Stream_Control_(Additive).vi

Use this VI in additive stream functions. This VI splits the stream control between fast data interface loops and slow data control/processing loops.

[IMAGE alt='Data Stream Control Additive' src='../data_stream_control_(additive).gif']

#### Monitor Stream.vi

This polymorphic VI provides several monitoring functions for FPGA streams. Refer to the specific instance VIs for details.

[IMAGE alt='Monitor stream' src='../monitor_fifo_health.gif']

This VI contains the following instance VIs:

- Monitor FIFO Health.vi
- Monitor Minimum Samples Ready.vi

#### Monitor FIFO Health.vi

Use this VI to enable applications to keep track of various parameters of a FIFO under control. This VI is optional, and is often most useful in diagnosing problems with throughput.

You can also use this VI to allow the host to wait for the FIFO to be full enough or empty enough to begin a transfer. This process is called priming the FIFO, and it ensures that data is available to use before starting a stream. If you want the FPGA to manage waiting for the FIFO to be primed, use the Monitor Minimum Samples Ready VI.

[IMAGE alt='Monitor FIFO Health' src='../monitor_fifo_health.gif']

Connect all terminals with a number suffix to the host by controls and indicators. The number allows the host to resolve different stream numbers from the host interface.

|  | Note Some terminals are optional. |
| --- | --- |

This VI is commonly used in conjunction with the Wait for Samples Ready or Get Stream Samples Ready host VIs, which inspect the value in **stream.num samples ready N**.

**Parameters**

**samples in fifo** Connect the output of the FPGA FIFO Method **Get Number of Elements to Read** or **Get Number of Elements to Write** for the FIFO that will be monitored.

**stream.reset health monitor *N*** Connect a control to this VI to allow the host to clear the state of the monitor and to clear the memory of the outputs **stream.max samples ready** and **stream.min samples ready**.

**stream.num samples ready *N*** reflects the current value reported to the **samples in fifo** terminal.

**stream.max samples ready *N*** reflects the highest value reported to the **samples in fifo** terminal since the last reset.

**stream.min samples ready *N*** reflects the lowest value reported to the **samples in fifo** terminal since the last reset.

#### Monitor Minimum Samples Ready.vi

This VI enables the FPGA to independently manage waiting for the FIFO to be primed. This VI is optional, and is most often useful in applications that require uninterrupted streaming output.

If you want the host to manage waiting for the FIFO to be primed, use the **Monitor FIFO Health** VI.

[IMAGE alt='Monitor Minimum Samples Ready' src='../monitor_minimum_samples_ready.gif']

Connect all terminals with a number suffix to the host by controls and indicators. The number allows the host to resolve different stream numbers from the host interface. However, this VI does not have a standard VI on the host to program this value. Use the stock NI-RIO FPGA Host Interface to write to the controls.

**Parameters**

**stream.minimum elements to start *N*** specifies the minimum number of samples to wait for permission to use before asserting the output **ready for start** to True.

**stream.num samples *N*** should be connected to the **stream.num samples *N*** control used in the Data Stream Control VI. This connection enables you to specify a transfer size smaller than the minimum but still automatically start when all data to be transferred is ready.

**permissed elements** 
Connect the output of the FPGA FIFO Method Get Number of Elements to Read or Get Number of Elements to Write for the FIFO that will be monitored.

**ready for start** is enabled when the minimum number of samples that you specified in **stream.minimum elements to start *N*** is reached.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_streaming_vis.html language=enus -->
## TOPIC 00059: Streaming VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_streaming_vis.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_streaming_vis.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Streaming VIs

#### Data Stream Control.vi

This VI enables the control and monitoring of finite and continuous streams of data.

[IMAGE alt='Data Stream Control' src='../data_stream_control.gif']

#### **Signals**

Use the **stream.request state** and **stream.num samples** inputs to control the stream. Use the **stream.state** and **stream.samples transferred** outputs to monitor the stream. You can also use **stream.metadata** to publish details about the form and function of the stream.

When **data valid** is True, and **ready for input?** is True, the Data Stream Control asserts **send data** until the transfer completes.

When **data valid** is True, but **ready for input?** is False, the stream stops asserting **send data** and enters the **Error** state.

When **force error** is True, the stream is forced into the Error state. This allows user logic to monitor for fatal conditions and stop the stream.

**stream.samples transferred** is updated after the **data valid** clock cycle that increments it. This enables this output to have an easier time meeting the timed loop deadline, as well as enables it to be directly wired up as an indexing input to a write memory element.

**request data** informs upstream nodes that the Data Stream Control is requesting data delivery in the next clock cycle.

Note, however, that the Data Stream Control does not provide caching. To avoid overflows, directly connect the **ready for input?** terminal to upstream data, as well as to the Data Stream Control.

**ready for data?** informs the Data Stream Control that the downstream node is ready to accept data.

#### **Detailed Operation**

The state machine has two fundamental modes of transfer: **Finite** and **Continuous**.

In **Finite** mode, the state machine counts **stream.num samples** in increments of **element count**. When the count is equal to or exceeds **stream.num samples**, it prevents the assertion of **send data** and enters the **Done** state. In the **Done** state the samples transferred continue to be reported until the user requests that the state machine return to **Idle.**

In **Continuous mode**, the state machine behaves identically to **Finite** mode, but continuously transfers samples instead of counting them.

#### **States**

The stream can exist in seven potential states. Monitor all commanded states from the controlling loop to ensure that the state is actually entered. The **stream.request state** commands the stream into a state, and **stream.state** reflects the current actual state.

**Idle** - When the stream is ready to enter into an active state, it is in the **Idle** state. While it can be commanded directly to **Idle** from any state (other than **Not Ready**), it is advisable to do so with caution as samples abandoned in transfers may still need to be manually cleared out. It is generally safe to go directly from **Done** to **Idle,** and it is generally safe to request a transition from **Not Ready** to **Idle.** Other states may require further clean-up such as stopping/starting FIFOs or resetting other code under the command of the stream. Consider using **Cancel** instead (such as through the Stop Stream VI in the host environment). While in **Idle** mode, **stream.samples transferred** is reset to 0.

**Finite Transfer** - Execute a transfer for the requested number of samples. **data valid** is passed through to **send data** until the stream terminates. Upon an orderly completion, this VI will automatically enter the **Done** state. If a stream overflows because **data valid** is True, but **ready for input?** is False, the stream stops asserting **send data** and enters the **Error** state.

**Continuous** - Execute a transfer indefinitely. This state operates identically to the **Finite Transfer** state, but without regard to the **stream.num samples** input.

**Done** - In an orderly termination of a finite stream, the stream should end up here. At this point, **stream.samples transferred** accurately reflects the terminal state of the transfer. The **Done** state should be exited by requesting **Idle.** **Cancel** mode or further active transfer modes (**Finite** or **Continuous**) will be ignored. This allows the host to distinguish between streams that are prematurely terminated (thus potentially requiring a flush of abandoned data) and ones that completed naturally.

**Error** - If the stream detects an unplanned interruption of the data, it enters the **Error** state. The error state is normally considered a fatal state, although one may enter it purposefully (such as at the end of a long, Continuous mode Host to Target transfer). The only way to exit the **Error** state is to command the Data Stream Control back to **Idle**, or reset the FPGA VI. When commanded to **Idle**, the Data Stream Control advances first to **Not Ready**.

**Not Ready** - In this state, the FPGA remains Not Ready until the **ready for input?** parameter becomes true. This prevents starting a transfer in an obviously invalid state, and allows host control to wait until the **not ready** state is removed (such as by clearing out a FIFO under the streaming API's control). Although unusual to command the stream into this state, you can use the features of this state to avoid going to idle until the FPGA indicates readiness.

**Cancel** - this state is indistinguishable from **Done,** but allows the controlling VI to know what condition caused the transfer to terminate.

#### Basic Start Trigger.vi

Provides a boolean start trigger function to control the start of data flow in a stream. All three boolean inputs are optional and are set to True by default.

[IMAGE alt='basic start trigger' src='../basic_start_trigger.gif']

You should connect the Basic Start Trigger **stream.state** to the Data Stream Control **stream.state** via a feedback node or shift register.

When the stream enters a transferring state, it indicates that the stream is active, and therefore can activate the flow of data using Basic Start Trigger.vi. The **data valid** output is gated on receiving a True on **start trigger** while the stream is active and **ready for start trigger** is also True. Once a start trigger is received, then the **data valid?** input is reflected through to the **data valid** output until the stream leaves an active state.

The **start trigger** does not need to coincide with a True on **data valid?** input.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen.html language=enus -->
## TOPIC 00060: Waveform Generation VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Waveform Generation VIs

#### Create Data Write DMA FIFO Resources.vi

[IMAGE alt='img.vi' src='../wfgencreate_data_write_dma_fifo_resources_u8x4.gif']

Instantiates the internal DMA FIFO resources that the Waveform Generation FPGA library uses, and bundles them with the external resource that you specify.

This polymorphic VI contains the following instance VI:

- Create Data Write DMA FIFO Resources U8x4

**Input Parameters**

**fifo** specifies the DMA FIFO, instantiated in the LabVIEW project, that the host uses to download waveforms and instructions to the target device. The DMA FIFO must have a predefined name based on the value passed to the **fifo instance** input. The format of the name is wfm gen.download fifo N, where N is the **fifo instance** and in the range of 0 to 7. For example, if the name is "wfm gen.fetch fifo 0", the **fifo instance** must be 0. 


The simplest method to instantiate a LabVIEW FPGA DMA FIFO is to copy and paste the FIFO from a sample project that already contains the FIFO, and update its configuration as required.

**fifo instance** specifies the Data Write DMA FIFO instance number. This number must match the suffix of the FIFO name passed to **fifo**.

**Output Parameters**

**data write dma fifo out** returns a reference to the data write DMA FIFO resource. Wire this reference to the **Create Resources** VI of this library.

#### Create Resources.vi

[IMAGE alt='img.vi' src='../wfgencreate_resources_dram_u128.gif']

Instantiates the internal memory, FIFOs, and other resources that the Waveform Generation FPGA library uses and bundles them with the external resource that you specify. 

Wire the **generation resources** output of this VI to the other Waveform Generation FPGA VIs that are used with this generation library instance in your FPGA application.

This polymorphic VI contains the following instance VIs:

- Create Resources DRAM U128
- Create Resources DRAM U256
- Create Resources DRAM U512

**Input Parameters**

**memory clock** specifies the clock domain used in the low-level read and write operations to DRAM. Use a faster clock to get better memory throughput and a slower clock to help the FPGA compilation meet timing constraints. The ideal clock rate for maximum throughput is the native DRAM clock rate of the FPGA target. The frequency of this clock can vary across different types of FPGA targets. Refer to the help file for the hardware that you use as the LabVIEW FPGA target for more information about the native DRAM clock rate.

**instance** specifies the instance number of this Waveform Generation FPGA library instantiation. The value that you specify for **instance** must be equal to the instance number that you specify in the **Open Session** VI of the Waveform Generation host library.

**memory** specifies the LabVIEW FPGA memory instantiated in the LabVIEW project that stores the waveforms downloaded from the host. This memory must use DRAM for its implementation. DRAM is instantiated in the LabVIEW project. The data type of this memory must match the type specified by the instance of the VI you are using.

**memory size (bytes)** specifies the size in bytes of the memory specified by **memory**.

**data write dma fifo resource** specifies the DMA FIFO resource that the host uses to download waveforms and instructions. The DMA FIFO resource is created by the **Create Data Write DMA FIFO Resources** VI of this library.

**Output Parameters**

**generation resources** returns the internal resources and resources that you specify that this instance of the Waveform Generation FPGA library uses. Wire this parameter to other Waveform Generation VIs that you use with this instance of the Waveform Generation library.

**generation subsystem** returns the resources used by the Waveform Generation FPGA Library to communicate with the host. Connect this wire to the Instruction Framework library using the **Add Subsystem** VI.

#### Process.vi

[IMAGE alt='img.vi' src='../wfgenprocess.gif']

Contains the free-running process of the Waveform Generation FPGA library. This process implements the various state machines and services needed to provide the core Waveform Generation functionality. This VI also implements interaction with DRAM memory. 


At least one instance of this VI must be present in your FPGA design for each instance of the Waveform Generation FPGA library.

**Input Parameters**

**generation resources** specifies the resources that the current instance of the library uses. You can obtain this value from the **Create Resources** VI of this library.

#### Retrieve Waveform Samples.vi

[IMAGE alt='img.vi' src='../wfgenretrieve_waveform_samples_i16.gif']

Generates waveform samples as specified by the selected script. This VI creates markers, provides generation status and events, and detects triggers. This VI implements the waveform generation functionality of this library.

When you call the **Start Generation** VI of the Waveform Generation host library, this VI starts processing instructions based on the **script name** input of the **Select Active Script** VI of the Waveform Generation host library. This VI produces the first sample of the sequence based on the detection of the Start Trigger, the priming condition specified in the **Set Priming Depth** VI of the Waveform Generation host library, and if the **ready for output** parameter of the **Retrieve Waveform Samples** VI is True.

This polymorphic VI contains the following instance VI:

- Retrieve Waveform Samples U32

**Input Parameters**

**output array size** specifies the size of the array for the **data array** output.

**generation resources** specifies the resources that the current instance of the library uses. You can obtain this value from the **Create Resources** VI of the Waveform Generation FPGA library.

**triggers** provides the Start Trigger or other general purpose triggers that a waveform script, which is defined in the Waveform Generation host library, can specify as a triggering condition.
 

 

This VI latches detected triggers even when there is no trigger evaluation. You can use this functionality to act upon triggers that occurred in the past prior to the trigger evaluation. If you want to ignore past triggers, specify clear trigger N, where *N* is the trigger number within the script, to clear the internal trigger latch prior to the beginning of the trigger evaluation.

**triggers.start trigger** provides the Start Trigger which is necessary to start generating sequences.

**triggers.trigger 1** provides trigger 1.

**triggers.trigger 2** provides trigger 2.

**triggers.trigger 3** provides trigger 3.

**triggers.trigger 4** provides trigger 4.

**triggers.trigger 5** provides trigger 5.

**triggers.trigger 6** provides trigger 6.

**triggers.trigger 7** provides trigger 7.

**ready for output** specifies whether the downstream nodes are ready for this VI to return a new value. The default is True.

**Output Parameters**

**retrieve data info** returns information related to the **data array** output.

**retrieve data info.valid data size** returns the number of samples within **data array** out that are valid.

**data array** returns the generated data. The size of the data array matches the number you specify in **output array size**. The first N samples of data are valid, where *N* is equal to the value of the **retrieve data info.valid data size** input.

**generation status** returns the current status of the generation state machine.

**generation status.idle** returns whether the generation state machine is currently idle. If you do not initiate a generation, the generation is idle.

**generation status.generation in progress** returns that the waveform generation engine received the Start Trigger and is generating waveform sequences.

**generation status.read underflow** returns whether the Retrieve Waveform Samples VI was unable to provide waveform samples. **Read underflow** returns True if this VI was unable to provide waveform samples during a sequence generation when the downstream nodes were ready to accept new data by asserting the **ready for output** parameter to True. After **read underflow** is set to True, it will be set to False only if a new generation is started or the library is reset.
 

 

The **Check Generation Status** VI of the Waveform Generation host library automatically returns an error if the **read underflow** parameter is set to True.

**events** reports various events that occur during the generation. Use these events to synchronize external logic with the state of the generation.

**events.ready for start trigger** returns whether the Waveform Generation FPGA library is ready to receive the Start Trigger.

**events.done** returns whether the generation sequences have ended. This event occurs after the generation ends successfully. This event also occurs when the **Abort Generation** VI or the **Reset** VI of the Waveform Generation host library is called during the generation.

**events.start trigger** returns whether the Start Trigger is recognized by the Waveform Generation FPGA library.

**events.started** returns whether the generation sequences start in the next clock cycle.

**output valid** returns whether **data array** and **marker bit field** are valid.

**marker bit field** returns marker information associated with the waveform generation. 
 

 

Markers are specified in a script written using **Write Script** VI of the Waveform Generation host library. A marker is an event that the **Retrieve Waveform Samples** VI generates in relation to a generated waveform. The event is configured to occur when a specific sample is produced by this VI. The specific sample is set using the keyword marker placed after the string generate waveform_name within a script, where *waveform_name* is the name of the waveform. For example, the string generate wfm0 marker0(10) within a script sets the 1st marker bit high when generating the 11th sample of the waveform wfm0.
 

 

**Marker bit field** returns High for the waveform sample bit with an associated marker and Low for all other waveform samples.
 

 

The size of the marker bit field array is equivalent to the value you specify for **output array size**. The marker bit field at the Nth index is associated with the data at the Nth index in **data array**.
 

 

The value returned by **marker bit field** is valid only when **output valid** is set to True.
 

 

You can use **marker bit field** to encode up to eight independent markers. You define the encoding of **marker bit field**. For example, you can use bit 0 to indicate the beginning of a generation, and bit 1 to drive an external digital line.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen_host.html language=enus -->
## TOPIC 00061: Waveform Generation Host VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen_host.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen_host.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Waveform Generation Host VIs

#### Abort Generation.vi

[IMAGE alt='img.vi' src='../abort_generation.gif']

Stops waveform generation.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Allocate Waveform.vi

[IMAGE alt='img.vi' src='../allocate_waveform.gif']

Allocates onboard memory space for the arbitrary waveform. Use this VI to specify the total size of a waveform before writing the data. Use this VI if you are calling the Write Waveform VI of this library multiple times to write a large waveform in smaller blocks.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**waveform name** specifies the name used this VI uses to store the waveform. This string is case-insensitive and alphanumeric.

**waveform size (samples)** specifies the size of the waveform to allocate, in samples. Each I/Q pair is considered one sample.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Check Generation Status.vi

[IMAGE alt='img.vi' src='../check_generation_status.gif']

Checks the status of the waveform generation. Use this VI to check for any errors that may occur during signal generation or to check whether the device has completed generation.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**done** indicates whether the waveform generation is complete.

**error out** contains error information. This output provides standard error out functionality.

#### Clear All Waveforms.vi

[IMAGE alt='img.vi' src='../clear_all_waveforms.gif']

Deletes all currently defined waveforms.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Clear Sequence.vi

[IMAGE alt='img.vi' src='../clear_sequence.gif']

Clears the sequence used to control waveform generation.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**sequence name** specifies the name this VI uses to store the sequence. This string is case-insensitive and alphanumeric.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Clear Waveform.vi

[IMAGE alt='img.vi' src='../clear_waveform.gif']

Deletes a specified waveform from the pool of waveforms that are currently defined.

If you call the Start Generation VI or the Select Active Script VI of this library immediately after calling the Clear Waveform VI, the Start Generation VI and the Select Active Script VI do not return errors because these VIs do not validate the selected sequence against existing waveforms.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**waveform name** specifies the name of the waveform this VI deletes. This string is case-insensitive and alphanumeric.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Close Session.vi

[IMAGE alt='img.vi' src='../close_session.gif']

Destroys the session to this library.

If you call this VI when a waveform generation is in progress, this VI does not abort the waveform generation.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**error out** contains error information. This output provides standard error out functionality.

#### Get Waveform Memory Size.vi

[IMAGE alt='img.vi' src='../get_waveform_memory_size.gif']

Returns the waveform memory size in samples.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**waveform memory size (samples)** passes the waveform memory size in samples.

**error out** contains error information. This output provides standard error out functionality.

#### Open Session.vi

[IMAGE alt='img.vi' src='../open_session.gif']

Opens a session to the instance of the Waveform Generation library on the device that is connected to the instance of **register bus session in**. Use **session out** to identify the Waveform Generation library in all subsequent Waveform Generation VIs.

**Input Parameters**

**register bus** specifies a reference to the Register Bus session, which identifies the instance of the Register Bus library to which this instance of the Waveform Generation library is connected in the FPGA.

**parent context** specifies the parent context under which the Waveform Generation FPGA library is located. When the Waveform Generation FPGA library is a child of a library, the parent library should obtain its context from the **Subsystem Lookup** VI in the Instruction Framework host library and pass its context to this parameter.

**fpga interface** specifies the reference to the FPGA interface.

**subsystem map** specifies the reference to the subsystem map. This reference is provided by calling the Read Subsystem Map VI from the Instruction Framework host library.

**instance** specifies the instance number of the Waveform Generation FPGA library for which to open a session. This value must match the value of **instance** of the **Create Resources** VI in the Waveform Generation FPGA library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Reset.vi

[IMAGE alt='img.vi' src='../reset.gif']

Resets the host and FPGA Waveform Generation libraries.

This VI clears all waveforms and sequences and aborts any active generation on the device.

**Note:** This VI does not change the current settings for the **Set Memory Read Grant Time**, **Set Memory Write Grant Time**, **Set Download FIFO Depth**, or **Set Priming Depth** VIs.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Select Active Script.vi

[IMAGE alt='img.vi' src='../select_active_script.gif']

Specifies the script to generate upon calling the **Start Generation** VI of this library and writes it to the device.

If you clear or resize waveforms referenced by **script name** after calling the **Write Script** VI, the sequence written to the device may become out of date and produce unexpected results. Call the **Write Script** VI again to prevent the sequence from becoming out of date.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**script name** specifies the script to write to the device, which is generated when the **Start Generation** VI of this library is called.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Set Download FIFO Depth.vi

[IMAGE alt='img.vi' src='../set_download_fifo_depth.gif']

Sets the size of the host DMA buffer for the host-to-target FIFO that downloads waveforms and sequences. When you call the **Open Session** VI of this library, the **Open Session** VI sets the depth of the download FIFO to a reasonable value and stores that value in the session. When you call this VI, it configures the FIFO to a new FIFO depth and the new value is stored in the session.

**Note:** Use this VI only in applications where the default settings are not appropriate, such as applications where the write waveform performance is very important. For such applications, consider using the **Set Memory Write Grant Time** VI in addition to or instead of using this VI.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**fifo depth (bytes)** specifies the number of elements of host memory to allocate for the DMA FIFO that writes waveforms and sequences to the device.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Set Memory Read Grant Time.vi

[IMAGE alt='img.vi' src='../set_memory_read_grant_time.gif']

Configures the read grant time setting of the time-slice arbiter that controls DRAM access on the device.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**mem read grant time (clocks)** specifies the number of back-to-back clock cycles to allocate for memory read operations. These are clock cycles of the **memory clock** input of the **Create Resources** VI of the Waveform Generation FPGA instance of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Set Memory Write Grant Time.vi

[IMAGE alt='img.vi' src='../set_memory_write_grant_time.gif']

Configures the write grant time setting of the time-slice arbiter that controls DRAM access on the device.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**mem write grant time (clocks)** specifies the number of back-to-back clock cycles to allocate for memory write operations. These are clock cycles of the **memory clock** input of the **Create Resources** VI of the Waveform Generation FPGA instance of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Set Priming Depth.vi

[IMAGE alt='img.vi' src='../set_priming_depth.gif']

Configures the number of samples that must be available to the **Retrieve Waveform Samples** VI on the FPGA before the first sample is returned.

Set **priming depth (samples)** to a larger value if you detect generation underflows, or to a smaller value if you want to reduce the first sample to output latency. The **Open Session** VI of this library sets this value to *200*(memory word bit width/bits per sample)*, which is appropriate for most applications.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**priming depth (samples)** specifies the number of samples that must be available to the **Retrieve Waveform Samples** VI on the FPGA before the first sample of the sequence is returned.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Set Selected Sequence.vi

[IMAGE alt='img.vi' src='../set_selected_sequence.gif']

Sets the specified sequence to control waveform generation.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**selected sequence** specifies the sequence to set.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Set Waveform Next Write Position.vi

[IMAGE alt='img.vi' src='../set_waveform_next_write_position.gif']

Configures the starting position to use for writing a waveform with the next call to the **Write Waveform** VI.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**waveform name** specifies the name this VI uses to store the waveform. This string is case-insensitive and alphanumeric.

**offset** specifies the offset (positive or negative) to move the write pointer relative to the position you specify in the **relative to**input.

**relative to (1:current)** specifies the location in the waveform that the **write offset** input is based on.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Start Generation.vi

[IMAGE alt='img.vi' src='../start_generation.gif']

Starts the waveform generation based on the sequence specified using the **Select Active Script** VI or **Set Selected Sequence** VI of this library.

This VI checks whether the total number of samples to generate in the selected sequence is greater than the priming depth. If the number of samples to generate in the sequence is less than the priming depth, this VI sets the priming depth to the number of samples to generate in order to ensure generation.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Write Script.vi

[IMAGE alt='img.vi' src='../write_script.gif']

Creates one or more sequences to control waveform generation based on the input script.

This VI creates one or more sequences from a user provided script. Call the **Set Active Script** VI of this library before you start the generation to specify which script you want the Waveform Generation FPGA library to generate.

Refer to the [**Retrieve Waveform Samples** VI](idl_wvfrmgen.html) of the Waveform Generation FPGA library for more information about the way different parameters of a sequence element define the behavior of the **Retrieve Waveform Samples** VI on the FPGA.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**waveform script** specifies a script.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Write Sequence (Nested Loops).vi

[IMAGE alt='img.vi' src='../write_sequence_nested_loops.gif']

Creates a sequence to control waveform generation.

This VI creates a sequence from an array of **sequence data** clusters, each of which defines a generation loop. This generation loop is referred to as a subsequence. Call the **Set Selected Sequence** VI of this library before you start the generation to specify which sequence you want the Waveform Generation FPGA library to generate.

Refer to the [**Retrieve Waveform Samples** VI](idl_wvfrmgen.html) of the Waveform Generation FPGA library for more information about the way different parameters of a sequence element define the behavior of that VI on the FPGA.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**sequence name** specifies the name this VI uses to store the sequence. This string is case-insensitive and alphanumeric.

**sequence data** specifies an array of clusters that defines the generation of multiple subsequences. Each subsequence specifies a generation of multiple waveforms. Each cluster contains the following elements:

**sequence data.loop type** specifies the type of looping for this subsequence.

**Finite** - The subsequence executes the number of times specified by the **loop count** element of this cluster.

**Forever** - The subsequence repeats until the generation is aborted.

**Until Trigger** - The subsequence repeats until the trigger specified in **repeat until trigger** is detected.

**sequence data.loop count** specifies the number of times to generate this subsequence when **loop type** is set to Finite.

**sequence data.repeat until trigger** specifies the trigger that must be detected to end the loop when **loop type** is set to Until Trigger.

**sequence data.clear trigger bit field** specifies the trigger or triggers that must be ignored if they are detected prior to the starting of this subsequence.

**sequence data.sequence array** specifies the waveforms to generate for this generation subsequence, along with their generation characteristics.

**sequence data.sequence array.wfm name** specifies the name of the waveform to generate.

**sequence data.sequence array.wait for trigger** specifies the trigger for which the subsequence must wait before generating the waveform.

**None** - The subsequence does not wait for any triggers.

**Start Trigger** - Not Supported.

**Trigger *x*** - The subsequence waits for Trigger *x* to be detected before generating the waveform, where *x* is a trigger number <0..7>.

**sequence data.sequence array.marker position** specifies the sample position in the waveform where the marker is generated.

**sequence data.sequence array.marker bit field** specifies the bit field associated with the marker. A value of zero is equivalent to no marker. You can use different bits to define different logical markers.

**sequence data.sequence array.start position** specifies the first sample of the waveform to generate.

**sequence data.sequence array.length (-1 = all)** specifies the total number of samples to generate for the waveform. A value of -1 specifies to generate all samples of the waveform. If **ignore data** is TRUE, l**ength (-1 = all)** must be greater than or equal to 1.

**sequence data.sequence array.ignore data** specifies whether the R**etrieve Waveform Samples** VI in the Waveform Generation FPGA library discards the number of samples specified by this sequence element in **length (-1 = all)**. For each of the discarded samples, the **data ignored** output of the **Retrieve Waveform Samples** VI returns a value of TRUE. The value specified for **wfm name** is ignored when this parameter is set to TRUE. You can use this parameter in combination with a custom value for **marker bit field** to control circuitry in the FPGA when waveform data should not be generated.

**sequence data.sequence array.clear trigger bit field** specifies the triggers to clear when the generation of this sequence element starts.

**repeat forever** specifies whether the specified **sequence data** repeats continuously until you abort the generation by calling the **Abort Generation** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

#### Write Sequence.vi

[IMAGE alt='img.vi' src='../write_sequence.gif']

Creates a sequence to control waveform generation.

This VI creates a sequence from an array of **sequence data** clusters, each of which defines a generation loop. This generation loop is referred to as a subsequence. Call the **Set Selected Sequence** VI of this library before you start the generation to specify which sequence you want the Waveform Generation FPGA library to generate.

Refer to the [**Retrieve Waveform Samples** VI](idl_wvfrmgen.html) of the Waveform Generation FPGA library for more information about the way different parameters of a sequence element define the behavior of that VI on the FPGA.

**Input Parameters**

**session in** identifies your session. This input is obtained from the **Open Session** VI of this library.

**sequence name** specifies the name this VI uses to store the sequence. This string is case-insensitive and alphanumeric.

**sequence data** specifies an array of clusters that defines the generation of multiple subsequences. Each subsequence specifies a generation of multiple waveforms. Each cluster contains the following elements:

**sequence data.loop type** specifies the type of looping for this subsequence.

**Finite** - The subsequence executes the number of times specified by the **loop count** element of this cluster.

**Forever** - The subsequence repeats until the generation is aborted.

**Until Trigger** - The subsequence repeats until the trigger specified in **repeat until trigger** is detected.

**sequence data.loop count** specifies the number of times to generate this subsequence when **loop type** is set to Finite.

**sequence data.repeat until trigger** specifies the trigger that must be detected to end the loop when **loop type** is set to Until Trigger.

**sequence data.clear trigger bit field** specifies the trigger or triggers that must be ignored if they are detected prior to the starting of this subsequence.

**sequence data.sequence array** specifies the waveforms to generate for this generation subsequence, along with their generation characteristics.

**sequence data.sequence array.wfm name** specifies the name of the waveform to generate.

**sequence data.sequence array.wait for trigger** specifies the trigger for which the subsequence must wait before generating the waveform.

**None** - The subsequence does not wait for any triggers.

**Start Trigger** - Not Supported.

**Trigger *x*** - The subsequence waits for Trigger *x* to be detected before generating the waveform, where *x* is a trigger number <0..7>.

**sequence data.sequence array.marker position** specifies the sample position in the waveform where the marker is generated.

**sequence data.sequence array.marker bit field** specifies the bit field associated with the marker. A value of zero is equivalent to no marker. You can use different bits to define different logical markers.

**sequence data.sequence array.start position** specifies the first sample of the waveform to generate.

**sequence data.sequence array.length (-1 = all)** specifies the total number of samples to generate for the waveform. A value of -1 specifies to generate all samples of the waveform. If **ignore data** is TRUE, l**ength (-1 = all)** must be greater than or equal to 1.

**sequence data.sequence array.ignore data** specifies whether the R**etrieve Waveform Samples** VI in the Waveform Generation FPGA library discards the number of samples specified by this sequence element in **length (-1 = all)**. For each of the discarded samples, the **data ignored** output of the **Retrieve Waveform Samples** VI returns a value of TRUE. The value specified for **wfm name** is ignored when this parameter is set to TRUE. You can use this parameter in combination with a custom value for **marker bit field** to control circuitry in the FPGA when waveform data should not be generated.

**sequence data.sequence array.clear trigger bit field** specifies the triggers to clear when the generation of this sequence element starts.

**repeat forever** specifies whether the specified **sequence data** repeats continuously until you abort the generation by calling the **Abort Generation** VI of this library.

**error in** describes error conditions that occur before this node runs. This input provides standard error in functionality.

**Output Parameters**

**session out** passes a reference to your session to the next VI.

**error out** contains error information. This output provides standard error out functionality.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen_ll.html language=enus -->
## TOPIC 00062: Waveform Generation Low-Level VIs

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen_ll.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/idl_wvfrmgen_ll.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Waveform Generation Low-Level VIs

#### Set Input FIFO.vi

[IMAGE alt='img.vi' src='../wfgenset_input_fifo_u6.gif']

Specifies the FIFO used to write waveform data to memory. This FIFO accepts waveform data after the target receives waveform data from the host through the data write DMA FIFO and transfers the waveform data to the memory clock domain.

You must select an instance of this polymorphic VI whose data type matches the memory width of the **Create Resources** VI of this library. For example, if you choose to use the **Create Resources** VI with a memory width of U128, you must also select the U128 instance of this polymorphic VI.

This polymorphic VI contains the following instance VIs:

- Set Input FIFO U64 Wrapper
- Set Input FIFO U128 Wrapper
- Set Input FIFO U256 Wrapper
- Set Input FIFO U512 Wrapper
- Set Input FIFO U768 Wrapper

**Input Parameters**

**generation resources in** specifies the resources that the current instance of the library uses. You can obtain this value from the **Create Resources** VI of this library.

**Output Parameters**

**generation resources out** indicates the resources that the current instance of the library uses. Wire this output to other Waveform Generation FPGA library VIs to pass the resource information.

#### Set Retrieve FIFO.vi

[IMAGE alt='img.vi' src='../wfgenset_retrieve_fifo.gif']

Specifies the FIFO used to retrieve waveform data from memory. This FIFO accepts samples read directly from the memory and transfers them to the clock domain to retrieve sample data using the **Retrieve Waveform Samples** VI of this library.

You must select an instance of this polymorphic VI whose data type matches the memory width of the **Create Resources** VI of this library. For example, if you choose to use the **Create Resources** VI with a memory width of U128, you must also select the U128 instance of this polymorphic VI.

This polymorphic VI contains the following instance VIs:

- Set Retrieve FIFO U64 Wrapper
- Set Retrieve FIFO U128 Wrapper
- Set Retrieve FIFO U256 Wrapper
- Set Retrieve FIFO U384 Wrapper
- Set Retrieve FIFO U512 Wrapper
- Set Retrieve FIFO U768 Wrapper

**Input Parameters**

**generation resources in** specifies the resources that the current instance of the library uses. You can obtain this value from the **Create Resources** VI of this library.

**size (elements)** specifies the size of sequence memory, in elements. The value of this input must be equal to the number of elements of the sequence memory resource.

**Output Parameters**

**generation resources out** indicates the resources that the current instance of the library uses. Wire this output to other Waveform Generation FPGA library VIs to pass the resource information.

#### Set Request FIFO.vi

[IMAGE alt='img.vi' src='../wfgenset_request_fifo.gif']

Specifies the FIFO used to request waveform data from memory. This FIFO accepts address values from the clock domain to retrieve sample data and transfers them to the **Process** VI of this library to pass the requests to memory.

**Input Parameters**

**generation resources in** specifies the resources that the current instance of the library uses. You can obtain this value from the **Create Resources** VI of this library.

**Output Parameters**

**generation resources out** indicates the resources that the current instance of the library uses. Wire this output to other Waveform Generation FPGA library VIs to pass the resource information.

#### Set Sequence Memory.vi

[IMAGE alt='img.vi' src='../wfgenset_sequence_memory.gif']

Specifies the block memory resource used to store generation sequences. This memory stores generation sequences that are downloaded from the host. Use this VI if your script is too long to fit into the default block memory resource that has a capacity of 6,144 instructions. You can also use this VI to reduce the resource utilization by specifying fewer than 6,144 elements for the block memory resource.

**Input Parameters**

**generation resources in** specifies the resources that the current instance of the library uses. You can obtain this value from the Create Resources VI of this library.

**memory size (elements)** specifies the size of sequence memory, in elements. The value of this input must be equal to the number of elements of the sequence memory resource.

**Input Parameters**

**generation resources out** indicates the resources that the current instance of the library uses. Wire this output to other Waveform Generation FPGA library VIs to pass the resource information.

#### Set MetaData FIFO.vi

[IMAGE alt='img.vi' src='../wfgenset_metadata_fifo.gif']

Specifies the FIFO used to transfer metadata internally.

**Input Parameters**

**generation resources in** specifies the resources that the current instance of the library uses. You can obtain this value from the **Create Resources** VI of this library.

**Output Parameters**

**generation resources out** indicates the resources that the current instance of the library uses. Wire this output to other Waveform Generation FPGA library VIs to pass the resource information.

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/pulse_expander.html language=enus -->
## TOPIC 00063: Pulse Expander

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/pulse_expander.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/pulse_expander.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Pulse Expander

Expands a pulse to respect a specified minimum pulse length.

[IMAGE alt='Pulse Expander' src='../flexrio_api_fpga_v1_lvlib_pulse_expanderc.gif']

|  | min pulse length specifies a minimum pulse length. |
| --- | --- |
|  | input pulse specifies the pulse to expand. |
|  | expanded pulse returns the pulse that results from expanding input pulse to respect the specified min pulse length. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/qsfppalette.html language=enus -->
## TOPIC 00064: QSFP Palette Overview

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/qsfppalette.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/qsfppalette.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

QSFP Palette Overview

Use the QSFP VIs to control and communicate with QSFP modules at the ports.

| Palette Object | Description |
| --- | --- |
| Write QSFP | Writes values to the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification. |
| Read QSFP | Returns values for the QSFP+ module connected at the specified port. For address and data information, refer to the SFF-8636 specification. |
| Reset QSFP Ports | Resets the QSFP+ modules connected to all ports. |
| Enable QSFP Low Power Mode | Enables low power mode for the QSFP+ modules connected to all ports. True enables low power mode. False enables high power mode. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/resetdspsynchronous.html language=enus -->
## TOPIC 00065: Reset DSP Synchronously (VI)

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/resetdspsynchronous.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/resetdspsynchronous.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Reset DSP Synchronously (VI)

Asserts DSP Reset on the same rising edge of TClk across all sessions. Use this function to synchronously assert a DSP Reset on multiple TClk synchronized boards on a common rising edge of TClk. This assumes that all boards have already been synchronized via a call to niTClk_Synchronize. Use this function in combination with the TClk Synchronized DSP Reset FPGA VI.

[IMAGE alt='reset_dsp_synchronous' src='../dsp_synchronous.gif']

|  | fpga interfaces in specifies the reference to the VI on the FPGA interface palette. |
| --- | --- |
|  | instance |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fpga interfaces out returns a reference to the VI on the FPGA interface palette. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/resetqsfpports.html language=enus -->
## TOPIC 00066: Reset QSFP Ports (VI)

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/resetqsfpports.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/resetqsfpports.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Reset QSFP Ports (VI)

Resets the QSFP+ modules connected to all ports.

[IMAGE alt='reset_qsfp' src='../reset_qsfp.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA interface palette. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fpga interface out returns a reference to the VI on the FPGA interface palette. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/start_cablesense.html language=enus -->
## TOPIC 00067: Start CableSense Signal(VI)

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/start_cablesense.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/start_cablesense.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Start CableSense Signal (VI)

Generates the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module, as configured by the CableSense Mode property.

[IMAGE alt='start_cablesense' src='../start_cablesense.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA interface palette. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fpga interface out returns a reference to the VI on the FPGA interface palette. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/start_trigger.html language=enus -->
## TOPIC 00068: Start Trigger

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/start_trigger.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/start_trigger.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Start Trigger

Conditions a start trigger to enable inter-device routing and TClk functionality.

[IMAGE alt='Start Trigger' src='../flexrio_api_fpga_v1_lvlib_start_triggerc.gif']

|  | dio for start export specifies the DIO for exporting the start trigger signal. |
| --- | --- |
|  | dio start specifies the DIO start trigger signal source. |
|  | flexrio.trigger.start.cfg 0 specifies start trigger configuration information. |
|  | analog trigger implements an analog start trigger. |
|  | user-defined start trigger implements a user-defined start trigger. |
|  | ready for start? specifies whether the downstream node is ready to receive the start trigger. |
|  | start trigger control contains the start trigger control information. arm start specifies whether to arm the start trigger. done specifies whether the stream is in a non-running state. |
|  | arm start specifies whether to arm the start trigger. |
|  | done specifies whether the stream is in a non-running state. |
|  | conditioned start trigger outputs the trigger signal conditioned for TClk and inter-device routing. |
|  | unconditioned start trigger outputs the unconditioned start trigger. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/stop_cablesense.html language=enus -->
## TOPIC 00069: Stop CableSense Signal(VI)

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/stop_cablesense.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/stop_cablesense.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Stop CableSense Signal (VI)

Disables the CableSense signal on all channels for which the signal is enabled on your compatible FlexRIO module.

[IMAGE alt='start_cablesense' src='../stop_cablesense.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA interface palette. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. |
|  | fpga interface out returns a reference to the VI on the FPGA interface palette. |
|  | error out contains error information. This output provides standard error out functionality. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/stream.html language=enus -->
## TOPIC 00070: FlexRIO Stream Palette Overview

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/stream.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/stream.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

FlexRIO Stream Palette Overview

Use the Stream VIs to configure streaming properties such as enabled channels and the number of samples to transfer.

| Palette Object | Description |
| --- | --- |
| Clear Stream | Clears samples from the stream. |
| Configure Stream Finite | Configures a stream to operate in a finite transfer bound by a specified number of samples. |
| Configure Stream Enabled Channels | Specifies which channels are enabled for the streaming session. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viclose.html language=enus -->
## TOPIC 00071: Close

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viclose.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viclose.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Close

Closes the streaming session, destroys the session reference, and deallocates resources associated with that session. Call this VI once for each unique named session that you have created.

[IMAGE alt='Close' src='../ni_flexrio_api_v1_lvlib_closec.png']

|  | FPGA VI Reference In specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viconfigureclock.html language=enus -->
## TOPIC 00072: Configure Clock

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viconfigureclock.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viconfigureclock.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Configure Clock

Configures the Reference Clock and external Sample Clock.

#### Configure Reference Clock

Configures the Reference Clock source. You can use this VI to set the onboard clock, the PXI backplane clock, or an external clock as the reference clock.

[IMAGE alt='Configure Reference Clock' src='../ni_flexrio_api_v1_lvlib_configure_reference_clockc.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | reference clock source specifies the Reference Clock source. Defined Values Default (0)The internal Sample Clock locks to the default Reference Clock. Onboard (1)The internal Sample Clock locks to an onboard voltage-controlled temperature compensated crystal oscillator (VCTCXO). PXI_Clk10 (2)The internal Sample Clock locks to the PXI 10 MHz Reference Clock, which is provided through the backplane. External (3)The internal Sample Clock locks to an external Reference Clock, which is provided through the CLK/REF IN front panel connector |
| Default (0) | The internal Sample Clock locks to the default Reference Clock. |
| Onboard (1) | The internal Sample Clock locks to an onboard voltage-controlled temperature compensated crystal oscillator (VCTCXO). |
| PXI_Clk10 (2) | The internal Sample Clock locks to the PXI 10 MHz Reference Clock, which is provided through the backplane. |
| External (3) | The internal Sample Clock locks to an external Reference Clock, which is provided through the CLK/REF IN front panel connector |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Configure External Clock

Configures external Sample Clock source and frequency.

[IMAGE alt='Configure External Clock' src='../ni_flexrio_api_v1_lvlib_configure_external_clockc.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | clock source identifies the source of the external Sample Clock. |
|  | frequency specifies the frequency of the external Sample Clock. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viconfigurestarttrigger.html language=enus -->
## TOPIC 00073: Configure Start Trigger

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viconfigurestarttrigger.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viconfigurestarttrigger.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Configure Start Trigger

Configures the start trigger type and conditions.

#### Configure Immediate Start Trigger

Configures the device to trigger itself immediately and independently of external signals.

[IMAGE alt='Configure Immediate Start Trigger' src='../ni_flexrio_api_v1_lvlib_configure_immediate_start_triggerc.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | trigger instance specifies an instance of a trigger. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | trigger instance out specifies an instance of a trigger. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Configure Analog Start Trigger

Configures the device to trigger on the rising or falling edge of an analog signal.

[IMAGE alt='Configure Analog Start Trigger' src='../ni_flexrio_api_v1_lvlib_configure_analog_start_triggerc.gif']

|  | rising edge? specifies whether to trigger on a rising edge. If this value is FALSE, this VI configures the device to trigger on a falling edge. |
| --- | --- |
|  | hysteresis specifies the size of the hysteresis window on either side of level in volts. |
|  | level specifies the trigger level in volts. |
|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
|  | trigger instance specifies an instance of a trigger. |
|  | channel specifies the channel to monitor for trigger conditions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | trigger instance out specifies an instance of a trigger. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Configure Digital Edge Start Trigger

Configures the device to trigger on the rising or falling edge of a digital signal.

[IMAGE alt='Configure Digital Edge Start Trigger' src='../ni_flexrio_api_v1_lvlib_configure_digital_edge_start_triggerc.gif']

|  | rising edge? specifies whether to trigger on a rising edge. If this value is FALSE, this VI configures the device to trigger on a falling edge. |
| --- | --- |
|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
|  | trigger instance specifies an instance of a trigger. |
|  | trigger source specifies the source of the signal to monitor for trigger conditions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | trigger instance out specifies an instance of a trigger. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

#### Configure Digital Level Start Trigger

Configures the device to trigger on the high or low level of a digital signal.

[IMAGE alt='Configure Digital Level Start Trigger' src='../ni_flexrio_api_v1_lvlib_configure_digital_level_start_triggerc.gif']

|  | high level? specifies whether to trigger on a high level. Set this value to FALSE to trigger on a low level. |
| --- | --- |
|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
|  | trigger instance specifies an instance of a trigger. |
|  | trigger source specifies the source of the signal to monitor for trigger conditions. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | trigger instance out specifies an instance of a trigger. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viconfigurestream.html language=enus -->
## TOPIC 00074: Configure Stream

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viconfigurestream.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viconfigurestream.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Configure Stream

Configures enabled channels and number of samples in the stream.

[IMAGE alt='Configure Stream' src='../ni_flexrio_api_v1_lvlib_configure_streamc.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | stream instance specifies an instance of a stream. |
|  | channels enabled identifies channels enabled in the streaming session. Syntax DescriptionExample Single channelAI0 List of channelsAI0,AI2 Range of channelsAI0-AI2 |
| Description | Example |
| Single channel | AI0 |
| List of channels | AI0,AI2 |
| Range of channels | AI0-AI2 |
|  | num samples specifies the maximum number of samples to transfer. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | stream instance out returns a copy of stream instance. |
|  | channel count indicates the total number of channels parsed. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viconfigurestreamenabledchannels.html language=enus -->
## TOPIC 00075: Configure Stream Enabled Channels

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viconfigurestreamenabledchannels.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viconfigurestreamenabledchannels.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Configure Stream Enabled Channels

Specifies which channels are enabled for the streaming session.

[IMAGE alt='Configure Stream Enabled Channels' src='../ni_flexrio_api_v1_lvlib_configure_stream_enabled_channelsc.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | stream instance identifies an instance of a stream. |
|  | channels enabled identifies channels enabled in the streaming session. Syntax DescriptionExample Single channelAI0 List of channelsAI0,AI2 Range of channelsAI0-AI2 |
| Description | Example |
| Single channel | AI0 |
| List of channels | AI0,AI2 |
| Range of channels | AI0-AI2 |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | copy of stream instance returns a copy of stream number. |
|  | channel count indicates the total number of channels enabled. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viupdateverificationinformation.html language=enus -->
## TOPIC 00076: Update Verification Information

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viupdateverificationinformation.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viupdateverificationinformation.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Update Verification Information

Updates verification time and verification temperature fields in the device's flash memory to current system time and device temperature, respectively. Use the FlexRIO API Property Node to read the values of these fields.

[IMAGE alt='Update Verification Information' src='../ni_flexrio_api_v1_lvlib_update_verification_informationc.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |

<!--NI_TOPIC bundle=flexrio-api-ref path=flexrio-api-ref/flexriointegratedmerge/viwritecalibrationdata.html language=enus -->
## TOPIC 00077: Write Calibration Data

- bundle_id: `flexrio-api-ref`
- source_path: `flexrio-api-ref/flexriointegratedmerge/viwritecalibrationdata.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-api-ref/raw/resource/enus/flexrio-api-ref/flexriointegratedmerge/viwritecalibrationdata.html
- document_id: `flexrio-api-ref`
- page_type: `leaf`
- content_type: ``

Write Calibration Data

Writes calibration data to the FlexRIO device's on-board flash memory.

[IMAGE alt='Write Calibration Data' src='../ni_flexrio_api_v1_lvlib_write_calibration_datac.gif']

|  | fpga interface in specifies the reference to the VI on the FPGA Interface palette. |
| --- | --- |
|  | offset specifies the byte address in the device's flash memory at which to begin the operation. |
|  | data specifies the data to write to the device's flash memory. |
|  | error in describes error conditions that occur before this node runs. This input provides standard error in functionality. status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred before this VI or function ran or FALSE (checkmark) to indicate a warning or that no error occurred before this VI or function ran. The default is FALSE. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | fpga interface out returns a reference to the VI on the FPGA Interface palette. |
|  | error out contains error information. This output provides standard error out functionality. status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
|  | status is TRUE (X) if an error occurred or FALSE (checkmark) to indicate a warning or that no error occurred. |
|  | code is the error or warning code. The default is 0. If status is TRUE, code is a negative error code. If status is FALSE, code is 0 or a warning code. |
|  | source identifies where an error occurred. The source string includes the name of the VI that produced the error, what inputs are in error, and how to eliminate the error. |
