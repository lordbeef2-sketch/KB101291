# NI OSS SOURCE SNAPSHOT: grpc-device

<!--NI_OSS_SNAPSHOT repo=ni/grpc-device commit=13c1d30177e5da4b0c444b2ceab74506ca3847fb -->

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k.proto sha256=93723be9ae1e36ee5b292d93ba9725816837c838952b4bea93906d868c4afbc0 bytes=104813 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k.proto

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k.proto`
- sha256: `93723be9ae1e36ee5b292d93ba9725816837c838952b4bea93906d868c4afbc0`
- bytes: 104813

````protobuf

//---------------------------------------------------------------------
// This file is generated from NI-rfmxcdma2k API metadata version 25.3.0
//---------------------------------------------------------------------
// Proto file for the NI-rfmxcdma2k Metadata
//---------------------------------------------------------------------
syntax = "proto3";

option java_multiple_files = true;
option java_package = "com.ni.grpc.nirfmxcdma2k";
option java_outer_classname = "NiRFmxCDMA2k";
option csharp_namespace = "NationalInstruments.Grpc.NiRFmxCDMA2k";

package nirfmxcdma2k_grpc;

import "nidevice.proto";
import "session.proto";

service NiRFmxCDMA2k {
  rpc ACPCfgAveraging(ACPCfgAveragingRequest) returns (ACPCfgAveragingResponse);
  rpc ACPCfgMeasurementMethod(ACPCfgMeasurementMethodRequest) returns (ACPCfgMeasurementMethodResponse);
  rpc ACPCfgNoiseCompensationEnabled(ACPCfgNoiseCompensationEnabledRequest) returns (ACPCfgNoiseCompensationEnabledResponse);
  rpc ACPCfgNumberOfOffsets(ACPCfgNumberOfOffsetsRequest) returns (ACPCfgNumberOfOffsetsResponse);
  rpc ACPCfgRBWFilter(ACPCfgRBWFilterRequest) returns (ACPCfgRBWFilterResponse);
  rpc ACPCfgSweepTime(ACPCfgSweepTimeRequest) returns (ACPCfgSweepTimeResponse);
  rpc ACPFetchAbsolutePowersTrace(ACPFetchAbsolutePowersTraceRequest) returns (ACPFetchAbsolutePowersTraceResponse);
  rpc ACPFetchCarrierAbsolutePower(ACPFetchCarrierAbsolutePowerRequest) returns (ACPFetchCarrierAbsolutePowerResponse);
  rpc ACPFetchOffsetMeasurement(ACPFetchOffsetMeasurementRequest) returns (ACPFetchOffsetMeasurementResponse);
  rpc ACPFetchOffsetMeasurementArray(ACPFetchOffsetMeasurementArrayRequest) returns (ACPFetchOffsetMeasurementArrayResponse);
  rpc ACPFetchRelativePowersTrace(ACPFetchRelativePowersTraceRequest) returns (ACPFetchRelativePowersTraceResponse);
  rpc ACPFetchSpectrum(ACPFetchSpectrumRequest) returns (ACPFetchSpectrumResponse);
  rpc AbortMeasurements(AbortMeasurementsRequest) returns (AbortMeasurementsResponse);
  rpc AnalyzeIQ1Waveform(AnalyzeIQ1WaveformRequest) returns (AnalyzeIQ1WaveformResponse);
  rpc AnalyzeIQ1WaveformInterleavedIQ(AnalyzeIQ1WaveformInterleavedIQRequest) returns (AnalyzeIQ1WaveformInterleavedIQResponse);
  rpc AnalyzeIQ1WaveformSplit(AnalyzeIQ1WaveformSplitRequest) returns (AnalyzeIQ1WaveformSplitResponse);
  rpc AnalyzeSpectrum1Waveform(AnalyzeSpectrum1WaveformRequest) returns (AnalyzeSpectrum1WaveformResponse);
  rpc AutoLevel(AutoLevelRequest) returns (AutoLevelResponse);
  rpc BuildChannelString(BuildChannelStringRequest) returns (BuildChannelStringResponse);
  rpc BuildOffsetString(BuildOffsetStringRequest) returns (BuildOffsetStringResponse);
  rpc BuildSignalString(BuildSignalStringRequest) returns (BuildSignalStringResponse);
  rpc CDACfgMeasurementChannel(CDACfgMeasurementChannelRequest) returns (CDACfgMeasurementChannelResponse);
  rpc CDACfgPowerUnit(CDACfgPowerUnitRequest) returns (CDACfgPowerUnitResponse);
  rpc CDACfgSynchronizationModeAndInterval(CDACfgSynchronizationModeAndIntervalRequest) returns (CDACfgSynchronizationModeAndIntervalResponse);
  rpc CDAFetchCodeDomainIAndQPower(CDAFetchCodeDomainIAndQPowerRequest) returns (CDAFetchCodeDomainIAndQPowerResponse);
  rpc CDAFetchCodeDomainIAndQPowerTrace(CDAFetchCodeDomainIAndQPowerTraceRequest) returns (CDAFetchCodeDomainIAndQPowerTraceResponse);
  rpc CDAFetchCodeDomainPower(CDAFetchCodeDomainPowerRequest) returns (CDAFetchCodeDomainPowerResponse);
  rpc CDAFetchIQImpairments(CDAFetchIQImpairmentsRequest) returns (CDAFetchIQImpairmentsResponse);
  rpc CDAFetchSymbolConstellationTrace(CDAFetchSymbolConstellationTraceRequest) returns (CDAFetchSymbolConstellationTraceResponse);
  rpc CDAFetchSymbolConstellationTraceInterleavedIQ(CDAFetchSymbolConstellationTraceInterleavedIQRequest) returns (CDAFetchSymbolConstellationTraceInterleavedIQResponse);
  rpc CDAFetchSymbolConstellationTraceSplit(CDAFetchSymbolConstellationTraceSplitRequest) returns (CDAFetchSymbolConstellationTraceSplitResponse);
  rpc CDAFetchSymbolEVM(CDAFetchSymbolEVMRequest) returns (CDAFetchSymbolEVMResponse);
  rpc CDAFetchSymbolEVMTrace(CDAFetchSymbolEVMTraceRequest) returns (CDAFetchSymbolEVMTraceResponse);
  rpc CDAFetchSymbolMagnitudeErrorTrace(CDAFetchSymbolMagnitudeErrorTraceRequest) returns (CDAFetchSymbolMagnitudeErrorTraceResponse);
  rpc CDAFetchSymbolPhaseErrorTrace(CDAFetchSymbolPhaseErrorTraceRequest) returns (CDAFetchSymbolPhaseErrorTraceResponse);
  rpc CDAFetchSymbolPowerTrace(CDAFetchSymbolPowerTraceRequest) returns (CDAFetchSymbolPowerTraceResponse);
  rpc CHPCfgAveraging(CHPCfgAveragingRequest) returns (CHPCfgAveragingResponse);
  rpc CHPCfgRBWFilter(CHPCfgRBWFilterRequest) returns (CHPCfgRBWFilterResponse);
  rpc CHPCfgSweepTime(CHPCfgSweepTimeRequest) returns (CHPCfgSweepTimeResponse);
  rpc CHPFetchCarrierAbsolutePower(CHPFetchCarrierAbsolutePowerRequest) returns (CHPFetchCarrierAbsolutePowerResponse);
  rpc CHPFetchSpectrum(CHPFetchSpectrumRequest) returns (CHPFetchSpectrumResponse);
  rpc CfgBandClass(CfgBandClassRequest) returns (CfgBandClassResponse);
  rpc CfgChannelConfigurationMode(CfgChannelConfigurationModeRequest) returns (CfgChannelConfigurationModeResponse);
  rpc CfgDigitalEdgeTrigger(CfgDigitalEdgeTriggerRequest) returns (CfgDigitalEdgeTriggerResponse);
  rpc CfgExternalAttenuation(CfgExternalAttenuationRequest) returns (CfgExternalAttenuationResponse);
  rpc CfgFrequency(CfgFrequencyRequest) returns (CfgFrequencyResponse);
  rpc CfgFrequencyChannelNumber(CfgFrequencyChannelNumberRequest) returns (CfgFrequencyChannelNumberResponse);
  rpc CfgFrequencyReference(CfgFrequencyReferenceRequest) returns (CfgFrequencyReferenceResponse);
  rpc CfgIQPowerEdgeTrigger(CfgIQPowerEdgeTriggerRequest) returns (CfgIQPowerEdgeTriggerResponse);
  rpc CfgMechanicalAttenuation(CfgMechanicalAttenuationRequest) returns (CfgMechanicalAttenuationResponse);
  rpc CfgNumberOfChannels(CfgNumberOfChannelsRequest) returns (CfgNumberOfChannelsResponse);
  rpc CfgRF(CfgRFRequest) returns (CfgRFResponse);
  rpc CfgRFAttenuation(CfgRFAttenuationRequest) returns (CfgRFAttenuationResponse);
  rpc CfgRadioConfiguration(CfgRadioConfigurationRequest) returns (CfgRadioConfigurationResponse);
  rpc CfgReferenceLevel(CfgReferenceLevelRequest) returns (CfgReferenceLevelResponse);
  rpc CfgSoftwareEdgeTrigger(CfgSoftwareEdgeTriggerRequest) returns (CfgSoftwareEdgeTriggerResponse);
  rpc CfgUplinkSpreading(CfgUplinkSpreadingRequest) returns (CfgUplinkSpreadingResponse);
  rpc CfgUserDefinedChannel(CfgUserDefinedChannelRequest) returns (CfgUserDefinedChannelResponse);
  rpc CfgUserDefinedChannelArray(CfgUserDefinedChannelArrayRequest) returns (CfgUserDefinedChannelArrayResponse);
  rpc CheckMeasurementStatus(CheckMeasurementStatusRequest) returns (CheckMeasurementStatusResponse);
  rpc ClearAllNamedResults(ClearAllNamedResultsRequest) returns (ClearAllNamedResultsResponse);
  rpc ClearNamedResult(ClearNamedResultRequest) returns (ClearNamedResultResponse);
  rpc CloneSignalConfiguration(CloneSignalConfigurationRequest) returns (CloneSignalConfigurationResponse);
  rpc Close(CloseRequest) returns (CloseResponse);
  rpc Commit(CommitRequest) returns (CommitResponse);
  rpc CreateSignalConfiguration(CreateSignalConfigurationRequest) returns (CreateSignalConfigurationResponse);
  rpc DeleteSignalConfiguration(DeleteSignalConfigurationRequest) returns (DeleteSignalConfigurationResponse);
  rpc DisableTrigger(DisableTriggerRequest) returns (DisableTriggerResponse);
  rpc GetAllNamedResultNames(GetAllNamedResultNamesRequest) returns (GetAllNamedResultNamesResponse);
  rpc GetAttributeF32(GetAttributeF32Request) returns (GetAttributeF32Response);
  rpc GetAttributeF32Array(GetAttributeF32ArrayRequest) returns (GetAttributeF32ArrayResponse);
  rpc GetAttributeF64(GetAttributeF64Request) returns (GetAttributeF64Response);
  rpc GetAttributeF64Array(GetAttributeF64ArrayRequest) returns (GetAttributeF64ArrayResponse);
  rpc GetAttributeI16(GetAttributeI16Request) returns (GetAttributeI16Response);
  rpc GetAttributeI32(GetAttributeI32Request) returns (GetAttributeI32Response);
  rpc GetAttributeI32Array(GetAttributeI32ArrayRequest) returns (GetAttributeI32ArrayResponse);
  rpc GetAttributeI64(GetAttributeI64Request) returns (GetAttributeI64Response);
  rpc GetAttributeI64Array(GetAttributeI64ArrayRequest) returns (GetAttributeI64ArrayResponse);
  rpc GetAttributeI8(GetAttributeI8Request) returns (GetAttributeI8Response);
  rpc GetAttributeI8Array(GetAttributeI8ArrayRequest) returns (GetAttributeI8ArrayResponse);
  rpc GetAttributeNIComplexDoubleArray(GetAttributeNIComplexDoubleArrayRequest) returns (GetAttributeNIComplexDoubleArrayResponse);
  rpc GetAttributeNIComplexSingleArray(GetAttributeNIComplexSingleArrayRequest) returns (GetAttributeNIComplexSingleArrayResponse);
  rpc GetAttributeString(GetAttributeStringRequest) returns (GetAttributeStringResponse);
  rpc GetAttributeU16(GetAttributeU16Request) returns (GetAttributeU16Response);
  rpc GetAttributeU32(GetAttributeU32Request) returns (GetAttributeU32Response);
  rpc GetAttributeU32Array(GetAttributeU32ArrayRequest) returns (GetAttributeU32ArrayResponse);
  rpc GetAttributeU64Array(GetAttributeU64ArrayRequest) returns (GetAttributeU64ArrayResponse);
  rpc GetAttributeU8(GetAttributeU8Request) returns (GetAttributeU8Response);
  rpc GetAttributeU8Array(GetAttributeU8ArrayRequest) returns (GetAttributeU8ArrayResponse);
  rpc GetError(GetErrorRequest) returns (GetErrorResponse);
  rpc GetErrorString(GetErrorStringRequest) returns (GetErrorStringResponse);
  rpc Initialize(InitializeRequest) returns (InitializeResponse);
  rpc InitializeFromNIRFSASession(InitializeFromNIRFSASessionRequest) returns (InitializeFromNIRFSASessionResponse);
  rpc Initiate(InitiateRequest) returns (InitiateResponse);
  rpc ModAccCfgSynchronizationModeAndInterval(ModAccCfgSynchronizationModeAndIntervalRequest) returns (ModAccCfgSynchronizationModeAndIntervalResponse);
  rpc ModAccFetchConstellationTrace(ModAccFetchConstellationTraceRequest) returns (ModAccFetchConstellationTraceResponse);
  rpc ModAccFetchConstellationTraceInterleavedIQ(ModAccFetchConstellationTraceInterleavedIQRequest) returns (ModAccFetchConstellationTraceInterleavedIQResponse);
  rpc ModAccFetchConstellationTraceSplit(ModAccFetchConstellationTraceSplitRequest) returns (ModAccFetchConstellationTraceSplitResponse);
  rpc ModAccFetchDetectedChannel(ModAccFetchDetectedChannelRequest) returns (ModAccFetchDetectedChannelResponse);
  rpc ModAccFetchDetectedChannelArray(ModAccFetchDetectedChannelArrayRequest) returns (ModAccFetchDetectedChannelArrayResponse);
  rpc ModAccFetchEVM(ModAccFetchEVMRequest) returns (ModAccFetchEVMResponse);
  rpc ModAccFetchEVMTrace(ModAccFetchEVMTraceRequest) returns (ModAccFetchEVMTraceResponse);
  rpc ModAccFetchIQImpairments(ModAccFetchIQImpairmentsRequest) returns (ModAccFetchIQImpairmentsResponse);
  rpc ModAccFetchMagnitudeErrorTrace(ModAccFetchMagnitudeErrorTraceRequest) returns (ModAccFetchMagnitudeErrorTraceResponse);
  rpc ModAccFetchNumberOfDetectedChannels(ModAccFetchNumberOfDetectedChannelsRequest) returns (ModAccFetchNumberOfDetectedChannelsResponse);
  rpc ModAccFetchPeakActiveCDE(ModAccFetchPeakActiveCDERequest) returns (ModAccFetchPeakActiveCDEResponse);
  rpc ModAccFetchPeakCDE(ModAccFetchPeakCDERequest) returns (ModAccFetchPeakCDEResponse);
  rpc ModAccFetchPhaseErrorTrace(ModAccFetchPhaseErrorTraceRequest) returns (ModAccFetchPhaseErrorTraceResponse);
  rpc OBWCfgAveraging(OBWCfgAveragingRequest) returns (OBWCfgAveragingResponse);
  rpc OBWCfgRBWFilter(OBWCfgRBWFilterRequest) returns (OBWCfgRBWFilterResponse);
  rpc OBWCfgSweepTime(OBWCfgSweepTimeRequest) returns (OBWCfgSweepTimeResponse);
  rpc OBWFetchMeasurement(OBWFetchMeasurementRequest) returns (OBWFetchMeasurementResponse);
  rpc OBWFetchSpectrum(OBWFetchSpectrumRequest) returns (OBWFetchSpectrumResponse);
  rpc QEVMCfgAveraging(QEVMCfgAveragingRequest) returns (QEVMCfgAveragingResponse);
  rpc QEVMCfgMeasurementLength(QEVMCfgMeasurementLengthRequest) returns (QEVMCfgMeasurementLengthResponse);
  rpc QEVMFetchConstellationTrace(QEVMFetchConstellationTraceRequest) returns (QEVMFetchConstellationTraceResponse);
  rpc QEVMFetchConstellationTraceInterleavedIQ(QEVMFetchConstellationTraceInterleavedIQRequest) returns (QEVMFetchConstellationTraceInterleavedIQResponse);
  rpc QEVMFetchConstellationTraceSplit(QEVMFetchConstellationTraceSplitRequest) returns (QEVMFetchConstellationTraceSplitResponse);
  rpc QEVMFetchEVM(QEVMFetchEVMRequest) returns (QEVMFetchEVMResponse);
  rpc QEVMFetchEVMTrace(QEVMFetchEVMTraceRequest) returns (QEVMFetchEVMTraceResponse);
  rpc QEVMFetchIQImpairments(QEVMFetchIQImpairmentsRequest) returns (QEVMFetchIQImpairmentsResponse);
  rpc QEVMFetchMagnitudeErrorTrace(QEVMFetchMagnitudeErrorTraceRequest) returns (QEVMFetchMagnitudeErrorTraceResponse);
  rpc QEVMFetchPhaseErrorTrace(QEVMFetchPhaseErrorTraceRequest) returns (QEVMFetchPhaseErrorTraceResponse);
  rpc ResetAttribute(ResetAttributeRequest) returns (ResetAttributeResponse);
  rpc ResetToDefault(ResetToDefaultRequest) returns (ResetToDefaultResponse);
  rpc SEMCfgAveraging(SEMCfgAveragingRequest) returns (SEMCfgAveragingResponse);
  rpc SEMCfgSweepTime(SEMCfgSweepTimeRequest) returns (SEMCfgSweepTimeResponse);
  rpc SEMFetchCarrierAbsoluteIntegratedPower(SEMFetchCarrierAbsoluteIntegratedPowerRequest) returns (SEMFetchCarrierAbsoluteIntegratedPowerResponse);
  rpc SEMFetchLowerOffsetMargin(SEMFetchLowerOffsetMarginRequest) returns (SEMFetchLowerOffsetMarginResponse);
  rpc SEMFetchLowerOffsetMarginArray(SEMFetchLowerOffsetMarginArrayRequest) returns (SEMFetchLowerOffsetMarginArrayResponse);
  rpc SEMFetchLowerOffsetPower(SEMFetchLowerOffsetPowerRequest) returns (SEMFetchLowerOffsetPowerResponse);
  rpc SEMFetchLowerOffsetPowerArray(SEMFetchLowerOffsetPowerArrayRequest) returns (SEMFetchLowerOffsetPowerArrayResponse);
  rpc SEMFetchMeasurementStatus(SEMFetchMeasurementStatusRequest) returns (SEMFetchMeasurementStatusResponse);
  rpc SEMFetchSpectrum(SEMFetchSpectrumRequest) returns (SEMFetchSpectrumResponse);
  rpc SEMFetchUpperOffsetMargin(SEMFetchUpperOffsetMarginRequest) returns (SEMFetchUpperOffsetMarginResponse);
  rpc SEMFetchUpperOffsetMarginArray(SEMFetchUpperOffsetMarginArrayRequest) returns (SEMFetchUpperOffsetMarginArrayResponse);
  rpc SEMFetchUpperOffsetPower(SEMFetchUpperOffsetPowerRequest) returns (SEMFetchUpperOffsetPowerResponse);
  rpc SEMFetchUpperOffsetPowerArray(SEMFetchUpperOffsetPowerArrayRequest) returns (SEMFetchUpperOffsetPowerArrayResponse);
  rpc SelectMeasurements(SelectMeasurementsRequest) returns (SelectMeasurementsResponse);
  rpc SendSoftwareEdgeTrigger(SendSoftwareEdgeTriggerRequest) returns (SendSoftwareEdgeTriggerResponse);
  rpc SetAttributeF32(SetAttributeF32Request) returns (SetAttributeF32Response);
  rpc SetAttributeF32Array(SetAttributeF32ArrayRequest) returns (SetAttributeF32ArrayResponse);
  rpc SetAttributeF64(SetAttributeF64Request) returns (SetAttributeF64Response);
  rpc SetAttributeF64Array(SetAttributeF64ArrayRequest) returns (SetAttributeF64ArrayResponse);
  rpc SetAttributeI16(SetAttributeI16Request) returns (SetAttributeI16Response);
  rpc SetAttributeI32(SetAttributeI32Request) returns (SetAttributeI32Response);
  rpc SetAttributeI32Array(SetAttributeI32ArrayRequest) returns (SetAttributeI32ArrayResponse);
  rpc SetAttributeI64(SetAttributeI64Request) returns (SetAttributeI64Response);
  rpc SetAttributeI64Array(SetAttributeI64ArrayRequest) returns (SetAttributeI64ArrayResponse);
  rpc SetAttributeI8(SetAttributeI8Request) returns (SetAttributeI8Response);
  rpc SetAttributeI8Array(SetAttributeI8ArrayRequest) returns (SetAttributeI8ArrayResponse);
  rpc SetAttributeNIComplexDoubleArray(SetAttributeNIComplexDoubleArrayRequest) returns (SetAttributeNIComplexDoubleArrayResponse);
  rpc SetAttributeNIComplexSingleArray(SetAttributeNIComplexSingleArrayRequest) returns (SetAttributeNIComplexSingleArrayResponse);
  rpc SetAttributeString(SetAttributeStringRequest) returns (SetAttributeStringResponse);
  rpc SetAttributeU16(SetAttributeU16Request) returns (SetAttributeU16Response);
  rpc SetAttributeU32(SetAttributeU32Request) returns (SetAttributeU32Response);
  rpc SetAttributeU32Array(SetAttributeU32ArrayRequest) returns (SetAttributeU32ArrayResponse);
  rpc SetAttributeU64Array(SetAttributeU64ArrayRequest) returns (SetAttributeU64ArrayResponse);
  rpc SetAttributeU8(SetAttributeU8Request) returns (SetAttributeU8Response);
  rpc SetAttributeU8Array(SetAttributeU8ArrayRequest) returns (SetAttributeU8ArrayResponse);
  rpc SlotPhaseCfgSynchronizationModeAndInterval(SlotPhaseCfgSynchronizationModeAndIntervalRequest) returns (SlotPhaseCfgSynchronizationModeAndIntervalResponse);
  rpc SlotPhaseFetchChipPhaseErrorLinearFitTrace(SlotPhaseFetchChipPhaseErrorLinearFitTraceRequest) returns (SlotPhaseFetchChipPhaseErrorLinearFitTraceResponse);
  rpc SlotPhaseFetchChipPhaseErrorTrace(SlotPhaseFetchChipPhaseErrorTraceRequest) returns (SlotPhaseFetchChipPhaseErrorTraceResponse);
  rpc SlotPhaseFetchMaximumPhaseDiscontinuity(SlotPhaseFetchMaximumPhaseDiscontinuityRequest) returns (SlotPhaseFetchMaximumPhaseDiscontinuityResponse);
  rpc SlotPhaseFetchPhaseDiscontinuities(SlotPhaseFetchPhaseDiscontinuitiesRequest) returns (SlotPhaseFetchPhaseDiscontinuitiesResponse);
  rpc SlotPowerCfgSynchronizationModeAndInterval(SlotPowerCfgSynchronizationModeAndIntervalRequest) returns (SlotPowerCfgSynchronizationModeAndIntervalResponse);
  rpc SlotPowerFetchPowers(SlotPowerFetchPowersRequest) returns (SlotPowerFetchPowersResponse);
  rpc WaitForAcquisitionComplete(WaitForAcquisitionCompleteRequest) returns (WaitForAcquisitionCompleteResponse);
  rpc WaitForMeasurementComplete(WaitForMeasurementCompleteRequest) returns (WaitForMeasurementCompleteResponse);
}

enum NiRFmxCDMA2kAttribute {
  NIRFMXCDMA2K_ATTRIBUTE_UNSPECIFIED = 0;
  NIRFMXCDMA2K_ATTRIBUTE_CENTER_FREQUENCY = 6291457;
  NIRFMXCDMA2K_ATTRIBUTE_REFERENCE_LEVEL = 6291458;
  NIRFMXCDMA2K_ATTRIBUTE_EXTERNAL_ATTENUATION = 6291459;
  NIRFMXCDMA2K_ATTRIBUTE_TRIGGER_TYPE = 6291460;
  NIRFMXCDMA2K_ATTRIBUTE_DIGITAL_EDGE_TRIGGER_SOURCE = 6291461;
  NIRFMXCDMA2K_ATTRIBUTE_DIGITAL_EDGE_TRIGGER_EDGE = 6291462;
  NIRFMXCDMA2K_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_SOURCE = 6291463;
  NIRFMXCDMA2K_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_LEVEL = 6291464;
  NIRFMXCDMA2K_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_SLOPE = 6291465;
  NIRFMXCDMA2K_ATTRIBUTE_TRIGGER_DELAY = 6291466;
  NIRFMXCDMA2K_ATTRIBUTE_TRIGGER_MINIMUM_QUIET_TIME_MODE = 6291467;
  NIRFMXCDMA2K_ATTRIBUTE_TRIGGER_MINIMUM_QUIET_TIME_DURATION = 6291468;
  NIRFMXCDMA2K_ATTRIBUTE_LINK_DIRECTION = 6291469;
  NIRFMXCDMA2K_ATTRIBUTE_BAND_CLASS = 6291472;
  NIRFMXCDMA2K_ATTRIBUTE_RADIO_CONFIGURATION = 6291473;
  NIRFMXCDMA2K_ATTRIBUTE_CHANNEL_CONFIGURATION_MODE = 6291474;
  NIRFMXCDMA2K_ATTRIBUTE_NUMBER_OF_CHANNELS = 6291478;
  NIRFMXCDMA2K_ATTRIBUTE_WALSH_CODE_LENGTH = 6291479;
  NIRFMXCDMA2K_ATTRIBUTE_WALSH_CODE_NUMBER = 6291480;
  NIRFMXCDMA2K_ATTRIBUTE_BRANCH = 6291481;
  NIRFMXCDMA2K_ATTRIBUTE_UPLINK_SPREADING_LONG_CODE_MASK = 6291486;
  NIRFMXCDMA2K_ATTRIBUTE_DOWNLINK_SPREADING_PN_OFFSET = 6291488;
  NIRFMXCDMA2K_ATTRIBUTE_REFERENCE_LEVEL_HEADROOM = 6295548;
  NIRFMXCDMA2K_ATTRIBUTE_SELECTED_PORTS = 6295549;
  NIRFMXCDMA2K_ATTRIBUTE_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE = 6295551;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_MEASUREMENT_ENABLED = 6295552;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_CARRIER_INTEGRATION_BANDWIDTH = 6295557;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_NUMBER_OF_OFFSETS = 6295560;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_OFFSET_FREQUENCY = 6295562;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_OFFSET_INTEGRATION_BANDWIDTH = 6295566;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_MEASUREMENT_METHOD = 6295570;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_NUMBER_OF_ANALYSIS_THREADS = 6295572;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_AVERAGING_COUNT = 6295573;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_AVERAGING_ENABLED = 6295574;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_AVERAGING_TYPE = 6295576;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RBW_FILTER_AUTO_BANDWIDTH = 6295579;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RBW_FILTER_BANDWIDTH = 6295580;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RBW_FILTER_TYPE = 6295581;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_SWEEP_TIME_AUTO = 6295582;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_SWEEP_TIME_INTERVAL = 6295583;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_NOISE_COMPENSATION_ENABLED = 6295584;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_ALL_TRACES_ENABLED = 6295585;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RESULTS_CARRIER_ABSOLUTE_POWER = 6295590;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RESULTS_LOWER_OFFSET_ABSOLUTE_POWER = 6295596;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RESULTS_LOWER_OFFSET_RELATIVE_POWER = 6295597;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RESULTS_UPPER_OFFSET_ABSOLUTE_POWER = 6295602;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_RESULTS_UPPER_OFFSET_RELATIVE_POWER = 6295603;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_IF_OUTPUT_POWER_OFFSET_AUTO = 6295604;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_NEAR_IF_OUTPUT_POWER_OFFSET = 6295605;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_FAR_IF_OUTPUT_POWER_OFFSET = 6295606;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_SEQUENTIAL_FFT_SIZE = 6295608;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_FFT_OVERLAP_MODE = 6295609;
  NIRFMXCDMA2K_ATTRIBUTE_ACP_FFT_OVERLAP = 6295610;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_MEASUREMENT_ENABLED = 6303744;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_INTEGRATION_BANDWIDTH = 6303746;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_NUMBER_OF_ANALYSIS_THREADS = 6303747;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_AVERAGING_COUNT = 6303750;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_AVERAGING_ENABLED = 6303751;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_AVERAGING_TYPE = 6303753;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_RBW_FILTER_AUTO_BANDWIDTH = 6303756;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_RBW_FILTER_BANDWIDTH = 6303757;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_RBW_FILTER_TYPE = 6303758;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_SWEEP_TIME_AUTO = 6303761;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_SWEEP_TIME_INTERVAL = 6303762;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_ALL_TRACES_ENABLED = 6303764;
  NIRFMXCDMA2K_ATTRIBUTE_CHP_RESULTS_CARRIER_ABSOLUTE_POWER = 6303765;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_MEASUREMENT_ENABLED = 6316032;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_NUMBER_OF_ANALYSIS_THREADS = 6316035;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_SPAN = 6316036;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_AVERAGING_COUNT = 6316038;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_AVERAGING_ENABLED = 6316039;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_AVERAGING_TYPE = 6316041;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RBW_FILTER_AUTO_BANDWIDTH = 6316044;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RBW_FILTER_BANDWIDTH = 6316045;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RBW_FILTER_TYPE = 6316046;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_SWEEP_TIME_AUTO = 6316047;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_SWEEP_TIME_INTERVAL = 6316048;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_ALL_TRACES_ENABLED = 6316050;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RESULTS_OCCUPIED_BANDWIDTH = 6316051;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RESULTS_ABSOLUTE_POWER = 6316052;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RESULTS_START_FREQUENCY = 6316053;
  NIRFMXCDMA2K_ATTRIBUTE_OBW_RESULTS_STOP_FREQUENCY = 6316054;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_MEASUREMENT_ENABLED = 6324224;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_CARRIER_INTEGRATION_BANDWIDTH = 6324229;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_NUMBER_OF_OFFSETS = 6324235;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_OFFSET_BANDWIDTH_INTEGRAL = 6324236;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_OFFSET_START_FREQUENCY = 6324244;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_OFFSET_STOP_FREQUENCY = 6324245;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_OFFSET_RBW_FILTER_BANDWIDTH = 6324247;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_OFFSET_RBW_FILTER_TYPE = 6324248;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_NUMBER_OF_ANALYSIS_THREADS = 6324253;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_AVERAGING_COUNT = 6324254;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_AVERAGING_ENABLED = 6324255;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_AVERAGING_TYPE = 6324257;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_SWEEP_TIME_AUTO = 6324261;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_SWEEP_TIME_INTERVAL = 6324262;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_ALL_TRACES_ENABLED = 6324263;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_MEASUREMENT_STATUS = 6324265;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_CARRIER_ABSOLUTE_INTEGRATED_POWER = 6324269;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_INTEGRATED_POWER = 6324276;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_RELATIVE_INTEGRATED_POWER = 6324277;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_ABSOLUTE_PEAK_POWER = 6324278;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_RELATIVE_PEAK_POWER = 6324279;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_PEAK_FREQUENCY = 6324280;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN = 6324281;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN_ABSOLUTE_POWER = 6324282;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN_RELATIVE_POWER = 6324283;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MARGIN_FREQUENCY = 6324284;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_LOWER_OFFSET_MEASUREMENT_STATUS = 6324285;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_INTEGRATED_POWER = 6324289;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_RELATIVE_INTEGRATED_POWER = 6324290;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_ABSOLUTE_PEAK_POWER = 6324291;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_RELATIVE_PEAK_POWER = 6324292;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_PEAK_FREQUENCY = 6324293;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN = 6324294;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN_ABSOLUTE_POWER = 6324295;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN_RELATIVE_POWER = 6324296;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MARGIN_FREQUENCY = 6324297;
  NIRFMXCDMA2K_ATTRIBUTE_SEM_RESULTS_UPPER_OFFSET_MEASUREMENT_STATUS = 6324298;
  NIRFMXCDMA2K_ATTRIBUTE_RESULT_FETCH_TIMEOUT = 6340608;
  NIRFMXCDMA2K_ATTRIBUTE_AUTO_LEVEL_INITIAL_REFERENCE_LEVEL = 6344704;
  NIRFMXCDMA2K_ATTRIBUTE_LIMITED_CONFIGURATION_CHANGE = 6344707;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_MEASUREMENT_ENABLED = 6361088;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_SYNCHRONIZATION_MODE = 6361093;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_MEASUREMENT_OFFSET = 6361094;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_MEASUREMENT_LENGTH = 6361095;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_IQ_OFFSET_REMOVAL_ENABLED = 6361096;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_SPECTRUM_INVERTED = 6361097;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_MULTI_CARRIER_FILTER_ENABLED = 6361104;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_ALL_TRACES_ENABLED = 6361109;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_RMS_EVM = 6361120;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_EVM = 6361121;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_RMS_MAGNITUDE_ERROR = 6361122;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_RMS_PHASE_ERROR = 6361123;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_IQ_ORIGIN_OFFSET = 6361124;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_IQ_GAIN_IMBALANCE = 6361125;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_IQ_QUADRATURE_ERROR = 6361126;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_FREQUENCY_ERROR = 6361127;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_RHO = 6361128;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_CDE = 6361129;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_CDE_WALSH_CODE_NUMBER = 6361131;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_ACTIVE_CDE = 6361132;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_LENGTH = 6361133;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_ACTIVE_CDE_WALSH_CODE_NUMBER = 6361135;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_SLOT_TIMING_ERROR = 6361136;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_CHIP_RATE_ERROR = 6361139;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_NUMBER_OF_DETECTED_CHANNELS = 6361140;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_DETECTED_WALSH_CODE_LENGTH = 6361141;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_DETECTED_WALSH_CODE_NUMBER = 6361142;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_DETECTED_BRANCH = 6361143;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_CDE_BRANCH = 6361144;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RESULTS_PEAK_ACTIVE_CDE_BRANCH = 6361145;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED = 6361249;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED = 6361250;
  NIRFMXCDMA2K_ATTRIBUTE_MODACC_RECEIVE_FILTER_ENABLED = 6361251;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_MEASUREMENT_ENABLED = 6365184;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_MEASUREMENT_LENGTH = 6365186;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_AVERAGING_ENABLED = 6365187;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_AVERAGING_COUNT = 6365188;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_SPECTRUM_INVERTED = 6365189;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_IQ_OFFSET_REMOVAL_ENABLED = 6365190;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED = 6365191;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED = 6365192;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RECEIVE_FILTER_ENABLED = 6365193;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_ALL_TRACES_ENABLED = 6365194;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_NUMBER_OF_ANALYSIS_THREADS = 6365195;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_RMS_EVM = 6365197;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_RMS_EVM = 6365198;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_PEAK_EVM = 6365199;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_PEAK_EVM = 6365200;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_MAGNITUDE_ERROR = 6365201;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_MAGNITUDE_ERROR = 6365202;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_PHASE_ERROR = 6365203;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_PHASE_ERROR = 6365204;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_FREQUENCY_ERROR = 6365205;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_FREQUENCY_ERROR = 6365206;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_IQ_ORIGIN_OFFSET = 6365207;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_IQ_ORIGIN_OFFSET = 6365208;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_IQ_GAIN_IMBALANCE = 6365209;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_IQ_GAIN_IMBALANCE = 6365210;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_IQ_QUADRATURE_ERROR = 6365211;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_IQ_QUADRATURE_ERROR = 6365212;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MEAN_CHIP_RATE_ERROR = 6365213;
  NIRFMXCDMA2K_ATTRIBUTE_QEVM_RESULTS_MAXIMUM_CHIP_RATE_ERROR = 6365214;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_MEASUREMENT_ENABLED = 6369280;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_SYNCHRONIZATION_MODE = 6369282;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_MEASUREMENT_OFFSET = 6369283;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_MEASUREMENT_LENGTH = 6369284;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_BASE_SPREADING_FACTOR = 6369285;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_LENGTH = 6369286;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_MEASUREMENT_CHANNEL_WALSH_CODE_NUMBER = 6369287;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_MEASUREMENT_CHANNEL_BRANCH = 6369288;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_POWER_UNIT = 6369289;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_SPECTRUM_INVERTED = 6369290;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_IQ_OFFSET_REMOVAL_ENABLED = 6369291;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED = 6369292;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED = 6369293;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RECEIVE_FILTER_ENABLED = 6369294;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_ALL_TRACES_ENABLED = 6369295;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_RMS_SYMBOL_EVM = 6369298;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_PEAK_SYMBOL_EVM = 6369299;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_RMS_SYMBOL_MAGNITUDE_ERROR = 6369300;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_RMS_SYMBOL_PHASE_ERROR = 6369301;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_MEAN_SYMBOL_POWER = 6369302;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_TOTAL_POWER = 6369303;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_TOTAL_ACTIVE_POWER = 6369304;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_MEAN_ACTIVE_POWER = 6369305;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_PEAK_ACTIVE_POWER = 6369306;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_MEAN_INACTIVE_POWER = 6369307;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_PEAK_INACTIVE_POWER = 6369308;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_I_MEAN_ACTIVE_POWER = 6369309;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_I_PEAK_INACTIVE_POWER = 6369310;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_Q_MEAN_ACTIVE_POWER = 6369311;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_Q_PEAK_INACTIVE_POWER = 6369312;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_MEAN_PILOT_POWER = 6369313;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_IQ_ORIGIN_OFFSET = 6369314;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_IQ_GAIN_IMBALANCE = 6369315;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_IQ_QUADRATURE_ERROR = 6369316;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_FREQUENCY_ERROR = 6369317;
  NIRFMXCDMA2K_ATTRIBUTE_CDA_RESULTS_CHIP_RATE_ERROR = 6369318;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPOWER_MEASUREMENT_ENABLED = 6373376;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPOWER_SYNCHRONIZATION_MODE = 6373378;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPOWER_MEASUREMENT_OFFSET = 6373379;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPOWER_MEASUREMENT_LENGTH = 6373380;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPOWER_SPECTRUM_INVERTED = 6373381;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPOWER_RECEIVE_FILTER_ENABLED = 6373382;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_MEASUREMENT_ENABLED = 6377472;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_SYNCHRONIZATION_MODE = 6377474;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_MEASUREMENT_OFFSET = 6377475;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_MEASUREMENT_LENGTH = 6377476;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_SPECTRUM_INVERTED = 6377477;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_RECEIVE_FILTER_ENABLED = 6377478;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_TRANSIENT_DURATION = 6377479;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_ALL_TRACES_ENABLED = 6377480;
  NIRFMXCDMA2K_ATTRIBUTE_SLOTPHASE_RESULTS_MAXIMUM_PHASE_DISCONTINUITY = 6377483;
}

enum AcpAveragingEnabled {
  ACP_AVERAGING_ENABLED_FALSE = 0;
  ACP_AVERAGING_ENABLED_TRUE = 1;
}

enum AcpAveragingType {
  ACP_AVERAGING_TYPE_RMS = 0;
  ACP_AVERAGING_TYPE_LOG = 1;
  ACP_AVERAGING_TYPE_SCALAR = 2;
  ACP_AVERAGING_TYPE_MAXIMUM = 3;
  ACP_AVERAGING_TYPE_MINIMUM = 4;
}

enum AcpMeasurementMethod {
  ACP_MEASUREMENT_METHOD_NORMAL = 0;
  ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE = 1;
  ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT = 2;
}

enum AcpNoiseCompensationEnabled {
  ACP_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  ACP_NOISE_COMPENSATION_ENABLED_TRUE = 1;
}

enum AcpRbwAutoBandwidth {
  ACP_RBW_AUTO_BANDWIDTH_FALSE = 0;
  ACP_RBW_AUTO_BANDWIDTH_TRUE = 1;
}

enum AcpRbwFilterType {
  ACP_RBW_FILTER_TYPE_FFT_BASED = 0;
  ACP_RBW_FILTER_TYPE_GAUSSIAN = 1;
  ACP_RBW_FILTER_TYPE_FLAT = 2;
}

enum AcpSweepTimeAuto {
  ACP_SWEEP_TIME_AUTO_FALSE = 0;
  ACP_SWEEP_TIME_AUTO_TRUE = 1;
}

enum Branch {
  BRANCH_I = 0;
  BRANCH_Q = 1;
  BRANCH_I_AND_Q = 2;
}

enum CdaMeasurementChannelBranch {
  CDA_MEASUREMENT_CHANNEL_BRANCH_I = 0;
  CDA_MEASUREMENT_CHANNEL_BRANCH_Q = 1;
}

enum CdaPowerUnit {
  CDA_POWER_UNIT_DB = 0;
  CDA_POWER_UNIT_DBM = 1;
}

enum CdaSynchronizationMode {
  CDA_SYNCHRONIZATION_MODE_FRAME = 0;
  CDA_SYNCHRONIZATION_MODE_SLOT = 1;
  CDA_SYNCHRONIZATION_MODE_ARBITRARY = 2;
}

enum ChannelConfigurationMode {
  CHANNEL_CONFIGURATION_MODE_AUTO_DETECT = 0;
  CHANNEL_CONFIGURATION_MODE_USER_DEFINED = 1;
}

enum ChpAveragingEnabled {
  CHP_AVERAGING_ENABLED_FALSE = 0;
  CHP_AVERAGING_ENABLED_TRUE = 1;
}

enum ChpAveragingType {
  CHP_AVERAGING_TYPE_RMS = 0;
  CHP_AVERAGING_TYPE_LOG = 1;
  CHP_AVERAGING_TYPE_SCALAR = 2;
  CHP_AVERAGING_TYPE_MAXIMUM = 3;
  CHP_AVERAGING_TYPE_MINIMUM = 4;
}

enum ChpRbwAutoBandwidth {
  CHP_RBW_AUTO_BANDWIDTH_FALSE = 0;
  CHP_RBW_AUTO_BANDWIDTH_TRUE = 1;
}

enum ChpRbwFilterType {
  CHP_RBW_FILTER_TYPE_FFT_BASED = 0;
  CHP_RBW_FILTER_TYPE_GAUSSIAN = 1;
  CHP_RBW_FILTER_TYPE_FLAT = 2;
}

enum ChpSweepTimeAuto {
  CHP_SWEEP_TIME_AUTO_FALSE = 0;
  CHP_SWEEP_TIME_AUTO_TRUE = 1;
}

enum DigitalEdgeTriggerEdge {
  DIGITAL_EDGE_TRIGGER_EDGE_RISING = 0;
  DIGITAL_EDGE_TRIGGER_EDGE_FALLING = 1;
}

enum DigitalEdgeTriggerSource {
  DIGITAL_EDGE_TRIGGER_SOURCE_UNSPECIFIED = 0;
  DIGITAL_EDGE_TRIGGER_SOURCE_PFI0 = 1;
  DIGITAL_EDGE_TRIGGER_SOURCE_PFI1 = 2;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0 = 3;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG1 = 4;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG2 = 5;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG3 = 6;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG4 = 7;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG5 = 8;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG6 = 9;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG7 = 10;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXI_STAR = 11;
  DIGITAL_EDGE_TRIGGER_SOURCE_PXIE_DSTARB = 12;
  DIGITAL_EDGE_TRIGGER_SOURCE_TIMER_EVENT = 13;
  DIGITAL_EDGE_TRIGGER_SOURCE_PULSE_IN = 14;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI0 = 15;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI1 = 16;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI2 = 17;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI3 = 18;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI4 = 19;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI5 = 20;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI6 = 21;
  DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI7 = 22;
}

enum FrequencyReferenceSource {
  FREQUENCY_REFERENCE_SOURCE_UNSPECIFIED = 0;
  FREQUENCY_REFERENCE_SOURCE_ONBOARD_CLOCK = 1;
  FREQUENCY_REFERENCE_SOURCE_REF_IN = 2;
  FREQUENCY_REFERENCE_SOURCE_PXI_CLK = 3;
  FREQUENCY_REFERENCE_SOURCE_CLK_IN = 4;
}

enum IQPowerEdgeTriggerLevelType {
  IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE = 0;
  IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE = 1;
}

enum IQPowerEdgeTriggerSlope {
  IQ_POWER_EDGE_TRIGGER_SLOPE_RISING = 0;
  IQ_POWER_EDGE_TRIGGER_SLOPE_FALLING = 1;
}

enum LinkDirection {
  LINK_DIRECTION_UNSPECIFIED = 0;
  LINK_DIRECTION_UPLINK = 1;
}

enum MeasurementTypes {
  MEASUREMENT_TYPES_UNSPECIFIED = 0;
  MEASUREMENT_TYPES_MODACC = 1;
  MEASUREMENT_TYPES_ACP = 2;
  MEASUREMENT_TYPES_CHP = 4;
  MEASUREMENT_TYPES_OBW = 8;
  MEASUREMENT_TYPES_SEM = 16;
  MEASUREMENT_TYPES_QEVM = 32;
  MEASUREMENT_TYPES_CDA = 64;
  MEASUREMENT_TYPES_SLOTPHASE = 128;
  MEASUREMENT_TYPES_SLOTPOWER = 256;
}

enum MechanicalAttenuationAuto {
  MECHANICAL_ATTENUATION_AUTO_FALSE = 0;
  MECHANICAL_ATTENUATION_AUTO_TRUE = 1;
}

enum ModAccDetectedBranch {
  MODACC_DETECTED_BRANCH_I = 0;
  MODACC_DETECTED_BRANCH_Q = 1;
  MODACC_DETECTED_BRANCH_I_AND_Q = 2;
}

enum ModAccPeakActiveCdeBranch {
  MODACC_PEAK_ACTIVE_CDE_BRANCH_I = 0;
  MODACC_PEAK_ACTIVE_CDE_BRANCH_Q = 1;
  MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q = 2;
}

enum ModAccPeakCdeBranch {
  MODACC_PEAK_CDE_BRANCH_I = 0;
  MODACC_PEAK_CDE_BRANCH_Q = 1;
  MODACC_PEAK_CDE_BRANCH_I_AND_Q = 2;
}

enum ModAccSynchronizationMode {
  MODACC_SYNCHRONIZATION_MODE_FRAME = 0;
  MODACC_SYNCHRONIZATION_MODE_SLOT = 1;
  MODACC_SYNCHRONIZATION_MODE_ARBITRARY = 2;
}

enum ObwAveragingEnabled {
  OBW_AVERAGING_ENABLED_FALSE = 0;
  OBW_AVERAGING_ENABLED_TRUE = 1;
}

enum ObwAveragingType {
  OBW_AVERAGING_TYPE_RMS = 0;
  OBW_AVERAGING_TYPE_LOG = 1;
  OBW_AVERAGING_TYPE_SCALAR = 2;
  OBW_AVERAGING_TYPE_MAXIMUM = 3;
  OBW_AVERAGING_TYPE_MINIMUM = 4;
}

enum ObwRbwAutoBandwidth {
  OBW_RBW_AUTO_BANDWIDTH_FALSE = 0;
  OBW_RBW_AUTO_BANDWIDTH_TRUE = 1;
}

enum ObwRbwFilterType {
  OBW_RBW_FILTER_TYPE_FFT_BASED = 0;
  OBW_RBW_FILTER_TYPE_GAUSSIAN = 1;
  OBW_RBW_FILTER_TYPE_FLAT = 2;
}

enum ObwSweepTimeAuto {
  OBW_SWEEP_TIME_AUTO_FALSE = 0;
  OBW_SWEEP_TIME_AUTO_TRUE = 1;
}

enum QevmAveragingEnabled {
  QEVM_AVERAGING_ENABLED_FALSE = 0;
  QEVM_AVERAGING_ENABLED_TRUE = 1;
}

enum RFAttenuationAuto {
  RF_ATTENUATION_AUTO_FALSE = 0;
  RF_ATTENUATION_AUTO_TRUE = 1;
}

enum RadioConfiguration {
  RADIO_CONFIGURATION_RC1 = 0;
  RADIO_CONFIGURATION_RC2 = 1;
  RADIO_CONFIGURATION_RC3 = 2;
  RADIO_CONFIGURATION_RC4 = 3;
  RADIO_CONFIGURATION_RC5 = 4;
}

enum SemAveragingEnabled {
  SEM_AVERAGING_ENABLED_FALSE = 0;
  SEM_AVERAGING_ENABLED_TRUE = 1;
}

enum SemAveragingType {
  SEM_AVERAGING_TYPE_RMS = 0;
  SEM_AVERAGING_TYPE_LOG = 1;
  SEM_AVERAGING_TYPE_SCALAR = 2;
  SEM_AVERAGING_TYPE_MAXIMUM = 3;
  SEM_AVERAGING_TYPE_MINIMUM = 4;
}

enum SemLowerOffsetMeasurementStatus {
  SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
}

enum SemMeasurementStatus {
  SEM_MEASUREMENT_STATUS_FAIL = 0;
  SEM_MEASUREMENT_STATUS_PASS = 1;
}

enum SemSweepTimeAuto {
  SEM_SWEEP_TIME_AUTO_FALSE = 0;
  SEM_SWEEP_TIME_AUTO_TRUE = 1;
}

enum SemUpperOffsetMeasurementStatus {
  SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
}

enum SlotPhaseSynchronizationMode {
  SLOT_PHASE_SYNCHRONIZATION_MODE_FRAME = 0;
  SLOT_PHASE_SYNCHRONIZATION_MODE_SLOT = 1;
}

enum SlotPowerSynchronizationMode {
  SLOT_POWER_SYNCHRONIZATION_MODE_FRAME = 0;
  SLOT_POWER_SYNCHRONIZATION_MODE_SLOT = 1;
}

enum TriggerMinimumQuietTimeMode {
  TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL = 0;
  TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO = 1;
}

enum NiRFmxCDMA2kInt32AttributeValues {
  option allow_alias = true;
  NIRFMXCDMA2K_INT32_UNSPECIFIED = 0;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_TYPE_RMS = 0;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_TYPE_LOG = 1;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXCDMA2K_INT32_ACP_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXCDMA2K_INT32_ACP_FFT_OVERLAP_MODE_DISABLED = 0;
  NIRFMXCDMA2K_INT32_ACP_FFT_OVERLAP_MODE_AUTOMATIC = 1;
  NIRFMXCDMA2K_INT32_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_FALSE = 0;
  NIRFMXCDMA2K_INT32_ACP_IF_OUTPUT_POWER_OFFSET_AUTO_TRUE = 1;
  NIRFMXCDMA2K_INT32_ACP_MEASUREMENT_METHOD_NORMAL = 0;
  NIRFMXCDMA2K_INT32_ACP_MEASUREMENT_METHOD_DYNAMIC_RANGE = 1;
  NIRFMXCDMA2K_INT32_ACP_MEASUREMENT_METHOD_SEQUENTIAL_FFT = 2;
  NIRFMXCDMA2K_INT32_ACP_NOISE_COMPENSATION_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_ACP_NOISE_COMPENSATION_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_ACP_RBW_AUTO_BANDWIDTH_FALSE = 0;
  NIRFMXCDMA2K_INT32_ACP_RBW_AUTO_BANDWIDTH_TRUE = 1;
  NIRFMXCDMA2K_INT32_ACP_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXCDMA2K_INT32_ACP_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXCDMA2K_INT32_ACP_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXCDMA2K_INT32_ACP_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXCDMA2K_INT32_ACP_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXCDMA2K_INT32_BRANCH_I = 0;
  NIRFMXCDMA2K_INT32_BRANCH_Q = 1;
  NIRFMXCDMA2K_INT32_BRANCH_I_AND_Q = 2;
  NIRFMXCDMA2K_INT32_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_CDA_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_CDA_IQ_OFFSET_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_CDA_IQ_OFFSET_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_CDA_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_CDA_MEASUREMENT_CHANNEL_BRANCH_I = 0;
  NIRFMXCDMA2K_INT32_CDA_MEASUREMENT_CHANNEL_BRANCH_Q = 1;
  NIRFMXCDMA2K_INT32_CDA_POWER_UNIT_DB = 0;
  NIRFMXCDMA2K_INT32_CDA_POWER_UNIT_DBM = 1;
  NIRFMXCDMA2K_INT32_CDA_RECEIVE_FILTER_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_CDA_RECEIVE_FILTER_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_CDA_SPECTRUM_INVERTED_FALSE = 0;
  NIRFMXCDMA2K_INT32_CDA_SPECTRUM_INVERTED_TRUE = 1;
  NIRFMXCDMA2K_INT32_CDA_SYNCHRONIZATION_MODE_FRAME = 0;
  NIRFMXCDMA2K_INT32_CDA_SYNCHRONIZATION_MODE_SLOT = 1;
  NIRFMXCDMA2K_INT32_CDA_SYNCHRONIZATION_MODE_ARBITRARY = 2;
  NIRFMXCDMA2K_INT32_CHANNEL_CONFIGURATION_MODE_AUTO_DETECT = 0;
  NIRFMXCDMA2K_INT32_CHANNEL_CONFIGURATION_MODE_USER_DEFINED = 1;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_TYPE_RMS = 0;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_TYPE_LOG = 1;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXCDMA2K_INT32_CHP_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXCDMA2K_INT32_CHP_RBW_AUTO_BANDWIDTH_FALSE = 0;
  NIRFMXCDMA2K_INT32_CHP_RBW_AUTO_BANDWIDTH_TRUE = 1;
  NIRFMXCDMA2K_INT32_CHP_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXCDMA2K_INT32_CHP_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXCDMA2K_INT32_CHP_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXCDMA2K_INT32_CHP_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXCDMA2K_INT32_CHP_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXCDMA2K_INT32_DIGITAL_EDGE_TRIGGER_EDGE_RISING = 0;
  NIRFMXCDMA2K_INT32_DIGITAL_EDGE_TRIGGER_EDGE_FALLING = 1;
  NIRFMXCDMA2K_INT32_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_RELATIVE = 0;
  NIRFMXCDMA2K_INT32_IQ_POWER_EDGE_TRIGGER_LEVEL_TYPE_ABSOLUTE = 1;
  NIRFMXCDMA2K_INT32_IQ_POWER_EDGE_TRIGGER_SLOPE_RISING = 0;
  NIRFMXCDMA2K_INT32_IQ_POWER_EDGE_TRIGGER_SLOPE_FALLING = 1;
  NIRFMXCDMA2K_INT32_LIMITED_CONFIGURATION_CHANGE_DISABLED = 0;
  NIRFMXCDMA2K_INT32_LIMITED_CONFIGURATION_CHANGE_NO_CHANGE = 1;
  NIRFMXCDMA2K_INT32_LIMITED_CONFIGURATION_CHANGE_FREQUENCY = 2;
  NIRFMXCDMA2K_INT32_LIMITED_CONFIGURATION_CHANGE_REFERENCE_LEVEL = 3;
  NIRFMXCDMA2K_INT32_LIMITED_CONFIGURATION_CHANGE_FREQUENCY_AND_REFERENCE_LEVEL = 4;
  NIRFMXCDMA2K_INT32_LIMITED_CONFIGURATION_CHANGE_SELECTED_PORTS_FREQUENCY_AND_REFERENCE_LEVEL = 5;
  NIRFMXCDMA2K_INT32_LINK_DIRECTION_UPLINK = 1;
  NIRFMXCDMA2K_INT32_MODACC_DETECTED_BRANCH_I = 0;
  NIRFMXCDMA2K_INT32_MODACC_DETECTED_BRANCH_Q = 1;
  NIRFMXCDMA2K_INT32_MODACC_DETECTED_BRANCH_I_AND_Q = 2;
  NIRFMXCDMA2K_INT32_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_MODACC_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_MODACC_IQ_OFFSET_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_MODACC_IQ_OFFSET_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_MODACC_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_MODACC_MULTI_CARRIER_FILTER_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_MODACC_MULTI_CARRIER_FILTER_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_MODACC_PEAK_ACTIVE_CDE_BRANCH_I = 0;
  NIRFMXCDMA2K_INT32_MODACC_PEAK_ACTIVE_CDE_BRANCH_Q = 1;
  NIRFMXCDMA2K_INT32_MODACC_PEAK_ACTIVE_CDE_BRANCH_I_AND_Q = 2;
  NIRFMXCDMA2K_INT32_MODACC_PEAK_CDE_BRANCH_I = 0;
  NIRFMXCDMA2K_INT32_MODACC_PEAK_CDE_BRANCH_Q = 1;
  NIRFMXCDMA2K_INT32_MODACC_PEAK_CDE_BRANCH_I_AND_Q = 2;
  NIRFMXCDMA2K_INT32_MODACC_RECEIVE_FILTER_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_MODACC_RECEIVE_FILTER_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_MODACC_SPECTRUM_INVERTED_FALSE = 0;
  NIRFMXCDMA2K_INT32_MODACC_SPECTRUM_INVERTED_TRUE = 1;
  NIRFMXCDMA2K_INT32_MODACC_SYNCHRONIZATION_MODE_FRAME = 0;
  NIRFMXCDMA2K_INT32_MODACC_SYNCHRONIZATION_MODE_SLOT = 1;
  NIRFMXCDMA2K_INT32_MODACC_SYNCHRONIZATION_MODE_ARBITRARY = 2;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_TYPE_RMS = 0;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_TYPE_LOG = 1;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXCDMA2K_INT32_OBW_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXCDMA2K_INT32_OBW_RBW_AUTO_BANDWIDTH_FALSE = 0;
  NIRFMXCDMA2K_INT32_OBW_RBW_AUTO_BANDWIDTH_TRUE = 1;
  NIRFMXCDMA2K_INT32_OBW_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXCDMA2K_INT32_OBW_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXCDMA2K_INT32_OBW_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXCDMA2K_INT32_OBW_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXCDMA2K_INT32_OBW_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXCDMA2K_INT32_QEVM_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_QEVM_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_QEVM_IQ_GAIN_IMBALANCE_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_QEVM_IQ_OFFSET_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_QEVM_IQ_OFFSET_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_QEVM_IQ_QUADRATURE_ERROR_REMOVAL_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_QEVM_RECEIVE_FILTER_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_QEVM_RECEIVE_FILTER_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_QEVM_SPECTRUM_INVERTED_FALSE = 0;
  NIRFMXCDMA2K_INT32_QEVM_SPECTRUM_INVERTED_TRUE = 1;
  NIRFMXCDMA2K_INT32_RADIO_CONFIGURATION_RC1 = 0;
  NIRFMXCDMA2K_INT32_RADIO_CONFIGURATION_RC2 = 1;
  NIRFMXCDMA2K_INT32_RADIO_CONFIGURATION_RC3 = 2;
  NIRFMXCDMA2K_INT32_RADIO_CONFIGURATION_RC4 = 3;
  NIRFMXCDMA2K_INT32_RADIO_CONFIGURATION_RC5 = 4;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_TYPE_RMS = 0;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_TYPE_LOG = 1;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_TYPE_SCALAR = 2;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_TYPE_MAXIMUM = 3;
  NIRFMXCDMA2K_INT32_SEM_AVERAGING_TYPE_MINIMUM = 4;
  NIRFMXCDMA2K_INT32_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXCDMA2K_INT32_SEM_LOWER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXCDMA2K_INT32_SEM_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXCDMA2K_INT32_SEM_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXCDMA2K_INT32_SEM_OFFSET_RBW_FILTER_TYPE_FFT_BASED = 0;
  NIRFMXCDMA2K_INT32_SEM_OFFSET_RBW_FILTER_TYPE_GAUSSIAN = 1;
  NIRFMXCDMA2K_INT32_SEM_OFFSET_RBW_FILTER_TYPE_FLAT = 2;
  NIRFMXCDMA2K_INT32_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_4 = 3;
  NIRFMXCDMA2K_INT32_SEM_OFFSET_RBW_FILTER_TYPE_SYNCH_TUNED_5 = 4;
  NIRFMXCDMA2K_INT32_SEM_SWEEP_TIME_AUTO_FALSE = 0;
  NIRFMXCDMA2K_INT32_SEM_SWEEP_TIME_AUTO_TRUE = 1;
  NIRFMXCDMA2K_INT32_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_FAIL = 0;
  NIRFMXCDMA2K_INT32_SEM_UPPER_OFFSET_MEASUREMENT_STATUS_PASS = 1;
  NIRFMXCDMA2K_INT32_SLOT_PHASE_RECEIVE_FILTER_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_SLOT_PHASE_RECEIVE_FILTER_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_SLOT_PHASE_SPECTRUM_INVERTED_FALSE = 0;
  NIRFMXCDMA2K_INT32_SLOT_PHASE_SPECTRUM_INVERTED_TRUE = 1;
  NIRFMXCDMA2K_INT32_SLOT_PHASE_SYNCHRONIZATION_MODE_FRAME = 0;
  NIRFMXCDMA2K_INT32_SLOT_PHASE_SYNCHRONIZATION_MODE_SLOT = 1;
  NIRFMXCDMA2K_INT32_SLOT_POWER_RECEIVE_FILTER_ENABLED_FALSE = 0;
  NIRFMXCDMA2K_INT32_SLOT_POWER_RECEIVE_FILTER_ENABLED_TRUE = 1;
  NIRFMXCDMA2K_INT32_SLOT_POWER_SPECTRUM_INVERTED_FALSE = 0;
  NIRFMXCDMA2K_INT32_SLOT_POWER_SPECTRUM_INVERTED_TRUE = 1;
  NIRFMXCDMA2K_INT32_SLOT_POWER_SYNCHRONIZATION_MODE_FRAME = 0;
  NIRFMXCDMA2K_INT32_SLOT_POWER_SYNCHRONIZATION_MODE_SLOT = 1;
  NIRFMXCDMA2K_INT32_TRIGGER_MINIMUM_QUIET_TIME_MODE_MANUAL = 0;
  NIRFMXCDMA2K_INT32_TRIGGER_MINIMUM_QUIET_TIME_MODE_AUTO = 1;
  NIRFMXCDMA2K_INT32_TRIGGER_TYPE_NONE = 0;
  NIRFMXCDMA2K_INT32_TRIGGER_TYPE_DIGITAL_EDGE = 1;
  NIRFMXCDMA2K_INT32_TRIGGER_TYPE_IQ_POWER_EDGE = 2;
  NIRFMXCDMA2K_INT32_TRIGGER_TYPE_SOFTWARE = 3;
}

enum NiRFmxCDMA2kStringAttributeValuesMapped {
  NIRFMXCDMA2K_STRING_MAPPED_UNSPECIFIED = 0;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PFI0 = 1;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PFI1 = 2;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG0 = 3;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG1 = 4;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG2 = 5;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG3 = 6;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG4 = 7;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG5 = 8;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG6 = 9;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_TRIG7 = 10;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXI_STAR = 11;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PXIE_DSTARB = 12;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_TIMER_EVENT = 13;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_PULSE_IN = 14;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI0 = 15;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI1 = 16;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI2 = 17;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI3 = 18;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI4 = 19;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI5 = 20;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI6 = 21;
  NIRFMXCDMA2K_STRING_DIGITAL_EDGE_TRIGGER_SOURCE_DIO_PFI7 = 22;
}

message ACPCfgAveragingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof averaging_enabled_enum {
    AcpAveragingEnabled averaging_enabled = 3;
    int32 averaging_enabled_raw = 4;
  }
  int32 averaging_count = 5;
  oneof averaging_type_enum {
    AcpAveragingType averaging_type = 6;
    int32 averaging_type_raw = 7;
  }
}

message ACPCfgAveragingResponse {
  int32 status = 1;
}

message ACPCfgMeasurementMethodRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof measurement_method_enum {
    AcpMeasurementMethod measurement_method = 3;
    int32 measurement_method_raw = 4;
  }
}

message ACPCfgMeasurementMethodResponse {
  int32 status = 1;
}

message ACPCfgNoiseCompensationEnabledRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof noise_compensation_enabled_enum {
    AcpNoiseCompensationEnabled noise_compensation_enabled = 3;
    int32 noise_compensation_enabled_raw = 4;
  }
}

message ACPCfgNoiseCompensationEnabledResponse {
  int32 status = 1;
}

message ACPCfgNumberOfOffsetsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_offsets = 3;
}

message ACPCfgNumberOfOffsetsResponse {
  int32 status = 1;
}

message ACPCfgRBWFilterRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof rbw_auto_enum {
    AcpRbwAutoBandwidth rbw_auto = 3;
    int32 rbw_auto_raw = 4;
  }
  double rbw = 5;
  oneof rbw_filter_type_enum {
    AcpRbwFilterType rbw_filter_type = 6;
    int32 rbw_filter_type_raw = 7;
  }
}

message ACPCfgRBWFilterResponse {
  int32 status = 1;
}

message ACPCfgSweepTimeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof sweep_time_auto_enum {
    AcpSweepTimeAuto sweep_time_auto = 3;
    int32 sweep_time_auto_raw = 4;
  }
  double sweep_time_interval = 5;
}

message ACPCfgSweepTimeResponse {
  int32 status = 1;
}

message ACPFetchAbsolutePowersTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
  int32 trace_index = 4;
}

message ACPFetchAbsolutePowersTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float absolute_powers_trace = 4;
  int32 actual_array_size = 5;
}

message ACPFetchCarrierAbsolutePowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchCarrierAbsolutePowerResponse {
  int32 status = 1;
  double carrier_absolute_power = 2;
}

message ACPFetchOffsetMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchOffsetMeasurementResponse {
  int32 status = 1;
  double lower_relative_power = 2;
  double upper_relative_power = 3;
  double lower_absolute_power = 4;
  double upper_absolute_power = 5;
}

message ACPFetchOffsetMeasurementArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchOffsetMeasurementArrayResponse {
  int32 status = 1;
  repeated double lower_relative_power = 2;
  repeated double upper_relative_power = 3;
  repeated double lower_absolute_power = 4;
  repeated double upper_absolute_power = 5;
  int32 actual_array_size = 6;
}

message ACPFetchRelativePowersTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
  int32 trace_index = 4;
}

message ACPFetchRelativePowersTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float relative_powers_trace = 4;
  int32 actual_array_size = 5;
}

message ACPFetchSpectrumRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ACPFetchSpectrumResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float spectrum = 4;
  int32 actual_array_size = 5;
}

message AbortMeasurementsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message AbortMeasurementsResponse {
  int32 status = 1;
}

message AnalyzeIQ1WaveformRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  double x0 = 4;
  double dx = 5;
  repeated nidevice_grpc.NIComplexNumberF32 iq = 6;
  int32 reset = 7;
}

message AnalyzeIQ1WaveformResponse {
  int32 status = 1;
}

message AnalyzeIQ1WaveformInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  double x0 = 4;
  double dx = 5;
  repeated float iq = 6;
  int32 reset = 7;
}

message AnalyzeIQ1WaveformInterleavedIQResponse {
  int32 status = 1;
}

message AnalyzeIQ1WaveformSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  double x0 = 4;
  double dx = 5;
  repeated float iqi = 6;
  repeated float iqq = 7;
  int32 reset = 8;
}

message AnalyzeIQ1WaveformSplitResponse {
  int32 status = 1;
}

message AnalyzeSpectrum1WaveformRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
  double x0 = 4;
  double dx = 5;
  repeated float spectrum = 6;
  int32 reset = 7;
}

message AnalyzeSpectrum1WaveformResponse {
  int32 status = 1;
}

message AutoLevelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double measurement_interval = 3;
}

message AutoLevelResponse {
  int32 status = 1;
  double reference_level = 2;
}

message BuildChannelStringRequest {
  string selector_string = 1;
  int32 channel_number = 2;
}

message BuildChannelStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildOffsetStringRequest {
  string selector_string = 1;
  int32 offset_number = 2;
}

message BuildOffsetStringResponse {
  int32 status = 1;
  string selector_string_out = 2;
}

message BuildSignalStringRequest {
  string signal_name = 1;
  string result_name = 2;
}

message BuildSignalStringResponse {
  int32 status = 1;
  string selector_string = 2;
}

message CDACfgMeasurementChannelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 walsh_code_length = 3;
  int32 walsh_code_number = 4;
  oneof branch_enum {
    CdaMeasurementChannelBranch branch = 5;
    int32 branch_raw = 6;
  }
}

message CDACfgMeasurementChannelResponse {
  int32 status = 1;
}

message CDACfgPowerUnitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof power_unit_enum {
    CdaPowerUnit power_unit = 3;
    int32 power_unit_raw = 4;
  }
}

message CDACfgPowerUnitResponse {
  int32 status = 1;
}

message CDACfgSynchronizationModeAndIntervalRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof synchronization_mode_enum {
    CdaSynchronizationMode synchronization_mode = 3;
    int32 synchronization_mode_raw = 4;
  }
  int32 measurement_offset = 5;
  int32 measurement_length = 6;
}

message CDACfgSynchronizationModeAndIntervalResponse {
  int32 status = 1;
}

message CDAFetchCodeDomainIAndQPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchCodeDomainIAndQPowerResponse {
  int32 status = 1;
  double i_mean_active_power = 2;
  double q_mean_active_power = 3;
  double i_peak_inactive_power = 4;
  double q_peak_inactive_power = 5;
}

message CDAFetchCodeDomainIAndQPowerTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchCodeDomainIAndQPowerTraceResponse {
  int32 status = 1;
  repeated float i_code_domain_powers = 2;
  repeated float q_code_domain_powers = 3;
  int32 actual_array_size = 4;
}

message CDAFetchCodeDomainPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchCodeDomainPowerResponse {
  int32 status = 1;
  double total_power = 2;
  double total_active_power = 3;
  double mean_active_power = 4;
  double peak_active_power = 5;
  double mean_inactive_power = 6;
  double peak_inactive_power = 7;
}

message CDAFetchIQImpairmentsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchIQImpairmentsResponse {
  int32 status = 1;
  double iq_origin_offset = 2;
  double iq_gain_imbalance = 3;
  double iq_quadrature_error = 4;
}

message CDAFetchSymbolConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 symbol_constellation = 2;
  int32 actual_array_size = 3;
}

message CDAFetchSymbolConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float symbol_constellation = 2;
  int32 actual_array_size = 3;
}

message CDAFetchSymbolConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float symbol_constellation_i = 2;
  repeated float symbol_constellation_q = 3;
  int32 actual_array_size = 4;
}

message CDAFetchSymbolEVMRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolEVMResponse {
  int32 status = 1;
  double rms_symbol_evm = 2;
  double peak_symbol_evm = 3;
  double rms_symbol_magnitude_error = 4;
  double rms_symbol_phase_error = 5;
  double mean_symbol_power = 6;
  double frequency_error = 7;
  double chip_rate_error = 8;
}

message CDAFetchSymbolEVMTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolEVMTraceResponse {
  int32 status = 1;
  repeated float symbol_evm = 2;
  int32 actual_array_size = 3;
}

message CDAFetchSymbolMagnitudeErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolMagnitudeErrorTraceResponse {
  int32 status = 1;
  repeated float symbol_magnitude_error = 2;
  int32 actual_array_size = 3;
}

message CDAFetchSymbolPhaseErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolPhaseErrorTraceResponse {
  int32 status = 1;
  repeated float symbol_phase_error = 2;
  int32 actual_array_size = 3;
}

message CDAFetchSymbolPowerTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CDAFetchSymbolPowerTraceResponse {
  int32 status = 1;
  repeated float symbol_powers = 2;
  int32 actual_array_size = 3;
}

message CHPCfgAveragingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof averaging_enabled_enum {
    ChpAveragingEnabled averaging_enabled = 3;
    int32 averaging_enabled_raw = 4;
  }
  int32 averaging_count = 5;
  oneof averaging_type_enum {
    ChpAveragingType averaging_type = 6;
    int32 averaging_type_raw = 7;
  }
}

message CHPCfgAveragingResponse {
  int32 status = 1;
}

message CHPCfgRBWFilterRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof rbw_auto_enum {
    ChpRbwAutoBandwidth rbw_auto = 3;
    int32 rbw_auto_raw = 4;
  }
  double rbw = 5;
  oneof rbw_filter_type_enum {
    ChpRbwFilterType rbw_filter_type = 6;
    int32 rbw_filter_type_raw = 7;
  }
}

message CHPCfgRBWFilterResponse {
  int32 status = 1;
}

message CHPCfgSweepTimeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof sweep_time_auto_enum {
    ChpSweepTimeAuto sweep_time_auto = 3;
    int32 sweep_time_auto_raw = 4;
  }
  double sweep_time_interval = 5;
}

message CHPCfgSweepTimeResponse {
  int32 status = 1;
}

message CHPFetchCarrierAbsolutePowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CHPFetchCarrierAbsolutePowerResponse {
  int32 status = 1;
  double carrier_absolute_power = 2;
}

message CHPFetchSpectrumRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message CHPFetchSpectrumResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float spectrum = 4;
  int32 actual_array_size = 5;
}

message CfgBandClassRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 band_class = 3;
}

message CfgBandClassResponse {
  int32 status = 1;
}

message CfgChannelConfigurationModeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof channel_configuration_mode_enum {
    ChannelConfigurationMode channel_configuration_mode = 3;
    int32 channel_configuration_mode_raw = 4;
  }
}

message CfgChannelConfigurationModeResponse {
  int32 status = 1;
}

message CfgDigitalEdgeTriggerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof digital_edge_source_enum {
    DigitalEdgeTriggerSource digital_edge_source_mapped = 3;
    string digital_edge_source_raw = 4;
  }
  oneof digital_edge_enum {
    DigitalEdgeTriggerEdge digital_edge = 5;
    int32 digital_edge_raw = 6;
  }
  double trigger_delay = 7;
  int32 enable_trigger = 8;
}

message CfgDigitalEdgeTriggerResponse {
  int32 status = 1;
}

message CfgExternalAttenuationRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double external_attenuation = 3;
}

message CfgExternalAttenuationResponse {
  int32 status = 1;
}

message CfgFrequencyRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double center_frequency = 3;
}

message CfgFrequencyResponse {
  int32 status = 1;
}

message CfgFrequencyChannelNumberRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof link_direction_enum {
    LinkDirection link_direction = 3;
    int32 link_direction_raw = 4;
  }
  int32 band_class = 5;
  int32 channel_number = 6;
}

message CfgFrequencyChannelNumberResponse {
  int32 status = 1;
}

message CfgFrequencyReferenceRequest {
  nidevice_grpc.Session instrument = 1;
  string channel_name = 2;
  oneof frequency_reference_source_enum {
    FrequencyReferenceSource frequency_reference_source_mapped = 3;
    string frequency_reference_source_raw = 4;
  }
  double frequency_reference_frequency = 5;
}

message CfgFrequencyReferenceResponse {
  int32 status = 1;
}

message CfgIQPowerEdgeTriggerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string iq_power_edge_source = 3;
  oneof iq_power_edge_slope_enum {
    IQPowerEdgeTriggerSlope iq_power_edge_slope = 4;
    int32 iq_power_edge_slope_raw = 5;
  }
  double iq_power_edge_level = 6;
  double trigger_delay = 7;
  oneof minimum_quiet_time_mode_enum {
    TriggerMinimumQuietTimeMode minimum_quiet_time_mode = 8;
    int32 minimum_quiet_time_mode_raw = 9;
  }
  double minimum_quiet_time = 10;
  oneof iq_power_edge_level_type_enum {
    IQPowerEdgeTriggerLevelType iq_power_edge_level_type = 11;
    int32 iq_power_edge_level_type_raw = 12;
  }
  int32 enable_trigger = 13;
}

message CfgIQPowerEdgeTriggerResponse {
  int32 status = 1;
}

message CfgMechanicalAttenuationRequest {
  nidevice_grpc.Session instrument = 1;
  string channel_name = 2;
  oneof mechanical_attenuation_auto_enum {
    MechanicalAttenuationAuto mechanical_attenuation_auto = 3;
    int32 mechanical_attenuation_auto_raw = 4;
  }
  double mechanical_attenuation_value = 5;
}

message CfgMechanicalAttenuationResponse {
  int32 status = 1;
}

message CfgNumberOfChannelsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 number_of_channels = 3;
}

message CfgNumberOfChannelsResponse {
  int32 status = 1;
}

message CfgRFRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double center_frequency = 3;
  double reference_level = 4;
  double external_attenuation = 5;
}

message CfgRFResponse {
  int32 status = 1;
}

message CfgRFAttenuationRequest {
  nidevice_grpc.Session instrument = 1;
  string channel_name = 2;
  oneof rf_attenuation_auto_enum {
    RFAttenuationAuto rf_attenuation_auto = 3;
    int32 rf_attenuation_auto_raw = 4;
  }
  double rf_attenuation_value = 5;
}

message CfgRFAttenuationResponse {
  int32 status = 1;
}

message CfgRadioConfigurationRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof radio_configuration_enum {
    RadioConfiguration radio_configuration = 3;
    int32 radio_configuration_raw = 4;
  }
}

message CfgRadioConfigurationResponse {
  int32 status = 1;
}

message CfgReferenceLevelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double reference_level = 3;
}

message CfgReferenceLevelResponse {
  int32 status = 1;
}

message CfgSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double trigger_delay = 3;
  int32 enable_trigger = 4;
}

message CfgSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message CfgUplinkSpreadingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int64 uplink_spreading_long_code_mask = 3;
}

message CfgUplinkSpreadingResponse {
  int32 status = 1;
}

message CfgUserDefinedChannelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 walsh_code_length = 3;
  int32 walsh_code_number = 4;
  oneof branch_enum {
    Branch branch = 5;
    int32 branch_raw = 6;
  }
}

message CfgUserDefinedChannelResponse {
  int32 status = 1;
}

message CfgUserDefinedChannelArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated int32 walsh_code_length = 3;
  repeated int32 walsh_code_number = 4;
  repeated Branch branch = 5;
}

message CfgUserDefinedChannelArrayResponse {
  int32 status = 1;
}

message CheckMeasurementStatusRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message CheckMeasurementStatusResponse {
  int32 status = 1;
  int32 done = 2;
}

message ClearAllNamedResultsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message ClearAllNamedResultsResponse {
  int32 status = 1;
}

message ClearNamedResultRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message ClearNamedResultResponse {
  int32 status = 1;
}

message CloneSignalConfigurationRequest {
  nidevice_grpc.Session instrument = 1;
  string old_signal_name = 2;
  string new_signal_name = 3;
}

message CloneSignalConfigurationResponse {
  int32 status = 1;
}

message CloseRequest {
  nidevice_grpc.Session instrument = 1;
  bool force_destroy = 2;
}

message CloseResponse {
  int32 status = 1;
}

message CommitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message CommitResponse {
  int32 status = 1;
}

message CreateSignalConfigurationRequest {
  nidevice_grpc.Session instrument = 1;
  string signal_name = 2;
}

message CreateSignalConfigurationResponse {
  int32 status = 1;
}

message DeleteSignalConfigurationRequest {
  nidevice_grpc.Session instrument = 1;
  string signal_name = 2;
}

message DeleteSignalConfigurationResponse {
  int32 status = 1;
}

message DisableTriggerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message DisableTriggerResponse {
  int32 status = 1;
}

message GetAllNamedResultNamesRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message GetAllNamedResultNamesResponse {
  int32 status = 1;
  string result_names = 2;
  int32 actual_result_names_size = 3;
  int32 default_result_exists = 4;
}

message GetAttributeF32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeF32Response {
  int32 status = 1;
  float attr_val = 2;
}

message GetAttributeF32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeF32ArrayResponse {
  int32 status = 1;
  repeated float attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeF64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeF64Response {
  int32 status = 1;
  double attr_val = 2;
}

message GetAttributeF64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeF64ArrayResponse {
  int32 status = 1;
  repeated double attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeI16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI16Response {
  int32 status = 1;
  int32 attr_val = 2;
}

message GetAttributeI32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI32Response {
  int32 status = 1;
  NiRFmxCDMA2kInt32AttributeValues attr_val = 2;
  int32 attr_val_raw = 3;
}

message GetAttributeI32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI32ArrayResponse {
  int32 status = 1;
  repeated NiRFmxCDMA2kInt32AttributeValues attr_val = 2;
  repeated int32 attr_val_raw = 3;
  int32 actual_array_size = 4;
}

message GetAttributeI64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI64Response {
  int32 status = 1;
  int64 attr_val = 2;
}

message GetAttributeI64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI64ArrayResponse {
  int32 status = 1;
  repeated int64 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeI8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI8Response {
  int32 status = 1;
  int32 attr_val = 2;
}

message GetAttributeI8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeI8ArrayResponse {
  int32 status = 1;
  repeated int32 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeNIComplexDoubleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeNIComplexDoubleArrayResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumber attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeNIComplexSingleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeNIComplexSingleArrayResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeStringRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeStringResponse {
  int32 status = 1;
  string attr_val = 2;
}

message GetAttributeU16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeU16Response {
  int32 status = 1;
  uint32 attr_val = 2;
}

message GetAttributeU32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeU32Response {
  int32 status = 1;
  uint32 attr_val = 2;
}

message GetAttributeU32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeU32ArrayResponse {
  int32 status = 1;
  repeated uint32 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeU64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeU64ArrayResponse {
  int32 status = 1;
  repeated uint64 attr_val = 2;
  int32 actual_array_size = 3;
}

message GetAttributeU8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeU8Response {
  int32 status = 1;
  uint32 attr_val = 2;
}

message GetAttributeU8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message GetAttributeU8ArrayResponse {
  int32 status = 1;
  bytes attr_val = 2;
  int32 actual_array_size = 3;
}

message GetErrorRequest {
  nidevice_grpc.Session instrument = 1;
}

message GetErrorResponse {
  int32 status = 1;
  int32 error_code = 2;
  string error_description = 3;
}

message GetErrorStringRequest {
  nidevice_grpc.Session instrument = 1;
  int32 error_code = 2;
}

message GetErrorStringResponse {
  int32 status = 1;
  string error_description = 2;
}

message InitializeRequest {
  string session_name = 1;
  string resource_name = 2;
  string option_string = 3;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 4;
}

message InitializeResponse {
  int32 status = 1;
  nidevice_grpc.Session instrument = 2;
  int32 is_new_session = 3;
  string error_message = 4 [deprecated = true];
  bool new_session_initialized = 5;
}

message InitializeFromNIRFSASessionRequest {
  string session_name = 1;
  nidevice_grpc.Session nirfsa_session = 2;
  nidevice_grpc.SessionInitializationBehavior initialization_behavior = 3;
}

message InitializeFromNIRFSASessionResponse {
  int32 status = 1;
  nidevice_grpc.Session instrument = 2;
  string error_message = 3 [deprecated = true];
  bool new_session_initialized = 4;
}

message InitiateRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  string result_name = 3;
}

message InitiateResponse {
  int32 status = 1;
}

message ModAccCfgSynchronizationModeAndIntervalRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof synchronization_mode_enum {
    ModAccSynchronizationMode synchronization_mode = 3;
    int32 synchronization_mode_raw = 4;
  }
  int32 measurement_offset = 5;
  int32 measurement_length = 6;
}

message ModAccCfgSynchronizationModeAndIntervalResponse {
  int32 status = 1;
}

message ModAccFetchConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float constellation = 2;
  int32 actual_array_size = 3;
}

message ModAccFetchConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float constellation_i = 2;
  repeated float constellation_q = 3;
  int32 actual_array_size = 4;
}

message ModAccFetchDetectedChannelRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchDetectedChannelResponse {
  int32 status = 1;
  int32 detected_walsh_code_length = 2;
  int32 detected_walsh_code_number = 3;
  ModAccDetectedBranch detected_branch = 4;
  int32 detected_branch_raw = 5;
}

message ModAccFetchDetectedChannelArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchDetectedChannelArrayResponse {
  int32 status = 1;
  repeated int32 detected_walsh_code_length = 2;
  repeated int32 detected_walsh_code_number = 3;
  repeated ModAccDetectedBranch detected_branch = 4;
  repeated int32 detected_branch_raw = 5;
  int32 actual_array_size = 6;
}

message ModAccFetchEVMRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchEVMResponse {
  int32 status = 1;
  double rms_evm = 2;
  double peak_evm = 3;
  double rho = 4;
  double frequency_error = 5;
  double chip_rate_error = 6;
  double rms_magnitude_error = 7;
  double rms_phase_error = 8;
}

message ModAccFetchEVMTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchEVMTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float evm = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchIQImpairmentsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchIQImpairmentsResponse {
  int32 status = 1;
  double iq_origin_offset = 2;
  double iq_gain_imbalance = 3;
  double iq_quadrature_error = 4;
}

message ModAccFetchMagnitudeErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchMagnitudeErrorTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float magnitude_error = 4;
  int32 actual_array_size = 5;
}

message ModAccFetchNumberOfDetectedChannelsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchNumberOfDetectedChannelsResponse {
  int32 status = 1;
  int32 number_of_detected_channels = 2;
}

message ModAccFetchPeakActiveCDERequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakActiveCDEResponse {
  int32 status = 1;
  double peak_active_cde = 2;
  int32 peak_active_cde_walsh_code_length = 3;
  int32 peak_active_cde_walsh_code_number = 4;
  ModAccPeakActiveCdeBranch peak_active_cde_branch = 5;
  int32 peak_active_cde_branch_raw = 6;
}

message ModAccFetchPeakCDERequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPeakCDEResponse {
  int32 status = 1;
  double peak_cde = 2;
  int32 peak_cde_walsh_code_number = 3;
  ModAccPeakCdeBranch peak_cde_branch = 4;
  int32 peak_cde_branch_raw = 5;
}

message ModAccFetchPhaseErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message ModAccFetchPhaseErrorTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float phase_error = 4;
  int32 actual_array_size = 5;
}

message OBWCfgAveragingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof averaging_enabled_enum {
    ObwAveragingEnabled averaging_enabled = 3;
    int32 averaging_enabled_raw = 4;
  }
  int32 averaging_count = 5;
  oneof averaging_type_enum {
    ObwAveragingType averaging_type = 6;
    int32 averaging_type_raw = 7;
  }
}

message OBWCfgAveragingResponse {
  int32 status = 1;
}

message OBWCfgRBWFilterRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof rbw_auto_enum {
    ObwRbwAutoBandwidth rbw_auto = 3;
    int32 rbw_auto_raw = 4;
  }
  double rbw = 5;
  oneof rbw_filter_type_enum {
    ObwRbwFilterType rbw_filter_type = 6;
    int32 rbw_filter_type_raw = 7;
  }
}

message OBWCfgRBWFilterResponse {
  int32 status = 1;
}

message OBWCfgSweepTimeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof sweep_time_auto_enum {
    ObwSweepTimeAuto sweep_time_auto = 3;
    int32 sweep_time_auto_raw = 4;
  }
  double sweep_time_interval = 5;
}

message OBWCfgSweepTimeResponse {
  int32 status = 1;
}

message OBWFetchMeasurementRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message OBWFetchMeasurementResponse {
  int32 status = 1;
  double occupied_bandwidth = 2;
  double absolute_power = 3;
  double start_frequency = 4;
  double stop_frequency = 5;
}

message OBWFetchSpectrumRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message OBWFetchSpectrumResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float spectrum = 4;
  int32 actual_array_size = 5;
}

message QEVMCfgAveragingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof averaging_enabled_enum {
    QevmAveragingEnabled averaging_enabled = 3;
    int32 averaging_enabled_raw = 4;
  }
  int32 averaging_count = 5;
}

message QEVMCfgAveragingResponse {
  int32 status = 1;
}

message QEVMCfgMeasurementLengthRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  int32 measurement_length = 3;
}

message QEVMCfgMeasurementLengthResponse {
  int32 status = 1;
}

message QEVMFetchConstellationTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchConstellationTraceResponse {
  int32 status = 1;
  repeated nidevice_grpc.NIComplexNumberF32 constellation = 2;
  int32 actual_array_size = 3;
}

message QEVMFetchConstellationTraceInterleavedIQRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchConstellationTraceInterleavedIQResponse {
  int32 status = 1;
  repeated float constellation = 2;
  int32 actual_array_size = 3;
}

message QEVMFetchConstellationTraceSplitRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchConstellationTraceSplitResponse {
  int32 status = 1;
  repeated float constellation_i = 2;
  repeated float constellation_q = 3;
  int32 actual_array_size = 4;
}

message QEVMFetchEVMRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchEVMResponse {
  int32 status = 1;
  double mean_rms_evm = 2;
  double maximum_peak_evm = 3;
  double mean_frequency_error = 4;
  double mean_magnitude_error = 5;
  double mean_phase_error = 6;
  double mean_chip_rate_error = 7;
}

message QEVMFetchEVMTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchEVMTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float evm = 4;
  int32 actual_array_size = 5;
}

message QEVMFetchIQImpairmentsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchIQImpairmentsResponse {
  int32 status = 1;
  double mean_iq_origin_offset = 2;
  double mean_iq_gain_imbalance = 3;
  double mean_iq_quadrature_error = 4;
  double maximum_iq_origin_offset = 5;
  double maximum_iq_gain_imbalance = 6;
  double maximum_iq_quadrature_error = 7;
}

message QEVMFetchMagnitudeErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchMagnitudeErrorTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float magnitude_error = 4;
  int32 actual_array_size = 5;
}

message QEVMFetchPhaseErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message QEVMFetchPhaseErrorTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float phase_error = 4;
  int32 actual_array_size = 5;
}

message ResetAttributeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
}

message ResetAttributeResponse {
  int32 status = 1;
}

message ResetToDefaultRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
}

message ResetToDefaultResponse {
  int32 status = 1;
}

message SEMCfgAveragingRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof averaging_enabled_enum {
    SemAveragingEnabled averaging_enabled = 3;
    int32 averaging_enabled_raw = 4;
  }
  int32 averaging_count = 5;
  oneof averaging_type_enum {
    SemAveragingType averaging_type = 6;
    int32 averaging_type_raw = 7;
  }
}

message SEMCfgAveragingResponse {
  int32 status = 1;
}

message SEMCfgSweepTimeRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof sweep_time_auto_enum {
    SemSweepTimeAuto sweep_time_auto = 3;
    int32 sweep_time_auto_raw = 4;
  }
  double sweep_time_interval = 5;
}

message SEMCfgSweepTimeResponse {
  int32 status = 1;
}

message SEMFetchCarrierAbsoluteIntegratedPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchCarrierAbsoluteIntegratedPowerResponse {
  int32 status = 1;
  double carrier_absolute_integrated_power = 2;
}

message SEMFetchLowerOffsetMarginRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchLowerOffsetMarginResponse {
  int32 status = 1;
  SemLowerOffsetMeasurementStatus measurement_status = 2;
  int32 measurement_status_raw = 3;
  double margin = 4;
  double margin_frequency = 5;
  double margin_absolute_power = 6;
  double margin_relative_power = 7;
}

message SEMFetchLowerOffsetMarginArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchLowerOffsetMarginArrayResponse {
  int32 status = 1;
  repeated SemLowerOffsetMeasurementStatus measurement_status = 2;
  repeated int32 measurement_status_raw = 3;
  repeated double margin = 4;
  repeated double margin_frequency = 5;
  repeated double margin_absolute_power = 6;
  repeated double margin_relative_power = 7;
  int32 actual_array_size = 8;
}

message SEMFetchLowerOffsetPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchLowerOffsetPowerResponse {
  int32 status = 1;
  double absolute_integrated_power = 2;
  double relative_integrated_power = 3;
  double absolute_peak_power = 4;
  double peak_frequency = 5;
  double relative_peak_power = 6;
}

message SEMFetchLowerOffsetPowerArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchLowerOffsetPowerArrayResponse {
  int32 status = 1;
  repeated double absolute_integrated_power = 2;
  repeated double relative_integrated_power = 3;
  repeated double absolute_peak_power = 4;
  repeated double peak_frequency = 5;
  repeated double relative_peak_power = 6;
  int32 actual_array_size = 7;
}

message SEMFetchMeasurementStatusRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchMeasurementStatusResponse {
  int32 status = 1;
  SemMeasurementStatus measurement_status = 2;
  int32 measurement_status_raw = 3;
}

message SEMFetchSpectrumRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchSpectrumResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float spectrum = 4;
  repeated float relative_mask = 5;
  repeated float absolute_mask = 6;
  int32 actual_array_size = 7;
}

message SEMFetchUpperOffsetMarginRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchUpperOffsetMarginResponse {
  int32 status = 1;
  SemUpperOffsetMeasurementStatus measurement_status = 2;
  int32 measurement_status_raw = 3;
  double margin = 4;
  double margin_frequency = 5;
  double margin_absolute_power = 6;
  double margin_relative_power = 7;
}

message SEMFetchUpperOffsetMarginArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchUpperOffsetMarginArrayResponse {
  int32 status = 1;
  repeated SemUpperOffsetMeasurementStatus measurement_status = 2;
  repeated int32 measurement_status_raw = 3;
  repeated double margin = 4;
  repeated double margin_frequency = 5;
  repeated double margin_absolute_power = 6;
  repeated double margin_relative_power = 7;
  int32 actual_array_size = 8;
}

message SEMFetchUpperOffsetPowerRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchUpperOffsetPowerResponse {
  int32 status = 1;
  double absolute_integrated_power = 2;
  double relative_integrated_power = 3;
  double absolute_peak_power = 4;
  double peak_frequency = 5;
  double relative_peak_power = 6;
}

message SEMFetchUpperOffsetPowerArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SEMFetchUpperOffsetPowerArrayResponse {
  int32 status = 1;
  repeated double absolute_integrated_power = 2;
  repeated double relative_integrated_power = 3;
  repeated double absolute_peak_power = 4;
  repeated double peak_frequency = 5;
  repeated double relative_peak_power = 6;
  int32 actual_array_size = 7;
}

message SelectMeasurementsRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  repeated MeasurementTypes measurements_array = 3;
  uint32 measurements_raw = 4;
  bool enable_all_traces = 5;
}

message SelectMeasurementsResponse {
  int32 status = 1;
}

message SendSoftwareEdgeTriggerRequest {
  nidevice_grpc.Session instrument = 1;
}

message SendSoftwareEdgeTriggerResponse {
  int32 status = 1;
}

message SetAttributeF32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  float attr_val = 4;
}

message SetAttributeF32Response {
  int32 status = 1;
}

message SetAttributeF32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated float attr_val = 4;
}

message SetAttributeF32ArrayResponse {
  int32 status = 1;
}

message SetAttributeF64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  double attr_val = 4;
}

message SetAttributeF64Response {
  int32 status = 1;
}

message SetAttributeF64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated double attr_val = 4;
}

message SetAttributeF64ArrayResponse {
  int32 status = 1;
}

message SetAttributeI16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  int32 attr_val = 4;
}

message SetAttributeI16Response {
  int32 status = 1;
}

message SetAttributeI32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  oneof attr_val_enum {
    NiRFmxCDMA2kInt32AttributeValues attr_val = 4;
    int32 attr_val_raw = 5;
  }
}

message SetAttributeI32Response {
  int32 status = 1;
}

message SetAttributeI32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated NiRFmxCDMA2kInt32AttributeValues attr_val = 4;
}

message SetAttributeI32ArrayResponse {
  int32 status = 1;
}

message SetAttributeI64Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  int64 attr_val = 4;
}

message SetAttributeI64Response {
  int32 status = 1;
}

message SetAttributeI64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated int64 attr_val = 4;
}

message SetAttributeI64ArrayResponse {
  int32 status = 1;
}

message SetAttributeI8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  int32 attr_val = 4;
}

message SetAttributeI8Response {
  int32 status = 1;
}

message SetAttributeI8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated int32 attr_val = 4;
}

message SetAttributeI8ArrayResponse {
  int32 status = 1;
}

message SetAttributeNIComplexDoubleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated nidevice_grpc.NIComplexNumber attr_val = 4;
}

message SetAttributeNIComplexDoubleArrayResponse {
  int32 status = 1;
}

message SetAttributeNIComplexSingleArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated nidevice_grpc.NIComplexNumberF32 attr_val = 4;
}

message SetAttributeNIComplexSingleArrayResponse {
  int32 status = 1;
}

message SetAttributeStringRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  oneof attr_val_enum {
    NiRFmxCDMA2kStringAttributeValuesMapped attr_val_mapped = 4;
    string attr_val_raw = 5;
  }
}

message SetAttributeStringResponse {
  int32 status = 1;
}

message SetAttributeU16Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  uint32 attr_val = 4;
}

message SetAttributeU16Response {
  int32 status = 1;
}

message SetAttributeU32Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  uint32 attr_val = 4;
}

message SetAttributeU32Response {
  int32 status = 1;
}

message SetAttributeU32ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated uint32 attr_val = 4;
}

message SetAttributeU32ArrayResponse {
  int32 status = 1;
}

message SetAttributeU64ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  repeated uint64 attr_val = 4;
}

message SetAttributeU64ArrayResponse {
  int32 status = 1;
}

message SetAttributeU8Request {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  uint32 attr_val = 4;
}

message SetAttributeU8Response {
  int32 status = 1;
}

message SetAttributeU8ArrayRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  NiRFmxCDMA2kAttribute attribute_id = 3;
  bytes attr_val = 4;
}

message SetAttributeU8ArrayResponse {
  int32 status = 1;
}

message SlotPhaseCfgSynchronizationModeAndIntervalRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof synchronization_mode_enum {
    SlotPhaseSynchronizationMode synchronization_mode = 3;
    int32 synchronization_mode_raw = 4;
  }
  int32 measurement_offset = 5;
  int32 measurement_length = 6;
}

message SlotPhaseCfgSynchronizationModeAndIntervalResponse {
  int32 status = 1;
}

message SlotPhaseFetchChipPhaseErrorLinearFitTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SlotPhaseFetchChipPhaseErrorLinearFitTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float chip_phase_error_linear_fit = 4;
  int32 actual_array_size = 5;
}

message SlotPhaseFetchChipPhaseErrorTraceRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SlotPhaseFetchChipPhaseErrorTraceResponse {
  int32 status = 1;
  double x0 = 2;
  double dx = 3;
  repeated float chip_phase_error = 4;
  int32 actual_array_size = 5;
}

message SlotPhaseFetchMaximumPhaseDiscontinuityRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SlotPhaseFetchMaximumPhaseDiscontinuityResponse {
  int32 status = 1;
  double maximum_phase_discontinuity = 2;
}

message SlotPhaseFetchPhaseDiscontinuitiesRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SlotPhaseFetchPhaseDiscontinuitiesResponse {
  int32 status = 1;
  repeated double slot_phase_discontinuity = 2;
  int32 actual_array_size = 3;
}

message SlotPowerCfgSynchronizationModeAndIntervalRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  oneof synchronization_mode_enum {
    SlotPowerSynchronizationMode synchronization_mode = 3;
    int32 synchronization_mode_raw = 4;
  }
  int32 measurement_offset = 5;
  int32 measurement_length = 6;
}

message SlotPowerCfgSynchronizationModeAndIntervalResponse {
  int32 status = 1;
}

message SlotPowerFetchPowersRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message SlotPowerFetchPowersResponse {
  int32 status = 1;
  repeated double slot_power = 2;
  repeated double slot_power_delta = 3;
  int32 actual_array_size = 4;
}

message WaitForAcquisitionCompleteRequest {
  nidevice_grpc.Session instrument = 1;
  double timeout = 2;
}

message WaitForAcquisitionCompleteResponse {
  int32 status = 1;
}

message WaitForMeasurementCompleteRequest {
  nidevice_grpc.Session instrument = 1;
  string selector_string = 2;
  double timeout = 3;
}

message WaitForMeasurementCompleteResponse {
  int32 status = 1;
}
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_client.cpp sha256=089fb6ded4c89b597bb7fae1149de3273d4c8615a40a405924bd7818e62eb2a9 bytes=124570 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_client.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_client.cpp`
- sha256: `089fb6ded4c89b597bb7fae1149de3273d4c8615a40a405924bd7818e62eb2a9`
- bytes: 124570

````cpp

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for NI-rfmxcdma2k.
//---------------------------------------------------------------------
#include "nirfmxcdma2k_client.h"

#include <grpcpp/grpcpp.h>

#include <nirfmxcdma2k.grpc.pb.h>

#include <cstdint>
#include <memory>
#include <stdexcept>
#include <vector>

namespace nirfmxcdma2k_grpc::experimental::client {

ACPCfgAveragingResponse
acp_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<AcpAveragingType, pb::int32>& averaging_type)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgAveragingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto averaging_enabled_ptr = averaging_enabled.get_if<AcpAveragingEnabled>();
  const auto averaging_enabled_raw_ptr = averaging_enabled.get_if<pb::int32>();
  if (averaging_enabled_ptr) {
    request.set_averaging_enabled(*averaging_enabled_ptr);
  }
  else if (averaging_enabled_raw_ptr) {
    request.set_averaging_enabled_raw(*averaging_enabled_raw_ptr);
  }
  request.set_averaging_count(averaging_count);
  const auto averaging_type_ptr = averaging_type.get_if<AcpAveragingType>();
  const auto averaging_type_raw_ptr = averaging_type.get_if<pb::int32>();
  if (averaging_type_ptr) {
    request.set_averaging_type(*averaging_type_ptr);
  }
  else if (averaging_type_raw_ptr) {
    request.set_averaging_type_raw(*averaging_type_raw_ptr);
  }

  auto response = ACPCfgAveragingResponse{};

  raise_if_error(
      stub->ACPCfgAveraging(&context, request, &response),
      context);

  return response;
}

ACPCfgMeasurementMethodResponse
acp_cfg_measurement_method(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpMeasurementMethod, pb::int32>& measurement_method)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgMeasurementMethodRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto measurement_method_ptr = measurement_method.get_if<AcpMeasurementMethod>();
  const auto measurement_method_raw_ptr = measurement_method.get_if<pb::int32>();
  if (measurement_method_ptr) {
    request.set_measurement_method(*measurement_method_ptr);
  }
  else if (measurement_method_raw_ptr) {
    request.set_measurement_method_raw(*measurement_method_raw_ptr);
  }

  auto response = ACPCfgMeasurementMethodResponse{};

  raise_if_error(
      stub->ACPCfgMeasurementMethod(&context, request, &response),
      context);

  return response;
}

ACPCfgNoiseCompensationEnabledResponse
acp_cfg_noise_compensation_enabled(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpNoiseCompensationEnabled, pb::int32>& noise_compensation_enabled)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgNoiseCompensationEnabledRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto noise_compensation_enabled_ptr = noise_compensation_enabled.get_if<AcpNoiseCompensationEnabled>();
  const auto noise_compensation_enabled_raw_ptr = noise_compensation_enabled.get_if<pb::int32>();
  if (noise_compensation_enabled_ptr) {
    request.set_noise_compensation_enabled(*noise_compensation_enabled_ptr);
  }
  else if (noise_compensation_enabled_raw_ptr) {
    request.set_noise_compensation_enabled_raw(*noise_compensation_enabled_raw_ptr);
  }

  auto response = ACPCfgNoiseCompensationEnabledResponse{};

  raise_if_error(
      stub->ACPCfgNoiseCompensationEnabled(&context, request, &response),
      context);

  return response;
}

ACPCfgNumberOfOffsetsResponse
acp_cfg_number_of_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_offsets)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgNumberOfOffsetsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_offsets(number_of_offsets);

  auto response = ACPCfgNumberOfOffsetsResponse{};

  raise_if_error(
      stub->ACPCfgNumberOfOffsets(&context, request, &response),
      context);

  return response;
}

ACPCfgRBWFilterResponse
acp_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<AcpRbwFilterType, pb::int32>& rbw_filter_type)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgRBWFilterRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto rbw_auto_ptr = rbw_auto.get_if<AcpRbwAutoBandwidth>();
  const auto rbw_auto_raw_ptr = rbw_auto.get_if<pb::int32>();
  if (rbw_auto_ptr) {
    request.set_rbw_auto(*rbw_auto_ptr);
  }
  else if (rbw_auto_raw_ptr) {
    request.set_rbw_auto_raw(*rbw_auto_raw_ptr);
  }
  request.set_rbw(rbw);
  const auto rbw_filter_type_ptr = rbw_filter_type.get_if<AcpRbwFilterType>();
  const auto rbw_filter_type_raw_ptr = rbw_filter_type.get_if<pb::int32>();
  if (rbw_filter_type_ptr) {
    request.set_rbw_filter_type(*rbw_filter_type_ptr);
  }
  else if (rbw_filter_type_raw_ptr) {
    request.set_rbw_filter_type_raw(*rbw_filter_type_raw_ptr);
  }

  auto response = ACPCfgRBWFilterResponse{};

  raise_if_error(
      stub->ACPCfgRBWFilter(&context, request, &response),
      context);

  return response;
}

ACPCfgSweepTimeResponse
acp_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval)
{
  ::grpc::ClientContext context;

  auto request = ACPCfgSweepTimeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto sweep_time_auto_ptr = sweep_time_auto.get_if<AcpSweepTimeAuto>();
  const auto sweep_time_auto_raw_ptr = sweep_time_auto.get_if<pb::int32>();
  if (sweep_time_auto_ptr) {
    request.set_sweep_time_auto(*sweep_time_auto_ptr);
  }
  else if (sweep_time_auto_raw_ptr) {
    request.set_sweep_time_auto_raw(*sweep_time_auto_raw_ptr);
  }
  request.set_sweep_time_interval(sweep_time_interval);

  auto response = ACPCfgSweepTimeResponse{};

  raise_if_error(
      stub->ACPCfgSweepTime(&context, request, &response),
      context);

  return response;
}

ACPFetchAbsolutePowersTraceResponse
acp_fetch_absolute_powers_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout, const pb::int32& trace_index)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchAbsolutePowersTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);
  request.set_trace_index(trace_index);

  auto response = ACPFetchAbsolutePowersTraceResponse{};

  raise_if_error(
      stub->ACPFetchAbsolutePowersTrace(&context, request, &response),
      context);

  return response;
}

ACPFetchCarrierAbsolutePowerResponse
acp_fetch_carrier_absolute_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchCarrierAbsolutePowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchCarrierAbsolutePowerResponse{};

  raise_if_error(
      stub->ACPFetchCarrierAbsolutePower(&context, request, &response),
      context);

  return response;
}

ACPFetchOffsetMeasurementResponse
acp_fetch_offset_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchOffsetMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchOffsetMeasurementResponse{};

  raise_if_error(
      stub->ACPFetchOffsetMeasurement(&context, request, &response),
      context);

  return response;
}

ACPFetchOffsetMeasurementArrayResponse
acp_fetch_offset_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchOffsetMeasurementArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchOffsetMeasurementArrayResponse{};

  raise_if_error(
      stub->ACPFetchOffsetMeasurementArray(&context, request, &response),
      context);

  return response;
}

ACPFetchRelativePowersTraceResponse
acp_fetch_relative_powers_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout, const pb::int32& trace_index)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchRelativePowersTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);
  request.set_trace_index(trace_index);

  auto response = ACPFetchRelativePowersTraceResponse{};

  raise_if_error(
      stub->ACPFetchRelativePowersTrace(&context, request, &response),
      context);

  return response;
}

ACPFetchSpectrumResponse
acp_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ACPFetchSpectrumRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ACPFetchSpectrumResponse{};

  raise_if_error(
      stub->ACPFetchSpectrum(&context, request, &response),
      context);

  return response;
}

AbortMeasurementsResponse
abort_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = AbortMeasurementsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = AbortMeasurementsResponse{};

  raise_if_error(
      stub->AbortMeasurements(&context, request, &response),
      context);

  return response;
}

AnalyzeIQ1WaveformResponse
analyze_iq1_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& iq, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeIQ1WaveformRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(iq, request.mutable_iq());
  request.set_reset(reset);

  auto response = AnalyzeIQ1WaveformResponse{};

  raise_if_error(
      stub->AnalyzeIQ1Waveform(&context, request, &response),
      context);

  return response;
}

AnalyzeIQ1WaveformInterleavedIQResponse
analyze_iq1_waveform_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& iq, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeIQ1WaveformInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(iq, request.mutable_iq());
  request.set_reset(reset);

  auto response = AnalyzeIQ1WaveformInterleavedIQResponse{};

  raise_if_error(
      stub->AnalyzeIQ1WaveformInterleavedIQ(&context, request, &response),
      context);

  return response;
}

AnalyzeIQ1WaveformSplitResponse
analyze_iq1_waveform_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& iqi, const std::vector<float>& iqq, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeIQ1WaveformSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(iqi, request.mutable_iqi());
  copy_array(iqq, request.mutable_iqq());
  request.set_reset(reset);

  auto response = AnalyzeIQ1WaveformSplitResponse{};

  raise_if_error(
      stub->AnalyzeIQ1WaveformSplit(&context, request, &response),
      context);

  return response;
}

AnalyzeSpectrum1WaveformResponse
analyze_spectrum1_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& spectrum, const pb::int32& reset)
{
  ::grpc::ClientContext context;

  auto request = AnalyzeSpectrum1WaveformRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);
  request.set_x0(x0);
  request.set_dx(dx);
  copy_array(spectrum, request.mutable_spectrum());
  request.set_reset(reset);

  auto response = AnalyzeSpectrum1WaveformResponse{};

  raise_if_error(
      stub->AnalyzeSpectrum1Waveform(&context, request, &response),
      context);

  return response;
}

AutoLevelResponse
auto_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& measurement_interval)
{
  ::grpc::ClientContext context;

  auto request = AutoLevelRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_measurement_interval(measurement_interval);

  auto response = AutoLevelResponse{};

  raise_if_error(
      stub->AutoLevel(&context, request, &response),
      context);

  return response;
}

BuildChannelStringResponse
build_channel_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& channel_number)
{
  ::grpc::ClientContext context;

  auto request = BuildChannelStringRequest{};
  request.set_selector_string(selector_string);
  request.set_channel_number(channel_number);

  auto response = BuildChannelStringResponse{};

  raise_if_error(
      stub->BuildChannelString(&context, request, &response),
      context);

  return response;
}

BuildOffsetStringResponse
build_offset_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& offset_number)
{
  ::grpc::ClientContext context;

  auto request = BuildOffsetStringRequest{};
  request.set_selector_string(selector_string);
  request.set_offset_number(offset_number);

  auto response = BuildOffsetStringResponse{};

  raise_if_error(
      stub->BuildOffsetString(&context, request, &response),
      context);

  return response;
}

BuildSignalStringResponse
build_signal_string(const StubPtr& stub, const std::string& signal_name, const std::string& result_name)
{
  ::grpc::ClientContext context;

  auto request = BuildSignalStringRequest{};
  request.set_signal_name(signal_name);
  request.set_result_name(result_name);

  auto response = BuildSignalStringResponse{};

  raise_if_error(
      stub->BuildSignalString(&context, request, &response),
      context);

  return response;
}

CDACfgMeasurementChannelResponse
cda_cfg_measurement_channel(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& walsh_code_length, const pb::int32& walsh_code_number, const simple_variant<CdaMeasurementChannelBranch, pb::int32>& branch)
{
  ::grpc::ClientContext context;

  auto request = CDACfgMeasurementChannelRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_walsh_code_length(walsh_code_length);
  request.set_walsh_code_number(walsh_code_number);
  const auto branch_ptr = branch.get_if<CdaMeasurementChannelBranch>();
  const auto branch_raw_ptr = branch.get_if<pb::int32>();
  if (branch_ptr) {
    request.set_branch(*branch_ptr);
  }
  else if (branch_raw_ptr) {
    request.set_branch_raw(*branch_raw_ptr);
  }

  auto response = CDACfgMeasurementChannelResponse{};

  raise_if_error(
      stub->CDACfgMeasurementChannel(&context, request, &response),
      context);

  return response;
}

CDACfgPowerUnitResponse
cda_cfg_power_unit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<CdaPowerUnit, pb::int32>& power_unit)
{
  ::grpc::ClientContext context;

  auto request = CDACfgPowerUnitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto power_unit_ptr = power_unit.get_if<CdaPowerUnit>();
  const auto power_unit_raw_ptr = power_unit.get_if<pb::int32>();
  if (power_unit_ptr) {
    request.set_power_unit(*power_unit_ptr);
  }
  else if (power_unit_raw_ptr) {
    request.set_power_unit_raw(*power_unit_raw_ptr);
  }

  auto response = CDACfgPowerUnitResponse{};

  raise_if_error(
      stub->CDACfgPowerUnit(&context, request, &response),
      context);

  return response;
}

CDACfgSynchronizationModeAndIntervalResponse
cda_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<CdaSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length)
{
  ::grpc::ClientContext context;

  auto request = CDACfgSynchronizationModeAndIntervalRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto synchronization_mode_ptr = synchronization_mode.get_if<CdaSynchronizationMode>();
  const auto synchronization_mode_raw_ptr = synchronization_mode.get_if<pb::int32>();
  if (synchronization_mode_ptr) {
    request.set_synchronization_mode(*synchronization_mode_ptr);
  }
  else if (synchronization_mode_raw_ptr) {
    request.set_synchronization_mode_raw(*synchronization_mode_raw_ptr);
  }
  request.set_measurement_offset(measurement_offset);
  request.set_measurement_length(measurement_length);

  auto response = CDACfgSynchronizationModeAndIntervalResponse{};

  raise_if_error(
      stub->CDACfgSynchronizationModeAndInterval(&context, request, &response),
      context);

  return response;
}

CDAFetchCodeDomainIAndQPowerResponse
cda_fetch_code_domain_i_and_q_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchCodeDomainIAndQPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchCodeDomainIAndQPowerResponse{};

  raise_if_error(
      stub->CDAFetchCodeDomainIAndQPower(&context, request, &response),
      context);

  return response;
}

CDAFetchCodeDomainIAndQPowerTraceResponse
cda_fetch_code_domain_i_and_q_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchCodeDomainIAndQPowerTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchCodeDomainIAndQPowerTraceResponse{};

  raise_if_error(
      stub->CDAFetchCodeDomainIAndQPowerTrace(&context, request, &response),
      context);

  return response;
}

CDAFetchCodeDomainPowerResponse
cda_fetch_code_domain_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchCodeDomainPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchCodeDomainPowerResponse{};

  raise_if_error(
      stub->CDAFetchCodeDomainPower(&context, request, &response),
      context);

  return response;
}

CDAFetchIQImpairmentsResponse
cda_fetch_iq_impairments(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchIQImpairmentsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchIQImpairmentsResponse{};

  raise_if_error(
      stub->CDAFetchIQImpairments(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolConstellationTraceResponse
cda_fetch_symbol_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolConstellationTraceResponse{};

  raise_if_error(
      stub->CDAFetchSymbolConstellationTrace(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolConstellationTraceInterleavedIQResponse
cda_fetch_symbol_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->CDAFetchSymbolConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolConstellationTraceSplitResponse
cda_fetch_symbol_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolConstellationTraceSplitResponse{};

  raise_if_error(
      stub->CDAFetchSymbolConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolEVMResponse
cda_fetch_symbol_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolEVMRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolEVMResponse{};

  raise_if_error(
      stub->CDAFetchSymbolEVM(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolEVMTraceResponse
cda_fetch_symbol_evm_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolEVMTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolEVMTraceResponse{};

  raise_if_error(
      stub->CDAFetchSymbolEVMTrace(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolMagnitudeErrorTraceResponse
cda_fetch_symbol_magnitude_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolMagnitudeErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolMagnitudeErrorTraceResponse{};

  raise_if_error(
      stub->CDAFetchSymbolMagnitudeErrorTrace(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolPhaseErrorTraceResponse
cda_fetch_symbol_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolPhaseErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolPhaseErrorTraceResponse{};

  raise_if_error(
      stub->CDAFetchSymbolPhaseErrorTrace(&context, request, &response),
      context);

  return response;
}

CDAFetchSymbolPowerTraceResponse
cda_fetch_symbol_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CDAFetchSymbolPowerTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CDAFetchSymbolPowerTraceResponse{};

  raise_if_error(
      stub->CDAFetchSymbolPowerTrace(&context, request, &response),
      context);

  return response;
}

CHPCfgAveragingResponse
chp_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<ChpAveragingType, pb::int32>& averaging_type)
{
  ::grpc::ClientContext context;

  auto request = CHPCfgAveragingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto averaging_enabled_ptr = averaging_enabled.get_if<ChpAveragingEnabled>();
  const auto averaging_enabled_raw_ptr = averaging_enabled.get_if<pb::int32>();
  if (averaging_enabled_ptr) {
    request.set_averaging_enabled(*averaging_enabled_ptr);
  }
  else if (averaging_enabled_raw_ptr) {
    request.set_averaging_enabled_raw(*averaging_enabled_raw_ptr);
  }
  request.set_averaging_count(averaging_count);
  const auto averaging_type_ptr = averaging_type.get_if<ChpAveragingType>();
  const auto averaging_type_raw_ptr = averaging_type.get_if<pb::int32>();
  if (averaging_type_ptr) {
    request.set_averaging_type(*averaging_type_ptr);
  }
  else if (averaging_type_raw_ptr) {
    request.set_averaging_type_raw(*averaging_type_raw_ptr);
  }

  auto response = CHPCfgAveragingResponse{};

  raise_if_error(
      stub->CHPCfgAveraging(&context, request, &response),
      context);

  return response;
}

CHPCfgRBWFilterResponse
chp_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<ChpRbwFilterType, pb::int32>& rbw_filter_type)
{
  ::grpc::ClientContext context;

  auto request = CHPCfgRBWFilterRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto rbw_auto_ptr = rbw_auto.get_if<ChpRbwAutoBandwidth>();
  const auto rbw_auto_raw_ptr = rbw_auto.get_if<pb::int32>();
  if (rbw_auto_ptr) {
    request.set_rbw_auto(*rbw_auto_ptr);
  }
  else if (rbw_auto_raw_ptr) {
    request.set_rbw_auto_raw(*rbw_auto_raw_ptr);
  }
  request.set_rbw(rbw);
  const auto rbw_filter_type_ptr = rbw_filter_type.get_if<ChpRbwFilterType>();
  const auto rbw_filter_type_raw_ptr = rbw_filter_type.get_if<pb::int32>();
  if (rbw_filter_type_ptr) {
    request.set_rbw_filter_type(*rbw_filter_type_ptr);
  }
  else if (rbw_filter_type_raw_ptr) {
    request.set_rbw_filter_type_raw(*rbw_filter_type_raw_ptr);
  }

  auto response = CHPCfgRBWFilterResponse{};

  raise_if_error(
      stub->CHPCfgRBWFilter(&context, request, &response),
      context);

  return response;
}

CHPCfgSweepTimeResponse
chp_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval)
{
  ::grpc::ClientContext context;

  auto request = CHPCfgSweepTimeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto sweep_time_auto_ptr = sweep_time_auto.get_if<ChpSweepTimeAuto>();
  const auto sweep_time_auto_raw_ptr = sweep_time_auto.get_if<pb::int32>();
  if (sweep_time_auto_ptr) {
    request.set_sweep_time_auto(*sweep_time_auto_ptr);
  }
  else if (sweep_time_auto_raw_ptr) {
    request.set_sweep_time_auto_raw(*sweep_time_auto_raw_ptr);
  }
  request.set_sweep_time_interval(sweep_time_interval);

  auto response = CHPCfgSweepTimeResponse{};

  raise_if_error(
      stub->CHPCfgSweepTime(&context, request, &response),
      context);

  return response;
}

CHPFetchCarrierAbsolutePowerResponse
chp_fetch_carrier_absolute_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CHPFetchCarrierAbsolutePowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CHPFetchCarrierAbsolutePowerResponse{};

  raise_if_error(
      stub->CHPFetchCarrierAbsolutePower(&context, request, &response),
      context);

  return response;
}

CHPFetchSpectrumResponse
chp_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = CHPFetchSpectrumRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = CHPFetchSpectrumResponse{};

  raise_if_error(
      stub->CHPFetchSpectrum(&context, request, &response),
      context);

  return response;
}

CfgBandClassResponse
cfg_band_class(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& band_class)
{
  ::grpc::ClientContext context;

  auto request = CfgBandClassRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_band_class(band_class);

  auto response = CfgBandClassResponse{};

  raise_if_error(
      stub->CfgBandClass(&context, request, &response),
      context);

  return response;
}

CfgChannelConfigurationModeResponse
cfg_channel_configuration_mode(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChannelConfigurationMode, pb::int32>& channel_configuration_mode)
{
  ::grpc::ClientContext context;

  auto request = CfgChannelConfigurationModeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto channel_configuration_mode_ptr = channel_configuration_mode.get_if<ChannelConfigurationMode>();
  const auto channel_configuration_mode_raw_ptr = channel_configuration_mode.get_if<pb::int32>();
  if (channel_configuration_mode_ptr) {
    request.set_channel_configuration_mode(*channel_configuration_mode_ptr);
  }
  else if (channel_configuration_mode_raw_ptr) {
    request.set_channel_configuration_mode_raw(*channel_configuration_mode_raw_ptr);
  }

  auto response = CfgChannelConfigurationModeResponse{};

  raise_if_error(
      stub->CfgChannelConfigurationMode(&context, request, &response),
      context);

  return response;
}

CfgDigitalEdgeTriggerResponse
cfg_digital_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<DigitalEdgeTriggerSource, std::string>& digital_edge_source, const simple_variant<DigitalEdgeTriggerEdge, pb::int32>& digital_edge, const double& trigger_delay, const pb::int32& enable_trigger)
{
  ::grpc::ClientContext context;

  auto request = CfgDigitalEdgeTriggerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto digital_edge_source_ptr = digital_edge_source.get_if<DigitalEdgeTriggerSource>();
  const auto digital_edge_source_raw_ptr = digital_edge_source.get_if<std::string>();
  if (digital_edge_source_ptr) {
    request.set_digital_edge_source_mapped(*digital_edge_source_ptr);
  }
  else if (digital_edge_source_raw_ptr) {
    request.set_digital_edge_source_raw(*digital_edge_source_raw_ptr);
  }
  const auto digital_edge_ptr = digital_edge.get_if<DigitalEdgeTriggerEdge>();
  const auto digital_edge_raw_ptr = digital_edge.get_if<pb::int32>();
  if (digital_edge_ptr) {
    request.set_digital_edge(*digital_edge_ptr);
  }
  else if (digital_edge_raw_ptr) {
    request.set_digital_edge_raw(*digital_edge_raw_ptr);
  }
  request.set_trigger_delay(trigger_delay);
  request.set_enable_trigger(enable_trigger);

  auto response = CfgDigitalEdgeTriggerResponse{};

  raise_if_error(
      stub->CfgDigitalEdgeTrigger(&context, request, &response),
      context);

  return response;
}

CfgExternalAttenuationResponse
cfg_external_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& external_attenuation)
{
  ::grpc::ClientContext context;

  auto request = CfgExternalAttenuationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_external_attenuation(external_attenuation);

  auto response = CfgExternalAttenuationResponse{};

  raise_if_error(
      stub->CfgExternalAttenuation(&context, request, &response),
      context);

  return response;
}

CfgFrequencyResponse
cfg_frequency(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& center_frequency)
{
  ::grpc::ClientContext context;

  auto request = CfgFrequencyRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_center_frequency(center_frequency);

  auto response = CfgFrequencyResponse{};

  raise_if_error(
      stub->CfgFrequency(&context, request, &response),
      context);

  return response;
}

CfgFrequencyChannelNumberResponse
cfg_frequency_channel_number(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<LinkDirection, pb::int32>& link_direction, const pb::int32& band_class, const pb::int32& channel_number)
{
  ::grpc::ClientContext context;

  auto request = CfgFrequencyChannelNumberRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto link_direction_ptr = link_direction.get_if<LinkDirection>();
  const auto link_direction_raw_ptr = link_direction.get_if<pb::int32>();
  if (link_direction_ptr) {
    request.set_link_direction(*link_direction_ptr);
  }
  else if (link_direction_raw_ptr) {
    request.set_link_direction_raw(*link_direction_raw_ptr);
  }
  request.set_band_class(band_class);
  request.set_channel_number(channel_number);

  auto response = CfgFrequencyChannelNumberResponse{};

  raise_if_error(
      stub->CfgFrequencyChannelNumber(&context, request, &response),
      context);

  return response;
}

CfgFrequencyReferenceResponse
cfg_frequency_reference(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<FrequencyReferenceSource, std::string>& frequency_reference_source, const double& frequency_reference_frequency)
{
  ::grpc::ClientContext context;

  auto request = CfgFrequencyReferenceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_channel_name(channel_name);
  const auto frequency_reference_source_ptr = frequency_reference_source.get_if<FrequencyReferenceSource>();
  const auto frequency_reference_source_raw_ptr = frequency_reference_source.get_if<std::string>();
  if (frequency_reference_source_ptr) {
    request.set_frequency_reference_source_mapped(*frequency_reference_source_ptr);
  }
  else if (frequency_reference_source_raw_ptr) {
    request.set_frequency_reference_source_raw(*frequency_reference_source_raw_ptr);
  }
  request.set_frequency_reference_frequency(frequency_reference_frequency);

  auto response = CfgFrequencyReferenceResponse{};

  raise_if_error(
      stub->CfgFrequencyReference(&context, request, &response),
      context);

  return response;
}

CfgIQPowerEdgeTriggerResponse
cfg_iq_power_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& iq_power_edge_source, const simple_variant<IQPowerEdgeTriggerSlope, pb::int32>& iq_power_edge_slope, const double& iq_power_edge_level, const double& trigger_delay, const simple_variant<TriggerMinimumQuietTimeMode, pb::int32>& minimum_quiet_time_mode, const double& minimum_quiet_time, const simple_variant<IQPowerEdgeTriggerLevelType, pb::int32>& iq_power_edge_level_type, const pb::int32& enable_trigger)
{
  ::grpc::ClientContext context;

  auto request = CfgIQPowerEdgeTriggerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_iq_power_edge_source(iq_power_edge_source);
  const auto iq_power_edge_slope_ptr = iq_power_edge_slope.get_if<IQPowerEdgeTriggerSlope>();
  const auto iq_power_edge_slope_raw_ptr = iq_power_edge_slope.get_if<pb::int32>();
  if (iq_power_edge_slope_ptr) {
    request.set_iq_power_edge_slope(*iq_power_edge_slope_ptr);
  }
  else if (iq_power_edge_slope_raw_ptr) {
    request.set_iq_power_edge_slope_raw(*iq_power_edge_slope_raw_ptr);
  }
  request.set_iq_power_edge_level(iq_power_edge_level);
  request.set_trigger_delay(trigger_delay);
  const auto minimum_quiet_time_mode_ptr = minimum_quiet_time_mode.get_if<TriggerMinimumQuietTimeMode>();
  const auto minimum_quiet_time_mode_raw_ptr = minimum_quiet_time_mode.get_if<pb::int32>();
  if (minimum_quiet_time_mode_ptr) {
    request.set_minimum_quiet_time_mode(*minimum_quiet_time_mode_ptr);
  }
  else if (minimum_quiet_time_mode_raw_ptr) {
    request.set_minimum_quiet_time_mode_raw(*minimum_quiet_time_mode_raw_ptr);
  }
  request.set_minimum_quiet_time(minimum_quiet_time);
  const auto iq_power_edge_level_type_ptr = iq_power_edge_level_type.get_if<IQPowerEdgeTriggerLevelType>();
  const auto iq_power_edge_level_type_raw_ptr = iq_power_edge_level_type.get_if<pb::int32>();
  if (iq_power_edge_level_type_ptr) {
    request.set_iq_power_edge_level_type(*iq_power_edge_level_type_ptr);
  }
  else if (iq_power_edge_level_type_raw_ptr) {
    request.set_iq_power_edge_level_type_raw(*iq_power_edge_level_type_raw_ptr);
  }
  request.set_enable_trigger(enable_trigger);

  auto response = CfgIQPowerEdgeTriggerResponse{};

  raise_if_error(
      stub->CfgIQPowerEdgeTrigger(&context, request, &response),
      context);

  return response;
}

CfgMechanicalAttenuationResponse
cfg_mechanical_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<MechanicalAttenuationAuto, pb::int32>& mechanical_attenuation_auto, const double& mechanical_attenuation_value)
{
  ::grpc::ClientContext context;

  auto request = CfgMechanicalAttenuationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_channel_name(channel_name);
  const auto mechanical_attenuation_auto_ptr = mechanical_attenuation_auto.get_if<MechanicalAttenuationAuto>();
  const auto mechanical_attenuation_auto_raw_ptr = mechanical_attenuation_auto.get_if<pb::int32>();
  if (mechanical_attenuation_auto_ptr) {
    request.set_mechanical_attenuation_auto(*mechanical_attenuation_auto_ptr);
  }
  else if (mechanical_attenuation_auto_raw_ptr) {
    request.set_mechanical_attenuation_auto_raw(*mechanical_attenuation_auto_raw_ptr);
  }
  request.set_mechanical_attenuation_value(mechanical_attenuation_value);

  auto response = CfgMechanicalAttenuationResponse{};

  raise_if_error(
      stub->CfgMechanicalAttenuation(&context, request, &response),
      context);

  return response;
}

CfgNumberOfChannelsResponse
cfg_number_of_channels(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_channels)
{
  ::grpc::ClientContext context;

  auto request = CfgNumberOfChannelsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_number_of_channels(number_of_channels);

  auto response = CfgNumberOfChannelsResponse{};

  raise_if_error(
      stub->CfgNumberOfChannels(&context, request, &response),
      context);

  return response;
}

CfgRFResponse
cfg_rf(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& center_frequency, const double& reference_level, const double& external_attenuation)
{
  ::grpc::ClientContext context;

  auto request = CfgRFRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_center_frequency(center_frequency);
  request.set_reference_level(reference_level);
  request.set_external_attenuation(external_attenuation);

  auto response = CfgRFResponse{};

  raise_if_error(
      stub->CfgRF(&context, request, &response),
      context);

  return response;
}

CfgRFAttenuationResponse
cfg_rf_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<RFAttenuationAuto, pb::int32>& rf_attenuation_auto, const double& rf_attenuation_value)
{
  ::grpc::ClientContext context;

  auto request = CfgRFAttenuationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_channel_name(channel_name);
  const auto rf_attenuation_auto_ptr = rf_attenuation_auto.get_if<RFAttenuationAuto>();
  const auto rf_attenuation_auto_raw_ptr = rf_attenuation_auto.get_if<pb::int32>();
  if (rf_attenuation_auto_ptr) {
    request.set_rf_attenuation_auto(*rf_attenuation_auto_ptr);
  }
  else if (rf_attenuation_auto_raw_ptr) {
    request.set_rf_attenuation_auto_raw(*rf_attenuation_auto_raw_ptr);
  }
  request.set_rf_attenuation_value(rf_attenuation_value);

  auto response = CfgRFAttenuationResponse{};

  raise_if_error(
      stub->CfgRFAttenuation(&context, request, &response),
      context);

  return response;
}

CfgRadioConfigurationResponse
cfg_radio_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<RadioConfiguration, pb::int32>& radio_configuration)
{
  ::grpc::ClientContext context;

  auto request = CfgRadioConfigurationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto radio_configuration_ptr = radio_configuration.get_if<RadioConfiguration>();
  const auto radio_configuration_raw_ptr = radio_configuration.get_if<pb::int32>();
  if (radio_configuration_ptr) {
    request.set_radio_configuration(*radio_configuration_ptr);
  }
  else if (radio_configuration_raw_ptr) {
    request.set_radio_configuration_raw(*radio_configuration_raw_ptr);
  }

  auto response = CfgRadioConfigurationResponse{};

  raise_if_error(
      stub->CfgRadioConfiguration(&context, request, &response),
      context);

  return response;
}

CfgReferenceLevelResponse
cfg_reference_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& reference_level)
{
  ::grpc::ClientContext context;

  auto request = CfgReferenceLevelRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_reference_level(reference_level);

  auto response = CfgReferenceLevelResponse{};

  raise_if_error(
      stub->CfgReferenceLevel(&context, request, &response),
      context);

  return response;
}

CfgSoftwareEdgeTriggerResponse
cfg_software_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& trigger_delay, const pb::int32& enable_trigger)
{
  ::grpc::ClientContext context;

  auto request = CfgSoftwareEdgeTriggerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_trigger_delay(trigger_delay);
  request.set_enable_trigger(enable_trigger);

  auto response = CfgSoftwareEdgeTriggerResponse{};

  raise_if_error(
      stub->CfgSoftwareEdgeTrigger(&context, request, &response),
      context);

  return response;
}

CfgUplinkSpreadingResponse
cfg_uplink_spreading(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int64& uplink_spreading_long_code_mask)
{
  ::grpc::ClientContext context;

  auto request = CfgUplinkSpreadingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_uplink_spreading_long_code_mask(uplink_spreading_long_code_mask);

  auto response = CfgUplinkSpreadingResponse{};

  raise_if_error(
      stub->CfgUplinkSpreading(&context, request, &response),
      context);

  return response;
}

CfgUserDefinedChannelResponse
cfg_user_defined_channel(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& walsh_code_length, const pb::int32& walsh_code_number, const simple_variant<Branch, pb::int32>& branch)
{
  ::grpc::ClientContext context;

  auto request = CfgUserDefinedChannelRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_walsh_code_length(walsh_code_length);
  request.set_walsh_code_number(walsh_code_number);
  const auto branch_ptr = branch.get_if<Branch>();
  const auto branch_raw_ptr = branch.get_if<pb::int32>();
  if (branch_ptr) {
    request.set_branch(*branch_ptr);
  }
  else if (branch_raw_ptr) {
    request.set_branch_raw(*branch_raw_ptr);
  }

  auto response = CfgUserDefinedChannelResponse{};

  raise_if_error(
      stub->CfgUserDefinedChannel(&context, request, &response),
      context);

  return response;
}

CfgUserDefinedChannelArrayResponse
cfg_user_defined_channel_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<pb::int32>& walsh_code_length, const std::vector<pb::int32>& walsh_code_number, const std::vector<pb::int32>& branch)
{
  ::grpc::ClientContext context;

  auto request = CfgUserDefinedChannelArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  copy_array(walsh_code_length, request.mutable_walsh_code_length());
  copy_array(walsh_code_number, request.mutable_walsh_code_number());
  copy_array(branch, request.mutable_branch());

  auto response = CfgUserDefinedChannelArrayResponse{};

  raise_if_error(
      stub->CfgUserDefinedChannelArray(&context, request, &response),
      context);

  return response;
}

CheckMeasurementStatusResponse
check_measurement_status(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = CheckMeasurementStatusRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = CheckMeasurementStatusResponse{};

  raise_if_error(
      stub->CheckMeasurementStatus(&context, request, &response),
      context);

  return response;
}

ClearAllNamedResultsResponse
clear_all_named_results(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = ClearAllNamedResultsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = ClearAllNamedResultsResponse{};

  raise_if_error(
      stub->ClearAllNamedResults(&context, request, &response),
      context);

  return response;
}

ClearNamedResultResponse
clear_named_result(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = ClearNamedResultRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = ClearNamedResultResponse{};

  raise_if_error(
      stub->ClearNamedResult(&context, request, &response),
      context);

  return response;
}

CloneSignalConfigurationResponse
clone_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& old_signal_name, const std::string& new_signal_name)
{
  ::grpc::ClientContext context;

  auto request = CloneSignalConfigurationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_old_signal_name(old_signal_name);
  request.set_new_signal_name(new_signal_name);

  auto response = CloneSignalConfigurationResponse{};

  raise_if_error(
      stub->CloneSignalConfiguration(&context, request, &response),
      context);

  return response;
}

CloseResponse
close(const StubPtr& stub, const nidevice_grpc::Session& instrument, const bool& force_destroy)
{
  ::grpc::ClientContext context;

  auto request = CloseRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_force_destroy(force_destroy);

  auto response = CloseResponse{};

  raise_if_error(
      stub->Close(&context, request, &response),
      context);

  return response;
}

CommitResponse
commit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = CommitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = CommitResponse{};

  raise_if_error(
      stub->Commit(&context, request, &response),
      context);

  return response;
}

CreateSignalConfigurationResponse
create_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& signal_name)
{
  ::grpc::ClientContext context;

  auto request = CreateSignalConfigurationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_signal_name(signal_name);

  auto response = CreateSignalConfigurationResponse{};

  raise_if_error(
      stub->CreateSignalConfiguration(&context, request, &response),
      context);

  return response;
}

DeleteSignalConfigurationResponse
delete_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& signal_name)
{
  ::grpc::ClientContext context;

  auto request = DeleteSignalConfigurationRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_signal_name(signal_name);

  auto response = DeleteSignalConfigurationResponse{};

  raise_if_error(
      stub->DeleteSignalConfiguration(&context, request, &response),
      context);

  return response;
}

DisableTriggerResponse
disable_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = DisableTriggerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = DisableTriggerResponse{};

  raise_if_error(
      stub->DisableTrigger(&context, request, &response),
      context);

  return response;
}

GetAllNamedResultNamesResponse
get_all_named_result_names(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = GetAllNamedResultNamesRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = GetAllNamedResultNamesResponse{};

  raise_if_error(
      stub->GetAllNamedResultNames(&context, request, &response),
      context);

  return response;
}

GetAttributeF32Response
get_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeF32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeF32Response{};

  raise_if_error(
      stub->GetAttributeF32(&context, request, &response),
      context);

  return response;
}

GetAttributeF32ArrayResponse
get_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeF32ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeF32ArrayResponse{};

  raise_if_error(
      stub->GetAttributeF32Array(&context, request, &response),
      context);

  return response;
}

GetAttributeF64Response
get_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeF64Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeF64Response{};

  raise_if_error(
      stub->GetAttributeF64(&context, request, &response),
      context);

  return response;
}

GetAttributeF64ArrayResponse
get_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeF64ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeF64ArrayResponse{};

  raise_if_error(
      stub->GetAttributeF64Array(&context, request, &response),
      context);

  return response;
}

GetAttributeI16Response
get_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI16Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI16Response{};

  raise_if_error(
      stub->GetAttributeI16(&context, request, &response),
      context);

  return response;
}

GetAttributeI32Response
get_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI32Response{};

  raise_if_error(
      stub->GetAttributeI32(&context, request, &response),
      context);

  return response;
}

GetAttributeI32ArrayResponse
get_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI32ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI32ArrayResponse{};

  raise_if_error(
      stub->GetAttributeI32Array(&context, request, &response),
      context);

  return response;
}

GetAttributeI64Response
get_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI64Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI64Response{};

  raise_if_error(
      stub->GetAttributeI64(&context, request, &response),
      context);

  return response;
}

GetAttributeI64ArrayResponse
get_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI64ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI64ArrayResponse{};

  raise_if_error(
      stub->GetAttributeI64Array(&context, request, &response),
      context);

  return response;
}

GetAttributeI8Response
get_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI8Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI8Response{};

  raise_if_error(
      stub->GetAttributeI8(&context, request, &response),
      context);

  return response;
}

GetAttributeI8ArrayResponse
get_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeI8ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeI8ArrayResponse{};

  raise_if_error(
      stub->GetAttributeI8Array(&context, request, &response),
      context);

  return response;
}

GetAttributeNIComplexDoubleArrayResponse
get_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeNIComplexDoubleArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeNIComplexDoubleArrayResponse{};

  raise_if_error(
      stub->GetAttributeNIComplexDoubleArray(&context, request, &response),
      context);

  return response;
}

GetAttributeNIComplexSingleArrayResponse
get_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeNIComplexSingleArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeNIComplexSingleArrayResponse{};

  raise_if_error(
      stub->GetAttributeNIComplexSingleArray(&context, request, &response),
      context);

  return response;
}

GetAttributeStringResponse
get_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeStringRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeStringResponse{};

  raise_if_error(
      stub->GetAttributeString(&context, request, &response),
      context);

  return response;
}

GetAttributeU16Response
get_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeU16Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeU16Response{};

  raise_if_error(
      stub->GetAttributeU16(&context, request, &response),
      context);

  return response;
}

GetAttributeU32Response
get_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeU32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeU32Response{};

  raise_if_error(
      stub->GetAttributeU32(&context, request, &response),
      context);

  return response;
}

GetAttributeU32ArrayResponse
get_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeU32ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeU32ArrayResponse{};

  raise_if_error(
      stub->GetAttributeU32Array(&context, request, &response),
      context);

  return response;
}

GetAttributeU64ArrayResponse
get_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeU64ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeU64ArrayResponse{};

  raise_if_error(
      stub->GetAttributeU64Array(&context, request, &response),
      context);

  return response;
}

GetAttributeU8Response
get_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeU8Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeU8Response{};

  raise_if_error(
      stub->GetAttributeU8(&context, request, &response),
      context);

  return response;
}

GetAttributeU8ArrayResponse
get_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = GetAttributeU8ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = GetAttributeU8ArrayResponse{};

  raise_if_error(
      stub->GetAttributeU8Array(&context, request, &response),
      context);

  return response;
}

GetErrorResponse
get_error(const StubPtr& stub, const nidevice_grpc::Session& instrument)
{
  ::grpc::ClientContext context;

  auto request = GetErrorRequest{};
  request.mutable_instrument()->CopyFrom(instrument);

  auto response = GetErrorResponse{};

  raise_if_error(
      stub->GetError(&context, request, &response),
      context);

  return response;
}

GetErrorStringResponse
get_error_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const pb::int32& error_code)
{
  ::grpc::ClientContext context;

  auto request = GetErrorStringRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_error_code(error_code);

  auto response = GetErrorStringResponse{};

  raise_if_error(
      stub->GetErrorString(&context, request, &response),
      context);

  return response;
}

InitializeResponse
initialize(const StubPtr& stub, const std::string& resource_name, const std::string& option_string, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior)
{
  ::grpc::ClientContext context;

  auto request = InitializeRequest{};
  request.set_resource_name(resource_name);
  request.set_option_string(option_string);
  request.set_initialization_behavior(initialization_behavior);

  auto response = InitializeResponse{};

  raise_if_error(
      stub->Initialize(&context, request, &response),
      context);

  return response;
}

InitializeFromNIRFSASessionResponse
initialize_from_nirfsa_session(const StubPtr& stub, const nidevice_grpc::Session& nirfsa_session, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior)
{
  ::grpc::ClientContext context;

  auto request = InitializeFromNIRFSASessionRequest{};
  request.mutable_nirfsa_session()->CopyFrom(nirfsa_session);
  request.set_initialization_behavior(initialization_behavior);

  auto response = InitializeFromNIRFSASessionResponse{};

  raise_if_error(
      stub->InitializeFromNIRFSASession(&context, request, &response),
      context);

  return response;
}

InitiateResponse
initiate(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name)
{
  ::grpc::ClientContext context;

  auto request = InitiateRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_result_name(result_name);

  auto response = InitiateResponse{};

  raise_if_error(
      stub->Initiate(&context, request, &response),
      context);

  return response;
}

ModAccCfgSynchronizationModeAndIntervalResponse
mod_acc_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ModAccSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length)
{
  ::grpc::ClientContext context;

  auto request = ModAccCfgSynchronizationModeAndIntervalRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto synchronization_mode_ptr = synchronization_mode.get_if<ModAccSynchronizationMode>();
  const auto synchronization_mode_raw_ptr = synchronization_mode.get_if<pb::int32>();
  if (synchronization_mode_ptr) {
    request.set_synchronization_mode(*synchronization_mode_ptr);
  }
  else if (synchronization_mode_raw_ptr) {
    request.set_synchronization_mode_raw(*synchronization_mode_raw_ptr);
  }
  request.set_measurement_offset(measurement_offset);
  request.set_measurement_length(measurement_length);

  auto response = ModAccCfgSynchronizationModeAndIntervalResponse{};

  raise_if_error(
      stub->ModAccCfgSynchronizationModeAndInterval(&context, request, &response),
      context);

  return response;
}

ModAccFetchConstellationTraceResponse
mod_acc_fetch_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchConstellationTraceResponse{};

  raise_if_error(
      stub->ModAccFetchConstellationTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchConstellationTraceInterleavedIQResponse
mod_acc_fetch_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->ModAccFetchConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

ModAccFetchConstellationTraceSplitResponse
mod_acc_fetch_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchConstellationTraceSplitResponse{};

  raise_if_error(
      stub->ModAccFetchConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

ModAccFetchDetectedChannelResponse
mod_acc_fetch_detected_channel(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchDetectedChannelRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchDetectedChannelResponse{};

  raise_if_error(
      stub->ModAccFetchDetectedChannel(&context, request, &response),
      context);

  return response;
}

ModAccFetchDetectedChannelArrayResponse
mod_acc_fetch_detected_channel_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchDetectedChannelArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchDetectedChannelArrayResponse{};

  raise_if_error(
      stub->ModAccFetchDetectedChannelArray(&context, request, &response),
      context);

  return response;
}

ModAccFetchEVMResponse
mod_acc_fetch_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchEVMRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchEVMResponse{};

  raise_if_error(
      stub->ModAccFetchEVM(&context, request, &response),
      context);

  return response;
}

ModAccFetchEVMTraceResponse
mod_acc_fetch_evm_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchEVMTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchEVMTraceResponse{};

  raise_if_error(
      stub->ModAccFetchEVMTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchIQImpairmentsResponse
mod_acc_fetch_iq_impairments(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchIQImpairmentsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchIQImpairmentsResponse{};

  raise_if_error(
      stub->ModAccFetchIQImpairments(&context, request, &response),
      context);

  return response;
}

ModAccFetchMagnitudeErrorTraceResponse
mod_acc_fetch_magnitude_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchMagnitudeErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchMagnitudeErrorTraceResponse{};

  raise_if_error(
      stub->ModAccFetchMagnitudeErrorTrace(&context, request, &response),
      context);

  return response;
}

ModAccFetchNumberOfDetectedChannelsResponse
mod_acc_fetch_number_of_detected_channels(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchNumberOfDetectedChannelsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchNumberOfDetectedChannelsResponse{};

  raise_if_error(
      stub->ModAccFetchNumberOfDetectedChannels(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakActiveCDEResponse
mod_acc_fetch_peak_active_cde(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakActiveCDERequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakActiveCDEResponse{};

  raise_if_error(
      stub->ModAccFetchPeakActiveCDE(&context, request, &response),
      context);

  return response;
}

ModAccFetchPeakCDEResponse
mod_acc_fetch_peak_cde(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPeakCDERequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPeakCDEResponse{};

  raise_if_error(
      stub->ModAccFetchPeakCDE(&context, request, &response),
      context);

  return response;
}

ModAccFetchPhaseErrorTraceResponse
mod_acc_fetch_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = ModAccFetchPhaseErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = ModAccFetchPhaseErrorTraceResponse{};

  raise_if_error(
      stub->ModAccFetchPhaseErrorTrace(&context, request, &response),
      context);

  return response;
}

OBWCfgAveragingResponse
obw_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<ObwAveragingType, pb::int32>& averaging_type)
{
  ::grpc::ClientContext context;

  auto request = OBWCfgAveragingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto averaging_enabled_ptr = averaging_enabled.get_if<ObwAveragingEnabled>();
  const auto averaging_enabled_raw_ptr = averaging_enabled.get_if<pb::int32>();
  if (averaging_enabled_ptr) {
    request.set_averaging_enabled(*averaging_enabled_ptr);
  }
  else if (averaging_enabled_raw_ptr) {
    request.set_averaging_enabled_raw(*averaging_enabled_raw_ptr);
  }
  request.set_averaging_count(averaging_count);
  const auto averaging_type_ptr = averaging_type.get_if<ObwAveragingType>();
  const auto averaging_type_raw_ptr = averaging_type.get_if<pb::int32>();
  if (averaging_type_ptr) {
    request.set_averaging_type(*averaging_type_ptr);
  }
  else if (averaging_type_raw_ptr) {
    request.set_averaging_type_raw(*averaging_type_raw_ptr);
  }

  auto response = OBWCfgAveragingResponse{};

  raise_if_error(
      stub->OBWCfgAveraging(&context, request, &response),
      context);

  return response;
}

OBWCfgRBWFilterResponse
obw_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<ObwRbwFilterType, pb::int32>& rbw_filter_type)
{
  ::grpc::ClientContext context;

  auto request = OBWCfgRBWFilterRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto rbw_auto_ptr = rbw_auto.get_if<ObwRbwAutoBandwidth>();
  const auto rbw_auto_raw_ptr = rbw_auto.get_if<pb::int32>();
  if (rbw_auto_ptr) {
    request.set_rbw_auto(*rbw_auto_ptr);
  }
  else if (rbw_auto_raw_ptr) {
    request.set_rbw_auto_raw(*rbw_auto_raw_ptr);
  }
  request.set_rbw(rbw);
  const auto rbw_filter_type_ptr = rbw_filter_type.get_if<ObwRbwFilterType>();
  const auto rbw_filter_type_raw_ptr = rbw_filter_type.get_if<pb::int32>();
  if (rbw_filter_type_ptr) {
    request.set_rbw_filter_type(*rbw_filter_type_ptr);
  }
  else if (rbw_filter_type_raw_ptr) {
    request.set_rbw_filter_type_raw(*rbw_filter_type_raw_ptr);
  }

  auto response = OBWCfgRBWFilterResponse{};

  raise_if_error(
      stub->OBWCfgRBWFilter(&context, request, &response),
      context);

  return response;
}

OBWCfgSweepTimeResponse
obw_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval)
{
  ::grpc::ClientContext context;

  auto request = OBWCfgSweepTimeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto sweep_time_auto_ptr = sweep_time_auto.get_if<ObwSweepTimeAuto>();
  const auto sweep_time_auto_raw_ptr = sweep_time_auto.get_if<pb::int32>();
  if (sweep_time_auto_ptr) {
    request.set_sweep_time_auto(*sweep_time_auto_ptr);
  }
  else if (sweep_time_auto_raw_ptr) {
    request.set_sweep_time_auto_raw(*sweep_time_auto_raw_ptr);
  }
  request.set_sweep_time_interval(sweep_time_interval);

  auto response = OBWCfgSweepTimeResponse{};

  raise_if_error(
      stub->OBWCfgSweepTime(&context, request, &response),
      context);

  return response;
}

OBWFetchMeasurementResponse
obw_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = OBWFetchMeasurementRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = OBWFetchMeasurementResponse{};

  raise_if_error(
      stub->OBWFetchMeasurement(&context, request, &response),
      context);

  return response;
}

OBWFetchSpectrumResponse
obw_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = OBWFetchSpectrumRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = OBWFetchSpectrumResponse{};

  raise_if_error(
      stub->OBWFetchSpectrum(&context, request, &response),
      context);

  return response;
}

QEVMCfgAveragingResponse
qevm_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<QevmAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count)
{
  ::grpc::ClientContext context;

  auto request = QEVMCfgAveragingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto averaging_enabled_ptr = averaging_enabled.get_if<QevmAveragingEnabled>();
  const auto averaging_enabled_raw_ptr = averaging_enabled.get_if<pb::int32>();
  if (averaging_enabled_ptr) {
    request.set_averaging_enabled(*averaging_enabled_ptr);
  }
  else if (averaging_enabled_raw_ptr) {
    request.set_averaging_enabled_raw(*averaging_enabled_raw_ptr);
  }
  request.set_averaging_count(averaging_count);

  auto response = QEVMCfgAveragingResponse{};

  raise_if_error(
      stub->QEVMCfgAveraging(&context, request, &response),
      context);

  return response;
}

QEVMCfgMeasurementLengthResponse
qevm_cfg_measurement_length(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& measurement_length)
{
  ::grpc::ClientContext context;

  auto request = QEVMCfgMeasurementLengthRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_measurement_length(measurement_length);

  auto response = QEVMCfgMeasurementLengthResponse{};

  raise_if_error(
      stub->QEVMCfgMeasurementLength(&context, request, &response),
      context);

  return response;
}

QEVMFetchConstellationTraceResponse
qevm_fetch_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchConstellationTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchConstellationTraceResponse{};

  raise_if_error(
      stub->QEVMFetchConstellationTrace(&context, request, &response),
      context);

  return response;
}

QEVMFetchConstellationTraceInterleavedIQResponse
qevm_fetch_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchConstellationTraceInterleavedIQRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchConstellationTraceInterleavedIQResponse{};

  raise_if_error(
      stub->QEVMFetchConstellationTraceInterleavedIQ(&context, request, &response),
      context);

  return response;
}

QEVMFetchConstellationTraceSplitResponse
qevm_fetch_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchConstellationTraceSplitRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchConstellationTraceSplitResponse{};

  raise_if_error(
      stub->QEVMFetchConstellationTraceSplit(&context, request, &response),
      context);

  return response;
}

QEVMFetchEVMResponse
qevm_fetch_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchEVMRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchEVMResponse{};

  raise_if_error(
      stub->QEVMFetchEVM(&context, request, &response),
      context);

  return response;
}

QEVMFetchEVMTraceResponse
qevm_fetch_evm_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchEVMTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchEVMTraceResponse{};

  raise_if_error(
      stub->QEVMFetchEVMTrace(&context, request, &response),
      context);

  return response;
}

QEVMFetchIQImpairmentsResponse
qevm_fetch_iq_impairments(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchIQImpairmentsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchIQImpairmentsResponse{};

  raise_if_error(
      stub->QEVMFetchIQImpairments(&context, request, &response),
      context);

  return response;
}

QEVMFetchMagnitudeErrorTraceResponse
qevm_fetch_magnitude_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchMagnitudeErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchMagnitudeErrorTraceResponse{};

  raise_if_error(
      stub->QEVMFetchMagnitudeErrorTrace(&context, request, &response),
      context);

  return response;
}

QEVMFetchPhaseErrorTraceResponse
qevm_fetch_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = QEVMFetchPhaseErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = QEVMFetchPhaseErrorTraceResponse{};

  raise_if_error(
      stub->QEVMFetchPhaseErrorTrace(&context, request, &response),
      context);

  return response;
}

ResetAttributeResponse
reset_attribute(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id)
{
  ::grpc::ClientContext context;

  auto request = ResetAttributeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);

  auto response = ResetAttributeResponse{};

  raise_if_error(
      stub->ResetAttribute(&context, request, &response),
      context);

  return response;
}

ResetToDefaultResponse
reset_to_default(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string)
{
  ::grpc::ClientContext context;

  auto request = ResetToDefaultRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);

  auto response = ResetToDefaultResponse{};

  raise_if_error(
      stub->ResetToDefault(&context, request, &response),
      context);

  return response;
}

SEMCfgAveragingResponse
sem_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<SemAveragingType, pb::int32>& averaging_type)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgAveragingRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto averaging_enabled_ptr = averaging_enabled.get_if<SemAveragingEnabled>();
  const auto averaging_enabled_raw_ptr = averaging_enabled.get_if<pb::int32>();
  if (averaging_enabled_ptr) {
    request.set_averaging_enabled(*averaging_enabled_ptr);
  }
  else if (averaging_enabled_raw_ptr) {
    request.set_averaging_enabled_raw(*averaging_enabled_raw_ptr);
  }
  request.set_averaging_count(averaging_count);
  const auto averaging_type_ptr = averaging_type.get_if<SemAveragingType>();
  const auto averaging_type_raw_ptr = averaging_type.get_if<pb::int32>();
  if (averaging_type_ptr) {
    request.set_averaging_type(*averaging_type_ptr);
  }
  else if (averaging_type_raw_ptr) {
    request.set_averaging_type_raw(*averaging_type_raw_ptr);
  }

  auto response = SEMCfgAveragingResponse{};

  raise_if_error(
      stub->SEMCfgAveraging(&context, request, &response),
      context);

  return response;
}

SEMCfgSweepTimeResponse
sem_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval)
{
  ::grpc::ClientContext context;

  auto request = SEMCfgSweepTimeRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto sweep_time_auto_ptr = sweep_time_auto.get_if<SemSweepTimeAuto>();
  const auto sweep_time_auto_raw_ptr = sweep_time_auto.get_if<pb::int32>();
  if (sweep_time_auto_ptr) {
    request.set_sweep_time_auto(*sweep_time_auto_ptr);
  }
  else if (sweep_time_auto_raw_ptr) {
    request.set_sweep_time_auto_raw(*sweep_time_auto_raw_ptr);
  }
  request.set_sweep_time_interval(sweep_time_interval);

  auto response = SEMCfgSweepTimeResponse{};

  raise_if_error(
      stub->SEMCfgSweepTime(&context, request, &response),
      context);

  return response;
}

SEMFetchCarrierAbsoluteIntegratedPowerResponse
sem_fetch_carrier_absolute_integrated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchCarrierAbsoluteIntegratedPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchCarrierAbsoluteIntegratedPowerResponse{};

  raise_if_error(
      stub->SEMFetchCarrierAbsoluteIntegratedPower(&context, request, &response),
      context);

  return response;
}

SEMFetchLowerOffsetMarginResponse
sem_fetch_lower_offset_margin(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchLowerOffsetMarginRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchLowerOffsetMarginResponse{};

  raise_if_error(
      stub->SEMFetchLowerOffsetMargin(&context, request, &response),
      context);

  return response;
}

SEMFetchLowerOffsetMarginArrayResponse
sem_fetch_lower_offset_margin_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchLowerOffsetMarginArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchLowerOffsetMarginArrayResponse{};

  raise_if_error(
      stub->SEMFetchLowerOffsetMarginArray(&context, request, &response),
      context);

  return response;
}

SEMFetchLowerOffsetPowerResponse
sem_fetch_lower_offset_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchLowerOffsetPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchLowerOffsetPowerResponse{};

  raise_if_error(
      stub->SEMFetchLowerOffsetPower(&context, request, &response),
      context);

  return response;
}

SEMFetchLowerOffsetPowerArrayResponse
sem_fetch_lower_offset_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchLowerOffsetPowerArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchLowerOffsetPowerArrayResponse{};

  raise_if_error(
      stub->SEMFetchLowerOffsetPowerArray(&context, request, &response),
      context);

  return response;
}

SEMFetchMeasurementStatusResponse
sem_fetch_measurement_status(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchMeasurementStatusRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchMeasurementStatusResponse{};

  raise_if_error(
      stub->SEMFetchMeasurementStatus(&context, request, &response),
      context);

  return response;
}

SEMFetchSpectrumResponse
sem_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchSpectrumRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchSpectrumResponse{};

  raise_if_error(
      stub->SEMFetchSpectrum(&context, request, &response),
      context);

  return response;
}

SEMFetchUpperOffsetMarginResponse
sem_fetch_upper_offset_margin(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchUpperOffsetMarginRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchUpperOffsetMarginResponse{};

  raise_if_error(
      stub->SEMFetchUpperOffsetMargin(&context, request, &response),
      context);

  return response;
}

SEMFetchUpperOffsetMarginArrayResponse
sem_fetch_upper_offset_margin_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchUpperOffsetMarginArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchUpperOffsetMarginArrayResponse{};

  raise_if_error(
      stub->SEMFetchUpperOffsetMarginArray(&context, request, &response),
      context);

  return response;
}

SEMFetchUpperOffsetPowerResponse
sem_fetch_upper_offset_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchUpperOffsetPowerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchUpperOffsetPowerResponse{};

  raise_if_error(
      stub->SEMFetchUpperOffsetPower(&context, request, &response),
      context);

  return response;
}

SEMFetchUpperOffsetPowerArrayResponse
sem_fetch_upper_offset_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SEMFetchUpperOffsetPowerArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SEMFetchUpperOffsetPowerArrayResponse{};

  raise_if_error(
      stub->SEMFetchUpperOffsetPowerArray(&context, request, &response),
      context);

  return response;
}

SelectMeasurementsResponse
select_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<std::vector<MeasurementTypes>, std::int32_t>& measurements, const bool& enable_all_traces)
{
  ::grpc::ClientContext context;

  auto request = SelectMeasurementsRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_measurements_raw(copy_bitfield_as_enum_array(measurements));
  request.set_enable_all_traces(enable_all_traces);

  auto response = SelectMeasurementsResponse{};

  raise_if_error(
      stub->SelectMeasurements(&context, request, &response),
      context);

  return response;
}

SendSoftwareEdgeTriggerResponse
send_software_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument)
{
  ::grpc::ClientContext context;

  auto request = SendSoftwareEdgeTriggerRequest{};
  request.mutable_instrument()->CopyFrom(instrument);

  auto response = SendSoftwareEdgeTriggerResponse{};

  raise_if_error(
      stub->SendSoftwareEdgeTrigger(&context, request, &response),
      context);

  return response;
}

SetAttributeF32Response
set_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const float& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeF32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeF32Response{};

  raise_if_error(
      stub->SetAttributeF32(&context, request, &response),
      context);

  return response;
}

SetAttributeF32ArrayResponse
set_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<float>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeF32ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeF32ArrayResponse{};

  raise_if_error(
      stub->SetAttributeF32Array(&context, request, &response),
      context);

  return response;
}

SetAttributeF64Response
set_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const double& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeF64Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeF64Response{};

  raise_if_error(
      stub->SetAttributeF64(&context, request, &response),
      context);

  return response;
}

SetAttributeF64ArrayResponse
set_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<double>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeF64ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeF64ArrayResponse{};

  raise_if_error(
      stub->SetAttributeF64Array(&context, request, &response),
      context);

  return response;
}

SetAttributeI16Response
set_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::int32& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI16Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeI16Response{};

  raise_if_error(
      stub->SetAttributeI16(&context, request, &response),
      context);

  return response;
}

SetAttributeI32Response
set_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const simple_variant<NiRFmxCDMA2kInt32AttributeValues, pb::int32>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  const auto attr_val_ptr = attr_val.get_if<NiRFmxCDMA2kInt32AttributeValues>();
  const auto attr_val_raw_ptr = attr_val.get_if<pb::int32>();
  if (attr_val_ptr) {
    request.set_attr_val(*attr_val_ptr);
  }
  else if (attr_val_raw_ptr) {
    request.set_attr_val_raw(*attr_val_raw_ptr);
  }

  auto response = SetAttributeI32Response{};

  raise_if_error(
      stub->SetAttributeI32(&context, request, &response),
      context);

  return response;
}

SetAttributeI32ArrayResponse
set_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::int32>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI32ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeI32ArrayResponse{};

  raise_if_error(
      stub->SetAttributeI32Array(&context, request, &response),
      context);

  return response;
}

SetAttributeI64Response
set_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::int64& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI64Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeI64Response{};

  raise_if_error(
      stub->SetAttributeI64(&context, request, &response),
      context);

  return response;
}

SetAttributeI64ArrayResponse
set_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::int64>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI64ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeI64ArrayResponse{};

  raise_if_error(
      stub->SetAttributeI64Array(&context, request, &response),
      context);

  return response;
}

SetAttributeI8Response
set_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::int32& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI8Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeI8Response{};

  raise_if_error(
      stub->SetAttributeI8(&context, request, &response),
      context);

  return response;
}

SetAttributeI8ArrayResponse
set_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::int32>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeI8ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeI8ArrayResponse{};

  raise_if_error(
      stub->SetAttributeI8Array(&context, request, &response),
      context);

  return response;
}

SetAttributeNIComplexDoubleArrayResponse
set_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumber>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeNIComplexDoubleArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeNIComplexDoubleArrayResponse{};

  raise_if_error(
      stub->SetAttributeNIComplexDoubleArray(&context, request, &response),
      context);

  return response;
}

SetAttributeNIComplexSingleArrayResponse
set_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumberF32>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeNIComplexSingleArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeNIComplexSingleArrayResponse{};

  raise_if_error(
      stub->SetAttributeNIComplexSingleArray(&context, request, &response),
      context);

  return response;
}

SetAttributeStringResponse
set_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const simple_variant<NiRFmxCDMA2kStringAttributeValuesMapped, std::string>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeStringRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  const auto attr_val_ptr = attr_val.get_if<NiRFmxCDMA2kStringAttributeValuesMapped>();
  const auto attr_val_raw_ptr = attr_val.get_if<std::string>();
  if (attr_val_ptr) {
    request.set_attr_val_mapped(*attr_val_ptr);
  }
  else if (attr_val_raw_ptr) {
    request.set_attr_val_raw(*attr_val_raw_ptr);
  }

  auto response = SetAttributeStringResponse{};

  raise_if_error(
      stub->SetAttributeString(&context, request, &response),
      context);

  return response;
}

SetAttributeU16Response
set_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::uint32& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeU16Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeU16Response{};

  raise_if_error(
      stub->SetAttributeU16(&context, request, &response),
      context);

  return response;
}

SetAttributeU32Response
set_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::uint32& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeU32Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeU32Response{};

  raise_if_error(
      stub->SetAttributeU32(&context, request, &response),
      context);

  return response;
}

SetAttributeU32ArrayResponse
set_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::uint32>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeU32ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeU32ArrayResponse{};

  raise_if_error(
      stub->SetAttributeU32Array(&context, request, &response),
      context);

  return response;
}

SetAttributeU64ArrayResponse
set_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::uint64>& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeU64ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  copy_array(attr_val, request.mutable_attr_val());

  auto response = SetAttributeU64ArrayResponse{};

  raise_if_error(
      stub->SetAttributeU64Array(&context, request, &response),
      context);

  return response;
}

SetAttributeU8Response
set_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::uint32& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeU8Request{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeU8Response{};

  raise_if_error(
      stub->SetAttributeU8(&context, request, &response),
      context);

  return response;
}

SetAttributeU8ArrayResponse
set_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::string& attr_val)
{
  ::grpc::ClientContext context;

  auto request = SetAttributeU8ArrayRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_attribute_id(attribute_id);
  request.set_attr_val(attr_val);

  auto response = SetAttributeU8ArrayResponse{};

  raise_if_error(
      stub->SetAttributeU8Array(&context, request, &response),
      context);

  return response;
}

SlotPhaseCfgSynchronizationModeAndIntervalResponse
slot_phase_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SlotPhaseSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length)
{
  ::grpc::ClientContext context;

  auto request = SlotPhaseCfgSynchronizationModeAndIntervalRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto synchronization_mode_ptr = synchronization_mode.get_if<SlotPhaseSynchronizationMode>();
  const auto synchronization_mode_raw_ptr = synchronization_mode.get_if<pb::int32>();
  if (synchronization_mode_ptr) {
    request.set_synchronization_mode(*synchronization_mode_ptr);
  }
  else if (synchronization_mode_raw_ptr) {
    request.set_synchronization_mode_raw(*synchronization_mode_raw_ptr);
  }
  request.set_measurement_offset(measurement_offset);
  request.set_measurement_length(measurement_length);

  auto response = SlotPhaseCfgSynchronizationModeAndIntervalResponse{};

  raise_if_error(
      stub->SlotPhaseCfgSynchronizationModeAndInterval(&context, request, &response),
      context);

  return response;
}

SlotPhaseFetchChipPhaseErrorLinearFitTraceResponse
slot_phase_fetch_chip_phase_error_linear_fit_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SlotPhaseFetchChipPhaseErrorLinearFitTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SlotPhaseFetchChipPhaseErrorLinearFitTraceResponse{};

  raise_if_error(
      stub->SlotPhaseFetchChipPhaseErrorLinearFitTrace(&context, request, &response),
      context);

  return response;
}

SlotPhaseFetchChipPhaseErrorTraceResponse
slot_phase_fetch_chip_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SlotPhaseFetchChipPhaseErrorTraceRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SlotPhaseFetchChipPhaseErrorTraceResponse{};

  raise_if_error(
      stub->SlotPhaseFetchChipPhaseErrorTrace(&context, request, &response),
      context);

  return response;
}

SlotPhaseFetchMaximumPhaseDiscontinuityResponse
slot_phase_fetch_maximum_phase_discontinuity(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SlotPhaseFetchMaximumPhaseDiscontinuityRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SlotPhaseFetchMaximumPhaseDiscontinuityResponse{};

  raise_if_error(
      stub->SlotPhaseFetchMaximumPhaseDiscontinuity(&context, request, &response),
      context);

  return response;
}

SlotPhaseFetchPhaseDiscontinuitiesResponse
slot_phase_fetch_phase_discontinuities(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SlotPhaseFetchPhaseDiscontinuitiesRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SlotPhaseFetchPhaseDiscontinuitiesResponse{};

  raise_if_error(
      stub->SlotPhaseFetchPhaseDiscontinuities(&context, request, &response),
      context);

  return response;
}

SlotPowerCfgSynchronizationModeAndIntervalResponse
slot_power_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SlotPowerSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length)
{
  ::grpc::ClientContext context;

  auto request = SlotPowerCfgSynchronizationModeAndIntervalRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  const auto synchronization_mode_ptr = synchronization_mode.get_if<SlotPowerSynchronizationMode>();
  const auto synchronization_mode_raw_ptr = synchronization_mode.get_if<pb::int32>();
  if (synchronization_mode_ptr) {
    request.set_synchronization_mode(*synchronization_mode_ptr);
  }
  else if (synchronization_mode_raw_ptr) {
    request.set_synchronization_mode_raw(*synchronization_mode_raw_ptr);
  }
  request.set_measurement_offset(measurement_offset);
  request.set_measurement_length(measurement_length);

  auto response = SlotPowerCfgSynchronizationModeAndIntervalResponse{};

  raise_if_error(
      stub->SlotPowerCfgSynchronizationModeAndInterval(&context, request, &response),
      context);

  return response;
}

SlotPowerFetchPowersResponse
slot_power_fetch_powers(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = SlotPowerFetchPowersRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = SlotPowerFetchPowersResponse{};

  raise_if_error(
      stub->SlotPowerFetchPowers(&context, request, &response),
      context);

  return response;
}

WaitForAcquisitionCompleteResponse
wait_for_acquisition_complete(const StubPtr& stub, const nidevice_grpc::Session& instrument, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = WaitForAcquisitionCompleteRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_timeout(timeout);

  auto response = WaitForAcquisitionCompleteResponse{};

  raise_if_error(
      stub->WaitForAcquisitionComplete(&context, request, &response),
      context);

  return response;
}

WaitForMeasurementCompleteResponse
wait_for_measurement_complete(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout)
{
  ::grpc::ClientContext context;

  auto request = WaitForMeasurementCompleteRequest{};
  request.mutable_instrument()->CopyFrom(instrument);
  request.set_selector_string(selector_string);
  request.set_timeout(timeout);

  auto response = WaitForMeasurementCompleteResponse{};

  raise_if_error(
      stub->WaitForMeasurementComplete(&context, request, &response),
      context);

  return response;
}


} // namespace nirfmxcdma2k_grpc::experimental::client
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_client.h sha256=328e56e9d31508cc85fdda64d2c4d7b0b21c28d23b140e9667faf2017048a559 bytes=37123 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_client.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_client.h`
- sha256: `328e56e9d31508cc85fdda64d2c4d7b0b21c28d23b140e9667faf2017048a559`
- bytes: 37123

````c

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// EXPERIMENTAL Client convenience wrapper for NI-rfmxcdma2k.
//---------------------------------------------------------------------
#ifndef NIRFMXCDMA2K_GRPC_CLIENT_H
#define NIRFMXCDMA2K_GRPC_CLIENT_H

#include <grpcpp/grpcpp.h>

#include <nirfmxcdma2k.grpc.pb.h>
#include <tests/utilities/client_helpers.h>

#include <memory>
#include <vector>

namespace nirfmxcdma2k_grpc::experimental::client {

namespace pb = ::google::protobuf;
using StubPtr = std::unique_ptr<NiRFmxCDMA2k::Stub>;
using namespace nidevice_grpc::experimental::client;


ACPCfgAveragingResponse acp_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<AcpAveragingType, pb::int32>& averaging_type);
ACPCfgMeasurementMethodResponse acp_cfg_measurement_method(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpMeasurementMethod, pb::int32>& measurement_method);
ACPCfgNoiseCompensationEnabledResponse acp_cfg_noise_compensation_enabled(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpNoiseCompensationEnabled, pb::int32>& noise_compensation_enabled);
ACPCfgNumberOfOffsetsResponse acp_cfg_number_of_offsets(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_offsets);
ACPCfgRBWFilterResponse acp_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<AcpRbwFilterType, pb::int32>& rbw_filter_type);
ACPCfgSweepTimeResponse acp_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<AcpSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
ACPFetchAbsolutePowersTraceResponse acp_fetch_absolute_powers_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout, const pb::int32& trace_index);
ACPFetchCarrierAbsolutePowerResponse acp_fetch_carrier_absolute_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchOffsetMeasurementResponse acp_fetch_offset_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchOffsetMeasurementArrayResponse acp_fetch_offset_measurement_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ACPFetchRelativePowersTraceResponse acp_fetch_relative_powers_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout, const pb::int32& trace_index);
ACPFetchSpectrumResponse acp_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
AbortMeasurementsResponse abort_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
AnalyzeIQ1WaveformResponse analyze_iq1_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<nidevice_grpc::NIComplexNumberF32>& iq, const pb::int32& reset);
AnalyzeIQ1WaveformInterleavedIQResponse analyze_iq1_waveform_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& iq, const pb::int32& reset);
AnalyzeIQ1WaveformSplitResponse analyze_iq1_waveform_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& iqi, const std::vector<float>& iqq, const pb::int32& reset);
AnalyzeSpectrum1WaveformResponse analyze_spectrum1_waveform(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name, const double& x0, const double& dx, const std::vector<float>& spectrum, const pb::int32& reset);
AutoLevelResponse auto_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& measurement_interval);
BuildChannelStringResponse build_channel_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& channel_number);
BuildOffsetStringResponse build_offset_string(const StubPtr& stub, const std::string& selector_string, const pb::int32& offset_number);
BuildSignalStringResponse build_signal_string(const StubPtr& stub, const std::string& signal_name, const std::string& result_name);
CDACfgMeasurementChannelResponse cda_cfg_measurement_channel(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& walsh_code_length, const pb::int32& walsh_code_number, const simple_variant<CdaMeasurementChannelBranch, pb::int32>& branch);
CDACfgPowerUnitResponse cda_cfg_power_unit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<CdaPowerUnit, pb::int32>& power_unit);
CDACfgSynchronizationModeAndIntervalResponse cda_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<CdaSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length);
CDAFetchCodeDomainIAndQPowerResponse cda_fetch_code_domain_i_and_q_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchCodeDomainIAndQPowerTraceResponse cda_fetch_code_domain_i_and_q_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchCodeDomainPowerResponse cda_fetch_code_domain_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchIQImpairmentsResponse cda_fetch_iq_impairments(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolConstellationTraceResponse cda_fetch_symbol_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolConstellationTraceInterleavedIQResponse cda_fetch_symbol_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolConstellationTraceSplitResponse cda_fetch_symbol_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolEVMResponse cda_fetch_symbol_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolEVMTraceResponse cda_fetch_symbol_evm_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolMagnitudeErrorTraceResponse cda_fetch_symbol_magnitude_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolPhaseErrorTraceResponse cda_fetch_symbol_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CDAFetchSymbolPowerTraceResponse cda_fetch_symbol_power_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPCfgAveragingResponse chp_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<ChpAveragingType, pb::int32>& averaging_type);
CHPCfgRBWFilterResponse chp_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<ChpRbwFilterType, pb::int32>& rbw_filter_type);
CHPCfgSweepTimeResponse chp_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChpSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
CHPFetchCarrierAbsolutePowerResponse chp_fetch_carrier_absolute_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CHPFetchSpectrumResponse chp_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
CfgBandClassResponse cfg_band_class(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& band_class);
CfgChannelConfigurationModeResponse cfg_channel_configuration_mode(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ChannelConfigurationMode, pb::int32>& channel_configuration_mode);
CfgDigitalEdgeTriggerResponse cfg_digital_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<DigitalEdgeTriggerSource, std::string>& digital_edge_source, const simple_variant<DigitalEdgeTriggerEdge, pb::int32>& digital_edge, const double& trigger_delay, const pb::int32& enable_trigger);
CfgExternalAttenuationResponse cfg_external_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& external_attenuation);
CfgFrequencyResponse cfg_frequency(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& center_frequency);
CfgFrequencyChannelNumberResponse cfg_frequency_channel_number(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<LinkDirection, pb::int32>& link_direction, const pb::int32& band_class, const pb::int32& channel_number);
CfgFrequencyReferenceResponse cfg_frequency_reference(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<FrequencyReferenceSource, std::string>& frequency_reference_source, const double& frequency_reference_frequency);
CfgIQPowerEdgeTriggerResponse cfg_iq_power_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& iq_power_edge_source, const simple_variant<IQPowerEdgeTriggerSlope, pb::int32>& iq_power_edge_slope, const double& iq_power_edge_level, const double& trigger_delay, const simple_variant<TriggerMinimumQuietTimeMode, pb::int32>& minimum_quiet_time_mode, const double& minimum_quiet_time, const simple_variant<IQPowerEdgeTriggerLevelType, pb::int32>& iq_power_edge_level_type, const pb::int32& enable_trigger);
CfgMechanicalAttenuationResponse cfg_mechanical_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<MechanicalAttenuationAuto, pb::int32>& mechanical_attenuation_auto, const double& mechanical_attenuation_value);
CfgNumberOfChannelsResponse cfg_number_of_channels(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& number_of_channels);
CfgRFResponse cfg_rf(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& center_frequency, const double& reference_level, const double& external_attenuation);
CfgRFAttenuationResponse cfg_rf_attenuation(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& channel_name, const simple_variant<RFAttenuationAuto, pb::int32>& rf_attenuation_auto, const double& rf_attenuation_value);
CfgRadioConfigurationResponse cfg_radio_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<RadioConfiguration, pb::int32>& radio_configuration);
CfgReferenceLevelResponse cfg_reference_level(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& reference_level);
CfgSoftwareEdgeTriggerResponse cfg_software_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& trigger_delay, const pb::int32& enable_trigger);
CfgUplinkSpreadingResponse cfg_uplink_spreading(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int64& uplink_spreading_long_code_mask);
CfgUserDefinedChannelResponse cfg_user_defined_channel(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& walsh_code_length, const pb::int32& walsh_code_number, const simple_variant<Branch, pb::int32>& branch);
CfgUserDefinedChannelArrayResponse cfg_user_defined_channel_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::vector<pb::int32>& walsh_code_length, const std::vector<pb::int32>& walsh_code_number, const std::vector<pb::int32>& branch);
CheckMeasurementStatusResponse check_measurement_status(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
ClearAllNamedResultsResponse clear_all_named_results(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
ClearNamedResultResponse clear_named_result(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
CloneSignalConfigurationResponse clone_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& old_signal_name, const std::string& new_signal_name);
CloseResponse close(const StubPtr& stub, const nidevice_grpc::Session& instrument, const bool& force_destroy);
CommitResponse commit(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
CreateSignalConfigurationResponse create_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& signal_name);
DeleteSignalConfigurationResponse delete_signal_configuration(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& signal_name);
DisableTriggerResponse disable_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
GetAllNamedResultNamesResponse get_all_named_result_names(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
GetAttributeF32Response get_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeF32ArrayResponse get_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeF64Response get_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeF64ArrayResponse get_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI16Response get_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI32Response get_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI32ArrayResponse get_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI64Response get_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI64ArrayResponse get_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI8Response get_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeI8ArrayResponse get_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeNIComplexDoubleArrayResponse get_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeNIComplexSingleArrayResponse get_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeStringResponse get_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeU16Response get_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeU32Response get_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeU32ArrayResponse get_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeU64ArrayResponse get_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeU8Response get_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetAttributeU8ArrayResponse get_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
GetErrorResponse get_error(const StubPtr& stub, const nidevice_grpc::Session& instrument);
GetErrorStringResponse get_error_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const pb::int32& error_code);
InitializeResponse initialize(const StubPtr& stub, const std::string& resource_name, const std::string& option_string, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior = nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED);
InitializeFromNIRFSASessionResponse initialize_from_nirfsa_session(const StubPtr& stub, const nidevice_grpc::Session& nirfsa_session, const nidevice_grpc::SessionInitializationBehavior& initialization_behavior = nidevice_grpc::SESSION_INITIALIZATION_BEHAVIOR_UNSPECIFIED);
InitiateResponse initiate(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const std::string& result_name);
ModAccCfgSynchronizationModeAndIntervalResponse mod_acc_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ModAccSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length);
ModAccFetchConstellationTraceResponse mod_acc_fetch_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchConstellationTraceInterleavedIQResponse mod_acc_fetch_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchConstellationTraceSplitResponse mod_acc_fetch_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchDetectedChannelResponse mod_acc_fetch_detected_channel(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchDetectedChannelArrayResponse mod_acc_fetch_detected_channel_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchEVMResponse mod_acc_fetch_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchEVMTraceResponse mod_acc_fetch_evm_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchIQImpairmentsResponse mod_acc_fetch_iq_impairments(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchMagnitudeErrorTraceResponse mod_acc_fetch_magnitude_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchNumberOfDetectedChannelsResponse mod_acc_fetch_number_of_detected_channels(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakActiveCDEResponse mod_acc_fetch_peak_active_cde(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPeakCDEResponse mod_acc_fetch_peak_cde(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ModAccFetchPhaseErrorTraceResponse mod_acc_fetch_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
OBWCfgAveragingResponse obw_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<ObwAveragingType, pb::int32>& averaging_type);
OBWCfgRBWFilterResponse obw_cfg_rbw_filter(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwRbwAutoBandwidth, pb::int32>& rbw_auto, const double& rbw, const simple_variant<ObwRbwFilterType, pb::int32>& rbw_filter_type);
OBWCfgSweepTimeResponse obw_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<ObwSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
OBWFetchMeasurementResponse obw_fetch_measurement(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
OBWFetchSpectrumResponse obw_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMCfgAveragingResponse qevm_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<QevmAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count);
QEVMCfgMeasurementLengthResponse qevm_cfg_measurement_length(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const pb::int32& measurement_length);
QEVMFetchConstellationTraceResponse qevm_fetch_constellation_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchConstellationTraceInterleavedIQResponse qevm_fetch_constellation_trace_interleaved_iq(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchConstellationTraceSplitResponse qevm_fetch_constellation_trace_split(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchEVMResponse qevm_fetch_evm(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchEVMTraceResponse qevm_fetch_evm_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchIQImpairmentsResponse qevm_fetch_iq_impairments(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchMagnitudeErrorTraceResponse qevm_fetch_magnitude_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
QEVMFetchPhaseErrorTraceResponse qevm_fetch_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
ResetAttributeResponse reset_attribute(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id);
ResetToDefaultResponse reset_to_default(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string);
SEMCfgAveragingResponse sem_cfg_averaging(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemAveragingEnabled, pb::int32>& averaging_enabled, const pb::int32& averaging_count, const simple_variant<SemAveragingType, pb::int32>& averaging_type);
SEMCfgSweepTimeResponse sem_cfg_sweep_time(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SemSweepTimeAuto, pb::int32>& sweep_time_auto, const double& sweep_time_interval);
SEMFetchCarrierAbsoluteIntegratedPowerResponse sem_fetch_carrier_absolute_integrated_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetMarginResponse sem_fetch_lower_offset_margin(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetMarginArrayResponse sem_fetch_lower_offset_margin_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetPowerResponse sem_fetch_lower_offset_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchLowerOffsetPowerArrayResponse sem_fetch_lower_offset_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchMeasurementStatusResponse sem_fetch_measurement_status(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchSpectrumResponse sem_fetch_spectrum(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetMarginResponse sem_fetch_upper_offset_margin(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetMarginArrayResponse sem_fetch_upper_offset_margin_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetPowerResponse sem_fetch_upper_offset_power(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SEMFetchUpperOffsetPowerArrayResponse sem_fetch_upper_offset_power_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SelectMeasurementsResponse select_measurements(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<std::vector<MeasurementTypes>, std::int32_t>& measurements, const bool& enable_all_traces);
SendSoftwareEdgeTriggerResponse send_software_edge_trigger(const StubPtr& stub, const nidevice_grpc::Session& instrument);
SetAttributeF32Response set_attribute_f32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const float& attr_val);
SetAttributeF32ArrayResponse set_attribute_f32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<float>& attr_val);
SetAttributeF64Response set_attribute_f64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const double& attr_val);
SetAttributeF64ArrayResponse set_attribute_f64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<double>& attr_val);
SetAttributeI16Response set_attribute_i16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::int32& attr_val);
SetAttributeI32Response set_attribute_i32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const simple_variant<NiRFmxCDMA2kInt32AttributeValues, pb::int32>& attr_val);
SetAttributeI32ArrayResponse set_attribute_i32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::int32>& attr_val);
SetAttributeI64Response set_attribute_i64(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::int64& attr_val);
SetAttributeI64ArrayResponse set_attribute_i64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::int64>& attr_val);
SetAttributeI8Response set_attribute_i8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::int32& attr_val);
SetAttributeI8ArrayResponse set_attribute_i8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::int32>& attr_val);
SetAttributeNIComplexDoubleArrayResponse set_attribute_ni_complex_double_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumber>& attr_val);
SetAttributeNIComplexSingleArrayResponse set_attribute_ni_complex_single_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<nidevice_grpc::NIComplexNumberF32>& attr_val);
SetAttributeStringResponse set_attribute_string(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const simple_variant<NiRFmxCDMA2kStringAttributeValuesMapped, std::string>& attr_val);
SetAttributeU16Response set_attribute_u16(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::uint32& attr_val);
SetAttributeU32Response set_attribute_u32(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::uint32& attr_val);
SetAttributeU32ArrayResponse set_attribute_u32_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::uint32>& attr_val);
SetAttributeU64ArrayResponse set_attribute_u64_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::vector<pb::uint64>& attr_val);
SetAttributeU8Response set_attribute_u8(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const pb::uint32& attr_val);
SetAttributeU8ArrayResponse set_attribute_u8_array(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const NiRFmxCDMA2kAttribute& attribute_id, const std::string& attr_val);
SlotPhaseCfgSynchronizationModeAndIntervalResponse slot_phase_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SlotPhaseSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length);
SlotPhaseFetchChipPhaseErrorLinearFitTraceResponse slot_phase_fetch_chip_phase_error_linear_fit_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SlotPhaseFetchChipPhaseErrorTraceResponse slot_phase_fetch_chip_phase_error_trace(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SlotPhaseFetchMaximumPhaseDiscontinuityResponse slot_phase_fetch_maximum_phase_discontinuity(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SlotPhaseFetchPhaseDiscontinuitiesResponse slot_phase_fetch_phase_discontinuities(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
SlotPowerCfgSynchronizationModeAndIntervalResponse slot_power_cfg_synchronization_mode_and_interval(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const simple_variant<SlotPowerSynchronizationMode, pb::int32>& synchronization_mode, const pb::int32& measurement_offset, const pb::int32& measurement_length);
SlotPowerFetchPowersResponse slot_power_fetch_powers(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);
WaitForAcquisitionCompleteResponse wait_for_acquisition_complete(const StubPtr& stub, const nidevice_grpc::Session& instrument, const double& timeout);
WaitForMeasurementCompleteResponse wait_for_measurement_complete(const StubPtr& stub, const nidevice_grpc::Session& instrument, const std::string& selector_string, const double& timeout);

} // namespace nirfmxcdma2k_grpc::experimental::client

#endif /* NIRFMXCDMA2K_GRPC_CLIENT_H */
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_compilation_test.cpp sha256=ddf98340ef1056efe2de87b58ede6f33117e129c6358289b1f0a3b291e73a361 bytes=50253 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_compilation_test.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_compilation_test.cpp`
- sha256: `ddf98340ef1056efe2de87b58ede6f33117e129c6358289b1f0a3b291e73a361`
- bytes: 50253

````cpp
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Compilation test for the NI-rfmxcdma2k Metadata
//---------------------------------------------------------------------
#include "nirfmxcdma2k_library.h"

namespace nirfmxcdma2k_grpc {

int32 ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxCDMA2k_ACPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)
{
  return RFmxCDMA2k_ACPCfgMeasurementMethod(instrumentHandle, selectorString, measurementMethod);
}

int32 ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)
{
  return RFmxCDMA2k_ACPCfgNoiseCompensationEnabled(instrumentHandle, selectorString, noiseCompensationEnabled);
}

int32 ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)
{
  return RFmxCDMA2k_ACPCfgNumberOfOffsets(instrumentHandle, selectorString, numberOfOffsets);
}

int32 ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  return RFmxCDMA2k_ACPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxCDMA2k_ACPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ACPFetchAbsolutePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, absolutePowersTrace, arraySize, actualArraySize);
}

int32 ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower)
{
  return RFmxCDMA2k_ACPFetchCarrierAbsolutePower(instrumentHandle, selectorString, timeout, carrierAbsolutePower);
}

int32 ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower)
{
  return RFmxCDMA2k_ACPFetchOffsetMeasurement(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower);
}

int32 ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ACPFetchOffsetMeasurementArray(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower, arraySize, actualArraySize);
}

int32 ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ACPFetchRelativePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, relativePowersTrace, arraySize, actualArraySize);
}

int32 ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ACPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxCDMA2k_AbortMeasurements(instrumentHandle, selectorString);
}

int32 AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxCDMA2k_AnalyzeIQ1Waveform(instrumentHandle, selectorString, resultName, x0, dx, iq, arraySize, reset, reserved);
}

int32 AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxCDMA2k_AnalyzeIQ1Waveform(instrumentHandle, selectorString, resultName, x0, dx, reinterpret_cast<NIComplexSingle*>(iq), arraySize/2, reset, reserved);
}

int32 AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxCDMA2k_AnalyzeIQ1WaveformSplit(instrumentHandle, selectorString, resultName, x0, dx, iqi, iqq, arraySize, reset, reserved);
}

int32 AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)
{
  return RFmxCDMA2k_AnalyzeSpectrum1Waveform(instrumentHandle, selectorString, resultName, x0, dx, spectrum, arraySize, reset, reserved);
}

int32 AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel)
{
  return RFmxCDMA2k_AutoLevel(instrumentHandle, selectorString, measurementInterval, referenceLevel);
}

int32 BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxCDMA2k_BuildChannelString(selectorString, channelNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  return RFmxCDMA2k_BuildOffsetString(selectorString, offsetNumber, selectorStringOutLength, selectorStringOut);
}

int32 BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])
{
  return RFmxCDMA2k_BuildSignalString(signalName, resultName, selectorStringLength, selectorString);
}

int32 CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)
{
  return RFmxCDMA2k_CDACfgMeasurementChannel(instrumentHandle, selectorString, walshCodeLength, walshCodeNumber, branch);
}

int32 CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)
{
  return RFmxCDMA2k_CDACfgPowerUnit(instrumentHandle, selectorString, powerUnit);
}

int32 CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  return RFmxCDMA2k_CDACfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iMeanActivePower, float64* qMeanActivePower, float64* iPeakInactivePower, float64* qPeakInactivePower)
{
  return RFmxCDMA2k_CDAFetchCodeDomainIAndQPower(instrumentHandle, selectorString, timeout, iMeanActivePower, qMeanActivePower, iPeakInactivePower, qPeakInactivePower);
}

int32 CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace(instrumentHandle, selectorString, timeout, iCodeDomainPowers, qCodeDomainPowers, arraySize, actualArraySize);
}

int32 CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalPower, float64* totalActivePower, float64* meanActivePower, float64* peakActivePower, float64* meanInactivePower, float64* peakInactivePower)
{
  return RFmxCDMA2k_CDAFetchCodeDomainPower(instrumentHandle, selectorString, timeout, totalPower, totalActivePower, meanActivePower, peakActivePower, meanInactivePower, peakInactivePower);
}

int32 CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError)
{
  return RFmxCDMA2k_CDAFetchIQImpairments(instrumentHandle, selectorString, timeout, iqOriginOffset, iqGainImbalance, iqQuadratureError);
}

int32 CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolConstellationTrace(instrumentHandle, selectorString, timeout, symbolConstellation, arraySize, actualArraySize);
}

int32 CDAFetchSymbolConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(symbolConstellation), arraySize, actualArraySize);
}

int32 CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit(instrumentHandle, selectorString, timeout, symbolConstellationI, symbolConstellationQ, arraySize, actualArraySize);
}

int32 CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsSymbolEVM, float64* peakSymbolEVM, float64* rmsSymbolMagnitudeError, float64* rmsSymbolPhaseError, float64* meanSymbolPower, float64* frequencyError, float64* chipRateError)
{
  return RFmxCDMA2k_CDAFetchSymbolEVM(instrumentHandle, selectorString, timeout, rmsSymbolEVM, peakSymbolEVM, rmsSymbolMagnitudeError, rmsSymbolPhaseError, meanSymbolPower, frequencyError, chipRateError);
}

int32 CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolEVMTrace(instrumentHandle, selectorString, timeout, symbolEVM, arraySize, actualArraySize);
}

int32 CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace(instrumentHandle, selectorString, timeout, symbolMagnitudeError, arraySize, actualArraySize);
}

int32 CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace(instrumentHandle, selectorString, timeout, symbolPhaseError, arraySize, actualArraySize);
}

int32 CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CDAFetchSymbolPowerTrace(instrumentHandle, selectorString, timeout, symbolPowers, arraySize, actualArraySize);
}

int32 CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxCDMA2k_CHPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  return RFmxCDMA2k_CHPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxCDMA2k_CHPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 CHPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower)
{
  return RFmxCDMA2k_CHPFetchCarrierAbsolutePower(instrumentHandle, selectorString, timeout, carrierAbsolutePower);
}

int32 CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_CHPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 CfgBandClass(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass)
{
  return RFmxCDMA2k_CfgBandClass(instrumentHandle, selectorString, bandClass);
}

int32 CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)
{
  return RFmxCDMA2k_CfgChannelConfigurationMode(instrumentHandle, selectorString, channelConfigurationMode);
}

int32 CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)
{
  return RFmxCDMA2k_CfgDigitalEdgeTrigger(instrumentHandle, selectorString, digitalEdgeSource, digitalEdge, triggerDelay, enableTrigger);
}

int32 CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)
{
  return RFmxCDMA2k_CfgExternalAttenuation(instrumentHandle, selectorString, externalAttenuation);
}

int32 CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)
{
  return RFmxCDMA2k_CfgFrequency(instrumentHandle, selectorString, centerFrequency);
}

int32 CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber)
{
  return RFmxCDMA2k_CfgFrequencyChannelNumber(instrumentHandle, selectorString, linkDirection, bandClass, channelNumber);
}

int32 CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)
{
  return RFmxCDMA2k_CfgFrequencyReference(instrumentHandle, channelName, frequencyReferenceSource, frequencyReferenceFrequency);
}

int32 CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)
{
  return RFmxCDMA2k_CfgIQPowerEdgeTrigger(instrumentHandle, selectorString, iqPowerEdgeSource, iqPowerEdgeSlope, iqPowerEdgeLevel, triggerDelay, minimumQuietTimeMode, minimumQuietTime, iqPowerEdgeLevelType, enableTrigger);
}

int32 CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)
{
  return RFmxCDMA2k_CfgMechanicalAttenuation(instrumentHandle, channelName, mechanicalAttenuationAuto, mechanicalAttenuationValue);
}

int32 CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)
{
  return RFmxCDMA2k_CfgNumberOfChannels(instrumentHandle, selectorString, numberOfChannels);
}

int32 CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)
{
  return RFmxCDMA2k_CfgRF(instrumentHandle, selectorString, centerFrequency, referenceLevel, externalAttenuation);
}

int32 CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)
{
  return RFmxCDMA2k_CfgRFAttenuation(instrumentHandle, channelName, rfAttenuationAuto, rfAttenuationValue);
}

int32 CfgRadioConfiguration(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration)
{
  return RFmxCDMA2k_CfgRadioConfiguration(instrumentHandle, selectorString, radioConfiguration);
}

int32 CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)
{
  return RFmxCDMA2k_CfgReferenceLevel(instrumentHandle, selectorString, referenceLevel);
}

int32 CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)
{
  return RFmxCDMA2k_CfgSoftwareEdgeTrigger(instrumentHandle, selectorString, triggerDelay, enableTrigger);
}

int32 CfgUplinkSpreading(niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask)
{
  return RFmxCDMA2k_CfgUplinkSpreading(instrumentHandle, selectorString, uplinkSpreadingLongCodeMask);
}

int32 CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)
{
  return RFmxCDMA2k_CfgUserDefinedChannel(instrumentHandle, selectorString, walshCodeLength, walshCodeNumber, branch);
}

int32 CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 branch[], int32 numberOfElements)
{
  return RFmxCDMA2k_CfgUserDefinedChannelArray(instrumentHandle, selectorString, walshCodeLength, walshCodeNumber, branch, numberOfElements);
}

int32 CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* done)
{
  return RFmxCDMA2k_CheckMeasurementStatus(instrumentHandle, selectorString, done);
}

int32 ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxCDMA2k_ClearAllNamedResults(instrumentHandle, selectorString);
}

int32 ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxCDMA2k_ClearNamedResult(instrumentHandle, selectorString);
}

int32 CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])
{
  return RFmxCDMA2k_CloneSignalConfiguration(instrumentHandle, oldSignalName, newSignalName);
}

int32 Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)
{
  return RFmxCDMA2k_Close(instrumentHandle, forceDestroy);
}

int32 Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxCDMA2k_Commit(instrumentHandle, selectorString);
}

int32 CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  return RFmxCDMA2k_CreateSignalConfiguration(instrumentHandle, signalName);
}

int32 DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  return RFmxCDMA2k_DeleteSignalConfiguration(instrumentHandle, signalName);
}

int32 DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxCDMA2k_DisableTrigger(instrumentHandle, selectorString);
}

int32 GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists)
{
  return RFmxCDMA2k_GetAllNamedResultNames(instrumentHandle, selectorString, resultNames, resultNamesBufferSize, actualResultNamesSize, defaultResultExists);
}

int32 GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal)
{
  return RFmxCDMA2k_GetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal)
{
  return RFmxCDMA2k_GetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal)
{
  return RFmxCDMA2k_GetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal)
{
  return RFmxCDMA2k_GetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal)
{
  return RFmxCDMA2k_GetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal)
{
  return RFmxCDMA2k_GetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[])
{
  return RFmxCDMA2k_GetAttributeString(instrumentHandle, selectorString, attributeID, arraySize, attrVal);
}

int32 GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal)
{
  return RFmxCDMA2k_GetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal)
{
  return RFmxCDMA2k_GetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal)
{
  return RFmxCDMA2k_GetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_GetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 GetError(niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  return RFmxCDMA2k_GetError(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  return RFmxCDMA2k_GetErrorString(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 Initialize(char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession)
{
  return RFmxCDMA2k_Initialize(resourceName, optionString, handleOut, isNewSession);
}

int32 InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle* handleOut)
{
  return RFmxCDMA2k_InitializeFromNIRFSASession(nirfsaSession, handleOut);
}

int32 Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])
{
  return RFmxCDMA2k_Initiate(instrumentHandle, selectorString, resultName);
}

int32 ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  return RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchConstellationTrace(instrumentHandle, selectorString, timeout, constellation, arraySize, actualArraySize);
}

int32 ModAccFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(constellation), arraySize, actualArraySize);
}

int32 ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchConstellationTraceSplit(instrumentHandle, selectorString, timeout, constellationI, constellationQ, arraySize, actualArraySize);
}

int32 ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* detectedWalshCodeLength, int32* detectedWalshCodeNumber, int32* detectedBranch)
{
  return RFmxCDMA2k_ModAccFetchDetectedChannel(instrumentHandle, selectorString, timeout, detectedWalshCodeLength, detectedWalshCodeNumber, detectedBranch);
}

int32 ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedWalshCodeLength[], int32 detectedWalshCodeNumber[], int32 detectedBranch[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchDetectedChannelArray(instrumentHandle, selectorString, timeout, detectedWalshCodeLength, detectedWalshCodeNumber, detectedBranch, arraySize, actualArraySize);
}

int32 ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsevm, float64* peakEVM, float64* rho, float64* frequencyError, float64* chipRateError, float64* rmsMagnitudeError, float64* rmsPhaseError)
{
  return RFmxCDMA2k_ModAccFetchEVM(instrumentHandle, selectorString, timeout, rmsevm, peakEVM, rho, frequencyError, chipRateError, rmsMagnitudeError, rmsPhaseError);
}

int32 ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchEVMTrace(instrumentHandle, selectorString, timeout, x0, dx, evm, arraySize, actualArraySize);
}

int32 ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError)
{
  return RFmxCDMA2k_ModAccFetchIQImpairments(instrumentHandle, selectorString, timeout, iqOriginOffset, iqGainImbalance, iqQuadratureError);
}

int32 ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, magnitudeError, arraySize, actualArraySize);
}

int32 ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* numberOfDetectedChannels)
{
  return RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels(instrumentHandle, selectorString, timeout, numberOfDetectedChannels);
}

int32 ModAccFetchPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakActiveCDE, int32* peakActiveCDEWalshCodeLength, int32* peakActiveCDEWalshCodeNumber, int32* peakActiveCDEBranch)
{
  return RFmxCDMA2k_ModAccFetchPeakActiveCDE(instrumentHandle, selectorString, timeout, peakActiveCDE, peakActiveCDEWalshCodeLength, peakActiveCDEWalshCodeNumber, peakActiveCDEBranch);
}

int32 ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakCDE, int32* peakCDEWalshCodeNumber, int32* peakCDEBranch)
{
  return RFmxCDMA2k_ModAccFetchPeakCDE(instrumentHandle, selectorString, timeout, peakCDE, peakCDEWalshCodeNumber, peakCDEBranch);
}

int32 ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_ModAccFetchPhaseErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, phaseError, arraySize, actualArraySize);
}

int32 OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxCDMA2k_OBWCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  return RFmxCDMA2k_OBWCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxCDMA2k_OBWCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency)
{
  return RFmxCDMA2k_OBWFetchMeasurement(instrumentHandle, selectorString, timeout, occupiedBandwidth, absolutePower, startFrequency, stopFrequency);
}

int32 OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_OBWFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)
{
  return RFmxCDMA2k_QEVMCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount);
}

int32 QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)
{
  return RFmxCDMA2k_QEVMCfgMeasurementLength(instrumentHandle, selectorString, measurementLength);
}

int32 QEVMFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_QEVMFetchConstellationTrace(instrumentHandle, selectorString, timeout, constellation, arraySize, actualArraySize);
}

int32 QEVMFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_QEVMFetchConstellationTrace(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(constellation), arraySize, actualArraySize);
}

int32 QEVMFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_QEVMFetchConstellationTraceSplit(instrumentHandle, selectorString, timeout, constellationI, constellationQ, arraySize, actualArraySize);
}

int32 QEVMFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanRMSEVM, float64* maximumPeakEVM, float64* meanFrequencyError, float64* meanMagnitudeError, float64* meanPhaseError, float64* meanChipRateError)
{
  return RFmxCDMA2k_QEVMFetchEVM(instrumentHandle, selectorString, timeout, meanRMSEVM, maximumPeakEVM, meanFrequencyError, meanMagnitudeError, meanPhaseError, meanChipRateError);
}

int32 QEVMFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_QEVMFetchEVMTrace(instrumentHandle, selectorString, timeout, x0, dx, evm, arraySize, actualArraySize);
}

int32 QEVMFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanIQOriginOffset, float64* meanIQGainImbalance, float64* meanIQQuadratureError, float64* maximumIQOriginOffset, float64* maximumIQGainImbalance, float64* maximumIQQuadratureError)
{
  return RFmxCDMA2k_QEVMFetchIQImpairments(instrumentHandle, selectorString, timeout, meanIQOriginOffset, meanIQGainImbalance, meanIQQuadratureError, maximumIQOriginOffset, maximumIQGainImbalance, maximumIQQuadratureError);
}

int32 QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, magnitudeError, arraySize, actualArraySize);
}

int32 QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_QEVMFetchPhaseErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, phaseError, arraySize, actualArraySize);
}

int32 ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID)
{
  return RFmxCDMA2k_ResetAttribute(instrumentHandle, selectorString, attributeID);
}

int32 ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  return RFmxCDMA2k_ResetToDefault(instrumentHandle, selectorString);
}

int32 SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  return RFmxCDMA2k_SEMCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  return RFmxCDMA2k_SEMCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsoluteIntegratedPower)
{
  return RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower(instrumentHandle, selectorString, timeout, carrierAbsoluteIntegratedPower);
}

int32 SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  return RFmxCDMA2k_SEMFetchLowerOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SEMFetchLowerOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower)
{
  return RFmxCDMA2k_SEMFetchLowerOffsetPower(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower);
}

int32 SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SEMFetchLowerOffsetPowerArray(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower, arraySize, actualArraySize);
}

int32 SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus)
{
  return RFmxCDMA2k_SEMFetchMeasurementStatus(instrumentHandle, selectorString, timeout, measurementStatus);
}

int32 SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SEMFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, relativeMask, absoluteMask, arraySize, actualArraySize);
}

int32 SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  return RFmxCDMA2k_SEMFetchUpperOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SEMFetchUpperOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower)
{
  return RFmxCDMA2k_SEMFetchUpperOffsetPower(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower);
}

int32 SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SEMFetchUpperOffsetPowerArray(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower, arraySize, actualArraySize);
}

int32 SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)
{
  return RFmxCDMA2k_SelectMeasurements(instrumentHandle, selectorString, measurements, enableAllTraces);
}

int32 SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)
{
  return RFmxCDMA2k_SendSoftwareEdgeTrigger(instrumentHandle);
}

int32 SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal)
{
  return RFmxCDMA2k_SetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal)
{
  return RFmxCDMA2k_SetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal)
{
  return RFmxCDMA2k_SetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal)
{
  return RFmxCDMA2k_SetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal)
{
  return RFmxCDMA2k_SetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal)
{
  return RFmxCDMA2k_SetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[])
{
  return RFmxCDMA2k_SetAttributeString(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal)
{
  return RFmxCDMA2k_SetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal)
{
  return RFmxCDMA2k_SetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal)
{
  return RFmxCDMA2k_SetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize)
{
  return RFmxCDMA2k_SetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  return RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace(instrumentHandle, selectorString, timeout, x0, dx, chipPhaseErrorLinearFit, arraySize, actualArraySize);
}

int32 SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseError[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, chipPhaseError, arraySize, actualArraySize);
}

int32 SlotPhaseFetchMaximumPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* maximumPhaseDiscontinuity)
{
  return RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity(instrumentHandle, selectorString, timeout, maximumPhaseDiscontinuity);
}

int32 SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities(instrumentHandle, selectorString, timeout, slotPhaseDiscontinuity, arraySize, actualArraySize);
}

int32 SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  return RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32* actualArraySize)
{
  return RFmxCDMA2k_SlotPowerFetchPowers(instrumentHandle, selectorString, timeout, slotPower, slotPowerDelta, arraySize, actualArraySize);
}

int32 WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)
{
  return RFmxCDMA2k_WaitForAcquisitionComplete(instrumentHandle, timeout);
}

int32 WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)
{
  return RFmxCDMA2k_WaitForMeasurementComplete(instrumentHandle, selectorString, timeout);
}

}  // namespace nirfmxcdma2k_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_library.cpp sha256=8646340ada38721bee32f6cd5d210cb4843983f814f2cf287438104d6cf22c28 bytes=111355 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_library.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_library.cpp`
- sha256: `8646340ada38721bee32f6cd5d210cb4843983f814f2cf287438104d6cf22c28`
- bytes: 111355

````cpp
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the NI-rfmxcdma2k Metadata
//---------------------------------------------------------------------
#include "nirfmxcdma2k_library.h"
#include <server/shared_library.h>

#include <memory>

#if defined(_MSC_VER)
static const char* kLibraryName = "niRFmxCDMA2k.dll";
#else
static const char* kLibraryName = "libnirfmxcdma2k.so.1";
#endif

namespace nirfmxcdma2k_grpc {

NiRFmxCDMA2kLibrary::NiRFmxCDMA2kLibrary() : NiRFmxCDMA2kLibrary(std::make_shared<nidevice_grpc::SharedLibrary>()) {}

NiRFmxCDMA2kLibrary::NiRFmxCDMA2kLibrary(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library) : shared_library_(shared_library)
{
  shared_library_->set_library_name(kLibraryName);
  shared_library_->load();
  bool loaded = shared_library_->is_loaded();
  memset(&function_pointers_, 0, sizeof(function_pointers_));
  if (!loaded) {
    return;
  }
  function_pointers_.ACPCfgAveraging = reinterpret_cast<ACPCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPCfgAveraging"));
  function_pointers_.ACPCfgMeasurementMethod = reinterpret_cast<ACPCfgMeasurementMethodPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPCfgMeasurementMethod"));
  function_pointers_.ACPCfgNoiseCompensationEnabled = reinterpret_cast<ACPCfgNoiseCompensationEnabledPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPCfgNoiseCompensationEnabled"));
  function_pointers_.ACPCfgNumberOfOffsets = reinterpret_cast<ACPCfgNumberOfOffsetsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPCfgNumberOfOffsets"));
  function_pointers_.ACPCfgRBWFilter = reinterpret_cast<ACPCfgRBWFilterPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPCfgRBWFilter"));
  function_pointers_.ACPCfgSweepTime = reinterpret_cast<ACPCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPCfgSweepTime"));
  function_pointers_.ACPFetchAbsolutePowersTrace = reinterpret_cast<ACPFetchAbsolutePowersTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPFetchAbsolutePowersTrace"));
  function_pointers_.ACPFetchCarrierAbsolutePower = reinterpret_cast<ACPFetchCarrierAbsolutePowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPFetchCarrierAbsolutePower"));
  function_pointers_.ACPFetchOffsetMeasurement = reinterpret_cast<ACPFetchOffsetMeasurementPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPFetchOffsetMeasurement"));
  function_pointers_.ACPFetchOffsetMeasurementArray = reinterpret_cast<ACPFetchOffsetMeasurementArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPFetchOffsetMeasurementArray"));
  function_pointers_.ACPFetchRelativePowersTrace = reinterpret_cast<ACPFetchRelativePowersTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPFetchRelativePowersTrace"));
  function_pointers_.ACPFetchSpectrum = reinterpret_cast<ACPFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ACPFetchSpectrum"));
  function_pointers_.AbortMeasurements = reinterpret_cast<AbortMeasurementsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_AbortMeasurements"));
  function_pointers_.AnalyzeIQ1Waveform = reinterpret_cast<AnalyzeIQ1WaveformPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_AnalyzeIQ1Waveform"));
  function_pointers_.AnalyzeIQ1WaveformInterleavedIQ = reinterpret_cast<AnalyzeIQ1WaveformInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_AnalyzeIQ1Waveform"));
  function_pointers_.AnalyzeIQ1WaveformSplit = reinterpret_cast<AnalyzeIQ1WaveformSplitPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_AnalyzeIQ1WaveformSplit"));
  function_pointers_.AnalyzeSpectrum1Waveform = reinterpret_cast<AnalyzeSpectrum1WaveformPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_AnalyzeSpectrum1Waveform"));
  function_pointers_.AutoLevel = reinterpret_cast<AutoLevelPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_AutoLevel"));
  function_pointers_.BuildChannelString = reinterpret_cast<BuildChannelStringPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_BuildChannelString"));
  function_pointers_.BuildOffsetString = reinterpret_cast<BuildOffsetStringPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_BuildOffsetString"));
  function_pointers_.BuildSignalString = reinterpret_cast<BuildSignalStringPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_BuildSignalString"));
  function_pointers_.CDACfgMeasurementChannel = reinterpret_cast<CDACfgMeasurementChannelPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDACfgMeasurementChannel"));
  function_pointers_.CDACfgPowerUnit = reinterpret_cast<CDACfgPowerUnitPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDACfgPowerUnit"));
  function_pointers_.CDACfgSynchronizationModeAndInterval = reinterpret_cast<CDACfgSynchronizationModeAndIntervalPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDACfgSynchronizationModeAndInterval"));
  function_pointers_.CDAFetchCodeDomainIAndQPower = reinterpret_cast<CDAFetchCodeDomainIAndQPowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchCodeDomainIAndQPower"));
  function_pointers_.CDAFetchCodeDomainIAndQPowerTrace = reinterpret_cast<CDAFetchCodeDomainIAndQPowerTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace"));
  function_pointers_.CDAFetchCodeDomainPower = reinterpret_cast<CDAFetchCodeDomainPowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchCodeDomainPower"));
  function_pointers_.CDAFetchIQImpairments = reinterpret_cast<CDAFetchIQImpairmentsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchIQImpairments"));
  function_pointers_.CDAFetchSymbolConstellationTrace = reinterpret_cast<CDAFetchSymbolConstellationTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolConstellationTrace"));
  function_pointers_.CDAFetchSymbolConstellationTraceInterleavedIQ = reinterpret_cast<CDAFetchSymbolConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolConstellationTrace"));
  function_pointers_.CDAFetchSymbolConstellationTraceSplit = reinterpret_cast<CDAFetchSymbolConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit"));
  function_pointers_.CDAFetchSymbolEVM = reinterpret_cast<CDAFetchSymbolEVMPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolEVM"));
  function_pointers_.CDAFetchSymbolEVMTrace = reinterpret_cast<CDAFetchSymbolEVMTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolEVMTrace"));
  function_pointers_.CDAFetchSymbolMagnitudeErrorTrace = reinterpret_cast<CDAFetchSymbolMagnitudeErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace"));
  function_pointers_.CDAFetchSymbolPhaseErrorTrace = reinterpret_cast<CDAFetchSymbolPhaseErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace"));
  function_pointers_.CDAFetchSymbolPowerTrace = reinterpret_cast<CDAFetchSymbolPowerTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CDAFetchSymbolPowerTrace"));
  function_pointers_.CHPCfgAveraging = reinterpret_cast<CHPCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CHPCfgAveraging"));
  function_pointers_.CHPCfgRBWFilter = reinterpret_cast<CHPCfgRBWFilterPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CHPCfgRBWFilter"));
  function_pointers_.CHPCfgSweepTime = reinterpret_cast<CHPCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CHPCfgSweepTime"));
  function_pointers_.CHPFetchCarrierAbsolutePower = reinterpret_cast<CHPFetchCarrierAbsolutePowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CHPFetchCarrierAbsolutePower"));
  function_pointers_.CHPFetchSpectrum = reinterpret_cast<CHPFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CHPFetchSpectrum"));
  function_pointers_.CfgBandClass = reinterpret_cast<CfgBandClassPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgBandClass"));
  function_pointers_.CfgChannelConfigurationMode = reinterpret_cast<CfgChannelConfigurationModePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgChannelConfigurationMode"));
  function_pointers_.CfgDigitalEdgeTrigger = reinterpret_cast<CfgDigitalEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgDigitalEdgeTrigger"));
  function_pointers_.CfgExternalAttenuation = reinterpret_cast<CfgExternalAttenuationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgExternalAttenuation"));
  function_pointers_.CfgFrequency = reinterpret_cast<CfgFrequencyPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgFrequency"));
  function_pointers_.CfgFrequencyChannelNumber = reinterpret_cast<CfgFrequencyChannelNumberPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgFrequencyChannelNumber"));
  function_pointers_.CfgFrequencyReference = reinterpret_cast<CfgFrequencyReferencePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgFrequencyReference"));
  function_pointers_.CfgIQPowerEdgeTrigger = reinterpret_cast<CfgIQPowerEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgIQPowerEdgeTrigger"));
  function_pointers_.CfgMechanicalAttenuation = reinterpret_cast<CfgMechanicalAttenuationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgMechanicalAttenuation"));
  function_pointers_.CfgNumberOfChannels = reinterpret_cast<CfgNumberOfChannelsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgNumberOfChannels"));
  function_pointers_.CfgRF = reinterpret_cast<CfgRFPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgRF"));
  function_pointers_.CfgRFAttenuation = reinterpret_cast<CfgRFAttenuationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgRFAttenuation"));
  function_pointers_.CfgRadioConfiguration = reinterpret_cast<CfgRadioConfigurationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgRadioConfiguration"));
  function_pointers_.CfgReferenceLevel = reinterpret_cast<CfgReferenceLevelPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgReferenceLevel"));
  function_pointers_.CfgSoftwareEdgeTrigger = reinterpret_cast<CfgSoftwareEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgSoftwareEdgeTrigger"));
  function_pointers_.CfgUplinkSpreading = reinterpret_cast<CfgUplinkSpreadingPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgUplinkSpreading"));
  function_pointers_.CfgUserDefinedChannel = reinterpret_cast<CfgUserDefinedChannelPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgUserDefinedChannel"));
  function_pointers_.CfgUserDefinedChannelArray = reinterpret_cast<CfgUserDefinedChannelArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CfgUserDefinedChannelArray"));
  function_pointers_.CheckMeasurementStatus = reinterpret_cast<CheckMeasurementStatusPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CheckMeasurementStatus"));
  function_pointers_.ClearAllNamedResults = reinterpret_cast<ClearAllNamedResultsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ClearAllNamedResults"));
  function_pointers_.ClearNamedResult = reinterpret_cast<ClearNamedResultPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ClearNamedResult"));
  function_pointers_.CloneSignalConfiguration = reinterpret_cast<CloneSignalConfigurationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CloneSignalConfiguration"));
  function_pointers_.Close = reinterpret_cast<ClosePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_Close"));
  function_pointers_.Commit = reinterpret_cast<CommitPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_Commit"));
  function_pointers_.CreateSignalConfiguration = reinterpret_cast<CreateSignalConfigurationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_CreateSignalConfiguration"));
  function_pointers_.DeleteSignalConfiguration = reinterpret_cast<DeleteSignalConfigurationPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_DeleteSignalConfiguration"));
  function_pointers_.DisableTrigger = reinterpret_cast<DisableTriggerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_DisableTrigger"));
  function_pointers_.GetAllNamedResultNames = reinterpret_cast<GetAllNamedResultNamesPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAllNamedResultNames"));
  function_pointers_.GetAttributeF32 = reinterpret_cast<GetAttributeF32Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeF32"));
  function_pointers_.GetAttributeF32Array = reinterpret_cast<GetAttributeF32ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeF32Array"));
  function_pointers_.GetAttributeF64 = reinterpret_cast<GetAttributeF64Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeF64"));
  function_pointers_.GetAttributeF64Array = reinterpret_cast<GetAttributeF64ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeF64Array"));
  function_pointers_.GetAttributeI16 = reinterpret_cast<GetAttributeI16Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI16"));
  function_pointers_.GetAttributeI32 = reinterpret_cast<GetAttributeI32Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI32"));
  function_pointers_.GetAttributeI32Array = reinterpret_cast<GetAttributeI32ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI32Array"));
  function_pointers_.GetAttributeI64 = reinterpret_cast<GetAttributeI64Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI64"));
  function_pointers_.GetAttributeI64Array = reinterpret_cast<GetAttributeI64ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI64Array"));
  function_pointers_.GetAttributeI8 = reinterpret_cast<GetAttributeI8Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI8"));
  function_pointers_.GetAttributeI8Array = reinterpret_cast<GetAttributeI8ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeI8Array"));
  function_pointers_.GetAttributeNIComplexDoubleArray = reinterpret_cast<GetAttributeNIComplexDoubleArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeNIComplexDoubleArray"));
  function_pointers_.GetAttributeNIComplexSingleArray = reinterpret_cast<GetAttributeNIComplexSingleArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeNIComplexSingleArray"));
  function_pointers_.GetAttributeString = reinterpret_cast<GetAttributeStringPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeString"));
  function_pointers_.GetAttributeU16 = reinterpret_cast<GetAttributeU16Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeU16"));
  function_pointers_.GetAttributeU32 = reinterpret_cast<GetAttributeU32Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeU32"));
  function_pointers_.GetAttributeU32Array = reinterpret_cast<GetAttributeU32ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeU32Array"));
  function_pointers_.GetAttributeU64Array = reinterpret_cast<GetAttributeU64ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeU64Array"));
  function_pointers_.GetAttributeU8 = reinterpret_cast<GetAttributeU8Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeU8"));
  function_pointers_.GetAttributeU8Array = reinterpret_cast<GetAttributeU8ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetAttributeU8Array"));
  function_pointers_.GetError = reinterpret_cast<GetErrorPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetError"));
  function_pointers_.GetErrorString = reinterpret_cast<GetErrorStringPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_GetErrorString"));
  function_pointers_.Initialize = reinterpret_cast<InitializePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_Initialize"));
  function_pointers_.InitializeFromNIRFSASession = reinterpret_cast<InitializeFromNIRFSASessionPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_InitializeFromNIRFSASession"));
  function_pointers_.Initiate = reinterpret_cast<InitiatePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_Initiate"));
  function_pointers_.ModAccCfgSynchronizationModeAndInterval = reinterpret_cast<ModAccCfgSynchronizationModeAndIntervalPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval"));
  function_pointers_.ModAccFetchConstellationTrace = reinterpret_cast<ModAccFetchConstellationTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchConstellationTrace"));
  function_pointers_.ModAccFetchConstellationTraceInterleavedIQ = reinterpret_cast<ModAccFetchConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchConstellationTrace"));
  function_pointers_.ModAccFetchConstellationTraceSplit = reinterpret_cast<ModAccFetchConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchConstellationTraceSplit"));
  function_pointers_.ModAccFetchDetectedChannel = reinterpret_cast<ModAccFetchDetectedChannelPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchDetectedChannel"));
  function_pointers_.ModAccFetchDetectedChannelArray = reinterpret_cast<ModAccFetchDetectedChannelArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchDetectedChannelArray"));
  function_pointers_.ModAccFetchEVM = reinterpret_cast<ModAccFetchEVMPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchEVM"));
  function_pointers_.ModAccFetchEVMTrace = reinterpret_cast<ModAccFetchEVMTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchEVMTrace"));
  function_pointers_.ModAccFetchIQImpairments = reinterpret_cast<ModAccFetchIQImpairmentsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchIQImpairments"));
  function_pointers_.ModAccFetchMagnitudeErrorTrace = reinterpret_cast<ModAccFetchMagnitudeErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace"));
  function_pointers_.ModAccFetchNumberOfDetectedChannels = reinterpret_cast<ModAccFetchNumberOfDetectedChannelsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels"));
  function_pointers_.ModAccFetchPeakActiveCDE = reinterpret_cast<ModAccFetchPeakActiveCDEPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchPeakActiveCDE"));
  function_pointers_.ModAccFetchPeakCDE = reinterpret_cast<ModAccFetchPeakCDEPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchPeakCDE"));
  function_pointers_.ModAccFetchPhaseErrorTrace = reinterpret_cast<ModAccFetchPhaseErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ModAccFetchPhaseErrorTrace"));
  function_pointers_.OBWCfgAveraging = reinterpret_cast<OBWCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_OBWCfgAveraging"));
  function_pointers_.OBWCfgRBWFilter = reinterpret_cast<OBWCfgRBWFilterPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_OBWCfgRBWFilter"));
  function_pointers_.OBWCfgSweepTime = reinterpret_cast<OBWCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_OBWCfgSweepTime"));
  function_pointers_.OBWFetchMeasurement = reinterpret_cast<OBWFetchMeasurementPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_OBWFetchMeasurement"));
  function_pointers_.OBWFetchSpectrum = reinterpret_cast<OBWFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_OBWFetchSpectrum"));
  function_pointers_.QEVMCfgAveraging = reinterpret_cast<QEVMCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMCfgAveraging"));
  function_pointers_.QEVMCfgMeasurementLength = reinterpret_cast<QEVMCfgMeasurementLengthPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMCfgMeasurementLength"));
  function_pointers_.QEVMFetchConstellationTrace = reinterpret_cast<QEVMFetchConstellationTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchConstellationTrace"));
  function_pointers_.QEVMFetchConstellationTraceInterleavedIQ = reinterpret_cast<QEVMFetchConstellationTraceInterleavedIQPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchConstellationTrace"));
  function_pointers_.QEVMFetchConstellationTraceSplit = reinterpret_cast<QEVMFetchConstellationTraceSplitPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchConstellationTraceSplit"));
  function_pointers_.QEVMFetchEVM = reinterpret_cast<QEVMFetchEVMPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchEVM"));
  function_pointers_.QEVMFetchEVMTrace = reinterpret_cast<QEVMFetchEVMTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchEVMTrace"));
  function_pointers_.QEVMFetchIQImpairments = reinterpret_cast<QEVMFetchIQImpairmentsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchIQImpairments"));
  function_pointers_.QEVMFetchMagnitudeErrorTrace = reinterpret_cast<QEVMFetchMagnitudeErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace"));
  function_pointers_.QEVMFetchPhaseErrorTrace = reinterpret_cast<QEVMFetchPhaseErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_QEVMFetchPhaseErrorTrace"));
  function_pointers_.ResetAttribute = reinterpret_cast<ResetAttributePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ResetAttribute"));
  function_pointers_.ResetToDefault = reinterpret_cast<ResetToDefaultPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_ResetToDefault"));
  function_pointers_.SEMCfgAveraging = reinterpret_cast<SEMCfgAveragingPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMCfgAveraging"));
  function_pointers_.SEMCfgSweepTime = reinterpret_cast<SEMCfgSweepTimePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMCfgSweepTime"));
  function_pointers_.SEMFetchCarrierAbsoluteIntegratedPower = reinterpret_cast<SEMFetchCarrierAbsoluteIntegratedPowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower"));
  function_pointers_.SEMFetchLowerOffsetMargin = reinterpret_cast<SEMFetchLowerOffsetMarginPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchLowerOffsetMargin"));
  function_pointers_.SEMFetchLowerOffsetMarginArray = reinterpret_cast<SEMFetchLowerOffsetMarginArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchLowerOffsetMarginArray"));
  function_pointers_.SEMFetchLowerOffsetPower = reinterpret_cast<SEMFetchLowerOffsetPowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchLowerOffsetPower"));
  function_pointers_.SEMFetchLowerOffsetPowerArray = reinterpret_cast<SEMFetchLowerOffsetPowerArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchLowerOffsetPowerArray"));
  function_pointers_.SEMFetchMeasurementStatus = reinterpret_cast<SEMFetchMeasurementStatusPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchMeasurementStatus"));
  function_pointers_.SEMFetchSpectrum = reinterpret_cast<SEMFetchSpectrumPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchSpectrum"));
  function_pointers_.SEMFetchUpperOffsetMargin = reinterpret_cast<SEMFetchUpperOffsetMarginPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchUpperOffsetMargin"));
  function_pointers_.SEMFetchUpperOffsetMarginArray = reinterpret_cast<SEMFetchUpperOffsetMarginArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchUpperOffsetMarginArray"));
  function_pointers_.SEMFetchUpperOffsetPower = reinterpret_cast<SEMFetchUpperOffsetPowerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchUpperOffsetPower"));
  function_pointers_.SEMFetchUpperOffsetPowerArray = reinterpret_cast<SEMFetchUpperOffsetPowerArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SEMFetchUpperOffsetPowerArray"));
  function_pointers_.SelectMeasurements = reinterpret_cast<SelectMeasurementsPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SelectMeasurements"));
  function_pointers_.SendSoftwareEdgeTrigger = reinterpret_cast<SendSoftwareEdgeTriggerPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SendSoftwareEdgeTrigger"));
  function_pointers_.SetAttributeF32 = reinterpret_cast<SetAttributeF32Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeF32"));
  function_pointers_.SetAttributeF32Array = reinterpret_cast<SetAttributeF32ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeF32Array"));
  function_pointers_.SetAttributeF64 = reinterpret_cast<SetAttributeF64Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeF64"));
  function_pointers_.SetAttributeF64Array = reinterpret_cast<SetAttributeF64ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeF64Array"));
  function_pointers_.SetAttributeI16 = reinterpret_cast<SetAttributeI16Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI16"));
  function_pointers_.SetAttributeI32 = reinterpret_cast<SetAttributeI32Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI32"));
  function_pointers_.SetAttributeI32Array = reinterpret_cast<SetAttributeI32ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI32Array"));
  function_pointers_.SetAttributeI64 = reinterpret_cast<SetAttributeI64Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI64"));
  function_pointers_.SetAttributeI64Array = reinterpret_cast<SetAttributeI64ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI64Array"));
  function_pointers_.SetAttributeI8 = reinterpret_cast<SetAttributeI8Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI8"));
  function_pointers_.SetAttributeI8Array = reinterpret_cast<SetAttributeI8ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeI8Array"));
  function_pointers_.SetAttributeNIComplexDoubleArray = reinterpret_cast<SetAttributeNIComplexDoubleArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeNIComplexDoubleArray"));
  function_pointers_.SetAttributeNIComplexSingleArray = reinterpret_cast<SetAttributeNIComplexSingleArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeNIComplexSingleArray"));
  function_pointers_.SetAttributeString = reinterpret_cast<SetAttributeStringPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeString"));
  function_pointers_.SetAttributeU16 = reinterpret_cast<SetAttributeU16Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeU16"));
  function_pointers_.SetAttributeU32 = reinterpret_cast<SetAttributeU32Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeU32"));
  function_pointers_.SetAttributeU32Array = reinterpret_cast<SetAttributeU32ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeU32Array"));
  function_pointers_.SetAttributeU64Array = reinterpret_cast<SetAttributeU64ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeU64Array"));
  function_pointers_.SetAttributeU8 = reinterpret_cast<SetAttributeU8Ptr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeU8"));
  function_pointers_.SetAttributeU8Array = reinterpret_cast<SetAttributeU8ArrayPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SetAttributeU8Array"));
  function_pointers_.SlotPhaseCfgSynchronizationModeAndInterval = reinterpret_cast<SlotPhaseCfgSynchronizationModeAndIntervalPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval"));
  function_pointers_.SlotPhaseFetchChipPhaseErrorLinearFitTrace = reinterpret_cast<SlotPhaseFetchChipPhaseErrorLinearFitTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace"));
  function_pointers_.SlotPhaseFetchChipPhaseErrorTrace = reinterpret_cast<SlotPhaseFetchChipPhaseErrorTracePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace"));
  function_pointers_.SlotPhaseFetchMaximumPhaseDiscontinuity = reinterpret_cast<SlotPhaseFetchMaximumPhaseDiscontinuityPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity"));
  function_pointers_.SlotPhaseFetchPhaseDiscontinuities = reinterpret_cast<SlotPhaseFetchPhaseDiscontinuitiesPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities"));
  function_pointers_.SlotPowerCfgSynchronizationModeAndInterval = reinterpret_cast<SlotPowerCfgSynchronizationModeAndIntervalPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval"));
  function_pointers_.SlotPowerFetchPowers = reinterpret_cast<SlotPowerFetchPowersPtr>(shared_library_->get_function_pointer("RFmxCDMA2k_SlotPowerFetchPowers"));
  function_pointers_.WaitForAcquisitionComplete = reinterpret_cast<WaitForAcquisitionCompletePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_WaitForAcquisitionComplete"));
  function_pointers_.WaitForMeasurementComplete = reinterpret_cast<WaitForMeasurementCompletePtr>(shared_library_->get_function_pointer("RFmxCDMA2k_WaitForMeasurementComplete"));
}

NiRFmxCDMA2kLibrary::~NiRFmxCDMA2kLibrary()
{
}

::grpc::Status NiRFmxCDMA2kLibrary::check_function_exists(std::string functionName)
{
  return shared_library_->function_exists(functionName.c_str())
    ? ::grpc::Status::OK
    : ::grpc::Status(::grpc::NOT_FOUND, "Could not find the function " + functionName);
}

int32 NiRFmxCDMA2kLibrary::ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.ACPCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPCfgAveraging.");
  }
  return function_pointers_.ACPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxCDMA2kLibrary::ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod)
{
  if (!function_pointers_.ACPCfgMeasurementMethod) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPCfgMeasurementMethod.");
  }
  return function_pointers_.ACPCfgMeasurementMethod(instrumentHandle, selectorString, measurementMethod);
}

int32 NiRFmxCDMA2kLibrary::ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled)
{
  if (!function_pointers_.ACPCfgNoiseCompensationEnabled) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPCfgNoiseCompensationEnabled.");
  }
  return function_pointers_.ACPCfgNoiseCompensationEnabled(instrumentHandle, selectorString, noiseCompensationEnabled);
}

int32 NiRFmxCDMA2kLibrary::ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets)
{
  if (!function_pointers_.ACPCfgNumberOfOffsets) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPCfgNumberOfOffsets.");
  }
  return function_pointers_.ACPCfgNumberOfOffsets(instrumentHandle, selectorString, numberOfOffsets);
}

int32 NiRFmxCDMA2kLibrary::ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  if (!function_pointers_.ACPCfgRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPCfgRBWFilter.");
  }
  return function_pointers_.ACPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 NiRFmxCDMA2kLibrary::ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.ACPCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPCfgSweepTime.");
  }
  return function_pointers_.ACPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxCDMA2kLibrary::ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchAbsolutePowersTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPFetchAbsolutePowersTrace.");
  }
  return function_pointers_.ACPFetchAbsolutePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, absolutePowersTrace, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower)
{
  if (!function_pointers_.ACPFetchCarrierAbsolutePower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPFetchCarrierAbsolutePower.");
  }
  return function_pointers_.ACPFetchCarrierAbsolutePower(instrumentHandle, selectorString, timeout, carrierAbsolutePower);
}

int32 NiRFmxCDMA2kLibrary::ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower)
{
  if (!function_pointers_.ACPFetchOffsetMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPFetchOffsetMeasurement.");
  }
  return function_pointers_.ACPFetchOffsetMeasurement(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower);
}

int32 NiRFmxCDMA2kLibrary::ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchOffsetMeasurementArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPFetchOffsetMeasurementArray.");
  }
  return function_pointers_.ACPFetchOffsetMeasurementArray(instrumentHandle, selectorString, timeout, lowerRelativePower, upperRelativePower, lowerAbsolutePower, upperAbsolutePower, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchRelativePowersTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPFetchRelativePowersTrace.");
  }
  return function_pointers_.ACPFetchRelativePowersTrace(instrumentHandle, selectorString, timeout, traceIndex, x0, dx, relativePowersTrace, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ACPFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ACPFetchSpectrum.");
  }
  return function_pointers_.ACPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.AbortMeasurements) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_AbortMeasurements.");
  }
  return function_pointers_.AbortMeasurements(instrumentHandle, selectorString);
}

int32 NiRFmxCDMA2kLibrary::AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeIQ1Waveform) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_AnalyzeIQ1Waveform.");
  }
  return function_pointers_.AnalyzeIQ1Waveform(instrumentHandle, selectorString, resultName, x0, dx, iq, arraySize, reset, reserved);
}

int32 NiRFmxCDMA2kLibrary::AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeIQ1WaveformInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_AnalyzeIQ1Waveform.");
  }
  return function_pointers_.AnalyzeIQ1WaveformInterleavedIQ(instrumentHandle, selectorString, resultName, x0, dx, reinterpret_cast<NIComplexSingle*>(iq), arraySize/2, reset, reserved);
}

int32 NiRFmxCDMA2kLibrary::AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeIQ1WaveformSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_AnalyzeIQ1WaveformSplit.");
  }
  return function_pointers_.AnalyzeIQ1WaveformSplit(instrumentHandle, selectorString, resultName, x0, dx, iqi, iqq, arraySize, reset, reserved);
}

int32 NiRFmxCDMA2kLibrary::AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved)
{
  if (!function_pointers_.AnalyzeSpectrum1Waveform) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_AnalyzeSpectrum1Waveform.");
  }
  return function_pointers_.AnalyzeSpectrum1Waveform(instrumentHandle, selectorString, resultName, x0, dx, spectrum, arraySize, reset, reserved);
}

int32 NiRFmxCDMA2kLibrary::AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel)
{
  if (!function_pointers_.AutoLevel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_AutoLevel.");
  }
  return function_pointers_.AutoLevel(instrumentHandle, selectorString, measurementInterval, referenceLevel);
}

int32 NiRFmxCDMA2kLibrary::BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildChannelString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_BuildChannelString.");
  }
  return function_pointers_.BuildChannelString(selectorString, channelNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxCDMA2kLibrary::BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[])
{
  if (!function_pointers_.BuildOffsetString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_BuildOffsetString.");
  }
  return function_pointers_.BuildOffsetString(selectorString, offsetNumber, selectorStringOutLength, selectorStringOut);
}

int32 NiRFmxCDMA2kLibrary::BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[])
{
  if (!function_pointers_.BuildSignalString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_BuildSignalString.");
  }
  return function_pointers_.BuildSignalString(signalName, resultName, selectorStringLength, selectorString);
}

int32 NiRFmxCDMA2kLibrary::CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)
{
  if (!function_pointers_.CDACfgMeasurementChannel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDACfgMeasurementChannel.");
  }
  return function_pointers_.CDACfgMeasurementChannel(instrumentHandle, selectorString, walshCodeLength, walshCodeNumber, branch);
}

int32 NiRFmxCDMA2kLibrary::CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit)
{
  if (!function_pointers_.CDACfgPowerUnit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDACfgPowerUnit.");
  }
  return function_pointers_.CDACfgPowerUnit(instrumentHandle, selectorString, powerUnit);
}

int32 NiRFmxCDMA2kLibrary::CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  if (!function_pointers_.CDACfgSynchronizationModeAndInterval) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDACfgSynchronizationModeAndInterval.");
  }
  return function_pointers_.CDACfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iMeanActivePower, float64* qMeanActivePower, float64* iPeakInactivePower, float64* qPeakInactivePower)
{
  if (!function_pointers_.CDAFetchCodeDomainIAndQPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchCodeDomainIAndQPower.");
  }
  return function_pointers_.CDAFetchCodeDomainIAndQPower(instrumentHandle, selectorString, timeout, iMeanActivePower, qMeanActivePower, iPeakInactivePower, qPeakInactivePower);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchCodeDomainIAndQPowerTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace.");
  }
  return function_pointers_.CDAFetchCodeDomainIAndQPowerTrace(instrumentHandle, selectorString, timeout, iCodeDomainPowers, qCodeDomainPowers, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalPower, float64* totalActivePower, float64* meanActivePower, float64* peakActivePower, float64* meanInactivePower, float64* peakInactivePower)
{
  if (!function_pointers_.CDAFetchCodeDomainPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchCodeDomainPower.");
  }
  return function_pointers_.CDAFetchCodeDomainPower(instrumentHandle, selectorString, timeout, totalPower, totalActivePower, meanActivePower, peakActivePower, meanInactivePower, peakInactivePower);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError)
{
  if (!function_pointers_.CDAFetchIQImpairments) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchIQImpairments.");
  }
  return function_pointers_.CDAFetchIQImpairments(instrumentHandle, selectorString, timeout, iqOriginOffset, iqGainImbalance, iqQuadratureError);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolConstellationTrace.");
  }
  return function_pointers_.CDAFetchSymbolConstellationTrace(instrumentHandle, selectorString, timeout, symbolConstellation, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolConstellationTrace.");
  }
  return function_pointers_.CDAFetchSymbolConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(symbolConstellation), arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit.");
  }
  return function_pointers_.CDAFetchSymbolConstellationTraceSplit(instrumentHandle, selectorString, timeout, symbolConstellationI, symbolConstellationQ, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsSymbolEVM, float64* peakSymbolEVM, float64* rmsSymbolMagnitudeError, float64* rmsSymbolPhaseError, float64* meanSymbolPower, float64* frequencyError, float64* chipRateError)
{
  if (!function_pointers_.CDAFetchSymbolEVM) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolEVM.");
  }
  return function_pointers_.CDAFetchSymbolEVM(instrumentHandle, selectorString, timeout, rmsSymbolEVM, peakSymbolEVM, rmsSymbolMagnitudeError, rmsSymbolPhaseError, meanSymbolPower, frequencyError, chipRateError);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolEVMTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolEVMTrace.");
  }
  return function_pointers_.CDAFetchSymbolEVMTrace(instrumentHandle, selectorString, timeout, symbolEVM, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolMagnitudeErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace.");
  }
  return function_pointers_.CDAFetchSymbolMagnitudeErrorTrace(instrumentHandle, selectorString, timeout, symbolMagnitudeError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolPhaseErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace.");
  }
  return function_pointers_.CDAFetchSymbolPhaseErrorTrace(instrumentHandle, selectorString, timeout, symbolPhaseError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CDAFetchSymbolPowerTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CDAFetchSymbolPowerTrace.");
  }
  return function_pointers_.CDAFetchSymbolPowerTrace(instrumentHandle, selectorString, timeout, symbolPowers, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.CHPCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CHPCfgAveraging.");
  }
  return function_pointers_.CHPCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxCDMA2kLibrary::CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  if (!function_pointers_.CHPCfgRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CHPCfgRBWFilter.");
  }
  return function_pointers_.CHPCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 NiRFmxCDMA2kLibrary::CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.CHPCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CHPCfgSweepTime.");
  }
  return function_pointers_.CHPCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxCDMA2kLibrary::CHPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower)
{
  if (!function_pointers_.CHPFetchCarrierAbsolutePower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CHPFetchCarrierAbsolutePower.");
  }
  return function_pointers_.CHPFetchCarrierAbsolutePower(instrumentHandle, selectorString, timeout, carrierAbsolutePower);
}

int32 NiRFmxCDMA2kLibrary::CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.CHPFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CHPFetchSpectrum.");
  }
  return function_pointers_.CHPFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::CfgBandClass(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass)
{
  if (!function_pointers_.CfgBandClass) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgBandClass.");
  }
  return function_pointers_.CfgBandClass(instrumentHandle, selectorString, bandClass);
}

int32 NiRFmxCDMA2kLibrary::CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode)
{
  if (!function_pointers_.CfgChannelConfigurationMode) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgChannelConfigurationMode.");
  }
  return function_pointers_.CfgChannelConfigurationMode(instrumentHandle, selectorString, channelConfigurationMode);
}

int32 NiRFmxCDMA2kLibrary::CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger)
{
  if (!function_pointers_.CfgDigitalEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgDigitalEdgeTrigger.");
  }
  return function_pointers_.CfgDigitalEdgeTrigger(instrumentHandle, selectorString, digitalEdgeSource, digitalEdge, triggerDelay, enableTrigger);
}

int32 NiRFmxCDMA2kLibrary::CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation)
{
  if (!function_pointers_.CfgExternalAttenuation) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgExternalAttenuation.");
  }
  return function_pointers_.CfgExternalAttenuation(instrumentHandle, selectorString, externalAttenuation);
}

int32 NiRFmxCDMA2kLibrary::CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency)
{
  if (!function_pointers_.CfgFrequency) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgFrequency.");
  }
  return function_pointers_.CfgFrequency(instrumentHandle, selectorString, centerFrequency);
}

int32 NiRFmxCDMA2kLibrary::CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber)
{
  if (!function_pointers_.CfgFrequencyChannelNumber) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgFrequencyChannelNumber.");
  }
  return function_pointers_.CfgFrequencyChannelNumber(instrumentHandle, selectorString, linkDirection, bandClass, channelNumber);
}

int32 NiRFmxCDMA2kLibrary::CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency)
{
  if (!function_pointers_.CfgFrequencyReference) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgFrequencyReference.");
  }
  return function_pointers_.CfgFrequencyReference(instrumentHandle, channelName, frequencyReferenceSource, frequencyReferenceFrequency);
}

int32 NiRFmxCDMA2kLibrary::CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger)
{
  if (!function_pointers_.CfgIQPowerEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgIQPowerEdgeTrigger.");
  }
  return function_pointers_.CfgIQPowerEdgeTrigger(instrumentHandle, selectorString, iqPowerEdgeSource, iqPowerEdgeSlope, iqPowerEdgeLevel, triggerDelay, minimumQuietTimeMode, minimumQuietTime, iqPowerEdgeLevelType, enableTrigger);
}

int32 NiRFmxCDMA2kLibrary::CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue)
{
  if (!function_pointers_.CfgMechanicalAttenuation) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgMechanicalAttenuation.");
  }
  return function_pointers_.CfgMechanicalAttenuation(instrumentHandle, channelName, mechanicalAttenuationAuto, mechanicalAttenuationValue);
}

int32 NiRFmxCDMA2kLibrary::CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels)
{
  if (!function_pointers_.CfgNumberOfChannels) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgNumberOfChannels.");
  }
  return function_pointers_.CfgNumberOfChannels(instrumentHandle, selectorString, numberOfChannels);
}

int32 NiRFmxCDMA2kLibrary::CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation)
{
  if (!function_pointers_.CfgRF) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgRF.");
  }
  return function_pointers_.CfgRF(instrumentHandle, selectorString, centerFrequency, referenceLevel, externalAttenuation);
}

int32 NiRFmxCDMA2kLibrary::CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue)
{
  if (!function_pointers_.CfgRFAttenuation) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgRFAttenuation.");
  }
  return function_pointers_.CfgRFAttenuation(instrumentHandle, channelName, rfAttenuationAuto, rfAttenuationValue);
}

int32 NiRFmxCDMA2kLibrary::CfgRadioConfiguration(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration)
{
  if (!function_pointers_.CfgRadioConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgRadioConfiguration.");
  }
  return function_pointers_.CfgRadioConfiguration(instrumentHandle, selectorString, radioConfiguration);
}

int32 NiRFmxCDMA2kLibrary::CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel)
{
  if (!function_pointers_.CfgReferenceLevel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgReferenceLevel.");
  }
  return function_pointers_.CfgReferenceLevel(instrumentHandle, selectorString, referenceLevel);
}

int32 NiRFmxCDMA2kLibrary::CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger)
{
  if (!function_pointers_.CfgSoftwareEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgSoftwareEdgeTrigger.");
  }
  return function_pointers_.CfgSoftwareEdgeTrigger(instrumentHandle, selectorString, triggerDelay, enableTrigger);
}

int32 NiRFmxCDMA2kLibrary::CfgUplinkSpreading(niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask)
{
  if (!function_pointers_.CfgUplinkSpreading) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgUplinkSpreading.");
  }
  return function_pointers_.CfgUplinkSpreading(instrumentHandle, selectorString, uplinkSpreadingLongCodeMask);
}

int32 NiRFmxCDMA2kLibrary::CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch)
{
  if (!function_pointers_.CfgUserDefinedChannel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgUserDefinedChannel.");
  }
  return function_pointers_.CfgUserDefinedChannel(instrumentHandle, selectorString, walshCodeLength, walshCodeNumber, branch);
}

int32 NiRFmxCDMA2kLibrary::CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 branch[], int32 numberOfElements)
{
  if (!function_pointers_.CfgUserDefinedChannelArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CfgUserDefinedChannelArray.");
  }
  return function_pointers_.CfgUserDefinedChannelArray(instrumentHandle, selectorString, walshCodeLength, walshCodeNumber, branch, numberOfElements);
}

int32 NiRFmxCDMA2kLibrary::CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* done)
{
  if (!function_pointers_.CheckMeasurementStatus) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CheckMeasurementStatus.");
  }
  return function_pointers_.CheckMeasurementStatus(instrumentHandle, selectorString, done);
}

int32 NiRFmxCDMA2kLibrary::ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ClearAllNamedResults) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ClearAllNamedResults.");
  }
  return function_pointers_.ClearAllNamedResults(instrumentHandle, selectorString);
}

int32 NiRFmxCDMA2kLibrary::ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ClearNamedResult) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ClearNamedResult.");
  }
  return function_pointers_.ClearNamedResult(instrumentHandle, selectorString);
}

int32 NiRFmxCDMA2kLibrary::CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[])
{
  if (!function_pointers_.CloneSignalConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CloneSignalConfiguration.");
  }
  return function_pointers_.CloneSignalConfiguration(instrumentHandle, oldSignalName, newSignalName);
}

int32 NiRFmxCDMA2kLibrary::Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy)
{
  if (!function_pointers_.Close) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_Close.");
  }
  return function_pointers_.Close(instrumentHandle, forceDestroy);
}

int32 NiRFmxCDMA2kLibrary::Commit(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.Commit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_Commit.");
  }
  return function_pointers_.Commit(instrumentHandle, selectorString);
}

int32 NiRFmxCDMA2kLibrary::CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  if (!function_pointers_.CreateSignalConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_CreateSignalConfiguration.");
  }
  return function_pointers_.CreateSignalConfiguration(instrumentHandle, signalName);
}

int32 NiRFmxCDMA2kLibrary::DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[])
{
  if (!function_pointers_.DeleteSignalConfiguration) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_DeleteSignalConfiguration.");
  }
  return function_pointers_.DeleteSignalConfiguration(instrumentHandle, signalName);
}

int32 NiRFmxCDMA2kLibrary::DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.DisableTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_DisableTrigger.");
  }
  return function_pointers_.DisableTrigger(instrumentHandle, selectorString);
}

int32 NiRFmxCDMA2kLibrary::GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists)
{
  if (!function_pointers_.GetAllNamedResultNames) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAllNamedResultNames.");
  }
  return function_pointers_.GetAllNamedResultNames(instrumentHandle, selectorString, resultNames, resultNamesBufferSize, actualResultNamesSize, defaultResultExists);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal)
{
  if (!function_pointers_.GetAttributeF32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeF32.");
  }
  return function_pointers_.GetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeF32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeF32Array.");
  }
  return function_pointers_.GetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal)
{
  if (!function_pointers_.GetAttributeF64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeF64.");
  }
  return function_pointers_.GetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeF64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeF64Array.");
  }
  return function_pointers_.GetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal)
{
  if (!function_pointers_.GetAttributeI16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI16.");
  }
  return function_pointers_.GetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal)
{
  if (!function_pointers_.GetAttributeI32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI32.");
  }
  return function_pointers_.GetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeI32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI32Array.");
  }
  return function_pointers_.GetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal)
{
  if (!function_pointers_.GetAttributeI64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI64.");
  }
  return function_pointers_.GetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeI64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI64Array.");
  }
  return function_pointers_.GetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal)
{
  if (!function_pointers_.GetAttributeI8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI8.");
  }
  return function_pointers_.GetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeI8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeI8Array.");
  }
  return function_pointers_.GetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeNIComplexDoubleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeNIComplexDoubleArray.");
  }
  return function_pointers_.GetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeNIComplexSingleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeNIComplexSingleArray.");
  }
  return function_pointers_.GetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[])
{
  if (!function_pointers_.GetAttributeString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeString.");
  }
  return function_pointers_.GetAttributeString(instrumentHandle, selectorString, attributeID, arraySize, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal)
{
  if (!function_pointers_.GetAttributeU16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeU16.");
  }
  return function_pointers_.GetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal)
{
  if (!function_pointers_.GetAttributeU32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeU32.");
  }
  return function_pointers_.GetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeU32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeU32Array.");
  }
  return function_pointers_.GetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeU64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeU64Array.");
  }
  return function_pointers_.GetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal)
{
  if (!function_pointers_.GetAttributeU8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeU8.");
  }
  return function_pointers_.GetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.GetAttributeU8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetAttributeU8Array.");
  }
  return function_pointers_.GetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::GetError(niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  if (!function_pointers_.GetError) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetError.");
  }
  return function_pointers_.GetError(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 NiRFmxCDMA2kLibrary::GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[])
{
  if (!function_pointers_.GetErrorString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_GetErrorString.");
  }
  return function_pointers_.GetErrorString(instrumentHandle, errorCode, errorDescriptionBufferSize, errorDescription);
}

int32 NiRFmxCDMA2kLibrary::Initialize(char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession)
{
  if (!function_pointers_.Initialize) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_Initialize.");
  }
  return function_pointers_.Initialize(resourceName, optionString, handleOut, isNewSession);
}

int32 NiRFmxCDMA2kLibrary::InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle* handleOut)
{
  if (!function_pointers_.InitializeFromNIRFSASession) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_InitializeFromNIRFSASession.");
  }
  return function_pointers_.InitializeFromNIRFSASession(nirfsaSession, handleOut);
}

int32 NiRFmxCDMA2kLibrary::Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[])
{
  if (!function_pointers_.Initiate) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_Initiate.");
  }
  return function_pointers_.Initiate(instrumentHandle, selectorString, resultName);
}

int32 NiRFmxCDMA2kLibrary::ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  if (!function_pointers_.ModAccCfgSynchronizationModeAndInterval) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval.");
  }
  return function_pointers_.ModAccCfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchConstellationTrace.");
  }
  return function_pointers_.ModAccFetchConstellationTrace(instrumentHandle, selectorString, timeout, constellation, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchConstellationTrace.");
  }
  return function_pointers_.ModAccFetchConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(constellation), arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchConstellationTraceSplit.");
  }
  return function_pointers_.ModAccFetchConstellationTraceSplit(instrumentHandle, selectorString, timeout, constellationI, constellationQ, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* detectedWalshCodeLength, int32* detectedWalshCodeNumber, int32* detectedBranch)
{
  if (!function_pointers_.ModAccFetchDetectedChannel) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchDetectedChannel.");
  }
  return function_pointers_.ModAccFetchDetectedChannel(instrumentHandle, selectorString, timeout, detectedWalshCodeLength, detectedWalshCodeNumber, detectedBranch);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedWalshCodeLength[], int32 detectedWalshCodeNumber[], int32 detectedBranch[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchDetectedChannelArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchDetectedChannelArray.");
  }
  return function_pointers_.ModAccFetchDetectedChannelArray(instrumentHandle, selectorString, timeout, detectedWalshCodeLength, detectedWalshCodeNumber, detectedBranch, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsevm, float64* peakEVM, float64* rho, float64* frequencyError, float64* chipRateError, float64* rmsMagnitudeError, float64* rmsPhaseError)
{
  if (!function_pointers_.ModAccFetchEVM) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchEVM.");
  }
  return function_pointers_.ModAccFetchEVM(instrumentHandle, selectorString, timeout, rmsevm, peakEVM, rho, frequencyError, chipRateError, rmsMagnitudeError, rmsPhaseError);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchEVMTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchEVMTrace.");
  }
  return function_pointers_.ModAccFetchEVMTrace(instrumentHandle, selectorString, timeout, x0, dx, evm, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError)
{
  if (!function_pointers_.ModAccFetchIQImpairments) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchIQImpairments.");
  }
  return function_pointers_.ModAccFetchIQImpairments(instrumentHandle, selectorString, timeout, iqOriginOffset, iqGainImbalance, iqQuadratureError);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchMagnitudeErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace.");
  }
  return function_pointers_.ModAccFetchMagnitudeErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, magnitudeError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* numberOfDetectedChannels)
{
  if (!function_pointers_.ModAccFetchNumberOfDetectedChannels) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels.");
  }
  return function_pointers_.ModAccFetchNumberOfDetectedChannels(instrumentHandle, selectorString, timeout, numberOfDetectedChannels);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakActiveCDE, int32* peakActiveCDEWalshCodeLength, int32* peakActiveCDEWalshCodeNumber, int32* peakActiveCDEBranch)
{
  if (!function_pointers_.ModAccFetchPeakActiveCDE) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchPeakActiveCDE.");
  }
  return function_pointers_.ModAccFetchPeakActiveCDE(instrumentHandle, selectorString, timeout, peakActiveCDE, peakActiveCDEWalshCodeLength, peakActiveCDEWalshCodeNumber, peakActiveCDEBranch);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakCDE, int32* peakCDEWalshCodeNumber, int32* peakCDEBranch)
{
  if (!function_pointers_.ModAccFetchPeakCDE) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchPeakCDE.");
  }
  return function_pointers_.ModAccFetchPeakCDE(instrumentHandle, selectorString, timeout, peakCDE, peakCDEWalshCodeNumber, peakCDEBranch);
}

int32 NiRFmxCDMA2kLibrary::ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.ModAccFetchPhaseErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ModAccFetchPhaseErrorTrace.");
  }
  return function_pointers_.ModAccFetchPhaseErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, phaseError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.OBWCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_OBWCfgAveraging.");
  }
  return function_pointers_.OBWCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxCDMA2kLibrary::OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType)
{
  if (!function_pointers_.OBWCfgRBWFilter) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_OBWCfgRBWFilter.");
  }
  return function_pointers_.OBWCfgRBWFilter(instrumentHandle, selectorString, rbwAuto, rbw, rbwFilterType);
}

int32 NiRFmxCDMA2kLibrary::OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.OBWCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_OBWCfgSweepTime.");
  }
  return function_pointers_.OBWCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxCDMA2kLibrary::OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency)
{
  if (!function_pointers_.OBWFetchMeasurement) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_OBWFetchMeasurement.");
  }
  return function_pointers_.OBWFetchMeasurement(instrumentHandle, selectorString, timeout, occupiedBandwidth, absolutePower, startFrequency, stopFrequency);
}

int32 NiRFmxCDMA2kLibrary::OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.OBWFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_OBWFetchSpectrum.");
  }
  return function_pointers_.OBWFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount)
{
  if (!function_pointers_.QEVMCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMCfgAveraging.");
  }
  return function_pointers_.QEVMCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount);
}

int32 NiRFmxCDMA2kLibrary::QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength)
{
  if (!function_pointers_.QEVMCfgMeasurementLength) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMCfgMeasurementLength.");
  }
  return function_pointers_.QEVMCfgMeasurementLength(instrumentHandle, selectorString, measurementLength);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.QEVMFetchConstellationTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchConstellationTrace.");
  }
  return function_pointers_.QEVMFetchConstellationTrace(instrumentHandle, selectorString, timeout, constellation, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.QEVMFetchConstellationTraceInterleavedIQ) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchConstellationTrace.");
  }
  return function_pointers_.QEVMFetchConstellationTraceInterleavedIQ(instrumentHandle, selectorString, timeout, reinterpret_cast<NIComplexSingle*>(constellation), arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.QEVMFetchConstellationTraceSplit) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchConstellationTraceSplit.");
  }
  return function_pointers_.QEVMFetchConstellationTraceSplit(instrumentHandle, selectorString, timeout, constellationI, constellationQ, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanRMSEVM, float64* maximumPeakEVM, float64* meanFrequencyError, float64* meanMagnitudeError, float64* meanPhaseError, float64* meanChipRateError)
{
  if (!function_pointers_.QEVMFetchEVM) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchEVM.");
  }
  return function_pointers_.QEVMFetchEVM(instrumentHandle, selectorString, timeout, meanRMSEVM, maximumPeakEVM, meanFrequencyError, meanMagnitudeError, meanPhaseError, meanChipRateError);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.QEVMFetchEVMTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchEVMTrace.");
  }
  return function_pointers_.QEVMFetchEVMTrace(instrumentHandle, selectorString, timeout, x0, dx, evm, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanIQOriginOffset, float64* meanIQGainImbalance, float64* meanIQQuadratureError, float64* maximumIQOriginOffset, float64* maximumIQGainImbalance, float64* maximumIQQuadratureError)
{
  if (!function_pointers_.QEVMFetchIQImpairments) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchIQImpairments.");
  }
  return function_pointers_.QEVMFetchIQImpairments(instrumentHandle, selectorString, timeout, meanIQOriginOffset, meanIQGainImbalance, meanIQQuadratureError, maximumIQOriginOffset, maximumIQGainImbalance, maximumIQQuadratureError);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.QEVMFetchMagnitudeErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace.");
  }
  return function_pointers_.QEVMFetchMagnitudeErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, magnitudeError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.QEVMFetchPhaseErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_QEVMFetchPhaseErrorTrace.");
  }
  return function_pointers_.QEVMFetchPhaseErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, phaseError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID)
{
  if (!function_pointers_.ResetAttribute) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ResetAttribute.");
  }
  return function_pointers_.ResetAttribute(instrumentHandle, selectorString, attributeID);
}

int32 NiRFmxCDMA2kLibrary::ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[])
{
  if (!function_pointers_.ResetToDefault) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_ResetToDefault.");
  }
  return function_pointers_.ResetToDefault(instrumentHandle, selectorString);
}

int32 NiRFmxCDMA2kLibrary::SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType)
{
  if (!function_pointers_.SEMCfgAveraging) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMCfgAveraging.");
  }
  return function_pointers_.SEMCfgAveraging(instrumentHandle, selectorString, averagingEnabled, averagingCount, averagingType);
}

int32 NiRFmxCDMA2kLibrary::SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval)
{
  if (!function_pointers_.SEMCfgSweepTime) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMCfgSweepTime.");
  }
  return function_pointers_.SEMCfgSweepTime(instrumentHandle, selectorString, sweepTimeAuto, sweepTimeInterval);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsoluteIntegratedPower)
{
  if (!function_pointers_.SEMFetchCarrierAbsoluteIntegratedPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower.");
  }
  return function_pointers_.SEMFetchCarrierAbsoluteIntegratedPower(instrumentHandle, selectorString, timeout, carrierAbsoluteIntegratedPower);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  if (!function_pointers_.SEMFetchLowerOffsetMargin) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchLowerOffsetMargin.");
  }
  return function_pointers_.SEMFetchLowerOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchLowerOffsetMarginArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchLowerOffsetMarginArray.");
  }
  return function_pointers_.SEMFetchLowerOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower)
{
  if (!function_pointers_.SEMFetchLowerOffsetPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchLowerOffsetPower.");
  }
  return function_pointers_.SEMFetchLowerOffsetPower(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchLowerOffsetPowerArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchLowerOffsetPowerArray.");
  }
  return function_pointers_.SEMFetchLowerOffsetPowerArray(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus)
{
  if (!function_pointers_.SEMFetchMeasurementStatus) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchMeasurementStatus.");
  }
  return function_pointers_.SEMFetchMeasurementStatus(instrumentHandle, selectorString, timeout, measurementStatus);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchSpectrum) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchSpectrum.");
  }
  return function_pointers_.SEMFetchSpectrum(instrumentHandle, selectorString, timeout, x0, dx, spectrum, relativeMask, absoluteMask, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower)
{
  if (!function_pointers_.SEMFetchUpperOffsetMargin) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchUpperOffsetMargin.");
  }
  return function_pointers_.SEMFetchUpperOffsetMargin(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchUpperOffsetMarginArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchUpperOffsetMarginArray.");
  }
  return function_pointers_.SEMFetchUpperOffsetMarginArray(instrumentHandle, selectorString, timeout, measurementStatus, margin, marginFrequency, marginAbsolutePower, marginRelativePower, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower)
{
  if (!function_pointers_.SEMFetchUpperOffsetPower) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchUpperOffsetPower.");
  }
  return function_pointers_.SEMFetchUpperOffsetPower(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower);
}

int32 NiRFmxCDMA2kLibrary::SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SEMFetchUpperOffsetPowerArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SEMFetchUpperOffsetPowerArray.");
  }
  return function_pointers_.SEMFetchUpperOffsetPowerArray(instrumentHandle, selectorString, timeout, absoluteIntegratedPower, relativeIntegratedPower, absolutePeakPower, peakFrequency, relativePeakPower, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces)
{
  if (!function_pointers_.SelectMeasurements) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SelectMeasurements.");
  }
  return function_pointers_.SelectMeasurements(instrumentHandle, selectorString, measurements, enableAllTraces);
}

int32 NiRFmxCDMA2kLibrary::SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle)
{
  if (!function_pointers_.SendSoftwareEdgeTrigger) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SendSoftwareEdgeTrigger.");
  }
  return function_pointers_.SendSoftwareEdgeTrigger(instrumentHandle);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal)
{
  if (!function_pointers_.SetAttributeF32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeF32.");
  }
  return function_pointers_.SetAttributeF32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeF32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeF32Array.");
  }
  return function_pointers_.SetAttributeF32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal)
{
  if (!function_pointers_.SetAttributeF64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeF64.");
  }
  return function_pointers_.SetAttributeF64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeF64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeF64Array.");
  }
  return function_pointers_.SetAttributeF64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal)
{
  if (!function_pointers_.SetAttributeI16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI16.");
  }
  return function_pointers_.SetAttributeI16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal)
{
  if (!function_pointers_.SetAttributeI32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI32.");
  }
  return function_pointers_.SetAttributeI32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeI32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI32Array.");
  }
  return function_pointers_.SetAttributeI32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal)
{
  if (!function_pointers_.SetAttributeI64) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI64.");
  }
  return function_pointers_.SetAttributeI64(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeI64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI64Array.");
  }
  return function_pointers_.SetAttributeI64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal)
{
  if (!function_pointers_.SetAttributeI8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI8.");
  }
  return function_pointers_.SetAttributeI8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeI8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeI8Array.");
  }
  return function_pointers_.SetAttributeI8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeNIComplexDoubleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeNIComplexDoubleArray.");
  }
  return function_pointers_.SetAttributeNIComplexDoubleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeNIComplexSingleArray) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeNIComplexSingleArray.");
  }
  return function_pointers_.SetAttributeNIComplexSingleArray(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[])
{
  if (!function_pointers_.SetAttributeString) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeString.");
  }
  return function_pointers_.SetAttributeString(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal)
{
  if (!function_pointers_.SetAttributeU16) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeU16.");
  }
  return function_pointers_.SetAttributeU16(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal)
{
  if (!function_pointers_.SetAttributeU32) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeU32.");
  }
  return function_pointers_.SetAttributeU32(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeU32Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeU32Array.");
  }
  return function_pointers_.SetAttributeU32Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeU64Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeU64Array.");
  }
  return function_pointers_.SetAttributeU64Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal)
{
  if (!function_pointers_.SetAttributeU8) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeU8.");
  }
  return function_pointers_.SetAttributeU8(instrumentHandle, selectorString, attributeID, attrVal);
}

int32 NiRFmxCDMA2kLibrary::SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize)
{
  if (!function_pointers_.SetAttributeU8Array) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SetAttributeU8Array.");
  }
  return function_pointers_.SetAttributeU8Array(instrumentHandle, selectorString, attributeID, attrVal, arraySize);
}

int32 NiRFmxCDMA2kLibrary::SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  if (!function_pointers_.SlotPhaseCfgSynchronizationModeAndInterval) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval.");
  }
  return function_pointers_.SlotPhaseCfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 NiRFmxCDMA2kLibrary::SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SlotPhaseFetchChipPhaseErrorLinearFitTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace.");
  }
  return function_pointers_.SlotPhaseFetchChipPhaseErrorLinearFitTrace(instrumentHandle, selectorString, timeout, x0, dx, chipPhaseErrorLinearFit, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseError[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SlotPhaseFetchChipPhaseErrorTrace) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace.");
  }
  return function_pointers_.SlotPhaseFetchChipPhaseErrorTrace(instrumentHandle, selectorString, timeout, x0, dx, chipPhaseError, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SlotPhaseFetchMaximumPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* maximumPhaseDiscontinuity)
{
  if (!function_pointers_.SlotPhaseFetchMaximumPhaseDiscontinuity) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity.");
  }
  return function_pointers_.SlotPhaseFetchMaximumPhaseDiscontinuity(instrumentHandle, selectorString, timeout, maximumPhaseDiscontinuity);
}

int32 NiRFmxCDMA2kLibrary::SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SlotPhaseFetchPhaseDiscontinuities) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities.");
  }
  return function_pointers_.SlotPhaseFetchPhaseDiscontinuities(instrumentHandle, selectorString, timeout, slotPhaseDiscontinuity, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength)
{
  if (!function_pointers_.SlotPowerCfgSynchronizationModeAndInterval) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval.");
  }
  return function_pointers_.SlotPowerCfgSynchronizationModeAndInterval(instrumentHandle, selectorString, synchronizationMode, measurementOffset, measurementLength);
}

int32 NiRFmxCDMA2kLibrary::SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32* actualArraySize)
{
  if (!function_pointers_.SlotPowerFetchPowers) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_SlotPowerFetchPowers.");
  }
  return function_pointers_.SlotPowerFetchPowers(instrumentHandle, selectorString, timeout, slotPower, slotPowerDelta, arraySize, actualArraySize);
}

int32 NiRFmxCDMA2kLibrary::WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout)
{
  if (!function_pointers_.WaitForAcquisitionComplete) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_WaitForAcquisitionComplete.");
  }
  return function_pointers_.WaitForAcquisitionComplete(instrumentHandle, timeout);
}

int32 NiRFmxCDMA2kLibrary::WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout)
{
  if (!function_pointers_.WaitForMeasurementComplete) {
    throw nidevice_grpc::LibraryLoadException("Could not find RFmxCDMA2k_WaitForMeasurementComplete.");
  }
  return function_pointers_.WaitForMeasurementComplete(instrumentHandle, selectorString, timeout);
}

}  // namespace nirfmxcdma2k_grpc
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_library.h sha256=6371a17f3d4b6033ad46dcf159b01c54e89f6762c856f16a1e1230c342035556 bytes=53639 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_library.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_library.h`
- sha256: `6371a17f3d4b6033ad46dcf159b01c54e89f6762c856f16a1e1230c342035556`
- bytes: 53639

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Real implementation of LibraryInterface for NI-rfmxcdma2k
//---------------------------------------------------------------------
#ifndef NIRFMXCDMA2K_GRPC_LIBRARY_H
#define NIRFMXCDMA2K_GRPC_LIBRARY_H

#include "nirfmxcdma2k_library_interface.h"

#include <server/shared_library_interface.h>

#include <memory>

namespace nirfmxcdma2k_grpc {

class NiRFmxCDMA2kLibrary : public nirfmxcdma2k_grpc::NiRFmxCDMA2kLibraryInterface {
 public:
  NiRFmxCDMA2kLibrary();
  explicit NiRFmxCDMA2kLibrary(std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library);
  virtual ~NiRFmxCDMA2kLibrary();

  ::grpc::Status check_function_exists(std::string functionName);
  int32 ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod) override;
  int32 ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled) override;
  int32 ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets) override;
  int32 ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) override;
  int32 ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower) override;
  int32 ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower) override;
  int32 ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize) override;
  int32 ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) override;
  int32 AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved) override;
  int32 AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel) override;
  int32 BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[]) override;
  int32 BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]) override;
  int32 CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch) override;
  int32 CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit) override;
  int32 CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) override;
  int32 CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iMeanActivePower, float64* qMeanActivePower, float64* iPeakInactivePower, float64* qPeakInactivePower) override;
  int32 CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalPower, float64* totalActivePower, float64* meanActivePower, float64* peakActivePower, float64* meanInactivePower, float64* peakInactivePower) override;
  int32 CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError) override;
  int32 CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchSymbolConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellation[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsSymbolEVM, float64* peakSymbolEVM, float64* rmsSymbolMagnitudeError, float64* rmsSymbolPhaseError, float64* meanSymbolPower, float64* frequencyError, float64* chipRateError) override;
  int32 CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32* actualArraySize) override;
  int32 CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32* actualArraySize) override;
  int32 CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) override;
  int32 CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 CHPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower) override;
  int32 CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) override;
  int32 CfgBandClass(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass) override;
  int32 CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode) override;
  int32 CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger) override;
  int32 CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation) override;
  int32 CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency) override;
  int32 CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber) override;
  int32 CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency) override;
  int32 CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger) override;
  int32 CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue) override;
  int32 CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels) override;
  int32 CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation) override;
  int32 CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue) override;
  int32 CfgRadioConfiguration(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration) override;
  int32 CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel) override;
  int32 CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger) override;
  int32 CfgUplinkSpreading(niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask) override;
  int32 CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch) override;
  int32 CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 branch[], int32 numberOfElements) override;
  int32 CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* done) override;
  int32 ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[]) override;
  int32 Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy) override;
  int32 Commit(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[]) override;
  int32 DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[]) override;
  int32 DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists) override;
  int32 GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal) override;
  int32 GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal) override;
  int32 GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal) override;
  int32 GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal) override;
  int32 GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal) override;
  int32 GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal) override;
  int32 GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]) override;
  int32 GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal) override;
  int32 GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal) override;
  int32 GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal) override;
  int32 GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize) override;
  int32 GetError(niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]) override;
  int32 GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]) override;
  int32 Initialize(char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession) override;
  int32 InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle* handleOut) override;
  int32 Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[]) override;
  int32 ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) override;
  int32 ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* detectedWalshCodeLength, int32* detectedWalshCodeNumber, int32* detectedBranch) override;
  int32 ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedWalshCodeLength[], int32 detectedWalshCodeNumber[], int32 detectedBranch[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsevm, float64* peakEVM, float64* rho, float64* frequencyError, float64* chipRateError, float64* rmsMagnitudeError, float64* rmsPhaseError) override;
  int32 ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError) override;
  int32 ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize) override;
  int32 ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* numberOfDetectedChannels) override;
  int32 ModAccFetchPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakActiveCDE, int32* peakActiveCDEWalshCodeLength, int32* peakActiveCDEWalshCodeNumber, int32* peakActiveCDEBranch) override;
  int32 ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakCDE, int32* peakCDEWalshCodeNumber, int32* peakCDEBranch) override;
  int32 ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize) override;
  int32 OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) override;
  int32 OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency) override;
  int32 OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) override;
  int32 QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount) override;
  int32 QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength) override;
  int32 QEVMFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 QEVMFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize) override;
  int32 QEVMFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize) override;
  int32 QEVMFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanRMSEVM, float64* maximumPeakEVM, float64* meanFrequencyError, float64* meanMagnitudeError, float64* meanPhaseError, float64* meanChipRateError) override;
  int32 QEVMFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize) override;
  int32 QEVMFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanIQOriginOffset, float64* meanIQGainImbalance, float64* meanIQQuadratureError, float64* maximumIQOriginOffset, float64* maximumIQGainImbalance, float64* maximumIQQuadratureError) override;
  int32 QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize) override;
  int32 QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize) override;
  int32 ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID) override;
  int32 ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[]) override;
  int32 SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) override;
  int32 SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) override;
  int32 SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsoluteIntegratedPower) override;
  int32 SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) override;
  int32 SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower) override;
  int32 SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus) override;
  int32 SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) override;
  int32 SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) override;
  int32 SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower) override;
  int32 SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize) override;
  int32 SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces) override;
  int32 SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle) override;
  int32 SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal) override;
  int32 SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize) override;
  int32 SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal) override;
  int32 SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize) override;
  int32 SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal) override;
  int32 SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal) override;
  int32 SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize) override;
  int32 SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal) override;
  int32 SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize) override;
  int32 SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal) override;
  int32 SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize) override;
  int32 SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize) override;
  int32 SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize) override;
  int32 SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[]) override;
  int32 SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal) override;
  int32 SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal) override;
  int32 SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize) override;
  int32 SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize) override;
  int32 SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal) override;
  int32 SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize) override;
  int32 SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) override;
  int32 SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32* actualArraySize) override;
  int32 SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseError[], int32 arraySize, int32* actualArraySize) override;
  int32 SlotPhaseFetchMaximumPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* maximumPhaseDiscontinuity) override;
  int32 SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32* actualArraySize) override;
  int32 SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) override;
  int32 SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32* actualArraySize) override;
  int32 WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout) override;
  int32 WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout) override;

 private:
  using ACPCfgAveragingPtr = decltype(&RFmxCDMA2k_ACPCfgAveraging);
  using ACPCfgMeasurementMethodPtr = decltype(&RFmxCDMA2k_ACPCfgMeasurementMethod);
  using ACPCfgNoiseCompensationEnabledPtr = decltype(&RFmxCDMA2k_ACPCfgNoiseCompensationEnabled);
  using ACPCfgNumberOfOffsetsPtr = decltype(&RFmxCDMA2k_ACPCfgNumberOfOffsets);
  using ACPCfgRBWFilterPtr = decltype(&RFmxCDMA2k_ACPCfgRBWFilter);
  using ACPCfgSweepTimePtr = decltype(&RFmxCDMA2k_ACPCfgSweepTime);
  using ACPFetchAbsolutePowersTracePtr = decltype(&RFmxCDMA2k_ACPFetchAbsolutePowersTrace);
  using ACPFetchCarrierAbsolutePowerPtr = decltype(&RFmxCDMA2k_ACPFetchCarrierAbsolutePower);
  using ACPFetchOffsetMeasurementPtr = decltype(&RFmxCDMA2k_ACPFetchOffsetMeasurement);
  using ACPFetchOffsetMeasurementArrayPtr = decltype(&RFmxCDMA2k_ACPFetchOffsetMeasurementArray);
  using ACPFetchRelativePowersTracePtr = decltype(&RFmxCDMA2k_ACPFetchRelativePowersTrace);
  using ACPFetchSpectrumPtr = decltype(&RFmxCDMA2k_ACPFetchSpectrum);
  using AbortMeasurementsPtr = decltype(&RFmxCDMA2k_AbortMeasurements);
  using AnalyzeIQ1WaveformPtr = decltype(&RFmxCDMA2k_AnalyzeIQ1Waveform);
  using AnalyzeIQ1WaveformInterleavedIQPtr = decltype(&RFmxCDMA2k_AnalyzeIQ1Waveform);
  using AnalyzeIQ1WaveformSplitPtr = decltype(&RFmxCDMA2k_AnalyzeIQ1WaveformSplit);
  using AnalyzeSpectrum1WaveformPtr = decltype(&RFmxCDMA2k_AnalyzeSpectrum1Waveform);
  using AutoLevelPtr = decltype(&RFmxCDMA2k_AutoLevel);
  using BuildChannelStringPtr = decltype(&RFmxCDMA2k_BuildChannelString);
  using BuildOffsetStringPtr = decltype(&RFmxCDMA2k_BuildOffsetString);
  using BuildSignalStringPtr = decltype(&RFmxCDMA2k_BuildSignalString);
  using CDACfgMeasurementChannelPtr = decltype(&RFmxCDMA2k_CDACfgMeasurementChannel);
  using CDACfgPowerUnitPtr = decltype(&RFmxCDMA2k_CDACfgPowerUnit);
  using CDACfgSynchronizationModeAndIntervalPtr = decltype(&RFmxCDMA2k_CDACfgSynchronizationModeAndInterval);
  using CDAFetchCodeDomainIAndQPowerPtr = decltype(&RFmxCDMA2k_CDAFetchCodeDomainIAndQPower);
  using CDAFetchCodeDomainIAndQPowerTracePtr = decltype(&RFmxCDMA2k_CDAFetchCodeDomainIAndQPowerTrace);
  using CDAFetchCodeDomainPowerPtr = decltype(&RFmxCDMA2k_CDAFetchCodeDomainPower);
  using CDAFetchIQImpairmentsPtr = decltype(&RFmxCDMA2k_CDAFetchIQImpairments);
  using CDAFetchSymbolConstellationTracePtr = decltype(&RFmxCDMA2k_CDAFetchSymbolConstellationTrace);
  using CDAFetchSymbolConstellationTraceInterleavedIQPtr = decltype(&RFmxCDMA2k_CDAFetchSymbolConstellationTrace);
  using CDAFetchSymbolConstellationTraceSplitPtr = decltype(&RFmxCDMA2k_CDAFetchSymbolConstellationTraceSplit);
  using CDAFetchSymbolEVMPtr = decltype(&RFmxCDMA2k_CDAFetchSymbolEVM);
  using CDAFetchSymbolEVMTracePtr = decltype(&RFmxCDMA2k_CDAFetchSymbolEVMTrace);
  using CDAFetchSymbolMagnitudeErrorTracePtr = decltype(&RFmxCDMA2k_CDAFetchSymbolMagnitudeErrorTrace);
  using CDAFetchSymbolPhaseErrorTracePtr = decltype(&RFmxCDMA2k_CDAFetchSymbolPhaseErrorTrace);
  using CDAFetchSymbolPowerTracePtr = decltype(&RFmxCDMA2k_CDAFetchSymbolPowerTrace);
  using CHPCfgAveragingPtr = decltype(&RFmxCDMA2k_CHPCfgAveraging);
  using CHPCfgRBWFilterPtr = decltype(&RFmxCDMA2k_CHPCfgRBWFilter);
  using CHPCfgSweepTimePtr = decltype(&RFmxCDMA2k_CHPCfgSweepTime);
  using CHPFetchCarrierAbsolutePowerPtr = decltype(&RFmxCDMA2k_CHPFetchCarrierAbsolutePower);
  using CHPFetchSpectrumPtr = decltype(&RFmxCDMA2k_CHPFetchSpectrum);
  using CfgBandClassPtr = decltype(&RFmxCDMA2k_CfgBandClass);
  using CfgChannelConfigurationModePtr = decltype(&RFmxCDMA2k_CfgChannelConfigurationMode);
  using CfgDigitalEdgeTriggerPtr = decltype(&RFmxCDMA2k_CfgDigitalEdgeTrigger);
  using CfgExternalAttenuationPtr = decltype(&RFmxCDMA2k_CfgExternalAttenuation);
  using CfgFrequencyPtr = decltype(&RFmxCDMA2k_CfgFrequency);
  using CfgFrequencyChannelNumberPtr = decltype(&RFmxCDMA2k_CfgFrequencyChannelNumber);
  using CfgFrequencyReferencePtr = decltype(&RFmxCDMA2k_CfgFrequencyReference);
  using CfgIQPowerEdgeTriggerPtr = decltype(&RFmxCDMA2k_CfgIQPowerEdgeTrigger);
  using CfgMechanicalAttenuationPtr = decltype(&RFmxCDMA2k_CfgMechanicalAttenuation);
  using CfgNumberOfChannelsPtr = decltype(&RFmxCDMA2k_CfgNumberOfChannels);
  using CfgRFPtr = decltype(&RFmxCDMA2k_CfgRF);
  using CfgRFAttenuationPtr = decltype(&RFmxCDMA2k_CfgRFAttenuation);
  using CfgRadioConfigurationPtr = decltype(&RFmxCDMA2k_CfgRadioConfiguration);
  using CfgReferenceLevelPtr = decltype(&RFmxCDMA2k_CfgReferenceLevel);
  using CfgSoftwareEdgeTriggerPtr = decltype(&RFmxCDMA2k_CfgSoftwareEdgeTrigger);
  using CfgUplinkSpreadingPtr = decltype(&RFmxCDMA2k_CfgUplinkSpreading);
  using CfgUserDefinedChannelPtr = decltype(&RFmxCDMA2k_CfgUserDefinedChannel);
  using CfgUserDefinedChannelArrayPtr = decltype(&RFmxCDMA2k_CfgUserDefinedChannelArray);
  using CheckMeasurementStatusPtr = decltype(&RFmxCDMA2k_CheckMeasurementStatus);
  using ClearAllNamedResultsPtr = decltype(&RFmxCDMA2k_ClearAllNamedResults);
  using ClearNamedResultPtr = decltype(&RFmxCDMA2k_ClearNamedResult);
  using CloneSignalConfigurationPtr = decltype(&RFmxCDMA2k_CloneSignalConfiguration);
  using ClosePtr = decltype(&RFmxCDMA2k_Close);
  using CommitPtr = decltype(&RFmxCDMA2k_Commit);
  using CreateSignalConfigurationPtr = decltype(&RFmxCDMA2k_CreateSignalConfiguration);
  using DeleteSignalConfigurationPtr = decltype(&RFmxCDMA2k_DeleteSignalConfiguration);
  using DisableTriggerPtr = decltype(&RFmxCDMA2k_DisableTrigger);
  using GetAllNamedResultNamesPtr = decltype(&RFmxCDMA2k_GetAllNamedResultNames);
  using GetAttributeF32Ptr = decltype(&RFmxCDMA2k_GetAttributeF32);
  using GetAttributeF32ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeF32Array);
  using GetAttributeF64Ptr = decltype(&RFmxCDMA2k_GetAttributeF64);
  using GetAttributeF64ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeF64Array);
  using GetAttributeI16Ptr = decltype(&RFmxCDMA2k_GetAttributeI16);
  using GetAttributeI32Ptr = decltype(&RFmxCDMA2k_GetAttributeI32);
  using GetAttributeI32ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeI32Array);
  using GetAttributeI64Ptr = decltype(&RFmxCDMA2k_GetAttributeI64);
  using GetAttributeI64ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeI64Array);
  using GetAttributeI8Ptr = decltype(&RFmxCDMA2k_GetAttributeI8);
  using GetAttributeI8ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeI8Array);
  using GetAttributeNIComplexDoubleArrayPtr = decltype(&RFmxCDMA2k_GetAttributeNIComplexDoubleArray);
  using GetAttributeNIComplexSingleArrayPtr = decltype(&RFmxCDMA2k_GetAttributeNIComplexSingleArray);
  using GetAttributeStringPtr = decltype(&RFmxCDMA2k_GetAttributeString);
  using GetAttributeU16Ptr = decltype(&RFmxCDMA2k_GetAttributeU16);
  using GetAttributeU32Ptr = decltype(&RFmxCDMA2k_GetAttributeU32);
  using GetAttributeU32ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeU32Array);
  using GetAttributeU64ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeU64Array);
  using GetAttributeU8Ptr = decltype(&RFmxCDMA2k_GetAttributeU8);
  using GetAttributeU8ArrayPtr = decltype(&RFmxCDMA2k_GetAttributeU8Array);
  using GetErrorPtr = decltype(&RFmxCDMA2k_GetError);
  using GetErrorStringPtr = decltype(&RFmxCDMA2k_GetErrorString);
  using InitializePtr = decltype(&RFmxCDMA2k_Initialize);
  using InitializeFromNIRFSASessionPtr = decltype(&RFmxCDMA2k_InitializeFromNIRFSASession);
  using InitiatePtr = decltype(&RFmxCDMA2k_Initiate);
  using ModAccCfgSynchronizationModeAndIntervalPtr = decltype(&RFmxCDMA2k_ModAccCfgSynchronizationModeAndInterval);
  using ModAccFetchConstellationTracePtr = decltype(&RFmxCDMA2k_ModAccFetchConstellationTrace);
  using ModAccFetchConstellationTraceInterleavedIQPtr = decltype(&RFmxCDMA2k_ModAccFetchConstellationTrace);
  using ModAccFetchConstellationTraceSplitPtr = decltype(&RFmxCDMA2k_ModAccFetchConstellationTraceSplit);
  using ModAccFetchDetectedChannelPtr = decltype(&RFmxCDMA2k_ModAccFetchDetectedChannel);
  using ModAccFetchDetectedChannelArrayPtr = decltype(&RFmxCDMA2k_ModAccFetchDetectedChannelArray);
  using ModAccFetchEVMPtr = decltype(&RFmxCDMA2k_ModAccFetchEVM);
  using ModAccFetchEVMTracePtr = decltype(&RFmxCDMA2k_ModAccFetchEVMTrace);
  using ModAccFetchIQImpairmentsPtr = decltype(&RFmxCDMA2k_ModAccFetchIQImpairments);
  using ModAccFetchMagnitudeErrorTracePtr = decltype(&RFmxCDMA2k_ModAccFetchMagnitudeErrorTrace);
  using ModAccFetchNumberOfDetectedChannelsPtr = decltype(&RFmxCDMA2k_ModAccFetchNumberOfDetectedChannels);
  using ModAccFetchPeakActiveCDEPtr = decltype(&RFmxCDMA2k_ModAccFetchPeakActiveCDE);
  using ModAccFetchPeakCDEPtr = decltype(&RFmxCDMA2k_ModAccFetchPeakCDE);
  using ModAccFetchPhaseErrorTracePtr = decltype(&RFmxCDMA2k_ModAccFetchPhaseErrorTrace);
  using OBWCfgAveragingPtr = decltype(&RFmxCDMA2k_OBWCfgAveraging);
  using OBWCfgRBWFilterPtr = decltype(&RFmxCDMA2k_OBWCfgRBWFilter);
  using OBWCfgSweepTimePtr = decltype(&RFmxCDMA2k_OBWCfgSweepTime);
  using OBWFetchMeasurementPtr = decltype(&RFmxCDMA2k_OBWFetchMeasurement);
  using OBWFetchSpectrumPtr = decltype(&RFmxCDMA2k_OBWFetchSpectrum);
  using QEVMCfgAveragingPtr = decltype(&RFmxCDMA2k_QEVMCfgAveraging);
  using QEVMCfgMeasurementLengthPtr = decltype(&RFmxCDMA2k_QEVMCfgMeasurementLength);
  using QEVMFetchConstellationTracePtr = decltype(&RFmxCDMA2k_QEVMFetchConstellationTrace);
  using QEVMFetchConstellationTraceInterleavedIQPtr = decltype(&RFmxCDMA2k_QEVMFetchConstellationTrace);
  using QEVMFetchConstellationTraceSplitPtr = decltype(&RFmxCDMA2k_QEVMFetchConstellationTraceSplit);
  using QEVMFetchEVMPtr = decltype(&RFmxCDMA2k_QEVMFetchEVM);
  using QEVMFetchEVMTracePtr = decltype(&RFmxCDMA2k_QEVMFetchEVMTrace);
  using QEVMFetchIQImpairmentsPtr = decltype(&RFmxCDMA2k_QEVMFetchIQImpairments);
  using QEVMFetchMagnitudeErrorTracePtr = decltype(&RFmxCDMA2k_QEVMFetchMagnitudeErrorTrace);
  using QEVMFetchPhaseErrorTracePtr = decltype(&RFmxCDMA2k_QEVMFetchPhaseErrorTrace);
  using ResetAttributePtr = decltype(&RFmxCDMA2k_ResetAttribute);
  using ResetToDefaultPtr = decltype(&RFmxCDMA2k_ResetToDefault);
  using SEMCfgAveragingPtr = decltype(&RFmxCDMA2k_SEMCfgAveraging);
  using SEMCfgSweepTimePtr = decltype(&RFmxCDMA2k_SEMCfgSweepTime);
  using SEMFetchCarrierAbsoluteIntegratedPowerPtr = decltype(&RFmxCDMA2k_SEMFetchCarrierAbsoluteIntegratedPower);
  using SEMFetchLowerOffsetMarginPtr = decltype(&RFmxCDMA2k_SEMFetchLowerOffsetMargin);
  using SEMFetchLowerOffsetMarginArrayPtr = decltype(&RFmxCDMA2k_SEMFetchLowerOffsetMarginArray);
  using SEMFetchLowerOffsetPowerPtr = decltype(&RFmxCDMA2k_SEMFetchLowerOffsetPower);
  using SEMFetchLowerOffsetPowerArrayPtr = decltype(&RFmxCDMA2k_SEMFetchLowerOffsetPowerArray);
  using SEMFetchMeasurementStatusPtr = decltype(&RFmxCDMA2k_SEMFetchMeasurementStatus);
  using SEMFetchSpectrumPtr = decltype(&RFmxCDMA2k_SEMFetchSpectrum);
  using SEMFetchUpperOffsetMarginPtr = decltype(&RFmxCDMA2k_SEMFetchUpperOffsetMargin);
  using SEMFetchUpperOffsetMarginArrayPtr = decltype(&RFmxCDMA2k_SEMFetchUpperOffsetMarginArray);
  using SEMFetchUpperOffsetPowerPtr = decltype(&RFmxCDMA2k_SEMFetchUpperOffsetPower);
  using SEMFetchUpperOffsetPowerArrayPtr = decltype(&RFmxCDMA2k_SEMFetchUpperOffsetPowerArray);
  using SelectMeasurementsPtr = decltype(&RFmxCDMA2k_SelectMeasurements);
  using SendSoftwareEdgeTriggerPtr = decltype(&RFmxCDMA2k_SendSoftwareEdgeTrigger);
  using SetAttributeF32Ptr = decltype(&RFmxCDMA2k_SetAttributeF32);
  using SetAttributeF32ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeF32Array);
  using SetAttributeF64Ptr = decltype(&RFmxCDMA2k_SetAttributeF64);
  using SetAttributeF64ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeF64Array);
  using SetAttributeI16Ptr = decltype(&RFmxCDMA2k_SetAttributeI16);
  using SetAttributeI32Ptr = decltype(&RFmxCDMA2k_SetAttributeI32);
  using SetAttributeI32ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeI32Array);
  using SetAttributeI64Ptr = decltype(&RFmxCDMA2k_SetAttributeI64);
  using SetAttributeI64ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeI64Array);
  using SetAttributeI8Ptr = decltype(&RFmxCDMA2k_SetAttributeI8);
  using SetAttributeI8ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeI8Array);
  using SetAttributeNIComplexDoubleArrayPtr = decltype(&RFmxCDMA2k_SetAttributeNIComplexDoubleArray);
  using SetAttributeNIComplexSingleArrayPtr = decltype(&RFmxCDMA2k_SetAttributeNIComplexSingleArray);
  using SetAttributeStringPtr = decltype(&RFmxCDMA2k_SetAttributeString);
  using SetAttributeU16Ptr = decltype(&RFmxCDMA2k_SetAttributeU16);
  using SetAttributeU32Ptr = decltype(&RFmxCDMA2k_SetAttributeU32);
  using SetAttributeU32ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeU32Array);
  using SetAttributeU64ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeU64Array);
  using SetAttributeU8Ptr = decltype(&RFmxCDMA2k_SetAttributeU8);
  using SetAttributeU8ArrayPtr = decltype(&RFmxCDMA2k_SetAttributeU8Array);
  using SlotPhaseCfgSynchronizationModeAndIntervalPtr = decltype(&RFmxCDMA2k_SlotPhaseCfgSynchronizationModeAndInterval);
  using SlotPhaseFetchChipPhaseErrorLinearFitTracePtr = decltype(&RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorLinearFitTrace);
  using SlotPhaseFetchChipPhaseErrorTracePtr = decltype(&RFmxCDMA2k_SlotPhaseFetchChipPhaseErrorTrace);
  using SlotPhaseFetchMaximumPhaseDiscontinuityPtr = decltype(&RFmxCDMA2k_SlotPhaseFetchMaximumPhaseDiscontinuity);
  using SlotPhaseFetchPhaseDiscontinuitiesPtr = decltype(&RFmxCDMA2k_SlotPhaseFetchPhaseDiscontinuities);
  using SlotPowerCfgSynchronizationModeAndIntervalPtr = decltype(&RFmxCDMA2k_SlotPowerCfgSynchronizationModeAndInterval);
  using SlotPowerFetchPowersPtr = decltype(&RFmxCDMA2k_SlotPowerFetchPowers);
  using WaitForAcquisitionCompletePtr = decltype(&RFmxCDMA2k_WaitForAcquisitionComplete);
  using WaitForMeasurementCompletePtr = decltype(&RFmxCDMA2k_WaitForMeasurementComplete);

  typedef struct FunctionPointers {
    ACPCfgAveragingPtr ACPCfgAveraging;
    ACPCfgMeasurementMethodPtr ACPCfgMeasurementMethod;
    ACPCfgNoiseCompensationEnabledPtr ACPCfgNoiseCompensationEnabled;
    ACPCfgNumberOfOffsetsPtr ACPCfgNumberOfOffsets;
    ACPCfgRBWFilterPtr ACPCfgRBWFilter;
    ACPCfgSweepTimePtr ACPCfgSweepTime;
    ACPFetchAbsolutePowersTracePtr ACPFetchAbsolutePowersTrace;
    ACPFetchCarrierAbsolutePowerPtr ACPFetchCarrierAbsolutePower;
    ACPFetchOffsetMeasurementPtr ACPFetchOffsetMeasurement;
    ACPFetchOffsetMeasurementArrayPtr ACPFetchOffsetMeasurementArray;
    ACPFetchRelativePowersTracePtr ACPFetchRelativePowersTrace;
    ACPFetchSpectrumPtr ACPFetchSpectrum;
    AbortMeasurementsPtr AbortMeasurements;
    AnalyzeIQ1WaveformPtr AnalyzeIQ1Waveform;
    AnalyzeIQ1WaveformInterleavedIQPtr AnalyzeIQ1WaveformInterleavedIQ;
    AnalyzeIQ1WaveformSplitPtr AnalyzeIQ1WaveformSplit;
    AnalyzeSpectrum1WaveformPtr AnalyzeSpectrum1Waveform;
    AutoLevelPtr AutoLevel;
    BuildChannelStringPtr BuildChannelString;
    BuildOffsetStringPtr BuildOffsetString;
    BuildSignalStringPtr BuildSignalString;
    CDACfgMeasurementChannelPtr CDACfgMeasurementChannel;
    CDACfgPowerUnitPtr CDACfgPowerUnit;
    CDACfgSynchronizationModeAndIntervalPtr CDACfgSynchronizationModeAndInterval;
    CDAFetchCodeDomainIAndQPowerPtr CDAFetchCodeDomainIAndQPower;
    CDAFetchCodeDomainIAndQPowerTracePtr CDAFetchCodeDomainIAndQPowerTrace;
    CDAFetchCodeDomainPowerPtr CDAFetchCodeDomainPower;
    CDAFetchIQImpairmentsPtr CDAFetchIQImpairments;
    CDAFetchSymbolConstellationTracePtr CDAFetchSymbolConstellationTrace;
    CDAFetchSymbolConstellationTraceInterleavedIQPtr CDAFetchSymbolConstellationTraceInterleavedIQ;
    CDAFetchSymbolConstellationTraceSplitPtr CDAFetchSymbolConstellationTraceSplit;
    CDAFetchSymbolEVMPtr CDAFetchSymbolEVM;
    CDAFetchSymbolEVMTracePtr CDAFetchSymbolEVMTrace;
    CDAFetchSymbolMagnitudeErrorTracePtr CDAFetchSymbolMagnitudeErrorTrace;
    CDAFetchSymbolPhaseErrorTracePtr CDAFetchSymbolPhaseErrorTrace;
    CDAFetchSymbolPowerTracePtr CDAFetchSymbolPowerTrace;
    CHPCfgAveragingPtr CHPCfgAveraging;
    CHPCfgRBWFilterPtr CHPCfgRBWFilter;
    CHPCfgSweepTimePtr CHPCfgSweepTime;
    CHPFetchCarrierAbsolutePowerPtr CHPFetchCarrierAbsolutePower;
    CHPFetchSpectrumPtr CHPFetchSpectrum;
    CfgBandClassPtr CfgBandClass;
    CfgChannelConfigurationModePtr CfgChannelConfigurationMode;
    CfgDigitalEdgeTriggerPtr CfgDigitalEdgeTrigger;
    CfgExternalAttenuationPtr CfgExternalAttenuation;
    CfgFrequencyPtr CfgFrequency;
    CfgFrequencyChannelNumberPtr CfgFrequencyChannelNumber;
    CfgFrequencyReferencePtr CfgFrequencyReference;
    CfgIQPowerEdgeTriggerPtr CfgIQPowerEdgeTrigger;
    CfgMechanicalAttenuationPtr CfgMechanicalAttenuation;
    CfgNumberOfChannelsPtr CfgNumberOfChannels;
    CfgRFPtr CfgRF;
    CfgRFAttenuationPtr CfgRFAttenuation;
    CfgRadioConfigurationPtr CfgRadioConfiguration;
    CfgReferenceLevelPtr CfgReferenceLevel;
    CfgSoftwareEdgeTriggerPtr CfgSoftwareEdgeTrigger;
    CfgUplinkSpreadingPtr CfgUplinkSpreading;
    CfgUserDefinedChannelPtr CfgUserDefinedChannel;
    CfgUserDefinedChannelArrayPtr CfgUserDefinedChannelArray;
    CheckMeasurementStatusPtr CheckMeasurementStatus;
    ClearAllNamedResultsPtr ClearAllNamedResults;
    ClearNamedResultPtr ClearNamedResult;
    CloneSignalConfigurationPtr CloneSignalConfiguration;
    ClosePtr Close;
    CommitPtr Commit;
    CreateSignalConfigurationPtr CreateSignalConfiguration;
    DeleteSignalConfigurationPtr DeleteSignalConfiguration;
    DisableTriggerPtr DisableTrigger;
    GetAllNamedResultNamesPtr GetAllNamedResultNames;
    GetAttributeF32Ptr GetAttributeF32;
    GetAttributeF32ArrayPtr GetAttributeF32Array;
    GetAttributeF64Ptr GetAttributeF64;
    GetAttributeF64ArrayPtr GetAttributeF64Array;
    GetAttributeI16Ptr GetAttributeI16;
    GetAttributeI32Ptr GetAttributeI32;
    GetAttributeI32ArrayPtr GetAttributeI32Array;
    GetAttributeI64Ptr GetAttributeI64;
    GetAttributeI64ArrayPtr GetAttributeI64Array;
    GetAttributeI8Ptr GetAttributeI8;
    GetAttributeI8ArrayPtr GetAttributeI8Array;
    GetAttributeNIComplexDoubleArrayPtr GetAttributeNIComplexDoubleArray;
    GetAttributeNIComplexSingleArrayPtr GetAttributeNIComplexSingleArray;
    GetAttributeStringPtr GetAttributeString;
    GetAttributeU16Ptr GetAttributeU16;
    GetAttributeU32Ptr GetAttributeU32;
    GetAttributeU32ArrayPtr GetAttributeU32Array;
    GetAttributeU64ArrayPtr GetAttributeU64Array;
    GetAttributeU8Ptr GetAttributeU8;
    GetAttributeU8ArrayPtr GetAttributeU8Array;
    GetErrorPtr GetError;
    GetErrorStringPtr GetErrorString;
    InitializePtr Initialize;
    InitializeFromNIRFSASessionPtr InitializeFromNIRFSASession;
    InitiatePtr Initiate;
    ModAccCfgSynchronizationModeAndIntervalPtr ModAccCfgSynchronizationModeAndInterval;
    ModAccFetchConstellationTracePtr ModAccFetchConstellationTrace;
    ModAccFetchConstellationTraceInterleavedIQPtr ModAccFetchConstellationTraceInterleavedIQ;
    ModAccFetchConstellationTraceSplitPtr ModAccFetchConstellationTraceSplit;
    ModAccFetchDetectedChannelPtr ModAccFetchDetectedChannel;
    ModAccFetchDetectedChannelArrayPtr ModAccFetchDetectedChannelArray;
    ModAccFetchEVMPtr ModAccFetchEVM;
    ModAccFetchEVMTracePtr ModAccFetchEVMTrace;
    ModAccFetchIQImpairmentsPtr ModAccFetchIQImpairments;
    ModAccFetchMagnitudeErrorTracePtr ModAccFetchMagnitudeErrorTrace;
    ModAccFetchNumberOfDetectedChannelsPtr ModAccFetchNumberOfDetectedChannels;
    ModAccFetchPeakActiveCDEPtr ModAccFetchPeakActiveCDE;
    ModAccFetchPeakCDEPtr ModAccFetchPeakCDE;
    ModAccFetchPhaseErrorTracePtr ModAccFetchPhaseErrorTrace;
    OBWCfgAveragingPtr OBWCfgAveraging;
    OBWCfgRBWFilterPtr OBWCfgRBWFilter;
    OBWCfgSweepTimePtr OBWCfgSweepTime;
    OBWFetchMeasurementPtr OBWFetchMeasurement;
    OBWFetchSpectrumPtr OBWFetchSpectrum;
    QEVMCfgAveragingPtr QEVMCfgAveraging;
    QEVMCfgMeasurementLengthPtr QEVMCfgMeasurementLength;
    QEVMFetchConstellationTracePtr QEVMFetchConstellationTrace;
    QEVMFetchConstellationTraceInterleavedIQPtr QEVMFetchConstellationTraceInterleavedIQ;
    QEVMFetchConstellationTraceSplitPtr QEVMFetchConstellationTraceSplit;
    QEVMFetchEVMPtr QEVMFetchEVM;
    QEVMFetchEVMTracePtr QEVMFetchEVMTrace;
    QEVMFetchIQImpairmentsPtr QEVMFetchIQImpairments;
    QEVMFetchMagnitudeErrorTracePtr QEVMFetchMagnitudeErrorTrace;
    QEVMFetchPhaseErrorTracePtr QEVMFetchPhaseErrorTrace;
    ResetAttributePtr ResetAttribute;
    ResetToDefaultPtr ResetToDefault;
    SEMCfgAveragingPtr SEMCfgAveraging;
    SEMCfgSweepTimePtr SEMCfgSweepTime;
    SEMFetchCarrierAbsoluteIntegratedPowerPtr SEMFetchCarrierAbsoluteIntegratedPower;
    SEMFetchLowerOffsetMarginPtr SEMFetchLowerOffsetMargin;
    SEMFetchLowerOffsetMarginArrayPtr SEMFetchLowerOffsetMarginArray;
    SEMFetchLowerOffsetPowerPtr SEMFetchLowerOffsetPower;
    SEMFetchLowerOffsetPowerArrayPtr SEMFetchLowerOffsetPowerArray;
    SEMFetchMeasurementStatusPtr SEMFetchMeasurementStatus;
    SEMFetchSpectrumPtr SEMFetchSpectrum;
    SEMFetchUpperOffsetMarginPtr SEMFetchUpperOffsetMargin;
    SEMFetchUpperOffsetMarginArrayPtr SEMFetchUpperOffsetMarginArray;
    SEMFetchUpperOffsetPowerPtr SEMFetchUpperOffsetPower;
    SEMFetchUpperOffsetPowerArrayPtr SEMFetchUpperOffsetPowerArray;
    SelectMeasurementsPtr SelectMeasurements;
    SendSoftwareEdgeTriggerPtr SendSoftwareEdgeTrigger;
    SetAttributeF32Ptr SetAttributeF32;
    SetAttributeF32ArrayPtr SetAttributeF32Array;
    SetAttributeF64Ptr SetAttributeF64;
    SetAttributeF64ArrayPtr SetAttributeF64Array;
    SetAttributeI16Ptr SetAttributeI16;
    SetAttributeI32Ptr SetAttributeI32;
    SetAttributeI32ArrayPtr SetAttributeI32Array;
    SetAttributeI64Ptr SetAttributeI64;
    SetAttributeI64ArrayPtr SetAttributeI64Array;
    SetAttributeI8Ptr SetAttributeI8;
    SetAttributeI8ArrayPtr SetAttributeI8Array;
    SetAttributeNIComplexDoubleArrayPtr SetAttributeNIComplexDoubleArray;
    SetAttributeNIComplexSingleArrayPtr SetAttributeNIComplexSingleArray;
    SetAttributeStringPtr SetAttributeString;
    SetAttributeU16Ptr SetAttributeU16;
    SetAttributeU32Ptr SetAttributeU32;
    SetAttributeU32ArrayPtr SetAttributeU32Array;
    SetAttributeU64ArrayPtr SetAttributeU64Array;
    SetAttributeU8Ptr SetAttributeU8;
    SetAttributeU8ArrayPtr SetAttributeU8Array;
    SlotPhaseCfgSynchronizationModeAndIntervalPtr SlotPhaseCfgSynchronizationModeAndInterval;
    SlotPhaseFetchChipPhaseErrorLinearFitTracePtr SlotPhaseFetchChipPhaseErrorLinearFitTrace;
    SlotPhaseFetchChipPhaseErrorTracePtr SlotPhaseFetchChipPhaseErrorTrace;
    SlotPhaseFetchMaximumPhaseDiscontinuityPtr SlotPhaseFetchMaximumPhaseDiscontinuity;
    SlotPhaseFetchPhaseDiscontinuitiesPtr SlotPhaseFetchPhaseDiscontinuities;
    SlotPowerCfgSynchronizationModeAndIntervalPtr SlotPowerCfgSynchronizationModeAndInterval;
    SlotPowerFetchPowersPtr SlotPowerFetchPowers;
    WaitForAcquisitionCompletePtr WaitForAcquisitionComplete;
    WaitForMeasurementCompletePtr WaitForMeasurementComplete;
  } FunctionLoadStatus;

  std::shared_ptr<nidevice_grpc::SharedLibraryInterface> shared_library_;
  FunctionPointers function_pointers_;
};

}  // namespace nirfmxcdma2k_grpc

#endif  // NIRFMXCDMA2K_GRPC_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_library_interface.h sha256=73a7f4a3b01f25859b40ecfcc81a8ddeeb0a25a01a08c758cdbfff035feea452 bytes=30462 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_library_interface.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_library_interface.h`
- sha256: `73a7f4a3b01f25859b40ecfcc81a8ddeeb0a25a01a08c758cdbfff035feea452`
- bytes: 30462

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Library wrapper for implementing interactions with NI-rfmxcdma2k
//---------------------------------------------------------------------
#ifndef NIRFMXCDMA2K_GRPC_LIBRARY_WRAPPER_H
#define NIRFMXCDMA2K_GRPC_LIBRARY_WRAPPER_H

#include <grpcpp/grpcpp.h>
#include <niRFmxCDMA2k.h>

namespace nirfmxcdma2k_grpc {

class NiRFmxCDMA2kLibraryInterface {
 public:
  virtual ~NiRFmxCDMA2kLibraryInterface() {}

  virtual int32 ACPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 ACPCfgMeasurementMethod(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod) = 0;
  virtual int32 ACPCfgNoiseCompensationEnabled(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled) = 0;
  virtual int32 ACPCfgNumberOfOffsets(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets) = 0;
  virtual int32 ACPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) = 0;
  virtual int32 ACPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 ACPFetchAbsolutePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower) = 0;
  virtual int32 ACPFetchOffsetMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower) = 0;
  virtual int32 ACPFetchOffsetMeasurementArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchRelativePowersTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ACPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 AbortMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 AnalyzeIQ1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AnalyzeIQ1WaveformInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AnalyzeIQ1WaveformSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AnalyzeSpectrum1Waveform(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved) = 0;
  virtual int32 AutoLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel) = 0;
  virtual int32 BuildChannelString(char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildOffsetString(char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[]) = 0;
  virtual int32 BuildSignalString(char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]) = 0;
  virtual int32 CDACfgMeasurementChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch) = 0;
  virtual int32 CDACfgPowerUnit(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit) = 0;
  virtual int32 CDACfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) = 0;
  virtual int32 CDAFetchCodeDomainIAndQPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iMeanActivePower, float64* qMeanActivePower, float64* iPeakInactivePower, float64* qPeakInactivePower) = 0;
  virtual int32 CDAFetchCodeDomainIAndQPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchCodeDomainPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalPower, float64* totalActivePower, float64* meanActivePower, float64* peakActivePower, float64* meanInactivePower, float64* peakInactivePower) = 0;
  virtual int32 CDAFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError) = 0;
  virtual int32 CDAFetchSymbolConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchSymbolConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchSymbolConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchSymbolEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsSymbolEVM, float64* peakSymbolEVM, float64* rmsSymbolMagnitudeError, float64* rmsSymbolPhaseError, float64* meanSymbolPower, float64* frequencyError, float64* chipRateError) = 0;
  virtual int32 CDAFetchSymbolEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchSymbolMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchSymbolPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CDAFetchSymbolPowerTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CHPCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 CHPCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) = 0;
  virtual int32 CHPCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 CHPFetchCarrierAbsolutePower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower) = 0;
  virtual int32 CHPFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 CfgBandClass(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass) = 0;
  virtual int32 CfgChannelConfigurationMode(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode) = 0;
  virtual int32 CfgDigitalEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger) = 0;
  virtual int32 CfgExternalAttenuation(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation) = 0;
  virtual int32 CfgFrequency(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency) = 0;
  virtual int32 CfgFrequencyChannelNumber(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber) = 0;
  virtual int32 CfgFrequencyReference(niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency) = 0;
  virtual int32 CfgIQPowerEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger) = 0;
  virtual int32 CfgMechanicalAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue) = 0;
  virtual int32 CfgNumberOfChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels) = 0;
  virtual int32 CfgRF(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation) = 0;
  virtual int32 CfgRFAttenuation(niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue) = 0;
  virtual int32 CfgRadioConfiguration(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration) = 0;
  virtual int32 CfgReferenceLevel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel) = 0;
  virtual int32 CfgSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger) = 0;
  virtual int32 CfgUplinkSpreading(niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask) = 0;
  virtual int32 CfgUserDefinedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch) = 0;
  virtual int32 CfgUserDefinedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 branch[], int32 numberOfElements) = 0;
  virtual int32 CheckMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], int32* done) = 0;
  virtual int32 ClearAllNamedResults(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 ClearNamedResult(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 CloneSignalConfiguration(niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[]) = 0;
  virtual int32 Close(niRFmxInstrHandle instrumentHandle, int32 forceDestroy) = 0;
  virtual int32 Commit(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 CreateSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[]) = 0;
  virtual int32 DeleteSignalConfiguration(niRFmxInstrHandle instrumentHandle, char signalName[]) = 0;
  virtual int32 DisableTrigger(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 GetAllNamedResultNames(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists) = 0;
  virtual int32 GetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal) = 0;
  virtual int32 GetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal) = 0;
  virtual int32 GetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal) = 0;
  virtual int32 GetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal) = 0;
  virtual int32 GetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal) = 0;
  virtual int32 GetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal) = 0;
  virtual int32 GetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]) = 0;
  virtual int32 GetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal) = 0;
  virtual int32 GetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal) = 0;
  virtual int32 GetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal) = 0;
  virtual int32 GetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 GetError(niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]) = 0;
  virtual int32 GetErrorString(niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]) = 0;
  virtual int32 Initialize(char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession) = 0;
  virtual int32 InitializeFromNIRFSASession(uInt32 nirfsaSession, niRFmxInstrHandle* handleOut) = 0;
  virtual int32 Initiate(niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[]) = 0;
  virtual int32 ModAccCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) = 0;
  virtual int32 ModAccFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchDetectedChannel(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* detectedWalshCodeLength, int32* detectedWalshCodeNumber, int32* detectedBranch) = 0;
  virtual int32 ModAccFetchDetectedChannelArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedWalshCodeLength[], int32 detectedWalshCodeNumber[], int32 detectedBranch[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsevm, float64* peakEVM, float64* rho, float64* frequencyError, float64* chipRateError, float64* rmsMagnitudeError, float64* rmsPhaseError) = 0;
  virtual int32 ModAccFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError) = 0;
  virtual int32 ModAccFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ModAccFetchNumberOfDetectedChannels(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* numberOfDetectedChannels) = 0;
  virtual int32 ModAccFetchPeakActiveCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakActiveCDE, int32* peakActiveCDEWalshCodeLength, int32* peakActiveCDEWalshCodeNumber, int32* peakActiveCDEBranch) = 0;
  virtual int32 ModAccFetchPeakCDE(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakCDE, int32* peakCDEWalshCodeNumber, int32* peakCDEBranch) = 0;
  virtual int32 ModAccFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 OBWCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 OBWCfgRBWFilter(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType) = 0;
  virtual int32 OBWCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 OBWFetchMeasurement(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency) = 0;
  virtual int32 OBWFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 QEVMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount) = 0;
  virtual int32 QEVMCfgMeasurementLength(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength) = 0;
  virtual int32 QEVMFetchConstellationTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 QEVMFetchConstellationTraceInterleavedIQ(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 QEVMFetchConstellationTraceSplit(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 QEVMFetchEVM(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanRMSEVM, float64* maximumPeakEVM, float64* meanFrequencyError, float64* meanMagnitudeError, float64* meanPhaseError, float64* meanChipRateError) = 0;
  virtual int32 QEVMFetchEVMTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 QEVMFetchIQImpairments(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanIQOriginOffset, float64* meanIQGainImbalance, float64* meanIQQuadratureError, float64* maximumIQOriginOffset, float64* maximumIQGainImbalance, float64* maximumIQQuadratureError) = 0;
  virtual int32 QEVMFetchMagnitudeErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 QEVMFetchPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 ResetAttribute(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID) = 0;
  virtual int32 ResetToDefault(niRFmxInstrHandle instrumentHandle, char selectorString[]) = 0;
  virtual int32 SEMCfgAveraging(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType) = 0;
  virtual int32 SEMCfgSweepTime(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval) = 0;
  virtual int32 SEMFetchCarrierAbsoluteIntegratedPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsoluteIntegratedPower) = 0;
  virtual int32 SEMFetchLowerOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) = 0;
  virtual int32 SEMFetchLowerOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchLowerOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower) = 0;
  virtual int32 SEMFetchLowerOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchMeasurementStatus(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus) = 0;
  virtual int32 SEMFetchSpectrum(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchUpperOffsetMargin(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower) = 0;
  virtual int32 SEMFetchUpperOffsetMarginArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SEMFetchUpperOffsetPower(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower) = 0;
  virtual int32 SEMFetchUpperOffsetPowerArray(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SelectMeasurements(niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces) = 0;
  virtual int32 SendSoftwareEdgeTrigger(niRFmxInstrHandle instrumentHandle) = 0;
  virtual int32 SetAttributeF32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal) = 0;
  virtual int32 SetAttributeF32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeF64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal) = 0;
  virtual int32 SetAttributeF64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeI16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal) = 0;
  virtual int32 SetAttributeI32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal) = 0;
  virtual int32 SetAttributeI32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeI64(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal) = 0;
  virtual int32 SetAttributeI64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeI8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal) = 0;
  virtual int32 SetAttributeI8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeNIComplexDoubleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeNIComplexSingleArray(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeString(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[]) = 0;
  virtual int32 SetAttributeU16(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal) = 0;
  virtual int32 SetAttributeU32(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal) = 0;
  virtual int32 SetAttributeU32Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeU64Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize) = 0;
  virtual int32 SetAttributeU8(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal) = 0;
  virtual int32 SetAttributeU8Array(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize) = 0;
  virtual int32 SlotPhaseCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) = 0;
  virtual int32 SlotPhaseFetchChipPhaseErrorLinearFitTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SlotPhaseFetchChipPhaseErrorTrace(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseError[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SlotPhaseFetchMaximumPhaseDiscontinuity(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* maximumPhaseDiscontinuity) = 0;
  virtual int32 SlotPhaseFetchPhaseDiscontinuities(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 SlotPowerCfgSynchronizationModeAndInterval(niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength) = 0;
  virtual int32 SlotPowerFetchPowers(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32* actualArraySize) = 0;
  virtual int32 WaitForAcquisitionComplete(niRFmxInstrHandle instrumentHandle, float64 timeout) = 0;
  virtual int32 WaitForMeasurementComplete(niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout) = 0;
};

}  // namespace nirfmxcdma2k_grpc
#endif  // NIRFMXCDMA2K_GRPC_LIBRARY_WRAPPER_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_mock_library.h sha256=7d1404304d3aa6e6b98f6f2d6416a9f02c0e41e4bcb2f70cda3921fa6417425f bytes=33235 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_mock_library.h

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_mock_library.h`
- sha256: `7d1404304d3aa6e6b98f6f2d6416a9f02c0e41e4bcb2f70cda3921fa6417425f`
- bytes: 33235

````c
//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Mock of LibraryInterface for NI-rfmxcdma2k
//---------------------------------------------------------------------
#ifndef NIRFMXCDMA2K_GRPC_MOCK_LIBRARY_H
#define NIRFMXCDMA2K_GRPC_MOCK_LIBRARY_H

#include <gmock/gmock.h>
#include <gtest/gtest.h>

#include "nirfmxcdma2k_library_interface.h"

namespace ni {
namespace tests {
namespace unit {

class NiRFmxCDMA2kMockLibrary : public nirfmxcdma2k_grpc::NiRFmxCDMA2kLibraryInterface {
 public:
  MOCK_METHOD(int32, ACPCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, ACPCfgMeasurementMethod, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementMethod), (override));
  MOCK_METHOD(int32, ACPCfgNoiseCompensationEnabled, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 noiseCompensationEnabled), (override));
  MOCK_METHOD(int32, ACPCfgNumberOfOffsets, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfOffsets), (override));
  MOCK_METHOD(int32, ACPCfgRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType), (override));
  MOCK_METHOD(int32, ACPCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, ACPFetchAbsolutePowersTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 absolutePowersTrace[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchCarrierAbsolutePower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower), (override));
  MOCK_METHOD(int32, ACPFetchOffsetMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* lowerRelativePower, float64* upperRelativePower, float64* lowerAbsolutePower, float64* upperAbsolutePower), (override));
  MOCK_METHOD(int32, ACPFetchOffsetMeasurementArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 lowerRelativePower[], float64 upperRelativePower[], float64 lowerAbsolutePower[], float64 upperAbsolutePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchRelativePowersTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 traceIndex, float64* x0, float64* dx, float32 relativePowersTrace[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ACPFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, AbortMeasurements, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, AnalyzeIQ1Waveform, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, NIComplexSingle iq[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AnalyzeIQ1WaveformInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iq[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AnalyzeIQ1WaveformSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 iqi[], float32 iqq[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AnalyzeSpectrum1Waveform, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[], float64 x0, float64 dx, float32 spectrum[], int32 arraySize, int32 reset, int64 reserved), (override));
  MOCK_METHOD(int32, AutoLevel, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 measurementInterval, float64* referenceLevel), (override));
  MOCK_METHOD(int32, BuildChannelString, (char selectorString[], int32 channelNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildOffsetString, (char selectorString[], int32 offsetNumber, int32 selectorStringOutLength, char selectorStringOut[]), (override));
  MOCK_METHOD(int32, BuildSignalString, (char signalName[], char resultName[], int32 selectorStringLength, char selectorString[]), (override));
  MOCK_METHOD(int32, CDACfgMeasurementChannel, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch), (override));
  MOCK_METHOD(int32, CDACfgPowerUnit, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 powerUnit), (override));
  MOCK_METHOD(int32, CDACfgSynchronizationModeAndInterval, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength), (override));
  MOCK_METHOD(int32, CDAFetchCodeDomainIAndQPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iMeanActivePower, float64* qMeanActivePower, float64* iPeakInactivePower, float64* qPeakInactivePower), (override));
  MOCK_METHOD(int32, CDAFetchCodeDomainIAndQPowerTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 iCodeDomainPowers[], float32 qCodeDomainPowers[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchCodeDomainPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* totalPower, float64* totalActivePower, float64* meanActivePower, float64* peakActivePower, float64* meanInactivePower, float64* peakInactivePower), (override));
  MOCK_METHOD(int32, CDAFetchIQImpairments, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError), (override));
  MOCK_METHOD(int32, CDAFetchSymbolConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle symbolConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchSymbolConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchSymbolConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolConstellationI[], float32 symbolConstellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchSymbolEVM, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsSymbolEVM, float64* peakSymbolEVM, float64* rmsSymbolMagnitudeError, float64* rmsSymbolPhaseError, float64* meanSymbolPower, float64* frequencyError, float64* chipRateError), (override));
  MOCK_METHOD(int32, CDAFetchSymbolEVMTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolEVM[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchSymbolMagnitudeErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolMagnitudeError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchSymbolPhaseErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPhaseError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CDAFetchSymbolPowerTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 symbolPowers[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CHPCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, CHPCfgRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType), (override));
  MOCK_METHOD(int32, CHPCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, CHPFetchCarrierAbsolutePower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsolutePower), (override));
  MOCK_METHOD(int32, CHPFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, CfgBandClass, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 bandClass), (override));
  MOCK_METHOD(int32, CfgChannelConfigurationMode, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 channelConfigurationMode), (override));
  MOCK_METHOD(int32, CfgDigitalEdgeTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[], char digitalEdgeSource[], int32 digitalEdge, float64 triggerDelay, int32 enableTrigger), (override));
  MOCK_METHOD(int32, CfgExternalAttenuation, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 externalAttenuation), (override));
  MOCK_METHOD(int32, CfgFrequency, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency), (override));
  MOCK_METHOD(int32, CfgFrequencyChannelNumber, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 linkDirection, int32 bandClass, int32 channelNumber), (override));
  MOCK_METHOD(int32, CfgFrequencyReference, (niRFmxInstrHandle instrumentHandle, char channelName[], char frequencyReferenceSource[], float64 frequencyReferenceFrequency), (override));
  MOCK_METHOD(int32, CfgIQPowerEdgeTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[], char iqPowerEdgeSource[], int32 iqPowerEdgeSlope, float64 iqPowerEdgeLevel, float64 triggerDelay, int32 minimumQuietTimeMode, float64 minimumQuietTime, int32 iqPowerEdgeLevelType, int32 enableTrigger), (override));
  MOCK_METHOD(int32, CfgMechanicalAttenuation, (niRFmxInstrHandle instrumentHandle, char channelName[], int32 mechanicalAttenuationAuto, float64 mechanicalAttenuationValue), (override));
  MOCK_METHOD(int32, CfgNumberOfChannels, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 numberOfChannels), (override));
  MOCK_METHOD(int32, CfgRF, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 centerFrequency, float64 referenceLevel, float64 externalAttenuation), (override));
  MOCK_METHOD(int32, CfgRFAttenuation, (niRFmxInstrHandle instrumentHandle, char channelName[], int32 rfAttenuationAuto, float64 rfAttenuationValue), (override));
  MOCK_METHOD(int32, CfgRadioConfiguration, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 radioConfiguration), (override));
  MOCK_METHOD(int32, CfgReferenceLevel, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 referenceLevel), (override));
  MOCK_METHOD(int32, CfgSoftwareEdgeTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 triggerDelay, int32 enableTrigger), (override));
  MOCK_METHOD(int32, CfgUplinkSpreading, (niRFmxInstrHandle instrumentHandle, char selectorString[], int64 uplinkSpreadingLongCodeMask), (override));
  MOCK_METHOD(int32, CfgUserDefinedChannel, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength, int32 walshCodeNumber, int32 branch), (override));
  MOCK_METHOD(int32, CfgUserDefinedChannelArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 walshCodeLength[], int32 walshCodeNumber[], int32 branch[], int32 numberOfElements), (override));
  MOCK_METHOD(int32, CheckMeasurementStatus, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32* done), (override));
  MOCK_METHOD(int32, ClearAllNamedResults, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, ClearNamedResult, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, CloneSignalConfiguration, (niRFmxInstrHandle instrumentHandle, char oldSignalName[], char newSignalName[]), (override));
  MOCK_METHOD(int32, Close, (niRFmxInstrHandle instrumentHandle, int32 forceDestroy), (override));
  MOCK_METHOD(int32, Commit, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, CreateSignalConfiguration, (niRFmxInstrHandle instrumentHandle, char signalName[]), (override));
  MOCK_METHOD(int32, DeleteSignalConfiguration, (niRFmxInstrHandle instrumentHandle, char signalName[]), (override));
  MOCK_METHOD(int32, DisableTrigger, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, GetAllNamedResultNames, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultNames[], int32 resultNamesBufferSize, int32* actualResultNamesSize, int32* defaultResultExists), (override));
  MOCK_METHOD(int32, GetAttributeF32, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeF32Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeF64, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeF64Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeI16, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeI32, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeI32Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeI64, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeI64Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeI8, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeI8Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeNIComplexDoubleArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeNIComplexSingleArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeString, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 arraySize, char attrVal[]), (override));
  MOCK_METHOD(int32, GetAttributeU16, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeU32, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeU32Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeU64Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetAttributeU8, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8* attrVal), (override));
  MOCK_METHOD(int32, GetAttributeU8Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, GetError, (niRFmxInstrHandle instrumentHandle, int32* errorCode, int32 errorDescriptionBufferSize, char errorDescription[]), (override));
  MOCK_METHOD(int32, GetErrorString, (niRFmxInstrHandle instrumentHandle, int32 errorCode, int32 errorDescriptionBufferSize, char errorDescription[]), (override));
  MOCK_METHOD(int32, Initialize, (char resourceName[], char optionString[], niRFmxInstrHandle* handleOut, int32* isNewSession), (override));
  MOCK_METHOD(int32, InitializeFromNIRFSASession, (uInt32 nirfsaSession, niRFmxInstrHandle* handleOut), (override));
  MOCK_METHOD(int32, Initiate, (niRFmxInstrHandle instrumentHandle, char selectorString[], char resultName[]), (override));
  MOCK_METHOD(int32, ModAccCfgSynchronizationModeAndInterval, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength), (override));
  MOCK_METHOD(int32, ModAccFetchConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchDetectedChannel, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* detectedWalshCodeLength, int32* detectedWalshCodeNumber, int32* detectedBranch), (override));
  MOCK_METHOD(int32, ModAccFetchDetectedChannelArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 detectedWalshCodeLength[], int32 detectedWalshCodeNumber[], int32 detectedBranch[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchEVM, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* rmsevm, float64* peakEVM, float64* rho, float64* frequencyError, float64* chipRateError, float64* rmsMagnitudeError, float64* rmsPhaseError), (override));
  MOCK_METHOD(int32, ModAccFetchEVMTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchIQImpairments, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* iqOriginOffset, float64* iqGainImbalance, float64* iqQuadratureError), (override));
  MOCK_METHOD(int32, ModAccFetchMagnitudeErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ModAccFetchNumberOfDetectedChannels, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* numberOfDetectedChannels), (override));
  MOCK_METHOD(int32, ModAccFetchPeakActiveCDE, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakActiveCDE, int32* peakActiveCDEWalshCodeLength, int32* peakActiveCDEWalshCodeNumber, int32* peakActiveCDEBranch), (override));
  MOCK_METHOD(int32, ModAccFetchPeakCDE, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* peakCDE, int32* peakCDEWalshCodeNumber, int32* peakCDEBranch), (override));
  MOCK_METHOD(int32, ModAccFetchPhaseErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, OBWCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, OBWCfgRBWFilter, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 rbwAuto, float64 rbw, int32 rbwFilterType), (override));
  MOCK_METHOD(int32, OBWCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, OBWFetchMeasurement, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* occupiedBandwidth, float64* absolutePower, float64* startFrequency, float64* stopFrequency), (override));
  MOCK_METHOD(int32, OBWFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, QEVMCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount), (override));
  MOCK_METHOD(int32, QEVMCfgMeasurementLength, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 measurementLength), (override));
  MOCK_METHOD(int32, QEVMFetchConstellationTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, NIComplexSingle constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, QEVMFetchConstellationTraceInterleavedIQ, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellation[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, QEVMFetchConstellationTraceSplit, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float32 constellationI[], float32 constellationQ[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, QEVMFetchEVM, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanRMSEVM, float64* maximumPeakEVM, float64* meanFrequencyError, float64* meanMagnitudeError, float64* meanPhaseError, float64* meanChipRateError), (override));
  MOCK_METHOD(int32, QEVMFetchEVMTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 evm[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, QEVMFetchIQImpairments, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* meanIQOriginOffset, float64* meanIQGainImbalance, float64* meanIQQuadratureError, float64* maximumIQOriginOffset, float64* maximumIQGainImbalance, float64* maximumIQQuadratureError), (override));
  MOCK_METHOD(int32, QEVMFetchMagnitudeErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 magnitudeError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, QEVMFetchPhaseErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 phaseError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, ResetAttribute, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID), (override));
  MOCK_METHOD(int32, ResetToDefault, (niRFmxInstrHandle instrumentHandle, char selectorString[]), (override));
  MOCK_METHOD(int32, SEMCfgAveraging, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 averagingEnabled, int32 averagingCount, int32 averagingType), (override));
  MOCK_METHOD(int32, SEMCfgSweepTime, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 sweepTimeAuto, float64 sweepTimeInterval), (override));
  MOCK_METHOD(int32, SEMFetchCarrierAbsoluteIntegratedPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* carrierAbsoluteIntegratedPower), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetMargin, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetMarginArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower), (override));
  MOCK_METHOD(int32, SEMFetchLowerOffsetPowerArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchMeasurementStatus, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus), (override));
  MOCK_METHOD(int32, SEMFetchSpectrum, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 spectrum[], float32 relativeMask[], float32 absoluteMask[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetMargin, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32* measurementStatus, float64* margin, float64* marginFrequency, float64* marginAbsolutePower, float64* marginRelativePower), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetMarginArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, int32 measurementStatus[], float64 margin[], float64 marginFrequency[], float64 marginAbsolutePower[], float64 marginRelativePower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetPower, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* absoluteIntegratedPower, float64* relativeIntegratedPower, float64* absolutePeakPower, float64* peakFrequency, float64* relativePeakPower), (override));
  MOCK_METHOD(int32, SEMFetchUpperOffsetPowerArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 absoluteIntegratedPower[], float64 relativeIntegratedPower[], float64 absolutePeakPower[], float64 peakFrequency[], float64 relativePeakPower[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SelectMeasurements, (niRFmxInstrHandle instrumentHandle, char selectorString[], uInt32 measurements, int32 enableAllTraces), (override));
  MOCK_METHOD(int32, SendSoftwareEdgeTrigger, (niRFmxInstrHandle instrumentHandle), (override));
  MOCK_METHOD(int32, SetAttributeF32, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeF32Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float32 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeF64, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeF64Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, float64 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeI16, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int16 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeI32, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeI32Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int32 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeI64, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeI64Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int64 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeI8, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeI8Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, int8 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeNIComplexDoubleArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexDouble attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeNIComplexSingleArray, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, NIComplexSingle attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeString, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, char attrVal[]), (override));
  MOCK_METHOD(int32, SetAttributeU16, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt16 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeU32, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeU32Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt32 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeU64Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt64 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SetAttributeU8, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal), (override));
  MOCK_METHOD(int32, SetAttributeU8Array, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 attributeID, uInt8 attrVal[], int32 arraySize), (override));
  MOCK_METHOD(int32, SlotPhaseCfgSynchronizationModeAndInterval, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength), (override));
  MOCK_METHOD(int32, SlotPhaseFetchChipPhaseErrorLinearFitTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseErrorLinearFit[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SlotPhaseFetchChipPhaseErrorTrace, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* x0, float64* dx, float32 chipPhaseError[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SlotPhaseFetchMaximumPhaseDiscontinuity, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64* maximumPhaseDiscontinuity), (override));
  MOCK_METHOD(int32, SlotPhaseFetchPhaseDiscontinuities, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPhaseDiscontinuity[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, SlotPowerCfgSynchronizationModeAndInterval, (niRFmxInstrHandle instrumentHandle, char selectorString[], int32 synchronizationMode, int32 measurementOffset, int32 measurementLength), (override));
  MOCK_METHOD(int32, SlotPowerFetchPowers, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout, float64 slotPower[], float64 slotPowerDelta[], int32 arraySize, int32* actualArraySize), (override));
  MOCK_METHOD(int32, WaitForAcquisitionComplete, (niRFmxInstrHandle instrumentHandle, float64 timeout), (override));
  MOCK_METHOD(int32, WaitForMeasurementComplete, (niRFmxInstrHandle instrumentHandle, char selectorString[], float64 timeout), (override));
};

}  // namespace unit
}  // namespace tests
}  // namespace ni
#endif  // NIRFMXCDMA2K_GRPC_MOCK_LIBRARY_H
````

<!--NI_OSS_SOURCE repo=grpc-device path=generated/nirfmxcdma2k/nirfmxcdma2k_service.cpp sha256=05fedf0bff51d1de0f23eb193fd3d25dd4129c78708f9ffb36c7ac36e2e228b4 bytes=330101 -->
## FILE: generated/nirfmxcdma2k/nirfmxcdma2k_service.cpp

- repository: `ni/grpc-device`
- source_path: `generated/nirfmxcdma2k/nirfmxcdma2k_service.cpp`
- sha256: `05fedf0bff51d1de0f23eb193fd3d25dd4129c78708f9ffb36c7ac36e2e228b4`
- bytes: 330101

````cpp

//---------------------------------------------------------------------
// This file is automatically generated. All manual edits will be lost.
//---------------------------------------------------------------------
// Service implementation for the NI-rfmxcdma2k Metadata
//---------------------------------------------------------------------
#include "nirfmxcdma2k_service.h"

#include <sstream>
#include <fstream>
#include <iostream>
#include <atomic>
#include <vector>
#include <server/converters.h>

namespace nirfmxcdma2k_grpc {

  using nidevice_grpc::converters::allocate_output_storage;
  using nidevice_grpc::converters::calculate_linked_array_size;
  using nidevice_grpc::converters::convert_from_grpc;
  using nidevice_grpc::converters::convert_to_grpc;
  using nidevice_grpc::converters::MatchState;

  const auto kErrorReadBufferTooSmall = -200229;
  const auto kWarningCAPIStringTruncatedToFitBuffer = 200026;

  NiRFmxCDMA2kService::NiRFmxCDMA2kService(
      LibrarySharedPtr library,
      ResourceRepositorySharedPtr resource_repository,
      ViSessionResourceRepositorySharedPtr vi_session_resource_repository,
      const NiRFmxCDMA2kFeatureToggles& feature_toggles)
      : library_(library),
      session_repository_(resource_repository),
      vi_session_resource_repository_(vi_session_resource_repository),
      feature_toggles_(feature_toggles)
  {
  }

  NiRFmxCDMA2kService::~NiRFmxCDMA2kService()
  {
  }

  // Returns true if it's safe to use outputs of a method with the given status.
  inline bool status_ok(int32 status)
  {
    return status >= 0;
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPCfgAveraging(::grpc::ServerContext* context, const ACPCfgAveragingRequest* request, ACPCfgAveragingResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 averaging_enabled;
      switch (request->averaging_enabled_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabled: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabledRaw: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgAveragingRequest::AveragingEnabledEnumCase::AVERAGING_ENABLED_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_enabled was not specified or out of range");
          break;
        }
      }

      int32 averaging_count = request->averaging_count();
      int32 averaging_type;
      switch (request->averaging_type_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgAveragingRequest::AveragingTypeEnumCase::kAveragingType: {
          averaging_type = static_cast<int32>(request->averaging_type());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgAveragingRequest::AveragingTypeEnumCase::kAveragingTypeRaw: {
          averaging_type = static_cast<int32>(request->averaging_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgAveragingRequest::AveragingTypeEnumCase::AVERAGING_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->ACPCfgAveraging(instrument, selector_string, averaging_enabled, averaging_count, averaging_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPCfgMeasurementMethod(::grpc::ServerContext* context, const ACPCfgMeasurementMethodRequest* request, ACPCfgMeasurementMethodResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 measurement_method;
      switch (request->measurement_method_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgMeasurementMethodRequest::MeasurementMethodEnumCase::kMeasurementMethod: {
          measurement_method = static_cast<int32>(request->measurement_method());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgMeasurementMethodRequest::MeasurementMethodEnumCase::kMeasurementMethodRaw: {
          measurement_method = static_cast<int32>(request->measurement_method_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgMeasurementMethodRequest::MeasurementMethodEnumCase::MEASUREMENT_METHOD_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for measurement_method was not specified or out of range");
          break;
        }
      }

      auto status = library_->ACPCfgMeasurementMethod(instrument, selector_string, measurement_method);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPCfgNoiseCompensationEnabled(::grpc::ServerContext* context, const ACPCfgNoiseCompensationEnabledRequest* request, ACPCfgNoiseCompensationEnabledResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 noise_compensation_enabled;
      switch (request->noise_compensation_enabled_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgNoiseCompensationEnabledRequest::NoiseCompensationEnabledEnumCase::kNoiseCompensationEnabled: {
          noise_compensation_enabled = static_cast<int32>(request->noise_compensation_enabled());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgNoiseCompensationEnabledRequest::NoiseCompensationEnabledEnumCase::kNoiseCompensationEnabledRaw: {
          noise_compensation_enabled = static_cast<int32>(request->noise_compensation_enabled_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgNoiseCompensationEnabledRequest::NoiseCompensationEnabledEnumCase::NOISE_COMPENSATION_ENABLED_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for noise_compensation_enabled was not specified or out of range");
          break;
        }
      }

      auto status = library_->ACPCfgNoiseCompensationEnabled(instrument, selector_string, noise_compensation_enabled);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPCfgNumberOfOffsets(::grpc::ServerContext* context, const ACPCfgNumberOfOffsetsRequest* request, ACPCfgNumberOfOffsetsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 number_of_offsets = request->number_of_offsets();
      auto status = library_->ACPCfgNumberOfOffsets(instrument, selector_string, number_of_offsets);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPCfgRBWFilter(::grpc::ServerContext* context, const ACPCfgRBWFilterRequest* request, ACPCfgRBWFilterResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 rbw_auto;
      switch (request->rbw_auto_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgRBWFilterRequest::RbwAutoEnumCase::kRbwAuto: {
          rbw_auto = static_cast<int32>(request->rbw_auto());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgRBWFilterRequest::RbwAutoEnumCase::kRbwAutoRaw: {
          rbw_auto = static_cast<int32>(request->rbw_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgRBWFilterRequest::RbwAutoEnumCase::RBW_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rbw_auto was not specified or out of range");
          break;
        }
      }

      float64 rbw = request->rbw();
      int32 rbw_filter_type;
      switch (request->rbw_filter_type_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgRBWFilterRequest::RbwFilterTypeEnumCase::kRbwFilterType: {
          rbw_filter_type = static_cast<int32>(request->rbw_filter_type());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgRBWFilterRequest::RbwFilterTypeEnumCase::kRbwFilterTypeRaw: {
          rbw_filter_type = static_cast<int32>(request->rbw_filter_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgRBWFilterRequest::RbwFilterTypeEnumCase::RBW_FILTER_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rbw_filter_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->ACPCfgRBWFilter(instrument, selector_string, rbw_auto, rbw, rbw_filter_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPCfgSweepTime(::grpc::ServerContext* context, const ACPCfgSweepTimeRequest* request, ACPCfgSweepTimeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 sweep_time_auto;
      switch (request->sweep_time_auto_enum_case()) {
        case nirfmxcdma2k_grpc::ACPCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAuto: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAutoRaw: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ACPCfgSweepTimeRequest::SweepTimeAutoEnumCase::SWEEP_TIME_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for sweep_time_auto was not specified or out of range");
          break;
        }
      }

      float64 sweep_time_interval = request->sweep_time_interval();
      auto status = library_->ACPCfgSweepTime(instrument, selector_string, sweep_time_auto, sweep_time_interval);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPFetchAbsolutePowersTrace(::grpc::ServerContext* context, const ACPFetchAbsolutePowersTraceRequest* request, ACPFetchAbsolutePowersTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 trace_index = request->trace_index();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ACPFetchAbsolutePowersTrace(instrument, selector_string, timeout, trace_index, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_absolute_powers_trace()->Resize(actual_array_size, 0);
        float32* absolute_powers_trace = response->mutable_absolute_powers_trace()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ACPFetchAbsolutePowersTrace(instrument, selector_string, timeout, trace_index, &x0, &dx, absolute_powers_trace, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_absolute_powers_trace()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPFetchCarrierAbsolutePower(::grpc::ServerContext* context, const ACPFetchCarrierAbsolutePowerRequest* request, ACPFetchCarrierAbsolutePowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 carrier_absolute_power {};
      auto status = library_->ACPFetchCarrierAbsolutePower(instrument, selector_string, timeout, &carrier_absolute_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_carrier_absolute_power(carrier_absolute_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPFetchOffsetMeasurement(::grpc::ServerContext* context, const ACPFetchOffsetMeasurementRequest* request, ACPFetchOffsetMeasurementResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 lower_relative_power {};
      float64 upper_relative_power {};
      float64 lower_absolute_power {};
      float64 upper_absolute_power {};
      auto status = library_->ACPFetchOffsetMeasurement(instrument, selector_string, timeout, &lower_relative_power, &upper_relative_power, &lower_absolute_power, &upper_absolute_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_lower_relative_power(lower_relative_power);
      response->set_upper_relative_power(upper_relative_power);
      response->set_lower_absolute_power(lower_absolute_power);
      response->set_upper_absolute_power(upper_absolute_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPFetchOffsetMeasurementArray(::grpc::ServerContext* context, const ACPFetchOffsetMeasurementArrayRequest* request, ACPFetchOffsetMeasurementArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ACPFetchOffsetMeasurementArray(instrument, selector_string, timeout, nullptr, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_lower_relative_power()->Resize(actual_array_size, 0);
        float64* lower_relative_power = response->mutable_lower_relative_power()->mutable_data();
        response->mutable_upper_relative_power()->Resize(actual_array_size, 0);
        float64* upper_relative_power = response->mutable_upper_relative_power()->mutable_data();
        response->mutable_lower_absolute_power()->Resize(actual_array_size, 0);
        float64* lower_absolute_power = response->mutable_lower_absolute_power()->mutable_data();
        response->mutable_upper_absolute_power()->Resize(actual_array_size, 0);
        float64* upper_absolute_power = response->mutable_upper_absolute_power()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ACPFetchOffsetMeasurementArray(instrument, selector_string, timeout, lower_relative_power, upper_relative_power, lower_absolute_power, upper_absolute_power, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_lower_relative_power()->Resize(actual_array_size, 0);
        response->mutable_upper_relative_power()->Resize(actual_array_size, 0);
        response->mutable_lower_absolute_power()->Resize(actual_array_size, 0);
        response->mutable_upper_absolute_power()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPFetchRelativePowersTrace(::grpc::ServerContext* context, const ACPFetchRelativePowersTraceRequest* request, ACPFetchRelativePowersTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 trace_index = request->trace_index();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ACPFetchRelativePowersTrace(instrument, selector_string, timeout, trace_index, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_relative_powers_trace()->Resize(actual_array_size, 0);
        float32* relative_powers_trace = response->mutable_relative_powers_trace()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ACPFetchRelativePowersTrace(instrument, selector_string, timeout, trace_index, &x0, &dx, relative_powers_trace, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_relative_powers_trace()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ACPFetchSpectrum(::grpc::ServerContext* context, const ACPFetchSpectrumRequest* request, ACPFetchSpectrumResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ACPFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        float32* spectrum = response->mutable_spectrum()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ACPFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, spectrum, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::AbortMeasurements(::grpc::ServerContext* context, const AbortMeasurementsRequest* request, AbortMeasurementsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto status = library_->AbortMeasurements(instrument, selector_string);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::AnalyzeIQ1Waveform(::grpc::ServerContext* context, const AnalyzeIQ1WaveformRequest* request, AnalyzeIQ1WaveformResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto result_name_mbcs = convert_from_grpc<std::string>(request->result_name());
      char* result_name = (char*)result_name_mbcs.c_str();
      float64 x0 = request->x0();
      float64 dx = request->dx();
      auto iq = convert_from_grpc<NIComplexSingle>(request->iq());
      auto array_size_raw = request->iq().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      int32 reset = request->reset();
      auto reserved = 0;
      auto status = library_->AnalyzeIQ1Waveform(instrument, selector_string, result_name, x0, dx, iq.data(), array_size, reset, reserved);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::AnalyzeIQ1WaveformInterleavedIQ(::grpc::ServerContext* context, const AnalyzeIQ1WaveformInterleavedIQRequest* request, AnalyzeIQ1WaveformInterleavedIQResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto result_name_mbcs = convert_from_grpc<std::string>(request->result_name());
      char* result_name = (char*)result_name_mbcs.c_str();
      float64 x0 = request->x0();
      float64 dx = request->dx();
      auto iq = const_cast<float32*>(request->iq().data());
      auto array_size_raw = request->iq().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      int32 reset = request->reset();
      auto reserved = 0;
      auto status = library_->AnalyzeIQ1WaveformInterleavedIQ(instrument, selector_string, result_name, x0, dx, iq, array_size, reset, reserved);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::AnalyzeIQ1WaveformSplit(::grpc::ServerContext* context, const AnalyzeIQ1WaveformSplitRequest* request, AnalyzeIQ1WaveformSplitResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto result_name_mbcs = convert_from_grpc<std::string>(request->result_name());
      char* result_name = (char*)result_name_mbcs.c_str();
      float64 x0 = request->x0();
      float64 dx = request->dx();
      auto iqi = const_cast<float32*>(request->iqi().data());
      auto iqq = const_cast<float32*>(request->iqq().data());
      auto array_size_determine_from_sizes = std::array<int, 2>
      {
        request->iqi_size(),
        request->iqq_size()
      };
      const auto array_size_size_calculation = calculate_linked_array_size(array_size_determine_from_sizes, true);

      if (array_size_size_calculation.match_state == MatchState::MISMATCH) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The sizes of linked repeated fields [iqi, iqq] do not match");
      }
      // NULL out optional params with zero sizes.
      if (array_size_size_calculation.match_state == MatchState::MATCH_OR_ZERO) {
        iqi = request->iqi_size() ? std::move(iqi) : nullptr;
        iqq = request->iqq_size() ? std::move(iqq) : nullptr;
      }
      auto array_size = array_size_size_calculation.size;

      int32 reset = request->reset();
      auto reserved = 0;
      auto status = library_->AnalyzeIQ1WaveformSplit(instrument, selector_string, result_name, x0, dx, iqi, iqq, array_size, reset, reserved);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::AnalyzeSpectrum1Waveform(::grpc::ServerContext* context, const AnalyzeSpectrum1WaveformRequest* request, AnalyzeSpectrum1WaveformResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto result_name_mbcs = convert_from_grpc<std::string>(request->result_name());
      char* result_name = (char*)result_name_mbcs.c_str();
      float64 x0 = request->x0();
      float64 dx = request->dx();
      auto spectrum = const_cast<float32*>(request->spectrum().data());
      auto array_size_raw = request->spectrum().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      int32 reset = request->reset();
      auto reserved = 0;
      auto status = library_->AnalyzeSpectrum1Waveform(instrument, selector_string, result_name, x0, dx, spectrum, array_size, reset, reserved);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::AutoLevel(::grpc::ServerContext* context, const AutoLevelRequest* request, AutoLevelResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 measurement_interval = request->measurement_interval();
      float64 reference_level {};
      auto status = library_->AutoLevel(instrument, selector_string, measurement_interval, &reference_level);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_reference_level(reference_level);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::BuildChannelString(::grpc::ServerContext* context, const BuildChannelStringRequest* request, BuildChannelStringResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 channel_number = request->channel_number();

      while (true) {
        auto status = library_->BuildChannelString(selector_string, channel_number, 0, nullptr);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
        }
        int32 selector_string_out_length = status;

        std::string selector_string_out;
        if (selector_string_out_length > 0) {
            selector_string_out.resize(selector_string_out_length - 1);
        }
        status = library_->BuildChannelString(selector_string, channel_number, selector_string_out_length, (char*)selector_string_out.data());
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(selector_string_out_length)) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
        }
        response->set_status(status);
        std::string selector_string_out_utf8;
        convert_to_grpc(selector_string_out, &selector_string_out_utf8);
        response->set_selector_string_out(selector_string_out_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_selector_string_out()));
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::BuildOffsetString(::grpc::ServerContext* context, const BuildOffsetStringRequest* request, BuildOffsetStringResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 offset_number = request->offset_number();

      while (true) {
        auto status = library_->BuildOffsetString(selector_string, offset_number, 0, nullptr);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
        }
        int32 selector_string_out_length = status;

        std::string selector_string_out;
        if (selector_string_out_length > 0) {
            selector_string_out.resize(selector_string_out_length - 1);
        }
        status = library_->BuildOffsetString(selector_string, offset_number, selector_string_out_length, (char*)selector_string_out.data());
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(selector_string_out_length)) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
        }
        response->set_status(status);
        std::string selector_string_out_utf8;
        convert_to_grpc(selector_string_out, &selector_string_out_utf8);
        response->set_selector_string_out(selector_string_out_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_selector_string_out()));
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::BuildSignalString(::grpc::ServerContext* context, const BuildSignalStringRequest* request, BuildSignalStringResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto signal_name_mbcs = convert_from_grpc<std::string>(request->signal_name());
      char* signal_name = (char*)signal_name_mbcs.c_str();
      auto result_name_mbcs = convert_from_grpc<std::string>(request->result_name());
      char* result_name = (char*)result_name_mbcs.c_str();

      while (true) {
        auto status = library_->BuildSignalString(signal_name, result_name, 0, nullptr);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
        }
        int32 selector_string_length = status;

        std::string selector_string;
        if (selector_string_length > 0) {
            selector_string.resize(selector_string_length - 1);
        }
        status = library_->BuildSignalString(signal_name, result_name, selector_string_length, (char*)selector_string.data());
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(selector_string_length)) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
        }
        response->set_status(status);
        std::string selector_string_utf8;
        convert_to_grpc(selector_string, &selector_string_utf8);
        response->set_selector_string(selector_string_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_selector_string()));
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDACfgMeasurementChannel(::grpc::ServerContext* context, const CDACfgMeasurementChannelRequest* request, CDACfgMeasurementChannelResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 walsh_code_length = request->walsh_code_length();
      int32 walsh_code_number = request->walsh_code_number();
      int32 branch;
      switch (request->branch_enum_case()) {
        case nirfmxcdma2k_grpc::CDACfgMeasurementChannelRequest::BranchEnumCase::kBranch: {
          branch = static_cast<int32>(request->branch());
          break;
        }
        case nirfmxcdma2k_grpc::CDACfgMeasurementChannelRequest::BranchEnumCase::kBranchRaw: {
          branch = static_cast<int32>(request->branch_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CDACfgMeasurementChannelRequest::BranchEnumCase::BRANCH_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for branch was not specified or out of range");
          break;
        }
      }

      auto status = library_->CDACfgMeasurementChannel(instrument, selector_string, walsh_code_length, walsh_code_number, branch);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDACfgPowerUnit(::grpc::ServerContext* context, const CDACfgPowerUnitRequest* request, CDACfgPowerUnitResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 power_unit;
      switch (request->power_unit_enum_case()) {
        case nirfmxcdma2k_grpc::CDACfgPowerUnitRequest::PowerUnitEnumCase::kPowerUnit: {
          power_unit = static_cast<int32>(request->power_unit());
          break;
        }
        case nirfmxcdma2k_grpc::CDACfgPowerUnitRequest::PowerUnitEnumCase::kPowerUnitRaw: {
          power_unit = static_cast<int32>(request->power_unit_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CDACfgPowerUnitRequest::PowerUnitEnumCase::POWER_UNIT_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for power_unit was not specified or out of range");
          break;
        }
      }

      auto status = library_->CDACfgPowerUnit(instrument, selector_string, power_unit);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDACfgSynchronizationModeAndInterval(::grpc::ServerContext* context, const CDACfgSynchronizationModeAndIntervalRequest* request, CDACfgSynchronizationModeAndIntervalResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 synchronization_mode;
      switch (request->synchronization_mode_enum_case()) {
        case nirfmxcdma2k_grpc::CDACfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationMode: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode());
          break;
        }
        case nirfmxcdma2k_grpc::CDACfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationModeRaw: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CDACfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::SYNCHRONIZATION_MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for synchronization_mode was not specified or out of range");
          break;
        }
      }

      int32 measurement_offset = request->measurement_offset();
      int32 measurement_length = request->measurement_length();
      auto status = library_->CDACfgSynchronizationModeAndInterval(instrument, selector_string, synchronization_mode, measurement_offset, measurement_length);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchCodeDomainIAndQPower(::grpc::ServerContext* context, const CDAFetchCodeDomainIAndQPowerRequest* request, CDAFetchCodeDomainIAndQPowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 i_mean_active_power {};
      float64 q_mean_active_power {};
      float64 i_peak_inactive_power {};
      float64 q_peak_inactive_power {};
      auto status = library_->CDAFetchCodeDomainIAndQPower(instrument, selector_string, timeout, &i_mean_active_power, &q_mean_active_power, &i_peak_inactive_power, &q_peak_inactive_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_i_mean_active_power(i_mean_active_power);
      response->set_q_mean_active_power(q_mean_active_power);
      response->set_i_peak_inactive_power(i_peak_inactive_power);
      response->set_q_peak_inactive_power(q_peak_inactive_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchCodeDomainIAndQPowerTrace(::grpc::ServerContext* context, const CDAFetchCodeDomainIAndQPowerTraceRequest* request, CDAFetchCodeDomainIAndQPowerTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchCodeDomainIAndQPowerTrace(instrument, selector_string, timeout, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_i_code_domain_powers()->Resize(actual_array_size, 0);
        float32* i_code_domain_powers = response->mutable_i_code_domain_powers()->mutable_data();
        response->mutable_q_code_domain_powers()->Resize(actual_array_size, 0);
        float32* q_code_domain_powers = response->mutable_q_code_domain_powers()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchCodeDomainIAndQPowerTrace(instrument, selector_string, timeout, i_code_domain_powers, q_code_domain_powers, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_i_code_domain_powers()->Resize(actual_array_size, 0);
        response->mutable_q_code_domain_powers()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchCodeDomainPower(::grpc::ServerContext* context, const CDAFetchCodeDomainPowerRequest* request, CDAFetchCodeDomainPowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 total_power {};
      float64 total_active_power {};
      float64 mean_active_power {};
      float64 peak_active_power {};
      float64 mean_inactive_power {};
      float64 peak_inactive_power {};
      auto status = library_->CDAFetchCodeDomainPower(instrument, selector_string, timeout, &total_power, &total_active_power, &mean_active_power, &peak_active_power, &mean_inactive_power, &peak_inactive_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_total_power(total_power);
      response->set_total_active_power(total_active_power);
      response->set_mean_active_power(mean_active_power);
      response->set_peak_active_power(peak_active_power);
      response->set_mean_inactive_power(mean_inactive_power);
      response->set_peak_inactive_power(peak_inactive_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchIQImpairments(::grpc::ServerContext* context, const CDAFetchIQImpairmentsRequest* request, CDAFetchIQImpairmentsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 iq_origin_offset {};
      float64 iq_gain_imbalance {};
      float64 iq_quadrature_error {};
      auto status = library_->CDAFetchIQImpairments(instrument, selector_string, timeout, &iq_origin_offset, &iq_gain_imbalance, &iq_quadrature_error);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_iq_origin_offset(iq_origin_offset);
      response->set_iq_gain_imbalance(iq_gain_imbalance);
      response->set_iq_quadrature_error(iq_quadrature_error);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolConstellationTrace(::grpc::ServerContext* context, const CDAFetchSymbolConstellationTraceRequest* request, CDAFetchSymbolConstellationTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolConstellationTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::vector<NIComplexSingle> symbol_constellation(actual_array_size, NIComplexSingle());
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolConstellationTrace(instrument, selector_string, timeout, symbol_constellation.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        convert_to_grpc(symbol_constellation, response->mutable_symbol_constellation());
        {
          auto shrunk_size = actual_array_size;
          auto current_size = response->mutable_symbol_constellation()->size();
          if (shrunk_size != current_size) {
            response->mutable_symbol_constellation()->DeleteSubrange(shrunk_size, current_size - shrunk_size);
          }
        }
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolConstellationTraceInterleavedIQ(::grpc::ServerContext* context, const CDAFetchSymbolConstellationTraceInterleavedIQRequest* request, CDAFetchSymbolConstellationTraceInterleavedIQResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolConstellationTraceInterleavedIQ(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_symbol_constellation()->Resize(actual_array_size * 2, 0);
        float32* symbol_constellation = response->mutable_symbol_constellation()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolConstellationTraceInterleavedIQ(instrument, selector_string, timeout, symbol_constellation, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_symbol_constellation()->Resize(actual_array_size * 2, 0);
        response->set_actual_array_size(actual_array_size * 2);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolConstellationTraceSplit(::grpc::ServerContext* context, const CDAFetchSymbolConstellationTraceSplitRequest* request, CDAFetchSymbolConstellationTraceSplitResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolConstellationTraceSplit(instrument, selector_string, timeout, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_symbol_constellation_i()->Resize(actual_array_size, 0);
        float32* symbol_constellation_i = response->mutable_symbol_constellation_i()->mutable_data();
        response->mutable_symbol_constellation_q()->Resize(actual_array_size, 0);
        float32* symbol_constellation_q = response->mutable_symbol_constellation_q()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolConstellationTraceSplit(instrument, selector_string, timeout, symbol_constellation_i, symbol_constellation_q, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_symbol_constellation_i()->Resize(actual_array_size, 0);
        response->mutable_symbol_constellation_q()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolEVM(::grpc::ServerContext* context, const CDAFetchSymbolEVMRequest* request, CDAFetchSymbolEVMResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 rms_symbol_evm {};
      float64 peak_symbol_evm {};
      float64 rms_symbol_magnitude_error {};
      float64 rms_symbol_phase_error {};
      float64 mean_symbol_power {};
      float64 frequency_error {};
      float64 chip_rate_error {};
      auto status = library_->CDAFetchSymbolEVM(instrument, selector_string, timeout, &rms_symbol_evm, &peak_symbol_evm, &rms_symbol_magnitude_error, &rms_symbol_phase_error, &mean_symbol_power, &frequency_error, &chip_rate_error);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_rms_symbol_evm(rms_symbol_evm);
      response->set_peak_symbol_evm(peak_symbol_evm);
      response->set_rms_symbol_magnitude_error(rms_symbol_magnitude_error);
      response->set_rms_symbol_phase_error(rms_symbol_phase_error);
      response->set_mean_symbol_power(mean_symbol_power);
      response->set_frequency_error(frequency_error);
      response->set_chip_rate_error(chip_rate_error);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolEVMTrace(::grpc::ServerContext* context, const CDAFetchSymbolEVMTraceRequest* request, CDAFetchSymbolEVMTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolEVMTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_symbol_evm()->Resize(actual_array_size, 0);
        float32* symbol_evm = response->mutable_symbol_evm()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolEVMTrace(instrument, selector_string, timeout, symbol_evm, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_symbol_evm()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolMagnitudeErrorTrace(::grpc::ServerContext* context, const CDAFetchSymbolMagnitudeErrorTraceRequest* request, CDAFetchSymbolMagnitudeErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolMagnitudeErrorTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_symbol_magnitude_error()->Resize(actual_array_size, 0);
        float32* symbol_magnitude_error = response->mutable_symbol_magnitude_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolMagnitudeErrorTrace(instrument, selector_string, timeout, symbol_magnitude_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_symbol_magnitude_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolPhaseErrorTrace(::grpc::ServerContext* context, const CDAFetchSymbolPhaseErrorTraceRequest* request, CDAFetchSymbolPhaseErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolPhaseErrorTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_symbol_phase_error()->Resize(actual_array_size, 0);
        float32* symbol_phase_error = response->mutable_symbol_phase_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolPhaseErrorTrace(instrument, selector_string, timeout, symbol_phase_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_symbol_phase_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CDAFetchSymbolPowerTrace(::grpc::ServerContext* context, const CDAFetchSymbolPowerTraceRequest* request, CDAFetchSymbolPowerTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CDAFetchSymbolPowerTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_symbol_powers()->Resize(actual_array_size, 0);
        float32* symbol_powers = response->mutable_symbol_powers()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CDAFetchSymbolPowerTrace(instrument, selector_string, timeout, symbol_powers, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_symbol_powers()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CHPCfgAveraging(::grpc::ServerContext* context, const CHPCfgAveragingRequest* request, CHPCfgAveragingResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 averaging_enabled;
      switch (request->averaging_enabled_enum_case()) {
        case nirfmxcdma2k_grpc::CHPCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabled: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabledRaw: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgAveragingRequest::AveragingEnabledEnumCase::AVERAGING_ENABLED_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_enabled was not specified or out of range");
          break;
        }
      }

      int32 averaging_count = request->averaging_count();
      int32 averaging_type;
      switch (request->averaging_type_enum_case()) {
        case nirfmxcdma2k_grpc::CHPCfgAveragingRequest::AveragingTypeEnumCase::kAveragingType: {
          averaging_type = static_cast<int32>(request->averaging_type());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgAveragingRequest::AveragingTypeEnumCase::kAveragingTypeRaw: {
          averaging_type = static_cast<int32>(request->averaging_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgAveragingRequest::AveragingTypeEnumCase::AVERAGING_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->CHPCfgAveraging(instrument, selector_string, averaging_enabled, averaging_count, averaging_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CHPCfgRBWFilter(::grpc::ServerContext* context, const CHPCfgRBWFilterRequest* request, CHPCfgRBWFilterResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 rbw_auto;
      switch (request->rbw_auto_enum_case()) {
        case nirfmxcdma2k_grpc::CHPCfgRBWFilterRequest::RbwAutoEnumCase::kRbwAuto: {
          rbw_auto = static_cast<int32>(request->rbw_auto());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgRBWFilterRequest::RbwAutoEnumCase::kRbwAutoRaw: {
          rbw_auto = static_cast<int32>(request->rbw_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgRBWFilterRequest::RbwAutoEnumCase::RBW_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rbw_auto was not specified or out of range");
          break;
        }
      }

      float64 rbw = request->rbw();
      int32 rbw_filter_type;
      switch (request->rbw_filter_type_enum_case()) {
        case nirfmxcdma2k_grpc::CHPCfgRBWFilterRequest::RbwFilterTypeEnumCase::kRbwFilterType: {
          rbw_filter_type = static_cast<int32>(request->rbw_filter_type());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgRBWFilterRequest::RbwFilterTypeEnumCase::kRbwFilterTypeRaw: {
          rbw_filter_type = static_cast<int32>(request->rbw_filter_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgRBWFilterRequest::RbwFilterTypeEnumCase::RBW_FILTER_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rbw_filter_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->CHPCfgRBWFilter(instrument, selector_string, rbw_auto, rbw, rbw_filter_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CHPCfgSweepTime(::grpc::ServerContext* context, const CHPCfgSweepTimeRequest* request, CHPCfgSweepTimeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 sweep_time_auto;
      switch (request->sweep_time_auto_enum_case()) {
        case nirfmxcdma2k_grpc::CHPCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAuto: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAutoRaw: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CHPCfgSweepTimeRequest::SweepTimeAutoEnumCase::SWEEP_TIME_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for sweep_time_auto was not specified or out of range");
          break;
        }
      }

      float64 sweep_time_interval = request->sweep_time_interval();
      auto status = library_->CHPCfgSweepTime(instrument, selector_string, sweep_time_auto, sweep_time_interval);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CHPFetchCarrierAbsolutePower(::grpc::ServerContext* context, const CHPFetchCarrierAbsolutePowerRequest* request, CHPFetchCarrierAbsolutePowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 carrier_absolute_power {};
      auto status = library_->CHPFetchCarrierAbsolutePower(instrument, selector_string, timeout, &carrier_absolute_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_carrier_absolute_power(carrier_absolute_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CHPFetchSpectrum(::grpc::ServerContext* context, const CHPFetchSpectrumRequest* request, CHPFetchSpectrumResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->CHPFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        float32* spectrum = response->mutable_spectrum()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->CHPFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, spectrum, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgBandClass(::grpc::ServerContext* context, const CfgBandClassRequest* request, CfgBandClassResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 band_class = request->band_class();
      auto status = library_->CfgBandClass(instrument, selector_string, band_class);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgChannelConfigurationMode(::grpc::ServerContext* context, const CfgChannelConfigurationModeRequest* request, CfgChannelConfigurationModeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 channel_configuration_mode;
      switch (request->channel_configuration_mode_enum_case()) {
        case nirfmxcdma2k_grpc::CfgChannelConfigurationModeRequest::ChannelConfigurationModeEnumCase::kChannelConfigurationMode: {
          channel_configuration_mode = static_cast<int32>(request->channel_configuration_mode());
          break;
        }
        case nirfmxcdma2k_grpc::CfgChannelConfigurationModeRequest::ChannelConfigurationModeEnumCase::kChannelConfigurationModeRaw: {
          channel_configuration_mode = static_cast<int32>(request->channel_configuration_mode_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgChannelConfigurationModeRequest::ChannelConfigurationModeEnumCase::CHANNEL_CONFIGURATION_MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for channel_configuration_mode was not specified or out of range");
          break;
        }
      }

      auto status = library_->CfgChannelConfigurationMode(instrument, selector_string, channel_configuration_mode);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgDigitalEdgeTrigger(::grpc::ServerContext* context, const CfgDigitalEdgeTriggerRequest* request, CfgDigitalEdgeTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      char* digital_edge_source;
      std::string digital_edge_source_buffer;
      switch (request->digital_edge_source_enum_case()) {
        case nirfmxcdma2k_grpc::CfgDigitalEdgeTriggerRequest::DigitalEdgeSourceEnumCase::kDigitalEdgeSourceMapped: {
          auto digital_edge_source_imap_it = digitaledgetriggersource_input_map_.find(request->digital_edge_source_mapped());
          if (digital_edge_source_imap_it == digitaledgetriggersource_input_map_.end()) {
            return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for digital_edge_source_mapped was not specified or out of range.");
          }
          digital_edge_source = const_cast<char*>((digital_edge_source_imap_it->second).c_str());
          break;
        }
        case nirfmxcdma2k_grpc::CfgDigitalEdgeTriggerRequest::DigitalEdgeSourceEnumCase::kDigitalEdgeSourceRaw: {
          digital_edge_source_buffer = convert_from_grpc<std::string>(request->digital_edge_source_raw());
          digital_edge_source = const_cast<char*>(digital_edge_source_buffer.c_str());
          break;
        }
        case nirfmxcdma2k_grpc::CfgDigitalEdgeTriggerRequest::DigitalEdgeSourceEnumCase::DIGITAL_EDGE_SOURCE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for digital_edge_source was not specified or out of range");
          break;
        }
      }

      int32 digital_edge;
      switch (request->digital_edge_enum_case()) {
        case nirfmxcdma2k_grpc::CfgDigitalEdgeTriggerRequest::DigitalEdgeEnumCase::kDigitalEdge: {
          digital_edge = static_cast<int32>(request->digital_edge());
          break;
        }
        case nirfmxcdma2k_grpc::CfgDigitalEdgeTriggerRequest::DigitalEdgeEnumCase::kDigitalEdgeRaw: {
          digital_edge = static_cast<int32>(request->digital_edge_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgDigitalEdgeTriggerRequest::DigitalEdgeEnumCase::DIGITAL_EDGE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for digital_edge was not specified or out of range");
          break;
        }
      }

      float64 trigger_delay = request->trigger_delay();
      int32 enable_trigger = request->enable_trigger();
      auto status = library_->CfgDigitalEdgeTrigger(instrument, selector_string, digital_edge_source, digital_edge, trigger_delay, enable_trigger);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgExternalAttenuation(::grpc::ServerContext* context, const CfgExternalAttenuationRequest* request, CfgExternalAttenuationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 external_attenuation = request->external_attenuation();
      auto status = library_->CfgExternalAttenuation(instrument, selector_string, external_attenuation);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgFrequency(::grpc::ServerContext* context, const CfgFrequencyRequest* request, CfgFrequencyResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 center_frequency = request->center_frequency();
      auto status = library_->CfgFrequency(instrument, selector_string, center_frequency);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgFrequencyChannelNumber(::grpc::ServerContext* context, const CfgFrequencyChannelNumberRequest* request, CfgFrequencyChannelNumberResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 link_direction;
      switch (request->link_direction_enum_case()) {
        case nirfmxcdma2k_grpc::CfgFrequencyChannelNumberRequest::LinkDirectionEnumCase::kLinkDirection: {
          link_direction = static_cast<int32>(request->link_direction());
          break;
        }
        case nirfmxcdma2k_grpc::CfgFrequencyChannelNumberRequest::LinkDirectionEnumCase::kLinkDirectionRaw: {
          link_direction = static_cast<int32>(request->link_direction_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgFrequencyChannelNumberRequest::LinkDirectionEnumCase::LINK_DIRECTION_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for link_direction was not specified or out of range");
          break;
        }
      }

      int32 band_class = request->band_class();
      int32 channel_number = request->channel_number();
      auto status = library_->CfgFrequencyChannelNumber(instrument, selector_string, link_direction, band_class, channel_number);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgFrequencyReference(::grpc::ServerContext* context, const CfgFrequencyReferenceRequest* request, CfgFrequencyReferenceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto channel_name_mbcs = convert_from_grpc<std::string>(request->channel_name());
      char* channel_name = (char*)channel_name_mbcs.c_str();
      char* frequency_reference_source;
      std::string frequency_reference_source_buffer;
      switch (request->frequency_reference_source_enum_case()) {
        case nirfmxcdma2k_grpc::CfgFrequencyReferenceRequest::FrequencyReferenceSourceEnumCase::kFrequencyReferenceSourceMapped: {
          auto frequency_reference_source_imap_it = frequencyreferencesource_input_map_.find(request->frequency_reference_source_mapped());
          if (frequency_reference_source_imap_it == frequencyreferencesource_input_map_.end()) {
            return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for frequency_reference_source_mapped was not specified or out of range.");
          }
          frequency_reference_source = const_cast<char*>((frequency_reference_source_imap_it->second).c_str());
          break;
        }
        case nirfmxcdma2k_grpc::CfgFrequencyReferenceRequest::FrequencyReferenceSourceEnumCase::kFrequencyReferenceSourceRaw: {
          frequency_reference_source_buffer = convert_from_grpc<std::string>(request->frequency_reference_source_raw());
          frequency_reference_source = const_cast<char*>(frequency_reference_source_buffer.c_str());
          break;
        }
        case nirfmxcdma2k_grpc::CfgFrequencyReferenceRequest::FrequencyReferenceSourceEnumCase::FREQUENCY_REFERENCE_SOURCE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for frequency_reference_source was not specified or out of range");
          break;
        }
      }

      float64 frequency_reference_frequency = request->frequency_reference_frequency();
      auto status = library_->CfgFrequencyReference(instrument, channel_name, frequency_reference_source, frequency_reference_frequency);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgIQPowerEdgeTrigger(::grpc::ServerContext* context, const CfgIQPowerEdgeTriggerRequest* request, CfgIQPowerEdgeTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto iq_power_edge_source_mbcs = convert_from_grpc<std::string>(request->iq_power_edge_source());
      char* iq_power_edge_source = (char*)iq_power_edge_source_mbcs.c_str();
      int32 iq_power_edge_slope;
      switch (request->iq_power_edge_slope_enum_case()) {
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::IqPowerEdgeSlopeEnumCase::kIqPowerEdgeSlope: {
          iq_power_edge_slope = static_cast<int32>(request->iq_power_edge_slope());
          break;
        }
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::IqPowerEdgeSlopeEnumCase::kIqPowerEdgeSlopeRaw: {
          iq_power_edge_slope = static_cast<int32>(request->iq_power_edge_slope_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::IqPowerEdgeSlopeEnumCase::IQ_POWER_EDGE_SLOPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for iq_power_edge_slope was not specified or out of range");
          break;
        }
      }

      float64 iq_power_edge_level = request->iq_power_edge_level();
      float64 trigger_delay = request->trigger_delay();
      int32 minimum_quiet_time_mode;
      switch (request->minimum_quiet_time_mode_enum_case()) {
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::MinimumQuietTimeModeEnumCase::kMinimumQuietTimeMode: {
          minimum_quiet_time_mode = static_cast<int32>(request->minimum_quiet_time_mode());
          break;
        }
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::MinimumQuietTimeModeEnumCase::kMinimumQuietTimeModeRaw: {
          minimum_quiet_time_mode = static_cast<int32>(request->minimum_quiet_time_mode_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::MinimumQuietTimeModeEnumCase::MINIMUM_QUIET_TIME_MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for minimum_quiet_time_mode was not specified or out of range");
          break;
        }
      }

      float64 minimum_quiet_time = request->minimum_quiet_time();
      int32 iq_power_edge_level_type;
      switch (request->iq_power_edge_level_type_enum_case()) {
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::IqPowerEdgeLevelTypeEnumCase::kIqPowerEdgeLevelType: {
          iq_power_edge_level_type = static_cast<int32>(request->iq_power_edge_level_type());
          break;
        }
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::IqPowerEdgeLevelTypeEnumCase::kIqPowerEdgeLevelTypeRaw: {
          iq_power_edge_level_type = static_cast<int32>(request->iq_power_edge_level_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgIQPowerEdgeTriggerRequest::IqPowerEdgeLevelTypeEnumCase::IQ_POWER_EDGE_LEVEL_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for iq_power_edge_level_type was not specified or out of range");
          break;
        }
      }

      int32 enable_trigger = request->enable_trigger();
      auto status = library_->CfgIQPowerEdgeTrigger(instrument, selector_string, iq_power_edge_source, iq_power_edge_slope, iq_power_edge_level, trigger_delay, minimum_quiet_time_mode, minimum_quiet_time, iq_power_edge_level_type, enable_trigger);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgMechanicalAttenuation(::grpc::ServerContext* context, const CfgMechanicalAttenuationRequest* request, CfgMechanicalAttenuationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto channel_name_mbcs = convert_from_grpc<std::string>(request->channel_name());
      char* channel_name = (char*)channel_name_mbcs.c_str();
      int32 mechanical_attenuation_auto;
      switch (request->mechanical_attenuation_auto_enum_case()) {
        case nirfmxcdma2k_grpc::CfgMechanicalAttenuationRequest::MechanicalAttenuationAutoEnumCase::kMechanicalAttenuationAuto: {
          mechanical_attenuation_auto = static_cast<int32>(request->mechanical_attenuation_auto());
          break;
        }
        case nirfmxcdma2k_grpc::CfgMechanicalAttenuationRequest::MechanicalAttenuationAutoEnumCase::kMechanicalAttenuationAutoRaw: {
          mechanical_attenuation_auto = static_cast<int32>(request->mechanical_attenuation_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgMechanicalAttenuationRequest::MechanicalAttenuationAutoEnumCase::MECHANICAL_ATTENUATION_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for mechanical_attenuation_auto was not specified or out of range");
          break;
        }
      }

      float64 mechanical_attenuation_value = request->mechanical_attenuation_value();
      auto status = library_->CfgMechanicalAttenuation(instrument, channel_name, mechanical_attenuation_auto, mechanical_attenuation_value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgNumberOfChannels(::grpc::ServerContext* context, const CfgNumberOfChannelsRequest* request, CfgNumberOfChannelsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 number_of_channels = request->number_of_channels();
      auto status = library_->CfgNumberOfChannels(instrument, selector_string, number_of_channels);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgRF(::grpc::ServerContext* context, const CfgRFRequest* request, CfgRFResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 center_frequency = request->center_frequency();
      float64 reference_level = request->reference_level();
      float64 external_attenuation = request->external_attenuation();
      auto status = library_->CfgRF(instrument, selector_string, center_frequency, reference_level, external_attenuation);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgRFAttenuation(::grpc::ServerContext* context, const CfgRFAttenuationRequest* request, CfgRFAttenuationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto channel_name_mbcs = convert_from_grpc<std::string>(request->channel_name());
      char* channel_name = (char*)channel_name_mbcs.c_str();
      int32 rf_attenuation_auto;
      switch (request->rf_attenuation_auto_enum_case()) {
        case nirfmxcdma2k_grpc::CfgRFAttenuationRequest::RfAttenuationAutoEnumCase::kRfAttenuationAuto: {
          rf_attenuation_auto = static_cast<int32>(request->rf_attenuation_auto());
          break;
        }
        case nirfmxcdma2k_grpc::CfgRFAttenuationRequest::RfAttenuationAutoEnumCase::kRfAttenuationAutoRaw: {
          rf_attenuation_auto = static_cast<int32>(request->rf_attenuation_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgRFAttenuationRequest::RfAttenuationAutoEnumCase::RF_ATTENUATION_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rf_attenuation_auto was not specified or out of range");
          break;
        }
      }

      float64 rf_attenuation_value = request->rf_attenuation_value();
      auto status = library_->CfgRFAttenuation(instrument, channel_name, rf_attenuation_auto, rf_attenuation_value);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgRadioConfiguration(::grpc::ServerContext* context, const CfgRadioConfigurationRequest* request, CfgRadioConfigurationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 radio_configuration;
      switch (request->radio_configuration_enum_case()) {
        case nirfmxcdma2k_grpc::CfgRadioConfigurationRequest::RadioConfigurationEnumCase::kRadioConfiguration: {
          radio_configuration = static_cast<int32>(request->radio_configuration());
          break;
        }
        case nirfmxcdma2k_grpc::CfgRadioConfigurationRequest::RadioConfigurationEnumCase::kRadioConfigurationRaw: {
          radio_configuration = static_cast<int32>(request->radio_configuration_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgRadioConfigurationRequest::RadioConfigurationEnumCase::RADIO_CONFIGURATION_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for radio_configuration was not specified or out of range");
          break;
        }
      }

      auto status = library_->CfgRadioConfiguration(instrument, selector_string, radio_configuration);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgReferenceLevel(::grpc::ServerContext* context, const CfgReferenceLevelRequest* request, CfgReferenceLevelResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 reference_level = request->reference_level();
      auto status = library_->CfgReferenceLevel(instrument, selector_string, reference_level);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgSoftwareEdgeTrigger(::grpc::ServerContext* context, const CfgSoftwareEdgeTriggerRequest* request, CfgSoftwareEdgeTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 trigger_delay = request->trigger_delay();
      int32 enable_trigger = request->enable_trigger();
      auto status = library_->CfgSoftwareEdgeTrigger(instrument, selector_string, trigger_delay, enable_trigger);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgUplinkSpreading(::grpc::ServerContext* context, const CfgUplinkSpreadingRequest* request, CfgUplinkSpreadingResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int64 uplink_spreading_long_code_mask = request->uplink_spreading_long_code_mask();
      auto status = library_->CfgUplinkSpreading(instrument, selector_string, uplink_spreading_long_code_mask);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgUserDefinedChannel(::grpc::ServerContext* context, const CfgUserDefinedChannelRequest* request, CfgUserDefinedChannelResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 walsh_code_length = request->walsh_code_length();
      int32 walsh_code_number = request->walsh_code_number();
      int32 branch;
      switch (request->branch_enum_case()) {
        case nirfmxcdma2k_grpc::CfgUserDefinedChannelRequest::BranchEnumCase::kBranch: {
          branch = static_cast<int32>(request->branch());
          break;
        }
        case nirfmxcdma2k_grpc::CfgUserDefinedChannelRequest::BranchEnumCase::kBranchRaw: {
          branch = static_cast<int32>(request->branch_raw());
          break;
        }
        case nirfmxcdma2k_grpc::CfgUserDefinedChannelRequest::BranchEnumCase::BRANCH_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for branch was not specified or out of range");
          break;
        }
      }

      auto status = library_->CfgUserDefinedChannel(instrument, selector_string, walsh_code_length, walsh_code_number, branch);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CfgUserDefinedChannelArray(::grpc::ServerContext* context, const CfgUserDefinedChannelArrayRequest* request, CfgUserDefinedChannelArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto walsh_code_length = const_cast<int32*>(reinterpret_cast<const int32*>(request->walsh_code_length().data()));
      auto walsh_code_number = const_cast<int32*>(reinterpret_cast<const int32*>(request->walsh_code_number().data()));
      auto branch_vector = std::vector<int32>();
      branch_vector.reserve(request->branch().size());
      std::transform(
        request->branch().begin(),
        request->branch().end(),
        std::back_inserter(branch_vector),
        [](auto x) { return x; });
      auto branch = branch_vector.data();

      auto number_of_elements_determine_from_sizes = std::array<int, 3>
      {
        request->walsh_code_length_size(),
        request->walsh_code_number_size(),
        request->branch_size()
      };
      const auto number_of_elements_size_calculation = calculate_linked_array_size(number_of_elements_determine_from_sizes, true);

      if (number_of_elements_size_calculation.match_state == MatchState::MISMATCH) {
        return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The sizes of linked repeated fields [walsh_code_length, walsh_code_number, branch] do not match");
      }
      // NULL out optional params with zero sizes.
      if (number_of_elements_size_calculation.match_state == MatchState::MATCH_OR_ZERO) {
        walsh_code_length = request->walsh_code_length_size() ? std::move(walsh_code_length) : nullptr;
        walsh_code_number = request->walsh_code_number_size() ? std::move(walsh_code_number) : nullptr;
        branch = request->branch_size() ? std::move(branch) : nullptr;
      }
      auto number_of_elements = number_of_elements_size_calculation.size;

      auto status = library_->CfgUserDefinedChannelArray(instrument, selector_string, walsh_code_length, walsh_code_number, branch, number_of_elements);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CheckMeasurementStatus(::grpc::ServerContext* context, const CheckMeasurementStatusRequest* request, CheckMeasurementStatusResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 done {};
      auto status = library_->CheckMeasurementStatus(instrument, selector_string, &done);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_done(done);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ClearAllNamedResults(::grpc::ServerContext* context, const ClearAllNamedResultsRequest* request, ClearAllNamedResultsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto status = library_->ClearAllNamedResults(instrument, selector_string);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ClearNamedResult(::grpc::ServerContext* context, const ClearNamedResultRequest* request, ClearNamedResultResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto status = library_->ClearNamedResult(instrument, selector_string);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CloneSignalConfiguration(::grpc::ServerContext* context, const CloneSignalConfigurationRequest* request, CloneSignalConfigurationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto old_signal_name_mbcs = convert_from_grpc<std::string>(request->old_signal_name());
      char* old_signal_name = (char*)old_signal_name_mbcs.c_str();
      auto new_signal_name_mbcs = convert_from_grpc<std::string>(request->new_signal_name());
      char* new_signal_name = (char*)new_signal_name_mbcs.c_str();
      auto status = library_->CloneSignalConfiguration(instrument, old_signal_name, new_signal_name);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::Close(::grpc::ServerContext* context, const CloseRequest* request, CloseResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      int32 force_destroy = request->force_destroy();
      session_repository_->remove_session(instrument_grpc_session.name());
      auto status = library_->Close(instrument, force_destroy);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::Commit(::grpc::ServerContext* context, const CommitRequest* request, CommitResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto status = library_->Commit(instrument, selector_string);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::CreateSignalConfiguration(::grpc::ServerContext* context, const CreateSignalConfigurationRequest* request, CreateSignalConfigurationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto signal_name_mbcs = convert_from_grpc<std::string>(request->signal_name());
      char* signal_name = (char*)signal_name_mbcs.c_str();
      auto status = library_->CreateSignalConfiguration(instrument, signal_name);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::DeleteSignalConfiguration(::grpc::ServerContext* context, const DeleteSignalConfigurationRequest* request, DeleteSignalConfigurationResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto signal_name_mbcs = convert_from_grpc<std::string>(request->signal_name());
      char* signal_name = (char*)signal_name_mbcs.c_str();
      auto status = library_->DeleteSignalConfiguration(instrument, signal_name);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::DisableTrigger(::grpc::ServerContext* context, const DisableTriggerRequest* request, DisableTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto status = library_->DisableTrigger(instrument, selector_string);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAllNamedResultNames(::grpc::ServerContext* context, const GetAllNamedResultNamesRequest* request, GetAllNamedResultNamesResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 actual_result_names_size {};
      int32 default_result_exists {};
      while (true) {
        auto status = library_->GetAllNamedResultNames(instrument, selector_string, nullptr, 0, &actual_result_names_size, &default_result_exists);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::string result_names;
        if (actual_result_names_size > 0) {
            result_names.resize(actual_result_names_size - 1);
        }
        auto result_names_buffer_size = actual_result_names_size;
        status = library_->GetAllNamedResultNames(instrument, selector_string, (char*)result_names.data(), result_names_buffer_size, &actual_result_names_size, &default_result_exists);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        std::string result_names_utf8;
        convert_to_grpc(result_names, &result_names_utf8);
        response->set_result_names(result_names_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_result_names()));
        response->set_actual_result_names_size(actual_result_names_size);
        response->set_default_result_exists(default_result_exists);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeF32(::grpc::ServerContext* context, const GetAttributeF32Request* request, GetAttributeF32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      float32 attr_val {};
      auto status = library_->GetAttributeF32(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeF32Array(::grpc::ServerContext* context, const GetAttributeF32ArrayRequest* request, GetAttributeF32ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeF32Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        float32* attr_val = response->mutable_attr_val()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->GetAttributeF32Array(instrument, selector_string, attribute_id, attr_val, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeF64(::grpc::ServerContext* context, const GetAttributeF64Request* request, GetAttributeF64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      float64 attr_val {};
      auto status = library_->GetAttributeF64(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeF64Array(::grpc::ServerContext* context, const GetAttributeF64ArrayRequest* request, GetAttributeF64ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeF64Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        float64* attr_val = response->mutable_attr_val()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->GetAttributeF64Array(instrument, selector_string, attribute_id, attr_val, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI16(::grpc::ServerContext* context, const GetAttributeI16Request* request, GetAttributeI16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int16 attr_val {};
      auto status = library_->GetAttributeI16(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI32(::grpc::ServerContext* context, const GetAttributeI32Request* request, GetAttributeI32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 attr_val {};
      auto status = library_->GetAttributeI32(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      auto checked_convert_attr_val = [](auto raw_value) {
        bool raw_value_is_valid = nirfmxcdma2k_grpc::NiRFmxCDMA2kInt32AttributeValues_IsValid(raw_value);
        auto valid_enum_value = raw_value_is_valid ? raw_value : 0;
        return static_cast<nirfmxcdma2k_grpc::NiRFmxCDMA2kInt32AttributeValues>(valid_enum_value);
      };
      response->set_attr_val(checked_convert_attr_val(attr_val));
      response->set_attr_val_raw(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI32Array(::grpc::ServerContext* context, const GetAttributeI32ArrayRequest* request, GetAttributeI32ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeI32Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_attr_val_raw()->Resize(actual_array_size, 0);
        int32* attr_val = reinterpret_cast<int32*>(response->mutable_attr_val_raw()->mutable_data());
        auto array_size = actual_array_size;
        status = library_->GetAttributeI32Array(instrument, selector_string, attribute_id, attr_val, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        auto checked_convert_attr_val = [](auto raw_value) {
          bool raw_value_is_valid = nirfmxcdma2k_grpc::NiRFmxCDMA2kInt32AttributeValues_IsValid(raw_value);
          auto valid_enum_value = raw_value_is_valid ? raw_value : 0;
          return static_cast<nirfmxcdma2k_grpc::NiRFmxCDMA2kInt32AttributeValues>(valid_enum_value);
        };
        response->mutable_attr_val()->Clear();
        response->mutable_attr_val()->Reserve(actual_array_size);
        std::transform(
          response->attr_val_raw().begin(),
          response->attr_val_raw().begin() + actual_array_size,
          google::protobuf::RepeatedFieldBackInserter(response->mutable_attr_val()),
          [&](auto x) {
              return checked_convert_attr_val(x);
          });
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI64(::grpc::ServerContext* context, const GetAttributeI64Request* request, GetAttributeI64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int64 attr_val {};
      auto status = library_->GetAttributeI64(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI64Array(::grpc::ServerContext* context, const GetAttributeI64ArrayRequest* request, GetAttributeI64ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeI64Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        int64* attr_val = reinterpret_cast<int64*>(response->mutable_attr_val()->mutable_data());
        auto array_size = actual_array_size;
        status = library_->GetAttributeI64Array(instrument, selector_string, attribute_id, attr_val, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI8(::grpc::ServerContext* context, const GetAttributeI8Request* request, GetAttributeI8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int8 attr_val {};
      auto status = library_->GetAttributeI8(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeI8Array(::grpc::ServerContext* context, const GetAttributeI8ArrayRequest* request, GetAttributeI8ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeI8Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::vector<int8> attr_val(actual_array_size);
        auto array_size = actual_array_size;
        status = library_->GetAttributeI8Array(instrument, selector_string, attribute_id, attr_val.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_attr_val()->Clear();
        response->mutable_attr_val()->Reserve(actual_array_size);
        std::transform(
          attr_val.begin(),
          attr_val.begin() + actual_array_size,
          google::protobuf::RepeatedFieldBackInserter(response->mutable_attr_val()),
          [&](auto x) {
              return x;
          });
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeNIComplexDoubleArray(::grpc::ServerContext* context, const GetAttributeNIComplexDoubleArrayRequest* request, GetAttributeNIComplexDoubleArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeNIComplexDoubleArray(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::vector<NIComplexDouble> attr_val(actual_array_size, NIComplexDouble());
        auto array_size = actual_array_size;
        status = library_->GetAttributeNIComplexDoubleArray(instrument, selector_string, attribute_id, attr_val.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        convert_to_grpc(attr_val, response->mutable_attr_val());
        {
          auto shrunk_size = actual_array_size;
          auto current_size = response->mutable_attr_val()->size();
          if (shrunk_size != current_size) {
            response->mutable_attr_val()->DeleteSubrange(shrunk_size, current_size - shrunk_size);
          }
        }
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeNIComplexSingleArray(::grpc::ServerContext* context, const GetAttributeNIComplexSingleArrayRequest* request, GetAttributeNIComplexSingleArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeNIComplexSingleArray(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::vector<NIComplexSingle> attr_val(actual_array_size, NIComplexSingle());
        auto array_size = actual_array_size;
        status = library_->GetAttributeNIComplexSingleArray(instrument, selector_string, attribute_id, attr_val.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        convert_to_grpc(attr_val, response->mutable_attr_val());
        {
          auto shrunk_size = actual_array_size;
          auto current_size = response->mutable_attr_val()->size();
          if (shrunk_size != current_size) {
            response->mutable_attr_val()->DeleteSubrange(shrunk_size, current_size - shrunk_size);
          }
        }
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeString(::grpc::ServerContext* context, const GetAttributeStringRequest* request, GetAttributeStringResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();

      while (true) {
        auto status = library_->GetAttributeString(instrument, selector_string, attribute_id, 0, nullptr);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        int32 array_size = status;

        std::string attr_val;
        if (array_size > 0) {
            attr_val.resize(array_size - 1);
        }
        status = library_->GetAttributeString(instrument, selector_string, attribute_id, array_size, (char*)attr_val.data());
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(array_size)) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        std::string attr_val_utf8;
        convert_to_grpc(attr_val, &attr_val_utf8);
        response->set_attr_val(attr_val_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_attr_val()));
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeU16(::grpc::ServerContext* context, const GetAttributeU16Request* request, GetAttributeU16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      uInt16 attr_val {};
      auto status = library_->GetAttributeU16(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeU32(::grpc::ServerContext* context, const GetAttributeU32Request* request, GetAttributeU32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      uInt32 attr_val {};
      auto status = library_->GetAttributeU32(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeU32Array(::grpc::ServerContext* context, const GetAttributeU32ArrayRequest* request, GetAttributeU32ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeU32Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        uInt32* attr_val = reinterpret_cast<uInt32*>(response->mutable_attr_val()->mutable_data());
        auto array_size = actual_array_size;
        status = library_->GetAttributeU32Array(instrument, selector_string, attribute_id, attr_val, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeU64Array(::grpc::ServerContext* context, const GetAttributeU64ArrayRequest* request, GetAttributeU64ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeU64Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        uInt64* attr_val = reinterpret_cast<uInt64*>(response->mutable_attr_val()->mutable_data());
        auto array_size = actual_array_size;
        status = library_->GetAttributeU64Array(instrument, selector_string, attribute_id, attr_val, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_attr_val()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeU8(::grpc::ServerContext* context, const GetAttributeU8Request* request, GetAttributeU8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      uInt8 attr_val {};
      auto status = library_->GetAttributeU8(instrument, selector_string, attribute_id, &attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_attr_val(attr_val);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetAttributeU8Array(::grpc::ServerContext* context, const GetAttributeU8ArrayRequest* request, GetAttributeU8ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->GetAttributeU8Array(instrument, selector_string, attribute_id, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::string attr_val(actual_array_size, '\0');
        auto array_size = actual_array_size;
        status = library_->GetAttributeU8Array(instrument, selector_string, attribute_id, (uInt8*)attr_val.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_attr_val(attr_val);
        response->mutable_attr_val()->resize(actual_array_size);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetError(::grpc::ServerContext* context, const GetErrorRequest* request, GetErrorResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());

      while (true) {
        auto status = library_->GetError(instrument, nullptr, 0, nullptr);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        int32 error_description_buffer_size = status;

        int32 error_code {};
        std::string error_description;
        if (error_description_buffer_size > 0) {
            error_description.resize(error_description_buffer_size - 1);
        }
        status = library_->GetError(instrument, &error_code, error_description_buffer_size, (char*)error_description.data());
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(error_description_buffer_size)) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_error_code(error_code);
        std::string error_description_utf8;
        convert_to_grpc(error_description, &error_description_utf8);
        response->set_error_description(error_description_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_error_description()));
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::GetErrorString(::grpc::ServerContext* context, const GetErrorStringRequest* request, GetErrorStringResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      int32 error_code = request->error_code();

      while (true) {
        auto status = library_->GetErrorString(instrument, error_code, 0, nullptr);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        int32 error_description_buffer_size = status;

        std::string error_description;
        if (error_description_buffer_size > 0) {
            error_description.resize(error_description_buffer_size - 1);
        }
        status = library_->GetErrorString(instrument, error_code, error_description_buffer_size, (char*)error_description.data());
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer || status > static_cast<decltype(status)>(error_description_buffer_size)) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        std::string error_description_utf8;
        convert_to_grpc(error_description, &error_description_utf8);
        response->set_error_description(error_description_utf8);
        nidevice_grpc::converters::trim_trailing_nulls(*(response->mutable_error_description()));
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::Initialize(::grpc::ServerContext* context, const InitializeRequest* request, InitializeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto resource_name_mbcs = convert_from_grpc<std::string>(request->resource_name());
      char* resource_name = (char*)resource_name_mbcs.c_str();
      auto option_string_mbcs = convert_from_grpc<std::string>(request->option_string());
      char* option_string = (char*)option_string_mbcs.c_str();
      auto initialization_behavior = request->initialization_behavior();

      int32 is_new_session {};
      bool new_session_initialized {};
      auto init_lambda = [&] () {
        niRFmxInstrHandle instrument;
        auto status = library_->Initialize(resource_name, option_string, &instrument, &is_new_session);
        return std::make_tuple(status, instrument);
      };
      std::string grpc_device_session_name = request->session_name();
      // Capture the library shared_ptr by value. Do not capture `this` or any references.
      LibrarySharedPtr library = library_;
      auto cleanup_lambda = [library] (niRFmxInstrHandle id) { library->Close(id, RFMXCDMA2K_VAL_FALSE); };
      int status = session_repository_->add_session(grpc_device_session_name, init_lambda, cleanup_lambda, initialization_behavior, &new_session_initialized);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
      }
      response->set_status(status);
      response->mutable_instrument()->set_name(grpc_device_session_name);
      response->set_is_new_session(is_new_session);
      response->set_new_session_initialized(new_session_initialized);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::InitializeFromNIRFSASession(::grpc::ServerContext* context, const InitializeFromNIRFSASessionRequest* request, InitializeFromNIRFSASessionResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto nirfsa_session_grpc_session = request->nirfsa_session();
      uInt32 nirfsa_session = vi_session_resource_repository_->access_session(nirfsa_session_grpc_session.name());
      auto initialization_behavior = request->initialization_behavior();

      bool new_session_initialized {};
      auto init_lambda = [&] () {
        niRFmxInstrHandle instrument;
        auto status = library_->InitializeFromNIRFSASession(nirfsa_session, &instrument);
        return std::make_tuple(status, instrument);
      };
      std::string grpc_device_session_name = request->session_name();
      // Capture the library shared_ptr by value. Do not capture `this` or any references.
      LibrarySharedPtr library = library_;
      auto cleanup_lambda = [library] (niRFmxInstrHandle id) { library->Close(id, RFMXCDMA2K_VAL_FALSE); };
      int status = session_repository_->add_session(grpc_device_session_name, init_lambda, cleanup_lambda, initialization_behavior, &new_session_initialized);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, 0);
      }
      response->set_status(status);
      response->mutable_instrument()->set_name(grpc_device_session_name);
      response->set_new_session_initialized(new_session_initialized);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::Initiate(::grpc::ServerContext* context, const InitiateRequest* request, InitiateResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto result_name_mbcs = convert_from_grpc<std::string>(request->result_name());
      char* result_name = (char*)result_name_mbcs.c_str();
      auto status = library_->Initiate(instrument, selector_string, result_name);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccCfgSynchronizationModeAndInterval(::grpc::ServerContext* context, const ModAccCfgSynchronizationModeAndIntervalRequest* request, ModAccCfgSynchronizationModeAndIntervalResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 synchronization_mode;
      switch (request->synchronization_mode_enum_case()) {
        case nirfmxcdma2k_grpc::ModAccCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationMode: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode());
          break;
        }
        case nirfmxcdma2k_grpc::ModAccCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationModeRaw: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode_raw());
          break;
        }
        case nirfmxcdma2k_grpc::ModAccCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::SYNCHRONIZATION_MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for synchronization_mode was not specified or out of range");
          break;
        }
      }

      int32 measurement_offset = request->measurement_offset();
      int32 measurement_length = request->measurement_length();
      auto status = library_->ModAccCfgSynchronizationModeAndInterval(instrument, selector_string, synchronization_mode, measurement_offset, measurement_length);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchConstellationTrace(::grpc::ServerContext* context, const ModAccFetchConstellationTraceRequest* request, ModAccFetchConstellationTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchConstellationTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::vector<NIComplexSingle> constellation(actual_array_size, NIComplexSingle());
        auto array_size = actual_array_size;
        status = library_->ModAccFetchConstellationTrace(instrument, selector_string, timeout, constellation.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        convert_to_grpc(constellation, response->mutable_constellation());
        {
          auto shrunk_size = actual_array_size;
          auto current_size = response->mutable_constellation()->size();
          if (shrunk_size != current_size) {
            response->mutable_constellation()->DeleteSubrange(shrunk_size, current_size - shrunk_size);
          }
        }
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchConstellationTraceInterleavedIQ(::grpc::ServerContext* context, const ModAccFetchConstellationTraceInterleavedIQRequest* request, ModAccFetchConstellationTraceInterleavedIQResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchConstellationTraceInterleavedIQ(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_constellation()->Resize(actual_array_size * 2, 0);
        float32* constellation = response->mutable_constellation()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ModAccFetchConstellationTraceInterleavedIQ(instrument, selector_string, timeout, constellation, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_constellation()->Resize(actual_array_size * 2, 0);
        response->set_actual_array_size(actual_array_size * 2);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchConstellationTraceSplit(::grpc::ServerContext* context, const ModAccFetchConstellationTraceSplitRequest* request, ModAccFetchConstellationTraceSplitResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchConstellationTraceSplit(instrument, selector_string, timeout, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_constellation_i()->Resize(actual_array_size, 0);
        float32* constellation_i = response->mutable_constellation_i()->mutable_data();
        response->mutable_constellation_q()->Resize(actual_array_size, 0);
        float32* constellation_q = response->mutable_constellation_q()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ModAccFetchConstellationTraceSplit(instrument, selector_string, timeout, constellation_i, constellation_q, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_constellation_i()->Resize(actual_array_size, 0);
        response->mutable_constellation_q()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchDetectedChannel(::grpc::ServerContext* context, const ModAccFetchDetectedChannelRequest* request, ModAccFetchDetectedChannelResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 detected_walsh_code_length {};
      int32 detected_walsh_code_number {};
      int32 detected_branch {};
      auto status = library_->ModAccFetchDetectedChannel(instrument, selector_string, timeout, &detected_walsh_code_length, &detected_walsh_code_number, &detected_branch);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_detected_walsh_code_length(detected_walsh_code_length);
      response->set_detected_walsh_code_number(detected_walsh_code_number);
      response->set_detected_branch(static_cast<nirfmxcdma2k_grpc::ModAccDetectedBranch>(detected_branch));
      response->set_detected_branch_raw(detected_branch);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchDetectedChannelArray(::grpc::ServerContext* context, const ModAccFetchDetectedChannelArrayRequest* request, ModAccFetchDetectedChannelArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchDetectedChannelArray(instrument, selector_string, timeout, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_detected_walsh_code_length()->Resize(actual_array_size, 0);
        int32* detected_walsh_code_length = reinterpret_cast<int32*>(response->mutable_detected_walsh_code_length()->mutable_data());
        response->mutable_detected_walsh_code_number()->Resize(actual_array_size, 0);
        int32* detected_walsh_code_number = reinterpret_cast<int32*>(response->mutable_detected_walsh_code_number()->mutable_data());
        response->mutable_detected_branch_raw()->Resize(actual_array_size, 0);
        int32* detected_branch = reinterpret_cast<int32*>(response->mutable_detected_branch_raw()->mutable_data());
        auto array_size = actual_array_size;
        status = library_->ModAccFetchDetectedChannelArray(instrument, selector_string, timeout, detected_walsh_code_length, detected_walsh_code_number, detected_branch, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_detected_walsh_code_length()->Resize(actual_array_size, 0);
        response->mutable_detected_walsh_code_number()->Resize(actual_array_size, 0);
        response->mutable_detected_branch()->Clear();
        response->mutable_detected_branch()->Reserve(actual_array_size);
        std::transform(
          response->detected_branch_raw().begin(),
          response->detected_branch_raw().begin() + actual_array_size,
          google::protobuf::RepeatedFieldBackInserter(response->mutable_detected_branch()),
          [&](auto x) {
              return static_cast<nirfmxcdma2k_grpc::ModAccDetectedBranch>(x);
          });
        response->mutable_detected_branch()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchEVM(::grpc::ServerContext* context, const ModAccFetchEVMRequest* request, ModAccFetchEVMResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 rms_evm {};
      float64 peak_evm {};
      float64 rho {};
      float64 frequency_error {};
      float64 chip_rate_error {};
      float64 rms_magnitude_error {};
      float64 rms_phase_error {};
      auto status = library_->ModAccFetchEVM(instrument, selector_string, timeout, &rms_evm, &peak_evm, &rho, &frequency_error, &chip_rate_error, &rms_magnitude_error, &rms_phase_error);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_rms_evm(rms_evm);
      response->set_peak_evm(peak_evm);
      response->set_rho(rho);
      response->set_frequency_error(frequency_error);
      response->set_chip_rate_error(chip_rate_error);
      response->set_rms_magnitude_error(rms_magnitude_error);
      response->set_rms_phase_error(rms_phase_error);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchEVMTrace(::grpc::ServerContext* context, const ModAccFetchEVMTraceRequest* request, ModAccFetchEVMTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchEVMTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_evm()->Resize(actual_array_size, 0);
        float32* evm = response->mutable_evm()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ModAccFetchEVMTrace(instrument, selector_string, timeout, &x0, &dx, evm, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_evm()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchIQImpairments(::grpc::ServerContext* context, const ModAccFetchIQImpairmentsRequest* request, ModAccFetchIQImpairmentsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 iq_origin_offset {};
      float64 iq_gain_imbalance {};
      float64 iq_quadrature_error {};
      auto status = library_->ModAccFetchIQImpairments(instrument, selector_string, timeout, &iq_origin_offset, &iq_gain_imbalance, &iq_quadrature_error);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_iq_origin_offset(iq_origin_offset);
      response->set_iq_gain_imbalance(iq_gain_imbalance);
      response->set_iq_quadrature_error(iq_quadrature_error);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchMagnitudeErrorTrace(::grpc::ServerContext* context, const ModAccFetchMagnitudeErrorTraceRequest* request, ModAccFetchMagnitudeErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchMagnitudeErrorTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_magnitude_error()->Resize(actual_array_size, 0);
        float32* magnitude_error = response->mutable_magnitude_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ModAccFetchMagnitudeErrorTrace(instrument, selector_string, timeout, &x0, &dx, magnitude_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_magnitude_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchNumberOfDetectedChannels(::grpc::ServerContext* context, const ModAccFetchNumberOfDetectedChannelsRequest* request, ModAccFetchNumberOfDetectedChannelsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 number_of_detected_channels {};
      auto status = library_->ModAccFetchNumberOfDetectedChannels(instrument, selector_string, timeout, &number_of_detected_channels);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_number_of_detected_channels(number_of_detected_channels);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchPeakActiveCDE(::grpc::ServerContext* context, const ModAccFetchPeakActiveCDERequest* request, ModAccFetchPeakActiveCDEResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 peak_active_cde {};
      int32 peak_active_cde_walsh_code_length {};
      int32 peak_active_cde_walsh_code_number {};
      int32 peak_active_cde_branch {};
      auto status = library_->ModAccFetchPeakActiveCDE(instrument, selector_string, timeout, &peak_active_cde, &peak_active_cde_walsh_code_length, &peak_active_cde_walsh_code_number, &peak_active_cde_branch);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_peak_active_cde(peak_active_cde);
      response->set_peak_active_cde_walsh_code_length(peak_active_cde_walsh_code_length);
      response->set_peak_active_cde_walsh_code_number(peak_active_cde_walsh_code_number);
      response->set_peak_active_cde_branch(static_cast<nirfmxcdma2k_grpc::ModAccPeakActiveCdeBranch>(peak_active_cde_branch));
      response->set_peak_active_cde_branch_raw(peak_active_cde_branch);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchPeakCDE(::grpc::ServerContext* context, const ModAccFetchPeakCDERequest* request, ModAccFetchPeakCDEResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 peak_cde {};
      int32 peak_cde_walsh_code_number {};
      int32 peak_cde_branch {};
      auto status = library_->ModAccFetchPeakCDE(instrument, selector_string, timeout, &peak_cde, &peak_cde_walsh_code_number, &peak_cde_branch);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_peak_cde(peak_cde);
      response->set_peak_cde_walsh_code_number(peak_cde_walsh_code_number);
      response->set_peak_cde_branch(static_cast<nirfmxcdma2k_grpc::ModAccPeakCdeBranch>(peak_cde_branch));
      response->set_peak_cde_branch_raw(peak_cde_branch);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ModAccFetchPhaseErrorTrace(::grpc::ServerContext* context, const ModAccFetchPhaseErrorTraceRequest* request, ModAccFetchPhaseErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->ModAccFetchPhaseErrorTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_phase_error()->Resize(actual_array_size, 0);
        float32* phase_error = response->mutable_phase_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->ModAccFetchPhaseErrorTrace(instrument, selector_string, timeout, &x0, &dx, phase_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_phase_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::OBWCfgAveraging(::grpc::ServerContext* context, const OBWCfgAveragingRequest* request, OBWCfgAveragingResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 averaging_enabled;
      switch (request->averaging_enabled_enum_case()) {
        case nirfmxcdma2k_grpc::OBWCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabled: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabledRaw: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled_raw());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgAveragingRequest::AveragingEnabledEnumCase::AVERAGING_ENABLED_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_enabled was not specified or out of range");
          break;
        }
      }

      int32 averaging_count = request->averaging_count();
      int32 averaging_type;
      switch (request->averaging_type_enum_case()) {
        case nirfmxcdma2k_grpc::OBWCfgAveragingRequest::AveragingTypeEnumCase::kAveragingType: {
          averaging_type = static_cast<int32>(request->averaging_type());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgAveragingRequest::AveragingTypeEnumCase::kAveragingTypeRaw: {
          averaging_type = static_cast<int32>(request->averaging_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgAveragingRequest::AveragingTypeEnumCase::AVERAGING_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->OBWCfgAveraging(instrument, selector_string, averaging_enabled, averaging_count, averaging_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::OBWCfgRBWFilter(::grpc::ServerContext* context, const OBWCfgRBWFilterRequest* request, OBWCfgRBWFilterResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 rbw_auto;
      switch (request->rbw_auto_enum_case()) {
        case nirfmxcdma2k_grpc::OBWCfgRBWFilterRequest::RbwAutoEnumCase::kRbwAuto: {
          rbw_auto = static_cast<int32>(request->rbw_auto());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgRBWFilterRequest::RbwAutoEnumCase::kRbwAutoRaw: {
          rbw_auto = static_cast<int32>(request->rbw_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgRBWFilterRequest::RbwAutoEnumCase::RBW_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rbw_auto was not specified or out of range");
          break;
        }
      }

      float64 rbw = request->rbw();
      int32 rbw_filter_type;
      switch (request->rbw_filter_type_enum_case()) {
        case nirfmxcdma2k_grpc::OBWCfgRBWFilterRequest::RbwFilterTypeEnumCase::kRbwFilterType: {
          rbw_filter_type = static_cast<int32>(request->rbw_filter_type());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgRBWFilterRequest::RbwFilterTypeEnumCase::kRbwFilterTypeRaw: {
          rbw_filter_type = static_cast<int32>(request->rbw_filter_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgRBWFilterRequest::RbwFilterTypeEnumCase::RBW_FILTER_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for rbw_filter_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->OBWCfgRBWFilter(instrument, selector_string, rbw_auto, rbw, rbw_filter_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::OBWCfgSweepTime(::grpc::ServerContext* context, const OBWCfgSweepTimeRequest* request, OBWCfgSweepTimeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 sweep_time_auto;
      switch (request->sweep_time_auto_enum_case()) {
        case nirfmxcdma2k_grpc::OBWCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAuto: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAutoRaw: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::OBWCfgSweepTimeRequest::SweepTimeAutoEnumCase::SWEEP_TIME_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for sweep_time_auto was not specified or out of range");
          break;
        }
      }

      float64 sweep_time_interval = request->sweep_time_interval();
      auto status = library_->OBWCfgSweepTime(instrument, selector_string, sweep_time_auto, sweep_time_interval);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::OBWFetchMeasurement(::grpc::ServerContext* context, const OBWFetchMeasurementRequest* request, OBWFetchMeasurementResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 occupied_bandwidth {};
      float64 absolute_power {};
      float64 start_frequency {};
      float64 stop_frequency {};
      auto status = library_->OBWFetchMeasurement(instrument, selector_string, timeout, &occupied_bandwidth, &absolute_power, &start_frequency, &stop_frequency);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_occupied_bandwidth(occupied_bandwidth);
      response->set_absolute_power(absolute_power);
      response->set_start_frequency(start_frequency);
      response->set_stop_frequency(stop_frequency);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::OBWFetchSpectrum(::grpc::ServerContext* context, const OBWFetchSpectrumRequest* request, OBWFetchSpectrumResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->OBWFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        float32* spectrum = response->mutable_spectrum()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->OBWFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, spectrum, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMCfgAveraging(::grpc::ServerContext* context, const QEVMCfgAveragingRequest* request, QEVMCfgAveragingResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 averaging_enabled;
      switch (request->averaging_enabled_enum_case()) {
        case nirfmxcdma2k_grpc::QEVMCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabled: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled());
          break;
        }
        case nirfmxcdma2k_grpc::QEVMCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabledRaw: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled_raw());
          break;
        }
        case nirfmxcdma2k_grpc::QEVMCfgAveragingRequest::AveragingEnabledEnumCase::AVERAGING_ENABLED_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_enabled was not specified or out of range");
          break;
        }
      }

      int32 averaging_count = request->averaging_count();
      auto status = library_->QEVMCfgAveraging(instrument, selector_string, averaging_enabled, averaging_count);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMCfgMeasurementLength(::grpc::ServerContext* context, const QEVMCfgMeasurementLengthRequest* request, QEVMCfgMeasurementLengthResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 measurement_length = request->measurement_length();
      auto status = library_->QEVMCfgMeasurementLength(instrument, selector_string, measurement_length);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchConstellationTrace(::grpc::ServerContext* context, const QEVMFetchConstellationTraceRequest* request, QEVMFetchConstellationTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->QEVMFetchConstellationTrace(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        std::vector<NIComplexSingle> constellation(actual_array_size, NIComplexSingle());
        auto array_size = actual_array_size;
        status = library_->QEVMFetchConstellationTrace(instrument, selector_string, timeout, constellation.data(), array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        convert_to_grpc(constellation, response->mutable_constellation());
        {
          auto shrunk_size = actual_array_size;
          auto current_size = response->mutable_constellation()->size();
          if (shrunk_size != current_size) {
            response->mutable_constellation()->DeleteSubrange(shrunk_size, current_size - shrunk_size);
          }
        }
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchConstellationTraceInterleavedIQ(::grpc::ServerContext* context, const QEVMFetchConstellationTraceInterleavedIQRequest* request, QEVMFetchConstellationTraceInterleavedIQResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->QEVMFetchConstellationTraceInterleavedIQ(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_constellation()->Resize(actual_array_size * 2, 0);
        float32* constellation = response->mutable_constellation()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->QEVMFetchConstellationTraceInterleavedIQ(instrument, selector_string, timeout, constellation, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_constellation()->Resize(actual_array_size * 2, 0);
        response->set_actual_array_size(actual_array_size * 2);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchConstellationTraceSplit(::grpc::ServerContext* context, const QEVMFetchConstellationTraceSplitRequest* request, QEVMFetchConstellationTraceSplitResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->QEVMFetchConstellationTraceSplit(instrument, selector_string, timeout, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_constellation_i()->Resize(actual_array_size, 0);
        float32* constellation_i = response->mutable_constellation_i()->mutable_data();
        response->mutable_constellation_q()->Resize(actual_array_size, 0);
        float32* constellation_q = response->mutable_constellation_q()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->QEVMFetchConstellationTraceSplit(instrument, selector_string, timeout, constellation_i, constellation_q, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_constellation_i()->Resize(actual_array_size, 0);
        response->mutable_constellation_q()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchEVM(::grpc::ServerContext* context, const QEVMFetchEVMRequest* request, QEVMFetchEVMResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 mean_rms_evm {};
      float64 maximum_peak_evm {};
      float64 mean_frequency_error {};
      float64 mean_magnitude_error {};
      float64 mean_phase_error {};
      float64 mean_chip_rate_error {};
      auto status = library_->QEVMFetchEVM(instrument, selector_string, timeout, &mean_rms_evm, &maximum_peak_evm, &mean_frequency_error, &mean_magnitude_error, &mean_phase_error, &mean_chip_rate_error);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_mean_rms_evm(mean_rms_evm);
      response->set_maximum_peak_evm(maximum_peak_evm);
      response->set_mean_frequency_error(mean_frequency_error);
      response->set_mean_magnitude_error(mean_magnitude_error);
      response->set_mean_phase_error(mean_phase_error);
      response->set_mean_chip_rate_error(mean_chip_rate_error);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchEVMTrace(::grpc::ServerContext* context, const QEVMFetchEVMTraceRequest* request, QEVMFetchEVMTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->QEVMFetchEVMTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_evm()->Resize(actual_array_size, 0);
        float32* evm = response->mutable_evm()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->QEVMFetchEVMTrace(instrument, selector_string, timeout, &x0, &dx, evm, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_evm()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchIQImpairments(::grpc::ServerContext* context, const QEVMFetchIQImpairmentsRequest* request, QEVMFetchIQImpairmentsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 mean_iq_origin_offset {};
      float64 mean_iq_gain_imbalance {};
      float64 mean_iq_quadrature_error {};
      float64 maximum_iq_origin_offset {};
      float64 maximum_iq_gain_imbalance {};
      float64 maximum_iq_quadrature_error {};
      auto status = library_->QEVMFetchIQImpairments(instrument, selector_string, timeout, &mean_iq_origin_offset, &mean_iq_gain_imbalance, &mean_iq_quadrature_error, &maximum_iq_origin_offset, &maximum_iq_gain_imbalance, &maximum_iq_quadrature_error);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_mean_iq_origin_offset(mean_iq_origin_offset);
      response->set_mean_iq_gain_imbalance(mean_iq_gain_imbalance);
      response->set_mean_iq_quadrature_error(mean_iq_quadrature_error);
      response->set_maximum_iq_origin_offset(maximum_iq_origin_offset);
      response->set_maximum_iq_gain_imbalance(maximum_iq_gain_imbalance);
      response->set_maximum_iq_quadrature_error(maximum_iq_quadrature_error);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchMagnitudeErrorTrace(::grpc::ServerContext* context, const QEVMFetchMagnitudeErrorTraceRequest* request, QEVMFetchMagnitudeErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->QEVMFetchMagnitudeErrorTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_magnitude_error()->Resize(actual_array_size, 0);
        float32* magnitude_error = response->mutable_magnitude_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->QEVMFetchMagnitudeErrorTrace(instrument, selector_string, timeout, &x0, &dx, magnitude_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_magnitude_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::QEVMFetchPhaseErrorTrace(::grpc::ServerContext* context, const QEVMFetchPhaseErrorTraceRequest* request, QEVMFetchPhaseErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->QEVMFetchPhaseErrorTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_phase_error()->Resize(actual_array_size, 0);
        float32* phase_error = response->mutable_phase_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->QEVMFetchPhaseErrorTrace(instrument, selector_string, timeout, &x0, &dx, phase_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_phase_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ResetAttribute(::grpc::ServerContext* context, const ResetAttributeRequest* request, ResetAttributeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto status = library_->ResetAttribute(instrument, selector_string, attribute_id);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::ResetToDefault(::grpc::ServerContext* context, const ResetToDefaultRequest* request, ResetToDefaultResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      auto status = library_->ResetToDefault(instrument, selector_string);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMCfgAveraging(::grpc::ServerContext* context, const SEMCfgAveragingRequest* request, SEMCfgAveragingResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 averaging_enabled;
      switch (request->averaging_enabled_enum_case()) {
        case nirfmxcdma2k_grpc::SEMCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabled: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled());
          break;
        }
        case nirfmxcdma2k_grpc::SEMCfgAveragingRequest::AveragingEnabledEnumCase::kAveragingEnabledRaw: {
          averaging_enabled = static_cast<int32>(request->averaging_enabled_raw());
          break;
        }
        case nirfmxcdma2k_grpc::SEMCfgAveragingRequest::AveragingEnabledEnumCase::AVERAGING_ENABLED_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_enabled was not specified or out of range");
          break;
        }
      }

      int32 averaging_count = request->averaging_count();
      int32 averaging_type;
      switch (request->averaging_type_enum_case()) {
        case nirfmxcdma2k_grpc::SEMCfgAveragingRequest::AveragingTypeEnumCase::kAveragingType: {
          averaging_type = static_cast<int32>(request->averaging_type());
          break;
        }
        case nirfmxcdma2k_grpc::SEMCfgAveragingRequest::AveragingTypeEnumCase::kAveragingTypeRaw: {
          averaging_type = static_cast<int32>(request->averaging_type_raw());
          break;
        }
        case nirfmxcdma2k_grpc::SEMCfgAveragingRequest::AveragingTypeEnumCase::AVERAGING_TYPE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for averaging_type was not specified or out of range");
          break;
        }
      }

      auto status = library_->SEMCfgAveraging(instrument, selector_string, averaging_enabled, averaging_count, averaging_type);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMCfgSweepTime(::grpc::ServerContext* context, const SEMCfgSweepTimeRequest* request, SEMCfgSweepTimeResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 sweep_time_auto;
      switch (request->sweep_time_auto_enum_case()) {
        case nirfmxcdma2k_grpc::SEMCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAuto: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto());
          break;
        }
        case nirfmxcdma2k_grpc::SEMCfgSweepTimeRequest::SweepTimeAutoEnumCase::kSweepTimeAutoRaw: {
          sweep_time_auto = static_cast<int32>(request->sweep_time_auto_raw());
          break;
        }
        case nirfmxcdma2k_grpc::SEMCfgSweepTimeRequest::SweepTimeAutoEnumCase::SWEEP_TIME_AUTO_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for sweep_time_auto was not specified or out of range");
          break;
        }
      }

      float64 sweep_time_interval = request->sweep_time_interval();
      auto status = library_->SEMCfgSweepTime(instrument, selector_string, sweep_time_auto, sweep_time_interval);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchCarrierAbsoluteIntegratedPower(::grpc::ServerContext* context, const SEMFetchCarrierAbsoluteIntegratedPowerRequest* request, SEMFetchCarrierAbsoluteIntegratedPowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 carrier_absolute_integrated_power {};
      auto status = library_->SEMFetchCarrierAbsoluteIntegratedPower(instrument, selector_string, timeout, &carrier_absolute_integrated_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_carrier_absolute_integrated_power(carrier_absolute_integrated_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchLowerOffsetMargin(::grpc::ServerContext* context, const SEMFetchLowerOffsetMarginRequest* request, SEMFetchLowerOffsetMarginResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 measurement_status {};
      float64 margin {};
      float64 margin_frequency {};
      float64 margin_absolute_power {};
      float64 margin_relative_power {};
      auto status = library_->SEMFetchLowerOffsetMargin(instrument, selector_string, timeout, &measurement_status, &margin, &margin_frequency, &margin_absolute_power, &margin_relative_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_measurement_status(static_cast<nirfmxcdma2k_grpc::SemLowerOffsetMeasurementStatus>(measurement_status));
      response->set_measurement_status_raw(measurement_status);
      response->set_margin(margin);
      response->set_margin_frequency(margin_frequency);
      response->set_margin_absolute_power(margin_absolute_power);
      response->set_margin_relative_power(margin_relative_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchLowerOffsetMarginArray(::grpc::ServerContext* context, const SEMFetchLowerOffsetMarginArrayRequest* request, SEMFetchLowerOffsetMarginArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SEMFetchLowerOffsetMarginArray(instrument, selector_string, timeout, nullptr, nullptr, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_measurement_status_raw()->Resize(actual_array_size, 0);
        int32* measurement_status = reinterpret_cast<int32*>(response->mutable_measurement_status_raw()->mutable_data());
        response->mutable_margin()->Resize(actual_array_size, 0);
        float64* margin = response->mutable_margin()->mutable_data();
        response->mutable_margin_frequency()->Resize(actual_array_size, 0);
        float64* margin_frequency = response->mutable_margin_frequency()->mutable_data();
        response->mutable_margin_absolute_power()->Resize(actual_array_size, 0);
        float64* margin_absolute_power = response->mutable_margin_absolute_power()->mutable_data();
        response->mutable_margin_relative_power()->Resize(actual_array_size, 0);
        float64* margin_relative_power = response->mutable_margin_relative_power()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SEMFetchLowerOffsetMarginArray(instrument, selector_string, timeout, measurement_status, margin, margin_frequency, margin_absolute_power, margin_relative_power, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_measurement_status()->Clear();
        response->mutable_measurement_status()->Reserve(actual_array_size);
        std::transform(
          response->measurement_status_raw().begin(),
          response->measurement_status_raw().begin() + actual_array_size,
          google::protobuf::RepeatedFieldBackInserter(response->mutable_measurement_status()),
          [&](auto x) {
              return static_cast<nirfmxcdma2k_grpc::SemLowerOffsetMeasurementStatus>(x);
          });
        response->mutable_measurement_status()->Resize(actual_array_size, 0);
        response->mutable_margin()->Resize(actual_array_size, 0);
        response->mutable_margin_frequency()->Resize(actual_array_size, 0);
        response->mutable_margin_absolute_power()->Resize(actual_array_size, 0);
        response->mutable_margin_relative_power()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchLowerOffsetPower(::grpc::ServerContext* context, const SEMFetchLowerOffsetPowerRequest* request, SEMFetchLowerOffsetPowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 absolute_integrated_power {};
      float64 relative_integrated_power {};
      float64 absolute_peak_power {};
      float64 peak_frequency {};
      float64 relative_peak_power {};
      auto status = library_->SEMFetchLowerOffsetPower(instrument, selector_string, timeout, &absolute_integrated_power, &relative_integrated_power, &absolute_peak_power, &peak_frequency, &relative_peak_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_absolute_integrated_power(absolute_integrated_power);
      response->set_relative_integrated_power(relative_integrated_power);
      response->set_absolute_peak_power(absolute_peak_power);
      response->set_peak_frequency(peak_frequency);
      response->set_relative_peak_power(relative_peak_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchLowerOffsetPowerArray(::grpc::ServerContext* context, const SEMFetchLowerOffsetPowerArrayRequest* request, SEMFetchLowerOffsetPowerArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SEMFetchLowerOffsetPowerArray(instrument, selector_string, timeout, nullptr, nullptr, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_absolute_integrated_power()->Resize(actual_array_size, 0);
        float64* absolute_integrated_power = response->mutable_absolute_integrated_power()->mutable_data();
        response->mutable_relative_integrated_power()->Resize(actual_array_size, 0);
        float64* relative_integrated_power = response->mutable_relative_integrated_power()->mutable_data();
        response->mutable_absolute_peak_power()->Resize(actual_array_size, 0);
        float64* absolute_peak_power = response->mutable_absolute_peak_power()->mutable_data();
        response->mutable_peak_frequency()->Resize(actual_array_size, 0);
        float64* peak_frequency = response->mutable_peak_frequency()->mutable_data();
        response->mutable_relative_peak_power()->Resize(actual_array_size, 0);
        float64* relative_peak_power = response->mutable_relative_peak_power()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SEMFetchLowerOffsetPowerArray(instrument, selector_string, timeout, absolute_integrated_power, relative_integrated_power, absolute_peak_power, peak_frequency, relative_peak_power, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_absolute_integrated_power()->Resize(actual_array_size, 0);
        response->mutable_relative_integrated_power()->Resize(actual_array_size, 0);
        response->mutable_absolute_peak_power()->Resize(actual_array_size, 0);
        response->mutable_peak_frequency()->Resize(actual_array_size, 0);
        response->mutable_relative_peak_power()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchMeasurementStatus(::grpc::ServerContext* context, const SEMFetchMeasurementStatusRequest* request, SEMFetchMeasurementStatusResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 measurement_status {};
      auto status = library_->SEMFetchMeasurementStatus(instrument, selector_string, timeout, &measurement_status);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_measurement_status(static_cast<nirfmxcdma2k_grpc::SemMeasurementStatus>(measurement_status));
      response->set_measurement_status_raw(measurement_status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchSpectrum(::grpc::ServerContext* context, const SEMFetchSpectrumRequest* request, SEMFetchSpectrumResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SEMFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        float32* spectrum = response->mutable_spectrum()->mutable_data();
        response->mutable_relative_mask()->Resize(actual_array_size, 0);
        float32* relative_mask = response->mutable_relative_mask()->mutable_data();
        response->mutable_absolute_mask()->Resize(actual_array_size, 0);
        float32* absolute_mask = response->mutable_absolute_mask()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SEMFetchSpectrum(instrument, selector_string, timeout, &x0, &dx, spectrum, relative_mask, absolute_mask, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_spectrum()->Resize(actual_array_size, 0);
        response->mutable_relative_mask()->Resize(actual_array_size, 0);
        response->mutable_absolute_mask()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchUpperOffsetMargin(::grpc::ServerContext* context, const SEMFetchUpperOffsetMarginRequest* request, SEMFetchUpperOffsetMarginResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 measurement_status {};
      float64 margin {};
      float64 margin_frequency {};
      float64 margin_absolute_power {};
      float64 margin_relative_power {};
      auto status = library_->SEMFetchUpperOffsetMargin(instrument, selector_string, timeout, &measurement_status, &margin, &margin_frequency, &margin_absolute_power, &margin_relative_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_measurement_status(static_cast<nirfmxcdma2k_grpc::SemUpperOffsetMeasurementStatus>(measurement_status));
      response->set_measurement_status_raw(measurement_status);
      response->set_margin(margin);
      response->set_margin_frequency(margin_frequency);
      response->set_margin_absolute_power(margin_absolute_power);
      response->set_margin_relative_power(margin_relative_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchUpperOffsetMarginArray(::grpc::ServerContext* context, const SEMFetchUpperOffsetMarginArrayRequest* request, SEMFetchUpperOffsetMarginArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SEMFetchUpperOffsetMarginArray(instrument, selector_string, timeout, nullptr, nullptr, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_measurement_status_raw()->Resize(actual_array_size, 0);
        int32* measurement_status = reinterpret_cast<int32*>(response->mutable_measurement_status_raw()->mutable_data());
        response->mutable_margin()->Resize(actual_array_size, 0);
        float64* margin = response->mutable_margin()->mutable_data();
        response->mutable_margin_frequency()->Resize(actual_array_size, 0);
        float64* margin_frequency = response->mutable_margin_frequency()->mutable_data();
        response->mutable_margin_absolute_power()->Resize(actual_array_size, 0);
        float64* margin_absolute_power = response->mutable_margin_absolute_power()->mutable_data();
        response->mutable_margin_relative_power()->Resize(actual_array_size, 0);
        float64* margin_relative_power = response->mutable_margin_relative_power()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SEMFetchUpperOffsetMarginArray(instrument, selector_string, timeout, measurement_status, margin, margin_frequency, margin_absolute_power, margin_relative_power, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_measurement_status()->Clear();
        response->mutable_measurement_status()->Reserve(actual_array_size);
        std::transform(
          response->measurement_status_raw().begin(),
          response->measurement_status_raw().begin() + actual_array_size,
          google::protobuf::RepeatedFieldBackInserter(response->mutable_measurement_status()),
          [&](auto x) {
              return static_cast<nirfmxcdma2k_grpc::SemUpperOffsetMeasurementStatus>(x);
          });
        response->mutable_measurement_status()->Resize(actual_array_size, 0);
        response->mutable_margin()->Resize(actual_array_size, 0);
        response->mutable_margin_frequency()->Resize(actual_array_size, 0);
        response->mutable_margin_absolute_power()->Resize(actual_array_size, 0);
        response->mutable_margin_relative_power()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchUpperOffsetPower(::grpc::ServerContext* context, const SEMFetchUpperOffsetPowerRequest* request, SEMFetchUpperOffsetPowerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 absolute_integrated_power {};
      float64 relative_integrated_power {};
      float64 absolute_peak_power {};
      float64 peak_frequency {};
      float64 relative_peak_power {};
      auto status = library_->SEMFetchUpperOffsetPower(instrument, selector_string, timeout, &absolute_integrated_power, &relative_integrated_power, &absolute_peak_power, &peak_frequency, &relative_peak_power);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_absolute_integrated_power(absolute_integrated_power);
      response->set_relative_integrated_power(relative_integrated_power);
      response->set_absolute_peak_power(absolute_peak_power);
      response->set_peak_frequency(peak_frequency);
      response->set_relative_peak_power(relative_peak_power);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SEMFetchUpperOffsetPowerArray(::grpc::ServerContext* context, const SEMFetchUpperOffsetPowerArrayRequest* request, SEMFetchUpperOffsetPowerArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SEMFetchUpperOffsetPowerArray(instrument, selector_string, timeout, nullptr, nullptr, nullptr, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_absolute_integrated_power()->Resize(actual_array_size, 0);
        float64* absolute_integrated_power = response->mutable_absolute_integrated_power()->mutable_data();
        response->mutable_relative_integrated_power()->Resize(actual_array_size, 0);
        float64* relative_integrated_power = response->mutable_relative_integrated_power()->mutable_data();
        response->mutable_absolute_peak_power()->Resize(actual_array_size, 0);
        float64* absolute_peak_power = response->mutable_absolute_peak_power()->mutable_data();
        response->mutable_peak_frequency()->Resize(actual_array_size, 0);
        float64* peak_frequency = response->mutable_peak_frequency()->mutable_data();
        response->mutable_relative_peak_power()->Resize(actual_array_size, 0);
        float64* relative_peak_power = response->mutable_relative_peak_power()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SEMFetchUpperOffsetPowerArray(instrument, selector_string, timeout, absolute_integrated_power, relative_integrated_power, absolute_peak_power, peak_frequency, relative_peak_power, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_absolute_integrated_power()->Resize(actual_array_size, 0);
        response->mutable_relative_integrated_power()->Resize(actual_array_size, 0);
        response->mutable_absolute_peak_power()->Resize(actual_array_size, 0);
        response->mutable_peak_frequency()->Resize(actual_array_size, 0);
        response->mutable_relative_peak_power()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SelectMeasurements(::grpc::ServerContext* context, const SelectMeasurementsRequest* request, SelectMeasurementsResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      const auto measurements = nidevice_grpc::converters::convert_bitfield_as_enum_array_input(
        request->measurements_array(),
        request->measurements_raw());

      int32 enable_all_traces = request->enable_all_traces();
      auto status = library_->SelectMeasurements(instrument, selector_string, measurements, enable_all_traces);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SendSoftwareEdgeTrigger(::grpc::ServerContext* context, const SendSoftwareEdgeTriggerRequest* request, SendSoftwareEdgeTriggerResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto status = library_->SendSoftwareEdgeTrigger(instrument);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeF32(::grpc::ServerContext* context, const SetAttributeF32Request* request, SetAttributeF32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      float32 attr_val = request->attr_val();
      auto status = library_->SetAttributeF32(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeF32Array(::grpc::ServerContext* context, const SetAttributeF32ArrayRequest* request, SetAttributeF32ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = const_cast<float32*>(request->attr_val().data());
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeF32Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeF64(::grpc::ServerContext* context, const SetAttributeF64Request* request, SetAttributeF64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      float64 attr_val = request->attr_val();
      auto status = library_->SetAttributeF64(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeF64Array(::grpc::ServerContext* context, const SetAttributeF64ArrayRequest* request, SetAttributeF64ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = const_cast<float64*>(request->attr_val().data());
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeF64Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI16(::grpc::ServerContext* context, const SetAttributeI16Request* request, SetAttributeI16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val_raw = request->attr_val();
      if (attr_val_raw < std::numeric_limits<int16>::min() || attr_val_raw > std::numeric_limits<int16>::max()) {
          std::string message("value ");
          message.append(std::to_string(attr_val_raw));
          message.append(" doesn't fit in datatype ");
          message.append("int16");
          throw nidevice_grpc::ValueOutOfRangeException(message);
      }
      auto attr_val = static_cast<int16>(attr_val_raw);

      auto status = library_->SetAttributeI16(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI32(::grpc::ServerContext* context, const SetAttributeI32Request* request, SetAttributeI32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int32 attr_val;
      switch (request->attr_val_enum_case()) {
        case nirfmxcdma2k_grpc::SetAttributeI32Request::AttrValEnumCase::kAttrVal: {
          attr_val = static_cast<int32>(request->attr_val());
          break;
        }
        case nirfmxcdma2k_grpc::SetAttributeI32Request::AttrValEnumCase::kAttrValRaw: {
          attr_val = static_cast<int32>(request->attr_val_raw());
          break;
        }
        case nirfmxcdma2k_grpc::SetAttributeI32Request::AttrValEnumCase::ATTR_VAL_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for attr_val was not specified or out of range");
          break;
        }
      }

      auto status = library_->SetAttributeI32(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI32Array(::grpc::ServerContext* context, const SetAttributeI32ArrayRequest* request, SetAttributeI32ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val_vector = std::vector<int32>();
      attr_val_vector.reserve(request->attr_val().size());
      std::transform(
        request->attr_val().begin(),
        request->attr_val().end(),
        std::back_inserter(attr_val_vector),
        [](auto x) { return x; });
      auto attr_val = attr_val_vector.data();

      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeI32Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI64(::grpc::ServerContext* context, const SetAttributeI64Request* request, SetAttributeI64Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      int64 attr_val = request->attr_val();
      auto status = library_->SetAttributeI64(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI64Array(::grpc::ServerContext* context, const SetAttributeI64ArrayRequest* request, SetAttributeI64ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = const_cast<int64*>(reinterpret_cast<const int64*>(request->attr_val().data()));
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeI64Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI8(::grpc::ServerContext* context, const SetAttributeI8Request* request, SetAttributeI8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val_raw = request->attr_val();
      if (attr_val_raw < std::numeric_limits<int8>::min() || attr_val_raw > std::numeric_limits<int8>::max()) {
          std::string message("value ");
          message.append(std::to_string(attr_val_raw));
          message.append(" doesn't fit in datatype ");
          message.append("int8");
          throw nidevice_grpc::ValueOutOfRangeException(message);
      }
      auto attr_val = static_cast<int8>(attr_val_raw);

      auto status = library_->SetAttributeI8(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeI8Array(::grpc::ServerContext* context, const SetAttributeI8ArrayRequest* request, SetAttributeI8ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val_raw = request->attr_val();
      auto attr_val = std::vector<int8>();
      attr_val.reserve(attr_val_raw.size());
      std::transform(
        attr_val_raw.begin(),
        attr_val_raw.end(),
        std::back_inserter(attr_val),
        [](auto x) {
              if (x < std::numeric_limits<int8>::min() || x > std::numeric_limits<int8>::max()) {
                  std::string message("value ");
                  message.append(std::to_string(x));
                  message.append(" doesn't fit in datatype ");
                  message.append("int8");
                  throw nidevice_grpc::ValueOutOfRangeException(message);
              }
              return static_cast<int8>(x);
        });

      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeI8Array(instrument, selector_string, attribute_id, attr_val.data(), array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeNIComplexDoubleArray(::grpc::ServerContext* context, const SetAttributeNIComplexDoubleArrayRequest* request, SetAttributeNIComplexDoubleArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = convert_from_grpc<NIComplexDouble>(request->attr_val());
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeNIComplexDoubleArray(instrument, selector_string, attribute_id, attr_val.data(), array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeNIComplexSingleArray(::grpc::ServerContext* context, const SetAttributeNIComplexSingleArrayRequest* request, SetAttributeNIComplexSingleArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = convert_from_grpc<NIComplexSingle>(request->attr_val());
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeNIComplexSingleArray(instrument, selector_string, attribute_id, attr_val.data(), array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeString(::grpc::ServerContext* context, const SetAttributeStringRequest* request, SetAttributeStringResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      char* attr_val;
      std::string attr_val_buffer;
      switch (request->attr_val_enum_case()) {
        case nirfmxcdma2k_grpc::SetAttributeStringRequest::AttrValEnumCase::kAttrValMapped: {
          auto attr_val_imap_it = nirfmxcdma2kstringattributevaluesmapped_input_map_.find(request->attr_val_mapped());
          if (attr_val_imap_it == nirfmxcdma2kstringattributevaluesmapped_input_map_.end()) {
            return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for attr_val_mapped was not specified or out of range.");
          }
          attr_val = const_cast<char*>((attr_val_imap_it->second).c_str());
          break;
        }
        case nirfmxcdma2k_grpc::SetAttributeStringRequest::AttrValEnumCase::kAttrValRaw: {
          attr_val_buffer = convert_from_grpc<std::string>(request->attr_val_raw());
          attr_val = const_cast<char*>(attr_val_buffer.c_str());
          break;
        }
        case nirfmxcdma2k_grpc::SetAttributeStringRequest::AttrValEnumCase::ATTR_VAL_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for attr_val was not specified or out of range");
          break;
        }
      }

      auto status = library_->SetAttributeString(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeU16(::grpc::ServerContext* context, const SetAttributeU16Request* request, SetAttributeU16Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val_raw = request->attr_val();
      if (attr_val_raw < std::numeric_limits<uInt16>::min() || attr_val_raw > std::numeric_limits<uInt16>::max()) {
          std::string message("value ");
          message.append(std::to_string(attr_val_raw));
          message.append(" doesn't fit in datatype ");
          message.append("uInt16");
          throw nidevice_grpc::ValueOutOfRangeException(message);
      }
      auto attr_val = static_cast<uInt16>(attr_val_raw);

      auto status = library_->SetAttributeU16(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeU32(::grpc::ServerContext* context, const SetAttributeU32Request* request, SetAttributeU32Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      uInt32 attr_val = request->attr_val();
      auto status = library_->SetAttributeU32(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeU32Array(::grpc::ServerContext* context, const SetAttributeU32ArrayRequest* request, SetAttributeU32ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = const_cast<uInt32*>(reinterpret_cast<const uInt32*>(request->attr_val().data()));
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeU32Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeU64Array(::grpc::ServerContext* context, const SetAttributeU64ArrayRequest* request, SetAttributeU64ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      auto attr_val = const_cast<uInt64*>(reinterpret_cast<const uInt64*>(request->attr_val().data()));
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeU64Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeU8(::grpc::ServerContext* context, const SetAttributeU8Request* request, SetAttributeU8Response* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      uInt8 attr_val = request->attr_val();
      auto status = library_->SetAttributeU8(instrument, selector_string, attribute_id, attr_val);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SetAttributeU8Array(::grpc::ServerContext* context, const SetAttributeU8ArrayRequest* request, SetAttributeU8ArrayResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 attribute_id = request->attribute_id();
      uInt8* attr_val = (uInt8*)request->attr_val().c_str();
      auto array_size_raw = request->attr_val().size();
      int32 array_size = nidevice_grpc::converters::convert_size<int32>(array_size_raw, "array_size");
      auto status = library_->SetAttributeU8Array(instrument, selector_string, attribute_id, attr_val, array_size);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPhaseCfgSynchronizationModeAndInterval(::grpc::ServerContext* context, const SlotPhaseCfgSynchronizationModeAndIntervalRequest* request, SlotPhaseCfgSynchronizationModeAndIntervalResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 synchronization_mode;
      switch (request->synchronization_mode_enum_case()) {
        case nirfmxcdma2k_grpc::SlotPhaseCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationMode: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode());
          break;
        }
        case nirfmxcdma2k_grpc::SlotPhaseCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationModeRaw: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode_raw());
          break;
        }
        case nirfmxcdma2k_grpc::SlotPhaseCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::SYNCHRONIZATION_MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for synchronization_mode was not specified or out of range");
          break;
        }
      }

      int32 measurement_offset = request->measurement_offset();
      int32 measurement_length = request->measurement_length();
      auto status = library_->SlotPhaseCfgSynchronizationModeAndInterval(instrument, selector_string, synchronization_mode, measurement_offset, measurement_length);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPhaseFetchChipPhaseErrorLinearFitTrace(::grpc::ServerContext* context, const SlotPhaseFetchChipPhaseErrorLinearFitTraceRequest* request, SlotPhaseFetchChipPhaseErrorLinearFitTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SlotPhaseFetchChipPhaseErrorLinearFitTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_chip_phase_error_linear_fit()->Resize(actual_array_size, 0);
        float32* chip_phase_error_linear_fit = response->mutable_chip_phase_error_linear_fit()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SlotPhaseFetchChipPhaseErrorLinearFitTrace(instrument, selector_string, timeout, &x0, &dx, chip_phase_error_linear_fit, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_chip_phase_error_linear_fit()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPhaseFetchChipPhaseErrorTrace(::grpc::ServerContext* context, const SlotPhaseFetchChipPhaseErrorTraceRequest* request, SlotPhaseFetchChipPhaseErrorTraceResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 x0 {};
      float64 dx {};
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SlotPhaseFetchChipPhaseErrorTrace(instrument, selector_string, timeout, &x0, &dx, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_chip_phase_error()->Resize(actual_array_size, 0);
        float32* chip_phase_error = response->mutable_chip_phase_error()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SlotPhaseFetchChipPhaseErrorTrace(instrument, selector_string, timeout, &x0, &dx, chip_phase_error, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->set_x0(x0);
        response->set_dx(dx);
        response->mutable_chip_phase_error()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPhaseFetchMaximumPhaseDiscontinuity(::grpc::ServerContext* context, const SlotPhaseFetchMaximumPhaseDiscontinuityRequest* request, SlotPhaseFetchMaximumPhaseDiscontinuityResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      float64 maximum_phase_discontinuity {};
      auto status = library_->SlotPhaseFetchMaximumPhaseDiscontinuity(instrument, selector_string, timeout, &maximum_phase_discontinuity);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      response->set_maximum_phase_discontinuity(maximum_phase_discontinuity);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPhaseFetchPhaseDiscontinuities(::grpc::ServerContext* context, const SlotPhaseFetchPhaseDiscontinuitiesRequest* request, SlotPhaseFetchPhaseDiscontinuitiesResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SlotPhaseFetchPhaseDiscontinuities(instrument, selector_string, timeout, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_slot_phase_discontinuity()->Resize(actual_array_size, 0);
        float64* slot_phase_discontinuity = response->mutable_slot_phase_discontinuity()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SlotPhaseFetchPhaseDiscontinuities(instrument, selector_string, timeout, slot_phase_discontinuity, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_slot_phase_discontinuity()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPowerCfgSynchronizationModeAndInterval(::grpc::ServerContext* context, const SlotPowerCfgSynchronizationModeAndIntervalRequest* request, SlotPowerCfgSynchronizationModeAndIntervalResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      int32 synchronization_mode;
      switch (request->synchronization_mode_enum_case()) {
        case nirfmxcdma2k_grpc::SlotPowerCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationMode: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode());
          break;
        }
        case nirfmxcdma2k_grpc::SlotPowerCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::kSynchronizationModeRaw: {
          synchronization_mode = static_cast<int32>(request->synchronization_mode_raw());
          break;
        }
        case nirfmxcdma2k_grpc::SlotPowerCfgSynchronizationModeAndIntervalRequest::SynchronizationModeEnumCase::SYNCHRONIZATION_MODE_ENUM_NOT_SET: {
          return ::grpc::Status(::grpc::INVALID_ARGUMENT, "The value for synchronization_mode was not specified or out of range");
          break;
        }
      }

      int32 measurement_offset = request->measurement_offset();
      int32 measurement_length = request->measurement_length();
      auto status = library_->SlotPowerCfgSynchronizationModeAndInterval(instrument, selector_string, synchronization_mode, measurement_offset, measurement_length);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::SlotPowerFetchPowers(::grpc::ServerContext* context, const SlotPowerFetchPowersRequest* request, SlotPowerFetchPowersResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      int32 actual_array_size {};
      while (true) {
        auto status = library_->SlotPowerFetchPowers(instrument, selector_string, timeout, nullptr, nullptr, 0, &actual_array_size);
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->mutable_slot_power()->Resize(actual_array_size, 0);
        float64* slot_power = response->mutable_slot_power()->mutable_data();
        response->mutable_slot_power_delta()->Resize(actual_array_size, 0);
        float64* slot_power_delta = response->mutable_slot_power_delta()->mutable_data();
        auto array_size = actual_array_size;
        status = library_->SlotPowerFetchPowers(instrument, selector_string, timeout, slot_power, slot_power_delta, array_size, &actual_array_size);
        if (status == kErrorReadBufferTooSmall || status == kWarningCAPIStringTruncatedToFitBuffer) {
          // buffer is now too small, try again
          continue;
        }
        if (!status_ok(status)) {
          return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
        }
        response->set_status(status);
        response->mutable_slot_power()->Resize(actual_array_size, 0);
        response->mutable_slot_power_delta()->Resize(actual_array_size, 0);
        response->set_actual_array_size(actual_array_size);
        return ::grpc::Status::OK;
      }
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::WaitForAcquisitionComplete(::grpc::ServerContext* context, const WaitForAcquisitionCompleteRequest* request, WaitForAcquisitionCompleteResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      float64 timeout = request->timeout();
      auto status = library_->WaitForAcquisitionComplete(instrument, timeout);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }

  //---------------------------------------------------------------------
  //---------------------------------------------------------------------
  ::grpc::Status NiRFmxCDMA2kService::WaitForMeasurementComplete(::grpc::ServerContext* context, const WaitForMeasurementCompleteRequest* request, WaitForMeasurementCompleteResponse* response)
  {
    if (context->IsCancelled()) {
      return ::grpc::Status::CANCELLED;
    }
    try {
      auto instrument_grpc_session = request->instrument();
      niRFmxInstrHandle instrument = session_repository_->access_session(instrument_grpc_session.name());
      auto selector_string_mbcs = convert_from_grpc<std::string>(request->selector_string());
      char* selector_string = (char*)selector_string_mbcs.c_str();
      float64 timeout = request->timeout();
      auto status = library_->WaitForMeasurementComplete(instrument, selector_string, timeout);
      if (!status_ok(status)) {
        return ConvertApiErrorStatusForNiRFmxInstrHandle(context, status, instrument);
      }
      response->set_status(status);
      return ::grpc::Status::OK;
    }
    catch (nidevice_grpc::NonDriverException& ex) {
      return ex.GetStatus();
    }
  }


  NiRFmxCDMA2kFeatureToggles::NiRFmxCDMA2kFeatureToggles(
    const nidevice_grpc::FeatureToggles& feature_toggles)
    : is_enabled(
        feature_toggles.is_feature_enabled("nirfmxcdma2k", CodeReadiness::kRelease))
  {
  }
} // namespace nirfmxcdma2k_grpc
````
