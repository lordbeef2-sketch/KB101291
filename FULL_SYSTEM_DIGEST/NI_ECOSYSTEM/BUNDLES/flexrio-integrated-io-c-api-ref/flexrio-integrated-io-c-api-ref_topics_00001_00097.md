# NI DOCUMENT BUNDLE: flexrio-integrated-io-c-api-ref

<!--NI_BUNDLE_CHUNK bundle=flexrio-integrated-io-c-api-ref start=1 end=97 -->
<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__attributes.html language=enus -->
## TOPIC 00001: NI FlexRIO C Attributes

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__attributes.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__attributes.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionFlexRIO_AttributeBoolFlexRIO_AttributeDoubleFlexRIO_AttributeInt32FlexRIO_AttributeStringFlexRIO_AttributeUInt64AttachmentsNone

### NI FlexRIO C Attributes

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| FlexRIO_AttributeBool |  |
| FlexRIO_AttributeDouble |  |
| FlexRIO_AttributeInt32 |  |
| FlexRIO_AttributeString |  |
| FlexRIO_AttributeUInt64 |  |

#### Attachments

None

Parent topic:

niflexrioapi.h

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__attributes_1ga4b7cdd030df23a66f72256f71aadba0b.html language=enus -->
## TOPIC 00002: FlexRIO_AttributeUInt64 Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__attributes_1ga4b7cdd030df23a66f72256f71aadba0b.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__attributes_1ga4b7cdd030df23a66f72256f71aadba0b.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_AttributeUInt64MembersNameValueDescriptionkFlexRIO_FirstUInt64Sentinel0x50000000kFlexRIO_StreamNumberOfSamples0x50000000Specifies the number of samples to transfer in a finite stream. kFlexRIO_StreamFifoSize0x50000001Specifies the number of samples allocated in each stream FIFO. S

### FlexRIO_AttributeUInt64 Enumeration

#### Syntax

enum FlexRIO_AttributeUInt64

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_FirstUInt64Sentinel | 0x50000000 |  |
| kFlexRIO_StreamNumberOfSamples | 0x50000000 | Specifies the number of samples to transfer in a finite stream. |
| kFlexRIO_StreamFifoSize | 0x50000001 | Specifies the number of samples allocated in each stream FIFO. Set this value to 0 to allow the driver to allocate the buffer according to its own heuristics. |
| kFlexRIO_StreamChannelsEnabled | 0x50000002 | Returns a bitmask indicating which channels will be transferred in this stream. |
| kFlexRIO_CalibrationDateTime | 0x50000003 | Indicates the time of the last write to calibration storage in seconds since 1904. |
| kFlexRIO_VerificationDateTime | 0x50000004 | Indicates the time of last verification in seconds since 1904. |
| kFlexRIO_CircularBufferSize | 0x50000006 | Specifies the capacity of the FPGA-side circular buffer. |
| kFlexRIO_CircularBufferElementsWritten | 0x50000007 | Specifies number of elements written into the FPGA's circular buffer. |
| kFlexRIO_LastUInt64Sentinel | 0x5000ffff |  |

Parent topic:

NI FlexRIO C Attributes

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__attributes_1ga8833142cd049045a8ec5214014445cc7.html language=enus -->
## TOPIC 00003: FlexRIO_AttributeInt32 Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__attributes_1ga8833142cd049045a8ec5214014445cc7.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__attributes_1ga8833142cd049045a8ec5214014445cc7.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_AttributeInt32MembersNameValueDescriptionkFlexRIO_FirstInt32Sentinel0x10000000kFlexRIO_ChannelsInStream0x10000000Specifies the number of channels available in the named stream. kFlexRIO_StreamDataFormat0x10000003kFlexRIO_AdcResolution0x10000005Indicates the number of bits of data

### FlexRIO_AttributeInt32 Enumeration

#### Syntax

enum FlexRIO_AttributeInt32

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_FirstInt32Sentinel | 0x10000000 |  |
| kFlexRIO_ChannelsInStream | 0x10000000 | Specifies the number of channels available in the named stream. |
| kFlexRIO_StreamDataFormat | 0x10000003 |  |
| kFlexRIO_AdcResolution | 0x10000005 | Indicates the number of bits of data returned to the FPGA diagram. |
| kFlexRIO_AdcSampleContainer | 0x10000006 | Indicates the number of bits used to represent data to the diagram. |
| kFlexRIO_TClkSessionReference | 0x10000007 | Internal TClk session reference memory |
| kFlexRIO_AnalogEdgeTriggerChannel | 0x10000008 | Specifies the channel to monitor for edge trigger conditions. |
| kFlexRIO_StartTriggerType | 0x10000009 | Specifies the trigger type. |
| kFlexRIO_ReferenceClockSource | 0x1000000b | Specifies the Reference Clock source. |
| kFlexRIO_CalibrationStorageSize | 0x1000000c | Indicates the size in bytes of available calibration storage. |
| kFlexRIO_IoError | 0x1000000d | Reports error codes when the I/O module enters an error state. |
| kFlexRIO_AiNyquistZone | 0x1000000e | Specifies the Nyquist Zone in which the input signal resides. |
| kFlexRIO_AiChannelCount | 0x1000000f | Indicates the number of analog input channels on the device. |
| kFlexRIO_AdcClockDivisor | 0x10000010 | Indicates the ratio between the sample clock timebase rate and the ADC sample clock. |
| kFlexRIO_AiCoupling | 0x10000011 | Specifies the coupling of the channel. |
| kFlexRIO_PhaseDacValue | 0x10000012 | Specifies the value of the clock phase digital-to-analog converter (DAC). |
| kFlexRIO_SampleClockSource | 0x10000013 | Specifies the Sample Clock source. |
| kFlexRIO_AiDecimationFilterBand | 0x10000014 | Specifies a highpass or lowpass filter response for the ADC decimation filter. |
| kFlexRIO_DataClockDivisor | 0x10000015 | Indicates the ratio between the Sample Clock timebase rate and the Data Clock. |
| kFlexRIO_StartTriggerSensitivity | 0x10000016 | Specifies the trigger sensitivity. |
| kFlexRIO_BaseboardReferenceClockSource | 0x10000018 | Specifies the source for the baseboard reference clock. |
| kFlexRIO_AdcInterleavingFactor | 0x10000019 | Specifies the number of ADC cores to interleave for time-interleaved sampling. |
| kFlexRIO_DacClockDivisor | 0x1000001a | Indicates the ratio between the sample clock timebase rate and the DAC sample clock. |
| kFlexRIO_AoChannelCount | 0x1000001b | Indicates the number of analog output channels on the device. |
| kFlexRIO_AiOffsetDac | 0x1000001c | Specifies the vertical offset of the channel in DAC codes. Setting this property will cause the value of the AI Offset property to be ignored. |
| kFlexRIO_BusType | 0x1000001d | Indicates the bus type for the device. |
| kFlexRIO_PrimaryTClkStreamInstance | 0x10000020 | Specifies which stream instance is the primary stream for TClk when serving as a TClk trigger master. |
| kFlexRIO_StartTriggerSynchronizer | 0x10000021 | Specifies the trigger synchronizer configuration. |
| kFlexRIO_DacResolution | 0x10000023 | Indicates the number of bits of data used to represent an output sample in the FPGA diagram. |
| kFlexRIO_UserClockCount | 0x10000024 | Specifies the number of user clocks available. |
| kFlexRIO_CableSenseMode | 0x10000025 | Specifies whether the CableSense signal will be generated on the specified channel. |
| kFlexRIO_SiChannelCount | 0x10000026 | Indicates the number of serial input channels on the device. |
| kFlexRIO_SoChannelCount | 0x10000027 | Indicates the number of serial output channels on the device. |
| kFlexRIO_SiPoCSource | 0x10000028 | Configures the power over coax source on the specified serial input channel. |
| kFlexRIO_SoPoCSink | 0x10000029 | Configures the power over coax sink on the specified serial output channel. |
| kFlexRIO_DiChannelCount | 0x1000002a | Indicates the number of digital input channels on the device. |
| kFlexRIO_DoChannelCount | 0x1000002b | Indicates the number of digital output channels on the device. |
| kFlexRIO_PfiChannelCount | 0x1000002c | Indicates the number of PFI channels on the device. |
| kFlexRIO_DiffPfiChannelCount | 0x1000002d | Indicates the number of differential PFI channels on the device. |
| kFlexRIO_PfiLineConfig | 0x1000002e | Specifies the line direction of the active channel. |
| kFlexRIO_DiffPfiLineConfig | 0x1000002f | Specifies the line direction of the active channel. |
| kFlexRIO_DioChannelCount | 0x10000030 | Indicates the number of digital I/O channels on the device. |
| kFlexRIO_DioLineConfig | 0x10000031 | Specifies the line direction of the active channel. |
| kFlexRIO_AoChannelStatus | 0x10000033 | Indicates the status of the channel. |
| kFlexRIO_SiCsi2Lanes | 0x10000035 | Specifies the number of active CSI-2 lanes. |
| kFlexRIO_SoCsi2Lanes | 0x10000036 | Specifies the number of active CSI-2 lanes. |
| kFlexRIO_CircularBufferSegments | 0x10000118 | Specifies the number of segments the FPGA-side circular buffer is divided into. |
| kFlexRIO_LastInt32Sentinel | 0x1000ffff |  |

Parent topic:

NI FlexRIO C Attributes

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__attributes_1ga9646f18662397674621cf812249d5cde.html language=enus -->
## TOPIC 00004: FlexRIO_AttributeBool Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__attributes_1ga9646f18662397674621cf812249d5cde.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__attributes_1ga9646f18662397674621cf812249d5cde.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_AttributeBoolMembersNameValueDescriptionkFlexRIO_FirstBoolSentinel0x40000000kFlexRIO_AiChannelEnabled0x40000000Specifies whether the active channel is enabled. kFlexRIO_StreamFinite0x40000001Specifies whether the stream should be finite. kFlexRIO_AnalogEdgeTriggerRising0x40000002S

### FlexRIO_AttributeBool Enumeration

#### Syntax

enum FlexRIO_AttributeBool

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_FirstBoolSentinel | 0x40000000 |  |
| kFlexRIO_AiChannelEnabled | 0x40000000 | Specifies whether the active channel is enabled. |
| kFlexRIO_StreamFinite | 0x40000001 | Specifies whether the stream should be finite. |
| kFlexRIO_AnalogEdgeTriggerRising | 0x40000002 | Specifies whether the analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge. |
| kFlexRIO_IoReady | 0x40000003 | Indicates whether the I/O is ready. |
| kFlexRIO_IocFilterEnable | 0x40000004 | Enables the interleaving offset correction filter for the ADC. |
| kFlexRIO_TClkApiControlEnabled | 0x40000007 | Specifies whether the TClk API will control this stream. |
| kFlexRIO_AoInvSincFilterEnabled | 0x40000008 | Enables the inverse sinc filter for the channel. |
| kFlexRIO_DacDigitalUpconverterEnabled | 0x40000009 | If true, this channel's output will be sourced from the DAC's digital upconverter. The user is expected to provide a complex waveform that will be properly steered to the DAC channels. |
| kFlexRIO_BaseboardReferenceClockExported | 0x4000000a | Controls whether the baseboard reference clock is exported. |
| kFlexRIO_ExternalAnalogEdgeTriggerRising | 0x4000000b | Specifies whether the external analog edge trigger triggers on a rising edge. Set this value to FALSE to trigger on a falling edge. |
| kFlexRIO_BaseboardReferenceClockPllLocked | 0x4000000c | Indicates whether the baseboard PLL is locked. |
| kFlexRIO_IsInputStream | 0x4000000e | Indicates whether the driver considers this stream to be an input stream (device to host). If false, then this is an output stream. |
| kFlexRIO_FpgaDdcEnabled | 0x4000000f | Enables the FPGA DDC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.ddc.enable N, where N is the stream number connected to this signal path. |
| kFlexRIO_DiEqualizationEnable | 0x40000010 | Specifies whether equalization is enabled for all digital input channels. |
| kFlexRIO_DoPreEmphasisEnable | 0x40000011 | Specifies whether pre-emphasis is enabled for all digital output channels. |
| kFlexRIO_DiffPfiInputEqualizationEnable | 0x40000012 | Specifies whether input equalization is enabled for all DIFF PFI channels. |
| kFlexRIO_DiffPfiOutputPreEmphasisEnable | 0x40000013 | Specifies whether output pre-emphasis is enabled for all DIFF PFI channels. |
| kFlexRIO_FpgaDdcIqEnabled | 0x40000019 | When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DDC is disabled. |
| kFlexRIO_FpgaDucEnabled | 0x4000001b | Enables the FPGA DUC chain for the device. Normally this will enable the decimator on modules that support it, as well as enable frequency shifting. However, details of the signal processing chain are dependent on the signal path in the FPGA. This property is detected by discovering flexrio.dsp.duc.enable N, where N is the stream number connected to this signal path. |
| kFlexRIO_FpgaDucIqEnabled | 0x4000001c | When IQ mode is enabled, both the I and Q data will be transferred to the stream. When it is disabled, only the I portions are captured on the device and transferred to the host. This property has no effect if the DUC is disabled. |
| kFlexRIO_DataPathIqEnabled | 0x4000001e | The data path on the FPGA uses complex data. This affects data steering in the FPGA. For a device with upconversion, this will be true when either the FPGA has a DUC operating in IQ mode (see the attribute 'FPGA DUC IQ Enabled'), or the device has an upconverter built into the front end that requires IQ data (see the attribute 'DAC Digital Upconverter Enabled'). In IQ mode, you are required to supply IQ data to WriteStream. |
| kFlexRIO_LinkedStartTrigger | 0x4000001f | Configures whether this stream's trigger is overridden to be linked to another stream's start event. Ensure the target stream is started before the trigger arrives. |
| kFlexRIO_BypassPll | 0x40000020 | Specifies whether the active user clock is a re-exported copy of the reference clock that bypasses the PLL. |
| kFlexRIO_UserClockEnabled | 0x40000021 | Specifies whether the active user clock is enabled. |
| kFlexRIO_SiPoCInRange | 0x40000022 | Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial input channel. |
| kFlexRIO_SoPoCInRange | 0x40000023 | Indicates whether power over coax is enabled, above the minimum valid voltage, and not receiving a fault signal on the specified serial output channel. |
| kFlexRIO_SiRefClkEnabled | 0x40000024 | Specifies whether the reference clock is enabled. |
| kFlexRIO_SoRefClkEnabled | 0x40000025 | Specifies whether the reference clock is enabled. |
| kFlexRIO_LastBoolSentinel | 0x4000ffff |  |

Parent topic:

NI FlexRIO C Attributes

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__attributes_1gacfa49c1351960724659db68249e6e678.html language=enus -->
## TOPIC 00005: FlexRIO_AttributeDouble Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__attributes_1gacfa49c1351960724659db68249e6e678.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__attributes_1gacfa49c1351960724659db68249e6e678.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_AttributeDoubleMembersNameValueDescriptionkFlexRIO_FirstDoubleSentinel0x20000000kFlexRIO_AnalogEdgeTriggerLevel0x20000002Specifies the trigger level in volts. kFlexRIO_AnalogEdgeTriggerHysteresis0x20000003Specifies the trigger hysteresis in volts. kFlexRIO_ExternalAnalogEdgeTrigge

### FlexRIO_AttributeDouble Enumeration

#### Syntax

