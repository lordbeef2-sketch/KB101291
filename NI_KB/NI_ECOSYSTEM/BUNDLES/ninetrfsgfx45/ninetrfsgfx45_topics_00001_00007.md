# NI DOCUMENT BUNDLE: ninetrfsgfx45

<!--NI_BUNDLE_CHUNK bundle=ninetrfsgfx45 start=1 end=7 -->
<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/mapping_rfsg.html language=enus -->
## TOPIC 00001: ninetrfsgfx45/xml/mapping_rfsg.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/mapping_rfsg.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/mapping_rfsg.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

Mapping the NI-RFSG .NET API to the NI-RFSG C API

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The following table maps the NI-RFSG .NET API members to the corresponding NI-RFSG C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIRfsg namespace.

| IVI .NET API Member | .NET API Member | .NET Object Hierarchy | C API Member |
| --- | --- | --- | --- |
|  | AdvancedPropertyAccessService Class |  |  |
|  | GetAttributeBoolean |  | niRFSG_GetAttributeViBoolean |
|  | GetAttributeDouble |  | niRFSG_GetAttributeViReal64 |
|  | GetAttributeInt32 |  | niRFSG_GetAttributeViInt32 |
|  | GetAttributeSession |  | niRFSG_GetAttributeViSession |
|  | GetAttributeString |  | niRFSG_GetAttributeViString |
|  | SetAttributeBoolean |  | niRFSG_SetAttributeViBoolean |
|  | SetAttributeDouble |  | niRFSG_SetAttributeViReal64 |
|  | SetAttributeInt32 |  | niRFSG_SetAttributeViInt32 |
|  | SetAttributeSession |  | niRFSG_SetAttributeViSession |
|  | SetAttributeString |  | niRFSG_SetAttributeViString |
|  | NIRfsg Class |  |  |
|  | Abort | rfsgSession.Abort | niRFSG_Abort |
|  | CheckGenerationStatus | rfsgSession.CheckGenerationStatus | niRFSG_CheckGenerationStatus |
| IIviDriver.Close | Close | rfsgSession.Close | niRFSG_close |
|  | Initiate | rfsgSession.Initiate | niRFSG_Initiate |
|  | RfsgAnalogModulation Class |  |  |
|  | AMSensitivity | rfsgSession.Modulation.AnalogModulation.AMSensitivity | NIRFSG_ATTR_ANALOG_MODULATION_AM_SENSITIVITY |
|  | FMBand | rfsgSession.Modulation.AnalogModulation.FMBand | NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND |
|  | FMDeviation | rfsgSession.Modulation.Analog.FMDeviation | NIRFSG_ATTR_ANALOG_MODULATION_FM_DEVIATION |
|  | FMNarrowbandIntegrator | rfsgSession.Modulation.AnalogModulation.FMNarrowbandIntegrator | NIRFSG_ATTR_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR |
|  | FMSensitivity | rfsgSession.Modulation.AnalogModulation.FMSensitivity | NIRFSG_ATTR_ANALOG_MODULATION_FM_SENSITIVITY |
|  | ModulationType | rfsgSession.Modulation.Analog.ModulationType | NIRFSG_ATTR_ANALOG_MODULATION_TYPE |
|  | PMDeviation | rfsgSession.Modulation.Analog.PMDeviation | NIRFSG_ATTR_ANALOG_MODULATION_PM_DEVIATION |
|  | PMMode | rfsgSession.Modulation.Analog.PMMode | NIRFSG_ATTR_ANALOG_MODULATION_PM_MODE |
|  | PMSensitivity | rfsgSession.Modulation.Analog.PMSensitivity | NIRFSG_ATTR_ANALOG_MODULATION_PM_SENSITIVITY |
|  | WaveformFrequency | rfsgSession.Modulation.Analog.WaveformFrequency | NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_FREQUENCY |
|  | WaveformType | rfsgSession.Modulation.Analog.WaveformType | NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_TYPE |
|  | RfsgArb Class |  |  |
|  | AbsoluteDelay | rfsgSession.Arb.AbsoluteDelay | NIRFSG_ATTR_ABSOLUTE_DELAY |
|  | BurstDetection | rfsgSession.Arb.BurstDetection | NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION |
|  | CarrierFrequency | rfsgSession.Arb.CarrierFrequency | NIRFSG_ATTR_ARB_CARRIER_FREQUENCY |
|  | DeviceInstantaneousBandwidth | rfsgSession.Arb.DeviceInstantaneousBandwidth | NIRFSG_ATTR_DEVICE_INSTANTANEOUS_BANDWIDTH |
|  | DigitalEqualizationEnabled | rfsgSession.Arb.DigitalEqualizationEnabled | NIRFSG_ATTR_DIGITAL_EQUALIZATION_ENABLED |
|  | DigitalGain | rfsgSession.Arb.DigitalGain | NIRFSG_ATTR_ARB_DIGITAL_GAIN |
|  | DigitalPatternEnabled | rfsgSession.Arb.DigitalPatternEnabled | NIRFSG_ATTR_DIGITAL_PATTERN |
|  | GenerationMode | rfsgSession.GenerationMode | NIRFSG_ATTR_GENERATION_MODE |
|  | InterpolationDelay | rfsgSession.Arb.InterpolationDelay | NIRFSG_ATTR_INTERPOLATION_DELAY |
|  | IQRate | rfsgSession.Arb. IQRate | NIRFSG_ATTR_IQ_RATE |
|  | IQSwapEnabled | rfsgSession.Arb.IQSwapEnabled | NIRFSG_ATTR_IQ_SWAP_ENABLED |
|  | IsWaveformRepeatCountFinite | rfsgSession.Arb.IsWaveformRepeatCountFinite | NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT_IS_FINITE |
|  | MemorySize | rfsgSession.Arb.MemorySize | NIRFSG_ATTR_MEMORY_SIZE |
|  | OutputPort | rfsgSession.Arb.OutputPort | NIRFSG_ATTR_OUTPUT_PORT |
|  | OverflowErrorReporting | rfsgSession.Arb.OverflowErrorReporting | NIRFSG_ATTR_OVERFLOW_ERROR_REPORTING |
|  | PhaseContinuityEnabled | rfsgSession.Arb.PhaseContinuityEnabled | NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED |
|  | Power | rfsgSession.Arb.Power | NIRFSG_ATTR_ARB_POWER |
|  | PreFilterGain | rfsgSession.Arb.PreFilterGain | NIRFSG_ATTR_ARB_PRE_FILTER_GAIN |
|  | RelativeDelay | rfsgSession.Arb.RelativeDelay | NIRFSG_ATTR_RELATIVE_DELAY |
|  | SelectedWaveform | rfsgSession.Arb. SelectedWaveform | NIRFSG_ATTR_ARB_SELECTED_WAVEFORM |
|  | SetArbWaveformNextWritePosition | rfsgSession.Arb.SetArbWaveformNextWritePosition | niRFSG_SetArbWaveformNextWritePosition |
|  | SignalBandwidth | rfsgSession.Arb.SignalBandwidth | NIRFSG_ATTR_SIGNAL_BANDWIDTH |
|  | WaveformRepeatCount | rfsgSession.Arb.WaveformRepeatCount | NIRFSG_ATTR_ARB_WAVEFORM_REPEAT_COUNT |
|  | WaveformSoftwareScalingFactor | rfsgSession.Arb.WaveformSoftwareScalingFactor | NIRFSG_ATTR_ARB_WAVEFORM_SOFTWARE_SCALING_FACTOR |
|  | AllocateWaveform | rfsgSession.Arb.AllocateWaveform | niRFSG_AllocateArbWaveform |
|  | CheckIfWaveformExists | rfsgSession.Arb.CheckIfWaveformExists | niRFSG_CheckIfWaveformExists |
|  | ClearAllWaveforms | rfsgSession.Arb.ClearAllWaveforms | niRFSG_ClearAllArbWaveforms |
|  | ClearWaveform | rfsgSession.Arb.ClearWaveform | niRFSG_ClearArbWaveform |
|  | WriteWaveform | rfsgSession.Arb.WriteWaveform | niRFSG_WriteArbWaveform |
|  | WriteWaveform<T> | rfsgSession.Arb.WriteWaveform<ComplexDouble> | niRFSG_WriteArbWaveformComplexF64 |
|  | WriteWaveform<T> | rfsgSession.Arb.WriteWaveform<ComplexInt16> | niRFSG_WriteArbWaveformComplexI16 |
|  | RfsgArbSampleClock Class |  |  |
|  | OnboardClockMode | rfsgSession.ArbSampleClock.OnboardClockMode | NIRFSG_ATTR_ARB_ONBOARD_SAMPLE_CLOCK_MODE |
|  | OscillatorPhaseDacValue | rfsgSession.ArbSampleClock.OscillatorPhaseDacValue | NIRFSG_ATTR_ARB_OSCILLATOR_PHASE_DAC_VALUE |
|  | Rate | rfsgSession.ArbSampleClock.Rate | NIRFSG_ATTR_ARB_SAMPLE_CLOCK_RATE |
|  | Source | rfsgSession.ArbSampleClock. Source | NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE |
|  | RfsgChannelBasedIQOutPort Class |  |  |
|  | CommonModeOffset | rfsgSession.IQOutPort[channelName].CommonModeOffset | NIRFSG_ATTR_IQ_OUT_PORT_COMMON_MODE_OFFSET |
|  | Level | rfsgSession.IQOutPort[channelName].Level | NIRFSG_ATTR_IQ_OUT_PORT_LEVEL |
|  | LoadImpedance | rfsgSession.IQOutPort[channelName].LoadImpedance | NIRFSG_ATTR_IQ_OUT_PORT_LOAD_IMPEDANCE |
|  | Offset | rfsgSession.IQOutPort[channelName].Offset | NIRFSG_ATTR_IQ_OUT_PORT_OFFSET |
|  | TerminalConfiguration | rfsgSession.IQOutPort[channelName].TerminalConfiguration | NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION |
|  | RfsgBasicConfigurationList Class |  |  |
|  | ActiveList | rfsgSession.BasicConfigurationList.ActiveList | NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST |
|  | ActiveStep | rfsgSession.BasicConfigurationList.ActiveStep | NIRFSG_ATTR_ACTIVE_CONFIGURATION_LIST_STEP |
|  | IsDone | rfsgSession.BasicConfigurationList.IsDone | NIRFSG_ATTR_CONFIGURATION_LIST_IS_DONE |
|  | Repeat | rfsgSession.BasicConfigurationList.Repeat | NIRFSG_ATTR_CONFIGURATION_LIST_REPEAT |
|  | StepInProgress | rfsgSession.BasicConfigurationList.StepInProgress | NIRFSG_ATTR_CONFIGURATION_LIST_STEP_IN_PROGRESS |
|  | CheckIfConfigurationListExists | rfsgSession.BasicConfigurationList.CheckIfConfigurationListExists | niRFSG_CheckIfConfigurationListExists |
|  | CreateConfigurationList | rfsgSession.BasicConfigurationList.CreateConfigurationList | niRFSG_CreateConfigurationList |
|  | CreateStep | rfsgSession.BasicConfigurationList.CreateStep | niRFSG_CreateConfigurationListStep |
|  | DeleteConfigurationList | rfsgSession.BasicConfigurationList.DeleteConfigurationList | niRFSG_DeleteConfigurationList |
|  | RfsgConfigurationListStepTrigger Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.Triggers.ConfigurationListStepTrigger.ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL |
|  | TerminalName | rfsgSession.Triggers.ConfigurationListStepTrigger.TerminalName | NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TERMINAL_NAME |
|  | TriggerType | rfsgSession.Triggers.ConfigurationListStepTrigger.TriggerType | NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE |
|  | Disable | rfsgSession.Triggers.ConfigurationListStepTrigger.Disable | niRFSG_DisableConfigurationListStepTrigger |
|  | RfsgConfigurationSettledEvent Class |  |  |
|  | OutputTerminal | rfsgSession.DeviceEvents.ConfigurationSettledEvent.OutputTerminal | NIRFSG_ATTR_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL |
|  | TerminalName | rfsgSession.DeviceEvents.ConfigurationSettledEvent.TerminalName | NIRFSG_ATTR_CONFIGURATION_SETTLED_EVENT_TERMINAL_NAME |
|  | RfsgDataTransfer Class |  |  |
|  | BlockSize | rfsgSession.DataTransfer.BlockSize | NIRFSG_ATTR_DATA_TRANSFER_BLOCK_SIZE |
|  | DirectDownloadEnabled | rfsgSession.DataTransfer.DirectDownloadEnabled | NIRFSG_ATTR_DIRECT_DOWNLOAD |
|  | MaximumBandwidth | rfsgSession.DataTransfer.MaximumBandwidth | NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_BANDWIDTH |
|  | RfsgDataTransferAdvanced Class |  |  |
|  | MaximumInFlightReadRequests | rfsgSession.DataTransfer.Advanced.MaximumInFlightReadRequests | NIRFSG_ATTR_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS |
|  | PreferredPacketSize | rfsgSession.DataTransfer.Advanced.PreferredPacketSize | NIRFSG_ATTR_DATA_TRANSFER_PREFERRED_PACKET_SIZE |
|  | RfsgDeembedding Class |  |  |
|  | ConfigureDeembeddingTableInterpolationLinear | rfsgSession.Deembedding.ConfigureDeembeddingTableInterpolationLinear | niRFSG_ConfigureDeembeddingTableInterpolationLinear |
|  | ConfigureDeembeddingTableInterpolationNearest | rfsgSession.Deembedding.CreateDeembeddingSParameterTableNearest | niRFSG_ConfigureDeembeddingTableInterpolationNearest |
|  | ConfigureDeembeddingTableInterpolationSpline | rfsgSession.Deembedding.ConfigureDeembeddingTableInterpolationSpline | niRFSG_ConfigureDeembeddingTableInterpolationSpline |
|  | CreateDeembeddingSParameterTableArray | rfsgSession.Deembedding.CreateDeembeddingSParameterTableArray | niRFSG_CreateDeembeddingSParameterTableArray |
|  | CreateDeembeddingSParameterTableS2pFile | rfsgSession.Deembedding.CreateDeembeddingSParameterTableS2pFile | niRFSG_CreateDeembeddingSParameterTableS2pFile |
|  | DeleteAllDeembeddingTables | rfsgSession.Deembedding.DeleteAllDeembeddingTables | niRFSG_DeleteAllDeembeddingTables |
|  | DeleteDeembeddingTable | rfsgSession.Deembedding.DeleteDeembeddingTable | niRFSG_DeleteDeembeddingTable |
|  | GetDeembeddingSParameters | rfsgSession.Deembedding.GetDeembeddingSParameters | niRFSG_GetDeembeddingSParameters |
|  | DeembeddingSelectedTable | rfsgSession.Deembedding.DeembeddingSelectedTable | NIRFSG_ATTR_DEEMBEDDING_SELECTED_TABLE |
|  | DeembeddingType | rfsgSession.Deembedding.DeembeddingType | NIRFSG_ATTR_DEEMBEDDING_TYPE |
|  | RfsgDeviceCharacteristics Class |  |  |
|  | AETemperature | rfsgSession.DeviceCharacteristics.AETemperature | NIRFSG_ATTR_AE_TEMPERATURE |
|  | FpgaBitfilePath | rfsgSession.DeviceCharacteristics.FpgaBitfilePath | NIRFSG_ATTR_FPGA_BITFILE_PATH |
|  | FpgaTargetName | rfsgSession.DeviceCharacteristics.FPGATargetName | NIRFSG_ATTR_FPGA_TARGET_NAME |
|  | FpgaTemperature | rfsgSession.DeviceCharacteristics.FpgaTemperature | NIRFSG_ATTR_FPGA_TEMPERATURE |
|  | AwgTemperature | rfsgSession.DeviceCharacteristics.AwgTemperature | NIRFSG_ATTR_ARB_TEMPERATURE |
|  | DeviceTemperature | rfsgSession.DeviceCharacteristics.DeviceTemperature | NIRFSG_ATTR_DEVICE_TEMPERATURE |
|  | LOTemperature | rfsgSession.DeviceCharacteristics.LOTemperature | NIRFSG_ATTR_LO_TEMPERATURE |
|  | ModulePowerConsumption | rfsgSession.DeviceCharacteristics.ModulePowerConsumption | NIRFSG_ATTR_MODULE_POWER_CONSUMPTION |
|  | ModuleRevision | rfsgSession.DeviceCharacteristics.ModuleRevision | NIRFSG_ATTR_MODULE_REVISION |
|  | TemperatureReadInterval | rfsgSession.DeviceCharacteristics.TemperatureReadInterval | NIRFSG_ATTR_TEMPERATURE_READ_INTERVAL |
|  | RfsgDeviceCharactersticsOptions Class |  |  |
|  | FastTuningOption | rfsgSession.DeviceCharacteristics.Option.FastTuningOption | NIRFSG_ATTR_FAST_TUNING_OPTION |
|  | RfsgDeviceEvents Class |  |  |
|  | Delay | rfsgSession.DeviceEvents.Delay | NIRFSG_ATTR_EVENTS_DELAY |
|  | RfsgDigitalEdgeConfigurationListStepTrigger Class |  |  |
|  | Edge | rfsgSession.Triggers.ConfigurationListStepTrigger.DigitalEdge.Edge | NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_EDGE |
|  | Source | rfsgSession.Triggers.ConfigurationListStepTrigger.DigitalEdge.Source | NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE |
|  | Configure | rfsgSession.Triggers.ConfigurationListStepTrigger.DigitalEdge.Configure | niRFSG_ConfigureDigitalEdgeConfigurationListStepTrigger |
|  | RfsgDigitalEdgeScriptTrigger Class |  |  |
|  | Edge | rfsgSession.Triggers.ScriptTriggers[index].DigitalEdge.Edge | NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE |
|  | Source | rfsgSession.Triggers.ScriptTriggers[index].DigitalEdge.Source | NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE |
|  | Configure | rfsgSession.Triggers.ScriptTriggers[index].DigitalEdge. Configure | niRFSG_ConfigureDigitalEdgeScriptTrigger |
|  | RfsgDigitalEdgeStartTrigger Class |  |  |
|  | Edge | rfsgSession.Triggers.StartTrigger. Edge | NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE |
|  | Source | rfsgSession.Triggers.StartTrigger.Source | NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE |
|  | Configure | rfsgSession.Triggers.StartTrigger.Configure | niRFSG_ConfigureDigitalEdgeStartTrigger |
|  | RfsgDigitalLevelScriptTrigger Class |  |  |
|  | Level | rfsgSession.Triggers.ScriptTriggers[index]. Level | NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL |
|  | Source | rfsgSession.Triggers.ScriptTriggers[index]. Source | NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE |
|  | Configure | rfsgSession.Triggers.ScriptTriggers[index]. Configure | niRFSG_ConfigureDigitalLevelScriptTrigger |
|  | RfsgDigitalModulation Class |  |  |
|  | FskDeviation | rfsgSession.Modulation.Digital.FskDeviation | NIRFSG_ATTR_DIGITAL_MODULATION_FSK_DEVIATION |
|  | ModulationType | rfsgSession.Modulation.Digital.ModulationType | NIRFSG_ATTR_DIGITAL_MODULATION_TYPE |
|  | PrbsOrder | rfsgSession.Modulation.Digital.PrbsOrder | NIRFSG_ATTR_DIGITAL_MODULATION_PRBS_ORDER |
|  | PrbsSeed | rfsgSession.Modulation.Digital.PrbsSeed | NIRFSG_ATTR_DIGITAL_MODULATION_PRBS_SEED |
|  | SymbolRate | rfsgSession.Modulation.Digital.SymbolRate | NIRFSG_ATTR_DIGITAL_MODULATION_SYMBOL_RATE |
|  | WaveformType | rfsgSession.Modulation.Digital.WaveformType | NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE |
|  | ConfigureUserDefinedWaveform | rfsgSession.Modulation.Digital.ConfigureUserDefinedWaveform | niRFSG_ConfigureDigitalModulationUserDefinedWaveform |
|  |  |  |  |
|  | RfsgDoneEvent Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.DeviceEvents.DoneEvent.ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL |
|  | TerminalName | rfsgSession.DeviceEvents.DoneEvent.TerminalName | NIRFSG_ATTR_DONE_EVENT_TERMINAL_NAME |
|  | RfsgDriverIdentity Class |  |  |
| IIviComponentIdentity.Description | Description | rfsgSession.Identity.Description | NIRFSG_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| IIviDriverIdentity.Identifier | Identifier | rfsgSession.Identity.Identifier | NIRFSG_ATTR_SERIAL_NUMBER |
| IIviDriverIdentity.InstrumentFirmwareRevision | InstrumentFirmwareRevision | rfsgSession.Identity.InstrumentFirmwareRevision | NIRFSG_ATTR_INSTRUMENT_FIRMWARE_REVISION |
| IIviDriverIdentity.InstrumentManufacturer | InstrumentManufacturer | rfsgSession.Identity.InstrumentManufacturer | NIRFSG_ATTR_INSTRUMENT_MANUFACTURER |
| IIviDriverIdentity.InstrumentModel | InstrumentModel | rfsgSession.Identity.InstrumentModel | NIRFSG_ATTR_INSTRUMENT_MODEL |
| IIviComponentIdentity.Revision | Revision | rfsgSession.Identity.Revision | NIRFSG_ATTR_SPECIFIC_DRIVER_REVISION |
|  | SpecificDriverMajorVersion | rfsgSession.Identity.SpecificDriverMajorVersion | NIRFSG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION |
|  | SpecificDriverMinorVersion | rfsgSession.Identity.SpecificDriverMinorVersion | NIRFSG_ATTR_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION |
| IIviComponentIdentity.Vendor | Vendor | rfsgSession.Identity.Vendor | NIRFSG_ATTR_SPECIFIC_DRIVER_VENDOR |
| IIviDriverIdentity.GetGroupCapabilities | GetGroupCapabilities | rfsgSession.Identity.GetGroupCapabilities | NIRFSG_ATTR_GROUP_CAPABILITIES |
| IIviDriverIdentity.GetSupportedInstrumentModels | GetSupportedInstrumentModels | rfsgSession.Identity.GetSupportedInstrumentModels | NIRFSG_ATTR_SUPPORTED_INSTRUMENT_MODELS |
|  | RevisionQuery | rfsgSession.Identity.RevisionQuery | niRFSG_revision_query |
|  | RfsgDriverOperation Class |  |  |
| IIviDriverOperation.Cache | Cache | rfsgSession.DriverOperation.Cache | NIRFSG_ATTR_CACHE |
| IIviDriverOperation.DriverSetup | DriverSetup | rfsgSession.DriverOperation.DriverSetup | NIRFSG_ATTR_DRIVER_SETUP |
|  | InterchangeCheck | rfsgSession.DriverOperation.InterchangeCheck | NIRFSG_ATTR_INTERCHANGE_CHECK |
| IIviDriverOperation.IOResourceDescriptor | IOResourceDescriptor | rfsgSession.DriverOperation.IOResourceDescriptor | NIRFSG_ATTR_IO_RESOURCE_DESCRIPTOR |
| IIviDriverOperation.LogicalName | LogicalName | rfsgSession.DriverOperation.LogicalName | NIRFSG_ATTR_LOGICAL_NAME |
| IIviDriverOperation.QueryInstrumentStatus | QueryInstrumentStatus | rfsgSession.DriverOperation.QueryInstrumentStatus | NIRFSG_ATTR_QUERY_INSTRUMENT_STATUS |
| IIviDriverOperation.RangeCheck | RangeCheck | rfsgSession.DriverOperation.RangeCheck | NIRFSG_ATTR_RANGE_CHECK |
|  | RecordCoercions | rfsgSession.DriverOperation.RecordCoercions | NIRFSG_ATTR_RECORD_COERCIONS |
| IIviDriverOperation.Simulate | Simulate | rfsgSession.DriverOperation.Simulate | NIRFSG_ATTR_SIMULATE |
| IIviDriverOperation.InvalidateAllAttributes | InvalidateAllAttributes | rfsgSession.DriverOperation.InvalidateAllAttributes | niRFSG_InvalidateAllAttributes |
|  | RfsgDriverUtility Class |  |  |
|  | Commit | rfsgSession.Utility.Commit | niRFSG_Commit |
| IIviDriverUtility.Disable | Disable | rfsgSession.Utility.Disable | niRFSG_Disable |
|  | PerformPowerSearch | rfsgSession.Utility.PerformPowerSearch | niRFSG_PerformPowerSearch |
|  | PerformThermalCorrection | rfsgSession.Utility.PerformThermalCorrection | niRFSG_PerformThermalCorrection |
| IIviDriverUtility.Reset | Reset | rfsgSession.Utility.Reset | niRFSG_reset |
|  | ResetAttribute | rfsgSession.Utility.ResetAttribute | niRFSG_ResetAttribute |
|  | ResetDevice | rfsgSession.Utility.ResetDevice | niRFSG_ResetDevice |
| IIviDriverUtility.ResetWithDefaults | ResetWithDefaults | rfsgSession.Utility.ResetWithDefaults | niRFSG_ResetWithDefaults |
| IIviDriverUtility.SelfTest | SelfTest | rfsgSession.Utility.SelfTest | niRFSG_self_test |
|  | WaitUntilSettled | rfsgSession.Utility.WaitUntilSettled | niRFSG_WaitUntilSettled |
|  | RfsgFrequencyReference Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.FrequencyReference.ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL |
|  | PxiChassisClock10Source | rfsgSession.FrequencyReference.PxiChassisClock10Source | NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE |
|  | Rate | rfsgSession.FrequencyReference.Rate | NIRFSG_ATTR_REF_CLOCK_RATE |
|  | Source | rfsgSession.FrequencyReference.Source | NIRFSG_ATTR_REF_CLOCK_SOURCE |
|  | Configure | rfsgSession.FrequencyReference.Configure | niRFSG_ConfigureRefClock |
|  | RfsgIQImpairment Class |  |  |
|  | Enabled | rfsgSession.IQImpairments.Enabled | NIRFSG_ATTR_IQ_IMPAIRMENT_ENABLED |
|  | GainImbalance | rfsgSession.IQImpairments.GainImbalance | NIRFSG_ATTR_IQ_GAIN_IMBALANCE |
|  | IOffset | rfsgSession.IQImpairments.IOffset | NIRFSG_ATTR_IQ_I_OFFSET |
|  | OffsetUnits | rfsgSession.IQImpairments.OffsetUnits | NIRFSG_ATTR_OFFSET_UNITS |
|  | QOffset | rfsgSession.IQImpairments.QOffset | NIRFSG_ATTR_IQ_Q_OFFSET |
|  | Skew | rfsgSession.IQImpairments.Skew | NIRFSG_ATTR_IQ_SKEW |
|  | RfsgIQOutPort Class |  |  |
|  | CarrierFrequency | rfsgSession.IQOutPort.CarrierFrequency | NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY |
|  | Temperature | rfsgSession.IQOutPort.Temperature | NIRFSG_ATTR_IQ_OUT_PORT_TEMPERATURE |
|  | RfsgMarkerEvent Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.DeviceEvents.MarkerEvents[index].ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL |
|  | OutputBehavior | rfsgSession.DeviceEvents.MarkerEvents[index].OutputBehaviour | NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR |
|  | PulseWidth | rfsgSession.DeviceEvents.MarkerEvents[index].PulseWidth | NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH |
|  | PulseWidthUnits | rfsgSession.DeviceEvents.MarkerEvents[index].PulseWidthUnits | NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS |
|  | TerminalName | rfsgSession.DeviceEvents.MarkerEvents[index].TerminalName | NIRFSG_ATTR_MARKER_EVENT_TERMINAL_NAME |
|  | ToggleInitialState | rfsgSession.DeviceEvents.MarkerEvents[index].ToggleInitialState | NIRFSG_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE |
|  | RfsgPulseShaping Class |  |  |
|  | Filter | rfsgSession.Arb.PulseShaping.Filter | NIRFSG_ATTR_ARB_FILTER_TYPE |
|  | RaisedCosineAlpha | rfsgSession.Arb.PulseShaping.RaisedCosineAlpha | NIRFSG_ATTR_ARB_FILTER_RAISED_COSINE_ALPHA |
|  | RootRaisedCosineAlpha | rfsgSession.Arb.PulseShaping.RootRaisedCosineAlpha | NIRFSG_ATTR_ARB_FILTER_ROOT_RAISED_COSINE_ALPHA |
|  | RfsgRF Class |  |  |
|  | ExternalGain | rfsgSession.RF.ExternalGain | NIRFSG_ATTR_EXTERNAL_GAIN |
|  | Frequency | rfsgSession.RF.Frequency | NIRFSG_ATTR_FREQUENCY |
|  | OutputEnabled | rfsgSession.RF.OutputEnabled | NIRFSG_ATTR_OUTPUT_ENABLED |
|  | PhaseOffset | rfsgSession.RF.PhaseOffset | NIRFSG_ATTR_PHASE_OFFSET |
|  | PowerLevel | rfsgSession.RF.PowerLevel | NIRFSG_ATTR_POWER_LEVEL |
|  | PowerLevelType | rfsgSession.RF.PowerLevelType | NIRFSG_ATTR_POWER_LEVEL_TYPE |
|  | RFBlankingSource | rfsgSession.RF.RFBlankingSource | NIRFSG_ATTR_RF_BLANKING_SOURCE |
|  | Configure | rfsgSession.RF.Configure | niRFSG_ConfigureRF |
|  | RfsgRFAdvanced Class |  |  |
|  | AlcControl | rfsgSession.RF.Advanced.AlcControl | NIRFSG_ATTR_ALC_CONTROL |
|  | AllowOutOfSpecificationUserSettings | rfsgSession.RF.Advanced.AllowOutOfSpecificationUserSettings | NIRFSG_ATTR_ALLOW_OUT_OF_SPECIFICATION_USER_SETTINGS |
|  | AmplificationPath | rfsgSession.RF.Advanced.AmplificationPath | NIRFSG_ATTR_AMP_PATH |
|  | AmplitudeSettling | rfsgSession.RF.Advanced.AmplitudeSettling | NIRFSG_ATTR_AMPLITUDE_SETTLING |
|  | AttenuatorHoldEnabled | rfsgSession.RF.Advanced.AttenuatorHoldEnabled | NIRFSG_ATTR_ATTENUATOR_HOLD_ENABLED |
|  | AttenuatorHoldMaximumPower | rfsgSession.RF.Advanced.AttenuatorHoldMaximumPower | NIRFSG_ATTR_ATTENUATOR_HOLD_MAX_POWER |
|  | AttenuatorSetting | rfsgSession.RF.Advanced.AttenuatorSetting | NIRFSG_ATTR_ATTENUATOR_SETTING |
|  | AutomaticThermalCorrection | rfsgSession.RF.Advanced.AutomaticThermalCorrection | NIRFSG_ATTR_AUTOMATIC_THERMAL_CORRECTION |
|  | AutoPowerSearch | rfsgSession.RF.Advanced.AutoPowerSearch | NIRFSG_ATTR_AUTO_POWER_SEARCH |
|  | CorrectionTemperature | rfsgSession.RF.Advanced.CorrectionTemperature | NIRFSG_ATTR_CORRECTION_TEMPERATURE |
|  | FrequencySettlingTime | rfsgSession.RF.Advanced.FrequencySettlingTime | NIRFSG_ATTR_FREQUENCY_SETTLING |
|  | FrequencySettlingUnits | rfsgSession.RF.Advanced.FrequencySettlingUnits | NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS |
|  | FrequencyTolerance | rfsgSession.RF.Advanced.FrequencyTolerance | NIRFSG_ATTR_FREQUENCY_TOLERANCE |
|  | LoopBandwidth | rfsgSession.RF.Advanced.LoopBandwidth | NIRFSG_ATTR_LOOP_BANDWIDTH |
|  | PeakEnvelopePower | rfsgSession.RF.Advanced.PeakEnvelopePower | NIRFSG_ATTR_PEAK_ENVELOPE_POWER |
|  | PeakPowerAdjustment | rfsgSession.RF.Advanced.PeakPowerAdjustment | NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT |
|  | PeakPowerAdjustmentInheritance | rfsgSession.RF.Advanced.PeakPowerAdjustmentInheritance | NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT_INHERITANCE |
|  | PulseModulationEnabled | rfsgSession.RF.Advanced.PulseModulationEnabled | NIRFSG_ATTR_PULSE_MODULATION_ENABLED |
|  | PulseModulationMode | rfsgSession.RF.Advanced.PulseModulationMode | NIRFSG_ATTR_PULSE_MODULATION_MODE |
|  | ReferencePllBandwidth | rfsgSession.RF.Advanced.ReferencePllBandwidth | NIRFSG_ATTR_REF_PLL_BANDWIDTH |
|  | ThermalCorrectionTemperature Resolution | rfsgSession.RF.Advanced.ThermalCorrectionTemperatureResolution | NIRFSG_ATTR_THERMAL_CORRECTION_TEMPERATURE_RESOLUTION |
|  | ThermalCorrectionHeadroomRange | rfsgSession.RF.Advanced.ThermalCorrectionHeadroomRange | NIRFSG_ATTR_THERMAL_CORRECTION_HEADROOM_RANGE |
|  | YigMainCoilDrive | rfsgSession.RF.Advanced.YigMainCoilDrive | NIRFSG_ATTR_YIG_MAIN_COIL_DRIVE |
|  | RfsgRFLocalOscillator Class |  |  |
|  | FrequencyStepSize | rfsgSession.RF.LocalOscillator.FrequencyStepSize | NIRFSG_ATTR_LO_FREQUENCY_STEP_SIZE |
|  | LOFrequency | rfsgSession.RF.LOFrequency | NIRFSG_ATTR_LO_FREQUENCY |
|  | LOInPower | rfsgSession.RF.LocalOscillator.LOInPower | NIRFSG_ATTR_LO_IN_POWER |
|  | LOOutEnabled | rfsgSession.RF.LocalOscillator.LOOutEnabled | NIRFSG_ATTR_LO_OUT_ENABLED |
|  | LOOutPower | rfsgSession.RF.LocalOscillator.LOOutPower | NIRFSG_ATTR_LO_OUT_POWER |
|  | LOVcoFrequencyStepSize | rfsgSession.RF.LOVcoFrequencyStepSize | NIRFSG_ATTR_LO_VCO_FREQUENCY_STEP_SIZE |
|  | PllFractionalModeEnabled | rfsgSession.RF.LocalOscillator.PllFractionalModeEnabled | NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED |
|  | Source | rfsgSession.RF.LocalOscillator.Source | NIRFSG_ATTR_LO_SOURCE |
|  | RfsgScripting Class |  |  |
|  | SelectedScriptName | rfsgSession.Arb.Scripting.SelectedScriptName | NIRFSG_ATTR_SELECTED_SCRIPT |
|  | CheckIfScriptExists | rfsgSession.Arb.Scripting.CheckIfScriptExists | niRFSG_CheckIfScriptExists |
|  | WriteScript | rfsgSession.Arb.Scripting.WriteScript | niRFSG_WriteScript |
|  | RfsgScriptTrigger Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.Triggers.ScriptTriggers[index].ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL |
|  | TerminalName | rfsgSession.Triggers.ScriptTriggers[index].TerminalName | NIRFSG_ATTR_SCRIPT_TRIGGER_TERMINAL_NAME |
|  | TriggerType | rfsgSession.Triggers.ScriptTriggers[index].TriggerType | NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE |
|  | ConfigureSoftwareTrigger | rfsgSession.Triggers.ScriptTriggers[index].ConfigureSoftwareTrigger | niRFSG_ConfigureSoftwareScriptTrigger |
|  | Disable | rfsgSession.Triggers.ScriptTriggers[index].Disable | niRFSG_DisableScriptTrigger |
|  | SendSoftwareEdgeTrigger | rfsgSession.Triggers.ScriptTriggers[index].SendSoftwareEdgeTrigger | niRFSG_SendSoftwareEdgeTrigger |
|  | RfsgSelfCalibration Class |  |  |
|  | AlignLODaisyChain5840 | rfsgSession.Calibration.Self.AlignLODaisyChain5840 | niRFSG_5840_AlignLODaisyChain |
|  | LastSelfCalibrationTemperature | rfsgSession.Calibration.Self.LastSelfCalibrationTemperature | NIRFSG_ATTR_SELF_CALIBRATION_TEMPERATURE |
|  | GetSelfCalibrationLastDateAndTime | rfsgSession.Calibration.Self.GetSelfCalibrationLastDateAndTime | niRFSG_GetSelfCalibrationDateAndTime |
|  | GetSelfCalibrationTemperature | rfsgSession.Calibration.Self.GetSelfCalibrationTemperature | niRFSG_GetSelfCalibrationTemperature |
|  | SelfCalibrate | rfsgSession.Calibration.Self.SelfCalibrate | niRFSG_SelfCal |
|  | SelfCalibrateRange | rfsgSession.Calibration.Self.SelfCalibrateRange | niRFSG_SelfCalibrateRange |
|  | RfsgSignalPath Class |  |  |
|  | AvailablePorts | rfsgSession.SignalPath.AvailablePorts | NIRFSG_ATTR_AVAILABLE_PORTS |
|  | SelectedPorts | rfsgSession.SignalPath.SelectedPorts | NIRFSG_ATTR_SELECTED_PORTS |
|  | RfsgStartedEvent Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.DeviceEvents.StartedEvent.ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL |
|  | TerminalName | rfsgSession.DeviceEvents.StartedEvent.TerminalName | NIRFSG_ATTR_STARTED_EVENT_TERMINAL_NAME |
|  | RfsgStartTrigger Class |  |  |
|  | ExportedOutputTerminal | rfsgSession.Triggers.StartTrigger.ExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL |
|  | TerminalName | rfsgSession.Triggers.StartTrigger.TerminalName | NIRFSG_ATTR_START_TRIGGER_TERMINAL_NAME |
|  | TriggerType | rfsgSession.Triggers.StartTrigger.TriggerType | NIRFSG_ATTR_START_TRIGGER_TYPE |
|  | ConfigureSoftwareTrigger | rfsgSession.Triggers.StartTrigger.ConfigureSoftwareTrigger | niRFSG_ConfigureSoftwareStartTrigger |
|  | Disable | rfsgSession.Triggers.StartTrigger.Disable | niRFSG_DisableStartTrigger |
|  | SendSoftwareEdgeTrigger | rfsgSession.Triggers.StartTrigger.SendSoftwareEdgeTrigger | niRFSG_SendSoftwareEdgeTrigger |
|  | RfsgSynchronizedSampleClock Class |  |  |
|  | DistributionLine | rfsgSession.ArbSampleClock.Synchronized.DistributionLine | NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE |
|  | IsMaster | rfsgSession.ArbSampleClock.Synchronized.IsMaster | NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_MASTER |
|  | RfsgStreaming Class |  |  |
|  | SpaceAvailableInWaveform | rfsgSession.Arb.DataTransfer.Streaming.SpaceAvailableInWaveform | NIRFSG_ATTR_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM |
|  | StreamingEnabled | rfsgSession.Arb.DataTransfer.Streaming.StreamingEnabled | NIRFSG_ATTR_STREAMING_ENABLED |
|  | StreamingWaveformName | rfsgSession.Arb.DataTransfer.Streaming.StreamingWaveformName | NIRFSG_ATTR_STREAMING_WAVEFORM_NAME |
|  | WriteTimeout | rfsgSession.Arb.DataTransfer.Streaming.WriteTimeout | NIRFSG_ATTR_STREAMING_WRITE_TIMEOUT |
|  | RfsgSynchronizedScriptTrigger Class |  |  |
|  | DistributionLine | rfsgSession.Triggers.ScriptTriggers[index].Synchronized.DistributionLine | NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_DIST_LINE |
|  | IsMaster | rfsgSession.Triggers.ScriptTriggers[index].Synchronized.IsMaster | NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_MASTER |
|  | RfsgSynchronizedStartTrigger Class |  |  |
|  | DistributionLine | rfsgSession.Triggers.StartTrigger.Synchronized.DistributionLine | NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_DIST_LINE |
|  | IsMaster | rfsgSession.Triggers.StartTrigger.Synchronized.IsMaster | NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_MASTER |
|  | RfsgTimerEvent Class |  |  |
|  | Interval | rfsgSession.DeviceEvents.Timer.Interval | NIRFSG_ATTR_TIMER_EVENT_INTERVAL |
|  | RfsgUpconverter Class |  |  |
|  | CenterFrequency | rfsgSession.RF.Upconverter.CenterFrequency | NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY |
|  | FrequencyOffset | rfsgSession.RF.Upconverter.CenterFrequency | NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET |
|  | FrequencyOffsetMode | rfsgSession.RF.Upconverter.FrequencyOffsetMode | NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE |
|  | Gain | rfsgSession.RF.Upconverter.Gain | NIRFSG_ATTR_UPCONVERTER_GAIN |
|  | RfsgWaveformCapabilities Class |  |  |
|  | MaximumNumberOfWaveforms | rfsgSession.Arb.WaveformCapabilities.MaximumNumberOfWaveforms | NIRFSG_ATTR_ARB_MAX_NUMBER_WAVEFORMS |
|  | WaveformQuantum | rfsgSession.Arb.WaveformCapabilities.WaveformQuantum | NIRFSG_ATTR_ARB_WAVEFORM_QUANTUM |
|  | WaveformSizeMaximum | rfsgSession.Arb.WaveformCapabilities.WaveformSizeMaximum | NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MAX |
|  | WaveformSizeMinimum | rfsgSession.Arb.WaveformCapabilities.WaveformSizeMinimum | NIRFSG_ATTR_ARB_WAVEFORM_SIZE_MIN |

[IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Concepts

Using the RFSG .NET Library

<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/mapping_rfsg_enums.html language=enus -->
## TOPIC 00002: ninetrfsgfx45/xml/mapping_rfsg_enums.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/mapping_rfsg_enums.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/mapping_rfsg_enums.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

Mapping the NI-RFSG .NET API Enums and Enum Values to the NI-RFSG C API Attributes/Functions and Values

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The following table maps the NI-RFSG .NET API enums and enum values to the corresponding NI-RFSG C API attributes/functions and values. All .NET members are in the NationalInstruments.ModularInstruments.NIRfsg namespace.

| .NET API Enums and Enum Values | C API Attributes/Functions and Values |
| --- | --- |
| RfsgAlcControl | NIRFSG_ATTR_ALC_CONTROL |
| Disable | NIRFSG_VAL_DISABLE |
| Enable | NIRFSG_VAL_ENABLE |
| RfsgAmplificationPath | NIRFSG_ATTR_AMP_PATH |
| HighPower | NIRFSG_VAL_HIGH_POWER |
| LowHarmonic | NIRFSG_VAL_LOW_HARMONIC |
| RfsgAnalogModulationFMBand | NIRFSG_ATTR_ANALOG_MODULATION_FM_BAND |
| Narrowband | NIRFSG_VAL_NARROWBAND |
| Wideband | NIRFSG_VAL_WIDEBAND |
| RfsgAnalogModulationFMNarrowbandIntegrator | NIRFSG_ATTR_ANALOG_MODULATION_FM_NARROWBAND_INTEGRATOR |
| FMNarrowband100HzTo1KHz | NIRFSG_VAL_100HZ_TO_1KHZ |
| FMNarrowband10KHzTo100KHz | NIRFSG_VAL_10KHZ_TO_100KHZ |
| FMNarrowband1KHzTo10KHz | NIRFSG_VAL_1KHZ_TO_10KHZ |
| RfsgAnalogModulationPMMode | NIRFSG_ATTR_ANALOG_MODULATION_PM_MODE |
| HighDeviation | NIRFSG_VAL_HIGH_DEVIATION |
| LowPhaseNoise | NIRFSG_VAL_LOW_PHASE_NOISE |
| RfsgAnalogModulationType | NIRFSG_ATTR_ANALOG_MODULATION_TYPE |
| AM | NIRFSG_VAL_AM |
| FM | NIRFSG_VAL_FM |
| None | NIRFSG_VAL_NONE |
| PM | NIRFSG_VAL_PM |
| RfsgAnalogModulationWaveformType | NIRFSG_ATTR_ANALOG_MODULATION_WAVEFORM_TYPE |
| Sine | NIRFSG_VAL_SINE |
| Square | NIRFSG_VAL_SQUARE |
| Triangle | NIRFSG_VAL_TRIANGLE |
| RfsgArbWaveformRelativeWritePosition | niRFSG_SetArbWaveformNextWritePosition |
| StartOfWaveform | NIRFSG_VAL_START_OF_WAVEFORM |
| CurrentPosition | NIRFSG_VAL_CURRENT_POSITION |
| RfsgAutoPowerSearch | NIRFSG_ATTR_AUTO_POWER_SEARCH |
| Disable | NIRFSG_VAL_DISABLE |
| Enable | NIRFSG_VAL_ENABLE |
| RfsgBasicConfigurationListRepeat | NIRFSG_ATTR_CONFIGURATION_LIST_REPEAT |
| Continuous | NIRFSG_VAL_CONFIGURATION_LIST_REPEAT_CONTINUOUS |
| Single | NIRFSG_VAL_CONFIGURATION_LIST_REPEAT_SINGLE |
| RfsgBurstDetectionEnabled | NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION |
| Enabled | NIRFSG_VAL_ENABLE |
| Disabled | NIRFSG_VAL_DISABLE |
| RfsgBurstDetectionMode | NIRFSG_ATTR_WRITE_WAVEFORM_BURST_DETECTION_MODE |
| Auto | NIRFSG_VAL_AUTO |
| Auto | NIRFSG_VAL_MANUAL |
| RfsgConfigurationListProperties | niRFSG_CreateConfigurationList |
| Frequency | NIRFSG_ATTR_FREQUENCY |
| PowerLevel | NIRFSG_ATTR_POWER_LEVEL |
| PhaseOffset | NIRFSG_ATTR_PHASE_OFFSET |
| TimerEventInterval | NIRFSG_ATTR_TIMER_EVENT_INTERVAL |
| FrequencySettlingTime | NIRFSG_ATTR_FREQUENCY_SETTLING |
| AlcControl | NIRFSG_ATTR_ALC_CONTROL |
| AmplificationPath | NIRFSG_ATTR_AMP_PATH |
| AmplitudeSettling | NIRFSG_ATTR_AMPLITUDE_SETTLING |
| AttenuatorSetting | NIRFSG_ATTR_ATTENUATOR_SETTING |
| AutoPowerSearch | NIRFSG_ATTR_AUTO_POWER_SEARCH |
| IQOutPortCarrierFrequency | NIRFSG_ATTR_IQ_OUT_PORT_CARRIER_FREQUENCY |
| IQOutPortLevel | NIRFSG_ATTR_IQ_OUT_PORT_LEVEL |
| IQOutPortOffset | NIRFSG_ATTR_IQ_OUT_PORT_OFFSET |
| IQOutPortCommonModeOffset | NIRFSG_ATTR_IQ_OUT_PORT_COMMON_MODE_OFFSET |
| OutputEnabled | NIRFSG_ATTR_OUTPUT_ENABLED |
| PulseModulationEnabled | NIRFSG_ATTR_PULSE_MODULATION_ENABLED |
| UpconverterCenterFrequency | NIRFSG_ATTR_UPCONVERTER_CENTER_FREQUENCY |
| ArbDigitalGain | NIRFSG_ATTR_ARB_DIGITAL_GAIN |
| OverflowErrorReporting | NIRFSG_ATTR_OVERFLOW_ERROR_REPORTING |
| Disabled | NIRFSG_VAL_ERROR_REPORTING_DISABLED |
| Warning | NIRFSG_VAL_ERROR_REPORTING_WARNING |
| RfsgConfigurationListStepTriggerType | NIRFSG_ATTR_CONFIGURATION_LIST_STEP_TRIGGER_TYPE |
| DigitalEdge | NIRFSG_VAL_DIGITAL_EDGE |
| None | NIRFSG_VAL_NONE |
| RfsgDeembeddingType | NIRFSG_ATTR_DEEMBEDDING_TYPE |
| None | NIRFSG_VAL_DEEMBEDDING_TYPE_NONE |
| Scalar | NIRFSG_VAL_DEEMBEDDING_TYPE_SCALAR |
| Vector | NIRFSG_VAL_DEEMBEDDING_TYPE_VECTOR |
| RfsgDeviceModule | niRFSG_GetSelfCalibrationDateAndTime |
| Awg | NIRFSG_VAL_AWG |
| LO | NIRFSG_VAL_LO |
| PrimaryModule | NIRFSG_VAL_PRIMARY_MODULE |
| RfsgDigitalModulationType | NIRFSG_ATTR_DIGITAL_MODULATION_TYPE |
| Fsk | NIRFSG_VAL_FSK |
| None | NIRFSG_VAL_NONE |
| Ook | NIRFSG_VAL_OOK |
| Psk | NIRFSG_VAL_PSK |
| RfsgDigitalModulationWaveformType | NIRFSG_ATTR_DIGITAL_MODULATION_WAVEFORM_TYPE |
| Prbs | NIRFSG_VAL_PRBS |
| UserDefined | NIRFSG_VAL_USER_DEFINED |
| RfsgFilterType | NIRFSG_ATTR_ARB_FILTER_TYPE |
| None | NIRFSG_VAL_ARB_FILTER_TYPE_NONE |
| RaisedCosine | NIRFSG_VAL_ARB_FILTER_TYPE_RAISED_COSINE |
| RootRaisedCosine | NIRFSG_VAL_ARB_FILTER_TYPE_ROOT_RAISED_COSINE |
| RfsgGenerationStatus | niRFSG_CheckGenerationStatus |
| InProgress | VI_TRUE |
| Complete | VI_FALSE |
| RfsgIQOffsetUnits | NIRFSG_ATTR_OFFSET_UNITS |
| Percentage | NIRFSG_VAL_PERCENT |
| Volts | NIRFSG_VAL_VOLTS |
| RfsgLinearInterpolationFormat | niRFSG_ConfigureDeembeddingTableInterpolationLinear |
| RealAndImaginary | NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_REAL_AND_IMAGINARY |
| MagnitudeAndPhase | NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_AND_PHASE |
| MagnitudeInDecibelAndPhase | NIRFSG_VAL_LINEAR_INTERPOLATION_FORMAT_MAGNITUDE_DB_AND_PHASE |
| RfsgLoadConfigurationsFromFileLoadOptions | NIRFSG_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS |
| SkipNone | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_NONE |
| SkipWaveforms | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_LOAD_OPTIONS_SKIP_WAVEFORMS |
| RfsgLoadConfigurationsFromFileResetOptions | NIRFSG_ATTR_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS |
| SkipNone | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_NONE |
| SkipWaveforms | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_WAVEFORMS |
| SkipScripts | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_SCRIPTS |
| SkipDeembeddingTables | RFSG_VAL_LOAD_CONFIGURATIONS_FROM_FILE_RESET_OPTIONS_SKIP_DEEMBEDDING_TABLES |
| RfsgLoopBandwidth | NIRFSG_ATTR_LOOP_BANDWIDTH |
| High | NIRFSG_VAL_HIGH |
| Low | NIRFSG_VAL_LOW |
| Medium | NIRFSG_VAL_MEDIUM |
| Narrow | NIRFSG_VAL_NARROW |
| Wide | NIRFSG_VAL_WIDE |
| RfsgLOOutExportConfigureFromRfsa | NIRFSG_ATTR_LO_OUT_EXPORT_CONFIGURE_FROM_RFSA |
| Disabled | NIRFSG_VAL_ENABLE |
| Enabled | NIRFSG_VAL_DISABLE |
| RfsgLOPllFractionalModeEnabled | NIRFSG_ATTR_LO_PLL_FRACTIONAL_MODE_ENABLED |
| Enable | NIRFSG_VAL_ENABLE |
| Disable | NIRFSG_VAL_DISABLE |
| RfsgMarkerEventOutputBehaviour | NIRFSG_ATTR_MARKER_EVENT_OUTPUT_BEHAVIOR |
| Pulse | NIRFSG_VAL_PULSE |
| Toggle | NIRFSG_VAL_TOGGLE |
| RfsgMarkerEventPulseWidthUnits | NIRFSG_ATTR_MARKER_EVENT_PULSE_WIDTH_UNITS |
| Seconds | NIRFSG_VAL_SECONDS |
| SampleClockPeriods | NIRFSG_VAL_SAMPLE_CLOCK_PERIODS |
| RfsgMarkerEventToggleInitialState | NIRFSG_ATTR_MARKER_EVENT_TOGGLE_INITIAL_STATE |
| DigitalLow | NIRFSG_VAL_DIGITAL_LOW |
| DigitalHigh | NIRFSG_VAL_DIGITAL_HIGH |
| RfsgModule | niRFSG_GetSelfCalibrationTemperature |
| PrimaryModule | NIRFSG_VAL_PRIMARY_MODULE |
| Awg | NIRFSG_VAL_AWG |
| LO | NIRFSG_VAL_LO |
| RfsgOnboardSampleClockMode | NIRFSG_ATTR_ARB_ONBOARD_SAMPLE_CLOCK_MODE |
| DivideDown | NIRFSG_VAL_DIVIDE_DOWN |
| HighResolution | NIRFSG_VAL_HIGH_RESOLUTION |
| RfsgOutputPort | NIRFSG_ATTR_OUTPUT_PORT |
| CalOut | NIRFSG_VAL_CAL_OUT |
| IOnly | NIRFSG_VAL_I_ONLY |
| IQOut | NIRFSG_VAL_IQ_OUT |
| RFOut | NIRFSG_VAL_RF_OUT |
| RfsgOverflowErrorReporting | NIRFSG_ATTR_OVERFLOW_ERROR_REPORTING |
| Warning | NIRFSG_VAL_ERROR_REPORTING_WARNING |
| Disabled | NIRFSG_VAL_ERROR_REPORTING_DISABLED |
| RfsgPeakPowerAdjustmentInheritance | NIRFSG_ATTR_PEAK_POWER_ADJUSTMENT_INHERITANCE |
| ExactMatch | NIRFSG_VAL_EXACT_MATCH |
| Minimum | NIRFSG_VAL_MINIMUM |
| Maximum | NIRFSG_VAL_MAXIMUM |
| RfsgPhaseContinuityEnabled | NIRFSG_ATTR_PHASE_CONTINUITY_ENABLED |
| Auto | NIRFSG_VAL_AUTO |
| Disabled | NIRFSG_VAL_DISABLE |
| Enabled | NIRFSG_VAL_ENABLE |
| RfsgPulseModulationMode | NIRFSG_ATTR_PULSE_MODULATION_MODE |
| HighIsolation | NIRFSG_VAL_HIGH_ISOLATION |
| OptimalMatch | NIRFSG_VAL_OPTIMAL_MATCH |
| RfsgReferencePllBandwidth | NIRFSG_ATTR_REF_PLL_BANDWIDTH |
| High | NIRFSG_VAL_HIGH |
| Low | NIRFSG_VAL_LOW |
| Medium | NIRFSG_VAL_MEDIUM |
| RfsgResetStepsToOmit | niRFSG_ResetWithOptions |
| None | NIRFSG_VAL_RESET_WITH_OPTIONS_NONE |
| Waveforms | NIRFSG_VAL_RESET_WITH_OPTIONS_WAVEFORMS |
| Scripts | NIRFSG_VAL_RESET_WITH_OPTIONS_SCRIPTS |
| Routes | NIRFSG_VAL_RESET_WITH_OPTIONS_ROUTES |
| DeembeddingTables | NIRFSG_VAL_RESET_WITH_OPTIONS_DEEMBEDDING_TABLES |
| RfsgRFBlanking | NIRFSG_ATTR_WAVEFORM_RF_BLANKING |
| Disable | NIRFSG_VAL_DISABLE |
| Enable | NIRFSG_VAL_ENABLE |
| RfsgRFFrequencySettlingUnits | NIRFSG_ATTR_FREQUENCY_SETTLING_UNITS |
| Ppm | NIRFSG_VAL_PPM |
| TimeAfterIO | NIRFSG_VAL_TIME_AFTER_IO |
| TimeAfterLock | NIRFSG_VAL_TIME_AFTER_LOCK |
| RfsgRFInLOExportEnabled | NIRFSG_ATTR_RF_IN_LO_EXPORT_ENABLED |
| Unspecified | NIRFSG_VAL_UNSPECIFIED |
| Disabled | NIRFSG_VAL_DISABLE |
| Enabled | NIRFSG_VAL_ENABLE |
| RfsgRFPortType | niRFSG_5840_AlignLODaisyChain |
| PortRFIn | NIRFSG_VAL_PORT_RF_IN |
| PortRFIn | NIRFSG_VAL_PORT_RF_OUT |
| RfsgRFPowerLevelType | NIRFSG_ATTR_POWER_LEVEL_TYPE |
| AveragePower | NIRFSG_VAL_AVERAGE_POWER |
| PeakPower | NIRFSG_VAL_PEAK_POWER |
| RfsgScriptTriggerType | NIRFSG_ATTR_SCRIPT_TRIGGER_TYPE |
| DigitalEdge | NIRFSG_VAL_DIGITAL_EDGE |
| DigitalLevel | NIRFSG_VAL_DIGITAL_LEVEL |
| None | NIRFSG_VAL_NONE |
| Software | NIRFSG_VAL_SOFTWARE |
| RfsgSelfCalibrationSteps | niRFSG_SelfCalibrateRange |
| ImageSuppression | NIRFSG_VAL_SELF_CAL_IMAGE_SUPPRESSION |
| LOSelfCal | NIRFSG_VAL_SELF_CAL_LO_SELF_CAL |
| OmitNone | NIRFSG_VAL_SELF_CAL_OMIT_NONE |
| PowerLevelAccuracy | NIRFSG_VAL_SELF_CAL_POWER_LEVEL_ACCURACY |
| ResidualLOPower | NIRFSG_VAL_SELF_CAL_RESIDUAL_LO_POWER |
| SynthesizerAlignment | NIRFSG_VAL_SELF_CAL_SYNTHESIZER_ALIGNMENT |
| RfsgSignalType |  |
| StartTrigger | NIRFSG_VAL_START_TRIGGER |
| ScriptTrigger | NIRFSG_VAL_SCRIPT_TRIGGER |
| MarkerEvent | NIRFSG_VAL_MARKER_EVENT |
| ReferenceClock | NIRFSG_VAL_REF_CLOCK |
| StartedEvent | NIRFSG_VAL_STARTED_EVENT |
| DoneEvent | NIRFSG_VAL_DONE_EVENT |
| ConfigurationListStepTrigger | NIRFSG_VAL_CONFIGURATION_LIST_STEP_TRIGGER |
| ConfigurationSettledEvent | NIRFSG_VAL_CONFIGURATION_SETTLED_EVENT |
| RfsgSparameterOrientation | niRFSG_CreateDeembeddingSparameterTableS2PFile |
| Port1TowardsDut | NIRFSG_VAL_PORT1_TOWARDS_DUT |
| Port2TowardsDut | NIRFSG_VAL_PORT2_TOWARDS_DUT |
| RfsgStartTriggerType | NIRFSG_ATTR_START_TRIGGER_TYPE |
| DigitalEdge | NIRFSG_VAL_DIGITAL_EDGE |
| None | NIRFSG_VAL_NONE |
| Software | NIRFSG_VAL_SOFTWARE |
| RfsgTerminalConfiguration | NIRFSG_ATTR_IQ_OUT_PORT_TERMINAL_CONFIGURATION |
| Differential | NIRFSG_VAL_DIFFERENTIAL |
| SingleEnded | NIRFSG_VAL_SINGLE_ENDED |
| RfsgTriggerEdge | NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE |
| FallingEdge | NIRFSG_VAL_FALLING_EDGE |
| RisingEdge | NIRFSG_VAL_RISING_EDGE |
| RfsgTriggerLevel | NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL |
| ActiveHigh | NIRFSG_VAL_ACTIVE_HIGH |
| ActiveLow | NIRFSG_VAL_ACTIVE_LOW |
| RfsgWaveformGenerationMode | NIRFSG_ATTR_GENERATION_MODE |
| ContinuousWave | NIRFSG_VAL_CW |
| ArbitraryWaveform | NIRFSG_VAL_ARB_WAVEFORM |
| Script | NIRFSG_VAL_SCRIPT |
| RfsgWriteWaveformNormalization | NIRFSG_ATTR_WRITE_WAVEFORM_NORMALIZATION |
| Enabled | NIRFSG_VAL_ENABLE |
| Disabled | NIRFSG_VAL_DISABLE |
| RfsgYigMainCoilDriveType | NIRFSG_ATTR_YIG_MAIN_COIL_DRIVE |
| Fast | NIRFSG_VAL_FAST |
| Slow | NIRFSG_VAL_SLOW |
| UpconverterFrequencyOffsetMode | NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE |
| Auto | NIRFSG_VAL_AUTO |
| UserDefined | NIRFSG_VAL_USER_DEFINED |
| Enabled | NIRFSG_VAL_ENABLE |

| .Net API Utility Classes for Predefined Strings | C API Attributes and Values |
| --- | --- |
| RfsgArbSampleClockSource | NIRFSG_ATTR_ARB_SAMPLE_CLOCK_SOURCE |
| ClockIn | NIRFSG_VAL_ONBOARD_CLK_STR |
| OnboardClock | NIRFSG_VAL_CLK_IN_STR |
| RfsgConfigurationListStepTriggerExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_CONFIGURATION_LIST_STEP_TRIGGER_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| RfsgConfigurationSettledEventExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_CONFIGURATION_SETTLED_EVENT_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| TriggerOutputTerminal | NIRFSG_VAL_TRIG_OUT_STR |
| RfsgDigitalEdgeConfigurationListStepTriggerSource | NIRFSG_ATTR_DIGITAL_EDGE_CONFIGURATION_LIST_STEP_TRIGGER_SOURCE |
| Marker0Event | NIRFSG_VAL_MARKER0_EVENT_STR |
| Marker1Event | NIRFSG_VAL_MARKER1_EVENT_STR |
| Marker2Event | NIRFSG_VAL_MARKER2_EVENT_STR |
| Marker3Event | NIRFSG_VAL_MARKER3_EVENT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| PXIeDStarB | NIRFSG_VAL_PXIE_DSTARB_STR |
| TimerEvent | NIRFSG_VAL_TIMER_EVENT_STR |
| TriggerInputTerminal | NIRFSG_VAL_TRIG_IN_STR |
| RfsgDigitalEdgeScriptTriggerSource | NIRFSG_ATTR_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| Pfi2 | NIRFSG_VAL_PFI2_STR |
| Pfi3 | NIRFSG_VAL_PFI3_STR |
| PxiStarLine | NIRFSG_VAL_PXI_STAR_STR |
| PXIeDStarB | NIRFSG_VAL_PXIE_DSTARB_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| RfsgDigitalEdgeStartTriggerSource | NIRFSG_ATTR_DIGITAL_EDGE_START_TRIGGER_SOURCE |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| Pfi2 | NIRFSG_VAL_PFI2_STR |
| Pfi3 | NIRFSG_VAL_PFI3_STR |
| PxiStarLine | NIRFSG_VAL_PXI_STAR_STR |
| PXIeDStarB | NIRFSG_VAL_PXIE_DSTARB_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| SynchronizationStartTriggerLine | NIRFSG_VAL_SYNC_START_TRIGGER_STR |
| TriggerInputTerminal | NIRFSG_VAL_TRIG_IN_STR |
| RfsgDigitalLevelScriptTriggerSource | NIRFSG_ATTR_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| Pfi2 | NIRFSG_VAL_PFI2_STR |
| Pfi3 | NIRFSG_VAL_PFI3_STR |
| PxiStarLine | NIRFSG_VAL_PXI_STAR_STR |
| PXIeDStarB | NIRFSG_VAL_PXIE_DSTARB_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| SynchronizationStartTriggerLine | NIRFSG_VAL_SYNC_START_TRIGGER_STR |
| RfsgDoneEventExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_DONE_EVENT_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| RfsgFrequencyReferenceExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_REF_CLOCK_OUTPUT_TERMINAL |
| ClockOut | NIRFSG_VAL_CLK_OUT_STR |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| ReferenceOut | NIRFSG_VAL_REF_OUT_STR |
| ReferenceOut2 | NIRFSG_VAL_REF_OUT2_STR |
| RfsgFrequencyReferenceSource | NIRFSG_ATTR_REF_CLOCK_SOURCE |
| ClockIn | NIRFSG_VAL_CLK_IN_STR |
| OnboardClock | NIRFSG_VAL_ONBOARD_CLOCK_STR |
| PxiClock | NIRFSG_VAL_PXI_CLK_STR |
| ReferenceIn | NIRFSG_VAL_REF_IN_STR |
| RfsgLocalOscillatorSource | NIRFSG_ATTR_LO_SOURCE |
| OnboardClock | NIRFSG_VAL_LO_SOURCE_ONBOARD_STR |
| LOIn | NIRFSG_VAL_LO_SOURCE_LO_IN_STR |
| Secondary | NIRFSG_VAL_SECONDARY |
| SGSAShared | NIRFSG_VAL_SG_SA_SHARED |
| RfsgMarkerEventExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_MARKER_EVENT_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| RfsgPxiChassisClock10Source | NIRFSG_ATTR_PXI_CHASSIS_CLK10_SOURCE |
| None | NIRFSG_VAL_NONE_STR |
| OnboardClock | NIRFSG_VAL_ONBOARD_CLOCK_STR |
| ReferenceIn | NIRFSG_VAL_REF_IN_STR |
| RfsgRFBlankingSource | NIRFSG_ATTR_RF_BLANKING_SOURCE |
| Disable | "" |
| Marker0 | NIRFSG_VAL_MARKER0 |
| Marker1 | NIRFSG_VAL_MARKER1 |
| Marker2 | NIRFSG_VAL_MARKER2 |
| Marker3 | NIRFSG_VAL_MARKER3 |
| RfsgScriptTriggerExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| TriggerOutputTerminal | NIRFSG_VAL_TRIG_OUT_STR |
| RfsgStartedEventExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_STARTED_EVENT_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| RfsgStartTriggerExportedOutputTerminal | NIRFSG_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| Pfi1 | NIRFSG_VAL_PFI1_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PXIeDStarC | NIRFSG_VAL_PXIE_DSTARC_STR |
| TriggerOutputTerminal | NIRFSG_VAL_TRIG_OUT_STR |
| RfsgSynchronizedSampleClockDistributionLine | NIRFSG_ATTR_SYNC_SAMPLE_CLOCK_DIST_LINE |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| RfsgSynchronizedScriptTriggerDistributionLine | NIRFSG_ATTR_SYNC_SCRIPT_TRIGGER_DIST_LINE |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| RfsgSynchronizedStartTriggerDistributionLine | NIRFSG_ATTR_SYNC_START_TRIGGER_DIST_LINE |
| DoNotExport | NIRFSG_VAL_DO_NOT_EXPORT_STR |
| Pfi0 | NIRFSG_VAL_PFI0_STR |
| PxiTriggerLine0 | NIRFSG_VAL_PXI_TRIG0_STR |
| PxiTriggerLine1 | NIRFSG_VAL_PXI_TRIG1_STR |
| PxiTriggerLine2 | NIRFSG_VAL_PXI_TRIG2_STR |
| PxiTriggerLine3 | NIRFSG_VAL_PXI_TRIG3_STR |
| PxiTriggerLine4 | NIRFSG_VAL_PXI_TRIG4_STR |
| PxiTriggerLine5 | NIRFSG_VAL_PXI_TRIG5_STR |
| PxiTriggerLine6 | NIRFSG_VAL_PXI_TRIG6_STR |
| PxiTriggerLine7 | NIRFSG_VAL_PXI_TRIG7_STR |
| RfsgUpconverterFrequencyOffsetMode | NIRFSG_ATTR_UPCONVERTER_FREQUENCY_OFFSET_MODE |
| Auto | NIRFSG_VAL_AUTOMATIC |
| UserDefined | NIRFSG_VAL_USER_DEFINED |
| Enable | NIRFSG_VAL_ENABLED |

[IMAGE alt='image' src='../icons/collapse_all.gif']See Also

###### Concepts

Using the NI-RFSG .NET Library

<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/rfsgbasicusage.html language=enus -->
## TOPIC 00003: ninetrfsgfx45/xml/rfsgbasicusage.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/rfsgbasicusage.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/rfsgbasicusage.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

Basic Usage

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

1. Initialization : Use a constructor to create a new instance of the NIRfsg class. 
 You must create an instance of this class before you can call into the underlying NI-RFSG driver. 
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETDim session As New NIRfsg(resourceName, True, False) ' Initialize [IMAGE alt='image' src='../icons/copycode.gif']CopyC#NIRfsg session = new NIRfsg(resourceName, true, false); // Initialize
2. Configuration : Use the NIRfsg object to configure the waveform properties.
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETDim session As New NIRfsg(resourceName, True, False) ' Initialize
session.RF.Configure(10000000.0, -10)
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave
session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10000000.0) [IMAGE alt='image' src='../icons/copycode.gif']CopyC#NIRfsg session = new NIRfsg(resourceName, true, false); // Initialize
session.RF.Configure(10E6, -10);
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave;
session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10E6);
3. Initiate : The NI-RFSG device starts generating the configured waveform signal as soon as you initiate the signal generation, unless the NI-RFSG driver is waiting for a trigger.
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETsession.Initiate() [IMAGE alt='image' src='../icons/copycode.gif']CopyC#session.Initiate();
4. Check generation status : Check whether the device is generating the signal or has stopped generating the signal. You use this step to check for any errors that might occur during signal generation or to check whether the device has completed the signal generation.
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETsession.CheckGenerationStatus() [IMAGE alt='image' src='../icons/copycode.gif']CopyC#session.CheckGenerationStatus();
5. Close : Close the session to the device and free unmanaged resources that are held by the session. You can close the session with Close or Dispose .
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETsession.Close()
 or
