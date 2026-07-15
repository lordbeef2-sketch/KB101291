# NI DOCUMENT BUNDLE: ni-fgen-.net-4.0-api-overview

<!--NI_BUNDLE_CHUNK bundle=ni-fgen-.net-4.0-api-overview start=1 end=20 -->
<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=creating-application-ni-fgen-.net-class.html language=enus -->
## TOPIC 00001: Creating an Application with the NI-FGEN .NET Class Library

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `creating-application-ni-fgen-.net-class.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/creating-application-ni-fgen-.net-class.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: To develop an NI-FGEN application using the NI-FGEN .NET class library, follow these general steps. Open an existing or new project file. Load the NI-FGEN .NET class library (NationalInstruments.ModularInstruments.NIFgen.Fx40.dll or NationalInstruments.ModularInstruments.NIFgen.Fx45.dll). Use the hi

Creating an Application with the NI-FGEN .NET Class Library

To develop an NI-FGEN application using the NI-FGEN .NET class library, follow these general steps.

#### NI-FGEN Example Programs for the .NET Class Library

1. Open an existing or new project file.
2. Load the NI-FGEN .NET class library ( NationalInstruments.ModularInstruments.NIFgen.Fx40.dll or 
 NationalInstruments.ModularInstruments.NIFgen.Fx45.dll ).
3. Use the hierarchy tree to navigate the sub-objects of NIFgen . The NIFgen object represents a session with your signal generator. All FGEN functionality will exist in NIFgen or one of its sub-objects.

Start

»

All Programs

»

National Instruments

»

NI-FGEN

»

NI-FGEN Examples

Note

Parent topic:

NI-FGEN .NET Class Library Help

Related information:

- NI-FGEN .NET Class Library
- NIFgen Class

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=netfgenexceptions.html language=enus -->
## TOPIC 00002: NI-FGEN Exceptions

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `netfgenexceptions.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/netfgenexceptions.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: If the NI-FGEN .NET API encounters an error, a .NET exception will be thrown. If this error occurs in the underlying C driver, an exception will be thrown with an inner exception of IviCDriverException. This IviCDriverException will contain an error code and error message documenting the error.

NI-FGEN Exceptions

If the NI-FGEN .NET API encounters an error, a .NET exception will be thrown. If this error occurs in the underlying C driver, an exception will be thrown with an inner exception of 
 IviCDriverException. This 
 IviCDriverException will contain an error code and error message documenting the error.

Parent topic:

NI-FGEN .NET API Tutorial

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=netfgenmain.html language=enus -->
## TOPIC 00003: NI-FGEN .NET Class Library Help

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `netfgenmain.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/netfgenmain.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: You can use the NI-FGEN .NET class library to configure and control NI signal generators in your applications. For additional information on developing applications using NI drivers and the .NET Framework, refer to ni.com/mstudio or visit ni.com/info and enter the Info Code NIdotNET. You can find ex

NI-FGEN .NET Class Library Help

You can use the NI-FGEN .NET class library to configure and control NI signal generators in your applications.

For additional information on developing applications using NI drivers and the .NET Framework, refer to 
 [ni.com/mstudio](http://www.ni.com/mstudio/) or visit 
 [ni.com/info](http://www.ni.com/info/) and enter the Info Code 
 NIdotNET.

You can find example applications by selecting 
 Start»All Programs»National Instruments»NI-FGEN»NI-FGEN Examples in the Start menu.

Note

Note

Measurement Studio Installer Builder

setup projects

merge modules

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=ni-fgen-.net-api-tutorial.html language=enus -->
## TOPIC 00004: NI-FGEN .NET API Tutorial

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `ni-fgen-.net-api-tutorial.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/ni-fgen-.net-api-tutorial.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: This tutorial explains how to complete the following programming steps: Initialize the session Configure the session Initiate generation Abort generation Close the session Retrieve error information After you understand the programming process outlined in this tutorial, you can find advanced informa

NI-FGEN .NET API Tutorial

This tutorial explains how to complete the following programming steps:

#### Example Programs

1. Initialize the session
2. Configure the session
3. Initiate generation
4. Abort generation
5. Close the session
6. Retrieve error information