enum FlexRIO_AttributeDouble

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_FirstDoubleSentinel | 0x20000000 |  |
| kFlexRIO_AnalogEdgeTriggerLevel | 0x20000002 | Specifies the trigger level in volts. |
| kFlexRIO_AnalogEdgeTriggerHysteresis | 0x20000003 | Specifies the trigger hysteresis in volts. |
| kFlexRIO_ExternalAnalogEdgeTriggerLevel | 0x20000004 | Specifies the trigger level in volts. |
| kFlexRIO_FpgaTemperature | 0x20000005 | Indicates the current FPGA temperature in degrees Celsius. |
| kFlexRIO_TotalPower | 0x20000006 | Indicates the total power consumed by the device in watts. |
| kFlexRIO_12vPower | 0x20000007 | Indicates the power consumed by the 12V rail in watts. |
| kFlexRIO_3v3Power | 0x20000008 | Indicates the power consumed by the 3.3V rail in watts. |
| kFlexRIO_12vIoPower | 0x20000009 | Indicates the power consumed by the 12V rail to the IO in watts. |
| kFlexRIO_TemperatureLimit | 0x2000000a | Indicates the temperature in degrees Celsius at which the device will shut down to prevent damage. |
| kFlexRIO_PowerLimit | 0x2000000b | Indicates the level of total power consumption in watts at which the device will shut down to prevent damage. |
| kFlexRIO_AdcTemperature | 0x2000000c | Indicates the current ADC temperature in degrees Celsius. |
| kFlexRIO_CalibrationTemperature | 0x2000000d | Indicates the FPGA temperature at last write to calibration storage in degrees Celsius. |
| kFlexRIO_VerificationTemperature | 0x2000000e | Indicates the FPGA temperature at last verification in degrees Celsius. |
| kFlexRIO_AiImpedance | 0x2000000f | Specifies the impedance of the channel in ohms. |
| kFlexRIO_AiRange | 0x20000010 | Specifies the vertical range of the channel in volts. |
| kFlexRIO_AiScalingGain | 0x20000011 | Specifies the ratio between volts and ADC codes on the channel data. |
| kFlexRIO_AiScalingOffset | 0x20000012 | Specifies the offset between volts and ADC codes on the channel data. |
| kFlexRIO_SampleDt | 0x20000013 | Overrides the dt metadata returned in waveforms. |
| kFlexRIO_DioVoltage | 0x20000014 | Specifies the DIO voltage. |
| kFlexRIO_DataClockRate | 0x20000015 | Indicates the Data Clock rate for the I/O module. |
| kFlexRIO_AdcSampleRate | 0x20000016 | Indicates the rate at which the analog-to-digital converter samples and digitizes a signal. |
| kFlexRIO_SampleClockTimebaseRate | 0x20000017 | Specifies the Sample Clock timebase rate. |
| kFlexRIO_ReferenceClockRate | 0x20000018 | Indicates the Reference Clock rate. |
| kFlexRIO_DataDelay | 0x20000019 | Specifies the delay after the sample clock rising edge when the device acquires a new data sample. |
| kFlexRIO_DacSampleRate | 0x2000001a | Indicates the rate at which the digital-to-analog converter outputs samples. |
| kFlexRIO_AoImpedance | 0x2000001b | Specifies the impedance of the channel in ohms. |
| kFlexRIO_AoScalingGain | 0x2000001c | Specifies the ratio between volts and DAC codes on the channel data. |
| kFlexRIO_AoScalingOffset | 0x2000001d | Specifies the offset between volts and DAC codes on the channel data. |
| kFlexRIO_AoRange | 0x2000001e | Specifies the vertical range of the channel in volts. |
| kFlexRIO_AiOffset | 0x2000001f | Specifies the vertical offset of the channel in volts. |
| kFlexRIO_ExternalAnalogEdgeTriggerHysteresis | 0x20000021 | Specifies the trigger hysteresis in volts. |
| kFlexRIO_DspFrequencyShiftMagnitude | 0x2000002a | Directly specifies the magnitude of the frequency shift applied to the signal. This is intended for advanced users who need to directly configure the magnitude without the units of the API. |
| kFlexRIO_DspFrequencyShift | 0x2000002b | When DSP is enabled, this attribute specifies the amount that the frequency spectrum will be shifted. For input streams, this means shifting the frequency spectrum down by the specified frequency. For output streams, this means shifting the spectrum up by the specified frequency. |
| kFlexRIO_UserClockFrequency | 0x2000002c | Configures the specified user clock to generate the requested frequency. |
| kFlexRIO_SiPoCVoltage | 0x2000002d | Indicates the power over coax voltage on the specified serial input channel. |
| kFlexRIO_SoPoCVoltage | 0x2000002e | Indicates the power over coax voltage on the specified serial output channel. |
| kFlexRIO_SiPoCCurrent | 0x2000002f | Indicates the power over coax current in amps on the specified serial input channel. |
| kFlexRIO_SoPoCCurrent | 0x20000030 | Indicates the power over coax current in amps on the specified serial output channel. |
| kFlexRIO_PfiVoltage | 0x20000031 | Specifies the PFI voltage. |
| kFlexRIO_DioLineVoltage | 0x20000032 | Specifies the DIO line voltage. |
| kFlexRIO_TotalIoPower | 0x20000033 | Indicates the total power consumed by the IO module in watts. |
| kFlexRIO_SoCsi2DataRate | 0x20000034 | Specifies the CSI-2 data rate. |
| kFlexRIO_SiRefClkFrequency | 0x20000035 | Specifies the reference clock associated with the serial input channel. |
| kFlexRIO_SoRefClkFrequency | 0x20000036 | Specifies the reference clock associated with the serial output channel. |
| kFlexRIO_LastDoubleSentinel | 0x2000ffff |  |

Parent topic:

NI FlexRIO C Attributes

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__attributes_1gafbb2aea534620173c0a8b61ab210cb66.html language=enus -->
## TOPIC 00006: FlexRIO_AttributeString Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__attributes_1gafbb2aea534620173c0a8b61ab210cb66.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__attributes_1gafbb2aea534620173c0a8b61ab210cb66.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_AttributeStringMembersNameValueDescriptionkFlexRIO_FirstStringSentinel0x30000000kFlexRIO_DigitalStartTriggerSource0x30000000Specifies the source of the digital start trigger. kFlexRIO_StreamFifoName0x30000002Returns a semicolon delimited list of the names of the FIFOs used on the

### FlexRIO_AttributeString Enumeration

#### Syntax

enum FlexRIO_AttributeString

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_FirstStringSentinel | 0x30000000 |  |
| kFlexRIO_DigitalStartTriggerSource | 0x30000000 | Specifies the source of the digital start trigger. |
| kFlexRIO_StreamFifoName | 0x30000002 | Returns a semicolon delimited list of the names of the FIFOs used on the stream. |
| kFlexRIO_StartTriggerOutputTerminal | 0x30000003 | Specifies the export destination for the start trigger. |
| kFlexRIO_StartTriggerForTClkOutputTerminal | 0x30000007 | Specifies the export destination for the TClk conditioned start trigger. |
| kFlexRIO_DspResetSendingTerm | 0x3000000a | Indicates the terminal that will generate the TClk synchronized DSP Reset event if this device is the DSP Reset Master. The DSP Reset Master device is the first device in the array of devices passed to SynchronizedDspReset. |
| kFlexRIO_DspResetSource | 0x3000000b | Specifies the source of the TClk synchronized DSP Reset event. |
| kFlexRIO_TClkStartTriggerTerm | 0x3000000c | Indicates the terminal that will export the TClk synchronized start trigger. |
| kFlexRIO_BitfileVersion | 0x3000000d |  |
| kFlexRIO_BitfileVendor | 0x3000000e | Indicates the vendor of the bitfile |
| kFlexRIO_BitfileIdentity | 0x3000000f | Indicates the identity of the bitfile |
| kFlexRIO_SerialNumber | 0x30000010 | Indicates the device serial number |
| kFlexRIO_SiI2cName | 0x30000011 | Indicates the name of the I2C bus instance associated with the specified serial input channel. |
| kFlexRIO_SoI2cName | 0x30000012 | Indicates the name of the I2C bus instance associated with the specified serial output channel. |
| kFlexRIO_SiRefClkName | 0x30000013 | Indicates the name of the reference clock associated with the specified serial input channel. |
| kFlexRIO_SoRefClkName | 0x30000014 | Indicates the name of the reference clock associated with the specified serial output channel. |
| kFlexRIO_FpgaTxClockSelect | 0x30000015 | Specifies the name of the user clock to be used as the FPGA generation clock. |
| kFlexRIO_SoDataClkName | 0x30000016 | Indicates the name of the CSI-2 data rate clock associated with the specified serial output channel. |
| kFlexRIO_LastStringSentinel | 0x3000ffff |  |

Parent topic:

NI FlexRIO C Attributes

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__defines.html language=enus -->
## TOPIC 00007: NI FlexRIO C Defines

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__defines.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__defines.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionFlexRIO_RouteTicketFlexRIO_StatusFlexRIO_WfmInfoThis structure is used by stream read endpoints to return additional information about the waveform. NIComplexI16NiFpga_SessionAttachmentsNone

### NI FlexRIO C Defines

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| FlexRIO_RouteTicket |  |
| FlexRIO_Status |  |
| FlexRIO_WfmInfo | This structure is used by stream read endpoints to return additional information about the waveform. |
| NIComplexI16 |  |
| NiFpga_Session |  |

#### Attachments

None

Parent topic:

niflexrioapi.h

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__defines_1ga11774adc54521a34b07d472d70996418.html language=enus -->
## TOPIC 00008: FlexRIO_Status

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__defines_1ga11774adc54521a34b07d472d70996418.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__defines_1ga11774adc54521a34b07d472d70996418.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxint32_t FlexRIO_StatusRemarksReports the status of this operation. To obtain a text description of the status code, call niFlexRIO_GetError. The general meaning of the status code is as follows:ValueMeaning0SuccessPositive valuesWarningsNegative valuesErrors

### FlexRIO_Status

#### Syntax

int32_t FlexRIO_Status

#### Remarks

Reports the status of this operation. To obtain a text description of the status code, call [niFlexRIO_GetError](group__functions_1ga07ed9d5bec88590e02e86dd4743d91e4.html). The general meaning of the status code is as follows:

| Value | Meaning |
| --- | --- |
| 0 | Success |
| Positive values | Warnings |
| Negative values | Errors |

Parent topic:

NI FlexRIO C Defines

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__defines_1ga2bcfaa592fb0ccba8e715fbac7f56404.html language=enus -->
## TOPIC 00009: NiFpga_Session

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__defines_1ga2bcfaa592fb0ccba8e715fbac7f56404.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__defines_1ga2bcfaa592fb0ccba8e715fbac7f56404.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxuint32_t NiFpga_Session

### NiFpga_Session

#### Syntax

uint32_t NiFpga_Session

Parent topic:

NI FlexRIO C Defines

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__defines_1gabb6d3e17de8e409b3715f27c9150f397.html language=enus -->
## TOPIC 00010: FlexRIO_RouteTicket

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__defines_1gabb6d3e17de8e409b3715f27c9150f397.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__defines_1gabb6d3e17de8e409b3715f27c9150f397.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxuint32_t FlexRIO_RouteTicket

### FlexRIO_RouteTicket

#### Syntax

uint32_t FlexRIO_RouteTicket

Parent topic:

NI FlexRIO C Defines

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums.html language=enus -->
## TOPIC 00011: NI FlexRIO C Enums

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionFlexRIO_AoChannelStatusFlexRIO_BaseboardRefClkSrcFlexRIO_BusTypeFlexRIO_CableSenseModeFlexRIO_CouplingFlexRIO_Csi2NumLanesFlexRIO_DacDigitalUpconverterModeFlexRIO_DiffPfiConfigurationFlexRIO_DioConfigurationFlexRIO_ExtClkSrcFlexRIO_IoModuleRefClkPinSrcFlexRIO_NI

### NI FlexRIO C Enums

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| FlexRIO_AoChannelStatus |  |
| FlexRIO_BaseboardRefClkSrc |  |
| FlexRIO_BusType |  |
| FlexRIO_CableSenseMode |  |
| FlexRIO_Coupling |  |
| FlexRIO_Csi2NumLanes |  |
| FlexRIO_DacDigitalUpconverterMode |  |
| FlexRIO_DiffPfiConfiguration |  |
| FlexRIO_DioConfiguration |  |
| FlexRIO_ExtClkSrc |  |
| FlexRIO_IoModuleRefClkPinSrc |  |
| FlexRIO_NI6569_Bank |  |
| FlexRIO_NI6569_RXClockSource |  |
| FlexRIO_NI6569_TXClockSource |  |
| FlexRIO_PfiConfiguration |  |
| FlexRIO_RefClkSrc |  |
| FlexRIO_SampleClkSrc |  |
| FlexRIO_SiPoCSource |  |
| FlexRIO_SoPoCSink |  |
| FlexRIO_StartTriggerSync |  |
| FlexRIO_StreamDataFormat |  |
| FlexRIO_TriggerSensitivity |  |
| FlexRIO_TriggerType |  |
| NIFLEXRIO_Status |  |

#### Attachments

None

Parent topic:

niflexrioapi.h

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga07eefc916c54d54d6ac51a53d92b3a3d.html language=enus -->
## TOPIC 00012: FlexRIO_RefClkSrc Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga07eefc916c54d54d6ac51a53d92b3a3d.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga07eefc916c54d54d6ac51a53d92b3a3d.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_RefClkSrcMembersNameValueDescriptionkFlexRIO_RefClkSrc_Default0Default for the board kFlexRIO_RefClkSrc_Onboard1Onboard reference clock kFlexRIO_RefClkSrc_PXI_Clk10210 MHz Backplane clock kFlexRIO_RefClkSrc_External3External reference source kFlexRIO_RefClkSrc_None4No reference cl

### FlexRIO_RefClkSrc Enumeration

#### Syntax

enum FlexRIO_RefClkSrc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_RefClkSrc_Default | 0 | Default for the board |
| kFlexRIO_RefClkSrc_Onboard | 1 | Onboard reference clock |
| kFlexRIO_RefClkSrc_PXI_Clk10 | 2 | 10 MHz Backplane clock |
| kFlexRIO_RefClkSrc_External | 3 | External reference source |
| kFlexRIO_RefClkSrc_None | 4 | No reference clock |
| kFlexRIO_RefClkSrc_BaseboardReference | 5 | Reference clock provided by the baseboard. The baseboard's reference can be controlled using the Baseboard Reference Clock Source attribute. |
| kFlexRIO_RefClkSrc_PXI_Clk100 | 6 | 100 MHz Backplane clock |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga2514b563d19380e070a3f8d9a633a88e.html language=enus -->
## TOPIC 00013: FlexRIO_DacDigitalUpconverterMode Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga2514b563d19380e070a3f8d9a633a88e.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga2514b563d19380e070a3f8d9a633a88e.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_DacDigitalUpconverterModeMembersNameValueDescriptionkFlexRIO_DacDigitalUpconverterMode_Disabled0Upconverter disabled kFlexRIO_DacDigitalUpconverterMode_EnabledAo01Enabled AO 0 kFlexRIO_DacDigitalUpconverterMode_EnabledAo12Enabled AO 1 kFlexRIO_DacDigitalUpconverterMode_EnabledAo0A

### FlexRIO_DacDigitalUpconverterMode Enumeration

#### Syntax