session.Dispose()
 or 
Using session As New NIRfsg(resourceName, True, True)
 'User code goes here. 
End Using [IMAGE alt='image' src='../icons/copycode.gif']CopyC#session.Close();
 or
session.Dispose();
 or
using (NIRfsg session = new NIRfsg(resourceName, true, true))
{
 // User code goes here.
}

The following code snippet generates a basic waveform:

[IMAGE alt='image' src='../icons/copycode.gif']

```text
Using session As New NIRfsg(resourceName, True, True) 
    session.RF.Configure(10000000.0, -10)
    session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave
    session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10000000.0)
    session.Initiate()
End Using
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
using (NIRfsg session = new NIRfsg(resourceName, true, true))
{
    session.RF.Configure(10E6, -10);
    session.Arb.GenerationMode = RfsgWaveformGenerationMode.ContinuousWave;
    session.FrequencyReference.Configure(RfsgFrequencyReferenceSource.ClockIn, 10E6);
    session.Initiate();
}
```

<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/rfsgenumandoutputterminals.html language=enus -->
## TOPIC 00004: ninetrfsgfx45/xml/rfsgenumandoutputterminals.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/rfsgenumandoutputterminals.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/rfsgenumandoutputterminals.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

Using Predefined or Custom Values for Source and Output Terminal Properties

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']How Do I Set the Source and Output Terminal Properties?

