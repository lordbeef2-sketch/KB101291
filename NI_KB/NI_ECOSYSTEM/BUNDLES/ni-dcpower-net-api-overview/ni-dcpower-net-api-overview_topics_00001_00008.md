# NI DOCUMENT BUNDLE: ni-dcpower-net-api-overview

<!--NI_BUNDLE_CHUNK bundle=ni-dcpower-net-api-overview start=1 end=8 -->
<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerapimap.html language=enus -->
## TOPIC 00001: Mapping the NI-DC Power .NET API to the NI-DC Power C API

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerapimap.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerapimap.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-DCPower .NET API members to the corresponding NI-DCPower C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIDCPower namespace. IVI .NET API Member .NET API Member C API Member DCPowerAdvanced Class AuxiliaryPowerSource

Mapping the NI-DC Power .NET API to the NI-DC Power C API

The following table maps the NI-DCPower .NET API members to the corresponding NI-DCPower C API and IVI .NET API members. All .NET members are in the NationalInstruments.ModularInstruments.NIDCPower namespace.

| IVI .NET API Member | .NET API Member | C API Member |
| --- | --- | --- |
|  | DCPowerAdvanced Class |  |
|  | AuxiliaryPowerSourceAvailable | NIDCPOWER_ATTR_AUXILIARY_POWER_SOURCE_AVAILABLE |
|  | PowerSource | NIDCPOWER_ATTR_POWER_SOURCE |
|  | PowerSourceInUse | NIDCPOWER_ATTR_POWER_SOURCE_IN_USE |
|  | DCPowerCalibrationUtility Class |  |
|  | ReadCurrentTemperature | niDCPower_ReadCurrentTemperature |
|  | DCPowerControl Class |  |
|  | Abort | niDCPower_Abort |
|  | Commit | niDCPower_Commit |
|  | Initiate | niDCPower_Initiate |
|  | DCPowerDigitalEdgeMeasureTrigger Class |  |
|  | Edge | NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE |
|  | InputTerminal | NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_INPUT_TERMINAL |
|  | Configure | niDCPower_ConfigureDigitalEdgeMeasureTrigger |
|  | DCPowerDigitalEdgePulseTrigger Class |  |
|  | Edge | NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_EDGE |
|  | InputTerminal | NIDCPOWER_ATTR_DIGITAL_EDGE_PULSE_TRIGGER_INPUT_TERMINAL |
|  | Configure | niDCPower_ConfigureDigitalEdgePulseTrigger |
|  | DCPowerDigitalEdgeShutdownTrigger Class |  |
|  | Edge | NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_EDGE |
|  | InputTerminal | NIDCPOWER_ATTR_DIGITAL_EDGE_SHUTDOWN_TRIGGER_INPUT_TERMINAL |
|  | Configure | niDCPower_ConfigureDigitalEdgeShutdownTrigger |
|  | DCPowerDigitalEdgeSourceTrigger Class |  |
|  | Edge | NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_EDGE |
|  | InputTerminal | NIDCPOWER_ATTR_DIGITAL_EDGE_SOURCE_TRIGGER_INPUT_TERMINAL |
|  | Configure | niDCPower_ConfigureDigitalEdgeSourceTrigger |
|  | DCPowerDigitalEdgeStartTrigger Class |  |
|  | Edge | NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_EDGE |
|  | InputTerminal | NIDCPOWER_ATTR_DIGITAL_EDGE_START_TRIGGER_INPUT_TERMINAL |
|  | Configure | niDCPower_ConfigureDigitalEdgeStartTrigger |
|  | DCPowerDriverIdentity Class |  |
| IIviComponentIdentity.Description | Description | NIDCPOWER_ATTR_SPECIFIC_DRIVER_DESCRIPTION |
| IIviDriverIdentity.Identifier | Identifier |  |
| IIviDriverIdentity.InstrumentFirmwareRevision | InstrumentFirmwareRevision | NIDCPOWER_ATTR_INSTRUMENT_FIRMWARE_REVISION |
| IIviDriverIdentity.InstrumentManufacturer | InstrumentManufacturer | NIDCPOWER_ATTR_INSTRUMENT_MANUFACTURER |
| IIviDriverIdentity.InstrumentModel | InstrumentModel | NIDCPOWER_ATTR_INSTRUMENT_MODEL |
| IIviComponentIdentity.Revision | Revision | NIDCPOWER_ATTR_SPECIFIC_DRIVER_REVISION |
|  | SerialNumber | NIDCPOWER_ATTR_SERIAL_NUMBER |
| IIviDriverIdentity.SpecificationMajorVersion | SpecificationMajorVersion |  |
| IIviDriverIdentity.SpecificationMinorVersion | SpecificationMinorVersion |  |
| IIviComponentIdentity.Vendor | Vendor | NIDCPOWER_ATTR_SPECIFIC_DRIVER_VENDOR |
| IIviDriverIdentity.GetGroupCapabilities() | GetGroupCapabilities | NIDCPOWER_ATTR_GROUP_CAPABILITIES |
| IIviDriverIdentity.GetSupportedInstrumentModels() | GetSupportedInstrumentModels | NIDCPOWER_ATTR_SUPPORTED_INSTRUMENT_MODELS |
|  | DCPowerDriverOperation Class |  |
| IIviDriverOperation.Cache | Cache | NIDCPOWER_ATTR_CACHE |
| IIviDriverOperation.DriverSetup | DriverSetup | NIDCPOWER_ATTR_DRIVER_SETUP |
| IIviDriverOperation.InterchangeCheck | InterchangeCheck |  |
| IIviDriverOperation.IOResourceDescriptor | IOResourceDescriptor | NIDCPOWER_ATTR_IO_RESOURCE_DESCRIPTOR |
| IIviDriverOperation.Simulate | Simulate | NIDCPOWER_ATTR_SIMULATE |
| IIviDriverOperation.LogicalName | LogicalName | NIDCPOWER_ATTR_LOGICAL_NAME |
| IIviDriverOperation.QueryInstrumentStatus | QueryInstrumentStatus | NIDCPOWER_ATTR_QUERY_INSTRUMENT_STATUS |
| IIviDriverOperation.RangeCheck | RangeCheck | NIDCPOWER_ATTR_RANGE_CHECK |
| IIviDriverOperation.InvalidateAllAttributes() | InvalidateAllAttributes |  |
| IIviDriverOperation.ResetInterchangeCheck() | ResetInterchangeCheck | niDCPower_ResetInterchangeCheck |
|  | DCPowerDriverUtility Class |  |
| IIviDriverUtility.Disable() | Disable | niDCPower_Disable |
|  | ExportAttributeConfigurationBuffer | niDCPower_ExportAttributeConfigurationBuffer |
|  | ExportAttributeConfigurationFile | niDCPower_ExportAttributeConfigurationFile |
|  | ImportAttributeConfigurationBuffer | niDCPower_ImportAttributeConfigurationBuffer |
|  | ImportAttributeConfigurationFile | niDCPower_ImportAttributeConfigurationFile |
| IIviDriverUtility.Lock() | Lock |  |
| IIviDriverUtility.Reset() | Reset | niDCPower_reset |
|  | ResetDevice | niDCPower_ResetDevice |
| IIviDriverUtility.ResetWithDefaults() | ResetWithDefaults | niDCPower_ResetWithDefaults |
| IIviDriverUtility.SelfTest() | SelfTest | niDCPower_self_test |
|  | DCPowerExternalCalibration Class |  |
|  | CalibrationUserDefinedInfo | niDCPower_SetCalUserDefinedInfo |
|  | CalibrationUserDefinedInfoMaxSize | niDCPower_GetCalUserDefinedInfoMaxSize |
|  | GetExternalCalibrationLastDateAndTime | niDCPower_GetSelfCalLastDateAndTime |
|  | GetExternalCalibrationLastTemperature | niDCPower_GetExtCalLastTemp |
|  | GetExternalCalibrationRecommendedInterval | niDCPower_GetExtCalRecommendedInterval |
|  | DCPowerMeasureCompleteEvent Class |  |
|  | Delay | NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_DELAY |
|  | OutputTerminal | NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_OUTPUT_TERMINAL |
|  | WaitForEvent | niDCPower_WaitForEvent |
|  | DCPowerMeasureCompleteEventPulse Class |  |
|  | Polarity | NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY |
|  | Width | NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_WIDTH |
|  | DCPowerMeasurement Class |  |
|  | BeginFetch | niDCPower_FetchMultiple |
|  | BeginMeasure | niDCPower_MeasureMultiple |
|  | EndFetch | niDCPower_FetchMultiple |
|  | EndMeasure | niDCPower_MeasureMultiple |
|  | FetchBacklog | NIDCPOWER_ATTR_FETCH_BACKLOG |
|  | SynchronizeCallbacks |  |
|  | Fetch | niDCPower_FetchMultiple |
|  | Measure | niDCPower_MeasureMultiple |
|  | QueryInCompliance | niDCPower_FetchMultiple |
| IIviDCPwrOutput.QueryState | QueryState | niDCPower_QueryOutputState |
|  | DCPowerMeasurementConfiguration Class |  |
|  | IsRecordLengthFinite | NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH_IS_FINITE |
|  | MeasureWhen | NIDCPOWER_ATTR_MEASURE_WHEN |
|  | RecordDeltaTime | NIDCPOWER_ATTR_MEASURE_RECORD_DELTA_TIME |
|  | DCPowerMeasureTrigger Class |  |
|  | ExportedOutputTerminal | NIDCPOWER_ATTR_EXPORTED_MEASURE_TRIGGER_OUTPUT_TERMINAL |
|  | Type | NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE |
|  | ConfigureSoftwareEdgeTrigger | niDCPower_ConfigureSoftwareEdgeMeasureTrigger |
|  | SendSoftwareEdgeTrigger | niDCPower_SendSoftwareEdgeTrigger |
|  | DCPowerOutput Class |  |
|  | Name |  |
| IIviDCPwrOutput.ConfigureCurrentLimit |  | niDCPower_ConfigureCurrentLimit |
| IIviDCPwrOutput.ConfigureOvp |  | niDCPower_ConfigureOVP |
| IIviDCPwrOutput.ConfigureRange |  | niDCPower_ConfigureOutputRange |
| IIviDCPwrOutput.Measure |  | niDCPower_Measure |
| IIviDCPwrOutput.QueryCurrentLimitMax |  | niDCPower_QueryMaxCurrentLimit |
| IIviDCPwrOutput.QueryState |  | niDCPower_QueryOutputState |
| IIviDCPwrOutput.QueryVoltageLevelMax |  | niDCPower_QueryMaxVoltageLevel |
| IIviDCPwrOutput.ResetOutputProtection |  | niDCPower_ResetOutputProtection |
|  | DCPowerOutputCollection Class |  |
| IIviRepeatedCapabilityCollection.Count | Count |  |
|  | Item |  |
|  | DCPowerOutputMeasurement Class |  |
|  | ApertureTime | NIDCPOWER_ATTR_APERTURE_TIME |
|  | ApertureTimeUnits | NIDCPOWER_ATTR_APERTURE_TIME_UNITS |
|  | AutoZero | NIDCPOWER_ATTR_AUTO_ZERO |
|  | NoiseRejection | NIDCPOWER_ATTR_DC_NOISE_REJECTION |
|  | PowerLineFrequency | NIDCPOWER_ATTR_POWER_LINE_FREQUENCY |
|  | RecordLength | NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH |
|  | BufferSize | NIDCPOWER_ATTR_MEASURE_BUFFER_SIZE |
|  | ResetAverageBeforeMeasurement | NIDCPOWER_ATTR_RESET_AVERAGE_BEFORE_MEASUREMENT |
|  | SamplesToAverage | NIDCPOWER_ATTR_SAMPLES_TO_AVERAGE |
|  | Sense | NIDCPOWER_ATTR_SENSE |
|  | ConfigureApertureTime | niDCPower_ConfigureApertureTime |
|  | DCPowerOutputSource Class |  |
|  | ActualPowerAllocation | NIDCPOWER_ATTR_ACTUAL_POWER_ALLOCATION |
|  | OutputCapacitance | NIDCPOWER_ATTR_OUTPUT_CAPACITANCE |
| IIviDCPwrOutput.OvpEnabled | OvpEnabled | NIDCPOWER_ATTR_OVP_ENABLED |
|  | PowerAllocationMode | NIDCPOWER_ATTR_POWER_ALLOCATION_MODE |
|  | PulseBiasDelay | NIDCPOWER_ATTR_PULSE_BIAS_DELAY |
|  | PulseOnTime | NIDCPOWER_ATTR_PULSE_ON_TIME |
|  | PulseOffTime | NIDCPOWER_ATTR_PULSE_OFF_TIME |
|  | RequestedPowerAllocation | NIDCPOWER_ATTR_REQUESTED_POWER_ALLOCATION |
|  | SourceDelay | NIDCPOWER_ATTR_SOURCE_DELAY |
|  | TransientResponse | NIDCPOWER_ATTR_TRANSIENT_RESPONSE |
| IIviDCPwrOutput.QueryCurrentLimitMax | QueryCurrentLimitMax | niDCPower_QueryMaxCurrentLimit |
|  | QueryCurrentLimitMin | niDCPower_QueryMinCurrentLimit |
| IIviDCPwrOutput.QueryVoltageLevelMax | QueryVoltageLevelMax | niDCPower_QueryMaxVoltageLevel |
|  | SetSequence | niDCPower_SetSequence |
|  | DCPowerOutputSourceAdvancedSequencing Class |  |
|  | ActiveAdvancedSequence | NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE |
|  | ActiveAdvancedSequenceStep | NIDCPOWER_ATTR_ACTIVE_ADVANCED_SEQUENCE_STEP |
|  | CreateAdvancedSequence | niDCPower_CreateAdvancedSequence |
|  | CreateAdvancedSequenceStep | niDCPower_CreateAdvancedSequenceStep |
|  | DeleteAdvancedSequence | niDCPower_DeleteAdvancedSequence |
|  | DCPowerOutputSourceCurrent Class |  |
|  | CurrentLevel | NIDCPOWER_ATTR_CURRENT_LEVEL |
|  | CurrentLevelAutorange | NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE |
|  | CurrentLevelRange | NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE |
|  | VoltageLimit | NIDCPOWER_ATTR_VOLTAGE_LIMIT |
|  | VoltageLimitAutorange | NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE |
|  | VoltageLimitRange | NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE |
|  | DCPowerOutputSourceCustomTransientResponse Class |  |
|  | DCPowerOutputSourceCustomTransientResponseCurrent Class |  |
|  | CompensationFrequency | NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY |
|  | GainBandwidth | NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH |
|  | PoleZeroRatio | NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO |
|  | DCPowerOutputSourceCustomTransientResponseVoltage Class |  |
|  | CompensationFrequency | NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY |
|  | GainBandwidth | NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH |
|  | PoleZeroRatio | NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO |
|  | DCPowerOutputSourceOutput Class |  |
|  | Connected | NIDCPOWER_ATTR_OUTPUT_CONNECTED |
| IIviDCPwrOutput.Enabled | Enabled | NIDCPOWER_ATTR_OUTPUT_ENABLED |
|  | Function | NIDCPOWER_ATTR_OUTPUT_FUNCTION |
|  | Resistance | NIDCPOWER_ATTR_OUTPUT_RESISTANCE |
|  | DCPowerOutputSourcePulseCurrent Class |  |
|  | BiasCurrentLevel | NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL |
|  | BiasVoltageLimit | NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT |
|  | CurrentLevel | NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL |
|  | CurrentLevelRange | NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL_RANGE |
|  | VoltageLimit | NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT |
|  | VoltageLimitRange | NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE |
|  | DCPowerOutputSourcePulseVoltage Class |  |
|  | BiasCurrentLimit | NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT |
|  | BiasVoltageLevel | NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL |
|  | CurrentLimit | NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT |
|  | CurrentLimitRange | NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE |
|  | VoltageLevel | NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL |
|  | VoltageLevelRange | NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE |
|  | DCPowerOutputSourceVoltage Class |  |
| IIviDCPwrOutput.CurrentLimit | CurrentLimit | NIDCPOWER_ATTR_CURRENT_LIMIT |
|  | CurrentLimitAutorange | NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE |
|  | CurrentLimitRange | NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE |
| IIviDCPwrOutput.VoltageLevel | VoltageLevel | NIDCPOWER_ATTR_VOLTAGE_LEVEL |
|  | VoltageLevelAutorange | NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE |
|  | VoltageLevelRange | NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE |
|  | DCPowerPulseCompleteEvent Class |  |
|  | OutputTerminal | NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_OUTPUT_TERMINAL |
|  | WaitForEvent | niDCPower_WaitForEvent |
|  | DCPowerPulseCompleteEventPulse Class |  |
|  | Polarity | NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY |
|  | Width | NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_WIDTH |
|  | DCPowerPulseTrigger Class |  |
|  | Type | NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE |
|  | ConfigureSoftwareEdgeTrigger | niDCPower_ConfigureSoftwareEdgePulseTrigger |
|  | Disable | niDCPower_DisablePulseTrigger |
|  | SendSoftwareEdgeTrigger | niDCPower_SendSoftwareEdgeTrigger |
|  | DCPowerReadyForPulseTriggerEvent Class |  |
|  | Type | NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE |
|  | ConfigureSoftwareEdgeTrigger | niDCPower_ConfigureSoftwareEdgePulseTrigger |
|  | Disable | niDCPower_DisablePulseTrigger |
|  | SendSoftwareEdgeTrigger | niDCPower_SendSoftwareEdgeTrigger |
|  | OutputTerminal | NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_OUTPUT_TERMINAL |
|  | DCPowerReadyForPulseTriggerEventPulse Class |  |
|  | Polarity | NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY |
|  | Width | NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_WIDTH |
|  | DCPowerSelfCalibration Class |  |
|  | SelfCalibrationPersistence | NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE |
|  | GetSelfCalibrationLastDateAndTime | niDCPower_GetSelfCalLastDateAndTime |
|  | GetSelfCalibrationLastTemperature | niDCPower_GetSelfCalLastTemp |
|  | SelfCalibrate | niDCPower_CalSelfCalibrate |
|  | DCPowerSequenceAdvanceTrigger Class |  |
|  | ExportedOutputTerminal | NIDCPOWER_ATTR_EXPORTED_SEQUENCE_ADVANCE_TRIGGER_OUTPUT_TERMINAL |
|  | Type | NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE |
|  | ConfigureSoftwareEdgeTrigger | niDCPower_ConfigureSoftwareEdgeSequenceAdvanceTrigger |
|  | Disable | niDCPower_DisableSequenceAdvanceTrigger |
|  | SendSoftwareEdgeTrigger | niDCPower_SendSoftwareEdgeTrigger |
|  | DCPowerSequenceEngineDoneEvent Class |  |
|  | OutputTerminal | NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_OUTPUT_TERMINAL |
|  | WaitForEvent | niDCPower_WaitForEvent |
|  | DCPowerSequenceEngineDoneEventPulse Class |  |
|  | Polarity | NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY |
|  | Width | NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_WIDTH |
|  | DCPowerSequenceIterationCompleteEvent Class |  |
|  | OutputTerminal | NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_OUTPUT_TERMINAL |
|  | WaitForEvent | niDCPower_WaitForEvent |
|  | DCPowerSequenceIterationCompleteEventPulse Class |  |
|  | Polarity | NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY |
|  | Width | NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_WIDTH |
|  | DCPowerSource Class |  |
|  | Mode | NIDCPOWER_ATTR_SOURCE_MODE |
|  | OverrangingEnabled | NIDCPOWER_ATTR_OVERRANGING_ENABLED |
|  | SequenceLoopCount | NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT |
|  | IsSequenceLoopCountFinite | NIDCPOWER_ATTR_SEQUENCE_LOOP_COUNT_IS_FINITE |
|  | DCPowerSourceCompleteEvent Class |  |
|  | OutputTerminal | NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_OUTPUT_TERMINAL |
|  | WaitForEvent | niDCPower_WaitForEvent |
|  | DCPowerSourceCompleteEventPulse Class |  |
|  | Polarity | NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY |
|  | Width | NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_WIDTH |
|  | DCPowerSourceTrigger Class |  |
|  | ExportedOutputTerminal | NIDCPOWER_ATTR_EXPORTED_SOURCE_TRIGGER_OUTPUT_TERMINAL |
|  | Type | NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE |
|  | ConfigureSoftwareEdgeTrigger | niDCPower_ConfigureSoftwareEdgeSourceTrigger |
|  | Disable | niDCPower_DisableSourceTrigger |
|  | DCPowerStartTrigger Class |  |
|  | ExportedOutputTerminal | NIDCPOWER_ATTR_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL |
|  | Type | NIDCPOWER_ATTR_START_TRIGGER_TYPE |
|  | ConfigureSoftwareEdgeTrigger | niDCPower_ConfigureSoftwareEdgeStartTrigger |
|  | Disable | niDCPower_DisableStartTrigger |
|  | SendSoftwareEdgeTrigger | niDCPower_SendSoftwareEdgeTrigger |
|  | NIDCPower Class |  |
|  | IsDisposed |  |
| IIviDriver.Close() | Close | niDCPower_close |
|  | DangerousGetInstrumentHandle |  |
|  | GetService |  |