enum FlexRIO_DacDigitalUpconverterMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_DacDigitalUpconverterMode_Disabled | 0 | Upconverter disabled |
| kFlexRIO_DacDigitalUpconverterMode_EnabledAo0 | 1 | Enabled AO 0 |
| kFlexRIO_DacDigitalUpconverterMode_EnabledAo1 | 2 | Enabled AO 1 |
| kFlexRIO_DacDigitalUpconverterMode_EnabledAo0Ao1 | 3 | Enabled AO 0 and AO 1 |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga28c44b857e7bfdd8bf74fcc9cdab3b75.html language=enus -->
## TOPIC 00014: FlexRIO_BaseboardRefClkSrc Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga28c44b857e7bfdd8bf74fcc9cdab3b75.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga28c44b857e7bfdd8bf74fcc9cdab3b75.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_BaseboardRefClkSrcMembersNameValueDescriptionkFlexRIO_BaseboardRefClkSrc_Onboard0Onboard reference clock. kFlexRIO_BaseboardRefClkSrc_SynchronizationConnector1Reference clock sourced from the FlexRIO synchronization connector.

### FlexRIO_BaseboardRefClkSrc Enumeration

#### Syntax

enum FlexRIO_BaseboardRefClkSrc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_BaseboardRefClkSrc_Onboard | 0 | Onboard reference clock. |
| kFlexRIO_BaseboardRefClkSrc_SynchronizationConnector | 1 | Reference clock sourced from the FlexRIO synchronization connector. |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga296c592a02714c054886ce182833a530.html language=enus -->
## TOPIC 00015: FlexRIO_TriggerType Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga296c592a02714c054886ce182833a530.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga296c592a02714c054886ce182833a530.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_TriggerTypeMembersNameValueDescriptionkFlexRIO_TriggerType_Immediate0Specifies an immediate trigger kFlexRIO_TriggerType_Digital1Specifies a digital trigger kFlexRIO_TriggerType_User2Specifies a user-defined trigger kFlexRIO_TriggerType_Dio3Specifies a DIO trigger kFlexRIO_Trigger

### FlexRIO_TriggerType Enumeration

#### Syntax

enum FlexRIO_TriggerType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_TriggerType_Immediate | 0 | Specifies an immediate trigger |
| kFlexRIO_TriggerType_Digital | 1 | Specifies a digital trigger |
| kFlexRIO_TriggerType_User | 2 | Specifies a user-defined trigger |
| kFlexRIO_TriggerType_Dio | 3 | Specifies a DIO trigger |
| kFlexRIO_TriggerType_Analog | 4 | Specifies an analog trigger |
| kFlexRIO_TriggerType_ExternalAnalog | 5 | Specifies an external analog trigger |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga30ca53d6a6063c13fc68797cdcbaad5c.html language=enus -->
## TOPIC 00016: FlexRIO_StartTriggerSync Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga30ca53d6a6063c13fc68797cdcbaad5c.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga30ca53d6a6063c13fc68797cdcbaad5c.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_StartTriggerSyncMembersNameValueDescriptionkFlexRIO_StartTriggerSync_Disabled0Start trigger synchronizers disabled. kFlexRIO_StartTriggerSync_Master1Start trigger synchronizers configured for being a TClk master. kFlexRIO_StartTriggerSync_Slave2Start trigger synchronizers configur

### FlexRIO_StartTriggerSync Enumeration

#### Syntax

enum FlexRIO_StartTriggerSync

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_StartTriggerSync_Disabled | 0 | Start trigger synchronizers disabled. |
| kFlexRIO_StartTriggerSync_Master | 1 | Start trigger synchronizers configured for being a TClk master. |
| kFlexRIO_StartTriggerSync_Slave | 2 | Start trigger synchronizers configured for being a TClk slave. |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga35cddf3b8594e0f947c01a59b71ae11c.html language=enus -->
## TOPIC 00017: FlexRIO_ExtClkSrc Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga35cddf3b8594e0f947c01a59b71ae11c.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga35cddf3b8594e0f947c01a59b71ae11c.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_ExtClkSrcMembersNameValueDescriptionkFlexRIO_ExtClkSrc_FrontPanel0External clock terminal on the front panel

### FlexRIO_ExtClkSrc Enumeration

#### Syntax

enum FlexRIO_ExtClkSrc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_ExtClkSrc_FrontPanel | 0 | External clock terminal on the front panel |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga487009f5da4110ef715877de1b4fd362.html language=enus -->
## TOPIC 00018: FlexRIO_DiffPfiConfiguration Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga487009f5da4110ef715877de1b4fd362.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga487009f5da4110ef715877de1b4fd362.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_DiffPfiConfigurationMembersNameValueDescriptionkFlexRIO_DiffPfiConfiguration_Input0Input Mode kFlexRIO_DiffPfiConfiguration_Output1Output Mode

### FlexRIO_DiffPfiConfiguration Enumeration

#### Syntax

enum FlexRIO_DiffPfiConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_DiffPfiConfiguration_Input | 0 | Input Mode |
| kFlexRIO_DiffPfiConfiguration_Output | 1 | Output Mode |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga625992f882ae5e0b6b783d76be065359.html language=enus -->
## TOPIC 00019: FlexRIO_DioConfiguration Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga625992f882ae5e0b6b783d76be065359.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga625992f882ae5e0b6b783d76be065359.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_DioConfigurationMembersNameValueDescriptionkFlexRIO_DioConfiguration_Input0Input Mode kFlexRIO_DioConfiguration_Output1Output Mode

### FlexRIO_DioConfiguration Enumeration

#### Syntax

enum FlexRIO_DioConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_DioConfiguration_Input | 0 | Input Mode |
| kFlexRIO_DioConfiguration_Output | 1 | Output Mode |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga6d9fa6ad1fea58d0a39918e78460205f.html language=enus -->
## TOPIC 00020: FlexRIO_BusType Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga6d9fa6ad1fea58d0a39918e78460205f.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga6d9fa6ad1fea58d0a39918e78460205f.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_BusTypeMembersNameValueDescriptionkFlexRIO_BusType_PXIe0PXI Express kFlexRIO_BusType_PCIe1PCI Express

### FlexRIO_BusType Enumeration

#### Syntax

enum FlexRIO_BusType

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_BusType_PXIe | 0 | PXI Express |
| kFlexRIO_BusType_PCIe | 1 | PCI Express |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga6dd826010d3030a8d1f0e0b0a8bba338.html language=enus -->
## TOPIC 00021: FlexRIO_NI6569_TXClockSource Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga6dd826010d3030a8d1f0e0b0a8bba338.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga6dd826010d3030a8d1f0e0b0a8bba338.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_NI6569_TXClockSourceMembersNameValueDescriptionkFlexRIO_NI6569_TXClockSource_Lmk0LMK04832 kFlexRIO_NI6569_TXClockSource_Si5142Si514

### FlexRIO_NI6569_TXClockSource Enumeration

#### Syntax

enum FlexRIO_NI6569_TXClockSource

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_NI6569_TXClockSource_Lmk | 0 | LMK04832 |
| kFlexRIO_NI6569_TXClockSource_Si514 | 2 | Si514 |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga74916b5f1384c9a6e0bd7fc1266e9ea6.html language=enus -->
## TOPIC 00022: FlexRIO_NI6569_Bank Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga74916b5f1384c9a6e0bd7fc1266e9ea6.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga74916b5f1384c9a6e0bd7fc1266e9ea6.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_NI6569_BankMembersNameValueDescriptionkFlexRIO_NI6569_Bank_Bank440Bank 44 kFlexRIO_NI6569_Bank_Bank451Bank 45 kFlexRIO_NI6569_Bank_Bank462Bank 46 kFlexRIO_NI6569_Bank_AllBanks2147483647All Banks

### FlexRIO_NI6569_Bank Enumeration

#### Syntax

enum FlexRIO_NI6569_Bank

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_NI6569_Bank_Bank44 | 0 | Bank 44 |
| kFlexRIO_NI6569_Bank_Bank45 | 1 | Bank 45 |
| kFlexRIO_NI6569_Bank_Bank46 | 2 | Bank 46 |
| kFlexRIO_NI6569_Bank_AllBanks | 2147483647 | All Banks |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga7c57e7d407fe7d4510056b4003cef091.html language=enus -->
## TOPIC 00023: FlexRIO_SoPoCSink Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga7c57e7d407fe7d4510056b4003cef091.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga7c57e7d407fe7d4510056b4003cef091.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_SoPoCSinkMembersNameValueDescriptionkFlexRIO_SoPoCSink_None0Power over Coax None kFlexRIO_SoPoCSink_Auxiliary2Power over Coax Auxiliary

### FlexRIO_SoPoCSink Enumeration

#### Syntax

enum FlexRIO_SoPoCSink

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_SoPoCSink_None | 0 | Power over Coax None |
| kFlexRIO_SoPoCSink_Auxiliary | 2 | Power over Coax Auxiliary |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga7eacf1989d101783c789c6ce6cb9ae96.html language=enus -->
## TOPIC 00024: FlexRIO_SiPoCSource Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga7eacf1989d101783c789c6ce6cb9ae96.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga7eacf1989d101783c789c6ce6cb9ae96.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_SiPoCSourceMembersNameValueDescriptionkFlexRIO_SiPoCSource_None0Power over Coax None kFlexRIO_SiPoCSource_Internal1Power over Coax Internal kFlexRIO_SiPoCSource_Auxiliary2Power over Coax Auxiliary

### FlexRIO_SiPoCSource Enumeration

#### Syntax

enum FlexRIO_SiPoCSource

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_SiPoCSource_None | 0 | Power over Coax None |
| kFlexRIO_SiPoCSource_Internal | 1 | Power over Coax Internal |
| kFlexRIO_SiPoCSource_Auxiliary | 2 | Power over Coax Auxiliary |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga817c17289e1c26ef6c59f722dd79f3c2.html language=enus -->
## TOPIC 00025: NIFLEXRIO_Status Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga817c17289e1c26ef6c59f722dd79f3c2.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga817c17289e1c26ef6c59f722dd79f3c2.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum NIFLEXRIO_StatusRemarksDeclaration of FlexRIO status codes. Use niFlexRIO_GetError() to get additional information about these errors. MembersNameValueDescriptionNIFLEXRIO_Status_Success0NIFLEXRIO_Status_iFifoInvalidArguments-304300The command was sent with invalid arguments. Check your a

### NIFLEXRIO_Status Enumeration

#### Syntax

enum NIFLEXRIO_Status

#### Remarks

Declaration of FlexRIO status codes. Use [niFlexRIO_GetError()](group__functions_1ga07ed9d5bec88590e02e86dd4743d91e4.html) to get additional information about these errors.

#### Members