There are certain properties, such as trigger sources, clock sources, and output terminals, that work with a set of predefined string values, but might also accept 
 custom values. For this you can use the utility classes that are part of the NI-Rfsg .NET API. 
 
 For example, the Source property in RfsgDigitalEdgeStartTrigger specifies an RfsgDigitalEdgeStartTriggerSource object.
 You can configure Source using one of the 
 predefined values, such as:

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.Pfi0
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.Pfi0;
```

Similarly, you can configure the ExportedOutputTerminal property using one of the 
 predefined values, such as:

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.DeviceEvents.DoneEvent.ExportedOutputTerminal = RfsgDoneEventExportedOutputTerminal.Pfi0
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.DeviceEvents.DoneEvent.ExportedOutputTerminal = RfsgDoneEventExportedOutputTerminal.Pfi0;
```

You can also create a custom value with the static FromString method.

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.FromString("CustomSource")
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = RfsgDigitalEdgeStartTriggerSource.FromString("CustomSource");
```

You can also directly set the source as a string instead of using the FromString method.

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = "CustomSource"
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = "CustomSource";
```

[IMAGE alt='image' src='../icons/collapse_all.gif']How Do I Get the Underlying String from Source or Output Terminal Value?

You can use the implicit conversion operator for conversion from and to string. Alternatively, you can also use the ToString method. For example, the following code shows how to retrieve the source name:

[IMAGE alt='image' src='../icons/copycode.gif']

```text
Dim triggerSource As String = RfsgDigitalEdgeStartTriggerSource.Pfi0
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
string triggerSource = RfsgDigitalEdgeStartTriggerSource.Pfi0;
```

You can use the underlying source value if you want to assign a trigger source to the same source as an output terminal.

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = (string)session.DeviceEvents.DoneEvent.ExportedOutputTerminal
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.Triggers.StartTrigger.DigitalEdge.Source = CType(session.DeviceEvents.DoneEvent.ExportedOutputTerminal, String);
```

<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/rfsgerrorwarning.html language=enus -->
## TOPIC 00005: ninetrfsgfx45/xml/rfsgerrorwarning.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/rfsgerrorwarning.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/rfsgerrorwarning.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

How Do I Manage Errors and Warnings in the NI-RFSG .NET Class Library?

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

The underlying NI-RFSG driver reports errors or warning through the function return values. Negative return values indicate errors whereas positive values indicate warnings.

[IMAGE alt='image' src='../icons/collapse_all.gif']How Do I Manage Errors in the NI-RFSG .NET Class Library?

The NI-RFSG .NET class library converts the error codes into exceptions.
 All exceptions are either .NET defined or IVI defined; none of them are custom exceptions. 
 The exception message for driver errors has the driver error code appended at the end.

[IMAGE alt='image' src='../icons/collapse_all.gif']How Do I Manage Warnings in the NI-RFSG .NET Class Library?

The NI-RFSG .NET class library converts the warning codes into events. 
 To receive warnings, you must subscribe to the Warning event as follows:

[IMAGE alt='image' src='../icons/copycode.gif']

```text
AddHandler session.DriverOperation.Warning, AddressOf Me.DriverOperation_Warning