Parent topic:

NI-DCPower .NET Class Library Help

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerbasic.html language=enus -->
## TOPIC 00002: Basic Usage

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerbasic.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerbasic.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `task`
- source_description: You can use the NI-DCPower .NET class library to initialize, configure, initiate, run, and close a session on your NI-DCPower device. The NI-DCPower .NET API is an Interchangeable Virtual Instrument (IVI)-compliant instrument driver that features a set of methods and properties that exercise the fun

Basic Usage

You can use the NI-DCPower .NET class library to initialize, configure, initiate, run, and close a session on your NI-DCPower device. The NI-DCPower .NET API is an Interchangeable Virtual Instrument (IVI)-compliant instrument driver that features a set of methods and properties that exercise the functionality of the NI-DCPower hardware.

1. Initialization—Use a constructor to create a new instance of the NIDCPowerclass. You must create an instance of this class before you can call into the underlying NI-DCPower driver. 
 VB.NET

Dim dcPowerSession As New NIDCPower("resourceName", "0", False) ' Initialize.
 Visual C#

NIDCPower dcPowerSession = new NIDCPower("resourceName", "0", false); // Initialize.
2. Configuration—Use the NIDCPower object to access various subobjects and to configure the NI-DCPower driver directly or indirectly. You can use the Outputs collection subobject to configure channel-specific properties. 
 VB.NET