| Name | Value | Description |
| --- | --- | --- |
| NIFLEXRIO_Status_Success | 0 |  |
| NIFLEXRIO_Status_iFifoInvalidArguments | -304300 | The command was sent with invalid arguments. Check your arguments and try again. |
| NIFLEXRIO_Status_iFifoInvalidCommand | -304301 | The command that was sent does not exist. |
| NIFLEXRIO_Status_iFifoUnsupportedCommand | -304302 | The command that was sent is not supported by this target. |
| NIFLEXRIO_Status_iFifoCommandTimeout | -304303 | An internal error has occurred. Contact National Instruments technical support at ni.com/support. |
| NIFLEXRIO_Status_iFifoCommandInternalError | -304304 | An internal error has occurred. Contact National Instruments technical support at ni.com/support. |
| NIFLEXRIO_Status_iFifoCommandSentWhenIoDisabled | -304305 | The command that was sent requires the FPGA IO to be enabled. Wait until the IO is enabled and try again. |
| NIFLEXRIO_Status_iFifoUnsupportedInterface | -304306 | The requested interface is not implemented on this endpoint. |
| NIFLEXRIO_Status_iFifoInterfaceVersionMismatch | -304307 | The requested interface version is not compatible with hardware. |
| NIFLEXRIO_Status_iFifoUserClockNotToggling | -304308 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_iFifoResetTimeout | -304309 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_iFifoEnableTimeout | -304310 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_iFifoDisableTimeout | -304311 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_ThermalShutdown | -304312 | The device has shut down to protect against excessive FPGA temperature. Check airflow and cooling and redownload the bitfile. To avoid this error, monitor the FPGA temperature, temperature shutdown threshold, and margin of the FPGA. If necessary, reduce FPGA temperature. |
| NIFLEXRIO_Status_PowerShutdown | -304313 | The device has shut down to protect against excessive power consumption. Check airflow and cooling and redownload the bitfile. To avoid this error, monitor the power consumption, power shutdown threshold, and margin of the device. If necessary, reduce FPGA power consumption. |
| NIFLEXRIO_Status_IoModuleNotReady | -304314 | The device has not become ready within the expected time. This may indicate a problem with the hardware initialization or the system configuration. Use the IO Error property to check for further information. |
| NIFLEXRIO_Status_PhaseDacCalibrationFailed | -304315 | Phase DAC calibration failed. |
| NIFLEXRIO_Status_IoPllLockTimedout | -304316 | The IO Module PLL did not lock to the provided reference in time. Please check your cable connections and system configuration and try again. |
| NIFLEXRIO_Status_IoJesdLinkError | -304317 | The IO Module was unable to configure. If you are using an external sample clock, check your cable connections and system configuration and try again. |
| NIFLEXRIO_Status_IoClipPllLockTimedout | -304318 | The IO Module was unable to configure. If you are using an external sample clock, check your cable connections and system configuration and try again. |
| NIFLEXRIO_Status_IoFirmwareRevTooLow | -304319 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_IoErrorFirmwareRevTooHigh | -304320 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_UserI2cTransactionFailed | -304321 | The requested I2C transaction was unable to complete. This is usually because the requested I2C address was not acknowledged, or because the I2C slave prematurely terminated the transaction. |
| NIFLEXRIO_Status_IoErrorRsvd1 | -304322 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_IoErrorRsvd2 | -304323 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_LinkCfgIoStratReadFailed | -304324 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_CalibrationWaitForIoTimeout | -304325 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_IsoPortNotReady | -304326 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_TdcNotReady | -304327 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_TdcMeasurementFailed | -304328 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_DspResetTimeoutWaitingForState | -304329 | DSP reset timed out waiting for a state transition. |
| NIFLEXRIO_Status_BaseboardPllLockTimeout | -304330 | Timed out waiting for baseboard PLL to lock. Check that the baseboard ribbon cable is correctly connected. |
| NIFLEXRIO_Status_QsfpCableNotPresent | -304331 | The specified QSFP connector is not present. Check that the cable is correctly connected. |
| NIFLEXRIO_Status_QsfpResetFailed | -304332 | Failed to reset the QSFP ports. |
| NIFLEXRIO_Status_CableSensePulseFailed | -304333 | Failed enable or disable the CableSense pulse. |
| NIFLEXRIO_Status_58WPowerAndCoolingChassisRequired | -304334 | This device requires a chassis with 58 W slot cooling capacity. Refer to your product documentation for more information. |
| NIFLEXRIO_Status_AnalogOutputShutdown | -304335 | Output channel(s) is shut down to protect against excessive power consumption or temperature. Check the status of analog output channel(s) to determine which channel(s) is shut down. Redownload the bitfile to restore normal operation of analog output channel(s). |
| NIFLEXRIO_Status_Flash_MultipleSessionsDetected | -304336 | Another flash session is already open. Close the other flash session and retry this operation. |
| NIFLEXRIO_Status_EEPROMWriteAccessDisabled | -304337 | The EEPROM write access is disabled. |
| NIFLEXRIO_Status_ConfigureAOFailed | -304338 | Internal HW Error, contact National Instruments. |
| NIFLEXRIO_Status_SoftwareError | -304400 | The software encountered an unspecific error. |
| NIFLEXRIO_Status_StreamWaveformMismatch | -304401 | The number of channels requested by ReadStream does not match those enabled on the stream, or there are no channels enabled via the API. |
| NIFLEXRIO_Status_NullPointer | -304402 | A user-provided pointer was NULL. This function does not have defined behavior for NULL |
| NIFLEXRIO_Status_AttributeTypeMismatch | -304403 | User accessed an attribute using the wrong data type. |
| NIFLEXRIO_Status_AttributeNotAvailable | -304404 | Attribute is undefined or not present in the currently running session. |
| NIFLEXRIO_Status_InvalidStreamIndex | -304405 | User accessed a stream that either does not exist or is not discoverable. |
| NIFLEXRIO_Status_CalibrationOutOfBounds | -304406 | User accessed a calibration index that is out of bounds. |
| NIFLEXRIO_Status_ImageMetadataAbsent | -304407 | User tried to load a bitfile from flash, but the flash did not have metadata for that image. |
| NIFLEXRIO_Status_InvalidAttributeValue | -304408 | Requested value is not a supported value for this property. The property value may be invalid because it conflicts with another property. |
| NIFLEXRIO_Status_TClkNotSupportedWithExternalSampleClock | -304409 | TClk is not supported when using an external sample clock. |
| NIFLEXRIO_Status_ExternalSampleClockSourceNotSupported | -304410 | The source provided for the external sample clock is invalid. |
| NIFLEXRIO_Status_TClkResourcesInUse | -304411 | TClk resources are currently in use by another session. |
| NIFLEXRIO_Status_MultipleSessionsDetected | -304412 | Another session is already open to the specified device. Close the other session and retry this operation. |
| NIFLEXRIO_Status_AttributeNotReadable | -304413 | Attribute is write-only. |
| NIFLEXRIO_Status_AttributeNotWritable | -304414 | Attribute is read-only. |
| NIFLEXRIO_Status_StreamTimedOutDueToStreamError | -304415 | The stream entered an error state due to a FIFO overflow or a forced error. The read was unable to complete because the requested samples have not arrived. |
| NIFLEXRIO_Status_StreamTimedOutDueToStreamCancel | -304416 | The stream entered an cancelled state. The read was unable to complete because the requested samples have not arrived. |
| NIFLEXRIO_Status_DramNotReady | -304417 | The DRAM buffer did not become ready within the specified timeout. |
| NIFLEXRIO_Status_DataNotValid | -304418 | The IO data did not become valid within the specified timeout. |
| NIFLEXRIO_Status_StringParsingError | -304419 | The string provided could not be parsed due to a formatting error. |
| NIFLEXRIO_Status_StringParsingTooManyEntries | -304420 | The string provided contains too many entries to be valid. |
| NIFLEXRIO_Status_StringParsingInvalidChannel | -304421 | The string provided contains an invalid channel. |
| NIFLEXRIO_Status_StringParsingInvalidStream | -304422 | The string provided contains an invalid stream number. |
| NIFLEXRIO_Status_AttributeContextMismatch | -304423 | Attribute is present in the currently running session, but not at the selected context. |
| NIFLEXRIO_Status_FirmwareUpdateInProgress | -304424 | Firmware update already in progress. |
| NIFLEXRIO_Status_FirmwareUpdateNotInProgress | -304425 | Firmware update is not yet in progress. |
| NIFLEXRIO_Status_DspNotReady | -304426 | The DSP did not become ready within the timeout period. This is likely a result of an improper connection or behavior of the 'flexrio.dsp.reset N' control or the 'flexrio.dsp.ready N' indicator. Validate the behavior of your FPGA diagram. |
| NIFLEXRIO_Status_LoopBufferNotFilled | -304427 | The onboard waveform looping buffer did not fill up within the timeout period. A write operation posted data for transfer to the FPGA, but the FPGA did not report that all the data arrived. Validate the behavior of your FPGA diagram. |
| NIFLEXRIO_Status_StringParsingInvalidClock | -304428 | The string provided contains an invalid clock number. |
| NIFLEXRIO_Status_InvalidStreamOperation | -304429 | This stream does not support the requested operation. Verify the stream number or the FPGA loaded. |
| NIFLEXRIO_Status_IoModuleNotPresent | -304430 | This operation requires a device with an IO Module connected, but there is no IO Module detected. |
| NIFLEXRIO_Status_InvalidFirmwareBundle | -304431 | This firmware bundle is not valid or is not compatible with the selected HW. |
| NIFLEXRIO_Status_CorruptFirmwareBundle | -304432 | This firmware bundle is corrupt and cannot be parsed. |
| NIFLEXRIO_Status_FileMissingInFirmwareBundle | -304433 | This firmware bundle is missing an expected file. |
| NIFLEXRIO_Status_RefClkRangeUnsupported | -304434 | The input reference clock could not be divided down to a valid PLL input. |
| NIFLEXRIO_Status_UserClockFreqInvalid | -304435 | Requested User Clock frequency does not fall within supported range of frequencies. |
| NIFLEXRIO_Status_BypassUnsupported | -304436 | User Clock configured for Bypass mode does not support Bypass functionality. |
| NIFLEXRIO_Status_UserClockFreqCombinationUnsupported | -304437 | Too many unique User Clock frequencies have been requested. |
| NIFLEXRIO_Status_CableSenseNotSupported | -304438 | CableSense is not supported on this device. |
| NIFLEXRIO_Status_NoCableSenseChannelsEnabled | -304439 | At least one channel must have CableSense Mode set to On Demand before starting CableSense. |
| NIFLEXRIO_Status_CableSenseInProgress | -304440 | CableSense attributes cannot be changed while CableSense is in progress. |
| NIFLEXRIO_Status_I2CInvalidBytesWrittenPointer | -304441 | The pointer provided to store the number of bytes written is invalid. |
| NIFLEXRIO_Status_I2CInvalidBytesReadPointer | -304442 | The pointer provided to store the number of bytes read is invalid. |
| NIFLEXRIO_Status_I2CInvalidWriteData | -304443 | The write data buffer provided is invalid. |
| NIFLEXRIO_Status_I2CInvalidReadData | -304444 | The read data buffer provided is invalid. |
| NIFLEXRIO_Status_I2CMaxWriteSizeExceeded | -304445 | The number of bytes to write exceeds the maximum for this device. |
| NIFLEXRIO_Status_I2CMaxReadSizeExceeded | -304446 | The number of bytes to read exceeds the maximum for this device. |
| NIFLEXRIO_Status_I2CInvalidSlaveAddress | -304447 | The slave address provided is out of the addressable range. |
| NIFLEXRIO_Status_I2CInvalidBusInstance | -304448 | The string provided is not a valid I2C bus instance. |
| NIFLEXRIO_Status_I2CBytesWrittenMismatch | -304449 | The number of bytes written does not match what was expected. |
| NIFLEXRIO_Status_I2CBytesReadMismatch | -304450 | The number of bytes read does not match what was expected. |
| NIFLEXRIO_Status_UserImageNotProgrammed | -304451 | User image has not been programmed. |
| NIFLEXRIO_Status_SessionHasNoBitstream | -304452 | The current session has no bitstream. Open a session with a bitstream to proceed. |
| NIFLEXRIO_Status_CrcMismatch | -304453 | The calculated CRC value does not match the expected CRC value. |
| NIFLEXRIO_Status_FirmwareRevisionMismatch | -304454 | The firmware revision does not match the expected revision. |
| NIFLEXRIO_Status_PoCSafeToDisconnectTimeout | -304455 | The serial channel(s) with power-over-coax did not deenergize within the expected time. |
| NIFLEXRIO_Status_InvalidPortIndex | -304456 | An invalid port index was specified. |
| NIFLEXRIO_Status_InvalidNumberOfPorts | -304457 | An invalid number of ports was specified. |
| NIFLEXRIO_Status_GenericInternalError | -304500 | The software encountered an unspecific error. |
| NIFLEXRIO_Status_UnhandledAttributeType | -304501 | The API attempted to access an attribute with an unhandled data type. |
| NIFLEXRIO_Status_InternalVersionMismatch | -304502 | The API attempted to access an function that has an incompatible version. |
| NIFLEXRIO_Status_UnsupportedTargetFifoType | -304503 | The API attempted to access a FIFO that transfers data in an unsupported format. Only integer FIFO types are supported. |
| NIFLEXRIO_Status_iFifoNotAccessible | -304504 | The requested Instruction FIFO is not accessible. Make sure it is present in this bitfile. |
| NIFLEXRIO_Status_iFifoVersionMismatch | -304505 | The Instruction FIFO version on the device is not compatible with the version supported by the driver. Update the bitfile loaded from flash and/or recompile. |
| NIFLEXRIO_Status_InvalidSensor | -304506 | The requested sensor was not found. |
| NIFLEXRIO_Status_ClipRequiresNewerDriverForSync | -304507 | This bitfile requires a newer driver for synchronization support. |
| NIFLEXRIO_Status_InstructionFIFOCreditError | -304508 | An internal error has occurred. Contact National Instruments technical support at ni.com/support. |
| NIFLEXRIO_Status_UserClockFreqNotFound | -304509 | An internal error has occurred. An invalid User Clock Frequency has been requested. |
| NIFLEXRIO_Status_InvalidPllCapabilities | -304510 | An internal error has occurred. Contact National Instruments technical support at ni.com/support. |
| NIFLEXRIO_Status_InvalidSerialChannelCapabilities | -304511 | An internal error has occurred. Contact National Instruments technical support at ni.com/support. |
| NIFLEXRIO_Status_CalibrationNoTemperature | 304300 | The temperature sensor could not be read and the calibration temperature reading was not updated as part of the calibration procedure. |
| NIFLEXRIO_Status_IoPllUnlockedWarning | 304316 | The IO Module PLL is unlocked. |
| NIFLEXRIO_Status_FixedLogicResetIssue | 304317 | This FPGA was built with a version of target support with a known issue. Rebuild the FPGA with updated target support to ensure data integrity. |
| NIFLEXRIO_Status_MemGuard | 0xFFFFFFFF |  |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga83d26897378d3a1b9bc9b3801fe8a1aa.html language=enus -->
## TOPIC 00026: FlexRIO_PfiConfiguration Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga83d26897378d3a1b9bc9b3801fe8a1aa.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga83d26897378d3a1b9bc9b3801fe8a1aa.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_PfiConfigurationMembersNameValueDescriptionkFlexRIO_PfiConfiguration_Input0Input Mode kFlexRIO_PfiConfiguration_Output1Output Mode

### FlexRIO_PfiConfiguration Enumeration

#### Syntax

enum FlexRIO_PfiConfiguration

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_PfiConfiguration_Input | 0 | Input Mode |
| kFlexRIO_PfiConfiguration_Output | 1 | Output Mode |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga8aa4fd3629d5f7c84fc54e3b513a2d59.html language=enus -->
## TOPIC 00027: FlexRIO_TriggerSensitivity Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga8aa4fd3629d5f7c84fc54e3b513a2d59.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga8aa4fd3629d5f7c84fc54e3b513a2d59.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_TriggerSensitivityMembersNameValueDescriptionkFlexRIO_TriggerSensitivity_RisingEdge2147483647Trigger is active on a transition from low to high kFlexRIO_TriggerSensitivity_FallingEdge2147483646Trigger is active on a transition from high to low kFlexRIO_TriggerSensitivity_HighLevel

### FlexRIO_TriggerSensitivity Enumeration

#### Syntax

enum FlexRIO_TriggerSensitivity

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_TriggerSensitivity_RisingEdge | 2147483647 | Trigger is active on a transition from low to high |
| kFlexRIO_TriggerSensitivity_FallingEdge | 2147483646 | Trigger is active on a transition from high to low |
| kFlexRIO_TriggerSensitivity_HighLevel | 2147483645 | Trigger is active on a high-level input |
| kFlexRIO_TriggerSensitivity_LowLevel | 2147483644 | Trigger is active on a low-level input |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga9390488a62c049438955df1f3ba79b14.html language=enus -->
## TOPIC 00028: FlexRIO_AoChannelStatus Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga9390488a62c049438955df1f3ba79b14.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga9390488a62c049438955df1f3ba79b14.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_AoChannelStatusMembersNameValueDescriptionkFlexRIO_AoChannelStatus_Normal0Channel is in normal state kFlexRIO_AoChannelStatus_Overpower1Channel is shut down due to excessive power consumption kFlexRIO_AoChannelStatus_Overtemperature2Channel is shut down due to excessive temperatur

### FlexRIO_AoChannelStatus Enumeration

#### Syntax

enum FlexRIO_AoChannelStatus

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_AoChannelStatus_Normal | 0 | Channel is in normal state |
| kFlexRIO_AoChannelStatus_Overpower | 1 | Channel is shut down due to excessive power consumption |
| kFlexRIO_AoChannelStatus_Overtemperature | 2 | Channel is shut down due to excessive temperature |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1ga9f58b574195a67f44f943759c7f46f57.html language=enus -->
## TOPIC 00029: FlexRIO_StreamDataFormat Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1ga9f58b574195a67f44f943759c7f46f57.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1ga9f58b574195a67f44f943759c7f46f57.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_StreamDataFormatMembersNameValueDescriptionkFlexRIO_StreamDataFormat_Interleaved0Indicates that data from all channels is interleaved and transferred via a single FIFO. kFlexRIO_StreamDataFormat_FifoPerChannel1Indicates that each channel has its own associated FIFO through which d

### FlexRIO_StreamDataFormat Enumeration

#### Syntax

enum FlexRIO_StreamDataFormat

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_StreamDataFormat_Interleaved | 0 | Indicates that data from all channels is interleaved and transferred via a single FIFO. |
| kFlexRIO_StreamDataFormat_FifoPerChannel | 1 | Indicates that each channel has its own associated FIFO through which data is transferred. |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1gab6aeb15b3f2da27a560c8cf040599b8b.html language=enus -->
## TOPIC 00030: FlexRIO_Csi2NumLanes Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1gab6aeb15b3f2da27a560c8cf040599b8b.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1gab6aeb15b3f2da27a560c8cf040599b8b.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_Csi2NumLanesMembersNameValueDescriptionkFlexRIO_Csi2NumLanes_111 Lane kFlexRIO_Csi2NumLanes_222 Lanes kFlexRIO_Csi2NumLanes_444 Lanes

### FlexRIO_Csi2NumLanes Enumeration

#### Syntax

enum FlexRIO_Csi2NumLanes

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_Csi2NumLanes_1 | 1 | 1 Lane |
| kFlexRIO_Csi2NumLanes_2 | 2 | 2 Lanes |
| kFlexRIO_Csi2NumLanes_4 | 4 | 4 Lanes |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1gac06324a021d3cefd212d4bec36ca9534.html language=enus -->
## TOPIC 00031: FlexRIO_SampleClkSrc Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1gac06324a021d3cefd212d4bec36ca9534.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1gac06324a021d3cefd212d4bec36ca9534.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_SampleClkSrcMembersNameValueDescriptionkFlexRIO_SampleClkSrc_Internal0Internally generated sample clock kFlexRIO_SampleClkSrc_FrontPanel1External clock terminal on the front panel

### FlexRIO_SampleClkSrc Enumeration

#### Syntax

enum FlexRIO_SampleClkSrc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_SampleClkSrc_Internal | 0 | Internally generated sample clock |
| kFlexRIO_SampleClkSrc_FrontPanel | 1 | External clock terminal on the front panel |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1gacc35d12cd7b40371e654b59c9daa8632.html language=enus -->
## TOPIC 00032: FlexRIO_IoModuleRefClkPinSrc Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1gacc35d12cd7b40371e654b59c9daa8632.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1gacc35d12cd7b40371e654b59c9daa8632.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_IoModuleRefClkPinSrcMembersNameValueDescriptionkFlexRIO_IoModuleRefClkPinSrc_Disabled0Disabled kFlexRIO_IoModuleRefClkPinSrc_PXI_Clk101Backplane 10MHz clock kFlexRIO_IoModuleRefClkPinSrc_PXIe_Clk1002Backplane 100MHz clock