Private Sub DriverOperation_Warning(ByVal sender As Object, ByVal e As RfsgWarningEventArgs)
    'User code goes here 
End Sub
```

[IMAGE alt='image' src='../icons/copycode.gif']

```text
session.DriverOperation.Warning += new EventHandler<RfsgWarningEventArgs>(DriverOperation_Warning);

void DriverOperation_Warning(object sender, RfsgWarningEventArgs e)
{
    //User code goes here
}
```

| Note: |
| --- |
| National Instruments recommends subscribing to the warning event immediate after creating the NIRfsg object, in order to avoid missing any warnings that might occur. |

The RfsgWarningEventArgs class contains a read-only property to get the RfsgWarning object out. For ease-of-use, it also gives direct access to the warning’s Code and Message.

RfsgWarning is an immutable class and hence its Equals method and the == operator are overloaded to compare values and not references.

The warning message for a particular warning code is dynamically generated by the driver, so it is possible for a warning with same code to have different messages. Even though the default behavior of Equals is to check value equality of both the Code and the Message, there exists an overload of the Equals method, which allows the user to ignore the Message while comparing two warnings.

<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/rfsgwritewaveform.html language=enus -->
## TOPIC 00006: ninetrfsgfx45/xml/rfsgwritewaveform.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/rfsgwritewaveform.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/rfsgwritewaveform.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

Writing Waveforms in NI-RFSG .NET Class Libraries

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

You can use one of the WriteWaveform methods to write waveform data to the onboard memory of an NI-RFSG device.

In order to write a waveform to the onboard memory, you use the Arb property. Use the following steps to write the waveform:

1. Set Generation Mode : Set the device in either ArbitraryWaveform mode or Script mode.
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETDim session As New NIRfsg(resourceName, True, False)
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ArbitraryWaveform [IMAGE alt='image' src='../icons/copycode.gif']CopyC#NIRfsg session = new NIRfsg(resourceName, true, false);
session.Arb.GenerationMode = RfsgWaveformGenerationMode.ArbitraryWaveform;
2. Allocate Waveform : National Instruments recommends allocating the onboard memory before writing the data into it.
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETsession.Arb.AllocateWaveform("waveformName", 1000) [IMAGE alt='image' src='../icons/copycode.gif']CopyC#session.Arb.AllocateWaveform("waveformName", 1000);
3. Write Waveform : Write waveform into the onboard memory. You can write one or more waveforms into the onboard memory; however, you can play only one waveform in the ArbitraryWaveform mode. Select this waveform using the SelectedWaveform property.
 You can use Script mode to generate multiple arbitrary waveforms based on the selected script. 
 
 [IMAGE alt='image' src='../icons/copycode.gif']CopyVB.NETDim dataArray As ComplexInt16() = New ComplexInt16(100) {}
For i as Short = 0 To dataArray.Length -1
 dataArray(i).Real = 1
 dataArray(i).Imaginary = 0 
Next
session.Arb.WriteWaveform(Of ComplexInt16)("waveformName", dataArray) [IMAGE alt='image' src='../icons/copycode.gif']CopyC#ComplexInt16[] dataArray = new ComplexInt16[100];
for (short i = 0; i < dataArray.Length; i++)
{
 dataArray[i].Real = 1;
 dataArray[i].Imaginary = 0;
}
session.Arb.WriteWaveform<ComplexInt16>("waveformName", dataArray);

<!--NI_TOPIC bundle=ninetrfsgfx45 path=ninetrfsgfx45/xml/using_ninet_rfsg.html language=enus -->
## TOPIC 00007: ninetrfsgfx45/xml/using_ninet_rfsg.html

- bundle_id: `ninetrfsgfx45`
- source_path: `ninetrfsgfx45/xml/using_ninet_rfsg.html`
- source_url: https://docs-be.ni.com/bundle/ninetrfsgfx45/raw/resource/enus/ninetrfsgfx45/xml/using_ninet_rfsg.html
- document_id: `ninetrfsgfx45`
- page_type: `leaf`
- content_type: ``

NI-RFSG .NET Class Library Help

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/collapse_all.gif']

[IMAGE alt='image' src='../icons/expand_all.gif']

[IMAGE alt='image' src='../icons/dropdown.gif']

[IMAGE alt='image' src='../icons/dropdownhover.gif']

[IMAGE alt='image' src='../icons/copycode.gif']

[IMAGE alt='image' src='../icons/copycodehighlight.gif']

You can use the NIRfsg .NET class library to initialize, configure, and generate from your NI-RFSG device.

| Note: |
| --- |
| Help for IVI Foundation interfaces is not provided. You must use the IntelliSense help. |

###### In This Section

- **Basic Usage**
  - Describes how to generate a waveform using the NI-RFSG .NET class library.
- **Using Predefined or Custom Values for Source and Output Terminal Properties**
  - Describes how to set source and output terminal properties.
- **How Do I Manage Errors and Warnings in the NI-RFSG .NET Class Library?**
  - Describes how to manage errors and warnings in the RFSG .NET class library.
- **Writing Waveforms in NI-RFSG .NET class library**
  - Describes how to write waveforms in NI-RFSG .NET class library.
- **Mapping the NI-RFSG .NET API to the NI-RFSG C API and IVI-RFSG .NET API**
  - Maps the NI-RFSG .NET API members to the corresponding NI-RFSG C API and IVI-RFSG .NET API members.
- **Mapping the NI-RFSG .NET API Enums and Enum Values to the NI-RFSG C API Attributes/Functions and Values**
  - Maps the NI-RFSG .NET API enums and enum values to the corresponding NI-RFSG C API attributes/functions and values.