Dim dcPowerSession As New NIDCPower("resourceName", "0", False)
dcPowerSession.Source.Mode = DCPowerSourceMode.SinglePoint
dcPowerSession.Outputs("0").Source.Output.Function = DCPowerSourceOutputFunction.DCCurrent
dcPowerSession.Outputs("0").Measurement.Sense = DCPowerMeasurementSense.Local
dcPowerSession.Outputs("0").Source.Current.CurrentLevel = 0.02
dcPowerSession.Measurement.Configuration.MeasureWhen = DCPowerMeasurementWhen.OnDemand
 Visual C#

NIDCPower dcPowerSession = new NIDCPower("resourceName", "0", false);
dcPowerSession.Source.Mode = DCPowerSourceMode.SinglePoint;
dcPowerSession.Outputs["0"].Source.Output.Function = DCPowerSourceOutputFunction.DCCurrent;
dcPowerSession.Outputs["0"].Measurement.Sense = DCPowerMeasurementSense.Local;
dcPowerSession.Outputs["0"].Source.Current.CurrentLevel = 0.02;
dcPowerSession.Measurement.Configuration.MeasureWhen = DCPowerMeasurementWhen.OnDemand;
3. Initiate—The NI-DCPower instrument starts sourcing or measuring, causing the NI-DCPower session to enter the running state. 
 VB.NET