### FlexRIO_IoModuleRefClkPinSrc Enumeration

#### Syntax

enum FlexRIO_IoModuleRefClkPinSrc

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_IoModuleRefClkPinSrc_Disabled | 0 | Disabled |
| kFlexRIO_IoModuleRefClkPinSrc_PXI_Clk10 | 1 | Backplane 10MHz clock |
| kFlexRIO_IoModuleRefClkPinSrc_PXIe_Clk100 | 2 | Backplane 100MHz clock |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1gad847552d41497a77efde74aaa0312874.html language=enus -->
## TOPIC 00033: FlexRIO_CableSenseMode Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1gad847552d41497a77efde74aaa0312874.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1gad847552d41497a77efde74aaa0312874.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_CableSenseModeMembersNameValueDescriptionkFlexRIO_CableSenseMode_Disabled0CableSense Disabled kFlexRIO_CableSenseMode_OnDemand1CableSense On Demand

### FlexRIO_CableSenseMode Enumeration

#### Syntax

enum FlexRIO_CableSenseMode

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_CableSenseMode_Disabled | 0 | CableSense Disabled |
| kFlexRIO_CableSenseMode_OnDemand | 1 | CableSense On Demand |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1gae5a0c7cbf49fd4f05828035815259837.html language=enus -->
## TOPIC 00034: FlexRIO_NI6569_RXClockSource Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1gae5a0c7cbf49fd4f05828035815259837.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1gae5a0c7cbf49fd4f05828035815259837.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_NI6569_RXClockSourceMembersNameValueDescriptionkFlexRIO_NI6569_RXClockSource_ExternalClock0External Clock kFlexRIO_NI6569_RXClockSource_TxClock1Transmit Clock

### FlexRIO_NI6569_RXClockSource Enumeration

#### Syntax

enum FlexRIO_NI6569_RXClockSource

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_NI6569_RXClockSource_ExternalClock | 0 | External Clock |
| kFlexRIO_NI6569_RXClockSource_TxClock | 1 | Transmit Clock |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__enums_1gaf337e41f09677c765c2346aa424f1cd7.html language=enus -->
## TOPIC 00035: FlexRIO_Coupling Enumeration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__enums_1gaf337e41f09677c765c2346aa424f1cd7.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__enums_1gaf337e41f09677c765c2346aa424f1cd7.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxenum FlexRIO_CouplingMembersNameValueDescriptionkFlexRIO_Coupling_Ac0kFlexRIO_Coupling_Dc1

### FlexRIO_Coupling Enumeration

#### Syntax

enum FlexRIO_Coupling

#### Members

| Name | Value | Description |
| --- | --- | --- |
| kFlexRIO_Coupling_Ac | 0 |  |
| kFlexRIO_Coupling_Dc | 1 |  |

Parent topic:

NI FlexRIO C Enums

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions.html language=enus -->
## TOPIC 00036: NI FlexRIO C Functions

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: GroupsNoneGroup membersNameDescriptionniFlexRIO_6569_ConfigureRXClocksniFlexRIO_6569_ConfigureTXClocksniFlexRIO_6569_GetRXClockConfigurationniFlexRIO_ClearStreamniFlexRIO_ClearUserImageniFlexRIO_CloseSessionniFlexRIO_CommitniFlexRIO_ConfigureAnalogEdgeTriggerniFlexRIO_ConfigureDigitalStartTriggerniF

### NI FlexRIO C Functions

#### Groups

None

#### Group members

| Name | Description |
| --- | --- |
| niFlexRIO_6569_ConfigureRXClocks |  |
| niFlexRIO_6569_ConfigureTXClocks |  |
| niFlexRIO_6569_GetRXClockConfiguration |  |
| niFlexRIO_ClearStream |  |
| niFlexRIO_ClearUserImage |  |
| niFlexRIO_CloseSession |  |
| niFlexRIO_Commit |  |
| niFlexRIO_ConfigureAnalogEdgeTrigger |  |
| niFlexRIO_ConfigureDigitalStartTrigger |  |
| niFlexRIO_ConfigureForExternalClock |  |
| niFlexRIO_ConfigureForReferenceClock |  |
| niFlexRIO_ConfigureImmediateTrigger |  |
| niFlexRIO_ConfigureStreamEnabledChannels |  |
| niFlexRIO_ConfigureStreamFinite |  |
| niFlexRIO_GetAttributeBoolean |  |
| niFlexRIO_GetAttributeDouble |  |
| niFlexRIO_GetAttributeInt32 |  |
| niFlexRIO_GetAttributeString |  |
| niFlexRIO_GetAttributeUInt64 |  |
| niFlexRIO_GetError |  |
| niFlexRIO_GetFirmwareUpdateProgress |  |
| niFlexRIO_GetSessionReference |  |
| niFlexRIO_OpenDefaultBitfile |  |
| niFlexRIO_OpenSession |  |
| niFlexRIO_PromoteSessionToUserImage |  |
| niFlexRIO_QSFPEnableLowPowerMode |  |
| niFlexRIO_QSFPGetModulePresent |  |
| niFlexRIO_QSFPRead |  |
| niFlexRIO_QSFPResetPorts |  |
| niFlexRIO_QSFPWrite |  |
| niFlexRIO_QueryBitfileFifo |  |
| niFlexRIO_QueryBitfileRegister |  |
| niFlexRIO_ReadCalibrationData |  |
| niFlexRIO_ReadI2C |  |
| niFlexRIO_ReadStream2DF64 |  |
| niFlexRIO_ReadStream2DI16 |  |
| niFlexRIO_ReadStreamF64 |  |
| niFlexRIO_ReadStreamI16 |  |
| niFlexRIO_ResetDspSynchronously |  |
| niFlexRIO_RouteSignal |  |
| niFlexRIO_SetAttributeBoolean |  |
| niFlexRIO_SetAttributeDouble |  |
| niFlexRIO_SetAttributeInt32 |  |
| niFlexRIO_SetAttributeString |  |
| niFlexRIO_SetAttributeUInt64 |  |
| niFlexRIO_SetUserAutoloadFlag |  |
| niFlexRIO_StartCableSense |  |
| niFlexRIO_StartStream |  |
| niFlexRIO_StopCableSense |  |
| niFlexRIO_TransferI2C |  |
| niFlexRIO_UnrouteSignal |  |
| niFlexRIO_UpdateFirmware |  |
| niFlexRIO_UpdateVerificationInformation |  |
| niFlexRIO_WaitForIoReady |  |
| niFlexRIO_WaitForPoCSafeToDisconnect |  |
| niFlexRIO_WaitForTransfer |  |
| niFlexRIO_WriteCalibrationData |  |
| niFlexRIO_WriteI2C |  |

#### Attachments

None

Parent topic:

niflexrioapi.h

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga0109d27d5a214d57728df6cef0d1d1df.html language=enus -->
## TOPIC 00037: niFlexRIO_SetAttributeUInt64

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga0109d27d5a214d57728df6cef0d1d1df.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga0109d27d5a214d57728df6cef0d1d1df.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeUInt64(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeUInt64 attrID, uint64_t value)RemarksSets the value of a 64-bit unsigned integer attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSp

### niFlexRIO_SetAttributeUInt64

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeUInt64(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeUInt64 attrID, uint64_t value)

#### Remarks

Sets the value of a 64-bit unsigned integer attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeUInt64 | Specifies an attribute. |
| value | [in] | uint64_t | Specifies the value to which to set the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga076122cac4cbfb786e36f0c066e85797.html language=enus -->
## TOPIC 00038: niFlexRIO_ReadStream2DI16

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga076122cac4cbfb786e36f0c066e85797.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga076122cac4cbfb786e36f0c066e85797.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStream2DI16(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfWfms, size_t numberOfElements, int16_t *elementArray, FlexRIO_WfmInfo *wfmInfoArray)RemarksReads data from a specified stream.ParametersNameDirectio

### niFlexRIO_ReadStream2DI16

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStream2DI16(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfWfms, size_t numberOfElements, int16_t *elementArray, FlexRIO_WfmInfo *wfmInfoArray)

#### Remarks

Reads data from a specified stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds. |
| numberOfWfms | [in] | size_t | Specifies the number of waveforms to output in elementArray. |
| numberOfElements | [in] | size_t | Specifies the number of elements to include in elementArray. |
| elementArray | [out] | int16_t * | Outputs the data read from the stream. |
| wfmInfoArray | [out] | FlexRIO_WfmInfo * | Contains information about waveforms read from the stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga07ed9d5bec88590e02e86dd4743d91e4.html language=enus -->
## TOPIC 00039: niFlexRIO_GetError

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga07ed9d5bec88590e02e86dd4743d91e4.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga07ed9d5bec88590e02e86dd4743d91e4.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetError(NiFpga_Session session, FlexRIO_Status errorIn, size_t size, char *errorElaboration)RemarksProvides descriptions of errors.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to the currently open NiFpga

### niFlexRIO_GetError

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetError(NiFpga_Session session, FlexRIO_Status errorIn, size_t size, char *errorElaboration)

#### Remarks

Provides descriptions of errors.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| errorIn | [in] | FlexRIO_Status | Specifies the error code returned by a FlexRIO API function. |
| size | [in] | size_t | Specifies the size of the buffer for errorElaboration. |
| errorElaboration | [out] | char * | Outputs the error description. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga0a463bb1fb8b4706b9f41123821bd27d.html language=enus -->
## TOPIC 00040: niFlexRIO_ReadStream2DF64

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga0a463bb1fb8b4706b9f41123821bd27d.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga0a463bb1fb8b4706b9f41123821bd27d.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStream2DF64(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfWfms, size_t numberOfElements, double *elementArray, FlexRIO_WfmInfo *wfmInfoArray)RemarksReads data from a specified stream.ParametersNameDirection

### niFlexRIO_ReadStream2DF64

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStream2DF64(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfWfms, size_t numberOfElements, double *elementArray, FlexRIO_WfmInfo *wfmInfoArray)

#### Remarks

Reads data from a specified stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds. |
| numberOfWfms | [in] | size_t | Specifies the number of waveforms to output in elementArray. |
| numberOfElements | [in] | size_t | Specifies the number of elements to include in elementArray. |
| elementArray | [out] | double * | Outputs the data read from the stream. |
| wfmInfoArray | [out] | FlexRIO_WfmInfo * | Contains information about waveforms read from the stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga0b0a1cc00245c8ae071256e4617b29bd.html language=enus -->
## TOPIC 00041: niFlexRIO_ConfigureForReferenceClock

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga0b0a1cc00245c8ae071256e4617b29bd.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga0b0a1cc00245c8ae071256e4617b29bd.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureForReferenceClock(NiFpga_Session session, FlexRIO_RefClkSrc referenceClockSource)RemarksConfigures the Reference Clock source. You can use this function to set the onboard clock, the PXI backplane clock, or an external clock as the Referen

### niFlexRIO_ConfigureForReferenceClock

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureForReferenceClock(NiFpga_Session session, FlexRIO_RefClkSrc referenceClockSource)

#### Remarks

Configures the Reference Clock source. You can use this function to set the onboard clock, the PXI backplane clock, or an external clock as the Reference Clock.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| referenceClockSource | [in] | FlexRIO_RefClkSrc | Specifies the Reference Clock source. Defined valuesOnboard (1)Specifies the onboard Reference Clock.PXI_Clk10 (2)Specifies a PXI backplane clock.External (3)Specifies an external Reference Clock. |
| Defined values |  |  |  |
| Onboard (1) | Specifies the onboard Reference Clock. |  |  |
| PXI_Clk10 (2) | Specifies a PXI backplane clock. |  |  |
| External (3) | Specifies an external Reference Clock. |  |  |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga1df8c9c167afe540155e92f3fd1eb00e.html language=enus -->
## TOPIC 00042: niFlexRIO_6569_ConfigureRXClocks

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga1df8c9c167afe540155e92f3fd1eb00e.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga1df8c9c167afe540155e92f3fd1eb00e.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_6569_ConfigureRXClocks(NiFpga_Session session, FlexRIO_NI6569_RXClockSource clockSource, FlexRIO_NI6569_Bank bank)RemarksTODO: add documentation for niFlexRIO_6569_ConfigureRXClocks

### niFlexRIO_6569_ConfigureRXClocks

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_6569_ConfigureRXClocks(NiFpga_Session session, FlexRIO_NI6569_RXClockSource clockSource, FlexRIO_NI6569_Bank bank)

#### Remarks

TODO: add documentation for niFlexRIO_6569_ConfigureRXClocks

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga1e730775ab92313deadc31d20cdd4b9a.html language=enus -->
## TOPIC 00043: niFlexRIO_Commit

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga1e730775ab92313deadc31d20cdd4b9a.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga1e730775ab92313deadc31d20cdd4b9a.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_Commit(NiFpga_Session session)RemarksCommits attribute settings to the hardware.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to the currently open NiFpga session. ReturnsFlexRIO_Status

### niFlexRIO_Commit

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_Commit(NiFpga_Session session)

#### Remarks

Commits attribute settings to the hardware.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga25a0d2188f37eeb245e98b224716c1b9.html language=enus -->
## TOPIC 00044: niFlexRIO_ReadStreamI16

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga25a0d2188f37eeb245e98b224716c1b9.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga25a0d2188f37eeb245e98b224716c1b9.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStreamI16(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfElements, int16_t *elementArray, FlexRIO_WfmInfo *wfmInfo)RemarksReads data from a specified stream.ParametersNameDirectionTypeDescriptionsession[in]N

### niFlexRIO_ReadStreamI16

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStreamI16(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfElements, int16_t *elementArray, FlexRIO_WfmInfo *wfmInfo)

#### Remarks

Reads data from a specified stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds. |
| numberOfElements | [in] | size_t | Specifies the number of elements to include in elementArray. |
| elementArray | [out] | int16_t * | Outputs the data read from the stream. |
| wfmInfo | [out] | FlexRIO_WfmInfo * | Contains information about the waveform read from the stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga2cf69430fe59acd492dc086d12960752.html language=enus -->
## TOPIC 00045: niFlexRIO_SetAttributeBoolean

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga2cf69430fe59acd492dc086d12960752.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga2cf69430fe59acd492dc086d12960752.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeBoolean(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeBool attrID, uint32_t value)RemarksSets the value of a Boolean attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the refer

### niFlexRIO_SetAttributeBoolean

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeBoolean(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeBool attrID, uint32_t value)

#### Remarks

Sets the value of a Boolean attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeBool | Specifies an attribute. |
| value | [in] | uint32_t | Specifies the value to which to set the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga2d7f284ab7c34294340e59266e8515ce.html language=enus -->
## TOPIC 00046: niFlexRIO_QueryBitfileRegister

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga2d7f284ab7c34294340e59266e8515ce.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga2d7f284ab7c34294340e59266e8515ce.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QueryBitfileRegister(NiFpga_Session session, const char *name, uint32_t type, uint32_t *offset)RemarksLooks up a control or indicator on the VI diagram in the current session's bitfile and outputs the offset of the register.ParametersNameDirectionT

### niFlexRIO_QueryBitfileRegister

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QueryBitfileRegister(NiFpga_Session session, const char *name, uint32_t type, uint32_t *offset)

#### Remarks