After you understand the programming process outlined in this tutorial, you can find advanced information about programming specific signal generator features with the NI-FGEN .NET class library in the [Features](https://SIGNGENHELP.CHM::/PROGRAMMING_FEATURES.HTML) section.

Start

»

All Programs

»

National Instruments

»

NI-FGEN

»

NI-FGEN Examples

Note

Parent topic:

NI-FGEN .NET Class Library Help

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=ni-fgen-c-api-ni-fgen-.net-api-map.html language=enus -->
## TOPIC 00005: NI-FGEN C API to NI-FGEN .NET API Map

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `ni-fgen-c-api-ni-fgen-.net-api-map.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/ni-fgen-c-api-ni-fgen-.net-api-map.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-FGEN .NET API members to the corresponding NI-FGEN C API members. All .NET members are in the NationalInstruments.ModularInstruments.NIFgen namespace. .NET Entry Point C Entry Point FgenOutput.OutputMode NIFGEN_ATTR_OUTPUT_MODE FgenOutput.GetEnabled(string channelName

NI-FGEN C API to NI-FGEN .NET API Map

The following table maps the NI-FGEN .NET API members to the corresponding NI-FGEN C API members. All .NET members are in the NationalInstruments.ModularInstruments.NIFgen namespace.

| .NET Entry Point | C Entry Point |
| --- | --- |
| FgenOutput.OutputMode | NIFGEN_ATTR_OUTPUT_MODE |
| FgenOutput.GetEnabled(string channelName) FgenOutput.SetEnabled(string channelName, bool enabled) | NIFGEN_ATTR_OUTPUT_ENABLED |
| FgenOutput.GetDigitalGain(string channelName) FgenOutput.SetDigitalGain(string channelName, double digitalGain) | NIFGEN_ATTR_DIGITAL_GAIN |
| FgenOutput.GetAnalogPath(string channelName) FgenOutput.SetAnalogPath(string channelName, AnalogPath analogPath) | NIFGEN_ATTR_ANALOG_PATH |
| FgenOutput.GetLoadImpedance(string channelName) FgenOutput.SetLoadImpedance(string channelName, double impedance) | NIFGEN_ATTR_LOAD_IMPEDANCE |
| FgenOutput.GetImpedance(string channelName) FgenOutput.SetImpedance(string channelName, double impedance) | NIFGEN_ATTR_OUTPUT_IMPEDANCE |
| FgenOutput.GetTerminalConfiguration(string channelName) FgenOutput.SetTerminalConfiguration(string channelName, TerminalConfiguration configuration) | NIFGEN_ATTR_TERMINAL_CONFIGURATION |
| FgenOutput.GetCommonModeOffset(string channelName) FgenOutput.SetCommonModeOffset(string channelName, double commonModeOffset) | NIFGEN_ATTR_COMMON_MODE_OFFSET |
| FgenOutput.GetChannelDelay(string channelName) FgenOutput.SetChannelDelay(string channelName, double channelDelay) | NIFGEN_ATTR_CHANNEL_DELAY |
| FgenOutputFilter.GetAnalogFilterEnabled(string channelName) FgenOutputFilter.SetAnalogFilterEnabled(string channelName, bool enabled) | NIFGEN_ATTR_ANALOG_FILTER_ENABLED |
| FgenOutputFilter.GetDigitalFilterEnabled(string channelName) FgenOutputFilter.SetDigitalFilterEnabled(string channelName, bool enabled) | NIFGEN_ATTR_DIGITAL_FILTER_ENABLED |
| FgenOutputFilter.GetDigitalFilterInterpolationFactor(string channelName) FgenOutputFilter.SetDigitalFilterInterpolationFactor(string channelName, double interpolationFactor) | NIFGEN_ATTR_DIGITAL_FILTER_INTERPOLATION_FACTOR |
| FgenOutputFilter.GetFlatnessCorrectionEnabled(string channelName) FgenOutputFilter.SetFlatnessCorrectionEnabled(string channelName, bool enabled) | NIFGEN_ATTR_FLATNESS_CORRECTION_ENABLED |
| FgenOutputDataMask.GetAnalogDataMask(string channelName) FgenOutputDataMask.SetAnalogDataMask(string channelName, int analogDataMask) | NIFGEN_ATTR_ANALOG_DATA_MASK |
| FgenOutputDataMask.GetAnalogStaticValue(string channelName) FgenOutputDataMask.SetAnalogStaticValue(string channelName, int analogStaticValue) | NIFGEN_ATTR_ANALOG_STATIC_VALUE |
| FgenOutputDataMask.GetDigitalDataMask(string channelName) FgenOutputDataMask.SetDigitalDataMask(string channelName, int digitalDataMask) | NIFGEN_ATTR_DIGITAL_DATA_MASK |
| FgenOutputDataMask.GetDigitalStaticValue(string channelName) FgenOutputDataMask.SetDigitalStaticValue(string channelName, int digitalStaticValue) | NIFGEN_ATTR_DIGITAL_STATIC_VALUE |
| FgenOutput.GetDigitalPatternEnabled(string channelName) FgenOutput.SetDigitalPatternEnabled(string channelName, bool enabled) | NIFGEN_ATTR_DIGITAL_PATTERN_ENABLED |
| FgenOutput.IdleBehavior | NIFGEN_ATTR_IDLE_BEHAVIOR |
| FgenOutput.GetIdleValue(string channelName) FgenOutput.SetIdleValue(string channelName, int idleValue) | NIFGEN_ATTR_IDLE_VALUE |
| FgenOutput.WaitBehavior | NIFGEN_ATTR_WAIT_BEHAVIOR |
| FgenOutput.GetWaitValue(string channelName) FgenOutput.SetWaitValue(string channelName, int waitValue) | NIFGEN_ATTR_WAIT_VALUE |
| FgenArbitrary.GetGain(string channelName) FgenArbitrary.SetGain(string channelName, double gain) | NIFGEN_ATTR_ARB_GAIN |
| FgenArbitrary.GetOffset(string channelName) FgenArbitrary.SetOffset(string channelName, double offset) | NIFGEN_ATTR_ARB_OFFSET |
| FgenArbitraryWaveform.Quantum | NIFGEN_ATTR_WAVEFORM_QUANTUM |
| FgenArbitraryWaveform.NumberWaveformsMax | NIFGEN_ATTR_MAX_NUM_WAVEFORMS |
| FgenArbitraryWaveform.SizeMin | NIFGEN_ATTR_MIN_WAVEFORM_SIZE |
| FgenArbitraryWaveform.SizeMax | NIFGEN_ATTR_MAX_WAVEFORM_SIZE |
| FgenArbitraryWaveform.GetHandle(string channelName) FgenArbitraryWaveform.SetHandle(string channelName, int handle) | NIFGEN_ATTR_ARB_WAVEFORM_HANDLE |
| FgenArbitraryWaveform.MarkerPosition | NIFGEN_ATTR_ARB_MARKER_POSITION |
| FgenArbitraryWaveform.RepeatCount | NIFGEN_ATTR_ARB_REPEAT_COUNT |
| FgenArbitrarySequence.GetHandle(string channelName) FgenArbitrarySequence.SetHandle(string channelName, int handle) | NIFGEN_ATTR_ARB_SEQUENCE_HANDLE |
| FgenArbitrarySequence.NumberSequencesMax | NIFGEN_ATTR_MAX_NUM_SEQUENCES |
| FgenArbitrarySequence.LengthMin | NIFGEN_ATTR_MIN_SEQUENCE_LENGTH |
| FgenArbitrarySequence.LengthMax | NIFGEN_ATTR_MAX_SEQUENCE_LENGTH |
| FgenArbitrarySequence.LoopCountMax | NIFGEN_ATTR_MAX_LOOP_COUNT |
| FgenScript.ScriptToGenerate | NIFGEN_ATTR_SCRIPT_TO_GENERATE |
| FgenDataTransfer.FileTransferBlockSize | NIFGEN_ATTR_FILE_TRANSFER_BLOCK_SIZE |
| FgenDataTransfer.BlockSize | NIFGEN_ATTR_DATA_TRANSFER_BLOCK_SIZE |
| FgenDataTransfer.MaximumBandwidth | NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH |
| N/A | NIFGEN_ATTR_DIRECT_DMA_ENABLED |
| N/A | NIFGEN_ATTR_DIRECT_DMA_WINDOW_SIZE |
| N/A | NIFGEN_ATTR_DIRECT_DMA_WINDOW_ADDRESS |
| FgenStreaming.WaveformName | NIFGEN_ATTR_STREAMING_WAVEFORM_NAME |
| FgenStreaming.WaveformHandle | NIFGEN_ATTR_STREAMING_WAVEFORM_HANDLE |
| FgenStreaming.SpaceAvailableInWaveform | NIFGEN_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM |
| FgenStreaming.WriteTimeout | NIFGEN_ATTR_STREAMING_WRITE_TIMEOUT |
| FgenDataTransfer.PreferredPacketSize | NIFGEN_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE |
| FgenDataTransfer.MaximumInFlightReads | NIFGEN_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS |
| N/A | NIFGEN_ATTR_PCI_DMA_OPTIMIZATIONS_ENABLED |
| FgenOnboardSignalProcessing.GetEnabled(string channelName) FgenOnboardSignalProcessing.SetEnabled(string channelName, bool enabled) | NIFGEN_ATTR_OSP_ENABLED |
| FgenOnboardSignalProcessing.GetIQRate(string channelName) FgenOnboardSignalProcessing.SetIQRate(string channelName, double rate) | NIFGEN_ATTR_OSP_IQ_RATE |
| FgenOnboardSignalProcessing.GetDataProcessingMode(string channelName) FgenOnboardSignalProcessing.SetDataProcessingMode(string channelName, OspDataProcessingMode dataProcessingMode) | NIFGEN_ATTR_OSP_DATA_PROCESSING_MODE |
| FgenOnboardSignalProcessing.GetMode(string channelName) FgenOnboardSignalProcessing.SetMode(string channelName, OspMode mode) | NIFGEN_ATTR_OSP_MODE |
| FgenOnboardSignalProcessing.GetFrequencyShift(string channelName) FgenOnboardSignalProcessing.SetFrequencyShift(string channelName, double frequencyShift) | NIFGEN_ATTR_OSP_FREQUENCY_SHIFT |
| FgenOnboardSignalProcessing.GetEnabled(string channelName) FgenOnboardSignalProcessing.SetEnabled(string channelName, bool enabled) | NIFGEN_ATTR_OSP_CARRIER_ENABLED |
| FgenOnboardSignalProcessing.GetFrequency(string channelName) FgenOnboardSignalProcessing.SetFrequency(string channelName, double frequency) | NIFGEN_ATTR_OSP_CARRIER_FREQUENCY |
| FgenOnboardSignalProcessing.GetPhaseI(string channelName) FgenOnboardSignalProcessing.SetPhaseI(string channelName, double phase) | NIFGEN_ATTR_OSP_CARRIER_PHASE_I |
| FgenOnboardSignalProcessing.GetPhaseQ(string channelName) FgenOnboardSignalProcessing.SetPhaseQ(string channelName, double phase) | NIFGEN_ATTR_OSP_CARRIER_PHASE_Q |
| FgenOnboardSignalProcessing.CompensateForFilterDelay | NIFGEN_ATTR_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY |
| FgenOnboardSignalProcessing.GetFilterType(string channelName) FgenOnboardSignalProcessing.SetFilterType(string channelName, OspFirFilterType firFilterType) | NIFGEN_ATTR_OSP_FIR_FILTER_TYPE |
| FgenOnboardSignalProcessing.GetEnabled(string firFilterName) FgenOnboardSignalProcessing.SetEnabled(string firFilterName, bool enabled) | NIFGEN_ATTR_OSP_FIR_FILTER_ENABLED |
| FgenOnboardSignalProcessing.GetInterpolationFactor(string firFilterName) FgenOnboardSignalProcessing.SetInterpolationFactor(string firFilterName, double interpolationFactor) | NIFGEN_ATTR_OSP_FIR_FILTER_INTERPOLATION |
| FgenOnboardSignalProcessing.GetEnabled(string channelName) FgenOnboardSignalProcessing.SetEnabled(string channelName, bool enabled) | NIFGEN_ATTR_OSP_CIC_FILTER_ENABLED |
| FgenOnboardSignalProcessing.GetInterpolationFactor(string channelName) FgenOnboardSignalProcessing.SetInterpolationFactor(string channelName, double interpolationFactor) | NIFGEN_ATTR_OSP_CIC_FILTER_INTERPOLATION |
| FgenOnboardSignalProcessing.GetRootRaisedCosineAlpha(string channelName) FgenOnboardSignalProcessing.SetRootRaisedCosineAlpha(string channelName, double alpha) | NIFGEN_ATTR_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA |
| FgenOnboardSignalProcessing.GetRaisedCosineAlpha(string channelName) FgenOnboardSignalProcessing.SetRaisedCosineAlpha(string channelName, double alpha) | NIFGEN_ATTR_OSP_FIR_FILTER_RAISED_COSINE_ALPHA |
| FgenOnboardSignalProcessing.GetFlatPassband(string channelName) FgenOnboardSignalProcessing.SetFlatPassband(string channelName, double passband) | NIFGEN_ATTR_OSP_FIR_FILTER_FLAT_PASSBAND |
| FgenOnboardSignalProcessing.GetGaussianBT(string channelName) FgenOnboardSignalProcessing.SetGaussianBT(string channelName, double btValue) | NIFGEN_ATTR_OSP_FIR_FILTER_GAUSSIAN_BT |
| FgenOnboardSignalProcessing.GetGain(string channelName) FgenOnboardSignalProcessing.SetGain(string channelName, double gain) | NIFGEN_ATTR_OSP_CIC_FILTER_GAIN |
| FgenOnboardSignalProcessing.GetPrefilterGainI(string channelName) FgenOnboardSignalProcessing.SetPrefilterGainI(string channelName, double gain) | NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_I |
| FgenOnboardSignalProcessing.GetPrefilterGainQ(string channelName) FgenOnboardSignalProcessing.SetPrefilterGainQ(string channelName, double gain) | NIFGEN_ATTR_OSP_PRE_FILTER_GAIN_Q |
| FgenOnboardSignalProcessing.GetPrefilterOffsetI(string channelName) FgenOnboardSignalProcessing.SetPrefilterOffsetI(string channelName, double offset) | NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_I |
| FgenOnboardSignalProcessing.GetPrefilterOffsetQ(string channelName) FgenOnboardSignalProcessing.SetPrefilterOffsetQ(string channelName, double offset) | NIFGEN_ATTR_OSP_PRE_FILTER_OFFSET_Q |
| FgenOnboardSignalProcessing.GetOverflowErrorReporting(string channelName) FgenOnboardSignalProcessing.SetOverflowErrorReporting(string channelName, OspOverflowErrorReporting errorReporting) | NIFGEN_ATTR_OSP_OVERFLOW_ERROR_REPORTING |
| FgenOnboardSignalProcessing.OverflowStatus | NIFGEN_ATTR_OSP_OVERFLOW_STATUS |
| N/A | NIFGEN_ATTR_P2P_ENABLED |
| N/A | NIFGEN_ATTR_P2P_DESTINATION_CHANNELS |
| N/A | NIFGEN_ATTR_P2P_ENDPOINT_SIZE |
| N/A | NIFGEN_ATTR_P2P_SPACE_AVAILABLE_IN_ENDPOINT |
| N/A | NIFGEN_ATTR_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT |
| N/A | NIFGEN_ATTR_P2P_ENDPOINT_COUNT |
| N/A | NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INTERVAL |
| N/A | NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS |
| N/A | NIFGEN_ATTR_P2P_MANUAL_CONFIGURATION_ENABLED |
| N/A | NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_ADDRESS |
| N/A | NIFGEN_ATTR_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE |
| N/A | NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS |
| N/A | NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE |
| N/A | NIFGEN_ATTR_P2P_ENDPOINT_WINDOW_SIZE |
| N/A | NIFGEN_ATTR_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL |
| N/A | NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS |
| N/A | NIFGEN_ATTR_P2P_DONE_NOTIFICATION_ADDRESS_TYPE |
| N/A | NIFGEN_ATTR_P2P_DONE_NOTIFICATION_VALUE |
| FgenStandardWaveform.GetWaveformFunction(string channelName) FgenStandardWaveform.SetWaveformFunction(string channelName, StandardWaveform waveformFunction) | NIFGEN_ATTR_FUNC_WAVEFORM |
| FgenStandardWaveform.GetAmplitude(string channelName) FgenStandardWaveform.SetAmplitude(string channelName, double amplitude) | NIFGEN_ATTR_FUNC_AMPLITUDE |
| FgenStandardWaveform.GetDCOffset(string channelName) FgenStandardWaveform.SetDCOffset(string channelName, double dcOffset) | NIFGEN_ATTR_FUNC_DC_OFFSET |
| FgenStandardWaveform.GetStartPhase(string channelName) FgenStandardWaveform.SetStartPhase(string channelName, double startPhase) | NIFGEN_ATTR_FUNC_START_PHASE |
| FgenStandardWaveform.GetDutyCycleHigh(string channelName) FgenStandardWaveform.SetDutyCycleHigh(string channelName, double dutyCycleHigh) | NIFGEN_ATTR_FUNC_DUTY_CYCLE_HIGH |
| N/A | NIFGEN_ATTR_SYNC_DUTY_CYCLE_HIGH |
| FgenStandardWaveform.SyncOutOutputTerminal | NIFGEN_ATTR_SYNC_OUT_OUTPUT_TERMINAL |
| FgenStandardWaveform.GetFrequency(string channelName) FgenStandardWaveform.SetFrequency(string channelName, double frequency) | NIFGEN_ATTR_FUNC_FREQUENCY |
| FgenStandardWaveform.BufferSize | NIFGEN_ATTR_FUNC_BUFFER_SIZE |
| FgenStandardWaveform.MaximumBufferSize | NIFGEN_ATTR_FUNC_MAX_BUFFER_SIZE |
| FgenFrequencyList.Handle | NIFGEN_ATTR_FREQ_LIST_HANDLE |
| FgenFrequencyList.MaximumNumber | NIFGEN_ATTR_MAX_NUM_FREQ_LISTS |
| FgenFrequencyList.GetMinimumLength(string channelName) | NIFGEN_ATTR_MIN_FREQ_LIST_LENGTH |
| FgenFrequencyList.GetMaximumLength(string channelName) | NIFGEN_ATTR_MAX_FREQ_LIST_LENGTH |
| FgenFrequencyList.GetMinimumDuration(string channelName) | NIFGEN_ATTR_MIN_FREQ_LIST_DURATION |
| FgenFrequencyList.GetMaximumDuration(string channelName) | NIFGEN_ATTR_MAX_FREQ_LIST_DURATION |
| FgenFrequencyList.DurationQuantum | NIFGEN_ATTR_FREQ_LIST_DURATION_QUANTUM |
| FgenReferenceClock.Source | NIFGEN_ATTR_REFERENCE_CLOCK_SOURCE |
| FgenReferenceClock.Frequency | NIFGEN_ATTR_REF_CLOCK_FREQUENCY |
| FgenReferenceClock.OutputTerminal | NIFGEN_ATTR_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL |
| FgenReferenceClock.OnboardOutputTerminal | NIFGEN_ATTR_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL |
| FgenArbitrary.SampleRate FgenSampleClock.Rate | NIFGEN_ATTR_ARB_SAMPLE_RATE |
| FgenSampleClock.ClockMode | NIFGEN_ATTR_CLOCK_MODE |
| FgenSampleClock.Source | NIFGEN_ATTR_SAMPLE_CLOCK_SOURCE |
| FgenSampleClock.OutputTerminal | NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL |
| FgenSampleClock.ExportedDivisor | NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_DIVISOR |
| FgenSampleClockTimebase.Source | NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_SOURCE |
| FgenSampleClockTimebase.Rate | NIFGEN_ATTR_SAMPLE_CLOCK_TIMEBASE_RATE |
| FgenSampleClockTimebase.OutputTerminal | NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL |
| FgenSampleClockTimebase.ExportedDivisor | NIFGEN_ATTR_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR |
| FgenSampleClock.ExternalMultiplier | NIFGEN_ATTR_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER |
| FgenSampleClock.AbsoluteDelay | NIFGEN_ATTR_SAMPLE_CLOCK_ABSOLUTE_DELAY |
| FgenSampleClock.OscillatorPhaseDacValue | NIFGEN_ATTR_OSCILLATOR_PHASE_DAC_VALUE |
| FgenSampleClock.ExternalClockDelayBinaryValue | NIFGEN_ATTR_EXTERNAL_CLOCK_DELAY_BINARY_VALUE |
| FgenMarkerEvent.GetOutputTerminal(string markerName) FgenMarkerEvent.SetOutputTerminal(string markerName, string outputTerminal) | NIFGEN_ATTR_MARKER_EVENT_OUTPUT_TERMINAL |
| FgenMarkerEvent.GetOutputBehavior(string markerName) FgenMarkerEvent.SetOutputBehavior(string markerName, OutputBehavior outputBehavior) | NIFGEN_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR |
| FgenMarkerEvent.GetPulsePolarity(string markerName) FgenMarkerEvent.SetPulsePolarity(string markerName, LogicLevel pulsePolarity) | NIFGEN_ATTR_MARKER_EVENT_PULSE_POLARITY |
| FgenMarkerEvent.GetPulseWidth(string markerName) FgenMarkerEvent.SetPulseWidth(string markerName, double pulseWidth) | NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH |
| FgenMarkerEvent.GetPulseWidthUnits(string markerName) FgenMarkerEvent.SetPulseWidthUnits(string markerName, PulseWidthUnits pulseWidthUnits) | NIFGEN_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS |
| FgenMarkerEvent.GetInitialState(string markerName) FgenMarkerEvent.SetInitialState(string markerName, LogicLevel initialState) | NIFGEN_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE |
| FgenMarkerEvent.GetDelay(string markerName) FgenMarkerEvent.SetDelay(string markerName, double delay) | NIFGEN_ATTR_MARKER_EVENT_DELAY |
| FgenMarkerEvent.GetDelayUnits(string markerName) FgenMarkerEvent.SetDelayUnits(string markerName, DelayUnits delayUnits) | NIFGEN_ATTR_MARKER_EVENT_DELAY_UNITS |
| FgenMarkerEvent.AllMarkerEventsLiveStatus | NIFGEN_ATTR_ALL_MARKER_EVENTS_LIVE_STATUS |
| FgenMarkerEvent.GetLiveStatus(string markerName) | NIFGEN_ATTR_MARKER_EVENT_LIVE_STATUS |
| FgenMarkerEvent.AllMarkerEventsLatchedStatus | NIFGEN_ATTR_ALL_MARKER_EVENTS_LATCHED_STATUS |
| FgenMarkerEvent.GetLatchedStatus(string markerName) FgenMarkerEvent.SetLatchedStatus(string markerName, bool latchedStatus) | NIFGEN_ATTR_MARKER_EVENT_LATCHED_STATUS |
| FgenDataMarkerEvent.GetDataBitNumber(string dataMarkerName) FgenDataMarkerEvent.SetDataBitNumber(string dataMarkerName, int dataBitNumber) | NIFGEN_ATTR_DATA_MARKER_EVENT_DATA_BIT_NUMBER |
| FgenDataMarkerEvent.GetActiveLevel(string dataMarkerName) FgenDataMarkerEvent.SetActiveLevel(string dataMarkerName, LogicLevel levelPolarity) | NIFGEN_ATTR_DATA_MARKER_EVENT_LEVEL_POLARITY |
| FgenDataMarkerEvent.GetOutputTerminal(string dataMarkerName) FgenDataMarkerEvent.SetOutputTerminal(string dataMarkerName, string outputTerminal) | NIFGEN_ATTR_DATA_MARKER_EVENT_OUTPUT_TERMINAL |
| FgenReadyForStartEvent.OutputTerminal | NIFGEN_ATTR_READY_FOR_START_EVENT_OUTPUT_TERMINAL |
| FgenReadyForStartEvent.ActiveLevel | NIFGEN_ATTR_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL |
| FgenReadyForStartEvent.LiveStatus | NIFGEN_ATTR_READY_FOR_START_EVENT_LIVE_STATUS |
| FgenStartedEvent.OutputTerminal | NIFGEN_ATTR_STARTED_EVENT_OUTPUT_TERMINAL |
| FgenStartedEvent.OutputBehavior | NIFGEN_ATTR_STARTED_EVENT_OUTPUT_BEHAVIOR |
| FgenStartedEvent.ActiveLevel | NIFGEN_ATTR_STARTED_EVENT_LEVEL_ACTIVE_LEVEL |
| FgenStartedEvent.PulsePolarity | NIFGEN_ATTR_STARTED_EVENT_PULSE_POLARITY |
| FgenStartedEvent.PulseWidthUnits | NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH_UNITS |
| FgenStartedEvent.PulseWidth | NIFGEN_ATTR_STARTED_EVENT_PULSE_WIDTH |
| FgenStartedEvent.Delay | NIFGEN_ATTR_STARTED_EVENT_DELAY |
| FgenStartedEvent.DelayUnits | NIFGEN_ATTR_STARTED_EVENT_DELAY_UNITS |
| FgenStartedEvent.IsLatched | NIFGEN_ATTR_STARTED_EVENT_LATCHED_STATUS |
| FgenDoneEvent.OutputTerminal | NIFGEN_ATTR_DONE_EVENT_OUTPUT_TERMINAL |
| FgenDoneEvent.OutputBehavior | NIFGEN_ATTR_DONE_EVENT_OUTPUT_BEHAVIOR |
| FgenDoneEvent.ActiveLevel | NIFGEN_ATTR_DONE_EVENT_LEVEL_ACTIVE_LEVEL |
| FgenDoneEvent.PulsePolarity | NIFGEN_ATTR_DONE_EVENT_PULSE_POLARITY |
| FgenDoneEvent.PulseWidthUnits | NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH_UNITS |
| FgenDoneEvent.PulseWidth | NIFGEN_ATTR_DONE_EVENT_PULSE_WIDTH |
| FgenDoneEvent.Delay | NIFGEN_ATTR_DONE_EVENT_DELAY |
| FgenDoneEvent.DelayUnits | NIFGEN_ATTR_DONE_EVENT_DELAY_UNITS |
| FgenDoneEvent.IsLatched | NIFGEN_ATTR_DONE_EVENT_LATCHED_STATUS |
| FgenTrigger.GetTriggerMode(string channelName) FgenTrigger.SetTriggerMode(string channelName, TriggerMode triggerMode) | NIFGEN_ATTR_TRIGGER_MODE |
| N/A | NIFGEN_ATTR_BURST_COUNT |
| FgenStartTrigger.TriggerType | NIFGEN_ATTR_START_TRIGGER_TYPE |
| FgenDigitalEdgeStartTrigger.Source | NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE |
| FgenDigitalEdgeStartTrigger.Edge | NIFGEN_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE |
| FgenStartTrigger.OutputTerminal | NIFGEN_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL |
| FgenScriptTrigger.GetTriggerType(string triggerId) FgenScriptTrigger.SetTriggerType(string triggerId, TriggerType triggerType) | NIFGEN_ATTR_SCRIPT_TRIGGER_TYPE |
| FgenDigitalEdgeScriptTrigger.GetSource(string triggerId) FgenDigitalEdgeScriptTrigger.SetSource(string triggerId, string source) | NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE |
| FgenDigitalEdgeScriptTrigger.GetEdge(string triggerId) FgenDigitalEdgeScriptTrigger.SetEdge(string triggerId, DigitalEdge edge | NIFGEN_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE |
| FgenDigitalLevelScriptTrigger.GetSource(string triggerId) FgenDigitalLevelScriptTrigger.SetSource(string triggerId, string source) | NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE |
| FgenDigitalLevelScriptTrigger.GetActiveLevel(string triggerId) FgenDigitalLevelScriptTrigger.SetActiveLevel(string triggerId, LogicLevel level) | NIFGEN_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL |
| FgenScriptTrigger.GetOutputTerminal(string triggerId) FgenScriptTrigger.SetOutputTerminal(string triggerId, string outputTerminal) | NIFGEN_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL |
| FgenDriverIdentity.BusType | NIFGEN_ATTR_BUS_TYPE |
| FgenDriverIdentity.MemorySize | NIFGEN_ATTR_MEMORY_SIZE |
| FgenDriverIdentity.SerialNumber | NIFGEN_ATTR_SERIAL_NUMBER |
| N/A | NIFGEN_ATTR_MARKER_EVENTS_COUNT |
| N/A | NIFGEN_ATTR_DATA_MARKER_EVENTS_COUNT |
| N/A | NIFGEN_ATTR_SCRIPT_TRIGGERS_COUNT |
| N/A | NIFGEN_ATTR_VIDEO_WAVEFORM_TYPE |
| N/A | NIFGEN_ATTR_FILTER_CORRECTION_FREQUENCY |
| N/A | NIFGEN_ATTR_TRIGGER_SOURCE |
| N/A | NIFGEN_ATTR_SYNCHRONIZATION |
| N/A | NIFGEN_ATTR_ID_QUERY_RESPONSE |
| N/A | NIFGEN_ATTR_GAIN_DAC_VALUE |
| N/A | NIFGEN_ATTR_OFFSET_DAC_VALUE |
| N/A | NIFGEN_ATTR_OSCILLATOR_FREQ_DAC_VALUE |
| N/A | NIFGEN_ATTR_CAL_ADC_INPUT |
| N/A | NIFGEN_ATTR_PRE_AMPLIFIER_ATTENUATION |
| N/A | NIFGEN_ATTR_POST_AMPLIFIER_ATTENUATION |
| FgenDriverOperation.Cache | NIFGEN_ATTR_CACHE |
| FgenDriverOperation.RangeCheck | NIFGEN_ATTR_RANGE_CHECK |
| FgenDriverOperation.QueryInstrumentStatus | NIFGEN_ATTR_QUERY_INSTRUMENT_STATUS |
| FgenDriverOperation.RecordCoercions | NIFGEN_ATTR_RECORD_COERCIONS |
| FgenDriverOperation.Simulate | NIFGEN_ATTR_SIMULATE |
| FgenDriverOperation.InterchangeCheck | NIFGEN_ATTR_INTERCHANGE_CHECK |
| FgenDriverIdentity.Description | NIFGEN_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| N/A | NIFGEN_ATTR_SPECIFIC_DRIVER_PREFIX |
| FgenDriverIdentity.Vendor | NIFGEN_ATTR_SPECIFIC_DRIVER_VENDOR |
| FgenDriverIdentity.Revision | NIFGEN_ATTR_SPECIFIC_DRIVER_REVISION |
| FgenDriverIdentity.SpecificationMajorVersion | NIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION |
| FgenDriverIdentity.SpecificationMinorVersion | NIFGEN_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION |
| FgenDriverIdentity.GetSupportedInstrumentModels() | NIFGEN_ATTR_SUPPORTED_INSTRUMENT_MODELS |
| FgenDriverIdentity.GetGroupCapabilities() | NIFGEN_ATTR_GROUP_CAPABILITIES |
| FgenDriverIdentity.ChannelCount | NIFGEN_ATTR_CHANNEL_COUNT |
| FgenDriverIdentity.InstrumentManufacturer | NIFGEN_ATTR_INSTRUMENT_MANUFACTURER |
| FgenDriverIdentity.InstrumentModel | NIFGEN_ATTR_INSTRUMENT_MODEL |
| FgenDriverIdentity.InstrumentFirmwareRevision | NIFGEN_ATTR_INSTRUMENT_FIRMWARE_REVISION |
| FgenDriverIdentity.ModuleRevision | NIFGEN_ATTR_MODULE_REVISION |
| FgenDriverOperation.IOResourceDescriptor | NIFGEN_ATTR_IO_RESOURCE_DESCRIPTOR |
| FgenDriverOperation.LogicalName | NIFGEN_ATTR_LOGICAL_NAME |
| FgenDriverOperation.DriverSetup | NIFGEN_ATTR_DRIVER_SETUP |
| NIFgen.NIFgen(string resourceName, bool idQuery, bool reset) | niFgen_init |
| NIFgen.NIFgen(string resourceName, bool idQuery, bool reset, string optionString) | niFgen_InitWithOptions |
| NIFgen.Close() | niFgen_close |
| FgenDriverUtility.ExportAttributeConfigurationBuffer | niFgen_ExportAttributeConfigurationBuffer |
| FgenDriverUtility.ExportAttributeConfigurationFile | niFgen_ExportAttributeConfigurationFile |
| FgenDriverUtility.ImportAttributeConfigurationBuffer | niFgen_ImportAttributeConfigurationBuffer |
| FgenDriverUtility.ImportAttributeConfigurationFile | niFgen_ImportAttributeConfigurationFile |
| FgenDriverUtility.Reset() | niFgen_reset |
| FgenDriverUtility.SelfTest() | niFgen_self_test |
| FgenDriverUtility.ErrorQuery() | niFgen_error_query |
| N/A | niFgen_error_message |
| N/A | niFgen_revision_query |
| N/A | niFgen_GetError |
| N/A | niFgen_ClearError |
| N/A | niFgen_ErrorHandler |
| N/A | niFgen_LockSession |
| N/A | niFgen_UnlockSession |
| FgenOutput.GetChannelName(int index) | niFgen_GetChannelName |
| N/A | niFgen_GetNextInterchangeWarning |
| FgenDriverOperation.ResetInterchangeCheck() | niFgen_ResetInterchangeCheck |
| N/A | niFgen_ClearInterchangeWarnings |
| N/A | niFgen_GetNextCoercionRecord |
| FgenDriverOperation.InvalidateAllAttributes() | niFgen_InvalidateAllAttributes |
| FgenDriverUtility.ResetWithDefaults() | niFgen_ResetWithDefaults |
| FgenDriverUtility.Disable() | niFgen_Disable |
| NIFgen.Commit() | niFgen_Commit |
| FgenDriverUtility.HardwareState | niFgen_GetHardwareState |
| NIFgen.WaitUntilDone(TimeSpan maxTime) | niFgen_WaitUntilDone |
| NIFgen.IsDone | niFgen_IsDone |
| FgenDriverUtility.ResetDevice() | niFgen_ResetDevice |
| N/A | niFgen_ConfigureOperationMode |
| N/A | niFgen_ConfigureOutputMode |
| FgenReferenceClock.Configure(string source, double frequency) | niFgen_ConfigureReferenceClock |
| N/A | niFgen_ConfigureOutputImpedance |
| N/A | niFgen_ConfigureOutputEnabled |
| NIFgen.ConfigureChannels(string channels) | niFgen_ConfigureChannels |
| NIFgen.InitiateGeneration() | niFgen_InitiateGeneration |
| NIFgen.AbortGeneration() | niFgen_AbortGeneration |
| FgenStandardWaveform.Configure(string channelName, StandardWaveform waveformFunction, double amplitude, double dcOffset, double frequency, double startPhase) | niFgen_ConfigureStandardWaveform |
| FgenStandardWaveform.DefineUserStandardWaveform(string channelName, double[] data) | niFgen_DefineUserStandardWaveform |
| FgenStandardWaveform.ClearUserStandardWaveform(string channelName) | niFgen_ClearUserStandardWaveform |
| FgenStandardWaveform.SetFrequency(string channelName, double frequency) | niFgen_ConfigureFrequency |
| FgenStandardWaveform.SetAmplitude(string channelName, double amplitude) | niFgen_ConfigureAmplitude |
| N/A | niFgen_QueryArbWfmCapabilities |
| FgenArbitraryWaveform.CreateChannelWaveform(string channelName, double[] waveform) FgenArbitraryWaveform.CreateChannelWaveform<T>(string channelName, AnalogWaveform<T> waveform) | niFgen_CreateWaveformF64 |
| FgenArbitraryWaveform.CreateChannelWaveform(string channelName, short[] waveform) | niFgen_CreateWaveformI16 |
| FgenArbitraryWaveform.CreateChannelWaveform(string channelName, ComplexDouble[] waveform) | niFgen_CreateWaveformComplexF64 |
| FgenArbitraryWaveform.CreateChannelWaveformInt16FromFile(string channelName, string fileName, ByteOrder byteOrder) | niFgen_CreateWaveformFromFileI16 |
| FgenArbitraryWaveform.CreateChannelWaveformDoubleFromFile(string channelName, string fileName, ByteOrder byteOrder) | niFgen_CreateWaveformFromFileF64 |
| N/A | niFgen_CreateWaveformFromFileHWS |
| FgenArbitrary.SampleRate | niFgen_ConfigureSampleRate |
| FgenArbitraryWaveform.Configure(string channelName, int handle, double gain, double offset) | niFgen_ConfigureArbWaveform |
| FgenArbitraryWaveform.Clear(int handle) | niFgen_ClearArbWaveform |
| FgenNamedWaveform.Allocate(string channelName, string waveformName, int numberOfSamples) | niFgen_AllocateNamedWaveform |
| FgenNamedWaveform.SetNextWritePosition(string channelName, string waveformName, WaveformWritePosition relativeTo, int offset) | niFgen_SetNamedWaveformNextWritePosition |
| FgenNamedWaveform.Write(string channelName, string waveformName, double[] waveform) FgenNamedWaveform.Write<TData>(string channelName, string waveformName, AnalogWaveform<TData> waveform) | niFgen_WriteNamedWaveformF64 |
| FgenNamedWaveform.Write(string channelName, string waveformName, short[] waveform) | niFgen_WriteNamedWaveformI16 |
| FgenNamedWaveform.Write(string channelName, string waveformName, ComplexDouble[] waveform) | niFgen_WriteNamedWaveformComplexF64 |
| FgenNamedWaveform.Write(string channelName, string waveformName, ComplexInt16[] waveform) | niFgen_WriteNamedWaveformComplexI16 |
| FgenNamedWaveform.Delete(string channelName, string waveformName) | niFgen_DeleteNamedWaveform |
| N/A | niFgen_QueryArbSeqCapabilities |
| FgenArbitrarySequence.Create(int[] waveformHandle, int[] loopCount) | niFgen_CreateArbSequence |
| FgenArbitrarySequence.Create(int[] waveformHandle, int[] loopCount, int[] sampleCounts, int[] markers, out int[] coercedMarkers) | niFgen_CreateAdvancedArbSequence |
| FgenArbitrarySequence.Configure(string channelName, int handle, double gain, double offset) | niFgen_ConfigureArbSequence |
| FgenArbitrarySequence.Clear(int handle) | niFgen_ClearArbSequence |
| FgenArbitrary.ClearMemory() | niFgen_ClearArbMemory |
| N/A | niFgen_QueryFreqListCapabilities |
| FgenFrequencyList.Create(StandardWaveform waveform, double[] frequencies, Ivi.Driver.PrecisionTimeSpan[] durations) | niFgen_CreateFreqList |
| FgenFrequencyList.Configure(string channelName, int frequencyListHandle, double amplitude, double dcOffset, double startPhase) | niFgen_ConfigureFreqList |
| FgenFrequencyList.Clear(int frequencyListHandle) | niFgen_ClearFreqList |
| FgenScript.Write(string channelName, string script) | niFgen_WriteScript |
| FgenScript.Delete(string channelName, string scriptName) | niFgen_DeleteScript |
| NIFgen.ExportSignal(SignalSource signalSource, string signalIdentifier, string outputTerminal) | niFgen_ExportSignal |
| N/A | niFgen_RouteSignalOut |
| FgenSoftwareEdgeScriptTrigger.Send(string triggerId) FgenSoftwareEdgeStartTrigger.Send() | niFgen_SendSoftwareEdgeTrigger |
| FgenDigitalEdgeStartTrigger.Configure(string source, DigitalEdge edge) | niFgen_ConfigureDigitalEdgeStartTrigger |
| FgenSoftwareEdgeStartTrigger.Configure() | niFgen_ConfigureSoftwareEdgeStartTrigger |
| FgenStartTrigger.Disable() | niFgen_DisableStartTrigger |
| N/A | niFgen_ConfigureP2PEndpointFullnessStartTrigger |
| FgenDigitalEdgeScriptTrigger.Configure(string triggerId, string source, DigitalEdge edge) | niFgen_ConfigureDigitalEdgeScriptTrigger |
| FgenDigitalLevelScriptTrigger.Configure(string triggerId, string source, LogicLevel level) | niFgen_ConfigureDigitalLevelScriptTrigger |
| FgenSoftwareEdgeScriptTrigger.Configure(string triggerId) | niFgen_ConfigureSoftwareEdgeScriptTrigger |
| FgenScriptTrigger.Disable(string triggerId) | niFgen_DisableScriptTrigger |
| N/A | niFgen_ConfigureClockMode |
| FgenSampleClock.AdjustRelativeDelay(Ivi.Driver.PrecisionTimeSpan time) | niFgen_AdjustSampleClockRelativeDelay |
| FgenArbitraryWaveform.Allocate(string channelName, int numberOfSamples) | niFgen_AllocateWaveform |
| FgenArbitraryWaveform.SetNextWritePosition(string channelName, int handle, WaveformWritePosition relativeTo, int offset) | niFgen_SetWaveformNextWritePosition |
| FgenArbitraryWaveform.Write(string channelName, int handle, double[] waveform) FgenArbitraryWaveform.Write<T>(string channelName, int handle, AnalogWaveform<T> waveform) | niFgen_WriteWaveform |
| FgenArbitraryWaveform.Write(string channelName, int handle, short[] waveform) | niFgen_WriteBinary16Waveform |
| FgenArbitraryWaveform.Write(string channelName, int handle, ComplexDouble[] waveform) | niFgen_WriteWaveformComplexF64 |
| FgenArbitraryWaveform.Write(string channelName, int handle, ComplexInt16[] waveform) | niFgen_WriteComplexBinary16Waveform |
| N/A | niFgen_InitExtCal |
| N/A | niFgen_InitializeOscillatorFrequencyCalibration |
| N/A | niFgen_InitializeAnalogOutputCalibration |
| N/A | niFgen_InitializeCalADCCalibration |
| N/A | niFgen_InitializeFlatnessCalibration |
| N/A | niFgen_CloseExtCal |
| N/A | niFgen_SelfCal |
| N/A | niFgen_RestoreLastExtCalConstants |
| N/A | niFgen_GetSelfCalSupported |
| N/A | niFgen_GetSelfCalLastDateAndTime |
| N/A | niFgen_GetExtCalLastDateAndTime |
| N/A | niFgen_GetSelfCalLastTemp |
| N/A | niFgen_GetExtCalLastTemp |
| N/A | niFgen_GetExtCalRecommendedInterval |
| N/A | niFgen_ChangeExtCalPassword |
| N/A | niFgen_SetCalUserDefinedInfo |
| N/A | niFgen_GetCalUserDefinedInfo |
| N/A | niFgen_GetCalUserDefinedInfoMaxSize |
| N/A | niFgen_ReadCurrentTemperature |
| N/A | niFgen_ReadCalADC |
| N/A | niFgen_WriteBinary16AnalogStaticValue |
| N/A | niFgen_CalAdjustMainPathPreAmpOffset |
| N/A | niFgen_CalAdjustMainPathPreAmpGain |
| N/A | niFgen_CalAdjustMainPathPostAmpGainAndOffset |
| N/A | niFgen_CalAdjustDirectPathGain |
| N/A | niFgen_CalAdjustMainPathOutputImpedance |
| N/A | niFgen_CalAdjustDirectPathOutputImpedance |
| N/A | niFgen_CalAdjustOscillatorFrequency |
| N/A | niFgen_CalAdjustADC |
| N/A | niFgen_CalAdjustFlatness |
| FgenOnboardSignalProcessing.ConfigureCustomCoefficients(string channelName, double[] coefficients) | niFgen_ConfigureCustomFIRFilterCoefficients |
| FgenOnboardSignalProcessing.GetCoefficients(string channelName) | niFgen_GetFIRFilterCoefficients |
| N/A | niFgen_GetStreamEndpointHandle |
| N/A | niFgen_ManualEnableP2PStream |
| N/A | niFgen_WriteP2PEndpointI16 |
| N/A | niFgen_ConfigureSynchronization |
| N/A | niFgen_EnableDigitalPatterning |
| N/A | niFgen_DisableDigitalPatterning |
| N/A | niFgen_EnableDigitalFilter |
| N/A | niFgen_DisableDigitalFilter |
| FgenOutputFilter.EnableAnalogFilter(string channelName, double filterCorrectionFrequency) | niFgen_EnableAnalogFilter |
| N/A | niFgen_DisableAnalogFilter |
| N/A | niFgen_ConfigureSampleClockSource |
| N/A | niFgen_ConfigureTriggerMode |

Parent topic:

NI-FGEN .NET Class Library Help

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialabort.1.html language=enus -->
## TOPIC 00006: Abort Generation

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialabort.1.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialabort.1.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: The abort generation step aborts any signal generation that was initiated in the initiate generation step. When you abort generation, you can choose to either abort to ground or abort to a known voltage (not available for OutputMode.Function or OutputMode.FrequencyList).

Abort Generation

The abort generation step aborts any signal generation that was initiated in the initiate generation step.

OutputMode.Function

OutputMode.FrequencyList

Parent topic:

NI-FGEN .NET API Tutorial

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialabort.html language=enus -->
## TOPIC 00007: Abort to Ground

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialabort.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialabort.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: All operation modes can abort to ground. To abort to ground you must disable the output enable relay to remove the DC voltage from the output. Call FgenOutput.SetEnabled with the enabled parameter set to false to disable the analog output and to remove any DC voltage on the analog output. Call NIFge

Abort to Ground

All operation modes can abort to ground. To abort to ground you must disable the output enable relay to remove the DC voltage from the output.

1. Call FgenOutput.SetEnabled with the enabled parameter set to 
 false to disable the analog output and to remove any DC voltage on the analog output.
2. Call NIFgen.AbortGeneration to stop the waveform generation.

Parent topic:

Abort Generation

Related information:

- FgenOutput.SetEnabled Method
- NIFgen.AbortGeneration Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialaborttoknownvoltage.html language=enus -->
## TOPIC 00008: Abort to a Known Voltage

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialaborttoknownvoltage.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialaborttoknownvoltage.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: OutputMode.Arbitrary, OutputMode.Sequence, and OutputMode.Script can abort generation to a known voltage. When waveform generation is aborted, the analog output signal remains at the voltage corresponding to the last waveform generated until the device is reconfigured for another generation. Closing

Abort to a Known Voltage

OutputMode.Arbitrary, OutputMode.Sequence, and OutputMode.Script can abort generation to a known voltage.

Note

To abort the generation to known voltage, complete the following steps:

1. During your application, download a small, constant–amplitude waveform that corresponds to the desired output voltage. You will generate this waveform at the end of your application.
2. Abort generation of the current waveform by calling NIFgen.AbortGeneration.
3. Reconfigure the device to generate the constant–amplitude waveform.
4. Call NIFgen.InitiateGeneration to transition the device to the generation state.
5. Call NIFgen.AbortGeneration to stop generation of the constant-amplitude waveform.

Parent topic:

Abort Generation

Related information:

- NIFgen.InitiateGeneration Method
- NIFgen.AbortGeneration Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialclosesession.html language=enus -->
## TOPIC 00009: Closing the Session

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialclosesession.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialclosesession.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: The closing step closes the session and deallocates any resources the session used. The session will be closed when the NIFgen object is disposed. NIFgen.Close can also be called to close the session, however, your NIFgen object will no longer be useful after the session has been closed. Closing the

Closing the Session

The closing step closes the session and deallocates any resources the session used.

NIFgen.Close

NIFgen.Close

Parent topic:

NI-FGEN .NET API Tutorial

Related information:

- NIFgen.Close Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigure.html language=enus -->
## TOPIC 00010: Configure

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigure.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigure.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Once you have opened a session to your signal generator, you need to configure the session to generate the signals you desire for your application. If your application requires triggers, clocking, or exported signals, you must configure them before waveform generation begins. If you are using a mult

Configure

Once you have opened a session to your signal generator, you need to configure the session to generate the signals you desire for your application.

1. If your application requires triggers, clocking, or exported signals, you must configure them before waveform generation begins.
2. If you are using a multichannel device, configure channels after initializing and before configuring any other feature of the device.
3. Configure the output mode of your device. You can choose to generate a standard waveform, an arbitrary waveform, an arbitrary sequence, a frequency list, or a script.

Parent topic:

NI-FGEN .NET API Tutorial

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigurearbitrarysm.html language=enus -->
## TOPIC 00011: Configure Arbitrary Sequence Mode

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigurearbitrarysm.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigurearbitrarysm.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use OutputMode.Sequence to load multiple waveforms in the onboard memory of the signal generator. The procedure below provides the basic steps required to configure an arbitrary sequence. Set OutputMode to OutputMode.Sequence. (Optional) Call FgenArbitrary.ClearMemory to clear any previously

Configure Arbitrary Sequence Mode

You can use OutputMode.Sequence to load multiple waveforms in the onboard memory of the signal generator.

The procedure below provides the basic steps required to configure an arbitrary sequence.

1. Set OutputMode to OutputMode.Sequence.
2. (Optional) Call FgenArbitrary.ClearMemory to clear any previously created arbitrary waveforms, sequences, and scripts from the signal generator memory.
3. Call FgenArbitrarySequence.Create using an array of waveform handles and an array of loop counts.
4. Call FgenArbitrarySequence.Configure to configure the gain and offset of the sequence.

Parent topic:

Configure Output Mode

Related information:

- OutputMode Enumeration
- FgenArbitrarySequence.Create Method
- FgenArbitrarySequence.Configure Method
- FgenArbitrary.ClearMemory Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigurearbitrarywm.html language=enus -->
## TOPIC 00012: Configure Arbitrary Waveform Mode

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigurearbitrarywm.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigurearbitrarywm.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use OutputMode.Arbitrary to generate waveforms from user–created or user–provided arrays of numeric data. The procedure below provides the basic steps required to configure an arbitrary waveform. Set FgenOutput.OutputMode to OutputMode.Arbitrary. (Optional) Call FgenArbitrary.ClearMemory to

Configure Arbitrary Waveform Mode

You can use OutputMode.Arbitrary to generate waveforms from user–created or user–provided arrays of numeric data.

The procedure below provides the basic steps required to configure an arbitrary waveform.

1. Set FgenOutput.OutputMode to OutputMode.Arbitrary.
2. (Optional) Call FgenArbitrary.ClearMemory to clear any previously created arbitrary waveforms, sequences, and scripts from the signal generator memory.
3. Call one of the FgenArbitraryWaveform.CreateChannelWaveform overloaded methods, depending on the size and type of the data you choose.
4. Call FgenArbitraryWaveform.Configure to configure the gain and offset of the waveform.

Parent topic:

Configure Output Mode

Related information:

- OutputMode Enumeration
- FgenArbitraryWaveform.CreateChannelWaveform Method
- FgenArbitraryWaveform.Configure Method
- FgenArbitrary.ClearMemory Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigurechannels.html language=enus -->
## TOPIC 00013: Configure Channels

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigurechannels.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigurechannels.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: If you want to configure a multichannel signal generator to generate data on more than one channel, you must configure the channels to be used, but if you are not using a multichannel signal generator or if you are only concerned with data generated on one channel of a multichannel signal generator,

Configure Channels

1. If you want to configure a multichannel signal generator to generate data on more than one channel, you must configure the channels to be used, but if you are not using a multichannel signal generator or if you are only concerned with data generated on one channel of a multichannel signal generator, you do not need to perform this step.
2. Call NIFgen.ConfigureChannels with channelName set to the channel or channels you want to configure. Valid values are non-negative integers. For example, 0 is the only valid value on devices with one channel, while devices with two channels support values of 0 and 1. You can specify more than one channel by inserting commas between values (for example, "0,1").

Parent topic:

Configure

Related information:

- NIFgen.ConfigureChannels Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigurefreqlistmode.html language=enus -->
## TOPIC 00014: Configure Frequency List Mode

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigurefreqlistmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigurefreqlistmode.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use OutputMode.FrequencyList mode to generate a standard function using a list of frequencies you define. The procedure below provides the basic steps required to configure a frequency list. Set FgenOutput.OutputMode to OutputMode.FrequencyList. (Optional) Call FgenFrequencyList.Clear to rem

Configure Frequency List Mode

You can use OutputMode.FrequencyList mode to generate a standard function using a list of frequencies you define.

The procedure below provides the basic steps required to configure a frequency list.

1. Set FgenOutput.OutputMode to OutputMode.FrequencyList.
2. (Optional) Call FgenFrequencyList.Clear to remove a previously created frequency list from the signal generator memory.
3. Call FgenFrequencyList.Create to set the waveform, the frequencies, and durations of each step in the list.
4. Call FgenFrequencyList.Configure to select the active frequencyListHandle and configure the amplitude, dcOffset, and startPhase of the generation.

Parent topic:

Configure Output Mode

Related information:

- OutputMode Enumeration
- FgenFrequencyList.Create Method
- FgenFrequencyList.Configure Method
- FgenFrequencyList.Clear Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigureoutput.html language=enus -->
## TOPIC 00015: Configure Output Mode

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigureoutput.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigureoutput.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: OutputMode determines the type of waveforms that will be generated by your device. Choose the OutputMode for the signal generator. Options include Arbitrary, FrequencyList, Function, and Script, and Sequence. Use FgenOutput.OutputMode to configure the output mode of the signal generator.

Configure Output Mode

OutputMode determines the type of waveforms that will be generated by your device.

1. Choose the OutputMode for the signal generator. Options include Arbitrary, FrequencyList, Function, and Script, and Sequence.
2. Use FgenOutput.OutputMode to configure the output mode of the signal generator.

Parent topic:

Configure

Related information:

- OutputMode Enumeration

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigurescriptmode.html language=enus -->
## TOPIC 00016: Configure Script Mode

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigurescriptmode.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigurescriptmode.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use OutputMode.Script to link and loop multiple waveforms in complex combinations using a script. The procedure below provides the basic steps required to configure scripts. Set FgenOutput.OutputMode to OutputMode.Script. Write all waveforms that are referenced in the script by using FgenNam

Configure Script Mode

You can use OutputMode.Script to link and loop multiple waveforms in complex combinations using a script.

The procedure below provides the basic steps required to configure scripts.

1. Set FgenOutput.OutputMode to OutputMode.Script.
2. Write all waveforms that are referenced in the script by using FgenNamedWaveform.Allocate and the FgenNamedWaveform.Write overloaded methods.
3. After your waveforms are written to your device, call FgenScript.Write to write the script(s) containing the generation instructions to be executed. 
 The script you write can manage waveform generation based on multiple waveforms and triggers. For example, you could download waveforms A, B, C, and D into device memory. You could then write a script that would wait for a trigger to initiate generation and, upon receiving this trigger, generate waveform A three times with a marker at position 16 each time and finally generate waveforms B, C, and D twice (BCDBCD). The following is the script of this example: 
 script myFirstScript
 wait until scriptTrigger0
 repeat 3
generate waveformA marker0(16)
 end repeat
 repeat 2
generate waveformB
generate waveformC
generate waveformD
 end repeat
end script
4. (Optional) You can write multiple scripts that exist simultaneously on your device. If you write multiple scripts to your device, you must select the one you wish to execute by setting FgenScript.ScriptToGenerate.

Parent topic:

Configure Output Mode

Related information:

- OutputMode Enumeration
- FgenScript.ScriptToGenerate Method
- FgenScript.Write Method
- FgenNamedWaveform.Allocate Method
- FgenNamedWaveform.Write Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialconfigurestandard.html language=enus -->
## TOPIC 00017: Configure Standard Function Mode

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialconfigurestandard.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialconfigurestandard.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: OutputMode.Function allows you to generate standard function waveforms such as sine, square, triangle, etc. The procedure below provides the basic steps required to configure a standard waveform. Set FgenOutput.OutputMode to OutputMode.Function. Choose the type of waveform you would like to generate

Configure Standard Function Mode

OutputMode.Function allows you to generate standard function waveforms such as sine, square, triangle, etc.

The procedure below provides the basic steps required to configure a standard waveform.

1. Set FgenOutput.OutputMode to OutputMode.Function.
2. Choose the type of waveform you would like to generate and configure it by calling FgenStandardWaveform.Configure.

Parent topic:

Configure Output Mode

Related information:

- OutputMode Enumeration
- FgenStandardWaveform.Configure Method

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialinitialize.html language=enus -->
## TOPIC 00018: Initialize

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialinitialize.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialinitialize.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Because you can have multiple signal generators connected to your computer, you must tell NI-FGEN which signal generator to communicate with by opening a session to the signal generator. A session establishes a connection between the signal generator and your application. After this connection is es

Initialize

Because you can have multiple signal generators connected to your computer, you must tell NI-FGEN which signal generator to communicate with by opening a session to the signal generator.

A session establishes a connection between the signal generator and your application. After this connection is established, the signal generator can transmit data to your application. Sessions also allow the driver to cache previous settings, which improves performance.

Initialize a new instance of the NIFgen class.

1. Set resourceName to the device identifier assigned to the signal generator in MAX. You can find or set the resource name for your signal generator by launching MAX and selecting Devices and Interfaces.
2. Use idQuery to specify whether or not to verify that NI-FGEN supports the device you initialize. Circumstances can arise where sending an ID query to the device is undesirable. When you set this parameter to 
 true, the method initializes the device without performing an ID query.
3. Reset the signal generator during initialization using reset.
4. Use the optionString parameter to create a simulated session, or to initialize the session with certain settings.

Parent topic:

NI-FGEN .NET API Tutorial

Related information:

- NIFgen Class

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutorialinitiategeneration.html language=enus -->
## TOPIC 00019: Initiate Generation

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutorialinitiategeneration.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutorialinitiategeneration.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: This step transitions the device from the committed state to the generation state. Once this transition has been made, the device is able to begin generating waveforms. Call NIFgen.InitiateGeneration to transition the device to the generation state.

Initiate Generation

This step transitions the device from the committed state to the generation state. Once this transition has been made, the device is able to begin generating waveforms.

NIFgen.InitiateGeneration

Parent topic:

NI-FGEN .NET API Tutorial

Related information:

- NIFgen.InitiateGeneration

<!--NI_TOPIC bundle=ni-fgen-.net-4.0-api-overview path=tutoriasettingattributes.html language=enus -->
## TOPIC 00020: Setting Driver Attributes Before Reading Driver Attributes

- bundle_id: `ni-fgen-.net-4.0-api-overview`
- source_path: `tutoriasettingattributes.html`
- source_url: https://docs-be.ni.com/bundle/ni-fgen-.net-4.0-api-overview/raw/resource/enus/tutoriasettingattributes.html
- document_id: `ni-fgen-.net-4.0-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: Properties are modified when you set them or when you call a configuration method that sets them. Perform all module configuration before writing data on output devices. It is important to set the properties or call any configuration methods before reading back any property values for the following

Setting Driver Attributes Before Reading Driver Attributes

Properties are modified when you set them or when you call a configuration method that sets them.

Note

1. Values read are coerced depending on the current configuration of the session. If you read a property value and then set other properties, the property value read may no longer be valid.
2. The driver verifies that the configuration of the device is valid at the time the property is read. It is possible to get an error when reading a property if the configuration is not valid at that point, even when a setting later could make it valid.
3. Reading properties causes the driver to verify the current configuration. If you change some of the settings later, those settings need to be validated again.

Parent topic:

Initiate Generation