dcPowerSession.Control.Initiate()
 Visual C#

dcPowerSession.Control.Initiate();
4. Running State—In the running state, you can take measurements, fetch buffered measurements, query the output state, or query the instrument state. 
 VB.NET

Dim result As DCPowerMeasureResult = dcPowerSession.Measurement.Measure("0") ' Measure the voltage and current. 
Dim inCompliance As Boolean = dcPowerSession.Measurement.QueryInCompliance("0") ' Determine if the output is in compliance.
 Visual C#

DCPowerMeasureResult result = dcPowerSession.Measurement.Measure("0"); // Measure the voltage and current. 
bool inCompliance = dcPowerSession.Measurement.QueryInCompliance("0"); // Determine if the output is in compliance.
5. Close—Close the session to the instrument and free unmanaged resources that are held by the session. You can close the session with Close or Dispose. 
 VB.NET

 dcPowerSession.Close()
 or
 dcPowerSession.Dispose()
 or 
 Using dcPowerSession As New NIDCPower("resourceName", "0", false)
' User code goes here. 
 End Using
 Visual C#

dcPowerSession.Close();
or
dcPowerSession.Dispose();
or
using (NIDCPower dcPowerSession = new NIDCPower("resourceName", "0", false))
{
 // User code goes here.
}

Refer to the 
 *Programming States* topic in the 
 *NI DC Power Supplies and SMUs Help* for information about the specific NI-DCPower software states.

Parent topic:

NI-DCPower .NET Class Library Help

Related information:

- NIDCPower Class
- Outputs Property
- Initiate Method
- Dispose Method

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerenummap.html language=enus -->
## TOPIC 00003: Mapping the NI-DCPower .NET API Enums and Enum Values to the NI-DCPower C API Attributes and Values

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerenummap.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerenummap.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `reference`
- source_description: The following table maps the NI-DCPower .NET API enums and enum values to the corresponding NI-DCPower C API attributes and values. All .NET members are in the NationalInstruments.ModularInstruments.NIDCPower namespace. .NET API Enums and Enum Values C API Attributes and Values DCPowerAdvancedSequen

Mapping the NI-DCPower .NET API Enums and Enum Values to the NI-DCPower C API Attributes and Values

The following table maps the NI-DCPower .NET API enums and enum values to the corresponding NI-DCPower C API attributes and values. All .NET members are in the NationalInstruments.ModularInstruments.NIDCPower namespace.