Looks up a control or indicator on the VI diagram in the current session's bitfile and outputs the offset of the register.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| name | [in] | const char * | Specifies the name of control or indicator on the VI diagram to look up in the current session's bitfile. |
| type | [in] | uint32_t | Specifies the type of the queried item. Currently only kFlexRIO_AnyType is supported. |
| offset | [out] | uint32_t * | Outputs the offset of the requested register. This can be passed back to NiFpga entry points for setting and getting values from controls and indicators. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga3408d74f10e6c8c49dd913cee141d02f.html language=enus -->
## TOPIC 00047: niFlexRIO_StartStream

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga3408d74f10e6c8c49dd913cee141d02f.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga3408d74f10e6c8c49dd913cee141d02f.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_StartStream(NiFpga_Session session, int32_t streamInstance)RemarksActivates a stream.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to the currently open NiFpga session. streamInstance[in]int32_tIdentifies an

### niFlexRIO_StartStream

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_StartStream(NiFpga_Session session, int32_t streamInstance)

#### Remarks

Activates a stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga3c7c33bbf909078501d866bcd9e32698.html language=enus -->
## TOPIC 00048: niFlexRIO_CloseSession

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga3c7c33bbf909078501d866bcd9e32698.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga3c7c33bbf909078501d866bcd9e32698.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_CloseSession(NiFpga_Session session, int32_t flags)RemarksCloses the NiFpga session, destroys the session reference, and deallocates resources associated with the session. Call this function once for each unique named session that you have created.

### niFlexRIO_CloseSession

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_CloseSession(NiFpga_Session session, int32_t flags)

#### Remarks

Closes the NiFpga session, destroys the session reference, and deallocates resources associated with the session. Call this function once for each unique named session that you have created.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| flags | [in] | int32_t | Specifies additional NiFpga session attributes. Set this value to 0 or bitwise OR of any of the NiFpga_CloseAttributes. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga3da828e63802cfcb9dd137eeac98ae7f.html language=enus -->
## TOPIC 00049: niFlexRIO_SetAttributeString

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga3da828e63802cfcb9dd137eeac98ae7f.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga3da828e63802cfcb9dd137eeac98ae7f.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeString(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeString attrID, const char *value)RemarksSets the value of a string attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the re

### niFlexRIO_SetAttributeString

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeString(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeString attrID, const char *value)

#### Remarks

Sets the value of a string attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeString | Specifies an attribute. |
| value | [in] | const char * | Specifies the value to which to set the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga3f00f61d6853d9d30aba29c74613a857.html language=enus -->
## TOPIC 00050: niFlexRIO_UpdateVerificationInformation

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga3f00f61d6853d9d30aba29c74613a857.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga3f00f61d6853d9d30aba29c74613a857.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_UpdateVerificationInformation(NiFpga_Session session)RemarksUpdates verification time and verification temperature fields in the device's flash memory to current system time and device temperature, respectively.ParametersNameDirectionTypeDescriptio

### niFlexRIO_UpdateVerificationInformation

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_UpdateVerificationInformation(NiFpga_Session session)

#### Remarks

Updates verification time and verification temperature fields in the device's flash memory to current system time and device temperature, respectively.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga4484b5b68def817e47837d494aca3337.html language=enus -->
## TOPIC 00051: niFlexRIO_QSFPRead

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga4484b5b68def817e47837d494aca3337.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga4484b5b68def817e47837d494aca3337.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPRead(NiFpga_Session session, uint8_t port, uint8_t address, uint8_t *data)ReturnsFlexRIO_Status

### niFlexRIO_QSFPRead

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPRead(NiFpga_Session session, uint8_t port, uint8_t address, uint8_t *data)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga472091bbd9f1f237d55acb5890f5fdff.html language=enus -->
## TOPIC 00052: niFlexRIO_ConfigureForExternalClock

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga472091bbd9f1f237d55acb5890f5fdff.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga472091bbd9f1f237d55acb5890f5fdff.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureForExternalClock(NiFpga_Session session, FlexRIO_ExtClkSrc clockSource, double frequency)RemarksConfigures external clock source and frequency.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to the cu

### niFlexRIO_ConfigureForExternalClock

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureForExternalClock(NiFpga_Session session, FlexRIO_ExtClkSrc clockSource, double frequency)

#### Remarks

Configures external clock source and frequency.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| clockSource | [in] | FlexRIO_ExtClkSrc | Identifies the source of the external Sample Clock. |
| frequency | [in] | double | Specifies the frequency of the external Sample Clock. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga507257f261d1cf366c58a97b00112a2f.html language=enus -->
## TOPIC 00053: niFlexRIO_ConfigureStreamFinite

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga507257f261d1cf366c58a97b00112a2f.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga507257f261d1cf366c58a97b00112a2f.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureStreamFinite(NiFpga_Session session, int32_t streamInstance, uint64_t numberOfSamples)RemarksConfigures a stream to operate in a finite transfer bound by a specified number of samples. Streams configured to operate in a finite transfer wil

### niFlexRIO_ConfigureStreamFinite

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureStreamFinite(NiFpga_Session session, int32_t streamInstance, uint64_t numberOfSamples)

#### Remarks

Configures a stream to operate in a finite transfer bound by a specified number of samples. Streams configured to operate in a finite transfer will autonomously stop after completing the requested number of samples or in response to an error state.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| numberOfSamples | [in] | uint64_t | Specifies the maximum number of samples to transfer. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga5fe00094f0eb88736fc2034c860914cf.html language=enus -->
## TOPIC 00054: niFlexRIO_WaitForIoReady

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga5fe00094f0eb88736fc2034c860914cf.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga5fe00094f0eb88736fc2034c860914cf.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_WaitForIoReady(NiFpga_Session session, int32_t timeoutInMs, uint32_t *ioReady, int32_t *ioError)RemarksPauses execution until the FlexRIO module I/O is ready.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to

### niFlexRIO_WaitForIoReady

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_WaitForIoReady(NiFpga_Session session, int32_t timeoutInMs, uint32_t *ioReady, int32_t *ioError)

#### Remarks

Pauses execution until the FlexRIO module I/O is ready.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds. |
| ioReady | [out] | uint32_t * | Indicates that the I/O is ready. |
| ioError | [out] | int32_t * | Outputs error codes that indicate why the I/O module is not ready. You can retrieve a description for an error code by passing the error code to niFlexRIO_GetError. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga6e1816ee3adce8bcfb8992664e736131.html language=enus -->
## TOPIC 00055: niFlexRIO_ResetDspSynchronously

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga6e1816ee3adce8bcfb8992664e736131.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga6e1816ee3adce8bcfb8992664e736131.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ResetDspSynchronously(NiFpga_Session *sessions, size_t numberOfSessions, int32_t instance, size_t size, char *errorElaboration)RemarksAsserts DSP Reset on the same rising edge of TClk across all sessions.ParametersNameDirectionTypeDescriptionsessio

### niFlexRIO_ResetDspSynchronously

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ResetDspSynchronously(NiFpga_Session *sessions, size_t numberOfSessions, int32_t instance, size_t size, char *errorElaboration)

#### Remarks