| .NET API Enums and Enum Values | C API Attributes and Values |
| --- | --- |
| DCPowerAdvancedSequenceProperty | niDCPower_CreateAdvancedSequence |
| ApertureTime | NIDCPOWER_ATTR_APERTURE_TIME |
| Compliance Limit Symmetry | NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY |
| CurrentCompensationFrequency | NIDCPOWER_ATTR_CURRENT_COMPENSATION_FREQUENCY |
| CurrentGainBandwidth | NIDCPOWER_ATTR_CURRENT_GAIN_BANDWIDTH |
| CurrentLevel | NIDCPOWER_ATTR_CURRENT_LEVEL |
| CurrentLevelRange | NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE |
| CurrentLimit | NIDCPOWER_ATTR_CURRENT_LIMIT |
| CurrentLimitHigh | NIDCPOWER_ATTR_CURRENT_LIMIT_HIGH |
| CurrentLimitLow | NIDCPOWER_ATTR_CURRENT_LIMIT_LOW |
| CurrentLimitRange | NIDCPOWER_ATTR_CURRENT_LIMIT_RANGE |
| CurrentPoleZeroRatio | NIDCPOWER_ATTR_CURRENT_POLE_ZERO_RATIO |
| DCNoiseRejection | NIDCPOWER_ATTR_DC_NOISE_REJECTION |
| MeasureRecordLength | NIDCPOWER_ATTR_MEASURE_RECORD_LENGTH |
| OutputEnabled | NIDCPOWER_ATTR_OUTPUT_ENABLED |
| OutputFunction | NIDCPOWER_ATTR_OUTPUT_FUNCTION |
| OutputResistance | NIDCPOWER_ATTR_OUTPUT_RESISTANCE |
| PulseBiasCurrentLevel | NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LEVEL |
| PulseBiasCurrentLimit | NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT |
| PulseBiasCurrentLimitHigh | NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_HIGH |
| PulseBiasCurrentLimitLow | NIDCPOWER_ATTR_PULSE_BIAS_CURRENT_LIMIT_LOW |
| PulseBiasDelay | NIDCPOWER_ATTR_PULSE_BIAS_DELAY |
| PulseBiasVoltageLevel | NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LEVEL |
| PulseBiasVoltageLimit | NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT |
| PulseBiasVoltageLimitHigh | NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_HIGH |
| PulseBiasVoltageLimitLow | NIDCPOWER_ATTR_PULSE_BIAS_VOLTAGE_LIMIT_LOW |
| PulseCurrentLevel | NIDCPOWER_ATTR_PULSE_CURRENT_LEVEL |
| PulseCurrentLevelRange | NIDCPOWER_ATTR_CURRENT_LEVEL_RANGE |
| PulseCurrentLimit | NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT |
| PulseCurrentLimitHigh | NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_HIGH |
| PulseCurrentLimitLow | NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_LOW |
| PulseCurrentLimitRange | NIDCPOWER_ATTR_PULSE_CURRENT_LIMIT_RANGE |
| PulseOffTime | NIDCPOWER_ATTR_PULSE_OFF_TIME |
| PulseOnTime | NIDCPOWER_ATTR_PULSE_ON_TIME |
| PulseVoltageLevel | NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL |
| PulseVoltageLevelRange | NIDCPOWER_ATTR_PULSE_VOLTAGE_LEVEL_RANGE |
| PulseVoltageLimit | NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT |
| PulseVoltageLimitHigh | NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_HIGH |
| PulseVoltageLimitLow | NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_LOW |
| PulseVoltageLimitRange | NIDCPOWER_ATTR_PULSE_VOLTAGE_LIMIT_RANGE |
| Sense | NIDCPOWER_ATTR_SENSE |
| SourceDelay | NIDCPOWER_ATTR_SOURCE_DELAY |
| TransientResponse | NIDCPOWER_ATTR_TRANSIENT_RESPONSE |
| VoltageCompensationFrequency | NIDCPOWER_ATTR_VOLTAGE_COMPENSATION_FREQUENCY |
| VoltageGainBandwidth | NIDCPOWER_ATTR_VOLTAGE_GAIN_BANDWIDTH |
| VoltageLevel | NIDCPOWER_ATTR_VOLTAGE_LEVEL |
| VoltageLevelRange | NIDCPOWER_ATTR_VOLTAGE_LEVEL_RANGE |
| VoltageLimit | NIDCPOWER_ATTR_VOLTAGE_LIMIT |
| VoltageLimitHigh | NIDCPOWER_ATTR_VOLTAGE_LIMIT_HIGH |
| VoltageLimitLow | NIDCPOWER_ATTR_VOLTAGE_LIMIT_LOW |
| VoltageLimitRange | NIDCPOWER_ATTR_VOLTAGE_LIMIT_RANGE |
| VoltagePoleZeroRatio | NIDCPOWER_ATTR_VOLTAGE_POLE_ZERO_RATIO |
| DCPowerComplianceLimitSymmetry | NIDCPOWER_ATTR_COMPLIANCE_LIMIT_SYMMETRY |
| Symmetric | NIDCPOWER_VAL_SYMMETRIC |
| Asymmetric | NIDCPOWER_VAL_ASYMMETRIC |
| DCPowerMeasureApertureTimeUnits | NIDCPOWER_ATTR_APERTURE_TIME_UNITS |
| PowerLineCycles | NIDCPOWER_VAL_POWER_LINE_CYCLES |
| Seconds | NIDCPOWER_VAL_SECONDS |
| DCPowerMeasurementAutoZero | NIDCPOWER_ATTR_AUTO_ZERO |
| Off | NIDCPOWER_VAL_OFF |
| On | NIDCPOWER_VAL_ON |
| Once | NIDCPOWER_VAL_ONCE |
| DCPowerMeasurementNoiseRejection | NIDCPOWER_ATTR_DC_NOISE_REJECTION |
| Normal | NIDCPOWER_VAL_DC_NOISE_REJECTION_NORMAL |
| SecondOrder | NIDCPOWER_VAL_DC_NOISE_REJECTION_SECOND_ORDER |
| DCPowerMeasurementOutputState | niDCPower_QueryOutputState |
| ConstantCurrent | NIDCPOWER_VAL_OUTPUT_CONSTANT_CURRENT |
| ConstantVoltage | NIDCPOWER_VAL_OUTPUT_CONSTANT_VOLTAGE |
| DCPowerMeasurementPowerLineFrequency | NIDCPOWER_ATTR_POWER_LINE_FREQUENCY |
| FiftyHertz | NIDCPOWER_VAL_50_HERTZ |
| SixtyHertz | NIDCPOWER_VAL_60_HERTZ |
| DCPowerMeasurementSense | NIDCPOWER_ATTR_SENSE |
| Local | NIDCPOWER_VAL_LOCAL |
| Remote | NIDCPOWER_VAL_REMOTE |
| DCPowerMeasurementWhen | NIDCPOWER_ATTR_MEASURE_WHEN |
| AutomaticallyAfterSourceComplete | NIDCPOWER_VAL_AUTOMATICALLY_AFTER_SOURCE_COMPLETE |
| OnDemand | NIDCPOWER_VAL_ON_DEMAND |
| OnMeasureTrigger | NIDCPOWER_VAL_ON_MEASURE_TRIGGER |
| DCPowerMeasureTriggerType | NIDCPOWER_ATTR_MEASURE_TRIGGER_TYPE |
| DigitalEdge | NIDCPOWER_VAL_DIGITAL_EDGE |
| SoftwareEdge | NIDCPOWER_VAL_SOFTWARE_EDGE |
| DCPowerPowerAllocationMode | NIDCPOWER_ATTR_POWER_ALLOCATION_MODE |
| Automatic | NIDCPOWER_VAL_POWER_ALLOCATION_MODE_AUTOMATIC |
| Disabled | NIDCPOWER_VAL_POWER_ALLOCATION_MODE_DISABLED |
| Manual | NIDCPOWER_VAL_POWER_ALLOCATION_MODE_MANUAL |
| DCPowerPowerSource | NIDCPOWER_ATTR_POWER_SOURCE |
| Automatic | NIDCPOWER_VAL_AUTOMATIC |
| Auxiliary | NIDCPOWER_VAL_AUXILIARY |
| Internal | NIDCPOWER_VAL_INTERNAL |
| DCPowerPowerSourceInUse | NIDCPOWER_ATTR_POWER_SOURCE_IN_USE |
| Auxiliary | NIDCPOWER_VAL_AUXILIARY |
| Internal | NIDCPOWER_VAL_INTERNAL |
| DCPowerPulsePolarity | NIDCPOWER_ATTR_MEASURE_COMPLETE_EVENT_PULSE_POLARITY NIDCPOWER_ATTR_PULSE_COMPLETE_EVENT_PULSE_POLARITY NIDCPOWER_ATTR_READY_FOR_PULSE_TRIGGER_EVENT_PULSE_POLARITY NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY NIDCPOWER_ATTR_SEQUENCE_ENGINE_DONE_EVENT_PULSE_POLARITY NIDCPOWER_ATTR_SEQUENCE_ITERATION_COMPLETE_EVENT_PULSE_POLARITY NIDCPOWER_ATTR_SOURCE_COMPLETE_EVENT_PULSE_POLARITY |
| ActiveHigh | NIDCPOWER_VAL_ACTIVE_HIGH |
| ActiveLow | NIDCPOWER_VAL_ACTIVE_LOW |
| DCPowerPulseTriggerType | NIDCPOWER_ATTR_PULSE_TRIGGER_TYPE |
| None | NIDCPOWER_VAL_NONE |
| DigitalEdge | NIDCPOWER_VAL_DIGITAL_EDGE |
| SoftwareEdge | NIDCPOWER_VAL_SOFTWARE_EDGE |
| DCPowerShutdownTriggerType | NIDCPOWER_ATTR_SHUTDOWN_TRIGGER_TYPE |
| None | NIDCPOWER_VAL_NONE |
| DigitalEdge | NIDCPOWER_VAL_DIGITAL_EDGE |
| SoftwareEdge | NIDCPOWER_VAL_SOFTWARE_EDGE |
| DCPowerSelfCalibrationPersistence | NIDCPOWER_ATTR_SELF_CALIBRATION_PERSISTENCE |
| KeepInMemory | NIDCPOWER_VAL_KEEP_IN_MEMORY |
| WriteToEeprom | NIDCPOWER_VAL_WRITE_TO_EEPROM |
| DCPowerSequenceAdvanceTriggerType | NIDCPOWER_ATTR_SEQUENCE_ADVANCE_TRIGGER_TYPE |
| DigitalEdge | NIDCPOWER_VAL_DIGITAL_EDGE |
| None | NIDCPOWER_VAL_NONE |
| SoftwareEdge | NIDCPOWER_VAL_SOFTWARE_EDGE |
| DCPowerSourceCurrentLevelAutorange | NIDCPOWER_ATTR_CURRENT_LEVEL_AUTORANGE |
| Off | NIDCPOWER_VAL_OFF |
| On | NIDCPOWER_VAL_ON |
| DCPowerSourceCurrentLimitAutorange | NIDCPOWER_ATTR_CURRENT_LIMIT_AUTORANGE |
| Off | NIDCPOWER_VAL_OFF |
| On | NIDCPOWER_VAL_ON |
| DCPowerSourceMode | NIDCPOWER_ATTR_SOURCE_MODE |
| Sequence | NIDCPOWER_VAL_SEQUENCE |
| SinglePoint | NIDCPOWER_VAL_SINGLE_POINT |
| DCPowerSourceOutputCapacitance | NIDCPOWER_ATTR_OUTPUT_CAPACITANCE |
| High | NIDCPOWER_VAL_HIGH |
| Low | NIDCPOWER_VAL_LOW |
| DCPowerSourceOutputFunction | NIDCPOWER_ATTR_OUTPUT_FUNCTION |
| DCCurrent | NIDCPOWER_VAL_DC_CURRENT |
| DCVoltage | NIDCPOWER_VAL_DC_VOLTAGE |
| PulseCurrent | NIDCPOWER_VAL_PULSE_CURRENT |
| PulseVoltage | NIDCPOWER_VAL_PULSE_VOLTAGE |
| DCPowerSourceTransientResponse | NIDCPOWER_ATTR_TRANSIENT_RESPONSE |
| Custom | NIDCPOWER_VAL_CUSTOM |
| Fast | NIDCPOWER_VAL_FAST |
| Normal | NIDCPOWER_VAL_NORMAL |
| Slow | NIDCPOWER_VAL_SLOW |
| DCPowerSourceTriggerType | NIDCPOWER_ATTR_SOURCE_TRIGGER_TYPE |
| DigitalEdge | NIDCPOWER_VAL_DIGITAL_EDGE |
| None | NIDCPOWER_VAL_NONE |
| SoftwareEdge | NIDCPOWER_VAL_SOFTWARE_EDGE |
| DCPowerSourceVoltageLevelAutorange | NIDCPOWER_ATTR_VOLTAGE_LEVEL_AUTORANGE |
| Off | NIDCPOWER_VAL_OFF |
| On | NIDCPOWER_VAL_ON |
| DCPowerSourceVoltageLimitAutorange | NIDCPOWER_ATTR_VOLTAGE_LIMIT_AUTORANGE |
| Off | NIDCPOWER_VAL_OFF |
| On | NIDCPOWER_VAL_ON |
| DCPowerStartTriggerType | NIDCPOWER_ATTR_START_TRIGGER_TYPE |
| DigitalEdge | NIDCPOWER_VAL_DIGITAL_EDGE |
| None | NIDCPOWER_VAL_NONE |
| SoftwareEdge | NIDCPOWER_VAL_SOFTWARE_EDGE |
| DCPowerTriggerEdge | NIDCPOWER_ATTR_DIGITAL_EDGE_MEASURE_TRIGGER_EDGE |
| Falling | NIDCPOWER_VAL_FALLING |
| Rising | NIDCPOWER_VAL_RISING |

Parent topic:

NI-DCPower .NET Class Library Help

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowererrors.html language=enus -->
## TOPIC 00004: How Do I Manage Errors and Warnings in the NI-DCPower .NET Class Library?

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowererrors.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowererrors.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The underlying NI-DCPower driver reports any errors or warnings as errors codes. Negative return values indicate errors whereas positive values indicate warnings. In case of warnings we raise a warning event, to which you can subscribe. Managing Errors in the NI-DCPower .NET Class Library The NI-DCP

How Do I Manage Errors and Warnings in the NI-DCPower .NET Class Library?

The underlying NI-DCPower driver reports any errors or warnings as errors codes. Negative return values indicate errors whereas positive values indicate warnings. In case of warnings we raise a warning event, to which you can subscribe.

#### Managing Errors in the NI-DCPower .NET Class Library

The NI-DCPower .NET API converts the negative error codes into exceptions and throws them. All exceptions that the API throws are either .NET defined or IVI defined; none of them are custom exceptions. The exception message for driver errors has the driver error code appended at the end.

#### Managing Warnings in the NI-DCPower .NET Class Library

Warnings are communicated to the user as events. In order to receive warnings your must subscribe to theWarning event as follows:

- Driver Warning 
 VB.NET

AddHandler dcPowerSession.DriverOperation.Warning, AddressOf DriverOperation_Warning
 Private Sub DriverOperation_Warning(ByVal sender As Object, ByVal e As Ivi.Driver.WarningEventArgs)
 'Do whatever that needs to be done for Warning. 
 End Sub 
 C#

dcPowerSessionSession.DriverOperation.Warning += new EventHandler<Ivi.Driver.WarningEventArgs>(DriverOperation_Warning);
 void DriverOperation_Warning(object sender, Ivi.Driver.WarningEventArgs e)
 {
 //Do whatever that needs to be done for Warning.
 }
- InterChangeCheckWarning 
 An InterchangeCheckWarning is communicated to the user as an event. In order to receive warnings your must subscribe to the InterchangeCheckWarning event as follows: 
 VB.NET

AddHandler dcPowerSession.DriverOperation.InterchangeCheckWarning, AddressOf DriverOperation_InterchangeCheckWarning
 Private Sub DriverOperation_InterchangeCheckWarning(ByVal sender As Object, ByVal e As Ivi.Driver.InterchangeCheckWarningEventArgs)
 'Do whatever that needs to be done for InterchangeCheckWarning. 
 End Sub 
 C#

dcPowerSession.DriverOperation.InterchangeCheckWarning += new EventHandler<Ivi.Driver.InterchangeCheckWarningEventArgs>(DriverOperation_InterchangeCheckWarning);
 void DriverOperation_InterchangeCheckWarning(object sender, Ivi.Driver.InterchangeCheckWarningEventArgs e)
 {
 //Do whatever that needs to be done for InterchangeCheckWarning.
 }
- Coercion Warning 
 Coercion warnings are communicated to the user as events. In order to receive warnings your must subscribe to the Coercion event as follows: 
 VB.NET

AddHandler dcPowerSession.DriverOperation.CoercionWarning, AddressOf DriverOperation_CoercionWarning
 Private Sub DriverOperation_CoercionWarning(ByVal sender As Object, ByVal e As Ivi.Driver.CoercionWarningEventArgs)
 'Do whatever that needs to be done for CoercionWarning. 
 End Sub 
 C#

dcPowerSession.DriverOperation.CoercionWarning += new EventHandler<Ivi.Driver.CoercionWarningEventArgs>(DriverOperation_CoercionWarning);
 void DriverOperation_CoercionWarning(object sender, Ivi.Driver.CoercionWarningEventArgs e)
 {
 //Do whatever that needs to be done for CoercionWarning.
 } 
 org.dita.html5/xsl/topic.xsl 455 Note National Instruments recommends subscribing to the warning event immediately after creating the NIDCPower object, in order to avoid missing any warnings that might occur.

#### Managing EventArgs

Each warning EventArgs class contains the read-only property Text to get the description of that event. For example:

- Ivi.Driver.CoercionEventArgs 
 VB.NET

Private Sub DriverOperation_CoercionWarning(ByVal sender As Object, ByVal e As Ivi.Driver.CoercionWarningEventArgs)
 Dim description As string = e.Text
 End Sub 
 C#

void DriverOperation_CoercionWarning(object sender, Ivi.Driver.CoercionWarningEventArgs e)
 {
 string description = e.Text;
 }