Asserts DSP Reset on the same rising edge of TClk across all sessions.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| sessions | [in] | NiFpga_Session * | Specifies an array of sessions to reset. |
| numberOfSessions | [in] | size_t | Specifies the number of sessions in the sessions array. |
| instance | [in] | int32_t | Specifies the DSP Reset instance to reset. |
| size | [in] | size_t | Specifies the size of the buffer for errorElaboration. |
| errorElaboration | [out] | char * | Outputs the error description. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga6e48f256002b09193e170b3841a86dad.html language=enus -->
## TOPIC 00056: niFlexRIO_ConfigureDigitalStartTrigger

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga6e48f256002b09193e170b3841a86dad.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga6e48f256002b09193e170b3841a86dad.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureDigitalStartTrigger(NiFpga_Session session, uint32_t instance, const char *triggerSource, FlexRIO_TriggerSensitivity sensitivity)RemarksConfigures the Start trigger for digital edge triggering.ParametersNameDirectionTypeDescriptionsession[

### niFlexRIO_ConfigureDigitalStartTrigger

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureDigitalStartTrigger(NiFpga_Session session, uint32_t instance, const char *triggerSource, FlexRIO_TriggerSensitivity sensitivity)

#### Remarks

Configures the Start trigger for digital edge triggering.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| instance | [in] | uint32_t | Specifies an instance of a trigger. |
| triggerSource | [in] | const char * | Specifies the trigger source. |
| sensitivity | [in] | FlexRIO_TriggerSensitivity | Specifies digital trigger conditions. Defined values2147483647Rising EdgeTrigger is active on a transition from low to high.2147483646Falling EdgeTrigger is active on a transition from high to low.2147483645High LevelTrigger is active on a high- level input.2147483644Low LevelTrigger is active on a low-level input. |
| Defined values |  |  |  |
| 2147483647 | Rising Edge | Trigger is active on a transition from low to high. |  |
| 2147483646 | Falling Edge | Trigger is active on a transition from high to low. |  |
| 2147483645 | High Level | Trigger is active on a high- level input. |  |
| 2147483644 | Low Level | Trigger is active on a low-level input. |  |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga72a0447d0d353462f63d670639453111.html language=enus -->
## TOPIC 00057: niFlexRIO_WriteCalibrationData

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga72a0447d0d353462f63d670639453111.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga72a0447d0d353462f63d670639453111.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_WriteCalibrationData(NiFpga_Session session, uint32_t offset, const uint8_t *data, size_t size)RemarksWrites calibration data to the FlexRIO device's on-board flash memory. You can find the available calibration storage by retrieving the value of k

### niFlexRIO_WriteCalibrationData

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_WriteCalibrationData(NiFpga_Session session, uint32_t offset, const uint8_t *data, size_t size)

#### Remarks

Writes calibration data to the FlexRIO device's on-board flash memory. You can find the available calibration storage by retrieving the value of kFlexRIO_CalibrationStorageSize.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| offset | [in] | uint32_t | Specifies the byte address in the device's flash memory at which to begin the operation. |
| data | [in] | const uint8_t * | Specifies the data to write to the device's flash memory. |
| size | [in] | size_t | Defines the number of bytes to read from the device's flash memory. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga7f2b8e8c5d69dfb3627deada363eb2ae.html language=enus -->
## TOPIC 00058: niFlexRIO_UpdateFirmware

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga7f2b8e8c5d69dfb3627deada363eb2ae.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga7f2b8e8c5d69dfb3627deada363eb2ae.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_UpdateFirmware(const char *resource, const char *modelName, size_t size, const uint8_t *firmware, uint8_t alwaysOverwrite)RemarksTODO: add documentation for niFlexRIO_UpdateFirmware

### niFlexRIO_UpdateFirmware

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_UpdateFirmware(const char *resource, const char *modelName, size_t size, const uint8_t *firmware, uint8_t alwaysOverwrite)

#### Remarks

TODO: add documentation for niFlexRIO_UpdateFirmware

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga80d8233e29ad1abc47e42f250a3c11c1.html language=enus -->
## TOPIC 00059: niFlexRIO_GetAttributeUInt64

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga80d8233e29ad1abc47e42f250a3c11c1.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga80d8233e29ad1abc47e42f250a3c11c1.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeUInt64(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeUInt64 attrID, uint64_t *value)RemarksQueries the value of a 64-bit unsigned integer attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_Sessi

### niFlexRIO_GetAttributeUInt64

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeUInt64(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeUInt64 attrID, uint64_t *value)

#### Remarks

Queries the value of a 64-bit unsigned integer attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeUInt64 | Specifies an attribute. |
| value | [out] | uint64_t * | Indicates the value of the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga87892e52bbceeff7bfee429fd721b0a9.html language=enus -->
## TOPIC 00060: niFlexRIO_StartCableSense

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga87892e52bbceeff7bfee429fd721b0a9.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga87892e52bbceeff7bfee429fd721b0a9.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_StartCableSense(NiFpga_Session session)ReturnsFlexRIO_Status

### niFlexRIO_StartCableSense

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_StartCableSense(NiFpga_Session session)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga8fdf3c7dbecaaf9a2025854590e2cb4f.html language=enus -->
## TOPIC 00061: niFlexRIO_WriteI2C

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga8fdf3c7dbecaaf9a2025854590e2cb4f.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga8fdf3c7dbecaaf9a2025854590e2cb4f.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_WriteI2C(NiFpga_Session session, const char *busInstanceName, uint16_t slaveAddress, const uint8_t *data, size_t numBytesToWrite, uint8_t repeatedStart, size_t *numBytesWritten)RemarksIssues an I2C write to the specified I2C bus instance.Parameters

### niFlexRIO_WriteI2C

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_WriteI2C(NiFpga_Session session, const char *busInstanceName, uint16_t slaveAddress, const uint8_t *data, size_t numBytesToWrite, uint8_t repeatedStart, size_t *numBytesWritten)

#### Remarks

Issues an I2C write to the specified I2C bus instance.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| busInstanceName | [in] | const char * | Specifies the I2C bus instance to which the read should be issued. |
| slaveAddress | [in] | uint16_t | Specifies the I2C slave address of the device to which the read should be issued. |
| data | [in] | const uint8_t * | Specifies the data to write to the I2C bus. |
| numBytesToWrite | [in] | size_t | Specifies the number of bytes to write to the stream. |
| repeatedStart | [in] | uint8_t | When repeatedStart is true, the I2C master will not send a stop condition at end of the I2C transaction. |
| numBytesWritten | [out] | size_t * | Returns the number of bytes written. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga9ab40d1df2957d5dcf8abd3e0b3bb2de.html language=enus -->
## TOPIC 00062: niFlexRIO_ConfigureImmediateTrigger

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga9ab40d1df2957d5dcf8abd3e0b3bb2de.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga9ab40d1df2957d5dcf8abd3e0b3bb2de.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureImmediateTrigger(NiFpga_Session session, uint32_t instance)RemarksConfigures the device to trigger itself immediately and independently of external signals.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the refere

### niFlexRIO_ConfigureImmediateTrigger

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureImmediateTrigger(NiFpga_Session session, uint32_t instance)

#### Remarks

Configures the device to trigger itself immediately and independently of external signals.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| instance | [in] | uint32_t | Specifies an instance of a trigger. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga9c9e55057c8667cd0ba307ade1b8cc1b.html language=enus -->
## TOPIC 00063: niFlexRIO_ClearUserImage

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga9c9e55057c8667cd0ba307ade1b8cc1b.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga9c9e55057c8667cd0ba307ade1b8cc1b.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ClearUserImage(NiFpga_Session session)RemarksTODO: add documentation for niFlexRIO_ClearUserImage

### niFlexRIO_ClearUserImage

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ClearUserImage(NiFpga_Session session)

#### Remarks

TODO: add documentation for niFlexRIO_ClearUserImage

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1ga9d7cd27d86e47f7bc7d2f1cabbb9d4b9.html language=enus -->
## TOPIC 00064: niFlexRIO_SetUserAutoloadFlag

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1ga9d7cd27d86e47f7bc7d2f1cabbb9d4b9.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1ga9d7cd27d86e47f7bc7d2f1cabbb9d4b9.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_SetUserAutoloadFlag(NiFpga_Session session, uint32_t autoload)RemarksTODO: add documentation for niFlexRIO_SetUserAutoloadFlag

### niFlexRIO_SetUserAutoloadFlag

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_SetUserAutoloadFlag(NiFpga_Session session, uint32_t autoload)

#### Remarks

TODO: add documentation for niFlexRIO_SetUserAutoloadFlag

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaa111201d116d860e844e243d5a31c305.html language=enus -->
## TOPIC 00065: niFlexRIO_QSFPGetModulePresent

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaa111201d116d860e844e243d5a31c305.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaa111201d116d860e844e243d5a31c305.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPGetModulePresent(NiFpga_Session session, uint8_t port, uint32_t *modulePresent)ReturnsFlexRIO_Status

### niFlexRIO_QSFPGetModulePresent

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPGetModulePresent(NiFpga_Session session, uint8_t port, uint32_t *modulePresent)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaa4a76a3c9404fb889ef5e30ad5ce0d74.html language=enus -->
## TOPIC 00066: niFlexRIO_ClearStream

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaa4a76a3c9404fb889ef5e30ad5ce0d74.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaa4a76a3c9404fb889ef5e30ad5ce0d74.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ClearStream(NiFpga_Session session, int32_t streamInstance)RemarksClears samples from the stream.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to the currently open NiFpga session. streamInstance[in]int32_tI

### niFlexRIO_ClearStream

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ClearStream(NiFpga_Session session, int32_t streamInstance)

#### Remarks

Clears samples from the stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaa53e57c838e0e80144f481acfc7bf062.html language=enus -->
## TOPIC 00067: niFlexRIO_QSFPWrite

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaa53e57c838e0e80144f481acfc7bf062.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaa53e57c838e0e80144f481acfc7bf062.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPWrite(NiFpga_Session session, uint8_t port, uint8_t address, uint8_t data)ReturnsFlexRIO_Status

### niFlexRIO_QSFPWrite

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPWrite(NiFpga_Session session, uint8_t port, uint8_t address, uint8_t data)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaa6385249d8f1311a20d5a9ab8bdd6afb.html language=enus -->
## TOPIC 00068: niFlexRIO_GetSessionReference

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaa6385249d8f1311a20d5a9ab8bdd6afb.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaa6385249d8f1311a20d5a9ab8bdd6afb.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetSessionReference(NiFpga_Session session, ViSession *sessionReference)RemarksOutputs a session reference that you can use to identify this session in calls to the NI-TClk API.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifie

### niFlexRIO_GetSessionReference

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetSessionReference(NiFpga_Session session, ViSession *sessionReference)

#### Remarks

Outputs a session reference that you can use to identify this session in calls to the NI-TClk API.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| sessionReference | [out] | ViSession * | Identifies this session. Use this session reference in calls to the NI-TClk API. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaa7e7bc9bff2a2620902103d63392d691.html language=enus -->
## TOPIC 00069: niFlexRIO_QSFPResetPorts

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaa7e7bc9bff2a2620902103d63392d691.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaa7e7bc9bff2a2620902103d63392d691.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPResetPorts(NiFpga_Session session)ReturnsFlexRIO_Status

### niFlexRIO_QSFPResetPorts

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPResetPorts(NiFpga_Session session)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaa97de213b3f4d37c6de85f1b9742a229.html language=enus -->
## TOPIC 00070: niFlexRIO_ReadCalibrationData

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaa97de213b3f4d37c6de85f1b9742a229.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaa97de213b3f4d37c6de85f1b9742a229.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadCalibrationData(NiFpga_Session session, uint32_t offset, uint8_t *data, size_t size)RemarksReads calibration data from the FlexRIO device's on-board flash memory. You can find the available calibration storage by retrieving the value of kFlexRI

### niFlexRIO_ReadCalibrationData

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadCalibrationData(NiFpga_Session session, uint32_t offset, uint8_t *data, size_t size)

#### Remarks

Reads calibration data from the FlexRIO device's on-board flash memory. You can find the available calibration storage by retrieving the value of kFlexRIO_CalibrationStorageSize.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| offset | [in] | uint32_t | Specifies the byte address in the device's flash memory at which to begin the operation. |
| size | [in] | size_t | Defines the number of bytes to read from the device's flash memory. |
| data | [out] | uint8_t * | Returns the data read from the device's flash memory. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaabf206369a43aca92741dc4fab858d45.html language=enus -->
## TOPIC 00071: niFlexRIO_PromoteSessionToUserImage

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaabf206369a43aca92741dc4fab858d45.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaabf206369a43aca92741dc4fab858d45.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_PromoteSessionToUserImage(NiFpga_Session session)RemarksTODO: add documentation for niFlexRIO_PromoteSessionToUserImage

### niFlexRIO_PromoteSessionToUserImage

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_PromoteSessionToUserImage(NiFpga_Session session)

#### Remarks

TODO: add documentation for niFlexRIO_PromoteSessionToUserImage

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gab1c057219df68d183793ae7ac2d39a8b.html language=enus -->
## TOPIC 00072: niFlexRIO_GetAttributeString

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gab1c057219df68d183793ae7ac2d39a8b.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gab1c057219df68d183793ae7ac2d39a8b.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeString(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeString attrID, size_t bufferSize, char *value)RemarksQueries the value of a string attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_Session

### niFlexRIO_GetAttributeString

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeString(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeString attrID, size_t bufferSize, char *value)

#### Remarks

Queries the value of a string attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeString | Specifies an attribute. |
| bufferSize | [in] | size_t | Specifies the string buffer size. |
| value | [out] | char * | Indicates the value of the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gab3bcb387b9dc24dae25dbf54b2ac87a8.html language=enus -->
## TOPIC 00073: niFlexRIO_StopCableSense

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gab3bcb387b9dc24dae25dbf54b2ac87a8.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gab3bcb387b9dc24dae25dbf54b2ac87a8.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_StopCableSense(NiFpga_Session session)ReturnsFlexRIO_Status

### niFlexRIO_StopCableSense

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_StopCableSense(NiFpga_Session session)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gab4bb91c511762354088388d7db836639.html language=enus -->
## TOPIC 00074: niFlexRIO_QSFPEnableLowPowerMode

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gab4bb91c511762354088388d7db836639.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gab4bb91c511762354088388d7db836639.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPEnableLowPowerMode(NiFpga_Session session, uint32_t enable)ReturnsFlexRIO_Status

### niFlexRIO_QSFPEnableLowPowerMode

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QSFPEnableLowPowerMode(NiFpga_Session session, uint32_t enable)

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gab6bdf768eb1bcb1a6b63a82baa6b893d.html language=enus -->
## TOPIC 00075: niFlexRIO_WaitForTransfer

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gab6bdf768eb1bcb1a6b63a82baa6b893d.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gab6bdf768eb1bcb1a6b63a82baa6b893d.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_WaitForTransfer(NiFpga_Session session, int32_t streamInstance, uint64_t waitForNSamples, int32_t timeoutInMs, uint64_t *samplesTransferred, uint8_t *state)RemarksWaits until a specified number of samples have been transferred.ParametersNameDirecti

### niFlexRIO_WaitForTransfer

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_WaitForTransfer(NiFpga_Session session, int32_t streamInstance, uint64_t waitForNSamples, int32_t timeoutInMs, uint64_t *samplesTransferred, uint8_t *state)

#### Remarks

Waits until a specified number of samples have been transferred.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| waitForNSamples | [in] | uint64_t | Specifies the number of samples after the transfer of which execution will resume. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds. |
| samplesTransferred | [out] | uint64_t * | Indicates the actual number of samples transferred in the stream including samples the host has not yet retrieved. |
| state | [out] | uint8_t * | Returns the state of the stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gabbefd8f2441c75713b0a0ef236b5d832.html language=enus -->
## TOPIC 00076: niFlexRIO_SetAttributeDouble

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gabbefd8f2441c75713b0a0ef236b5d832.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gabbefd8f2441c75713b0a0ef236b5d832.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeDouble(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeDouble attrID, double value)RemarksSets the value of a double attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the referen

### niFlexRIO_SetAttributeDouble

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeDouble(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeDouble attrID, double value)

#### Remarks

Sets the value of a double attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeDouble | Specifies an attribute. |
| value | [in] | double | Specifies the value to which to set the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gac0262ca520c1c9402fe0feb13f419a15.html language=enus -->
## TOPIC 00077: niFlexRIO_GetAttributeInt32

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gac0262ca520c1c9402fe0feb13f419a15.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gac0262ca520c1c9402fe0feb13f419a15.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeInt32(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeInt32 attrID, int32_t *value)RemarksQueries the value of a 32-bit integer attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies

### niFlexRIO_GetAttributeInt32

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeInt32(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeInt32 attrID, int32_t *value)

#### Remarks

Queries the value of a 32-bit integer attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeInt32 | Specifies an attribute. |
| value | [out] | int32_t * | Indicates the value of the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gac0b4fe0f5967f04ce6a513d324809827.html language=enus -->
## TOPIC 00078: niFlexRIO_GetAttributeBoolean

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gac0b4fe0f5967f04ce6a513d324809827.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gac0b4fe0f5967f04ce6a513d324809827.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeBoolean(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeBool attrID, uint32_t *value)RemarksQueries the value of a Boolean attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the r

### niFlexRIO_GetAttributeBoolean

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeBoolean(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeBool attrID, uint32_t *value)

#### Remarks

Queries the value of a Boolean attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeBool | Specifies an attribute. |
| value | [out] | uint32_t * | Indicates the value of the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gac21ec8a592fe5e5b50bd4d1a382d6ade.html language=enus -->
## TOPIC 00079: niFlexRIO_SetAttributeInt32

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gac21ec8a592fe5e5b50bd4d1a382d6ade.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gac21ec8a592fe5e5b50bd4d1a382d6ade.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeInt32(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeInt32 attrID, int32_t value)RemarksSets the value of a 32-bit integer attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the

### niFlexRIO_SetAttributeInt32

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_SetAttributeInt32(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeInt32 attrID, int32_t value)

#### Remarks

Sets the value of a 32-bit integer attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeInt32 | Specifies an attribute. |
| value | [in] | int32_t | Specifies the value to which to set the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gac23f69e09c11014b61c27572b795f511.html language=enus -->
## TOPIC 00080: niFlexRIO_ReadI2C

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gac23f69e09c11014b61c27572b795f511.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gac23f69e09c11014b61c27572b795f511.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadI2C(NiFpga_Session session, const char *busInstanceName, uint16_t slaveAddress, uint8_t *data, size_t numBytesToRead, uint8_t repeatedStart, size_t *numBytesRead)RemarksIssues an I2C read to the specified I2C bus instance.ParametersNameDirectio

### niFlexRIO_ReadI2C

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadI2C(NiFpga_Session session, const char *busInstanceName, uint16_t slaveAddress, uint8_t *data, size_t numBytesToRead, uint8_t repeatedStart, size_t *numBytesRead)

#### Remarks

Issues an I2C read to the specified I2C bus instance.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| busInstanceName | [in] | const char * | Specifies the I2C bus instance to which the read should be issued. |
| slaveAddress | [in] | uint16_t | Specifies the I2C slave address of the device to which the read should be issued. |
| data | [out] | uint8_t * | returns the data read from the I2C bus. |
| numBytesToRead | [in] | size_t | Specifies the number of bytes to be read. |
| repeatedStart | [in] | uint8_t | When repeatedStart is true, the I2C master will not send a stop condition at end of the I2C transaction. |
| numBytesRead | [out] | size_t * | Returns the number of bytes read. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gac5ac979f139a2f712c94396d64b67175.html language=enus -->
## TOPIC 00081: niFlexRIO_OpenDefaultBitfile

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gac5ac979f139a2f712c94396d64b67175.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gac5ac979f139a2f712c94396d64b67175.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxniFlexRIO_OpenDefaultBitfile(resourceName, flags, newSession) niFlexRIO_OpenSession(resourceName, NULL, flags, newSession)

### niFlexRIO_OpenDefaultBitfile

#### Syntax

niFlexRIO_OpenDefaultBitfile(resourceName, flags, newSession) niFlexRIO_OpenSession(resourceName, NULL, flags, newSession)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gac85b9652fd212d8a057c939381315bee.html language=enus -->
## TOPIC 00082: niFlexRIO_WaitForPoCSafeToDisconnect

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gac85b9652fd212d8a057c939381315bee.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gac85b9652fd212d8a057c939381315bee.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_WaitForPoCSafeToDisconnect(NiFpga_Session session, const char *channels, int32_t timeoutInMs, size_t bufferSize, char *channelsTimedOutIn)RemarksWaits and blocks until specified channels with power-over-coax are safe to disconnect.ParametersNameDir

### niFlexRIO_WaitForPoCSafeToDisconnect

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_WaitForPoCSafeToDisconnect(NiFpga_Session session, const char *channels, int32_t timeoutInMs, size_t bufferSize, char *channelsTimedOutIn)

#### Remarks

Waits and blocks until specified channels with power-over-coax are safe to disconnect.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| channels | [in] | const char * | Specifies the channels to wait until safe to disconnect. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds to wait until safe to disconnect. A value of -1 indicates to wait indefinitely |
| bufferSize | [in] | size_t | Specifies the string buffer size for the timed out channels. |
| channelsTimedOutIn | [out] | char * | Indicates which channels failed to deenergize. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gad1c9dfe94567fe7fee27e3bd94b527d4.html language=enus -->
## TOPIC 00083: niFlexRIO_TransferI2C

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gad1c9dfe94567fe7fee27e3bd94b527d4.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gad1c9dfe94567fe7fee27e3bd94b527d4.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_TransferI2C(NiFpga_Session session, const char *busInstanceName, uint16_t slaveAddress, const uint8_t *writeData, size_t numBytesToWrite, uint8_t *readData, size_t numBytesToRead, uint8_t repeatedStart, size_t *numBytesWritten, size_t *numBytesRead

### niFlexRIO_TransferI2C

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_TransferI2C(NiFpga_Session session, const char *busInstanceName, uint16_t slaveAddress, const uint8_t *writeData, size_t numBytesToWrite, uint8_t *readData, size_t numBytesToRead, uint8_t repeatedStart, size_t *numBytesWritten, size_t *numBytesRead)

#### Remarks

Issues an I2C write, without a stop condition, before issuing an I2C read.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| busInstanceName | [in] | const char * | Specifies the I2C bus instance to which the read should be issued. |
| slaveAddress | [in] | uint16_t | Specifies the I2C slave address of the device to which the read should be issued. |
| writeData | [in] | const uint8_t * | Specifies the data to write to the I2C bus. |
| numBytesToWrite | [in] | size_t | Specifies the number of bytes to write to the stream. |
| readData | [out] | uint8_t * | Returns the data read from the I2C bus. |
| numBytesToRead | [in] | size_t | Specifies the number of bytes to be read. |
| repeatedStart | [in] | uint8_t | When repeatedStart is true, the I2C master will not send a stop condition at end of the I2C transaction. |
| numBytesWritten | [out] | size_t * | Returns the number of bytes written. |
| numBytesRead | [out] | size_t * | Returns the number of bytes read. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gadfccf1468bdc560f9648d28c8551d338.html language=enus -->
## TOPIC 00084: niFlexRIO_ConfigureStreamEnabledChannels

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gadfccf1468bdc560f9648d28c8551d338.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gadfccf1468bdc560f9648d28c8551d338.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureStreamEnabledChannels(NiFpga_Session session, int32_t streamInstance, const char *channelsEnabled, int32_t *channelCount)RemarksConfigures which channels are enabled for a specified stream.ParametersNameDirectionTypeDescriptionsession[in]N

### niFlexRIO_ConfigureStreamEnabledChannels

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureStreamEnabledChannels(NiFpga_Session session, int32_t streamInstance, const char *channelsEnabled, int32_t *channelCount)

#### Remarks

Configures which channels are enabled for a specified stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| channelsEnabled | [in] | const char * | Specifies the channels to enable for the specified stream. |
| channelCount | [out] | int32_t * | Indicates the total number of channels parsed during execution of this function. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gae1d760416b468b7b92e10ddf304d8143.html language=enus -->
## TOPIC 00085: niFlexRIO_6569_GetRXClockConfiguration

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gae1d760416b468b7b92e10ddf304d8143.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gae1d760416b468b7b92e10ddf304d8143.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_6569_GetRXClockConfiguration(NiFpga_Session session, FlexRIO_NI6569_RXClockSource *clockSource, FlexRIO_NI6569_Bank bank)RemarksTODO: add documentation for niFlexRIO_6569_GetRXClockConfiguration

### niFlexRIO_6569_GetRXClockConfiguration

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_6569_GetRXClockConfiguration(NiFpga_Session session, FlexRIO_NI6569_RXClockSource *clockSource, FlexRIO_NI6569_Bank bank)

#### Remarks

TODO: add documentation for niFlexRIO_6569_GetRXClockConfiguration

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gae2aca18322e4fbac60128063dd857d93.html language=enus -->
## TOPIC 00086: niFlexRIO_UnrouteSignal

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gae2aca18322e4fbac60128063dd857d93.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gae2aca18322e4fbac60128063dd857d93.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_UnrouteSignal(NiFpga_Session session, FlexRIO_RouteTicket routeTicket)RemarksUnroutes a signal specified by a route ticket.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the reference to the currently open NiFpga session.

### niFlexRIO_UnrouteSignal

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_UnrouteSignal(NiFpga_Session session, FlexRIO_RouteTicket routeTicket)

#### Remarks

Unroutes a signal specified by a route ticket.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| routeTicket | [in] | FlexRIO_RouteTicket | Identifies a signal route. The route ticket originates from niFlexRIO_RouteSignal. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaf0c1e969c56a312bd2cd0c44aba40c5f.html language=enus -->
## TOPIC 00087: niFlexRIO_OpenSession

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaf0c1e969c56a312bd2cd0c44aba40c5f.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaf0c1e969c56a312bd2cd0c44aba40c5f.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_OpenSession(const char *const resourceName, const char *bitfile, int32_t flags, NiFpga_Session *newSession)RemarksOpens a session to the FlexRIO device using a specified bitfile and creates an NiFpga session reference that you can use to identify t

### niFlexRIO_OpenSession

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_OpenSession(const char *const resourceName, const char *bitfile, int32_t flags, NiFpga_Session *newSession)

#### Remarks

Opens a session to the FlexRIO device using a specified bitfile and creates an NiFpga session reference that you can use to identify this session in subsequent FlexRIO API function calls.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| resourceName | [in] | const char *const | Specifies the resource name of the FlexRIO device. |
| bitfile | [in] | const char * | Specifies the FPGA image to load to the FPGA. |
| flags | [in] | int32_t | Specifies additional NiFpga session attributes. Set this value to 0 or bitwise OR of any of the NiFpga_OpenAttributes. |
| newSession | [out] | NiFpga_Session * | Outputs the NiFpga session reference. Destroy this session reference by calling niFlexRIO_CloseSession when the session is no longer needed. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaf77a596b024d6be4eedcb47cbd138fb8.html language=enus -->
## TOPIC 00088: niFlexRIO_GetFirmwareUpdateProgress

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaf77a596b024d6be4eedcb47cbd138fb8.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaf77a596b024d6be4eedcb47cbd138fb8.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetFirmwareUpdateProgress(const char *resource, uint32_t *progress, uint8_t *isUpdateInProgress, uint8_t *updateFailed)RemarksTODO: add documentation for niFlexRIO_GetFirmwareUpdateProgress

### niFlexRIO_GetFirmwareUpdateProgress

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetFirmwareUpdateProgress(const char *resource, uint32_t *progress, uint8_t *isUpdateInProgress, uint8_t *updateFailed)

#### Remarks

TODO: add documentation for niFlexRIO_GetFirmwareUpdateProgress

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaf788d195731b9ff436c6dd93a58c2731.html language=enus -->
## TOPIC 00089: niFlexRIO_RouteSignal

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaf788d195731b9ff436c6dd93a58c2731.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaf788d195731b9ff436c6dd93a58c2731.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_RouteSignal(NiFpga_Session session, const char *source, const char *destination, FlexRIO_RouteTicket *routeTicket)RemarksRoutes a signal from a specified source to a specified destination and creates a route ticket that identifies the route.Paramet

### niFlexRIO_RouteSignal

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_RouteSignal(NiFpga_Session session, const char *source, const char *destination, FlexRIO_RouteTicket *routeTicket)

#### Remarks

Routes a signal from a specified source to a specified destination and creates a route ticket that identifies the route.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| source | [in] | const char * | Specifies the source of the signal to route. |
| destination | [in] | const char * | Specifies the destination to which to route the signal. |
| routeTicket | [out] | FlexRIO_RouteTicket * | Identifies a signal route. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaf7c85572325d4a3063a8214af354a77e.html language=enus -->
## TOPIC 00090: niFlexRIO_GetAttributeDouble

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaf7c85572325d4a3063a8214af354a77e.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaf7c85572325d4a3063a8214af354a77e.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeDouble(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeDouble attrID, double *value)RemarksQueries the value of a double attribute.ParametersNameDirectionTypeDescriptionsession[in]NiFpga_SessionSpecifies the ref

### niFlexRIO_GetAttributeDouble

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_GetAttributeDouble(NiFpga_Session session, const char *repeatedCapability, FlexRIO_AttributeDouble attrID, double *value)

#### Remarks

Queries the value of a double attribute.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| repeatedCapability | [in] | const char * | Specifies a repeated capability. If attrID is based on a repeated capability, pass a repeated capability identifier. If attrID is not based on a repeated capability, pass NULL or an empty string. |
| attrID | [in] | FlexRIO_AttributeDouble | Specifies an attribute. |
| value | [out] | double * | Indicates the value of the attribute. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gafb53e936355fa7f2cfbdcc9684884d99.html language=enus -->
## TOPIC 00091: niFlexRIO_6569_ConfigureTXClocks

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gafb53e936355fa7f2cfbdcc9684884d99.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gafb53e936355fa7f2cfbdcc9684884d99.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_6569_ConfigureTXClocks(NiFpga_Session session, FlexRIO_NI6569_TXClockSource clockSource, double frequency)RemarksTODO: add documentation for niFlexRIO_6569_ConfigureTXClocks

### niFlexRIO_6569_ConfigureTXClocks

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_6569_ConfigureTXClocks(NiFpga_Session session, FlexRIO_NI6569_TXClockSource clockSource, double frequency)

#### Remarks

TODO: add documentation for niFlexRIO_6569_ConfigureTXClocks

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gafc94257450252074d89468d4cdf6f51e.html language=enus -->
## TOPIC 00092: niFlexRIO_ReadStreamF64

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gafc94257450252074d89468d4cdf6f51e.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gafc94257450252074d89468d4cdf6f51e.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStreamF64(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfElements, double *elementArray, FlexRIO_WfmInfo *wfmInfo)RemarksReads data from a specified stream.ParametersNameDirectionTypeDescriptionsession[in]Ni

### niFlexRIO_ReadStreamF64

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ReadStreamF64(NiFpga_Session session, int32_t streamInstance, int32_t timeoutInMs, size_t numberOfElements, double *elementArray, FlexRIO_WfmInfo *wfmInfo)

#### Remarks

Reads data from a specified stream.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| streamInstance | [in] | int32_t | Identifies an instance of a stream. |
| timeoutInMs | [in] | int32_t | Specifies a time limit in milliseconds. |
| numberOfElements | [in] | size_t | Specifies the number of elements to include in elementArray. |
| elementArray | [out] | double * | Outputs the data read from the stream. |
| wfmInfo | [out] | FlexRIO_WfmInfo * | Contains information about the waveform read from the stream. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gafccf5b3225c3e1764435875f6bd83d58.html language=enus -->
## TOPIC 00093: niFlexRIO_ConfigureAnalogEdgeTrigger

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gafccf5b3225c3e1764435875f6bd83d58.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gafccf5b3225c3e1764435875f6bd83d58.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureAnalogEdgeTrigger(NiFpga_Session session, uint32_t instance, const char *channel, uint32_t rising, double level, double hysteresis)RemarksConfigures the Start trigger for analog edge triggering.ParametersNameDirectionTypeDescriptionsession

### niFlexRIO_ConfigureAnalogEdgeTrigger

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_ConfigureAnalogEdgeTrigger(NiFpga_Session session, uint32_t instance, const char *channel, uint32_t rising, double level, double hysteresis)

#### Remarks

Configures the Start trigger for analog edge triggering.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| instance | [in] | uint32_t | Specifies an instance of a trigger. |
| channel | [in] | const char * | Specifies the channel to monitor for trigger conditions. |
| rising | [in] | uint32_t | Specifies whether to trigger on a rising edge. If this value is false, the device will trigger on a falling edge. |
| level | [in] | double | Specifies the trigger level in volts. |
| hysteresis | [in] | double | Specifies the size of the hysteresis window on either side of level in volts. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__functions_1gaff1639287e1086d0bc57a985afd55a4e.html language=enus -->
## TOPIC 00094: niFlexRIO_QueryBitfileFifo

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__functions_1gaff1639287e1086d0bc57a985afd55a4e.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__functions_1gaff1639287e1086d0bc57a985afd55a4e.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: SyntaxFlexRIO_Status _NIFLEXRIOAPI_EXPORT niFlexRIO_QueryBitfileFifo(NiFpga_Session session, const char *name, uint32_t type, uint32_t *offset)RemarksLooks up a FIFO on the VI diagram in the current session's bitfile and outputs the offset of the register.ParametersNameDirectionTypeDescriptionsessio

### niFlexRIO_QueryBitfileFifo

#### Syntax

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html) _NIFLEXRIOAPI_EXPORT niFlexRIO_QueryBitfileFifo(NiFpga_Session session, const char *name, uint32_t type, uint32_t *offset)

#### Remarks

Looks up a FIFO on the VI diagram in the current session's bitfile and outputs the offset of the register.

#### Parameters

| Name | Direction | Type | Description |
| --- | --- | --- | --- |
| session | [in] | NiFpga_Session | Specifies the reference to the currently open NiFpga session. |
| name | [in] | const char * | Specifies the name of the FIFO on the VI diagram to look up in the current session's bitfile. |
| type | [in] | uint32_t | Specifies the type of the queried item. Currently only kFlexRIO_AnyType is supported. |
| offset | [out] | uint32_t * | Outputs the offset of the requested register. This can be passed back to NiFpga entry points for interacting with FPGA FIFOs. |

#### Returns

[FlexRIO_Status](group__defines_1ga11774adc54521a34b07d472d70996418.html)

Parent topic:

NI FlexRIO C Functions

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=group__root__niflexrioapi.html language=enus -->
## TOPIC 00095: niflexrioapi.h

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `group__root__niflexrioapi.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/group__root__niflexrioapi.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This is the landing page for FlexRIO Integrated IO C API reference. GroupsNI FlexRIO C AttributesNI FlexRIO C DefinesNI FlexRIO C EnumsNI FlexRIO C FunctionsGroup membersNoneAttachmentsNone

### niflexrioapi.h

This is the landing page for FlexRIO Integrated IO C API reference.

#### Groups

- NI FlexRIO C Attributes
- NI FlexRIO C Defines
- NI FlexRIO C Enums
- NI FlexRIO C Functions

#### Group members

None

#### Attachments

None

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=struct_flex_r_i_o___wfm_info.html language=enus -->
## TOPIC 00096: FlexRIO_WfmInfo

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `struct_flex_r_i_o___wfm_info.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/struct_flex_r_i_o___wfm_info.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: This structure is used by stream read endpoints to return additional information about the waveform. Syntaxstruct FlexRIO_WfmInfo { double absoluteInitialXLower; double absoluteInitialXUpper; uint64_t actualNumSamples; double dt; double gain; double offset; double relativeInitialX; double reserved1;

### FlexRIO_WfmInfo

This structure is used by stream read endpoints to return additional information about the waveform.

#### Syntax

```text
struct FlexRIO_WfmInfo {
  double absoluteInitialXLower;
  double absoluteInitialXUpper;
  uint64_t actualNumSamples;
  double dt;
  double gain;
  double offset;
  double relativeInitialX;
  double reserved1;
  double reserved2;
  uint64_t reserved3;
}
```

#### Members

| Name | Description |
| --- | --- |
| absoluteInitialXLower | Residual difference in seconds from absoluteInitialXUpper |
| absoluteInitialXUpper | Difference in seconds from an arbitrary starting point |
| actualNumSamples | Indicates the number of samples stored in this waveform |
| dt | Difference in seconds between samples |
| gain | Difference in volts between adjacent elements |
| offset | Difference in volts between the scaled waveform value '0' and zero volts |
| relativeInitialX | Difference in seconds from the trigger position |
| reserved1 | Reserved for future use. |
| reserved2 | Reserved for future future use. |
| reserved3 | Reserved for future use. |

#### Remarks

The API is capable of returning less data than requested for a variety of reasons. The actualNumSamples will reflect the amount written to the user's buffer for this waveform. However, if the function returns any error other than a timeout, this field may not contain the correct information.

In the event of a timeout, all fields that can be filled out shall be.

The timestamps absoluteInitialX will be 0 in situations where it is unsupported. Otherwise, the value will be a time offset to the first sample in this read that is how far that sample is in time from an arbitrary starting point. This can be used to compare times across different streaming acquisitions, as long as the timing source is maintained (ie: the clock isn't reconfigured).

There are two absoluteInitialX values (upper and lower). The actual time is the sum of these two values. However, because of the precision in doubles (about 15 significant decimal digits), one double can't contain enough information to convey this information over a long period of time. This method is chosen to ensure portability to all programming environments.

The timestamp relativeInitialX will be 0 in situations where it is unsupported. Otherwise, the value will be a time offset to the first sample in this read that is how far that sample is in time from the reference point. The reference point is typically the start of this waveform. The relativeInitialX has the same limitations as absoluteInitialX in that the precision can roll off, however since it is always relative to the trigger event, it is uncommon for this to matter in practice.

In practice, relativeInitialX is supported in all cases. But if it were not, the value shall be zero.

If dt == 0, then the driver does not know the dt. If gain == 0, then the driver does not know the gain (and offset).

For integer output data, the scaling coefficients to transform binary data into scaled data (typically volts), are indicated as data_in_volts = (data[i] * gain) + offset;

For floating point data, the scaling coefficients are still the same, but they can be used in reverse to recover the unscaled data.

Do not reference the reserved fields. If they become used some day, then the name will change to reflect that and your code will no longer compile.

Parent topic:

NI FlexRIO C Defines

<!--NI_TOPIC bundle=flexrio-integrated-io-c-api-ref path=struct_n_i_complex_i16__struct.html language=enus -->
## TOPIC 00097: NIComplexI16_struct

- bundle_id: `flexrio-integrated-io-c-api-ref`
- source_path: `struct_n_i_complex_i16__struct.html`
- source_url: https://docs-be.ni.com/bundle/flexrio-integrated-io-c-api-ref/raw/resource/enus/struct_n_i_complex_i16__struct.html
- document_id: `flexrio-integrated-io-c-api-ref`
- page_type: `leaf`
- content_type: `reference`
- source_description: Syntaxstruct NIComplexI16_struct { int16_t imaginary; int16_t real; }MembersNameDescriptionimaginaryQ realI

### NIComplexI16_struct

#### Syntax

```text
struct NIComplexI16_struct {
  int16_t imaginary;
  int16_t real;
}
```

#### Members

| Name | Description |
| --- | --- |
| imaginary | Q |
| real | I |

Parent topic:

NI FlexRIO C Defines