- Ivi.Driver.InterchangeCheckWarningEventArgs 
 VB.NET

Private Sub DriverOperation_InterchangeCheckWarning(ByVal sender As Object, ByVal e As Ivi.Driver.InterchangeCheckWarningEventArgs)
 Dim description As string = e.Text
 End Sub 
 C#

void DriverOperation_InterchangeCheckWarning(object sender, Ivi.Driver.InterchangeCheckWarningEventArgs e)
 {
 string description = e.Text;
 }

Parent topic:

NI-DCPower .NET Class Library Help

Related information:

- InterchangeCheckWarning Event
- Coercion Event

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerfetch.html language=enus -->
## TOPIC 00005: Using Fetch and Measure Methods

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerfetch.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerfetch.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: This topic describes the different types of Fetch and Measure methods and when to use them. The Fetch and Measure methods are present in the DCPowerMeasurement class. A session must be opened, configured correctly, and initiated before you can use Fetch and Measure methods. The Fetch and Measure met

Using Fetch and Measure Methods

This topic describes the different types of Fetch and Measure methods and when to use them.

The Fetch and Measure methods are present in the DCPowerMeasurement class. A session must be opened, configured correctly, and initiated before you can use Fetch and Measure methods.

The Fetch and Measure methods can be categorized into normal and async methods.

#### Using Async Methods

For every non-asynchronous method present, there is a corresponding method which does the same operation asynchronously. We follow the 
 [Asynchronous Programming Model](https://docs.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/asynchronous-programming-model-apm). The asynchronous methods perform the fetch or measure operation in a separate worker thread. This permits the client program to perform other operations, including driver operations, without waiting for the I/O operation to complete. In the APM, an asynchronous operation is implemented as two methods: Begin< Operation> and End< Operation>, where < Operation > is the name of an I/O method that operates synchronously. After calling the Begin < Operation> method, a client program can continue executing instructions on the calling thread while the specific driver performs an < Operation> on a different thread. For each call to the Begin < Operation> method, the client program calls the End < Operation> method to get the results of the operation. The following code shows how to fetch measurements asynchronously.

```text
VB.NET

  Private dcPowerSession As NIDCPower
  Private Sub Start()
    dcPowerSession = New NIDCPower("ResourceName", "0", False)
    Dim result As DCPowerFetchResult = New DCPowerFetchResult
    Dim callBack As New AsyncCallback(AddressOf ProcessFetch)
    dcPowerSession.Source.Mode = DCPowerSourceMode.SinglePoint
    dcPowerSession.Outputs("0").Source.Output.Function = DCPowerSourceOutputFunction.DCCurrent
    dcPowerSession.Measurement.Configuration.MeasureWhen = DCPowerMeasurementWhen.AutomaticallyAfterSourceComplete
    dcPowerSession.Outputs("0").Measurement.Sense = DCPowerMeasurementSense.Local
    dcPowerSession.Outputs("0").Source.Current.CurrentLevel = 0.02
    dcPowerSession.Outputs("0").Source.Current.VoltageLimit = 2.0
    dcPowerSession.Outputs("0").Source.Current.CurrentLevelRange = 0.02
    dcPowerSession.Outputs("0").Source.Current.VoltageLimitRange = 6.0
    dcPowerSession.Outputs("0").Source.SourceDelay = New PrecisionTimeSpan(0.05)
    dcPowerSession.Control.Initiate()
    dcPowerSession.Events.SourceCompleteEvent.WaitForEvent(New PrecisionTimeSpan(5.0))
    Dim asyncResult As IAsyncResult = dcPowerSession.Measurement.BeginFetch("0", New PrecisionTimeSpan(1.0), 1, result, callBack, DBNull.Value)
    '…  
    'Do any additional work that can be done here   
    'while the Fetch operation executes on a different thread.  
    '…  
End Sub 

Private Sub ProcessFetch(ByVal asyncResult As IAsyncResult)

    Dim result As DCPowerFetchResult = New DCPowerFetchResult
    Try 
        ' EndFetch blocks until the async work is complete. 
        result = dcPowerSession.Measurement.EndFetch(asyncResult)
        ' Handle exception from async Fetch operation.  
    Catch ex As Exception
        ' ...  
    Finally 

        ' ...
        dcPowerSession.Close()
    End Try 
End Sub
```

```text
C#

NIDCPower dcPowerSession = new NIDCPower("ResourceName", "0", false);
DCPowerFetchResult result= new DCPowerFetchResult();
dcPowerSession.Source.Mode = DCPowerSourceMode.SinglePoint;
dcPowerSession.Outputs["0"].Source.Output.Function = DCPowerSourceOutputFunction.DCCurrent;
dcPowerSession.Outputs["0"].Measurement.Sense = DCPowerMeasurementSense.Local;
dcPowerSession.Outputs["0"].Source.Current.CurrentLevel = 0.02;
dcPowerSession.Outputs["0"].Source.Current.VoltageLimit = 2.0;
dcPowerSession.Outputs["0"].Source.Current.CurrentLevelRange = 0.02;
dcPowerSession.Outputs["0"].Source.Current.VoltageLimitRange = 6.0;
dcPowerSession.Outputs["0"].Source.SourceDelay = new PrecisionTimeSpan(0.05);
dcPowerSession.Measurement.Configuration.MeasureWhen = DCPowerMeasurementWhen.AutomaticallyAfterSourceComplete;
dcPowerSession.Control.Initiate();
IAsyncResult asyncResult = dcPowerSession.Measurement.BeginFetch("0", new PrecisionTimeSpan(1.0), 1, result, null, null);
// …  
// Do any additional work that can be done here   
// while the Fetch operation executes on a different thread.  
// …  
try
{
    // EndFetch blocks until the async work is complete.
    result = dcPowerSession.Measurement.EndFetch(asyncResult);
}
catch (Exception ex)
{
    // Handle exception from async Fetch operation.
}

dcPowerSession.Close();
```

Parent topic:

NI-DCPower .NET Class Library Help

Related information:

- NIDCPower Class

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerivi.html language=enus -->
## TOPIC 00006: IVI Interchangeability for NI-DCPower

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerivi.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerivi.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: The .NET API for NI-DCPower is IVI.NET class-compliant. You can use the NI-DCPower .NET API to run IVI.NET-compliant applications using DCPower hardware when you have the NI-DCPower driver and the .NET API for NI-DCPower installed. For more information, refer to the NI DC Power Supplies and SMUs Hel

IVI Interchangeability for NI-DCPower

The .NET API for NI-DCPower is IVI.NET class-compliant. You can use the NI-DCPower .NET API to run IVI.NET-compliant applications using DCPower hardware when you have the NI-DCPower driver and the .NET API for NI-DCPower installed. For more information, refer to the 
 *NI DC Power Supplies and SMUs Help*.

Note

#### Using the NI-DCPower .NET Library in IVI.NET Applications

The .NET API for NI-DCPower has two parts: the IVI .NET class-compliant API, and the specific driver API. The following code snippet demonstrates how you can use an NI-DCPower .NET specific driver API from a session obtained from an IVI .NET class-compliant API.

```text
VB.NET

' Create an IVI DCPower session. 
Dim iviDCPowerSession As IIviDCPwr = Ivi.DCPwr.IviDCPwr.Create("logicalName", True, True)
' ... 
' Work with iviDCPowerSession object (IVI.NET class compliant API). 
' ... 
' Get an NI-DCPower session from the IVI DCPower session and access specific driver API. 
Dim dcPowerSession As NIDCPower = TryCast(iviDCPowerSession.GetService(GetType(NIDCPower)), NIDCPower)
If dcPowerSession IsNot Nothing Then 
    ' ... 
    ' Work with dcPowerSession object (specific driver API). 
    ' ... 
End If
iviDCPowerSession.Close()
```

```text
C#

// Create an IVI DCPower session.
IIviDCPwr iviDCPowerSession = Ivi.DCPwr.IviDCPwr.Create("logicalName", true, true);
// ... 
// Work with iviDCPowerSession object (IVI.NET class compliant API). 
// ... 
// Get an NI-DCPower session from the IVI DCPower session and access specific driver API.
NIDCPower dcPowerSession = iviDCPowerSession.GetService(typeof(NIDCPower)) as NIDCPower;
if (dcPowerSession != null)
{
    // ... 
    // Work with dcPowerSession object (specific driver API). 
    // ...
}
iviDCPowerSession.Close();
```

#### Using IVI Functionality in an NI-DCPower .NET Application

The following code snippet demonstrates how you can switch from an NI-DCPower .NET specific driver session to an IVI.NET DCPower session in the application.

Note

```text
VB.NET
Dim dcPowerSession As New NIDCPower("resourceName", "0", True)
' ... 
' Work with dcPowerSession object (specific driver API).. 
' ... 
' Use the NIDCPower to obtain an IVI DCPower session. 
Dim serviceProvider As IServiceProvider = TryCast(dcPowerSession, IServiceProvider)
Dim iviDCPowerSession As IIviDCPwr = TryCast(serviceProvider.GetService(GetType(IIviDCPwr)), IIviDCPwr)
If iviDCPowerSession IsNot Nothing Then 
    ' ... 
    ' Work with iviDCPowerSession object (IVI.NET class compliant API). 
    ' ... 
End If
dcPowerSession.Close()
```

```text
C#

NIDCPower dcPowerSession = new NIDCPower("resourceName", "0", true);
// ... 
// Work with dcPowerSession object (specific driver API). 
// ... 
// Use the NIDCPower to obtain an IVI DCPower session.
IServiceProvider serviceProvider = dcPowerSession as IServiceProvider;
IIviDCPwr iviDCPowerSession = serviceProvider.GetService(typeof(IIviDCPwr)) as IIviDCPwr;
if (iviDCPowerSession != null)
{
    // ... 
    // Work with iviDCPowerSession object (IVI.NET class compliant API). 
    // ...
}
dcPowerSession.Close();
```

Parent topic:

NI-DCPower .NET Class Library Help

Related information:

- NIDCPower Class
- IviDCPwr Reference

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerusing.html language=enus -->
## TOPIC 00007: NI-DCPower .NET Class Library Help

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerusing.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerusing.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: November 2020 You can use the NI-DCPower .NET API to configure and control NI power supplies and source-measure units (SMUs) and the NI-DCPower instrument driver. For additional information, refer to the NI-DCPower instrument driver documentation. Select StartAll ProgramsNational InstrumentsNI-DCPow

NI-DCPower .NET Class Library Help

You can use the
 NI-DCPower .NET API to configure and control NI power supplies and source-measure
 units (SMUs) and the NI-DCPower instrument driver. For additional information, refer
 to the NI-DCPower instrument driver documentation. Select Start»All Programs»National Instruments»NI-DCPower»NI-DCPower Documentation to access the NI-DCPower instrument driver readme and documentation.

For additional information on developing applications using NI drivers and the .NET
 Framework, refer to [ni.com/mstudio](http://www.ni.com/mstudio/) or visit [ni.com/info](http://www.ni.com/info/)
 and enter the Info Code NIdotNET.

You can find example applications by selecting National Instruments»NI-DCPower»NI-DCPower Examples in the Start menu.

© 2020 National Instruments Corporation. All rights reserved.

Related information:

- NIDCPower Namespace

<!--NI_TOPIC bundle=ni-dcpower-net-api-overview path=netdcpowerusingcustom.html language=enus -->
## TOPIC 00008: Using Predefined or Custom Values for Source and Output Terminal Properties

- bundle_id: `ni-dcpower-net-api-overview`
- source_path: `netdcpowerusingcustom.html`
- source_url: https://docs-be.ni.com/bundle/ni-dcpower-net-api-overview/raw/resource/enus/netdcpowerusingcustom.html
- document_id: `ni-dcpower-net-api-overview`
- page_type: `leaf`
- content_type: `concept`
- source_description: How Do I Pass a Predefined Value to an NI-DCPower Property? There are certain properties, such as trigger sources and trigger and event output terminals, that work with a set of predefined string values, but might also accept custom values. For this you can use the utility classes that are part of N

Using Predefined or Custom Values for Source and Output Terminal Properties

#### How Do I Pass a Predefined Value to an NI-DCPower Property?

There are certain properties, such as trigger sources and trigger and event output terminals, that work with a set of predefined string values, but might also accept custom values. For this you can use the utility classes that are part of NI-DCPower .NET API. For example, the InputTerminal property specifies a DCPowerDigitalEdgeSourceTriggerInputTerminal object. You can configure InputTerminal using one of the predefined values, such as:

```text
VB.NET

dcPowerSession.Triggers.MeasureTrigger.DigitalEdge.InputTerminal = DCPowerDigitalEdgeMeasureTriggerInputTerminal.PxiTriggerLine0
```

```text
C# 

dcPowerSession.Triggers.MeasureTrigger.DigitalEdge.InputTerminal = DCPowerDigitalEdgeMeasureTriggerInputTerminal.PxiTriggerLine0;
```

You can also create a custom value with the static FromString method:

```text
VB.NET

dcPowerSession.Triggers.MeasureTrigger.DigitalEdge.InputTerminal = DCPowerDigitalEdgeMeasureTriggerInputTerminal.FromString("CustomInputTerminal")
```

```text
C#

dcPowerSession.Triggers.MeasureTrigger.DigitalEdge.InputTerminal = DCPowerDigitalEdgeMeasureTriggerInputTerminal.FromString("CustomInputTerminal");
```

You can also directly set the source as a string instead of using the FromString method:

```text
VB.NET

dcPowerSession.Triggers.MeasureTrigger.DigitalEdge.InputTerminal = "CustomInputTerminal"
```

```text
C#

dcPowerSession.Triggers.MeasureTrigger.DigitalEdge.InputTerminal = "CustomInputTerminal";
```

#### How Do I Get the Underlying String from Source or Output Terminal Value?

You can use the ToString method to retrieve the underlying source values. For example, the following code shows how to retrieve the source name:

```text
VB.NET

Dim triggerInputTerminal As String = DCPowerDigitalEdgeMeasureTriggerInputTerminal.PxiTriggerLine0.ToString()
```

```text
C#

string triggerInputTerminal = DCPowerDigitalEdgeMeasureTriggerInputTerminal.PxiTriggerLine0.ToString();
```

You can use the underlying string value to assign a source or output terminal to some other source or output terminal.

```text
VB.NET

dcPowerSession1.Events.MeasureCompleteEvent.OutputTerminal = DCPowerMeasureCompleteEventOutputTerminal.PxiTriggerLine0
```

```text
C#

dcPowerSession1.Events.MeasureCompleteEvent.OutputTerminal = DCPowerMeasureCompleteEventOutputTerminal.PxiTriggerLine0;
```

Parent topic:

NI-DCPower .NET Class Library Help

Related information:

- DCPowerDigitalEdgeSourceTriggerInputTerminal Class
- ToString Method
